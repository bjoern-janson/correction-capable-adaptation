"""Verify Submission 03 provenance, deterministic runtime, and equivalence."""
from __future__ import annotations

import argparse
import ast
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
from typing import Any

import numpy as np
import pandas as pd


SUBMISSION_ID = "SUBMISSION_03_M1_CAL_CONTROL"
PACKAGE_FILENAME = "trace_the_ace_submission_03_m1_cal_control.zip"
EXPECTED_MEMBERS = {
    "main.py",
    "assets/m1_cal_model.npz",
    "assets/model_manifest.json",
}
EXPECTED_REPO_BASE_SHA = "4d02c557e234772ed28319fd4cf67098341318fd"
EXPECTED_HISTORICAL_M1_CAL_HEAD = "b6327193f38ef2a303718eb25740c15811755489"
EXPECTED_HISTORICAL_PARENT_SHA = "a067828455a9d992023213a9d9bd113e1ec041c73f1178b6706961760f219484"
EXPECTED_RECONSTITUTED_PARENT_SHA = "d5f2c1ce4f8433de29c4cdd54834801ca20b24cbc885f6a485e15d02cef5c34a"
EXPECTED_RECONSTITUTED_M1_CAL_CONFIG_SHA = "a72778946c6c67e768a882dccae66650a903dbb403827e7234cd6addd4b5a07d"
EXPECTED_SOURCE_SHA256 = {
    "m1_prime_runner": "e8134bf4ec8d18aca74c6fb5e7bcf3d02ab327f0f96115e5b566474cf500f208",
    "m1_prime_config": "a8998153f3545b97e68e7095fdafeb28ee195b6f2ef3a910ee82b85cd2260aed",
    "m1_cal_runner": "901cbe97c25673adbeb562c4bfdd422c3cb99da6774880ddfe2a39b80487ecb8",
    "m1_cal_config": "fbdcdd3e589401dfdb47d1eb8f589695bb86c62a1cf30e1838f12e7b1b7767fe",
}
EXPECTED_INPUT_SHA256 = {
    "train_features": "71bea3abb76a1cff5e1eaa75b9cbcfaf26d0419f6274b83a199ed520047a5063",
    "train_labels": "d98ee4389e5cde3f66d6d15b7b574261024a80e405958eca333d3c1921fd65b9",
    "transcripts_part1": "f8172da9547286f7bd09967571c56626f63e39fb6e24ffcdf475071db57836b7",
    "transcripts_part2": "22ff3c12b599ec82489d9cb546cc2dd2322a8e77dc812ea15352f4830f24cd82",
    "canonical_index": "296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60",
    "canonical_folds": "014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6",
    "m0_session_features": "29f972858d5193b07d89d17cd55041f89de85ca77a0ddb875cd2c7cbaf6c364b",
}
EXPECTED_STATE_SHAPES = {
    "text_coef": (262_144,),
    "structural_coef": (4,),
    "base_intercept": (1,),
    "structural_medians": (4,),
    "scaler_mean": (4,),
    "scaler_scale": (4,),
    "platt_slope": (1,),
    "platt_intercept": (1,),
}
INITIAL_AUTHORITY = {
    "engineering_control_prepared": False,
    "competition_submission_executed": False,
    "submission_04_authorized": False,
    "calibration_search_opened": False,
    "blending_opened": False,
    "cca_authority_changed": False,
}
FINAL_AUTHORITY = {**INITIAL_AUTHORITY, "engineering_control_prepared": True}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            indent=2,
            ensure_ascii=True,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _require_finite_numbers(value: Any, path: str = "manifest") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            _require_finite_numbers(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _require_finite_numbers(child, f"{path}[{index}]")
    elif isinstance(value, float) and not np.isfinite(value):
        raise RuntimeError(f"BLOCKED_PACKAGED_EQUIVALENCE: non-finite {path}")


def verify_offline_source(source: str) -> None:
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        raise RuntimeError(f"BLOCKED_RUNTIME_CONTRACT: invalid main.py: {error}") from error
    forbidden_roots = {
        "http",
        "httpx",
        "requests",
        "socket",
        "subprocess",
        "urllib",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            modules = [(node.module or "").split(".")[0]]
        else:
            continue
        if forbidden_roots.intersection(modules):
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: network/process import")


def verify_archive(path: Path, manifest: dict[str, Any]) -> tuple[dict[str, bytes], dict[str, Any]]:
    package = manifest["package"]
    if path.name != PACKAGE_FILENAME or package.get("filename") != PACKAGE_FILENAME:
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: package filename")
    if sha256_file(path) != package.get("sha256"):
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: package SHA-256")
    if path.stat().st_size != package.get("byte_size"):
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: package byte size")
    with zipfile.ZipFile(path) as archive:
        names = {info.filename for info in archive.infolist() if not info.is_dir()}
        if names != EXPECTED_MEMBERS or len(archive.infolist()) != len(EXPECTED_MEMBERS):
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: exact package member set")
        members = {name: archive.read(name) for name in sorted(names)}
    hashes = {name: sha256_bytes(payload) for name, payload in members.items()}
    if hashes != package.get("member_sha256"):
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: package member SHA-256")
    try:
        inner = json.loads(members["assets/model_manifest.json"])
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: inner manifest") from error
    verify_offline_source(members["main.py"].decode("utf-8"))
    return members, inner


def verify_manifest_preconditions(
    package_path: Path, manifest: dict[str, Any]
) -> tuple[dict[str, bytes], dict[str, Any]]:
    try:
        if manifest.get("schema_version") != 1 or manifest.get("submission_id") != SUBMISSION_ID:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: manifest identity")
        status = manifest.get("status")
        if status not in {"BUILT_PENDING_VERIFICATION", "PREPARED_NOT_SUBMITTED"}:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: manifest state")
        expected_authority = INITIAL_AUTHORITY if status == "BUILT_PENDING_VERIFICATION" else FINAL_AUTHORITY
        if manifest.get("authority") != expected_authority:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: authority state")
        if manifest.get("repo_base_sha") != EXPECTED_REPO_BASE_SHA:
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: repository base")
        if manifest.get("historical_m1_cal_pr") != 27 or manifest.get(
            "historical_m1_cal_head"
        ) != EXPECTED_HISTORICAL_M1_CAL_HEAD:
            raise RuntimeError("BLOCKED_HISTORICAL_IDENTITY: M1-cal lineage")
        if manifest.get("historical_source_sha256") != EXPECTED_SOURCE_SHA256:
            raise RuntimeError("BLOCKED_HISTORICAL_IDENTITY: source SHA-256")
        if manifest.get("training_input_sha256") != EXPECTED_INPUT_SHA256:
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: frozen input SHA-256")

        phase = manifest["phase_a_reconstitution"]
        if phase.get("status") != "PASS":
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: Phase A")
        if phase.get("historical_parent_sha256") != EXPECTED_HISTORICAL_PARENT_SHA:
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: historical parent")
        if phase.get("regenerated_parent_sha256") != EXPECTED_RECONSTITUTED_PARENT_SHA:
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: engineering parent")
        if phase.get(
            "reconstituted_m1_cal_config_sha256"
        ) != EXPECTED_RECONSTITUTED_M1_CAL_CONFIG_SHA:
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: derived config")
        if phase.get("historical_parent_byte_identity") != "NOT_REPRODUCED" or phase.get(
            "regenerated_parent_numerical_identity"
        ) != "PASS":
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: parent labeling")
        if phase.get("objective_information_present") is not False or phase.get(
            "maximum_within_session_probability_range"
        ) != 0.0:
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: objective exclusion")
        if len(phase.get("inner_base_n_iter", [])) != 25 or any(
            int(value) <= 0 or int(value) >= 500
            for value in phase["inner_base_n_iter"]
        ):
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: inner convergence")
        raw = phase["m1_prime"]
        calibrated = phase["m1_cal"]
        phase_checks = {
            "raw_ll": (raw["log_loss"], 0.5765421662, 1e-6),
            "raw_auc": (raw["auc"], 0.6765416347, 1e-6),
            "cal_ll": (calibrated["log_loss"], 0.5683582154, 1e-5),
            "cal_auc": (calibrated["auc"], 0.6765200311, 1e-5),
            "brier": (calibrated["brier"], 0.1921277205, 1e-5),
            "ece": (calibrated["ece_10"], 0.0159898481, 1e-4),
            "bias": (calibrated["absolute_mean_bias"], 0.0105359299, 1e-4),
        }
        for label, (observed, expected, tolerance) in phase_checks.items():
            if not np.isfinite(observed) or abs(float(observed) - expected) > tolerance:
                raise RuntimeError(
                    f"BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: {label}"
                )
        if not float(calibrated["log_loss"]) < float(raw["log_loss"]):
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: LL direction")

        summary = manifest["deployment_fit_summary"]
        if summary.get("rows") != 35_072 or summary.get("sessions") != 22_821:
            raise RuntimeError("BLOCKED_FULL_FIT: population counts")
        if summary.get("feature_dimension") != 262_148 or summary.get(
            "coefficient_shape"
        ) != [1, 262_148]:
            raise RuntimeError("BLOCKED_FULL_FIT: fitted shape")
        if not 0 < int(summary.get("full_base_n_iter", 500)) < 500:
            raise RuntimeError("BLOCKED_FULL_FIT: convergence")
        folds = summary.get("crossfit_folds", [])
        if len(folds) != 5 or sorted(int(fold.get("fold", -1)) for fold in folds) != list(range(5)):
            raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: folds")
        if sum(int(fold.get("responses", 0)) for fold in folds) != 35_072:
            raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: fold coverage")
        if any(not 0 < int(fold.get("base_n_iter", 500)) < 500 for fold in folds):
            raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: convergence")
        if not np.isfinite(summary.get("platt_slope", np.nan)) or float(
            summary["platt_slope"]
        ) <= 0:
            raise RuntimeError("BLOCKED_CALIBRATOR_FIT: Platt slope")
        if not np.isfinite(summary.get("platt_intercept", np.nan)):
            raise RuntimeError("BLOCKED_CALIBRATOR_FIT: Platt intercept")
        if float(summary.get("stored_state_raw_max_abs_difference", 1.0)) > 1e-12:
            raise RuntimeError("BLOCKED_FITTED_STATE_EQUIVALENCE: raw score")
        if float(summary.get("stored_state_probability_max_abs_difference", 1.0)) > 1e-12:
            raise RuntimeError("BLOCKED_FITTED_STATE_EQUIVALENCE: probability")

        members, inner = verify_archive(package_path, manifest)
        if inner.get("schema_version") != 1 or inner.get("submission_id") != SUBMISSION_ID:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: inner identity")
        if inner.get("objective_information_present") is not False:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: inner objective exclusion")
        source = inner["source_identity"]
        if source.get("repo_base_sha") != EXPECTED_REPO_BASE_SHA or source.get(
            "historical_m1_cal_head"
        ) != EXPECTED_HISTORICAL_M1_CAL_HEAD:
            raise RuntimeError("BLOCKED_HISTORICAL_IDENTITY: packaged lineage")
        for key, expected in EXPECTED_SOURCE_SHA256.items():
            if source.get(key) != expected:
                raise RuntimeError("BLOCKED_HISTORICAL_IDENTITY: packaged source")
        parent = inner["parent_identity"]
        if parent != {
            "historical_parent_sha256": EXPECTED_HISTORICAL_PARENT_SHA,
            "regenerated_parent_sha256": EXPECTED_RECONSTITUTED_PARENT_SHA,
            "historical_parent_byte_identity": "NOT_REPRODUCED",
            "regenerated_parent_numerical_identity": "PASS",
            "engineering_parent_label": "M1_PRIME_RECONSTITUTED",
        }:
            raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: packaged parent")
        if inner.get("model_specification") != manifest.get("model_specification"):
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model specification")
        model_state = inner["model_state"]
        if model_state != manifest.get("fitted_state"):
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fitted-state provenance")
        model_bytes = members["assets/m1_cal_model.npz"]
        if sha256_bytes(model_bytes) != model_state.get("sha256"):
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model asset SHA-256")
        with np.load(io.BytesIO(model_bytes), allow_pickle=False) as model:
            if set(model.files) != set(EXPECTED_STATE_SHAPES):
                raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model keys")
            for key, shape in EXPECTED_STATE_SHAPES.items():
                value = np.asarray(model[key])
                described = model_state["arrays"][key]
                if value.shape != shape or list(value.shape) != described.get("shape"):
                    raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model shape")
                if str(value.dtype) != described.get("dtype") or not np.isfinite(value).all():
                    raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: model dtype/value")
            if np.any(np.asarray(model["scaler_scale"]) <= 0) or float(
                model["platt_slope"][0]
            ) <= 0:
                raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: invalid state geometry")
        _require_finite_numbers(manifest)
        return members, inner
    except RuntimeError:
        raise
    except (KeyError, TypeError, ValueError, OSError, zipfile.BadZipFile) as error:
        raise RuntimeError(
            f"BLOCKED_PACKAGED_EQUIVALENCE: malformed provenance: {error}"
        ) from error


def extract_package(path: Path, destination: Path) -> Path:
    root = destination / "package"
    root.mkdir(parents=True)
    with zipfile.ZipFile(path) as archive:
        if {info.filename for info in archive.infolist()} != EXPECTED_MEMBERS:
            raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: extraction member set")
        archive.extractall(root)
    return root


def run_extracted_once(
    package_path: Path,
    fixture_data: Path,
    temporary_root: Path,
    runtime_python: Path,
    runtime_pythonpath: list[Path],
) -> tuple[pd.DataFrame, str, Path]:
    package_root = extract_package(package_path, temporary_root)
    shutil.copytree(fixture_data, package_root / "data")
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONNOUSERSITE"] = "1"
    if runtime_pythonpath:
        environment["PYTHONPATH"] = os.pathsep.join(str(path) for path in runtime_pythonpath)
    result = subprocess.run(
        [str(runtime_python), str(package_root / "main.py")],
        cwd=temporary_root,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=300,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "BLOCKED_RUNTIME_CONTRACT: packaged inference failed: "
            + result.stderr[-2000:]
        )
    output_path = package_root / "submission.csv"
    if not output_path.is_file():
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: missing submission.csv")
    return (
        pd.read_csv(output_path, dtype={"response_id": str}),
        sha256_file(output_path),
        package_root,
    )


def verify_output_contract(output: pd.DataFrame, expected_ids: list[str]) -> np.ndarray:
    if list(output.columns) != ["response_id", "probability"]:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: exact columns")
    if len(output) != len(expected_ids) or not output["response_id"].is_unique:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: response identity")
    if output["response_id"].tolist() != expected_ids:
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: response order")
    probability = output["probability"].to_numpy(dtype=np.float64)
    if not np.isfinite(probability).all() or np.any((probability < 0) | (probability > 1)):
        raise RuntimeError("BLOCKED_OUTPUT_SCHEMA: invalid probability")
    return probability


def load_packaged_runtime(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("submission03_packaged_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: load packaged runtime")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def component_raw_scores(package_root: Path, fixture_data: Path) -> tuple[list[str], np.ndarray]:
    runtime = load_packaged_runtime(package_root / "main.py")
    submission = pd.read_csv(
        fixture_data / "submission_format.csv", dtype={"response_id": str}
    )
    features = pd.read_csv(
        fixture_data / "test_features.csv",
        dtype={"response_id": str, "session_id": str},
    )
    frame = submission[["response_id"]].merge(
        features[["response_id", "session_id"]],
        on="response_id",
        validate="one_to_one",
        sort=False,
    )
    sessions = sorted(frame["session_id"].unique())
    texts = []
    ordinary = {}
    for session_id in sessions:
        text, values = runtime.transcript_blocks(
            fixture_data / "test_transcripts" / f"{session_id}.csv"
        )
        texts.append(text)
        ordinary[session_id] = values
    session_text = runtime.make_vectorizer().transform(texts).tocsr().astype(np.float32)
    session_row = {session_id: index for index, session_id in enumerate(sessions)}
    rows = np.fromiter(
        (session_row[session_id] for session_id in frame["session_id"]),
        dtype=np.int32,
        count=len(frame),
    )
    ordinary_matrix = np.vstack([ordinary[sid] for sid in frame["session_id"]])
    with np.load(package_root / "assets" / "m1_cal_model.npz", allow_pickle=False) as model:
        raw, _, _ = runtime.predict_blocks(session_text[rows].tocsr(), ordinary_matrix, model)
    return frame["response_id"].tolist(), raw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--fixture-dir", required=True, type=Path)
    parser.add_argument("--runtime-python", type=Path, default=Path(sys.executable))
    parser.add_argument("--runtime-pythonpath", action="append", type=Path, default=[])
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    verify_manifest_preconditions(args.zip, manifest)
    fixture_record = manifest.get("fixture", {})
    direct_path = args.fixture_dir / "direct_predictions.csv"
    if fixture_record.get("selection_is_label_free") is not True or fixture_record.get(
        "direct_predictions_sha256"
    ) != sha256_file(direct_path):
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture provenance")
    direct = pd.read_csv(
        direct_path, dtype={"response_id": str}
    )
    if list(direct.columns) != ["response_id", "probability", "raw_score"]:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: direct fixture schema")
    expected_ids = direct["response_id"].tolist()
    if fixture_record.get("responses") != len(expected_ids) or fixture_record.get(
        "response_order_sha256"
    ) != sha256_bytes("\n".join(expected_ids).encode("utf-8")):
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture response identity")
    if not direct["response_id"].is_unique:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: direct fixture identity")
    direct_probability = direct["probability"].to_numpy(dtype=np.float64)
    direct_raw = direct["raw_score"].to_numpy(dtype=np.float64)
    if not np.isfinite(direct_probability).all() or not np.isfinite(direct_raw).all():
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: direct fixture values")

    with tempfile.TemporaryDirectory(prefix="submission03_verify_first_") as first:
        first_output, first_hash, first_root = run_extracted_once(
            args.zip,
            args.fixture_dir / "data",
            Path(first),
            args.runtime_python,
            args.runtime_pythonpath,
        )
        first_probability = verify_output_contract(first_output, expected_ids)
        component_ids, packaged_raw = component_raw_scores(
            first_root, args.fixture_dir / "data"
        )
    with tempfile.TemporaryDirectory(prefix="submission03_verify_second_") as second:
        second_output, second_hash, _ = run_extracted_once(
            args.zip,
            args.fixture_dir / "data",
            Path(second),
            args.runtime_python,
            args.runtime_pythonpath,
        )
        second_probability = verify_output_contract(second_output, expected_ids)
    if first_hash != second_hash or not np.array_equal(first_probability, second_probability):
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: nondeterministic submission.csv")
    if component_ids != expected_ids:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: component response order")
    raw_difference = float(np.max(np.abs(direct_raw - packaged_raw)))
    final_difference = float(np.max(np.abs(direct_probability - first_probability)))
    if raw_difference > 1e-10:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: raw-score difference")
    if final_difference > 1e-10:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: final-probability difference")

    manifest["verification"] = {
        "historical_m1_prime_numerical_reproduction": "PASS",
        "historical_m1_cal_numerical_reconstitution": "PASS",
        "full_training_base_fit": "PASS",
        "deployment_crossfit_platt": "PASS",
        "zip_created": "PASS",
        "deterministic_zip_rebuild": "PASS",
        "direct_package_equivalence": "PASS",
        "direct_package_raw_max_abs_difference": raw_difference,
        "direct_package_final_max_abs_difference": final_difference,
        "deterministic_submission_csv": "PASS",
        "submission_csv_sha256": first_hash,
        "offline_runtime": "PASS",
        "clean_working_directory_runtime": "PASS",
        "output_schema": "PASS",
        "smoke_test_ready": True,
        "competition_submission_executed": False,
    }
    manifest["status"] = "PREPARED_NOT_SUBMITTED"
    manifest["authority"] = FINAL_AUTHORITY
    args.manifest.write_bytes(json_bytes(manifest))
    print(
        json.dumps(
            {
                "STOP": "READY_FOR_HUMAN_SUBMISSION_REVIEW",
                "status": manifest["status"],
                "zip_sha256": manifest["package"]["sha256"],
                "submission_csv_sha256": first_hash,
                "max_abs_difference": final_difference,
                "competition_submission_executed": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
