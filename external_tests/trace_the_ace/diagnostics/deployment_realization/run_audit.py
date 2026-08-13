#!/usr/bin/env python3
"""Phase-0-only gate for the Trace-the-Ace deployment-realization audit.

This program intentionally cannot fit a model, generate a split, extract a
score, compare probabilities, or read public/hidden test data. It verifies the
allowlisted training corpus, frozen Submission 01 package, and research-source
identities. Required primary comparison objects must be supplied explicitly;
omission or identity failure produces the contract's fail-closed state.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


STOP = "BLOCKED_MISSING_INPUT"
D_DEPLOYMENT = "UNIDENTIFIED_INPUT_BLOCKED"
PARENT_COMMIT = "4d02c557e234772ed28319fd4cf67098341318fd"

EXPECTED_INPUTS = {
    "features": (
        "train_features_TMQTWsB.csv",
        "71bea3abb76a1cff5e1eaa75b9cbcfaf26d0419f6274b83a199ed520047a5063",
    ),
    "labels": (
        "train_labels_44ujmj2.csv",
        "d98ee4389e5cde3f66d6d15b7b574261024a80e405958eca333d3c1921fd65b9",
    ),
    "transcripts_part1": (
        "train_transcripts_part1.zip",
        "f8172da9547286f7bd09967571c56626f63e39fb6e24ffcdf475071db57836b7",
    ),
    "transcripts_part2": (
        "train_transcripts_part2.zip",
        "22ff3c12b599ec82489d9cb546cc2dd2322a8e77dc812ea15352f4830f24cd82",
    ),
    "submission_zip": (
        "trace_the_ace_submission_01_m2s.zip",
        "48d4d2f1db873e77a5c185cce6649d1425090ad710767b7541eb225035c93aec",
    ),
    "glove_archive": (
        "glove.2024.wikigiga.50d.zip",
        "afa5e258ee38272db6394547c4b075ecbb7b2164e98542c8d1237b6029b35a65",
    ),
}

EXPECTED_GLOVE_MEMBER = {
    "name": "wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt",
    "size_bytes": 842192707,
    "sha256": "16c4253cb9a19045dcdc758b6a1eda52d3c37b894dea2601a45046b4300a8d10",
}

EXPECTED_SUBMISSION_MEMBERS = {
    "main.py": "28c7f515e6a388a03b4eadca0b083fb3577bd05c8d530341116a065ada30941c",
    "assets/model.npz": "a5af72f06930ac2a5c43a69d2c5a0b8ffc1765631b18e55afa7dd91cbf120742",
    "assets/glove_filtered.npz": "2af970dfabbcb70fa8247d646532e1b420afa09f1d02fe545fca317d6bf3c17b",
    "assets/model_manifest.json": "5c555adcb7295bc538802d473c6945dc3c3b6f4196dedccb93c8ad995ccffee2",
}

EXPECTED_RESEARCH_FILES = {
    "external_tests/trace_the_ace/baselines/m0/train.py":
        "5c36a4dfaf528fac3e86face05dda13eecebbaeaf9b2ebdc6e9bc80e50009e57",
    "external_tests/trace_the_ace/baselines/m1_prime/train.py":
        "e8134bf4ec8d18aca74c6fb5e7bcf3d02ab327f0f96115e5b566474cf500f208",
    "external_tests/trace_the_ace/baselines/m2/train.py":
        "c693b23a9d09a73bfadbfb33476b9fe8c16a3d21d24d76ded74e0b02a71d77f7",
    "external_tests/trace_the_ace/baselines/m2_sem/aggregate.py":
        "7d958aac68461e598ff6c6c428cdf282524f2d9b609f8fc7b86eb8e85c67f59d",
    "external_tests/trace_the_ace/baselines/m2_sem/checkpoint_arm.py":
        "d3c4efb5c08f3b89ea241b8921a83d7e96bd7b3d46f298a1c837a7c1a60ffc8e",
    "external_tests/trace_the_ace/baselines/m2_sem/config.yaml":
        "6953bdfaf77bbe60b1bf7214626150d74e5e4911283a7250c1254d93695bae2e",
    "external_tests/trace_the_ace/baselines/m2_sem/feature_stage.py":
        "231d89f8d5250b0b01b0f34697233eafd86c34ee086199c6f9a6071c4a7e0132",
    "external_tests/trace_the_ace/data/build_index.py":
        "ae3da3fcaafdf137dec5941b012ea200dc450aa73edcc56ba4e6e4e90c694090",
    "external_tests/trace_the_ace/validation/make_folds.py":
        "7ced032076ac74e4b0bfa7d8071a0034335ff67a729f622509142189b412c717",
}

REQUIRED_PRIMARY_OBJECTS = {
    "historical_m2s_oof":
        "64679b828af9737e5245dd1348f2c8e0cf5a38e013eefaee02266de7277e096f",
    "historical_outer_folds":
        "014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6",
    "deployment_crossfit_scores": None,
    "deployment_crossfit_fitting_implementation": None,
    "deployment_crossfit_platt_geometry": None,
}

FORBIDDEN_PATH_TERMS = (
    "hidden_test",
    "hidden-test",
    "public_test",
    "public-test",
    "leaderboard",
    "submission_format",
    "test_features",
    "test_transcripts",
)


@dataclass(frozen=True)
class ObjectCheck:
    object_id: str
    path: str | None
    status: str
    expected_sha256: str | None
    observed_sha256: str | None

    def as_dict(self) -> dict[str, str | None]:
        return {
            "expected_sha256": self.expected_sha256,
            "observed_sha256": self.observed_sha256,
            "path": self.path,
            "status": self.status,
        }


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_stream(stream: object, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    while True:
        chunk = stream.read(chunk_size)
        if not chunk:
            return digest.hexdigest()
        digest.update(chunk)


def ensure_allowlisted_path(path: Path) -> None:
    normalized = str(path).replace("\\", "/").lower()
    if any(term in normalized for term in FORBIDDEN_PATH_TERMS):
        raise ValueError(f"public/hidden-test path is forbidden: {path}")


def check_object(
    object_id: str,
    path: Path | None,
    expected_sha256: str | None,
) -> ObjectCheck:
    if path is None:
        return ObjectCheck(object_id, None, "ABSENT", expected_sha256, None)
    ensure_allowlisted_path(path)
    if not path.is_file():
        return ObjectCheck(object_id, str(path), "ABSENT", expected_sha256, None)
    observed = sha256_file(path)
    if expected_sha256 is None:
        return ObjectCheck(
            object_id,
            str(path),
            "PRESENT_IDENTITY_UNCONSTITUTED",
            None,
            observed,
        )
    if expected_sha256 is not None and observed != expected_sha256:
        return ObjectCheck(
            object_id, str(path), "HASH_MISMATCH", expected_sha256, observed
        )
    return ObjectCheck(object_id, str(path), "PRESENT_HASH_VALID", expected_sha256, observed)


def read_csv_identity(
    path: Path,
    *,
    id_column: str = "response_id",
    session_column: str | None = None,
) -> tuple[list[str], set[str]]:
    response_ids: list[str] = []
    sessions: set[str] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = set(reader.fieldnames or ())
        if id_column not in fields:
            raise ValueError(f"{path.name} lacks required column {id_column}")
        if session_column is not None and session_column not in fields:
            raise ValueError(f"{path.name} lacks required column {session_column}")
        for row in reader:
            response_ids.append(row[id_column])
            if session_column is not None:
                sessions.add(row[session_column])
    if len(response_ids) != len(set(response_ids)):
        raise ValueError(f"{path.name} has duplicate {id_column} values")
    return response_ids, sessions


def validate_training_alignment(features: Path, labels: Path) -> dict[str, object]:
    feature_ids, sessions = read_csv_identity(
        features, id_column="response_id", session_column="session_id"
    )
    label_ids, _ = read_csv_identity(labels, id_column="response_id")
    if feature_ids != label_ids:
        raise ValueError("feature and label response_id identity/order differ")
    if len(feature_ids) != 35072 or len(sessions) != 22821:
        raise ValueError("training row/session counts differ from frozen contract")
    return {
        "response_id_order_matches": True,
        "response_ids_unique": True,
        "rows": len(feature_ids),
        "session_ids": sessions,
        "sessions": len(sessions),
    }


def zip_csv_stems(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
    return [Path(name).stem for name in names]


def validate_transcript_coverage(
    part1: Path,
    part2: Path,
    expected_sessions: set[str],
) -> dict[str, object]:
    stems1 = zip_csv_stems(part1)
    stems2 = zip_csv_stems(part2)
    combined = stems1 + stems2
    if len(combined) != len(set(combined)):
        raise ValueError("transcript archives contain duplicate session stems")
    if set(combined) != expected_sessions:
        raise ValueError("transcript session coverage differs from features")
    return {
        "combined_session_coverage_matches": True,
        "part1_csv_members": len(stems1),
        "part2_csv_members": len(stems2),
        "sessions": len(combined),
    }


def validate_submission_members(path: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    with zipfile.ZipFile(path) as archive:
        archive_names = set(archive.namelist())
        if archive_names != set(EXPECTED_SUBMISSION_MEMBERS):
            raise ValueError("Submission 01 member set differs from frozen package")
        for name, expected in EXPECTED_SUBMISSION_MEMBERS.items():
            actual = sha256_bytes(archive.read(name))
            if actual != expected:
                raise ValueError(f"Submission 01 member hash mismatch: {name}")
            observed[name] = actual
    return observed


def validate_glove_archive(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if names != [EXPECTED_GLOVE_MEMBER["name"]]:
            raise ValueError("GloVe archive member identity differs from frozen resource")
        info = archive.getinfo(names[0])
        if info.file_size != EXPECTED_GLOVE_MEMBER["size_bytes"]:
            raise ValueError("GloVe extracted-member size differs from frozen resource")
        with archive.open(names[0]) as stream:
            observed = sha256_stream(stream)
        if observed != EXPECTED_GLOVE_MEMBER["sha256"]:
            raise ValueError("GloVe extracted-member hash differs from frozen resource")
    return {
        "member": names[0],
        "member_sha256": observed,
        "member_size_bytes": info.file_size,
    }


def validate_research_sources(repository_root: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in EXPECTED_RESEARCH_FILES.items():
        path = repository_root / relative
        actual = sha256_file(path) if path.is_file() else None
        if actual != expected:
            raise ValueError(f"research implementation identity failure: {relative}")
        observed[relative] = actual
    return observed


def primary_paths(args: argparse.Namespace) -> dict[str, Path | None]:
    return {
        "historical_m2s_oof": args.research_oof,
        "historical_outer_folds": args.outer_folds,
        "deployment_crossfit_scores": args.deployment_crossfit_scores,
        "deployment_crossfit_fitting_implementation": args.deployment_fit_implementation,
        "deployment_crossfit_platt_geometry": args.deployment_platt_geometry,
    }


def build_blocked_result(
    checks: Mapping[str, ObjectCheck],
    *,
    training_alignment: Mapping[str, object],
    transcript_coverage: Mapping[str, object],
    additional_missing: Sequence[str] = (),
    phase0_overrides: Mapping[str, str] | None = None,
    verification_extra: Mapping[str, object] | None = None,
) -> dict[str, object]:
    primary_missing = [
        object_id
        for object_id in REQUIRED_PRIMARY_OBJECTS
        if checks[object_id].status != "PRESENT_HASH_VALID"
    ]
    missing = list(dict.fromkeys([*additional_missing, *primary_missing]))
    if not missing:
        raise RuntimeError(
            "all primary objects are present; this Phase-0-only program must stop "
            "without opening Phases 1-4"
        )
    phase0 = {
        "external_semantic_resource_integrity": "PASS",
        "paired_score_row_identity": "NOT_CONSTITUTABLE",
        "required_object_availability": "FAIL",
        "research_implementation_integrity": "PASS",
        "state": "COMPLETED_BLOCKED",
        "submission_01_integrity": "PASS",
        "training_feature_label_row_alignment": "PASS",
        "training_input_integrity": "PASS",
        "training_transcript_session_coverage": "PASS",
    }
    phase0.update(phase0_overrides or {})
    verification_detail: dict[str, object] = {
        "primary_objects": {key: value.as_dict() for key, value in checks.items()},
        "training": {
            key: value
            for key, value in training_alignment.items()
            if key != "session_ids"
        },
        "transcripts": dict(transcript_coverage),
    }
    verification_detail.update(verification_extra or {})
    return {
        "D_deployment": D_DEPLOYMENT,
        "STOP": STOP,
        "audit_id": "TRACE_THE_ACE_DEPLOYMENT_REALIZATION",
        "authority": {
            "authorized_interpretation": "INPUT_AND_PROVENANCE_DIAGNOSIS_ONLY",
            "calibration_selection_reopened": False,
            "cca_update_authorized": False,
            "deployment_mismatch_conclusion_authorized": False,
            "hidden_or_public_test_information_used": False,
            "model_search_reopened": False,
            "submission_02_authorized": False,
        },
        "metrics": None,
        "missing_required_objects": missing,
        "parent_commit": PARENT_COMMIT,
        "phase0": phase0,
        "phases": {
            "phase1_raw_score_comparison": "NOT_RUN_BLOCKED_MISSING_INPUT",
            "phase2_fixed_family_platt_comparison": "NOT_RUN_BLOCKED_MISSING_INPUT",
            "phase3_packaged_implementation_equivalence": "NOT_RUN_BLOCKED_MISSING_INPUT",
            "phase4_full_fit_secondary_diagnostic": "NOT_RUN_BLOCKED_MISSING_INPUT",
        },
        "schema_version": 1,
        "tests": {
            "direct_vs_packaged_probability_equivalence": "NOT_REACHED",
            "direct_vs_packaged_raw_score_equivalence": "NOT_REACHED",
            "phase0_fail_closed_contract": "PASS",
            "primary_paired_row_alignment": "NOT_REACHED",
            "score_extraction_consistency": "NOT_REACHED",
        },
        "verification_detail": verification_detail,
    }


def blocked_preflight_result(
    args: argparse.Namespace,
    *,
    missing: Sequence[str],
    phase0_overrides: Mapping[str, str],
    verification_extra: Mapping[str, object] | None = None,
) -> dict[str, object]:
    checks = {
        object_id: check_object(
            object_id,
            primary_paths(args)[object_id],
            required_hash,
        )
        for object_id, required_hash in REQUIRED_PRIMARY_OBJECTS.items()
    }
    return build_blocked_result(
        checks,
        training_alignment={},
        transcript_coverage={},
        additional_missing=missing,
        phase0_overrides=phase0_overrides,
        verification_extra=verification_extra,
    )


def path_arg(value: str) -> Path:
    return Path(value).expanduser().resolve()


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Verify only the Phase-0 availability/identity gate from issue #48."
    )
    result.add_argument("--repository-root", required=True, type=path_arg)
    result.add_argument("--features", required=True, type=path_arg)
    result.add_argument("--labels", required=True, type=path_arg)
    result.add_argument("--transcripts-part1", required=True, type=path_arg)
    result.add_argument("--transcripts-part2", required=True, type=path_arg)
    result.add_argument("--submission-zip", required=True, type=path_arg)
    result.add_argument("--glove-archive", required=True, type=path_arg)
    result.add_argument("--research-oof", type=path_arg)
    result.add_argument("--outer-folds", type=path_arg)
    result.add_argument("--deployment-crossfit-scores", type=path_arg)
    result.add_argument("--deployment-fit-implementation", type=path_arg)
    result.add_argument("--deployment-platt-geometry", type=path_arg)
    result.add_argument("--output", type=path_arg)
    return result


def run(args: argparse.Namespace) -> dict[str, object]:
    allowlisted_paths = {
        "features": args.features,
        "labels": args.labels,
        "transcripts_part1": args.transcripts_part1,
        "transcripts_part2": args.transcripts_part2,
        "submission_zip": args.submission_zip,
        "glove_archive": args.glove_archive,
    }
    input_checks: dict[str, ObjectCheck] = {}
    for object_id, path in allowlisted_paths.items():
        expected_name, expected_hash = EXPECTED_INPUTS[object_id]
        ensure_allowlisted_path(path)
        if path.name != expected_name:
            input_checks[object_id] = ObjectCheck(
                object_id,
                str(path),
                "FILENAME_MISMATCH",
                expected_hash,
                sha256_file(path) if path.is_file() else None,
            )
            continue
        check = check_object(object_id, path, expected_hash)
        input_checks[object_id] = check

    invalid_inputs = [
        f"required_input:{object_id}"
        for object_id, check in input_checks.items()
        if check.status != "PRESENT_HASH_VALID"
    ]
    if invalid_inputs:
        return blocked_preflight_result(
            args,
            missing=invalid_inputs,
            phase0_overrides={
                "external_semantic_resource_integrity": "NOT_REACHED",
                "research_implementation_integrity": "NOT_REACHED",
                "submission_01_integrity": "NOT_REACHED",
                "training_feature_label_row_alignment": "NOT_REACHED",
                "training_input_integrity": "FAIL",
                "training_transcript_session_coverage": "NOT_REACHED",
            },
            verification_extra={
                "required_inputs": {
                    key: value.as_dict() for key, value in input_checks.items()
                }
            },
        )

    try:
        alignment = validate_training_alignment(args.features, args.labels)
    except ValueError as error:
        return blocked_preflight_result(
            args,
            missing=["training_feature_label_row_identity"],
            phase0_overrides={
                "external_semantic_resource_integrity": "NOT_REACHED",
                "research_implementation_integrity": "NOT_REACHED",
                "submission_01_integrity": "NOT_REACHED",
                "training_feature_label_row_alignment": "FAIL",
                "training_transcript_session_coverage": "NOT_REACHED",
            },
            verification_extra={"phase0_error": str(error)},
        )
    try:
        coverage = validate_transcript_coverage(
            args.transcripts_part1,
            args.transcripts_part2,
            alignment["session_ids"],
        )
    except ValueError as error:
        return blocked_preflight_result(
            args,
            missing=["training_transcript_session_coverage"],
            phase0_overrides={
                "external_semantic_resource_integrity": "NOT_REACHED",
                "research_implementation_integrity": "NOT_REACHED",
                "submission_01_integrity": "NOT_REACHED",
                "training_transcript_session_coverage": "FAIL",
            },
            verification_extra={"phase0_error": str(error)},
        )
    try:
        validate_submission_members(args.submission_zip)
    except ValueError as error:
        return blocked_preflight_result(
            args,
            missing=["submission_01_member_identity"],
            phase0_overrides={
                "external_semantic_resource_integrity": "NOT_REACHED",
                "research_implementation_integrity": "NOT_REACHED",
                "submission_01_integrity": "FAIL",
            },
            verification_extra={"phase0_error": str(error)},
        )
    try:
        validate_glove_archive(args.glove_archive)
    except ValueError as error:
        return blocked_preflight_result(
            args,
            missing=["external_semantic_resource_identity"],
            phase0_overrides={
                "external_semantic_resource_integrity": "FAIL",
                "research_implementation_integrity": "NOT_REACHED",
            },
            verification_extra={"phase0_error": str(error)},
        )
    try:
        validate_research_sources(args.repository_root)
    except ValueError as error:
        return blocked_preflight_result(
            args,
            missing=["research_implementation_identity"],
            phase0_overrides={"research_implementation_integrity": "FAIL"},
            verification_extra={"phase0_error": str(error)},
        )

    checks = {
        object_id: check_object(
            object_id,
            primary_paths(args)[object_id],
            required_hash,
        )
        for object_id, required_hash in REQUIRED_PRIMARY_OBJECTS.items()
    }
    return build_blocked_result(
        checks,
        training_alignment=alignment,
        transcript_coverage=coverage,
    )


def dump_result(result: Mapping[str, object], output: Path | None) -> None:
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if output is None:
        sys.stdout.write(rendered)
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8", newline="\n")


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    result = run(args)
    dump_result(result, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
