#!/usr/bin/env python3
"""Build and validate the canonical Trace the Ace training index.

This script is intentionally strict. Any mismatch in response/session/transcript identity
is a data-integrity failure; nothing is silently dropped or repaired.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from dataclasses import dataclass
from multiprocessing import Pool
from pathlib import Path
from typing import Iterable
import zipfile

import pandas as pd

EXPECTED_FEATURE_COLUMNS = [
    "response_id",
    "session_id",
    "learning_objective_id",
    "learning_objective",
]
EXPECTED_LABEL_COLUMNS = ["response_id", "is_correct"]
EXPECTED_TRANSCRIPT_COLUMNS = [
    "session_id",
    "utterance_id",
    "role",
    "content",
    "timestamp",
]
EXPECTED_RESPONSES = 35_072
EXPECTED_SESSIONS = 22_821
EXPECTED_OBJECTIVES = 398


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def stable_json_hash(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class TranscriptRef:
    session_id: str
    kind: str
    container: str
    member: str
    size: int
    crc32: int | None


def discover_transcripts(roots: list[Path], zips: list[Path]) -> dict[str, TranscriptRef]:
    refs: dict[str, TranscriptRef] = {}

    for root in roots:
        for path in sorted(root.rglob("*.csv")):
            sid = path.stem
            ref = TranscriptRef(
                session_id=sid,
                kind="file",
                container=str(path),
                member="",
                size=path.stat().st_size,
                crc32=None,
            )
            if sid in refs:
                raise AssertionError(f"duplicate transcript session_id: {sid}")
            refs[sid] = ref

    for zip_path in zips:
        with zipfile.ZipFile(zip_path) as zf:
            for info in zf.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".csv"):
                    continue
                sid = Path(info.filename).stem
                ref = TranscriptRef(
                    session_id=sid,
                    kind="zip",
                    container=str(zip_path),
                    member=info.filename,
                    size=info.file_size,
                    crc32=info.CRC,
                )
                if sid in refs:
                    raise AssertionError(f"duplicate transcript session_id: {sid}")
                refs[sid] = ref

    if not refs:
        raise AssertionError("no transcript CSVs found")
    return refs


def _validate_rows(rows: Iterable[dict[str, str]], sid: str, fieldnames: list[str] | None) -> int:
    if fieldnames != EXPECTED_TRANSCRIPT_COLUMNS:
        raise AssertionError(
            f"{sid}: transcript columns {fieldnames!r} != {EXPECTED_TRANSCRIPT_COLUMNS!r}"
        )
    n = 0
    for expected_uid, row in enumerate(rows):
        for col in EXPECTED_TRANSCRIPT_COLUMNS:
            value = row.get(col)
            if value is None or value == "":
                raise AssertionError(f"{sid}: missing {col} at row {expected_uid}")
        if row["session_id"] != sid:
            raise AssertionError(
                f"{sid}: internal session_id {row['session_id']!r} does not match filename"
            )
        try:
            uid = int(row["utterance_id"])
        except ValueError as exc:
            raise AssertionError(f"{sid}: non-integer utterance_id {row['utterance_id']!r}") from exc
        if uid != expected_uid:
            raise AssertionError(
                f"{sid}: utterance_id {uid} at row {expected_uid}; expected {expected_uid}"
            )
        n += 1
    if n == 0:
        raise AssertionError(f"{sid}: empty transcript")
    return n


def validate_transcript(ref: TranscriptRef) -> tuple[str, int, str]:
    import io
    if ref.kind == "file":
        payload = Path(ref.container).read_bytes()
    elif ref.kind == "zip":
        with zipfile.ZipFile(ref.container) as zf:
            payload = zf.read(ref.member)
    else:
        raise AssertionError(f"unknown transcript ref kind: {ref.kind}")
    digest = hashlib.sha256(payload).hexdigest()
    text = io.TextIOWrapper(io.BytesIO(payload), encoding="utf-8-sig", newline="")
    reader = csv.DictReader(text)
    n = _validate_rows(reader, ref.session_id, reader.fieldnames)
    return ref.session_id, n, digest


def validate_zip_archive(zip_path: Path) -> list[tuple[str, int, str]]:
    """Validate one ZIP in a single open/scan pass."""
    import io
    out: list[tuple[str, int, str]] = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir() or not info.filename.lower().endswith(".csv"):
                continue
            sid = Path(info.filename).stem
            payload = zf.read(info)
            digest = hashlib.sha256(payload).hexdigest()
            text = io.TextIOWrapper(io.BytesIO(payload), encoding="utf-8-sig", newline="")
            reader = csv.DictReader(text)
            n = _validate_rows(reader, sid, reader.fieldnames)
            out.append((sid, n, digest))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True, type=Path)
    ap.add_argument("--labels", required=True, type=Path)
    ap.add_argument("--transcripts-root", action="append", default=[], type=Path)
    ap.add_argument("--transcripts-zip", action="append", default=[], type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--record", required=True, type=Path)
    ap.add_argument("--workers", type=int, default=min(24, os.cpu_count() or 1))
    args = ap.parse_args()

    features = pd.read_csv(args.features)
    labels = pd.read_csv(args.labels)

    assert features.columns.tolist() == EXPECTED_FEATURE_COLUMNS, features.columns.tolist()
    assert labels.columns.tolist() == EXPECTED_LABEL_COLUMNS, labels.columns.tolist()
    assert len(features) == EXPECTED_RESPONSES, len(features)
    assert len(labels) == EXPECTED_RESPONSES, len(labels)
    assert features["response_id"].is_unique
    assert labels["response_id"].is_unique
    assert not features.isna().any().any()
    assert not labels.isna().any().any()
    assert set(labels["is_correct"].unique()).issubset({0, 1, 0.0, 1.0})

    index = features.merge(labels, on="response_id", how="inner", validate="one_to_one")
    assert len(index) == EXPECTED_RESPONSES
    assert index["session_id"].nunique() == EXPECTED_SESSIONS
    assert index["learning_objective_id"].nunique() == EXPECTED_OBJECTIVES

    # One objective ID must carry one stable text description.
    obj_counts = index.groupby("learning_objective_id")["learning_objective"].nunique()
    assert int(obj_counts.max()) == 1

    refs = discover_transcripts(args.transcripts_root, args.transcripts_zip)
    feature_sessions = set(index["session_id"])
    transcript_sessions = set(refs)
    missing = sorted(feature_sessions - transcript_sessions)
    extra = sorted(transcript_sessions - feature_sessions)
    assert not missing, f"missing transcript sessions: {missing[:10]} (n={len(missing)})"
    assert not extra, f"extra transcript sessions: {extra[:10]} (n={len(extra)})"
    assert len(refs) == EXPECTED_SESSIONS

    # Deep validation is deliberately outcome-blind. File trees are parallelized per file;
    # ZIP archives are each opened once to avoid per-session archive reopen overhead.
    file_refs = [ref for ref in refs.values() if ref.kind == "file"]
    validated: list[tuple[str, int, str]] = []
    if file_refs:
        with Pool(processes=args.workers) as pool:
            validated.extend(pool.map(validate_transcript, file_refs, chunksize=32))
    if args.transcripts_zip:
        with Pool(processes=min(len(args.transcripts_zip), args.workers)) as pool:
            blocks = pool.map(validate_zip_archive, args.transcripts_zip)
        for block in blocks:
            validated.extend(block)
    assert len(validated) == len(refs)
    assert len({sid for sid, _, _ in validated}) == len(refs)
    utterance_counts = {sid: n for sid, n, _ in validated}
    transcript_hashes = {sid: digest for sid, _, digest in validated}
    assert len(utterance_counts) == EXPECTED_SESSIONS

    # Packaging/location-independent manifest identity: filename stem + uncompressed content hash.
    manifest_rows = [
        {
            "session_id": sid,
            "sha256": transcript_hashes[sid],
            "utterances": utterance_counts[sid],
        }
        for sid in sorted(refs)
    ]
    transcript_manifest_hash = stable_json_hash(manifest_rows)

    # The canonical index contains scientific identity, never machine-local absolute paths.
    index = index.sort_values("response_id").reset_index(drop=True)
    index["transcript_file"] = index["session_id"].map(lambda sid: f"{sid}.csv")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    index.to_csv(args.output, index=False, lineterminator="\n")
    index_hash = sha256_file(args.output)

    record = {
        "schema_version": 1,
        "status": "PASS",
        "expected": {
            "responses": EXPECTED_RESPONSES,
            "sessions": EXPECTED_SESSIONS,
            "objectives": EXPECTED_OBJECTIVES,
            "transcript_sessions": EXPECTED_SESSIONS,
        },
        "observed": {
            "responses": len(index),
            "sessions": int(index["session_id"].nunique()),
            "objectives": int(index["learning_objective_id"].nunique()),
            "transcript_sessions": len(refs),
            "total_utterances": int(sum(utterance_counts.values())),
        },
        "hashes": {
            "features_sha256": sha256_file(args.features),
            "labels_sha256": sha256_file(args.labels),
            "transcript_manifest_sha256": transcript_manifest_hash,
            "index_sha256": index_hash,
        },
        "assertions": {
            "response_feature_label_mapping": "PASS",
            "session_coverage": "PASS",
            "objective_text_stability": "PASS",
            "transcript_coverage": "PASS",
            "transcript_schema": "PASS",
            "internal_session_id_matches_filename": "PASS",
            "utterance_ids_contiguous_zero_based": "PASS",
            "required_transcript_fields_nonmissing": "PASS",
        },
    }
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
