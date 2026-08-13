from __future__ import annotations

import ast
import csv
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("deployment_realization_audit", ROOT / "run_audit.py")
assert SPEC is not None and SPEC.loader is not None
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class PhaseZeroContractTests(unittest.TestCase):
    def test_checked_result_is_fail_closed(self) -> None:
        result = json.loads((ROOT / "result.json").read_text(encoding="utf-8"))
        self.assertEqual(result["STOP"], "BLOCKED_MISSING_INPUT")
        self.assertEqual(result["D_deployment"], "UNIDENTIFIED_INPUT_BLOCKED")
        self.assertIsNone(result["metrics"])
        self.assertFalse(result["authority"]["hidden_or_public_test_information_used"])
        self.assertFalse(result["authority"]["model_search_reopened"])
        self.assertFalse(result["authority"]["calibration_selection_reopened"])
        self.assertFalse(result["authority"]["submission_02_authorized"])
        self.assertEqual(
            set(result["missing_required_objects"]),
            set(audit.REQUIRED_PRIMARY_OBJECTS),
        )
        self.assertTrue(
            all(value == "NOT_RUN_BLOCKED_MISSING_INPUT" for value in result["phases"].values())
        )
        not_reached = {
            key for key, value in result["tests"].items() if value == "NOT_REACHED"
        }
        self.assertEqual(
            not_reached,
            {
                "direct_vs_packaged_probability_equivalence",
                "direct_vs_packaged_raw_score_equivalence",
                "primary_paired_row_alignment",
                "score_extraction_consistency",
            },
        )

    def test_manifest_parent_and_missing_object_identities_are_frozen(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["frozen_parent"]["commit"], audit.PARENT_COMMIT)
        self.assertEqual(manifest["frozen_parent"]["pull_request"], 47)
        self.assertEqual(
            set(manifest["required_missing_objects"]),
            set(audit.REQUIRED_PRIMARY_OBJECTS),
        )
        self.assertFalse(manifest["authority"]["raw_competition_data_committed"])
        self.assertFalse(manifest["authority"]["hidden_or_public_test_information_used"])

    def test_missing_primary_objects_force_blocked_result(self) -> None:
        checks = {
            object_id: audit.check_object(object_id, None, expected_hash)
            for object_id, expected_hash in audit.REQUIRED_PRIMARY_OBJECTS.items()
        }
        result = audit.build_blocked_result(
            checks,
            training_alignment={
                "response_id_order_matches": True,
                "response_ids_unique": True,
                "rows": 35072,
                "session_ids": set(),
                "sessions": 22821,
            },
            transcript_coverage={
                "combined_session_coverage_matches": True,
                "part1_csv_members": 11400,
                "part2_csv_members": 11421,
                "sessions": 22821,
            },
        )
        self.assertEqual(result["STOP"], audit.STOP)
        self.assertEqual(result["D_deployment"], audit.D_DEPLOYMENT)
        self.assertIsNone(result["metrics"])
        self.assertEqual(result["phase0"]["paired_score_row_identity"], "NOT_CONSTITUTABLE")

    def test_phase_zero_program_refuses_to_open_downstream_when_objects_exist(self) -> None:
        checks = {
            object_id: audit.ObjectCheck(
                object_id,
                f"{object_id}.artifact",
                "PRESENT_HASH_VALID",
                expected_hash,
                expected_hash or hashlib.sha256(object_id.encode()).hexdigest(),
            )
            for object_id, expected_hash in audit.REQUIRED_PRIMARY_OBJECTS.items()
        }
        with self.assertRaisesRegex(RuntimeError, "must stop without opening"):
            audit.build_blocked_result(
                checks,
                training_alignment={"session_ids": set()},
                transcript_coverage={},
            )

    def test_training_alignment_requires_exact_unique_row_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            features = root / "features.csv"
            labels = root / "labels.csv"
            self._write_csv(
                features,
                ["response_id", "session_id"],
                [("r1", "s1"), ("r2", "s2")],
            )
            self._write_csv(labels, ["response_id", "is_correct"], [("r2", 0), ("r1", 1)])
            with self.assertRaisesRegex(ValueError, "identity/order differ"):
                audit.validate_training_alignment(features, labels)

            self._write_csv(labels, ["response_id", "is_correct"], [("r1", 0), ("r1", 1)])
            with self.assertRaisesRegex(ValueError, "duplicate response_id"):
                audit.validate_training_alignment(features, labels)

    def test_hash_and_submission_member_checks_are_exact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "artifact.bin"
            artifact.write_bytes(b"frozen")
            expected = hashlib.sha256(b"frozen").hexdigest()
            self.assertEqual(audit.sha256_file(artifact), expected)
            check = audit.check_object("artifact", artifact, expected)
            self.assertEqual(check.status, "PRESENT_HASH_VALID")
            bad = audit.check_object("artifact", artifact, "0" * 64)
            self.assertEqual(bad.status, "HASH_MISMATCH")
            unconstituted = audit.check_object("artifact", artifact, None)
            self.assertEqual(unconstituted.status, "PRESENT_IDENTITY_UNCONSTITUTED")

            package = root / "submission.zip"
            with zipfile.ZipFile(package, "w") as archive:
                for name in audit.EXPECTED_SUBMISSION_MEMBERS:
                    archive.writestr(name, b"wrong")
            with self.assertRaisesRegex(ValueError, "member hash mismatch"):
                audit.validate_submission_members(package)

    def test_public_and_hidden_test_paths_are_rejected(self) -> None:
        forbidden = (
            "hidden_test/features.csv",
            "public-test/scores.csv",
            "leaderboard/export.csv",
            "data/submission_format.csv",
            "data/test_features.csv",
            "data/test_transcripts/s1.csv",
        )
        for value in forbidden:
            with self.subTest(path=value):
                with self.assertRaisesRegex(ValueError, "forbidden"):
                    audit.ensure_allowlisted_path(Path(value))

    def test_missing_required_training_input_returns_blocked_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = Namespace(
                repository_root=root,
                features=root / audit.EXPECTED_INPUTS["features"][0],
                labels=root / audit.EXPECTED_INPUTS["labels"][0],
                transcripts_part1=root / audit.EXPECTED_INPUTS["transcripts_part1"][0],
                transcripts_part2=root / audit.EXPECTED_INPUTS["transcripts_part2"][0],
                submission_zip=root / audit.EXPECTED_INPUTS["submission_zip"][0],
                glove_archive=root / audit.EXPECTED_INPUTS["glove_archive"][0],
                research_oof=None,
                outer_folds=None,
                deployment_crossfit_scores=None,
                deployment_fit_implementation=None,
                deployment_platt_geometry=None,
                output=None,
            )
            result = audit.run(args)
        self.assertEqual(result["STOP"], "BLOCKED_MISSING_INPUT")
        self.assertEqual(result["D_deployment"], "UNIDENTIFIED_INPUT_BLOCKED")
        self.assertEqual(result["phase0"]["training_input_integrity"], "FAIL")
        self.assertIsNone(result["metrics"])
        self.assertTrue(
            any(item.startswith("required_input:") for item in result["missing_required_objects"])
        )

    def test_runner_contains_no_fitting_or_scoring_dependency(self) -> None:
        source = (ROOT / "run_audit.py").read_text(encoding="utf-8")
        parsed = ast.parse(source)
        imported_roots = set()
        for node in ast.walk(parsed):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])
        self.assertTrue(imported_roots.isdisjoint({"numpy", "pandas", "sklearn", "scipy"}))
        self.assertNotIn(".fit(", source)
        self.assertNotIn("predict_proba", source)
        self.assertNotIn("decision_function", source)

    @staticmethod
    def _write_csv(path: Path, fields: list[str], rows: list[tuple[object, ...]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(fields)
            writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
