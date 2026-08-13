#!/usr/bin/env python3
"""Calibration-only successor to frozen M1-prime.

Outer M1-prime probabilities are historical and never retrained here. The only evaluated
change is a Platt map fitted from leakage-safe inner session-grouped OOF raw scores inside
each outer training partition.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from scipy import sparse
import sklearn
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler


def load_parent(path: Path):
    spec = importlib.util.spec_from_file_location("m1_prime_parent", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import parent runner: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_parent_runner(arg: Path | None) -> Path:
    if arg is not None:
        return arg
    return Path(__file__).resolve().parents[1] / "m1_prime" / "train.py"


def raw_score_from_probability(p: np.ndarray) -> np.ndarray:
    if np.any((p <= 0.0) | (p >= 1.0)):
        raise AssertionError("parent probabilities must be strictly inside (0,1) for exact logit")
    return np.log(p) - np.log1p(-p)


def make_calibrator(cfg: dict) -> LogisticRegression:
    return LogisticRegression(
        penalty=cfg["penalty"],
        solver=cfg["solver"],
        fit_intercept=bool(cfg["fit_intercept"]),
        max_iter=int(cfg["max_iter"]),
        tol=float(cfg["tol"]),
        class_weight=cfg["class_weight"],
    )


def fit_structured_blocks(
    parent,
    X_text: sparse.csr_matrix,
    X_struct_raw: np.ndarray,
    y: np.ndarray,
    tr_idx: np.ndarray,
    va_idx: np.ndarray,
    classifier_cfg: dict,
) -> tuple[np.ndarray, int]:
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
    model = parent.make_classifier(classifier_cfg)
    model.fit(Xtr, y[tr_idx])
    score = np.asarray(model.decision_function(Xva), dtype=float).reshape(-1)
    n_iter = int(np.asarray(model.n_iter_).max())
    return score, n_iter


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--folds", required=True, type=Path)
    ap.add_argument("--m0-session-features", required=True, type=Path)
    ap.add_argument("--m1-prime-oof", required=True, type=Path)
    ap.add_argument("--transcripts-root", action="append", required=True, type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--batch-size", type=int, default=128)
    ap.add_argument("--parent-runner", type=Path, default=None)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if cfg["experiment_id"] != "M1_CAL":
        raise AssertionError("wrong experiment config")
    if bool(cfg["objective_information_allowed"]):
        raise AssertionError("objective information must remain disabled")
    if bool(cfg["cca_derived_features_allowed"]):
        raise AssertionError("CCA-derived features must remain disabled")

    parent_path = resolve_parent_runner(args.parent_runner)
    parent = load_parent(parent_path)

    fold_hash = parent.sha256_file(args.folds)
    if fold_hash != cfg["fold_sha256_required"]:
        raise AssertionError(f"fold artifact mismatch: {fold_hash}")
    parent_oof_hash = parent.sha256_file(args.m1_prime_oof)
    if parent_oof_hash != cfg["parent_oof_sha256_required"]:
        raise AssertionError(f"parent OOF mismatch: {parent_oof_hash}")

    index = pd.read_csv(args.index)
    folds = pd.read_csv(args.folds)
    m0_features = pd.read_csv(args.m0_session_features)
    pfile = pd.read_csv(args.m1_prime_oof)
    if not index["response_id"].is_unique or not folds["session_id"].is_unique:
        raise AssertionError("non-unique response or fold identity")
    if not m0_features["session_id"].is_unique or not pfile["response_id"].is_unique:
        raise AssertionError("non-unique feature or parent prediction identity")

    parent_col = "m1_prime_probability"
    if parent_col not in pfile.columns:
        raise AssertionError(f"parent OOF missing {parent_col}")

    df = index[["response_id", "session_id", "is_correct"]].merge(
        folds, on="session_id", validate="many_to_one"
    )
    ordinary = list(cfg["ordinary_covariates"])
    df = df.merge(
        m0_features[["session_id", *ordinary]], on="session_id", validate="many_to_one"
    )
    df = df.merge(
        pfile[["response_id", parent_col]], on="response_id", validate="one_to_one"
    )
    if df.isna().loc[:, ["response_id", "session_id", "is_correct", "fold", parent_col]].any().any():
        raise AssertionError("missing required joined values")

    sessions = sorted(df["session_id"].unique())
    path_map = parent.transcript_path_map(args.transcripts_root)
    if set(path_map) != set(sessions):
        raise AssertionError("transcript coverage mismatch")
    vectorizer = parent.make_vectorizer(cfg["semantic_representation"])
    X_session = parent.build_session_text_matrix(
        sessions,
        path_map,
        vectorizer,
        cfg["text_serialization"]["role_markers"],
        args.batch_size,
    )
    sid_to_row = {sid: i for i, sid in enumerate(sessions)}
    response_session_idx = np.fromiter((sid_to_row[s] for s in df["session_id"]), dtype=np.int32)
    X_text = X_session[response_session_idx].tocsr()
    del X_session

    y = df["is_correct"].to_numpy(dtype=np.int8)
    groups = df["session_id"].to_numpy()
    folds_arr = df["fold"].to_numpy(dtype=np.int16)
    X_struct_raw = df[ordinary].to_numpy(dtype=float)
    raw_p = df[parent_col].to_numpy(dtype=float)
    raw_s = raw_score_from_probability(raw_p)
    if not np.allclose(1.0 / (1.0 + np.exp(-raw_s)), raw_p, rtol=0.0, atol=2e-15):
        raise AssertionError("raw score inversion does not reproduce parent probabilities")

    cal_p = np.full(len(df), np.nan, dtype=float)
    fold_records: list[dict] = []
    inner_cfg = cfg["inner_crossfit"]
    max_iter = int(cfg["base_classifier"]["max_iter"])
    all_inner_converged = True

    for outer in sorted(int(x) for x in np.unique(folds_arr)):
        outer_tr = np.flatnonzero(folds_arr != outer)
        outer_va = np.flatnonzero(folds_arr == outer)
        if set(groups[outer_tr]) & set(groups[outer_va]):
            raise AssertionError(f"outer session leakage in fold {outer}")

        inner_scores = np.full(len(outer_tr), np.nan, dtype=float)
        inner_iters: list[int] = []
        splitter = StratifiedGroupKFold(
            n_splits=int(inner_cfg["n_splits"]),
            shuffle=bool(inner_cfg["shuffle"]),
            random_state=int(inner_cfg["random_state"]),
        )
        y_outer = y[outer_tr]
        g_outer = groups[outer_tr]
        for inner_train_rel, inner_val_rel in splitter.split(
            np.zeros(len(outer_tr), dtype=np.int8), y_outer, groups=g_outer
        ):
            inner_train = outer_tr[inner_train_rel]
            inner_val = outer_tr[inner_val_rel]
            if set(groups[inner_train]) & set(groups[inner_val]):
                raise AssertionError(f"inner session leakage outer={outer}")
            score, n_iter = fit_structured_blocks(
                parent,
                X_text,
                X_struct_raw,
                y,
                inner_train,
                inner_val,
                cfg["base_classifier"],
            )
            inner_scores[inner_val_rel] = score
            inner_iters.append(n_iter)
        if not np.isfinite(inner_scores).all():
            raise AssertionError(f"inner OOF scores incomplete outer={outer}")
        fold_inner_converged = all(n < max_iter for n in inner_iters)
        all_inner_converged = all_inner_converged and fold_inner_converged

        calibrator = make_calibrator(cfg["calibrator"])
        calibrator.fit(inner_scores.reshape(-1, 1), y_outer)
        pred = calibrator.predict_proba(raw_s[outer_va].reshape(-1, 1))[:, 1]
        cal_p[outer_va] = pred

        raw_metrics = parent.calibration_summary(y[outer_va], raw_p[outer_va])
        cal_metrics = parent.calibration_summary(y[outer_va], pred)
        raw_ll = float(log_loss(y[outer_va], raw_p[outer_va]))
        cal_ll = float(log_loss(y[outer_va], pred))
        fold_records.append(
            {
                "fold": outer,
                "responses": int(len(outer_va)),
                "sessions": int(pd.Series(groups[outer_va]).nunique()),
                "raw_log_loss": raw_ll,
                "calibrated_log_loss": cal_ll,
                "delta_log_loss_cal_minus_raw": cal_ll - raw_ll,
                "raw_brier": raw_metrics["brier_score"],
                "calibrated_brier": cal_metrics["brier_score"],
                "raw_ece_10": raw_metrics["ece_10_equal_width"],
                "calibrated_ece_10": cal_metrics["ece_10_equal_width"],
                "raw_mean_bias": abs(raw_metrics["mean_probability"] - raw_metrics["observed_rate"]),
                "calibrated_mean_bias": abs(cal_metrics["mean_probability"] - cal_metrics["observed_rate"]),
                "platt_slope": float(calibrator.coef_[0, 0]),
                "platt_intercept": float(calibrator.intercept_[0]),
                "platt_n_iter": int(np.asarray(calibrator.n_iter_).max()),
                "inner_base_n_iter": inner_iters,
                "inner_base_converged": fold_inner_converged,
            }
        )

    if not np.isfinite(cal_p).all():
        raise AssertionError("calibrated OOF incomplete")

    raw_cal = parent.calibration_summary(y, raw_p)
    cal_cal = parent.calibration_summary(y, cal_p)
    raw_ll = float(log_loss(y, raw_p))
    cal_ll = float(log_loss(y, cal_p))
    raw_auc = float(roc_auc_score(y, raw_p))
    cal_auc = float(roc_auc_score(y, cal_p))
    raw_bias = abs(raw_cal["mean_probability"] - raw_cal["observed_rate"])
    cal_bias = abs(cal_cal["mean_probability"] - cal_cal["observed_rate"])
    gates_cfg = cfg["prospective_gates"]
    frac = 1.0 - float(gates_cfg["ece_relative_reduction_minimum"])

    objective_ranges = (
        pd.DataFrame({"session_id": df["session_id"], "p": cal_p})
        .groupby("session_id")["p"]
        .agg(lambda x: float(x.max() - x.min()))
    )
    objective_exact = bool(float(objective_ranges.max()) == 0.0)

    gate_results = {
        "pooled_log_loss_strictly_better_than_parent": bool(cal_ll < raw_ll),
        "brier_not_worse_than_parent": bool(cal_cal["brier_score"] <= raw_cal["brier_score"]),
        "ece_relative_reduction_minimum": bool(cal_cal["ece_10_equal_width"] <= frac * raw_cal["ece_10_equal_width"]),
        "absolute_mean_probability_bias_relative_reduction_minimum": bool(cal_bias <= frac * raw_bias),
        "objective_exclusion_exact": objective_exact,
        "inner_base_models_converged": bool(all_inner_converged),
    }
    calibration_gate_pass = all(gate_results.values())

    uncertainty = parent.paired_session_bootstrap(
        groups,
        parent.per_row_log_loss(y, cal_p),
        parent.per_row_log_loss(y, raw_p),
        int(cfg["uncertainty"]["replicates"]),
        int(cfg["uncertainty"]["random_seed"]),
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_oof = args.output_dir / "oof_predictions.csv"
    pd.DataFrame(
        {
            "response_id": df["response_id"],
            "session_id": df["session_id"],
            "fold": folds_arr,
            "is_correct": y,
            "m1_prime_probability": raw_p,
            "m1_cal_probability": cal_p,
        }
    ).sort_values("response_id").to_csv(out_oof, index=False, lineterminator="\n")

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
        "experiment_id": "M1_CAL",
        "parent_experiment_id": "M1_PRIME",
        "status": "DIAGNOSED_PASS" if calibration_gate_pass else "DIAGNOSED_UNRESOLVED",
        "objective_information_present": False,
        "cca_derived_features_present": False,
        "identity": {
            "dataset_index_sha256": parent.sha256_file(args.index),
            "fold_artifact_sha256": fold_hash,
            "m0_session_features_sha256": parent.sha256_file(args.m0_session_features),
            "parent_oof_sha256": parent_oof_hash,
            "config_sha256": parent.sha256_file(args.config),
            "parent_runner_sha256": parent.sha256_file(parent_path),
            "semantic_representation_sha256": parent.stable_hash(cfg["semantic_representation"]),
            "ordinary_covariates_sha256": parent.stable_hash(ordinary),
            "base_classifier_sha256": parent.stable_hash(cfg["base_classifier"]),
            "calibrator_sha256": parent.stable_hash(cfg["calibrator"]),
            "runtime_environment_sha256": parent.stable_hash(env),
        },
        "comparison": {
            "raw_m1_prime_log_loss": raw_ll,
            "calibrated_log_loss": cal_ll,
            "delta_log_loss_cal_minus_raw": cal_ll - raw_ll,
            "raw_auc": raw_auc,
            "calibrated_auc": cal_auc,
            "raw_calibration": raw_cal,
            "calibrated_calibration": cal_cal,
            "raw_absolute_mean_probability_bias": raw_bias,
            "calibrated_absolute_mean_probability_bias": cal_bias,
            "ece_relative_reduction": 1.0 - cal_cal["ece_10_equal_width"] / raw_cal["ece_10_equal_width"],
            "absolute_mean_bias_relative_reduction": 1.0 - cal_bias / raw_bias,
            "folds": fold_records,
            "uncertainty": uncertainty,
        },
        "gates": gate_results,
        "diagnosis": {
            "calibration_gate": "PASS" if calibration_gate_pass else "FAIL",
            "baseline_gate": "PASS" if calibration_gate_pass else "UNRESOLVED",
            "m2_authorized": bool(calibration_gate_pass),
            "shallowest_remaining_boundary": None if calibration_gate_pass else "probability_calibration",
        },
        "authority": {
            "inherited": [
                "generic_transcript_semantics_add_predictive_information_beyond_M0",
                "convergence_boundary_resolved",
            ],
            "gained": (["ordinary_semantic_probability_calibration_repaired", "M2_may_be_opened"] if calibration_gate_pass else []),
            "not_gained": [
                "CCA_support", "CCA_refutation", "causal_evidence", "H_O_support",
                "G1_evidence", "PMC_evidence", "repeated_correction_evidence",
                "JT_evidence", "C_improve_measurement",
            ],
        },
        "environment": env,
    }
    (args.output_dir / "m1_cal_record.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
