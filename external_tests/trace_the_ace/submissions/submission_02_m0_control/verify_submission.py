"""Verify Submission 02 direct/package and offline runtime equivalence."""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Iterable, Mapping

import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import runtime_main  # noqa: E402


EXPECTED_MEMBERS = {
    "main.py",
    "assets/m0_model.npz",
    "assets/model_manifest.json",
}
EXPECTED_TRANSCRIPT_ARCHIVE_SHA256 = (
    "f8172da9547286f7bd09967571c56626f63e39fb6e24ffcdf475071db57836b7",
    "22ff3c12b599ec82489d9cb546cc2dd2322a8e77dc812ea15352f4830f24cd82",
)
EXPECTED_REPO_BASE_SHA = "4d02c557e234772ed28319fd4cf67098341318fd"
EXPECTED_HISTORICAL_M0_HEAD = "feffb83ce92d4e4688b982be536e81cf026d3068"
EXPECTED_M0_TRAIN_SHA256 = "5c36a4dfaf528fac3e86face05dda13eecebbaeaf9b2ebdc6e9bc80e50009e57"
EXPECTED_M0_CONFIG_SHA256 = "b6431c9e7cacbcdb265ed319f4a15f6e32d5a267051a0065f0fc5bf703a152f6"
EXPECTED_INPUT_SHA256 = {
    "train_features": "71bea3abb76a1cff5e1eaa75b9cbcfaf26d0419f6274b83a199ed520047a5063",
    "train_labels": "d98ee4389e5cde3f66d6d15b7b574261024a80e405958eca333d3c1921fd65b9",
    "train_transcripts_part1": EXPECTED_TRANSCRIPT_ARCHIVE_SHA256[0],
    "train_transcripts_part2": EXPECTED_TRANSCRIPT_ARCHIVE_SHA256[1],
    "submission_01_zip": "48d4d2f1db873e77a5c185cce6649d1425090ad710767b7541eb225035c93aec",
    "canonical_index": "296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60",
    "regenerated_folds": "014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6",
}
EXPECTED_SUBMISSION_01_MEMBERS = {
    "main.py": "28c7f515e6a388a03b4eadca0b083fb3577bd05c8d530341116a065ada30941c",
    "assets/model.npz": "a5af72f06930ac2a5c43a69d2c5a0b8ffc1765631b18e55afa7dd91cbf120742",
    "assets/glove_filtered.npz": "2af970dfabbcb70fa8247d646532e1b420afa09f1d02fe545fca317d6bf3c17b",
    "assets/model_manifest.json": "5c555adcb7295bc538802d473c6945dc3c3b6f4196dedccb93c8ad995ccffee2",
}
EXPECTED_PHASE0 = {
    "base_log_loss": 0.6088918065840663,
    "model_log_loss": 0.6053677970854194,
    "auc": 0.5473456079616892,
    "n_student_words": 0.06836157563364859,
    "numeric_turns_per_word": -0.21051638172143497,
    "digit_chars_per_word": 0.07569770194075158,
    "pooled_log_loss": 0.6045154928170339,
    "pooled_auc": 0.5566948897220998,
    "brier_score": 0.207221464432313,
    "ece_10_equal_width": 0.004379974720982257,
}
EXPECTED_FEATURE_DEFINITION = {
    "eligibility": "n_student_words >= 100",
    "features": [
        "n_student_words",
        "numeric_turns_per_word",
        "digit_chars_per_word",
    ],
    "definitions": {
        "n_student_words": (
            "count of word_regex matches over all student utterances in the session"
        ),
        "numeric_turns_per_word": (
            "number of student turns containing at least one digit / n_student_words"
        ),
        "digit_chars_per_word": (
            "total digit characters in student utterances / n_student_words"
        ),
    },
    "word_regex": r"[a-z0-9]+(?:'[a-z]+)?",
    "digit_regex": r"\d",
    "student_utterances_only": True,
    "zero_word_ratios": "NaN",
    "preprocessing": [
        "eligible-training-response median imputation",
        "eligible-training-response StandardScaler",
    ],
    "quiet_prediction": "eligible full-training response base rate",
}
INITIAL_AUTHORITY = {
    "engineering_control_prepared": False,
    "competition_submission_executed": False,
    "cca_authority_changed": False,
    "research_diagnosis_changed": False,
    "submission_03_authorized": False,
}
FINAL_AUTHORITY = {
    **INITIAL_AUTHORITY,
    "engineering_control_prepared": True,
}
ALLOWED_RUNTIME_IMPORTS = {
    "__future__",
    "csv",
    "re",
    "pathlib",
    "typing",
    "numpy",
    "pandas",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def verify_archive(path: Path, manifest: dict[str, Any]) -> dict[str, str]:
    if sha256_file(path) != manifest["package"]["sha256"]:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: package SHA-256 mismatch")
    hashes: dict[str, str] = {}
    with zipfile.ZipFile(path) as archive:
        names = {info.filename for info in archive.infolist() if not info.is_dir()}
        if names != EXPECTED_MEMBERS:
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: package member set mismatch")
        for name in sorted(names):
            hashes[name] = hashlib.sha256(archive.read(name)).hexdigest()
    if hashes != manifest["package"]["member_sha256"]:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: member hash mismatch")
    return hashes


def verify_transcript_archive_identities(paths: list[Path]) -> None:
    if len(paths) != len(EXPECTED_TRANSCRIPT_ARCHIVE_SHA256):
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: expected two transcript ZIPs")
    for path, expected in zip(paths, EXPECTED_TRANSCRIPT_ARCHIVE_SHA256):
        if not path.is_file() or sha256_file(path) != expected:
            raise RuntimeError(
                "BLOCKED_INPUT_IDENTITY: transcript ZIP identity mismatch"
            )


def load_packaged_runtime(path: Path) -> Any:
    """Load feature/inference functions from the extracted package itself."""

    spec = importlib.util.spec_from_file_location("s2_m0_extracted_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: packaged runtime not loadable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require_finite_numbers(value: Any, path: str = "manifest") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            _require_finite_numbers(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _require_finite_numbers(child, f"{path}[{index}]")
    elif isinstance(value, float) and not np.isfinite(value):
        raise RuntimeError(
            f"BLOCKED_PACKAGED_EQUIVALENCE: non-finite value at {path}"
        )


def verify_manifest_preconditions(package_path: Path, manifest: dict[str, Any]) -> None:
    """Bind READY to the frozen builder inputs and packaged fitted state."""

    try:
        if manifest.get("schema_version") != 1 or manifest.get("submission_id") != "S2_M0_CONTROL":
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: manifest identity mismatch")
        status = manifest.get("status")
        if status not in {"BUILT_PENDING_VERIFICATION", "PREPARED_NOT_SUBMITTED"}:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: manifest state mismatch")
        if manifest.get("repo_base_sha") != EXPECTED_REPO_BASE_SHA:
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: repository base mismatch")
        if manifest.get("historical_m0_pr") != 24 or manifest.get(
            "historical_m0_head"
        ) != EXPECTED_HISTORICAL_M0_HEAD:
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: historical M0 identity mismatch")
        expected_authority = (
            INITIAL_AUTHORITY
            if status == "BUILT_PENDING_VERIFICATION"
            else FINAL_AUTHORITY
        )
        if manifest.get("authority") != expected_authority:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: pre-verification authority mismatch")

        training = manifest["training_input_sha256"]
        for key, expected in EXPECTED_INPUT_SHA256.items():
            if training.get(key) != expected:
                raise RuntimeError(f"BLOCKED_INPUT_IDENTITY: {key} identity mismatch")
        if training.get("submission_01_members") != EXPECTED_SUBMISSION_01_MEMBERS:
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: Submission 01 member mismatch")

        phase0 = manifest["phase0_reproduction"]
        if phase0.get("status") != "PASS":
            raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: Phase-0 status mismatch")
        identity = phase0["identity"]
        if identity.get("dataset_index_sha256") != EXPECTED_INPUT_SHA256["canonical_index"]:
            raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: index identity mismatch")
        if identity.get("fold_artifact_sha256") != EXPECTED_INPUT_SHA256["regenerated_folds"]:
            raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: fold identity mismatch")
        if identity.get("session_features_sha256") != training.get("session_features"):
            raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: session-feature linkage mismatch")
        reference = phase0["reference"]
        canonical = phase0["canonical_oof"]
        observed_phase0 = {
            "base_log_loss": reference["base_log_loss"],
            "model_log_loss": reference["model_log_loss"],
            "auc": reference["auc"],
            **reference["coefficients"],
            "pooled_log_loss": canonical["pooled_log_loss"],
            "pooled_auc": canonical["pooled_auc"],
            "brier_score": canonical["calibration"]["brier_score"],
            "ece_10_equal_width": canonical["calibration"]["ece_10_equal_width"],
        }
        for key, expected in EXPECTED_PHASE0.items():
            observed = float(observed_phase0[key])
            if not np.isfinite(observed) or abs(observed - expected) > 1e-8:
                raise RuntimeError(
                    f"BLOCKED_M0_REPRODUCTION_DRIFT: {key} metric mismatch"
                )

        if manifest.get("feature_definition") != EXPECTED_FEATURE_DEFINITION:
            raise RuntimeError("BLOCKED_FULL_FIT: frozen feature definition mismatch")
        summary = manifest["deployment_fit_summary"]
        if summary.get("eligible_responses", 0) + summary.get("quiet_responses", 0) != 35_072:
            raise RuntimeError("BLOCKED_FULL_FIT: response-count partition mismatch")
        if summary.get("eligible_sessions", 0) + summary.get("quiet_sessions", 0) != 22_821:
            raise RuntimeError("BLOCKED_FULL_FIT: session-count partition mismatch")
        if summary.get("sklearn_direct_max_abs_difference", 1.0) > 1e-12:
            raise RuntimeError("BLOCKED_FULL_FIT: stored-state equivalence mismatch")
        if len(summary.get("n_iter", [])) != 1 or summary["n_iter"][0] <= 0:
            raise RuntimeError("BLOCKED_FULL_FIT: invalid iteration record")
        _require_finite_numbers(summary, "manifest.deployment_fit_summary")
        _require_finite_numbers(
            manifest["fitted_numerical_state"], "manifest.fitted_numerical_state"
        )

        package = manifest["package"]
        if package.get("filename") != "trace_the_ace_submission_02_m0_control.zip":
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: package filename mismatch")
        if package.get("byte_size") != package_path.stat().st_size:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: package size mismatch")
        with zipfile.ZipFile(package_path) as archive:
            inner = json.loads(archive.read("assets/model_manifest.json"))
            if inner.get("schema_version") != 1 or inner.get("submission_id") != "S2_M0_CONTROL":
                raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: inner manifest identity")
            source = inner["source_identity"]
            if source.get("repo_base_sha") != EXPECTED_REPO_BASE_SHA or source.get(
                "historical_m0_head"
            ) != EXPECTED_HISTORICAL_M0_HEAD:
                raise RuntimeError("BLOCKED_INPUT_IDENTITY: packaged source mismatch")
            if source.get("m0_train_sha256") != EXPECTED_M0_TRAIN_SHA256 or source.get(
                "m0_config_sha256"
            ) != EXPECTED_M0_CONFIG_SHA256:
                raise RuntimeError("BLOCKED_INPUT_IDENTITY: packaged M0 source mismatch")
            for inner_key, outer_key in (
                ("feature_definition", "feature_definition"),
                ("fit_summary", "deployment_fit_summary"),
                ("fitted_state", "fitted_numerical_state"),
                ("runtime_environment", "runtime_environment"),
            ):
                if inner.get(inner_key) != manifest.get(outer_key):
                    raise RuntimeError(
                        f"BLOCKED_PACKAGED_EQUIVALENCE: {inner_key} provenance mismatch"
                    )
            with np.load(
                io.BytesIO(archive.read("assets/m0_model.npz")), allow_pickle=False
            ) as model:
                outer_state = manifest["fitted_numerical_state"]
                if set(model.files) != set(outer_state):
                    raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model state keys")
                for key in model.files:
                    expected = np.asarray(outer_state[key], dtype=model[key].dtype)
                    if not np.array_equal(model[key], expected):
                        raise RuntimeError(
                            f"BLOCKED_PACKAGED_EQUIVALENCE: model state {key} mismatch"
                        )
    except RuntimeError:
        raise
    except (KeyError, TypeError, ValueError, OSError, zipfile.BadZipFile) as error:
        raise RuntimeError(
            f"BLOCKED_PACKAGED_EQUIVALENCE: malformed provenance manifest: {error}"
        ) from error


def verify_offline_source(source: str) -> None:
    tree = ast.parse(source)
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    unexpected = imported - ALLOWED_RUNTIME_IMPORTS
    if unexpected:
        raise RuntimeError(
            f"BLOCKED_RUNTIME_CONTRACT: runtime imports outside allowlist {unexpected}"
        )
    forbidden_tokens = (
        "http://",
        "https://",
        "requests",
        "urllib",
        "socket",
        "download",
    )
    lowered = source.lower()
    if any(token in lowered for token in forbidden_tokens):
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: network-capable runtime source")


def extract_package(path: Path, root: Path) -> Path:
    package_root = root / "package"
    package_root.mkdir(parents=True)
    with zipfile.ZipFile(path) as archive:
        names = {info.filename for info in archive.infolist() if not info.is_dir()}
        if names != EXPECTED_MEMBERS:
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: package member set mismatch")
        archive.extractall(package_root)
    return package_root


def run_extracted_once(
    package_path: Path,
    fixture_data: Path,
    temporary_root: Path,
) -> tuple[pd.DataFrame, str, Path]:
    package_root = extract_package(package_path, temporary_root)
    shutil.copytree(fixture_data, package_root / "data")
    foreign_cwd = temporary_root / "foreign_working_directory"
    foreign_cwd.mkdir()
    environment = os.environ.copy()
    # Exercise only the interpreter's ordinary installed runtime.  The verifier
    # itself may use an explicit scientific PYTHONPATH, but the packaged program
    # must not inherit that local build-time dependency path.
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONNOUSERSITE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(package_root / "main.py")],
        cwd=foreign_cwd,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
        timeout=180,
    )
    if completed.returncode:
        raise RuntimeError(
            "BLOCKED_RUNTIME_CONTRACT: extracted main.py failed: "
            f"{completed.stderr.strip()}"
        )
    output_path = package_root / "submission.csv"
    if not output_path.is_file():
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: submission.csv missing")
    output_hash = sha256_file(output_path)
    output = pd.read_csv(output_path, dtype={"response_id": str})
    return output, output_hash, package_root


