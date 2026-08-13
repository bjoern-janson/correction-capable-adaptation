from __future__ import annotations

import csv
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
import build_submission
import runtime_main
import verify_submission


TRANSCRIPT_HEADER = [
    "session_id",
    "utterance_id",
    "role",
    "content",
    "timestamp",
]


def row(session_id: str, utterance_id: int, role: str, content: str) -> dict[str, str]:
    return {
        "session_id": session_id,
        "utterance_id": str(utterance_id),
        "role": role,
        "content": content,
        "timestamp": str(utterance_id),
    }


def write_transcript(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRANSCRIPT_HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def simple_state(base_rate: float = 0.7) -> dict[str, np.ndarray]:
    return {
        "coef": np.zeros(3, dtype=np.float64),
        "eligible_base_rate": np.asarray([base_rate], dtype=np.float64),
        "feature_median": np.asarray([100.0, 0.0, 0.0], dtype=np.float64),
        "intercept": np.asarray([0.0], dtype=np.float64),
        "min_student_words": np.asarray([100], dtype=np.int64),
        "scaler_mean": np.asarray([100.0, 0.0, 0.0], dtype=np.float64),
        "scaler_scale": np.ones(3, dtype=np.float64),
    }


class M0ControlTests(unittest.TestCase):
    def test_exact_student_only_feature_definition(self) -> None:
        rows = [
            row("s", 0, "tutor", "999 ignored words"),
            row("s", 1, "student", "can't solve 12 plus 3"),
            row("s", 2, "student", "plain words"),
        ]
        value = runtime_main.session_features_from_rows(rows)
        # can't, solve, 12, plus, 3, plain, words
        np.testing.assert_allclose(value, [7.0, 1.0 / 7.0, 3.0 / 7.0])

    def test_zero_student_words_produces_nan_features(self) -> None:
        value = runtime_main.session_features_from_rows(
            [row("s", 0, "tutor", "123 tutor only")]
        )
        self.assertTrue(np.isnan(value).all())

    def test_n_turns_is_not_a_predictive_feature(self) -> None:
        student = row("s", 0, "student", "one 2")
        base = runtime_main.session_features_from_rows([student])
        expanded = runtime_main.session_features_from_rows(
            [
                row("s", 1, "tutor", "extra"),
                row("s", 2, "background", "extra"),
                student,
            ]
        )
        np.testing.assert_array_equal(base, expanded)
        self.assertEqual(runtime_main.FEATURE_COLUMNS, [
            "n_student_words",
            "numeric_turns_per_word",
            "digit_chars_per_word",
        ])

    def test_quiet_fallback_and_eligible_score(self) -> None:
        probabilities = runtime_main.predict_feature_matrix(
            np.asarray([[np.nan, np.nan, np.nan], [100.0, 0.0, 0.0]]),
            simple_state(),
        )
        np.testing.assert_allclose(probabilities, [0.7, 0.5], atol=0, rtol=0)

    def test_stable_sigmoid(self) -> None:
        values = runtime_main.sigmoid(np.asarray([-1000.0, 0.0, 1000.0]))
        self.assertTrue(np.isfinite(values).all())
        self.assertEqual(values[1], 0.5)
        self.assertEqual(values[2], 1.0)
        self.assertEqual(values[0], 0.0)

    def test_deterministic_npz(self) -> None:
        first = build_submission.deterministic_npz_bytes(simple_state())
        second = build_submission.deterministic_npz_bytes(simple_state())
        self.assertEqual(first, second)
        with np.load(io.BytesIO(first), allow_pickle=False) as restored:
            np.testing.assert_array_equal(restored["coef"], np.zeros(3))

    def test_deterministic_zip_member_order_and_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.zip"
            second = Path(tmp) / "second.zip"
            members = {"main.py": b"x\n", "assets/a": b"a"}
            build_submission.write_deterministic_zip(first, members)
            build_submission.write_deterministic_zip(second, members)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), ["assets/a", "main.py"])

    def test_runtime_source_is_offline_and_has_no_sklearn(self) -> None:
        source = (SCRIPT_DIR / "runtime_main.py").read_text(encoding="utf-8")
        verify_submission.verify_offline_source(source)
        self.assertNotIn("sklearn", source)

    def test_output_contract_requires_exact_order(self) -> None:
        valid = pd.DataFrame({"response_id": ["b", "a"], "probability": [0.2, 0.8]})
        verify_submission.verify_output_contract(valid, ["b", "a"])
        with self.assertRaisesRegex(RuntimeError, "identity/order"):
            verify_submission.verify_output_contract(valid, ["a", "b"])

    def test_nonfinite_direct_predictions_fail_closed(self) -> None:
        direct = pd.DataFrame(
            {"response_id": ["r1"], "probability": [float("nan")]}
        )
        with self.assertRaisesRegex(RuntimeError, "non-finite direct probability"):
            verify_submission.verify_direct_predictions(direct)

    def test_raw_response_order_gate_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            features = Path(tmp) / "features.csv"
            labels = Path(tmp) / "labels.csv"
            pd.DataFrame({"response_id": ["a"], "session_id": ["s"]}).to_csv(
                features, index=False
            )
            pd.DataFrame({"response_id": ["a"], "is_correct": [1]}).to_csv(
                labels, index=False
            )
            with self.assertRaisesRegex(RuntimeError, "row count"):
                build_submission.verify_raw_response_order(features, labels)

    def test_full_fit_is_bound_to_phase0_session_features(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "session_features.csv"
            path.write_bytes(b"session_id,n_student_words\ns1,100\n")
            digest = build_submission.sha256_file(path)
            record = {"identity": {"session_features_sha256": digest}}
            self.assertEqual(
                build_submission.verify_phase0_linked_session_features(record, path),
                digest,
            )
            path.write_bytes(b"session_id,n_student_words\ns1,101\n")
            with self.assertRaisesRegex(
                RuntimeError, "session-feature artifact identity mismatch"
            ):
                build_submission.verify_phase0_linked_session_features(record, path)

    def test_nonfinite_phase0_metric_fails_closed(self) -> None:
        record = {
            "status": "DIAGNOSED_PASS",
            "reference_reproduction": {
                "base_log_loss": float("nan"),
                "model_log_loss": build_submission.EXPECTED_PHASE0["model_log_loss"],
                "auc": build_submission.EXPECTED_PHASE0["reference_auc"],
                "coefficients": {
                    "n_student_words": build_submission.EXPECTED_PHASE0[
                        "n_student_words_coef"
                    ],
                    "numeric_turns_per_word": build_submission.EXPECTED_PHASE0[
                        "numeric_turns_per_word_coef"
                    ],
                    "digit_chars_per_word": build_submission.EXPECTED_PHASE0[
                        "digit_chars_per_word_coef"
                    ],
                },
                "reproduced": True,
            },
            "canonical_oof": {
                "pooled_log_loss": build_submission.EXPECTED_PHASE0[
                    "pooled_log_loss"
                ],
                "pooled_auc": build_submission.EXPECTED_PHASE0["pooled_auc"],
                "calibration": {
                    "brier_score": build_submission.EXPECTED_PHASE0["brier_score"],
                    "ece_10_equal_width": build_submission.EXPECTED_PHASE0[
                        "ece_10_equal_width"
                    ],
                },
            },
            "identity": {
                "dataset_index_sha256": build_submission.EXPECTED_INDEX_SHA256,
                "fold_artifact_sha256": build_submission.EXPECTED_FOLD_SHA256,
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "phase0.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "non-finite Phase-0"):
                build_submission.verify_phase0(path)

    def test_runtime_normal_path_preserves_schema_order_and_quiet_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "package"
            data = root / "data"
            transcripts = data / "test_transcripts"
            assets = root / "assets"
            transcripts.mkdir(parents=True)
            assets.mkdir()
            (root / "main.py").write_bytes(
                build_submission.normalized_source_bytes(SCRIPT_DIR / "runtime_main.py")
            )
            (assets / "m0_model.npz").write_bytes(
                build_submission.deterministic_npz_bytes(simple_state())
            )
            pd.DataFrame(
                {"response_id": ["quiet", "eligible"], "probability": [0.0, 0.0]}
            ).to_csv(data / "submission_format.csv", index=False)
            pd.DataFrame(
                {
                    "response_id": ["eligible", "quiet"],
                    "session_id": ["e", "q"],
                    "learning_objective": ["unused", "unused"],
                }
            ).to_csv(data / "test_features.csv", index=False)
            write_transcript(
                transcripts / "e.csv",
                [row("e", 0, "student", " ".join(["word"] * 100))],
            )
            write_transcript(
                transcripts / "q.csv", [row("q", 0, "tutor", "no student words")]
            )
            foreign = Path(tmp) / "foreign"
            foreign.mkdir()
            subprocess.run(
                [sys.executable, str(root / "main.py")],
                cwd=foreign,
                env=os.environ.copy(),
                check=True,
                capture_output=True,
                text=True,
            )
            output = pd.read_csv(root / "submission.csv")
            self.assertEqual(output["response_id"].tolist(), ["quiet", "eligible"])
            np.testing.assert_allclose(output["probability"], [0.7, 0.5])

    def test_archive_verification_rejects_extra_members(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.zip"
            build_submission.write_deterministic_zip(path, {"unexpected": b"x"})
            manifest = {
                "package": {
                    "sha256": build_submission.sha256_file(path),
                    "member_sha256": {
                        "unexpected": build_submission.sha256_bytes(b"x")
                    },
                }
            }
            with self.assertRaisesRegex(RuntimeError, "member set"):
                verify_submission.verify_archive(path, manifest)

    def test_transcript_archive_identity_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "part1.zip"
            second = Path(tmp) / "part2.zip"
            first.write_bytes(b"not the frozen archive")
            second.write_bytes(b"not the frozen archive")
            with self.assertRaisesRegex(RuntimeError, "transcript ZIP identity"):
                verify_submission.verify_transcript_archive_identities(
                    [first, second]
                )

    def test_ready_provenance_rejects_wrong_repository_base(self) -> None:
        manifest = {
            "schema_version": 1,
            "submission_id": "S2_M0_CONTROL",
            "status": "BUILT_PENDING_VERIFICATION",
            "repo_base_sha": "wrong",
            "historical_m0_pr": 24,
            "historical_m0_head": verify_submission.EXPECTED_HISTORICAL_M0_HEAD,
            "authority": verify_submission.INITIAL_AUTHORITY,
        }
        with self.assertRaisesRegex(RuntimeError, "repository base mismatch"):
            verify_submission.verify_manifest_preconditions(
                Path("unreached.zip"), manifest
            )


if __name__ == "__main__":
    unittest.main()
