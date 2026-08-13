"""Build the frozen Trace the Ace Submission 03 M1-cal transport control.

The historical/reconstituted Phase-A result is an explicit input.  This script
does not rewrite or silently bypass either historical runner and does not run
the expensive historical nested calibration procedure itself.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import platform
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any, Iterable, Mapping

import numpy as np
import pandas as pd
import scipy
import sklearn
import yaml
from scipy import sparse
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import runtime_main  # noqa: E402


SUBMISSION_ID = "SUBMISSION_03_M1_CAL_CONTROL"
PACKAGE_FILENAME = "trace_the_ace_submission_03_m1_cal_control.zip"
MANIFEST_FILENAME = "submission_03_manifest.json"
REPO_BASE_SHA = "4d02c557e234772ed28319fd4cf67098341318fd"
HISTORICAL_M1_CAL_PR = 27
HISTORICAL_M1_CAL_HEAD = "b6327193f38ef2a303718eb25740c15811755489"
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
HISTORICAL_PARENT_SHA256 = "a067828455a9d992023213a9d9bd113e1ec041c73f1178b6706961760f219484"
RECONSTITUTED_PARENT_SHA256 = "d5f2c1ce4f8433de29c4cdd54834801ca20b24cbc885f6a485e15d02cef5c34a"
RECONSTITUTED_M1_CAL_CONFIG_SHA256 = "a72778946c6c67e768a882dccae66650a903dbb403827e7234cd6addd4b5a07d"
HISTORICAL_M1_PRIME = {"log_loss": 0.5765421662, "auc": 0.6765416347}
HISTORICAL_M1_CAL = {
    "log_loss": 0.5683582154,
    "auc": 0.6765200311,
    "brier": 0.1921277205,
    "ece_10": 0.0159898481,
    "absolute_mean_bias": 0.0105359299,
    "delta_log_loss": -0.0081839508,
}
PHASE_A_TOLERANCE = {
    "log_loss": 1e-5,
    "auc": 1e-5,
    "brier": 1e-5,
    "ece_10": 1e-4,
    "absolute_mean_bias": 1e-4,
}
EXPECTED_PACKAGE_MEMBERS = {
    "main.py",
    "assets/m1_cal_model.npz",
    "assets/model_manifest.json",
}
INITIAL_AUTHORITY = {
    "engineering_control_prepared": False,
    "competition_submission_executed": False,
    "submission_04_authorized": False,
    "calibration_search_opened": False,
    "blending_opened": False,
    "cca_authority_changed": False,
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def verify_hash(path: Path, expected: str, label: str) -> str:
    if not path.is_file():
        raise RuntimeError(f"BLOCKED_INPUT_IDENTITY: missing {label}: {path}")
    observed = sha256_file(path)
    if observed != expected:
        raise RuntimeError(
            f"BLOCKED_INPUT_IDENTITY: {label} SHA-256 {observed} != {expected}"
        )
    return observed


def normalized_source_bytes(path: Path) -> bytes:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")


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


def _zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def write_deterministic_zip(path: Path, members: Mapping[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(members):
            archive.writestr(_zip_info(name), members[name], compresslevel=9)


def deterministic_npz_bytes(arrays: Mapping[str, np.ndarray]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(arrays):
            array_buffer = io.BytesIO()
            np.lib.format.write_array(
                array_buffer, np.asarray(arrays[name]), allow_pickle=False
            )
            archive.writestr(
                _zip_info(f"{name}.npy"), array_buffer.getvalue(), compresslevel=9
            )
    return output.getvalue()


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"BLOCKED_HISTORICAL_IDENTITY: cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def calibration_summary(y: np.ndarray, probability: np.ndarray) -> dict[str, float]:
    edges = np.linspace(0.0, 1.0, 11)
    bin_index = np.clip(
        np.digitize(probability, edges[1:-1], right=False), 0, 9
    )
    ece = 0.0
    for index in range(10):
        mask = bin_index == index
        if np.any(mask):
            ece += float(mask.mean()) * abs(
                float(probability[mask].mean()) - float(y[mask].mean())
            )
    return {
        "brier": float(brier_score_loss(y, probability)),
        "ece_10": float(ece),
        "absolute_mean_bias": abs(float(probability.mean()) - float(y.mean())),
    }


def verify_historical_sources(
    m1_prime_runner: Path,
    m1_prime_config: Path,
    m1_cal_runner: Path,
    m1_cal_config: Path,
) -> dict[str, str]:
    paths = {
        "m1_prime_runner": m1_prime_runner,
        "m1_prime_config": m1_prime_config,
        "m1_cal_runner": m1_cal_runner,
        "m1_cal_config": m1_cal_config,
    }
    observed = {}
    for key, path in paths.items():
        try:
            observed[key] = verify_hash(path, EXPECTED_SOURCE_SHA256[key], key)
        except RuntimeError as error:
            raise RuntimeError(str(error).replace("BLOCKED_INPUT_IDENTITY", "BLOCKED_HISTORICAL_IDENTITY")) from error
    return observed


def verify_raw_inputs(args: argparse.Namespace) -> dict[str, str]:
    if len(args.transcripts_zip) != 2:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: expected exactly two transcript ZIPs")
    hashes = {
        "train_features": verify_hash(
            args.train_features, EXPECTED_INPUT_SHA256["train_features"], "train features"
        ),
        "train_labels": verify_hash(
            args.train_labels, EXPECTED_INPUT_SHA256["train_labels"], "train labels"
        ),
        "canonical_index": verify_hash(
            args.index, EXPECTED_INPUT_SHA256["canonical_index"], "canonical index"
        ),
        "canonical_folds": verify_hash(
            args.folds, EXPECTED_INPUT_SHA256["canonical_folds"], "canonical folds"
        ),
        "m0_session_features": verify_hash(
            args.m0_session_features,
            EXPECTED_INPUT_SHA256["m0_session_features"],
            "M0 session features",
        ),
    }
    for path, key in zip(args.transcripts_zip, ("transcripts_part1", "transcripts_part2")):
        hashes[key] = verify_hash(path, EXPECTED_INPUT_SHA256[key], key)
    verify_transcript_root_equivalence(args.transcripts_zip, args.transcripts_root)

    features = pd.read_csv(
        args.train_features, dtype={"response_id": str, "session_id": str}
    )
    labels = pd.read_csv(args.train_labels, dtype={"response_id": str})
    if len(features) != 35_072 or features["session_id"].nunique() != 22_821:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: training row/session counts")
    if features["response_id"].tolist() != labels["response_id"].tolist():
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: feature/label response order")
    return hashes


def verify_transcript_root_equivalence(
    archives: list[Path],
    roots: list[Path],
    expected_counts: tuple[int, ...] = (11_400, 11_421),
) -> None:
    """Require every extracted transcript byte to match the frozen ZIP corpus."""

    root_paths: dict[str, Path] = {}
    for root in roots:
        for path in root.rglob("*.csv"):
            if path.stem in root_paths:
                raise RuntimeError(
                    "BLOCKED_INPUT_IDENTITY: duplicate extracted transcript"
                )
            root_paths[path.stem] = path
    archive_members: dict[str, tuple[Path, str]] = {}
    archive_counts = []
    for archive_path in archives:
        count = 0
        with zipfile.ZipFile(archive_path) as archive:
            for info in archive.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".csv"):
                    continue
                session_id = Path(info.filename).stem
                if session_id in archive_members:
                    raise RuntimeError(
                        "BLOCKED_INPUT_IDENTITY: duplicate archived transcript"
                    )
                archive_members[session_id] = (archive_path, info.filename)
                count += 1
        archive_counts.append(count)
    if archive_counts != list(expected_counts) or set(root_paths) != set(archive_members):
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: transcript corpus coverage")
    open_archives = {path: zipfile.ZipFile(path) for path in archives}
    try:
        for session_id in sorted(root_paths):
            archive_path, member = archive_members[session_id]
            if root_paths[session_id].read_bytes() != open_archives[archive_path].read(
                member
            ):
                raise RuntimeError(
                    "BLOCKED_INPUT_IDENTITY: extracted transcript byte mismatch"
                )
    finally:
        for archive in open_archives.values():
            archive.close()


def verify_phase_a(
    index_path: Path,
    parent_oof_path: Path,
    parent_record_path: Path,
    m1_cal_oof_path: Path,
    m1_cal_record_path: Path,
) -> dict[str, Any]:
    verify_hash(
        parent_oof_path,
        RECONSTITUTED_PARENT_SHA256,
        "M1_PRIME_RECONSTITUTED OOF",
    )
    parent_record = json.loads(parent_record_path.read_text(encoding="utf-8"))
    cal_record = json.loads(m1_cal_record_path.read_text(encoding="utf-8"))
    cal_identity = cal_record.get("identity", {})
    expected_cal_identity = {
        "dataset_index_sha256": EXPECTED_INPUT_SHA256["canonical_index"],
        "fold_artifact_sha256": EXPECTED_INPUT_SHA256["canonical_folds"],
        "m0_session_features_sha256": EXPECTED_INPUT_SHA256["m0_session_features"],
        "parent_oof_sha256": RECONSTITUTED_PARENT_SHA256,
        "parent_runner_sha256": EXPECTED_SOURCE_SHA256["m1_prime_runner"],
        "config_sha256": RECONSTITUTED_M1_CAL_CONFIG_SHA256,
    }
    if any(cal_identity.get(key) != value for key, value in expected_cal_identity.items()):
        raise RuntimeError(
            "BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: Phase-A procedure identity"
        )
    index = pd.read_csv(index_path, dtype={"response_id": str, "session_id": str})
    parent = pd.read_csv(parent_oof_path, dtype={"response_id": str})
    calibrated = pd.read_csv(
        m1_cal_oof_path, dtype={"response_id": str, "session_id": str}
    )
    required_parent = {"response_id", "m1_prime_probability"}
    required_cal = {"response_id", "session_id", "m1_cal_probability"}
    if not required_parent.issubset(parent.columns) or not required_cal.issubset(calibrated.columns):
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: OOF schema")
    if not parent["response_id"].is_unique or not calibrated["response_id"].is_unique:
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: duplicate OOF identity")
    frame = index[["response_id", "session_id", "is_correct"]].merge(
        parent[["response_id", "m1_prime_probability"]],
        on="response_id",
        validate="one_to_one",
    ).merge(
        calibrated[["response_id", "session_id", "m1_cal_probability"]],
        on=["response_id", "session_id"],
        validate="one_to_one",
    )
    if len(frame) != 35_072 or frame.isna().any().any():
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: OOF coverage")
    y = frame["is_correct"].to_numpy(dtype=np.int8)
    raw_probability = frame["m1_prime_probability"].to_numpy(dtype=np.float64)
    cal_probability = frame["m1_cal_probability"].to_numpy(dtype=np.float64)
    if not np.isfinite(raw_probability).all() or not np.isfinite(cal_probability).all():
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: non-finite OOF")

    raw_metrics = {
        "log_loss": float(log_loss(y, raw_probability)),
        "auc": float(roc_auc_score(y, raw_probability)),
    }
    cal_metrics = {
        "log_loss": float(log_loss(y, cal_probability)),
        "auc": float(roc_auc_score(y, cal_probability)),
        **calibration_summary(y, cal_probability),
    }
    cal_metrics["delta_log_loss"] = cal_metrics["log_loss"] - raw_metrics["log_loss"]
    for key, expected in HISTORICAL_M1_PRIME.items():
        if abs(raw_metrics[key] - expected) > 1e-6:
            raise RuntimeError(
                f"BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: parent {key} drift"
            )
    for key, tolerance in PHASE_A_TOLERANCE.items():
        if abs(cal_metrics[key] - HISTORICAL_M1_CAL[key]) > tolerance:
            raise RuntimeError(
                f"BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: calibrated {key} drift"
            )
    if not cal_metrics["log_loss"] < raw_metrics["log_loss"]:
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: LL not improved")

    folds = cal_record.get("comparison", {}).get("folds", [])
    inner_iters = [
        int(value)
        for fold in folds
        for value in fold.get("inner_base_n_iter", [])
    ]
    if len(folds) != 5 or sorted(int(fold.get("fold", -1)) for fold in folds) != list(range(5)):
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: incomplete folds")
    if len(inner_iters) != 25 or any(value <= 0 or value >= 500 for value in inner_iters):
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: inner fit convergence")
    objective_range = (
        frame.assign(probability=cal_probability)
        .groupby("session_id")["probability"]
        .agg(lambda values: float(values.max() - values.min()))
        .max()
    )
    if float(objective_range) != 0.0:
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: objective exclusion")
    if parent_record.get("objective_information_present") is not False or cal_record.get(
        "objective_information_present"
    ) is not False:
        raise RuntimeError("BLOCKED_M1_CAL_NUMERICAL_RECONSTITUTION: objective provenance")
    return {
        "status": "PASS",
        "historical_parent_sha256": HISTORICAL_PARENT_SHA256,
        "regenerated_parent_sha256": RECONSTITUTED_PARENT_SHA256,
        "reconstituted_m1_cal_config_sha256": RECONSTITUTED_M1_CAL_CONFIG_SHA256,
        "historical_parent_byte_identity": "NOT_REPRODUCED",
        "regenerated_parent_numerical_identity": "PASS",
        "m1_prime": raw_metrics,
        "m1_cal": cal_metrics,
        "m1_cal_oof_sha256": sha256_file(m1_cal_oof_path),
        "inner_base_n_iter": inner_iters,
        "objective_information_present": False,
        "maximum_within_session_probability_range": float(objective_range),
    }


def prepare_training_frame(
    index_path: Path,
    folds_path: Path,
    session_features_path: Path,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    index = pd.read_csv(index_path, dtype={"response_id": str, "session_id": str})
    folds = pd.read_csv(folds_path, dtype={"session_id": str})
    features = pd.read_csv(session_features_path, dtype={"session_id": str})
    if not index["response_id"].is_unique or not folds["session_id"].is_unique:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: duplicate index/fold identity")
    if not features["session_id"].is_unique:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: duplicate session features")
    ordinary = runtime_main.ORDINARY_COLUMNS
    frame = index[["response_id", "session_id", "is_correct"]].merge(
        features[["session_id", *ordinary]],
        on="session_id",
        validate="many_to_one",
        sort=False,
    )
    if len(frame) != 35_072 or frame["session_id"].nunique() != 22_821:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: training frame coverage")
    return frame, folds


def build_text_matrix(
    frame: pd.DataFrame,
    transcript_roots: list[Path],
    parent: Any,
    config: dict[str, Any],
    batch_size: int,
) -> sparse.csr_matrix:
    sessions = sorted(frame["session_id"].unique())
    paths = parent.transcript_path_map(transcript_roots)
    if set(paths) != set(sessions):
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: transcript coverage mismatch")
    vectorizer = parent.make_vectorizer(config["semantic_representation"])
    session_matrix = parent.build_session_text_matrix(
        sessions,
        paths,
        vectorizer,
        config["text_serialization"]["role_markers"],
        batch_size,
    )
    row_by_session = {session_id: index for index, session_id in enumerate(sessions)}
    response_rows = np.fromiter(
        (row_by_session[session_id] for session_id in frame["session_id"]),
        dtype=np.int32,
        count=len(frame),
    )
    return session_matrix[response_rows].tocsr()


def fit_deployment(
    frame: pd.DataFrame,
    text_matrix: sparse.csr_matrix,
    parent: Any,
    m1_cal: Any,
    config: dict[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any], Any, Any, sparse.csr_matrix]:
    y = frame["is_correct"].to_numpy(dtype=np.int8)
    groups = frame["session_id"].to_numpy()
    structural_raw = frame[runtime_main.ORDINARY_COLUMNS].to_numpy(dtype=np.float64)

    # Phase B: fit the separately frozen full-training base before constructing
    # the deployment crossfit calibration map.
    medians = np.nanmedian(structural_raw, axis=0)
    imputed = structural_raw.copy()
    missing = np.where(np.isnan(imputed))
    imputed[missing] = medians[missing[1]]
    scaler = StandardScaler()
    standardized = scaler.fit_transform(imputed).astype(np.float32)
    design = sparse.hstack(
        [text_matrix, sparse.csr_matrix(standardized)], format="csr", dtype=np.float32
    )
    classifier = parent.make_classifier(config["base_classifier"])
    classifier.fit(design, y)
    full_n_iter = int(np.asarray(classifier.n_iter_).max())
    if full_n_iter <= 0 or full_n_iter >= 500:
        raise RuntimeError("BLOCKED_FULL_FIT: base convergence")
    coefficient = np.asarray(classifier.coef_[0])
    if coefficient.shape != (runtime_main.N_HASH_FEATURES + 4,):
        raise RuntimeError("BLOCKED_FULL_FIT: coefficient shape")

    # Phase C: generate exactly one grouped crossfit raw score per response and
    # fit the single frozen deployment Platt map.
    split_config = config["inner_crossfit"]
    splitter = StratifiedGroupKFold(
        n_splits=int(split_config["n_splits"]),
        shuffle=bool(split_config["shuffle"]),
        random_state=int(split_config["random_state"]),
    )
    crossfit_score = np.full(len(frame), np.nan, dtype=np.float64)
    assignment = np.full(len(frame), -1, dtype=np.int8)
    fold_records = []
    for fold, (train_index, validation_index) in enumerate(
        splitter.split(np.zeros(len(frame), dtype=np.int8), y, groups=groups)
    ):
        if set(groups[train_index]) & set(groups[validation_index]):
            raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: session leakage")
        score, n_iter = m1_cal.fit_structured_blocks(
            parent,
            text_matrix,
            structural_raw,
            y,
            train_index,
            validation_index,
            config["base_classifier"],
        )
        if n_iter <= 0 or n_iter >= 500:
            raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: base convergence")
        crossfit_score[validation_index] = score
        assignment[validation_index] = fold
        fold_records.append(
            {
                "fold": fold,
                "responses": int(len(validation_index)),
                "sessions": int(pd.Series(groups[validation_index]).nunique()),
                "base_n_iter": int(n_iter),
            }
        )
    if not np.isfinite(crossfit_score).all() or np.any(assignment < 0):
        raise RuntimeError("BLOCKED_DEPLOYMENT_CROSSFIT: incomplete raw scores")
    calibrator = m1_cal.make_calibrator(config["calibrator"])
    calibrator.fit(crossfit_score.reshape(-1, 1), y)
    slope = float(calibrator.coef_[0, 0])
    cal_intercept = float(calibrator.intercept_[0])
    if not np.isfinite([slope, cal_intercept]).all() or slope <= 0:
        raise RuntimeError("BLOCKED_CALIBRATOR_FIT: invalid Platt geometry")

    state = {
        "text_coef": coefficient[: runtime_main.N_HASH_FEATURES].copy(),
        "structural_coef": coefficient[runtime_main.N_HASH_FEATURES :].copy(),
        "base_intercept": np.asarray(classifier.intercept_).reshape(1).copy(),
        "structural_medians": np.asarray(medians).copy(),
        "scaler_mean": np.asarray(scaler.mean_).copy(),
        "scaler_scale": np.asarray(scaler.scale_).copy(),
        "platt_slope": np.asarray([slope], dtype=np.float64),
        "platt_intercept": np.asarray([cal_intercept], dtype=np.float64),
    }
    direct_raw = np.asarray(classifier.decision_function(design), dtype=np.float64)
    stored_raw, _, stored_probability = runtime_main.predict_blocks(
        text_matrix, structural_raw, state
    )
    direct_probability = calibrator.predict_proba(direct_raw.reshape(-1, 1))[:, 1]
    raw_difference = float(np.max(np.abs(direct_raw - stored_raw)))
    probability_difference = float(
        np.max(np.abs(direct_probability - stored_probability))
    )
    if raw_difference > 1e-12 or probability_difference > 1e-12:
        raise RuntimeError("BLOCKED_FITTED_STATE_EQUIVALENCE: numerical state")

    crossfit_probability = calibrator.predict_proba(
        crossfit_score.reshape(-1, 1)
    )[:, 1]
    assignment_payload = pd.DataFrame(
        {"response_id": frame["response_id"], "fold": assignment}
    ).to_csv(index=False, lineterminator="\n").encode("utf-8")
    summary = {
        "rows": int(len(frame)),
        "sessions": int(frame["session_id"].nunique()),
        "feature_dimension": int(design.shape[1]),
        "coefficient_shape": list(classifier.coef_.shape),
        "coefficient_dtype": str(classifier.coef_.dtype),
        "base_intercept": float(classifier.intercept_[0]),
        "full_base_n_iter": full_n_iter,
        "crossfit_folds": fold_records,
        "crossfit_assignment_sha256": sha256_bytes(assignment_payload),
        "crossfit_raw_score_sha256": sha256_bytes(
            np.asarray(crossfit_score, dtype="<f8").tobytes()
        ),
        "crossfit_log_loss": float(log_loss(y, crossfit_probability)),
        "crossfit_auc": float(roc_auc_score(y, crossfit_probability)),
        "platt_slope": slope,
        "platt_intercept": cal_intercept,
        "platt_n_iter": int(np.asarray(calibrator.n_iter_).max()),
        "stored_state_raw_max_abs_difference": raw_difference,
        "stored_state_probability_max_abs_difference": probability_difference,
    }
    return state, summary, classifier, calibrator, design


def _copy_fixture_transcript(session_id: str, roots: Iterable[Path], destination: Path) -> None:
    matches = [root / f"{session_id}.csv" for root in roots]
    matches = [path for path in matches if path.is_file()]
    if len(matches) != 1:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture transcript identity")
    shutil.copyfile(matches[0], destination)


def build_fixture(
    output_dir: Path,
    raw_features_path: Path,
    transcript_roots: list[Path],
    frame: pd.DataFrame,
    design: sparse.csr_matrix,
    classifier: Any,
    calibrator: Any,
) -> dict[str, Any]:
    fixture_root = output_dir / "fixture"
    data_dir = fixture_root / "data"
    transcript_dir = data_dir / "test_transcripts"
    transcript_dir.mkdir(parents=True, exist_ok=True)
    session_table = frame.drop_duplicates("session_id").sort_values(
        ["n_student_words", "n_turns", "session_id"], na_position="first"
    )
    positions = np.linspace(0, len(session_table) - 1, num=64, dtype=int)
    selected_sessions = session_table.iloc[np.unique(positions)]["session_id"].tolist()
    raw_features = pd.read_csv(
        raw_features_path, dtype={"response_id": str, "session_id": str}
    )
    fixture_features = raw_features.loc[
        raw_features["session_id"].isin(selected_sessions)
    ].copy()
    if fixture_features.empty or not fixture_features["response_id"].is_unique:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture identities")
    fixture_features.to_csv(
        data_dir / "test_features.csv", index=False, lineterminator="\n"
    )
    pd.DataFrame(
        {
            "response_id": fixture_features["response_id"],
            "probability": np.zeros(len(fixture_features), dtype=np.float64),
        }
    ).to_csv(data_dir / "submission_format.csv", index=False, lineterminator="\n")
    for session_id in selected_sessions:
        _copy_fixture_transcript(
            session_id, transcript_roots, transcript_dir / f"{session_id}.csv"
        )

    row_by_response = pd.Series(np.arange(len(frame)), index=frame["response_id"])
    fixture_rows = row_by_response.loc[fixture_features["response_id"]].to_numpy(
        dtype=np.int64
    )
    direct_raw = np.asarray(
        classifier.decision_function(design[fixture_rows]), dtype=np.float64
    )
    direct_probability = calibrator.predict_proba(
        direct_raw.reshape(-1, 1)
    )[:, 1]
    pd.DataFrame(
        {
            "response_id": fixture_features["response_id"],
            "probability": direct_probability,
            "raw_score": direct_raw,
        }
    ).to_csv(fixture_root / "direct_predictions.csv", index=False, lineterminator="\n")
    return {
        "selection_is_label_free": True,
        "sessions": len(selected_sessions),
        "responses": len(fixture_features),
        "response_order_sha256": sha256_bytes(
            "\n".join(fixture_features["response_id"]).encode("utf-8")
        ),
        "direct_predictions_sha256": sha256_file(
            fixture_root / "direct_predictions.csv"
        ),
    }


def runtime_environment() -> dict[str, Any]:
    return {
        "python": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "scikit_learn": sklearn.__version__,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--index", required=True, type=Path)
    parser.add_argument("--folds", required=True, type=Path)
    parser.add_argument("--m0-session-features", required=True, type=Path)
    parser.add_argument("--m1-prime-oof", required=True, type=Path)
    parser.add_argument("--m1-prime-record", required=True, type=Path)
    parser.add_argument("--m1-cal-oof", required=True, type=Path)
    parser.add_argument("--m1-cal-record", required=True, type=Path)
    parser.add_argument("--train-features", required=True, type=Path)
    parser.add_argument("--train-labels", required=True, type=Path)
    parser.add_argument("--transcripts-root", action="append", required=True, type=Path)
    parser.add_argument("--transcripts-zip", action="append", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--batch-size", type=int, default=128)
    args = parser.parse_args()
    if len(args.transcripts_root) != 2:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: expected two transcript roots")

    baseline = args.repo_root / "external_tests" / "trace_the_ace" / "baselines"
    m1_prime_runner = baseline / "m1_prime" / "train.py"
    m1_prime_config = baseline / "m1_prime" / "config.yaml"
    m1_cal_runner = baseline / "m1_cal" / "train.py"
    m1_cal_config = baseline / "m1_cal" / "config.yaml"
    source_hashes = verify_historical_sources(
        m1_prime_runner, m1_prime_config, m1_cal_runner, m1_cal_config
    )
    input_hashes = verify_raw_inputs(args)
    phase_a = verify_phase_a(
        args.index,
        args.m1_prime_oof,
        args.m1_prime_record,
        args.m1_cal_oof,
        args.m1_cal_record,
    )
    parent = load_module(m1_prime_runner, "submission03_historical_m1_prime")
    m1_cal = load_module(m1_cal_runner, "submission03_historical_m1_cal")
    config = yaml.safe_load(m1_cal_config.read_text(encoding="utf-8"))
    if bool(config["objective_information_allowed"]) or bool(
        config["cca_derived_features_allowed"]
    ):
        raise RuntimeError("BLOCKED_HISTORICAL_IDENTITY: forbidden feature authority")

    frame, _ = prepare_training_frame(
        args.index, args.folds, args.m0_session_features
    )
    text_matrix = build_text_matrix(
        frame, args.transcripts_root, parent, config, args.batch_size
    )
    state, deployment, classifier, calibrator, design = fit_deployment(
        frame, text_matrix, parent, m1_cal, config
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    fixture = build_fixture(
        args.output_dir,
        args.train_features,
        args.transcripts_root,
        frame,
        design,
        classifier,
        calibrator,
    )
    model_bytes = deterministic_npz_bytes(state)
    model_manifest = {
        "schema_version": 1,
        "submission_id": SUBMISSION_ID,
        "objective_information_present": False,
        "source_identity": {
            "repo_base_sha": REPO_BASE_SHA,
            "historical_m1_cal_pr": HISTORICAL_M1_CAL_PR,
            "historical_m1_cal_head": HISTORICAL_M1_CAL_HEAD,
            **source_hashes,
        },
        "parent_identity": {
            "historical_parent_sha256": HISTORICAL_PARENT_SHA256,
            "regenerated_parent_sha256": RECONSTITUTED_PARENT_SHA256,
            "historical_parent_byte_identity": "NOT_REPRODUCED",
            "regenerated_parent_numerical_identity": "PASS",
            "engineering_parent_label": "M1_PRIME_RECONSTITUTED",
        },
        "model_specification": {
            "ordinary_covariates": runtime_main.ORDINARY_COLUMNS,
            "hash_features": runtime_main.N_HASH_FEATURES,
            "text_serialization": config["text_serialization"],
            "semantic_representation": config["semantic_representation"],
            "base_classifier": config["base_classifier"],
            "structural_preprocessing": config["structural_preprocessing"],
            "calibrator": config["calibrator"],
        },
        "model_state": {
            "sha256": sha256_bytes(model_bytes),
            "arrays": {
                key: {"shape": list(np.asarray(value).shape), "dtype": str(np.asarray(value).dtype)}
                for key, value in sorted(state.items())
            },
        },
    }
    package_members = {
        "main.py": normalized_source_bytes(HERE / "runtime_main.py"),
        "assets/m1_cal_model.npz": model_bytes,
        "assets/model_manifest.json": json_bytes(model_manifest),
    }
    if set(package_members) != EXPECTED_PACKAGE_MEMBERS:
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: package member set")
    package_path = args.output_dir / PACKAGE_FILENAME
    rebuild_path = args.output_dir / f".{PACKAGE_FILENAME}.rebuild"
    write_deterministic_zip(package_path, package_members)
    write_deterministic_zip(rebuild_path, package_members)
    if package_path.read_bytes() != rebuild_path.read_bytes():
        raise RuntimeError("BLOCKED_RUNTIME_CONTRACT: nondeterministic ZIP rebuild")
    rebuild_path.unlink()

    manifest = {
        "schema_version": 1,
        "submission_id": SUBMISSION_ID,
        "status": "BUILT_PENDING_VERIFICATION",
        "repo_base_sha": REPO_BASE_SHA,
        "historical_m1_cal_pr": HISTORICAL_M1_CAL_PR,
        "historical_m1_cal_head": HISTORICAL_M1_CAL_HEAD,
        "historical_source_sha256": source_hashes,
        "training_input_sha256": input_hashes,
        "phase_a_reconstitution": phase_a,
        "model_specification": model_manifest["model_specification"],
        "deployment_fit_summary": deployment,
        "fitted_state": model_manifest["model_state"],
        "runtime_environment": runtime_environment(),
        "fixture": fixture,
        "package": {
            "filename": PACKAGE_FILENAME,
            "byte_size": package_path.stat().st_size,
            "sha256": sha256_file(package_path),
            "member_sha256": {
                name: sha256_bytes(value) for name, value in sorted(package_members.items())
            },
            "deterministic_rebuild": "PASS",
        },
        "verification": None,
        "authority": INITIAL_AUTHORITY,
    }
    (args.output_dir / MANIFEST_FILENAME).write_bytes(json_bytes(manifest))
    print(json.dumps({"status": manifest["status"], "zip": str(package_path), "sha256": manifest["package"]["sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