def verify_output_contract(
    output: pd.DataFrame,
    expected_ids: list[str],
) -> None:
    if list(output.columns) != ["response_id", "probability"]:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: output columns mismatch")
    if len(output) != len(expected_ids):
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: output row count mismatch")
    if not output["response_id"].is_unique:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: duplicate output response_id")
    if output["response_id"].tolist() != expected_ids:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: output identity/order mismatch")
    probabilities = output["probability"].to_numpy(dtype=np.float64)
    if not np.isfinite(probabilities).all():
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: non-finite probability")
    if np.any((probabilities < 0.0) | (probabilities > 1.0)):
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: probability outside [0,1]")


def verify_direct_predictions(direct: pd.DataFrame) -> None:
    if list(direct.columns) != ["response_id", "probability"]:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: direct schema mismatch")
    if not direct["response_id"].is_unique:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: duplicate direct response_id")
    probabilities = direct["probability"].to_numpy(dtype=np.float64)
    if not np.isfinite(probabilities).all():
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: non-finite direct probability")
    if np.any((probabilities < 0.0) | (probabilities > 1.0)):
        raise RuntimeError(
            "BLOCKED_PACKAGED_EQUIVALENCE: direct probability outside [0,1]"
        )


def _transcript_lookup(paths: Iterable[Path]) -> dict[str, tuple[Path, str]]:
    lookup: dict[str, tuple[Path, str]] = {}
    for path in paths:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".csv"):
                    continue
                session_id = Path(info.filename).stem
                if session_id in lookup:
                    raise RuntimeError("BLOCKED_INPUT_IDENTITY: duplicate transcript session")
                lookup[session_id] = (path, info.filename)
    return lookup


