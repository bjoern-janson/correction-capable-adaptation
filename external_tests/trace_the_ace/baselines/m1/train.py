#!/usr/bin/env python3
"""Execute the frozen Trace the Ace M1 ordinary transcript-semantic baseline.

M1 contains no objective information and no CCA-derived features.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
import sklearn
import yaml
from scipy import sparse
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
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


def per_row_log_loss(y: np.ndarray, p: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-15, 1 - 1e-15)
    y = np.asarray(y, dtype=float)
    return -(y * np.log(p) + (1.0 - y) * np.log(1.0 - p))


def paired_session_bootstrap(
    session_ids: np.ndarray,
    m1_loss: np.ndarray,
    m0_loss: np.ndarray,
    replicates: int,
    seed: int,
) -> dict[str, float]:
    tmp = pd.DataFrame({"session_id": session_ids, "delta": m1_loss - m0_loss})
    agg = tmp.groupby("session_id", sort=True)["delta"].agg(["sum", "count"])
    sums = agg["sum"].to_numpy(dtype=float)
    counts = agg["count"].to_numpy(dtype=float)
    n = len(agg)
    rng = np.random.default_rng(seed)
    out = np.empty(replicates, dtype=float)
    chunk = 100
    done = 0
    while done < replicates:
        k = min(chunk, replicates - done)
        draw = rng.integers(0, n, size=(k, n))
        out[done:done+k] = sums[draw].sum(axis=1) / counts[draw].sum(axis=1)
        done += k
    q025, q975 = np.quantile(out, [0.025, 0.975])
    return {
        "point_delta_log_loss": float((m1_loss - m0_loss).mean()),
        "ci95_lower": float(q025),
        "ci95_upper": float(q975),
        "replicates": int(replicates),
        "seed": int(seed),
        "clusters": int(n),
    }


def normalize_text(text: str) -> str:
    return " ".join((text or "").split())


def serialize_transcript(path: Path, role_markers: dict[str, str]) -> str:
    parts: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        expected = ["session_id", "utterance_id", "role", "content", "timestamp"]
        if reader.fieldnames != expected:
            raise AssertionError(f"schema mismatch: {path}: {reader.fieldnames}")
        for row in reader:
            role = row["role"]
            if role not in role_markers:
                raise AssertionError(f"unexpected role {role!r} in {path}")
            content = normalize_text(row["content"])
            parts.append(f"{role_markers[role]} {content}")
    return "\n".join(parts)


def transcript_path_map(roots: list[Path]) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for root in roots:
        for p in root.rglob("*.csv"):
            sid = p.stem
            if sid in out:
                raise AssertionError(f"duplicate transcript session_id: {sid}")
            out[sid] = p
    return out


def make_vectorizer(cfg: dict) -> HashingVectorizer:
    dtype_name = str(cfg["dtype"])
    dtype = np.float32 if dtype_name == "float32" else np.float64
    return HashingVectorizer(
        analyzer=cfg["analyzer"],
        ngram_range=tuple(cfg["ngram_range"]),
        n_features=int(cfg["n_features"]),
        alternate_sign=bool(cfg["alternate_sign"]),
        binary=bool(cfg["binary"]),
        norm=cfg["norm"],
        lowercase=bool(cfg["lowercase"]),
        token_pattern=cfg["token_pattern"],
        dtype=dtype,
    )


def build_session_text_matrix(
    session_ids: list[str],
    paths: dict[str, Path],
    vectorizer: HashingVectorizer,
    role_markers: dict[str, str],
    batch_size: int,
) -> sparse.csr_matrix:
    blocks: list[sparse.csr_matrix] = []
    n = len(session_ids)
    for start in range(0, n, batch_size):
        batch_ids = session_ids[start:start + batch_size]
        texts = [serialize_transcript(paths[sid], role_markers) for sid in batch_ids]
        block = vectorizer.transform(texts).tocsr()
        if block.dtype != np.float32:
            block = block.astype(np.float32)
        blocks.append(block)
    return sparse.vstack(blocks, format="csr", dtype=np.float32)


def make_classifier(cfg: dict) -> SGDClassifier:
    return SGDClassifier(
        loss=cfg["loss"],
        penalty=cfg["penalty"],
        alpha=float(cfg["alpha"]),
        max_iter=int(cfg["max_iter"]),
        tol=float(cfg["tol"]),
        shuffle=bool(cfg["shuffle"]),
        random_state=int(cfg["random_state"]),
        average=bool(cfg["average"]),
        fit_intercept=bool(cfg["fit_intercept"]),
        class_weight=cfg["class_weight"],
        early_stopping=bool(cfg["early_stopping"]),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--folds", required=True, type=Path)
    ap.add_argument("--m0-session-features", required=True, type=Path)
    ap.add_argument("--m0-oof", required=True, type=Path)
    ap.add_argument("--transcripts-root", action="append", required=True, type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--batch-size", type=int, default=128)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if cfg["experiment_id"] != "M1":
        raise AssertionError("wrong experiment config")
    if bool(cfg["objective_information_allowed"]):
        raise AssertionError("M1 objective information must be disabled")
    if bool(cfg["cca_derived_features_allowed"]):
        raise AssertionError("M1 CCA-derived features must be disabled")

    required_fold_hash = cfg["fold_sha256_required"]
    observed_fold_hash = sha256_file(args.folds)
    if observed_fold_hash != required_fold_hash:
        raise AssertionError(
            f"fold artifact mismatch: expected {required_fold_hash}, got {observed_fold_hash}"
        )

    index = pd.read_csv(args.index)
    folds = pd.read_csv(args.folds)
    m0_features = pd.read_csv(args.m0_session_features)
    m0_oof = pd.read_csv(args.m0_oof)

    required_index = {"response_id", "session_id", "is_correct"}
    if not required_index.issubset(index.columns):
        raise AssertionError(f"index missing columns: {required_index - set(index.columns)}")
    if not index["response_id"].is_unique:
        raise AssertionError("response_id must be unique")
    if not folds["session_id"].is_unique:
        raise AssertionError("fold session_id must be unique")
    if not m0_features["session_id"].is_unique:
        raise AssertionError("M0 session features must be one row per session")
    if not m0_oof["response_id"].is_unique:
        raise AssertionError("M0 OOF response_id must be unique")

    df = index[["response_id", "session_id", "is_correct"]].merge(
        folds, on="session_id", validate="many_to_one"
    )
    ordinary = list(cfg["ordinary_covariates"])
    required_m0 = {"session_id", *ordinary}
    if not required_m0.issubset(m0_features.columns):
        raise AssertionError(f"M0 feature artifact missing: {required_m0 - set(m0_features.columns)}")
    df = df.merge(m0_features[["session_id", *ordinary]], on="session_id", validate="many_to_one")
    df = df.merge(
        m0_oof[["response_id", "probability"]].rename(columns={"probability": "m0_probability"}),
        on="response_id",
        validate="one_to_one",
    )
    if df[["response_id", "session_id", "is_correct", "fold", "m0_probability"]].isna().any().any():
        raise AssertionError("required M1 join fields contain missing values")

    sessions = sorted(df["session_id"].unique())
    path_map = transcript_path_map(args.transcripts_root)
    if set(path_map) != set(sessions):
        missing = set(sessions) - set(path_map)
        extra = set(path_map) - set(sessions)
        raise AssertionError(f"transcript coverage mismatch missing={len(missing)} extra={len(extra)}")

    vectorizer = make_vectorizer(cfg["semantic_representation"])
    role_markers = cfg["text_serialization"]["role_markers"]
    X_session = build_session_text_matrix(
        sessions, path_map, vectorizer, role_markers, args.batch_size
    )
    if X_session.shape != (len(sessions), int(cfg["semantic_representation"]["n_features"])):
        raise AssertionError(f"unexpected text matrix shape {X_session.shape}")

    sid_to_row = {sid: i for i, sid in enumerate(sessions)}
    response_session_idx = np.fromiter((sid_to_row[s] for s in df["session_id"]), dtype=np.int32)
    X_text = X_session[response_session_idx].tocsr()
    del X_session

    y = df["is_correct"].to_numpy(dtype=np.int8)
    folds_arr = df["fold"].to_numpy(dtype=np.int16)
    X_struct_raw = df[ordinary].to_numpy(dtype=float)
    oof = np.full(len(df), np.nan, dtype=float)
    fold_records: list[dict] = []

    expected_folds = sorted(int(x) for x in np.unique(folds_arr))
    for fold in expected_folds:
        tr_idx = np.flatnonzero(folds_arr != fold)
        va_idx = np.flatnonzero(folds_arr == fold)
        tr_sessions = set(df.iloc[tr_idx]["session_id"])
        va_sessions = set(df.iloc[va_idx]["session_id"])
        if tr_sessions & va_sessions:
            raise AssertionError(f"session leakage in fold {fold}")

        tr_struct = X_struct_raw[tr_idx].copy()
        va_struct = X_struct_raw[va_idx].copy()
        medians = np.nanmedian(tr_struct, axis=0)
        tr_nan = np.where(np.isnan(tr_struct))
        va_nan = np.where(np.isnan(va_struct))
        tr_struct[tr_nan] = medians[tr_nan[1]]
        va_struct[va_nan] = medians[va_nan[1]]
        scaler = StandardScaler()
        tr_struct = scaler.fit_transform(tr_struct).astype(np.float32)
        va_struct = scaler.transform(va_struct).astype(np.float32)

        Xtr = sparse.hstack(
            [X_text[tr_idx], sparse.csr_matrix(tr_struct)], format="csr", dtype=np.float32
        )
        Xva = sparse.hstack(
            [X_text[va_idx], sparse.csr_matrix(va_struct)], format="csr", dtype=np.float32
        )

        model = make_classifier(cfg["classifier"])
        model.fit(Xtr, y[tr_idx])
        pred = model.predict_proba(Xva)[:, 1]
        oof[va_idx] = pred

        m0_fold = df.iloc[va_idx]["m0_probability"].to_numpy(dtype=float)
        m1_ll = float(log_loss(y[va_idx], pred))
        m0_ll = float(log_loss(y[va_idx], m0_fold))
        fold_records.append(
            {
                "fold": int(fold),
                "responses": int(len(va_idx)),
                "sessions": int(len(va_sessions)),
                "m0_log_loss": m0_ll,
                "m1_log_loss": m1_ll,
                "delta_log_loss_m1_minus_m0": m1_ll - m0_ll,
                "m1_auc": float(roc_auc_score(y[va_idx], pred)),
                "n_iter": int(np.asarray(model.n_iter_).max()),
            }
        )
        del Xtr, Xva, tr_struct, va_struct, model

    if not np.isfinite(oof).all():
        raise AssertionError("M1 OOF predictions incomplete")

    m0_p = df["m0_probability"].to_numpy(dtype=float)
    m0_ll = float(log_loss(y, m0_p))
    m1_ll = float(log_loss(y, oof))
    m1_auc = float(roc_auc_score(y, oof))
    calibration = calibration_summary(y, oof)
    uncertainty = paired_session_bootstrap(
        df["session_id"].to_numpy(),
        per_row_log_loss(y, oof),
        per_row_log_loss(y, m0_p),
        int(cfg["uncertainty"]["replicates"]),
        int(cfg["uncertainty"]["random_seed"]),
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    oof_path = args.output_dir / "oof_predictions.csv"
    pd.DataFrame(
        {
            "response_id": df["response_id"],
            "session_id": df["session_id"],
            "fold": folds_arr,
            "is_correct": y,
            "m0_probability": m0_p,
            "m1_probability": oof,
        }
    ).sort_values("response_id").to_csv(oof_path, index=False, lineterminator="\n")

    env = {
        "python": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "cpu_count": os.cpu_count(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "scikit_learn": sklearn.__version__,
        "pyyaml": yaml.__version__,
    }
    result = {
        "schema_version": 1,
        "experiment_id": "M1",
        "status": "EXECUTED",
        "objective_information_present": False,
        "cca_derived_features_present": False,
        "data": {
            "responses": int(len(df)),
            "sessions": int(df["session_id"].nunique()),
        },
        "identity": {
            "dataset_index_sha256": sha256_file(args.index),
            "fold_artifact_sha256": observed_fold_hash,
            "m0_session_features_sha256": sha256_file(args.m0_session_features),
            "m0_oof_sha256": sha256_file(args.m0_oof),
            "config_sha256": sha256_file(args.config),
            "semantic_representation_sha256": stable_hash(cfg["semantic_representation"]),
            "ordinary_covariates_sha256": stable_hash(ordinary),
            "classifier_sha256": stable_hash(cfg["classifier"]),
            "runtime_environment_sha256": stable_hash(env),
        },
        "comparison": {
            "m0_pooled_log_loss_recomputed": m0_ll,
            "m1_pooled_log_loss": m1_ll,
            "delta_log_loss_m1_minus_m0": m1_ll - m0_ll,
            "m1_better_than_m0": bool(m1_ll < m0_ll),
            "m1_pooled_auc": m1_auc,
            "calibration": calibration,
            "uncertainty": uncertainty,
            "folds": fold_records,
        },
        "text_matrix": {
            "response_rows": int(X_text.shape[0]),
            "features": int(X_text.shape[1]),
            "nnz": int(X_text.nnz),
        },
        "environment": env,
        "authority": {
            "gained_if_diagnosed": [
                "generic_transcript_semantics_add_predictive_information_beyond_M0"
            ] if m1_ll < m0_ll else [],
            "not_gained": [
                "CCA_support",
                "CCA_refutation",
                "causal_evidence",
                "H_O_support",
                "G1_evidence",
                "PMC_evidence",
                "repeated_correction_evidence",
                "JT_evidence",
                "C_improve_measurement",
            ],
        },
    }
    record_path = args.output_dir / "m1_record.json"
    record_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
