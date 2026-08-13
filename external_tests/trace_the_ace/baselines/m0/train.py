#!/usr/bin/env python3
"""Reproduce the published Trace the Ace M0 and evaluate it on canonical grouped folds.

M0 is measurement infrastructure only. It contains no CCA-derived features.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import re
import sys
from multiprocessing import Pool
from pathlib import Path
from typing import Iterable
import zipfile

import numpy as np
import pandas as pd
import sklearn
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def stable_hash(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def session_feature_from_rows(
    sid: str,
    rows: Iterable[dict[str, str]],
    word_re: re.Pattern[str],
    digit_re: re.Pattern[str],
) -> tuple[str, int, float, float, float]:
    n_turns = 0
    n_student_words = 0
    numeric_turns = 0
    digit_chars = 0
    for row in rows:
        n_turns += 1
        if row.get("role") != "student":
            continue
        text = row.get("content") or ""
        n_student_words += len(word_re.findall(text))
        if digit_re.search(text):
            numeric_turns += 1
        digit_chars += len(digit_re.findall(text))
    denom = float(n_student_words) if n_student_words else float("nan")
    return (
        sid,
        n_turns,
        float(n_student_words) if n_student_words else float("nan"),
        numeric_turns / denom,
        digit_chars / denom,
    )


def _file_feature_job(args: tuple[str, str, str, str]) -> tuple[str, int, float, float, float]:
    sid, path, word_pattern, digit_pattern = args
    word_re = re.compile(word_pattern, re.I)
    digit_re = re.compile(digit_pattern)
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return session_feature_from_rows(sid, reader, word_re, digit_re)


def _zip_feature_job(args: tuple[str, str, str]) -> list[tuple[str, int, float, float, float]]:
    zip_path, word_pattern, digit_pattern = args
    word_re = re.compile(word_pattern, re.I)
    digit_re = re.compile(digit_pattern)
    out = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir() or not info.filename.lower().endswith(".csv"):
                continue
            sid = Path(info.filename).stem
            with zf.open(info) as raw:
                import io
                text = io.TextIOWrapper(raw, encoding="utf-8-sig", newline="")
                reader = csv.DictReader(text)
                out.append(session_feature_from_rows(sid, reader, word_re, digit_re))
    return out


def extract_session_features(
    roots: list[Path],
    zips: list[Path],
    word_pattern: str,
    digit_pattern: str,
    workers: int,
) -> pd.DataFrame:
    rows: list[tuple[str, int, float, float, float]] = []
    seen: set[str] = set()

    file_jobs = []
    for root in roots:
        for path in sorted(root.rglob("*.csv")):
            sid = path.stem
            if sid in seen:
                raise AssertionError(f"duplicate transcript session_id: {sid}")
            seen.add(sid)
            file_jobs.append((sid, str(path), word_pattern, digit_pattern))
    if file_jobs:
        with Pool(processes=workers) as pool:
            rows.extend(pool.map(_file_feature_job, file_jobs, chunksize=40))

    if zips:
        # Open each archive only once. This avoids the pathological per-session ZIP reopen pattern.
        zip_jobs = [(str(z), word_pattern, digit_pattern) for z in zips]
        with Pool(processes=min(len(zip_jobs), workers)) as pool:
            zip_results = pool.map(_zip_feature_job, zip_jobs)
        for block in zip_results:
            for row in block:
                sid = row[0]
                if sid in seen:
                    raise AssertionError(f"duplicate transcript session_id: {sid}")
                seen.add(sid)
            rows.extend(block)

    if not rows:
        raise AssertionError("no transcript inputs supplied")

    return pd.DataFrame(
        rows,
        columns=[
            "session_id",
            "n_turns",
            "n_student_words",
            "numeric_turns_per_word",
            "digit_chars_per_word",
        ],
    ).sort_values("session_id").reset_index(drop=True)


def fit_reference_model(train: pd.DataFrame, val: pd.DataFrame, features: list[str], max_iter: int):
    medians = train[features].median()
    x_train = train[features].fillna(medians)
    x_val = val[features].fillna(medians)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=max_iter))
    model.fit(x_train, train["is_correct"])
    pred = model.predict_proba(x_val)[:, 1]
    return model, pred


def calibration_summary(y: np.ndarray, p: np.ndarray, bins: int = 10) -> dict[str, float]:
    edges = np.linspace(0.0, 1.0, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1], right=False), 0, bins - 1)
    ece = 0.0
    for b in range(bins):
        mask = idx == b
        if not np.any(mask):
            continue
        ece += float(mask.mean()) * abs(float(p[mask].mean()) - float(y[mask].mean()))
    return {
        "mean_probability": float(np.mean(p)),
        "observed_rate": float(np.mean(y)),
        "brier_score": float(brier_score_loss(y, p)),
        "ece_10_equal_width": float(ece),
    }


def check_rounded(value: float, spec: dict) -> bool:
    return round(float(value), int(spec["decimals"])) == float(spec["value"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--folds", required=True, type=Path)
    ap.add_argument("--transcripts-root", action="append", default=[], type=Path)
    ap.add_argument("--transcripts-zip", action="append", default=[], type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--workers", type=int, default=min(24, os.cpu_count() or 1))
    args = ap.parse_args()

    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    features = list(config["features"])
    min_student_words = int(config["min_student_words"])
    max_iter = int(config["reference_model"]["max_iter"])

    index = pd.read_csv(args.index)
    folds = pd.read_csv(args.folds)
    assert index["response_id"].is_unique
    assert folds["session_id"].is_unique
    df = index.merge(folds, on="session_id", validate="many_to_one")
    assert not df["fold"].isna().any()

    session_features = extract_session_features(
        args.transcripts_root,
        args.transcripts_zip,
        config["word_regex"],
        config["digit_regex"],
        args.workers,
    )
    assert session_features["session_id"].is_unique
    assert set(session_features["session_id"]) == set(df["session_id"])
    df = df.merge(session_features, on="session_id", validate="many_to_one")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    session_feature_path = args.output_dir / "session_features.csv"
    session_features.to_csv(session_feature_path, index=False, lineterminator="\n")

    eligible = df["n_student_words"].ge(min_student_words)
    quiet_sessions = int((~session_features["n_student_words"].ge(min_student_words)).sum())
    quiet_responses = int((~eligible).sum())
    quiet_correct_rate = float(df.loc[~eligible, "is_correct"].mean())

    # Published reference reproduction witness. This is intentionally separate from canonical CV.
    ref_df = df.loc[eligible].copy()
    ref_cfg = config["reference_split"]
    tr_idx, va_idx = next(
        GroupShuffleSplit(
            n_splits=1,
            test_size=float(ref_cfg["test_size"]),
            random_state=int(ref_cfg["random_state"]),
        ).split(ref_df, ref_df["is_correct"], groups=ref_df["session_id"])
    )
    tr, va = ref_df.iloc[tr_idx], ref_df.iloc[va_idx]
    ref_model, ref_pred = fit_reference_model(tr, va, features, max_iter)
    ref_base = float(tr["is_correct"].mean())
    ref_base_ll = float(log_loss(va["is_correct"], np.full(len(va), ref_base)))
    ref_model_ll = float(log_loss(va["is_correct"], ref_pred))
    ref_auc = float(roc_auc_score(va["is_correct"], ref_pred))
    coef = ref_model.named_steps["logisticregression"].coef_[0]
    ref_coefficients = {name: float(value) for name, value in zip(features, coef)}

    targets = config["reference_targets"]
    reproduction_checks = {
        "base_log_loss": check_rounded(ref_base_ll, targets["base_log_loss"]),
        "model_log_loss": check_rounded(ref_model_ll, targets["model_log_loss"]),
        "auc": check_rounded(ref_auc, targets["auc"]),
        "coefficients": all(
            round(ref_coefficients[name], int(targets["coefficients"]["decimals"]))
            == float(targets["coefficients"]["values"][name])
            for name in features
        ),
    }
    reference_reproduced = all(reproduction_checks.values())

    # Canonical OOF evaluation. Quiet validation sessions receive the training base-rate fallback.
    n_splits = int(config["canonical_cv"]["n_splits"])
    expected_folds = set(range(n_splits))
    assert set(df["fold"].astype(int).unique()) == expected_folds
    oof = np.full(len(df), np.nan, dtype=float)
    fold_records = []

    for fold in range(n_splits):
        train_mask = df["fold"].ne(fold) & eligible
        val_mask = df["fold"].eq(fold)
        val_eligible = val_mask & eligible
        val_quiet = val_mask & ~eligible
        train = df.loc[train_mask]
        val = df.loc[val_eligible]
        assert set(train["session_id"]).isdisjoint(set(df.loc[val_mask, "session_id"]))

        model, pred = fit_reference_model(train, val, features, max_iter)
        oof[np.where(val_eligible)[0]] = pred
        train_base = float(train["is_correct"].mean())
        oof[np.where(val_quiet)[0]] = train_base

        y_fold = df.loc[val_mask, "is_correct"].to_numpy()
        p_fold = oof[np.where(val_mask)[0]]
        fold_records.append(
            {
                "fold": fold,
                "responses": int(val_mask.sum()),
                "sessions": int(df.loc[val_mask, "session_id"].nunique()),
                "quiet_responses": int(val_quiet.sum()),
                "log_loss": float(log_loss(y_fold, p_fold)),
                "auc": float(roc_auc_score(y_fold, p_fold)),
                "train_base_rate": train_base,
            }
        )

    assert np.isfinite(oof).all()
    y = df["is_correct"].to_numpy()
    pooled_ll = float(log_loss(y, oof))
    pooled_auc = float(roc_auc_score(y, oof))
    calibration = calibration_summary(y, oof)

    oof_path = args.output_dir / "oof_predictions.csv"
    pd.DataFrame(
        {
            "response_id": df["response_id"],
            "session_id": df["session_id"],
            "fold": df["fold"].astype(int),
            "is_correct": df["is_correct"],
            "m0_eligible": eligible,
            "probability": oof,
        }
    ).sort_values("response_id").to_csv(oof_path, index=False, lineterminator="\n")

    env = {
        "python": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "cpu_count": os.cpu_count(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scikit_learn": sklearn.__version__,
        "pyyaml": yaml.__version__,
    }
    preprocessing_identity = {
        "feature_definition": config["feature_definition"],
        "min_student_words": min_student_words,
        "features": features,
        "word_regex": config["word_regex"],
        "digit_regex": config["digit_regex"],
        "quiet_session_prediction": config["canonical_cv"]["quiet_session_prediction"],
    }
    model_identity = config["reference_model"]

    record = {
        "schema_version": 1,
        "experiment_id": "M0",
        "status": "DIAGNOSED_PASS" if reference_reproduced else "DIAGNOSED_DISCREPANCY",
        "cca_features_present": False,
        "data": {
            "responses": int(len(df)),
            "sessions": int(df["session_id"].nunique()),
            "quiet_sessions": quiet_sessions,
            "quiet_responses": quiet_responses,
            "quiet_correct_rate": quiet_correct_rate,
        },
        "identity": {
            "dataset_index_sha256": sha256_file(args.index),
            "fold_artifact_sha256": sha256_file(args.folds),
            "preprocessing_config_sha256": stable_hash(preprocessing_identity),
            "model_config_sha256": stable_hash(model_identity),
            "runtime_environment_sha256": stable_hash(env),
            "full_config_sha256": sha256_file(args.config),
            "session_features_sha256": sha256_file(session_feature_path),
        },
        "reference_reproduction": {
            "reproduced": reference_reproduced,
            "checks": reproduction_checks,
            "train_responses": int(len(tr)),
            "validation_responses": int(len(va)),
            "validation_sessions": int(va["session_id"].nunique()),
            "base_log_loss": ref_base_ll,
            "model_log_loss": ref_model_ll,
            "auc": ref_auc,
            "coefficients": ref_coefficients,
        },
        "canonical_oof": {
            "n_splits": n_splits,
            "pooled_log_loss": pooled_ll,
            "pooled_auc": pooled_auc,
            "calibration": calibration,
            "folds": fold_records,
            "oof_predictions_sha256": sha256_file(oof_path),
        },
        "environment": env,
        "diagnosis": {
            "apparatus_reproducible": reference_reproduced,
            "discrepancies": [] if reference_reproduced else [
                name for name, passed in reproduction_checks.items() if not passed
            ],
            "failure_locus": None if reference_reproduced else "M0_REFERENCE_REPRODUCTION",
        },
        "authority": {
            "gained": [
                "M0_reference_implementation_reproduced",
                "canonical_session_grouped_OOF_apparatus_executed",
            ] if reference_reproduced else [],
            "not_gained": [
                "CCA_support",
                "CCA_refutation",
                "causal_evidence",
                "G1_evidence",
                "PMC_evidence",
                "JT_evidence",
                "C_improve_measurement",
            ],
        },
    }
    record_path = args.output_dir / "m0_record.json"
    record_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))

    if not reference_reproduced:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