def transcript_source_equivalence(
    transcript_paths: list[Path],
    fixture_data: Path,
    package_root: Path,
    packaged_output: pd.DataFrame,
    packaged_runtime: Any,
) -> tuple[float, float]:
    test_features = pd.read_csv(
        fixture_data / "test_features.csv",
        dtype={"response_id": str, "session_id": str},
    )
    lookup = _transcript_lookup(transcript_paths)
    session_ids = sorted(test_features["session_id"].unique())
    directory_features: dict[str, np.ndarray] = {}
    archive_features: dict[str, np.ndarray] = {}
    maximum_feature_difference = 0.0
    for session_id in session_ids:
        directory_value = packaged_runtime.session_features(
            fixture_data / "test_transcripts" / f"{session_id}.csv"
        )
        if session_id not in lookup:
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: archive transcript missing")
        archive_path, member = lookup[session_id]
        with zipfile.ZipFile(archive_path) as archive:
            payload = archive.read(member)
        text = io.TextIOWrapper(io.BytesIO(payload), encoding="utf-8-sig", newline="")
        reader = csv.DictReader(text)
        if reader.fieldnames != packaged_runtime.TRANSCRIPT_COLUMNS:
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: archive transcript schema")
        archive_value = packaged_runtime.session_features_from_rows(reader)
        if not np.array_equal(directory_value, archive_value, equal_nan=True):
            difference = np.nanmax(np.abs(directory_value - archive_value))
            maximum_feature_difference = max(maximum_feature_difference, float(difference))
            raise RuntimeError(
                "BLOCKED_RUNTIME_CONTRACT: ZIP/directory feature mismatch"
            )
        directory_features[session_id] = directory_value
        archive_features[session_id] = archive_value

    archive_matrix = np.vstack(
        [archive_features[session_id] for session_id in test_features["session_id"]]
    )
    with np.load(package_root / "assets" / "m0_model.npz", allow_pickle=False) as model:
        archive_probabilities = packaged_runtime.predict_feature_matrix(
            archive_matrix, model
        )
    packaged_probabilities = packaged_output["probability"].to_numpy(dtype=np.float64)
    probability_difference = float(
        np.max(np.abs(archive_probabilities - packaged_probabilities))
    )
    if probability_difference > 1e-12:
        raise RuntimeError(
            "BLOCKED_RUNTIME_CONTRACT: ZIP/directory prediction mismatch "
            f"{probability_difference}"
        )
    return maximum_feature_difference, probability_difference


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--fixture-dir", required=True, type=Path)
    parser.add_argument("--direct-predictions", required=True, type=Path)
    parser.add_argument("--transcripts-zip", action="append", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output-record", required=True, type=Path)
    args = parser.parse_args()
    if len(args.transcripts_zip) != 2:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: expected exactly two transcript ZIPs")
    verify_transcript_archive_identities(args.transcripts_zip)

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    verify_archive(args.zip, manifest)
    verify_manifest_preconditions(args.zip, manifest)
    with zipfile.ZipFile(args.zip) as archive:
        runtime_source = archive.read("main.py").decode("utf-8")
    verify_offline_source(runtime_source)

    direct = pd.read_csv(
        args.direct_predictions, dtype={"response_id": str}
    )
    verify_direct_predictions(direct)
    expected_ids = direct["response_id"].tolist()

    with tempfile.TemporaryDirectory(prefix="s2_m0_verify_a_") as first_tmp:
        first, first_hash, first_root = run_extracted_once(
            args.zip, args.fixture_dir, Path(first_tmp)
        )
        verify_output_contract(first, expected_ids)
        if direct["response_id"].tolist() != first["response_id"].tolist():
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: response order mismatch")
        max_difference = float(
            np.max(
                np.abs(
                    direct["probability"].to_numpy(dtype=np.float64)
                    - first["probability"].to_numpy(dtype=np.float64)
                )
            )
        )
        if max_difference > 1e-12:
            raise RuntimeError(
                "BLOCKED_PACKAGED_EQUIVALENCE: max abs difference "
                f"{max_difference}"
            )
        feature_difference, transcript_probability_difference = (
            transcript_source_equivalence(
                args.transcripts_zip,
                args.fixture_dir,
                first_root,
                first,
                load_packaged_runtime(first_root / "main.py"),
            )
        )

    with tempfile.TemporaryDirectory(prefix="s2_m0_verify_b_") as second_tmp:
        second, second_hash, _ = run_extracted_once(
            args.zip, args.fixture_dir, Path(second_tmp)
        )
        verify_output_contract(second, expected_ids)
    if first_hash != second_hash:
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: nondeterministic submission.csv")

    checks = {
        "m0_historical_reproduction": "PASS",
        "full_training_m0_fit": "PASS",
        "zip_created": "PASS",
        "direct_packaged_equivalence": "PASS",
        "zip_directory_transcript_equivalence": "PASS",
        "working_directory_independence": "PASS",
        "deterministic_rerun": "PASS",
        "clean_environment_extraction": "PASS",
        "offline_runtime": "PASS",
        "output_schema": "PASS",
    }
    verification = {
        "schema_version": 1,
        "stop": "READY_FOR_HUMAN_SUBMISSION_REVIEW",
        "D_Submission02": "PREPARED_ENGINEERING_CONTROL",
        "checks": checks,
        "direct_packaged_max_abs_difference": max_difference,
        "zip_directory_max_abs_feature_difference": feature_difference,
        "zip_directory_max_abs_probability_difference": (
            transcript_probability_difference
        ),
        "deterministic_submission_csv_sha256": first_hash,
        "offline_basis": {
            "runtime_import_allowlist": sorted(ALLOWED_RUNTIME_IMPORTS),
            "build_time_pythonpath_removed": True,
            "user_site_disabled": True,
            "network_disabled_environment": os.environ.get(
                "CODEX_SANDBOX_NETWORK_DISABLED"
            )
            == "1",
            "network_calls_in_runtime": False,
        },
    }
    args.output_record.parent.mkdir(parents=True, exist_ok=True)
    args.output_record.write_bytes(json_bytes(verification))

    manifest["status"] = "PREPARED_NOT_SUBMITTED"
    manifest["verification"] = verification
    manifest["authority"] = FINAL_AUTHORITY
    args.manifest.write_bytes(json_bytes(manifest))
    print(json.dumps(verification, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
