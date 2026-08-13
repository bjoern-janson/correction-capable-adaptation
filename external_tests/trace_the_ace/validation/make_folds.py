#!/usr/bin/env python3
"""Create one immutable session-grouped fold assignment for Trace the Ace."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--record", required=True, type=Path)
    ap.add_argument("--n-splits", type=int, default=5)
    ap.add_argument("--seed", type=int, default=3)
    args = ap.parse_args()

    df = pd.read_csv(args.index)
    required = {"response_id", "session_id", "is_correct"}
    assert required.issubset(df.columns)
    assert df["response_id"].is_unique

    splitter = StratifiedGroupKFold(
        n_splits=args.n_splits,
        shuffle=True,
        random_state=args.seed,
    )

    session_fold: dict[str, int] = {}
    for fold, (_, val_idx) in enumerate(
        splitter.split(df, y=df["is_correct"], groups=df["session_id"])
    ):
        val_sessions = set(df.iloc[val_idx]["session_id"])
        for sid in val_sessions:
            if sid in session_fold:
                raise AssertionError(f"session assigned twice: {sid}")
            session_fold[sid] = fold

    all_sessions = set(df["session_id"])
    assert set(session_fold) == all_sessions
    assert len(session_fold) == df["session_id"].nunique()

    folds = pd.DataFrame(
        sorted(session_fold.items()), columns=["session_id", "fold"]
    )
    assert folds["session_id"].is_unique
    assert set(folds["fold"]) == set(range(args.n_splits))

    # Hard leakage assertion: no session can appear in both train and validation for any fold.
    leakage = {}
    merged = df.merge(folds, on="session_id", validate="many_to_one")
    fold_summary = []
    for fold in range(args.n_splits):
        val_sessions = set(merged.loc[merged["fold"].eq(fold), "session_id"])
        train_sessions = set(merged.loc[~merged["fold"].eq(fold), "session_id"])
        overlap = val_sessions & train_sessions
        leakage[str(fold)] = len(overlap)
        assert not overlap
        val = merged.loc[merged["fold"].eq(fold)]
        fold_summary.append(
            {
                "fold": fold,
                "responses": int(len(val)),
                "sessions": int(val["session_id"].nunique()),
                "correct_rate": float(val["is_correct"].mean()),
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    folds.to_csv(args.output, index=False, lineterminator="\n")

    record = {
        "schema_version": 1,
        "status": "PASS",
        "splitter": "StratifiedGroupKFold",
        "n_splits": args.n_splits,
        "seed": args.seed,
        "grouping_key": "session_id",
        "index_sha256": sha256_file(args.index),
        "fold_sha256": sha256_file(args.output),
        "sessions": int(len(folds)),
        "leakage_session_overlap_by_fold": leakage,
        "fold_summary": fold_summary,
    }
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
