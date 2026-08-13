"""Build the exact Trace the Ace Submission 02 M0 engineering control.

This script performs identity and Phase-0 gates before fitting.  It writes all
competition-derived assets and predictions only to the caller-supplied local
output directory; none are repository artifacts.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import platform
import sys
import zipfile
from pathlib import Path
from typing import Any, Iterable, Mapping

import numpy as np
import pandas as pd
import scipy
import sklearn
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import runtime_main  # noqa: E402


SUBMISSION_ID = "S2_M0_CONTROL"
REPO_BASE_SHA = "4d02c557e234772ed28319fd4cf67098341318fd"
HISTORICAL_M0_PR = 24
HISTORICAL_M0_HEAD = "feffb83ce92d4e4688b982be536e81cf026d3068"
EXPECTED_M0_TRAIN_SHA256 = (
    "5c36a4dfaf528fac3e86face05dda13eecebbaeaf9b2ebdc6e9bc80e50009e57"
)
EXPECTED_M0_CONFIG_SHA256 = (
    "b6431c9e7cacbcdb265ed319f4a15f6e32d5a267051a0065f0fc5bf703a152f6"
)
EXPECTED_INDEX_SHA256 = (
    "296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60"
)
EXPECTED_FOLD_SHA256 = (
    "014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6"
)
EXPECTED_INPUT_HASHES = {
    "train_features": "71bea3abb76a1cff5e1eaa75b9cbcfaf26d0419f6274b83a199ed520047a5063",
    "train_labels": "d98ee4389e5cde3f66d6d15b7b574261024a80e405958eca333d3c1921fd65b9",
    "train_transcripts_part1": "f8172da9547286f7bd09967571c56626f63e39fb6e24ffcdf475071db57836b7",
    "train_transcripts_part2": "22ff3c12b599ec82489d9cb546cc2dd2322a8e77dc812ea15352f4830f24cd82",
    "submission_01_zip": "48d4d2f1db873e77a5c185cce6649d1425090ad710767b7541eb225035c93aec",
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
    "reference_auc": 0.5473456079616892,
    "n_student_words_coef": 0.06836157563364859,
    "numeric_turns_per_word_coef": -0.21051638172143497,
    "digit_chars_per_word_coef": 0.07569770194075158,
    "pooled_log_loss": 0.6045154928170339,
    "pooled_auc": 0.5566948897220998,
    "brier_score": 0.207221464432313,
    "ece_10_equal_width": 0.004379974720982257,
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
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


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
                array_buffer,
                np.asarray(arrays[name]),
                allow_pickle=False,
            )
            archive.writestr(
                _zip_info(f"{name}.npy"), array_buffer.getvalue(), compresslevel=9
            )
    return output.getvalue()


def verify_submission_01(path: Path) -> dict[str, str]:
    verify_hash(path, EXPECTED_INPUT_HASHES["submission_01_zip"], "Submission 01 ZIP")
    observed: dict[str, str] = {}
    with zipfile.ZipFile(path) as archive:
        files = {
            info.filename
            for info in archive.infolist()
            if not info.is_dir()
        }
        if files != set(EXPECTED_SUBMISSION_01_MEMBERS):
            raise RuntimeError("BLOCKED_INPUT_IDENTITY: Submission 01 member set mismatch")
        for name, expected in EXPECTED_SUBMISSION_01_MEMBERS.items():
            digest = sha256_bytes(archive.read(name))
            if digest != expected:
                raise RuntimeError(
                    f"BLOCKED_INPUT_IDENTITY: Submission 01 {name} hash mismatch"
                )
            observed[name] = digest
    return observed


def verify_phase0(record_path: Path) -> dict[str, Any]:
    record = json.loads(record_path.read_text(encoding="utf-8"))
    if record.get("status") != "DIAGNOSED_PASS":
        raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: Phase-0 status is not PASS")
    reference = record["reference_reproduction"]
    canonical = record["canonical_oof"]
    calibration = canonical["calibration"]
    coefficients = reference["coefficients"]
    observed = {
        "base_log_loss": reference["base_log_loss"],
        "model_log_loss": reference["model_log_loss"],
        "reference_auc": reference["auc"],
        "n_student_words_coef": coefficients["n_student_words"],
        "numeric_turns_per_word_coef": coefficients["numeric_turns_per_word"],
        "digit_chars_per_word_coef": coefficients["digit_chars_per_word"],
        "pooled_log_loss": canonical["pooled_log_loss"],
        "pooled_auc": canonical["pooled_auc"],
        "brier_score": calibration["brier_score"],
        "ece_10_equal_width": calibration["ece_10_equal_width"],
    }
    non_finite = [
        key for key, value in observed.items() if not np.isfinite(float(value))
    ]
    if non_finite:
        raise RuntimeError(
            "BLOCKED_M0_REPRODUCTION_DRIFT: non-finite Phase-0 metrics "
            f"{non_finite}"
        )
    drift = {
        key: (float(observed[key]), expected)
        for key, expected in EXPECTED_PHASE0.items()
        if abs(float(observed[key]) - expected) > 1e-8
    }
    if drift or not reference.get("reproduced"):
        raise RuntimeError(f"BLOCKED_M0_REPRODUCTION_DRIFT: {drift}")
    if record["identity"]["dataset_index_sha256"] != EXPECTED_INDEX_SHA256:
        raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: index identity mismatch")
    if record["identity"]["fold_artifact_sha256"] != EXPECTED_FOLD_SHA256:
        raise RuntimeError("BLOCKED_M0_REPRODUCTION_DRIFT: fold identity mismatch")
    return record


def verify_phase0_linked_session_features(
    record: Mapping[str, Any], session_features_path: Path
) -> str:
    """Bind the full-fit input to the exact artifact reproduced in Phase 0."""

    expected = record.get("identity", {}).get("session_features_sha256")
    if not isinstance(expected, str):
        raise RuntimeError(
            "BLOCKED_M0_REPRODUCTION_DRIFT: Phase-0 session-feature identity missing"
        )
    if not session_features_path.is_file():
        raise RuntimeError(
            "BLOCKED_INPUT_IDENTITY: missing Phase-0 session-feature artifact"
        )
    observed = sha256_file(session_features_path)
    if observed != expected:
        raise RuntimeError(
            "BLOCKED_M0_REPRODUCTION_DRIFT: session-feature artifact identity mismatch"
        )
    return observed


def verify_raw_response_order(features_path: Path, labels_path: Path) -> None:
    features = pd.read_csv(features_path, dtype={"response_id": str})
    labels = pd.read_csv(labels_path, dtype={"response_id": str})
    if len(features) != 35_072 or len(labels) != 35_072:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: training row count mismatch")
    if not features["response_id"].is_unique or not labels["response_id"].is_unique:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: duplicate training response_id")
    if features["response_id"].tolist() != labels["response_id"].tolist():
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: feature/label response order mismatch")


def load_and_validate_config(path: Path) -> dict[str, Any]:
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    expected = {
        "min_student_words": 100,
        "features": runtime_main.FEATURE_COLUMNS,
        "word_regex": r"[a-z0-9]+(?:'[a-z]+)?",
        "digit_regex": r"\d",
    }
    for key, value in expected.items():
        if config.get(key) != value:
            raise RuntimeError(f"BLOCKED_FULL_FIT: frozen M0 {key} mismatch")
    if config["reference_model"] != {
        "scaler": "StandardScaler",
        "classifier": "LogisticRegression",
        "max_iter": 1000,
    }:
        raise RuntimeError("BLOCKED_FULL_FIT: frozen M0 model configuration mismatch")
    return config


def fit_full_model(
    index_path: Path,
    session_features_path: Path,
    config: Mapping[str, Any],
) -> tuple[dict[str, np.ndarray], dict[str, Any], Any, StandardScaler, pd.DataFrame]:
    index = pd.read_csv(
        index_path, dtype={"response_id": str, "session_id": str}
    )
    session_features = pd.read_csv(
        session_features_path, dtype={"session_id": str}
    )
    required = {"session_id", *runtime_main.FEATURE_COLUMNS}
    if not required.issubset(session_features.columns):
        raise RuntimeError("BLOCKED_FULL_FIT: session feature schema mismatch")
    if not session_features["session_id"].is_unique:
        raise RuntimeError("BLOCKED_FULL_FIT: duplicate session feature identity")
    frame = index.merge(
        session_features[["session_id", *runtime_main.FEATURE_COLUMNS]],
        on="session_id",
        how="left",
        validate="many_to_one",
    )
    if frame[runtime_main.FEATURE_COLUMNS].isna().all(axis=1).any():
        # A true zero-word row has all three NaN, but its session must still exist.
        missing_sessions = set(index["session_id"]) - set(session_features["session_id"])
        if missing_sessions:
            raise RuntimeError("BLOCKED_FULL_FIT: session feature coverage mismatch")

    minimum = int(config["min_student_words"])
    eligible = frame["n_student_words"].ge(minimum)
    training = frame.loc[eligible]
    if training.empty:
        raise RuntimeError("BLOCKED_FULL_FIT: no eligible training responses")
    features = runtime_main.FEATURE_COLUMNS
    medians = training[features].median()
    imputed = training[features].fillna(medians).to_numpy(dtype=np.float64)
    scaler = StandardScaler()
    standardized = scaler.fit_transform(imputed)
    classifier = LogisticRegression(max_iter=1000)
    classifier.fit(standardized, training["is_correct"])

    coefficients = classifier.coef_[0].astype(np.float64, copy=True)
    state = {
        "coef": coefficients,
        "eligible_base_rate": np.asarray(
            [float(training["is_correct"].mean())], dtype=np.float64
        ),
        "feature_median": medians.to_numpy(dtype=np.float64),
        "intercept": classifier.intercept_.astype(np.float64, copy=True),
        "min_student_words": np.asarray([minimum], dtype=np.int64),
        "scaler_mean": scaler.mean_.astype(np.float64, copy=True),
        "scaler_scale": scaler.scale_.astype(np.float64, copy=True),
    }

    full_feature_matrix = frame[features].to_numpy(dtype=np.float64)
    direct_numpy = runtime_main.predict_feature_matrix(full_feature_matrix, state)
    expected = np.full(
        len(frame), float(state["eligible_base_rate"][0]), dtype=np.float64
    )
    expected[eligible.to_numpy()] = classifier.predict_proba(standardized)[:, 1]
    state_equivalence = float(np.max(np.abs(expected - direct_numpy)))
    if state_equivalence > 1e-12:
        raise RuntimeError(
            "BLOCKED_FULL_FIT: sklearn/direct numerical state mismatch "
            f"{state_equivalence}"
        )

    eligible_sessions = session_features["n_student_words"].ge(minimum)
    summary = {
        "eligible_responses": int(eligible.sum()),
        "eligible_sessions": int(eligible_sessions.sum()),
        "quiet_responses": int((~eligible).sum()),
        "quiet_sessions": int((~eligible_sessions).sum()),
        "eligible_training_base_rate": float(state["eligible_base_rate"][0]),
        "feature_medians": state["feature_median"].tolist(),
        "scaler_mean": state["scaler_mean"].tolist(),
        "scaler_scale": state["scaler_scale"].tolist(),
        "coefficients": coefficients.tolist(),
        "intercept": float(state["intercept"][0]),
        "n_iter": classifier.n_iter_.astype(int).tolist(),
        "sklearn_direct_max_abs_difference": state_equivalence,
    }
    return state, summary, classifier, scaler, frame


def _read_transcript_members(paths: Iterable[Path]) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    for path in paths:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".csv"):
                    continue
                session_id = Path(info.filename).stem
                if session_id in members:
                    raise RuntimeError("BLOCKED_INPUT_IDENTITY: duplicate transcript session")
                members[session_id] = archive.read(info)
    return members


def build_fixture(
    output_dir: Path,
    raw_features_path: Path,
    transcript_paths: list[Path],
    session_features_path: Path,
    frame: pd.DataFrame,
    state: Mapping[str, np.ndarray],
    classifier: LogisticRegression,
    scaler: StandardScaler,
) -> dict[str, Any]:
    fixture_root = output_dir / "fixture"
    data_dir = fixture_root / "data"
    transcript_dir = data_dir / "test_transcripts"
    transcript_dir.mkdir(parents=True, exist_ok=True)

    session_features = pd.read_csv(
        session_features_path, dtype={"session_id": str}
    )
    eligible_sessions = sorted(
        session_features.loc[
            session_features["n_student_words"].ge(100), "session_id"
        ].tolist()
    )[:16]
    quiet_sessions = sorted(
        session_features.loc[
            ~session_features["n_student_words"].ge(100), "session_id"
        ].tolist()
    )[:16]
    selected_sessions = eligible_sessions + quiet_sessions
    if len(eligible_sessions) != 16 or len(quiet_sessions) != 16:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture strata unavailable")

    raw_features = pd.read_csv(
        raw_features_path, dtype={"response_id": str, "session_id": str}
    )
    fixture_features = raw_features.loc[
        raw_features["session_id"].isin(selected_sessions)
    ].copy()
    if fixture_features.empty or not fixture_features["response_id"].is_unique:
        raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: invalid fixture identities")
    fixture_features.to_csv(
        data_dir / "test_features.csv", index=False, lineterminator="\n"
    )
    pd.DataFrame(
        {
            "response_id": fixture_features["response_id"],
            "probability": np.zeros(len(fixture_features), dtype=np.float64),
        }
    ).to_csv(data_dir / "submission_format.csv", index=False, lineterminator="\n")

    members = _read_transcript_members(transcript_paths)
    for session_id in selected_sessions:
        if session_id not in members:
            raise RuntimeError("BLOCKED_PACKAGED_EQUIVALENCE: fixture transcript missing")
        (transcript_dir / f"{session_id}.csv").write_bytes(members[session_id])

    selected_frame = frame.set_index("response_id").loc[
        fixture_features["response_id"].tolist()
    ]
    feature_matrix = selected_frame[runtime_main.FEATURE_COLUMNS].to_numpy(
        dtype=np.float64
    )
    minimum = int(np.asarray(state["min_student_words"])[0])
    eligible = feature_matrix[:, 0] >= minimum
    expected = np.full(
        len(feature_matrix), float(np.asarray(state["eligible_base_rate"])[0])
    )
    if np.any(eligible):
        eligible_matrix = feature_matrix[eligible].copy()
        medians = np.asarray(state["feature_median"])
        missing = np.where(np.isnan(eligible_matrix))
        eligible_matrix[missing] = medians[missing[1]]
        expected[eligible] = classifier.predict_proba(
            scaler.transform(eligible_matrix)
        )[:, 1]
    pd.DataFrame(
        {
            "response_id": fixture_features["response_id"],
            "probability": expected,
        }
    ).to_csv(fixture_root / "direct_predictions.csv", index=False, lineterminator="\n")
    return {
        "sessions": len(selected_sessions),
        "eligible_sessions": len(eligible_sessions),
        "quiet_sessions": len(quiet_sessions),
        "responses": len(fixture_features),
        "response_id_order_sha256": sha256_bytes(
            "\n".join(fixture_features["response_id"]).encode("utf-8")
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
        "pyyaml": yaml.__version__,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--features", required=True, type=Path)
    parser.add_argument("--labels", required=True, type=Path)
    parser.add_argument("--transcripts-zip", action="append", required=True, type=Path)
    parser.add_argument("--submission-01", required=True, type=Path)
    parser.add_argument("--index", required=True, type=Path)
    parser.add_argument("--folds", required=True, type=Path)
    parser.add_argument("--session-features", required=True, type=Path)
    parser.add_argument("--phase0-record", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    if len(args.transcripts_zip) != 2:
        raise RuntimeError("BLOCKED_INPUT_IDENTITY: expected exactly two transcript ZIPs")
    m0_dir = args.repo_root / "external_tests" / "trace_the_ace" / "baselines" / "m0"
    train_path = m0_dir / "train.py"
    config_path = m0_dir / "config.yaml"
    verify_hash(train_path, EXPECTED_M0_TRAIN_SHA256, "historical M0 train.py")
    verify_hash(config_path, EXPECTED_M0_CONFIG_SHA256, "historical M0 config.yaml")
    verify_hash(args.features, EXPECTED_INPUT_HASHES["train_features"], "train features")
    verify_hash(args.labels, EXPECTED_INPUT_HASHES["train_labels"], "train labels")
    for path, key in zip(
        args.transcripts_zip,
        ("train_transcripts_part1", "train_transcripts_part2"),
    ):
        verify_hash(path, EXPECTED_INPUT_HASHES[key], key)
    submission_01_members = verify_submission_01(args.submission_01)
    verify_hash(args.index, EXPECTED_INDEX_SHA256, "canonical index")
    verify_hash(args.folds, EXPECTED_FOLD_SHA256, "canonical folds")
    verify_raw_response_order(args.features, args.labels)
    phase0 = verify_phase0(args.phase0_record)
    session_features_sha256 = verify_phase0_linked_session_features(
        phase0, args.session_features
    )
    config = load_and_validate_config(config_path)

    try:
        state, fit_summary, classifier, scaler, frame = fit_full_model(
            args.index, args.session_features, config
        )
    except RuntimeError:
        raise
    except Exception as error:
        raise RuntimeError(f"BLOCKED_FULL_FIT: {error}") from error

    args.output_dir.mkdir(parents=True, exist_ok=True)
    model_bytes = deterministic_npz_bytes(state)
    model_sha256 = sha256_bytes(model_bytes)
    environment = runtime_environment()
    model_manifest = {
        "schema_version": 1,
        "submission_id": SUBMISSION_ID,
        "status": "BUILT_PENDING_VERIFICATION",
        "feature_definition": {
            "eligibility": "n_student_words >= 100",
            "features": runtime_main.FEATURE_COLUMNS,
            "definitions": {
                "n_student_words": (
                    "count of word_regex matches over all student utterances "
                    "in the session"
                ),
                "numeric_turns_per_word": (
                    "number of student turns containing at least one digit "
                    "/ n_student_words"
                ),
                "digit_chars_per_word": (
                    "total digit characters in student utterances "
                    "/ n_student_words"
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
        },
        "fit_summary": fit_summary,
        "fitted_state": {key: np.asarray(value).tolist() for key, value in state.items()},
        "runtime_environment": environment,
        "source_identity": {
            "repo_base_sha": REPO_BASE_SHA,
            "historical_m0_pr": HISTORICAL_M0_PR,
            "historical_m0_head": HISTORICAL_M0_HEAD,
            "m0_train_sha256": EXPECTED_M0_TRAIN_SHA256,
            "m0_config_sha256": EXPECTED_M0_CONFIG_SHA256,
        },
    }
    model_manifest_bytes = json_bytes(model_manifest)
    runtime_bytes = normalized_source_bytes(HERE / "runtime_main.py")
    package_members = {
        "main.py": runtime_bytes,
        "assets/m0_model.npz": model_bytes,
        "assets/model_manifest.json": model_manifest_bytes,
    }
    package_path = args.output_dir / "trace_the_ace_submission_02_m0_control.zip"
    write_deterministic_zip(package_path, package_members)
    package_member_hashes = {
        name: sha256_bytes(payload) for name, payload in package_members.items()
    }

    fixture = build_fixture(
        args.output_dir,
        args.features,
        args.transcripts_zip,
        args.session_features,
        frame,
        state,
        classifier,
        scaler,
    )

    manifest = {
        "schema_version": 1,
        "submission_id": SUBMISSION_ID,
        "status": "BUILT_PENDING_VERIFICATION",
        "repo_base_sha": REPO_BASE_SHA,
        "historical_m0_pr": HISTORICAL_M0_PR,
        "historical_m0_head": HISTORICAL_M0_HEAD,
        "training_input_sha256": {
            **{
                key: value
                for key, value in EXPECTED_INPUT_HASHES.items()
                if key != "submission_01_zip"
            },
            "submission_01_zip": EXPECTED_INPUT_HASHES["submission_01_zip"],
            "submission_01_members": submission_01_members,
            "canonical_index": EXPECTED_INDEX_SHA256,
            "regenerated_folds": EXPECTED_FOLD_SHA256,
            "session_features": session_features_sha256,
        },
        "phase0_reproduction": {
            "status": "PASS",
            "identity": phase0["identity"],
            "reference": phase0["reference_reproduction"],
            "canonical_oof": phase0["canonical_oof"],
        },
        "feature_definition": model_manifest["feature_definition"],
        "deployment_fit_summary": fit_summary,
        "fitted_numerical_state": model_manifest["fitted_state"],
        "runtime_environment": environment,
        "fixture": fixture,
        "package": {
            "filename": package_path.name,
            "byte_size": package_path.stat().st_size,
            "sha256": sha256_file(package_path),
            "member_sha256": package_member_hashes,
        },
        "verification": {
            "direct_packaged_max_abs_difference": None,
            "deterministic_submission_csv_sha256": None,
            "checks": "PENDING",
        },
        "authority": {
            "engineering_control_prepared": False,
            "competition_submission_executed": False,
            "cca_authority_changed": False,
            "research_diagnosis_changed": False,
            "submission_03_authorized": False,
        },
    }
    manifest_path = args.output_dir / "submission_02_m0_manifest.json"
    manifest_path.write_bytes(json_bytes(manifest))
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
