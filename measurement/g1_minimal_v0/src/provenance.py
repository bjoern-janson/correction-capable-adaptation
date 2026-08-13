import hashlib
import json
from pathlib import Path


def canonical_bytes(record: dict) -> bytes:
    return json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def chained_record(record: dict, previous_hash: str) -> tuple[dict, str]:
    payload = {
        "previous_hash": previous_hash,
        "record": record,
    }
    digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return {**payload, "record_hash": digest}, digest


def append_record(path: str | Path, record: dict, previous_hash: str) -> str:
    wrapped, digest = chained_record(record, previous_hash)
    with Path(path).open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(wrapped, sort_keys=True, separators=(",", ":")))
        fh.write("\n")
    return digest
