from __future__ import annotations

import csv
import importlib.util
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import StratifiedGroupKFold


SCRIPT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRIPT_DIR.parents[3]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_submission
import runtime_main
import verify_submission


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HISTORICAL_M0 = load_module(
    REPO_ROOT / "external_tests" / "trace_the_ace" / "baselines" / "m0" / "train.py",
    "submission03_test_historical_m0",
)
HISTORICAL_M1_PRIME = load_module(
    REPO_ROOT
    / "external_tests"
    / "trace_the_ace"
    / "baselines"
    / "m1_prime"
    / "train.py",
    "submission03_test_historical_m1_prime",
)


def row(
    session_id: str,
    utterance_id: int,
    role: str,
    content: str,
    timestamp: str = "",
) -> dict[str, str]:
    return {
        "session_id": session_id,
        "utterance_id": str(utterance_id),
        "role": role,
        "content": content,
        "timestamp": timestamp,
    }


def write_transcript(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=runtime_main.TRANSCRIPT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def simple_state() -> dict[str, np.ndarray]:
    text_coef = np.zeros(runtime_main.N_HASH_FEATURES, dtype=np.float32)
    text_coef[3] = 0.25
    return {
        "text_coef": text_coef,
        "structural_coef": np.asarray([0.2, -0.1, 0.3, -0.4], dtype=np.float32),
        "base_intercept": np.asarray([0.15], dtype=np.float32),
        "structural_medians": np.asarray([2.0, 5.0, 0.1, 0.2]),
        "scaler_mean": np.asarray([2.0, 5.0, 0.1, 0.2]),
        "scaler_scale": np.asarray([1.0, 2.0, 0.5, 0.25]),
        "platt_slope": np.asarray([0.75]),
        "platt_intercept": np.asarray([-0.05]),
    }


class Submission03M1CalControlTests(unittest.TestCase):
    def test_transcript_serialization_matches_historical_helper(self) -> None:
        rows = [
            row("s", 9, "background", "  context\t with   spaces "),
            row("s", 1, "student", "I see 12 and 3."),
            row("s", 4, "tutor", ""),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "s.csv"
            write_transcript(path, rows)
            packaged_text, _ = runtime_main.transcript_blocks(path)
            historical_text = HISTORICAL_M1_PRIME.serialize_transcript(
                path, runtime_main.ROLE_MARKERS
            )
        self.assertEqual(packaged_text, historical_text)
        self.assertEqual(
            packaged_text,
            "__ROLE_BACKGROUND__ context with spaces\n"
            "__ROLE_STUDENT__ I see 12 and 3.\n"
            "__ROLE_TUTOR__ ",
        )

    def test_transcript_row_order_is_not_utterance_id_order(self) -> None:
        text, _ = runtime_main.transcript_blocks_from_rows(
            [row("s", 8, "student", "first"), row("s", 1, "tutor", "second")]
        )
        self.assertEqual(
            text, "__ROLE_STUDENT__ first\n__ROLE_TUTOR__ second"
        )

    def test_unknown_role_fails_closed(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "unexpected transcript role"):
            runtime_main.transcript_blocks_from_rows([row("s", 1, "system", "x")])

    def test_hashing_vectorizer_is_exact_historical_configuration(self) -> None:
        texts = [
            "__ROLE_STUDENT__ Alpha 12\n__ROLE_TUTOR__ beta",
            "punctuation, whitespace and TWO words",
            "",
        ]
        expected = HashingVectorizer(
            analyzer="word",
            ngram_range=(1, 2),
            n_features=262_144,
            alternate_sign=False,
            binary=False,
            norm="l2",
            lowercase=True,
            token_pattern=r"(?u)\b\w+\b",
            dtype=np.float32,
        ).transform(texts).tocsr()
        actual = runtime_main.make_vectorizer().transform(texts).tocsr()
        np.testing.assert_array_equal(actual.indptr, expected.indptr)
        np.testing.assert_array_equal(actual.indices, expected.indices)
        np.testing.assert_array_equal(actual.data, expected.data)
        self.assertEqual(actual.dtype, np.float32)

    def test_four_ordinary_features_match_historical_m0(self) -> None:
        rows = [
            row("s", 1, "tutor", "Tutor has 999"),
            row("s", 2, "student", "I've got 12 apples"),
            row("s", 3, "background", "8"),
            row("s", 4, "student", "three"),
        ]
        _, actual = runtime_main.transcript_blocks_from_rows(rows)
        _, n_turns, n_words, numeric_ratio, digit_ratio = (
            HISTORICAL_M0.session_feature_from_rows(
                "s", rows, runtime_main.WORD_RE, runtime_main.DIGIT_RE
            )
        )
        np.testing.assert_allclose(
            actual,
            [n_turns, n_words, numeric_ratio, digit_ratio],
            rtol=0,
            atol=0,
        )

    def test_zero_student_words_keeps_turn_count_and_three_nans(self) -> None:
        _, values = runtime_main.transcript_blocks_from_rows(
            [row("s", 1, "tutor", "1"), row("s", 2, "background", "2")]
        )
        self.assertEqual(values[0], 2.0)
        self.assertTrue(np.isnan(values[1:]).all())

    def test_stored_state_matches_sparse_linear_and_platt_calculation(self) -> None:
        state = simple_state()
        text = sparse.csr_matrix(
            (
                np.asarray([0.5, 1.0], dtype=np.float32),
                (np.asarray([0, 1]), np.asarray([3, 9])),
            ),
            shape=(2, runtime_main.N_HASH_FEATURES),
            dtype=np.float32,
        )
        ordinary = np.asarray(
            [[2.0, 7.0, 0.1, 0.2], [3.0, np.nan, np.nan, np.nan]]
        )
        raw, calibrated, probability = runtime_main.predict_blocks(
            text, ordinary, state
        )
        imputed = ordinary.copy()
        missing = np.where(np.isnan(imputed))
        imputed[missing] = state["structural_medians"][missing[1]]
        standardized = (
            (imputed - state["scaler_mean"]) / state["scaler_scale"]
        ).astype(np.float32)
        design = sparse.hstack(
            [text, sparse.csr_matrix(standardized)], format="csr", dtype=np.float32
        )
        coefficient = np.concatenate(
            [state["text_coef"], state["structural_coef"]]
        ).reshape(1, -1)
        expected_raw = np.asarray(
            design @ coefficient.T + state["base_intercept"]
        ).reshape(-1)
        expected_calibrated = (
            state["platt_slope"][0] * expected_raw + state["platt_intercept"][0]
        )
        np.testing.assert_array_equal(raw, expected_raw)
        np.testing.assert_array_equal(calibrated, expected_calibrated)
        np.testing.assert_array_equal(
            probability, runtime_main.stable_sigmoid(expected_calibrated)
        )

    def test_stable_sigmoid_is_finite_at_extremes(self) -> None:
        values = runtime_main.stable_sigmoid(np.asarray([-1000.0, 0.0, 1000.0]))
        np.testing.assert_array_equal(np.isfinite(values), [True, True, True])
        np.testing.assert_allclose(values, [0.0, 0.5, 1.0], rtol=0, atol=0)

    def test_state_validation_rejects_nonpositive_platt_slope(self) -> None:
        state = simple_state()
        state["platt_slope"] = np.asarray([0.0])
        with self.assertRaisesRegex(RuntimeError, "Platt slope"):
            runtime_main.validate_state(state)

    def test_deterministic_npz_and_exact_keys(self) -> None:
        first = build_submission.deterministic_npz_bytes(simple_state())
        second = build_submission.deterministic_npz_bytes(simple_state())
        self.assertEqual(first, second)
        with np.load(io.BytesIO(first), allow_pickle=False) as state:
            self.assertEqual(set(state.files), runtime_main.MODEL_STATE_KEYS)

    def test_deterministic_zip_member_order_and_bytes(self) -> None:
        members = {
            "main.py": b"print('x')\n",
            "assets/m1_cal_model.npz": b"model",
            "assets/model_manifest.json": b"{}\n",
        }
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first.zip"
            second = Path(temporary) / "second.zip"
            build_submission.write_deterministic_zip(first, members)
            build_submission.write_deterministic_zip(second, members)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), sorted(members))

    def test_grouped_crossfit_is_complete_deterministic_and_session_disjoint(self) -> None:
        groups = np.repeat([f"s{i:02d}" for i in range(20)], 2)
        y = np.tile([0, 1], 20)
        def assignments() -> np.ndarray:
            result = np.full(len(y), -1, dtype=np.int8)
            splitter = StratifiedGroupKFold(
                n_splits=5, shuffle=True, random_state=1703
            )
            for fold, (train, validation) in enumerate(
                splitter.split(np.zeros(len(y)), y, groups=groups)
            ):
                self.assertFalse(set(groups[train]) & set(groups[validation]))
                result[validation] = fold
            return result
        first = assignments()
        second = assignments()
        self.assertTrue(np.all(first >= 0))
        np.testing.assert_array_equal(first, second)

    def test_output_contract_requires_exact_order_and_finite_range(self) -> None:
        valid = pd.DataFrame(
            {"response_id": ["b", "a"], "probability": [0.2, 0.8]}
        )
        np.testing.assert_array_equal(
            verify_submission.verify_output_contract(valid, ["b", "a"]), [0.2, 0.8]
        )
        with self.assertRaisesRegex(RuntimeError, "response order"):
            verify_submission.verify_output_contract(valid, ["a", "b"])
        invalid = valid.copy()
        invalid.loc[0, "probability"] = np.nan
        with self.assertRaisesRegex(RuntimeError, "invalid probability"):
            verify_submission.verify_output_contract(invalid, ["b", "a"])

    def test_offline_check_allows_sklearn_but_rejects_network_import(self) -> None:
        verify_submission.verify_offline_source(
            "from sklearn.feature_extraction.text import HashingVectorizer\n"
        )
        with self.assertRaisesRegex(RuntimeError, "network/process import"):
            verify_submission.verify_offline_source("import socket\n")

    def test_runtime_normal_path_preserves_order_and_ignores_objective(self) -> None:
        old_root, old_data, old_assets = (
            runtime_main.ROOT,
            runtime_main.DATA,
            runtime_main.ASSETS,
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            data = root / "data"
            assets = root / "assets"
            transcripts = data / "test_transcripts"
            transcripts.mkdir(parents=True)
            assets.mkdir()
            write_transcript(
                transcripts / "s1.csv",
                [row("s1", 1, "student", "one 2")],
            )
            write_transcript(
                transcripts / "s2.csv",
                [row("s2", 1, "tutor", "hello"), row("s2", 2, "student", "three")],
            )
            pd.DataFrame(
                {"response_id": ["r2", "r1"], "probability": [0.0, 0.0]}
            ).to_csv(data / "submission_format.csv", index=False)
            features = pd.DataFrame(
                {
                    "response_id": ["r1", "r2"],
                    "session_id": ["s1", "s2"],
                    "learning_objective": ["secret A", "secret B"],
                }
            )
            features.to_csv(data / "test_features.csv", index=False)
            (assets / "m1_cal_model.npz").write_bytes(
                build_submission.deterministic_npz_bytes(simple_state())
            )
            (assets / "model_manifest.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "submission_id": runtime_main.SUBMISSION_ID,
                        "objective_information_present": False,
                    }
                ),
                encoding="utf-8",
            )
            runtime_main.ROOT, runtime_main.DATA, runtime_main.ASSETS = root, data, assets
            try:
                runtime_main.main()
                first = (root / "submission.csv").read_bytes()
                features["learning_objective"] = ["changed", "completely changed"]
                features.to_csv(data / "test_features.csv", index=False)
                runtime_main.main()
                second = (root / "submission.csv").read_bytes()
            finally:
                runtime_main.ROOT, runtime_main.DATA, runtime_main.ASSETS = (
                    old_root,
                    old_data,
                    old_assets,
                )
        self.assertEqual(first, second)
        output = pd.read_csv(io.BytesIO(first), dtype={"response_id": str})
        self.assertEqual(output["response_id"].tolist(), ["r2", "r1"])

    def test_archive_rejects_extra_member(self) -> None:
        members = {
            "main.py": b"print('x')\n",
            "assets/m1_cal_model.npz": b"x",
            "assets/model_manifest.json": b"{}",
            "extra.txt": b"x",
        }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / build_submission.PACKAGE_FILENAME
            build_submission.write_deterministic_zip(path, members)
            manifest = {
                "package": {
                    "filename": build_submission.PACKAGE_FILENAME,
                    "sha256": build_submission.sha256_file(path),
                    "byte_size": path.stat().st_size,
                    "member_sha256": {
                        key: build_submission.sha256_bytes(value)
                        for key, value in members.items()
                    },
                }
            }
            with self.assertRaisesRegex(RuntimeError, "exact package member set"):
                verify_submission.verify_archive(path, manifest)

    def test_extracted_transcript_bytes_must_match_frozen_archives(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            roots = [root / "part1", root / "part2"]
            archives = [root / "part1.zip", root / "part2.zip"]
            for index, (directory, archive_path) in enumerate(zip(roots, archives)):
                directory.mkdir()
                payload = f"session_id,utterance_id,role,content,timestamp\ns{index},1,student,x,\n".encode()
                (directory / f"s{index}.csv").write_bytes(payload)
                with zipfile.ZipFile(archive_path, "w") as archive:
                    archive.writestr(f"nested/s{index}.csv", payload)
            build_submission.verify_transcript_root_equivalence(
                archives, roots, expected_counts=(1, 1)
            )
            (roots[1] / "s1.csv").write_bytes(b"changed")
            with self.assertRaisesRegex(RuntimeError, "byte mismatch"):
                build_submission.verify_transcript_root_equivalence(
                    archives, roots, expected_counts=(1, 1)
                )


if __name__ == "__main__":
    unittest.main()
