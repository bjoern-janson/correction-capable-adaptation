#!/usr/bin/env python3
"""Execute frozen Trace the Ace M2 objective-conditioning experiment.

M2 preserves the calibrated ordinary semantic baseline and adds only objective information.
It includes an objective-main-effect control (M2_O) and a separate lexical interaction
(M2) so objective identity/content is not conflated with objective-conditioned relevance.
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


def make_calibrator(cfg: dict) -> LogisticRegression:
    return LogisticRegression(
        penalty=cfg["penalty"], solver=cfg["solver"], fit_intercept=bool(cfg["fit_intercept"]),
        max_iter=int(cfg["max_iter"]), tol=float(cfg["tol"]), class_weight=cfg["class_weight"]
    )


def normalize_objective(text: str) -> str:
    return " ".join((text or "").split())


def structured_train_val(X_struct_raw, tr_idx, va_idx):
    tr_struct = X_struct_raw[tr_idx].copy(); va_struct = X_struct_raw[va_idx].copy()
    medians = np.nanmedian(tr_struct, axis=0)
    tr_nan = np.where(np.isnan(tr_struct)); va_nan = np.where(np.isnan(va_struct))
    tr_struct[tr_nan] = medians[tr_nan[1]]; va_struct[va_nan] = medians[va_nan[1]]
    scaler = StandardScaler()
    return scaler.fit_transform(tr_struct).astype(np.float32), scaler.transform(va_struct).astype(np.float32)


def fit_score(parent, arm, X_text, X_obj, X_inter, X_struct_raw, y, tr_idx, va_idx, classifier_cfg):
    tr_struct, va_struct = structured_train_val(X_struct_raw, tr_idx, va_idx)
    tr_blocks = [X_text[tr_idx], X_obj[tr_idx]]; va_blocks = [X_text[va_idx], X_obj[va_idx]]
    if arm == "M2":
        tr_blocks.append(X_inter[tr_idx]); va_blocks.append(X_inter[va_idx])
    elif arm != "M2_O":
        raise AssertionError(f"unknown arm {arm}")
    tr_blocks.append(sparse.csr_matrix(tr_struct)); va_blocks.append(sparse.csr_matrix(va_struct))
    Xtr = sparse.hstack(tr_blocks, format="csr", dtype=np.float32)
    Xva = sparse.hstack(va_blocks, format="csr", dtype=np.float32)
    model = parent.make_classifier(classifier_cfg); model.fit(Xtr, y[tr_idx])
    return np.asarray(model.decision_function(Xva), dtype=float).reshape(-1), int(np.asarray(model.n_iter_).max())


def run_arm(parent, arm, X_text, X_obj, X_inter, X_struct_raw, y, groups, folds_arr, cfg):
    raw_scores = np.full(len(y), np.nan); cal_p = np.full(len(y), np.nan); records = []
    inner_cfg = cfg["inner_crossfit"]; max_iter = int(cfg["base_classifier"]["max_iter"]); all_converged = True
    for outer in sorted(int(x) for x in np.unique(folds_arr)):
        outer_tr = np.flatnonzero(folds_arr != outer); outer_va = np.flatnonzero(folds_arr == outer)
        if set(groups[outer_tr]) & set(groups[outer_va]): raise AssertionError(f"outer leakage {outer}")
        outer_score, outer_n_iter = fit_score(parent, arm, X_text, X_obj, X_inter, X_struct_raw, y, outer_tr, outer_va, cfg["base_classifier"])
        raw_scores[outer_va] = outer_score; outer_converged = outer_n_iter < max_iter
        inner_scores = np.full(len(outer_tr), np.nan); inner_iters = []
        splitter = StratifiedGroupKFold(n_splits=int(inner_cfg["n_splits"]), shuffle=bool(inner_cfg["shuffle"]), random_state=int(inner_cfg["random_state"]))
        y_outer = y[outer_tr]; g_outer = groups[outer_tr]
        for itr, iva in splitter.split(np.zeros(len(outer_tr), dtype=np.int8), y_outer, groups=g_outer):
            tr = outer_tr[itr]; va = outer_tr[iva]
            if set(groups[tr]) & set(groups[va]): raise AssertionError(f"inner leakage {outer}")
            score, n_iter = fit_score(parent, arm, X_text, X_obj, X_inter, X_struct_raw, y, tr, va, cfg["base_classifier"])
            inner_scores[iva] = score; inner_iters.append(n_iter)
        if not np.isfinite(inner_scores).all(): raise AssertionError(f"inner scores incomplete {outer} {arm}")
        inner_converged = all(n < max_iter for n in inner_iters); all_converged &= outer_converged and inner_converged
        calibrator = make_calibrator(cfg["calibrator"]); calibrator.fit(inner_scores.reshape(-1, 1), y_outer)
        pred = calibrator.predict_proba(outer_score.reshape(-1, 1))[:, 1]; cal_p[outer_va] = pred
        raw_p = 1.0 / (1.0 + np.exp(-outer_score)); raw_metrics = parent.calibration_summary(y[outer_va], raw_p); cal_metrics = parent.calibration_summary(y[outer_va], pred)
        records.append({"fold": outer, "responses": int(len(outer_va)), "sessions": int(pd.Series(groups[outer_va]).nunique()), "raw_log_loss": float(log_loss(y[outer_va], raw_p)), "calibrated_log_loss": float(log_loss(y[outer_va], pred)), "raw_brier": raw_metrics["brier_score"], "calibrated_brier": cal_metrics["brier_score"], "raw_ece_10": raw_metrics["ece_10_equal_width"], "calibrated_ece_10": cal_metrics["ece_10_equal_width"], "outer_base_n_iter": outer_n_iter, "outer_base_converged": outer_converged, "inner_base_n_iter": inner_iters, "inner_base_converged": inner_converged, "platt_slope": float(calibrator.coef_[0,0]), "platt_intercept": float(calibrator.intercept_[0])})
    if not np.isfinite(raw_scores).all() or not np.isfinite(cal_p).all(): raise AssertionError(f"incomplete {arm}")
    return raw_scores, cal_p, records, all_converged


def objective_variation_check(df, X_obj):
    for _, idxs_raw in df.groupby("session_id", sort=False).indices.items():
        idxs = np.asarray(idxs_raw, dtype=int)
        if len(idxs) < 2: continue
        ids = df.iloc[idxs]["learning_objective_id"].astype(str).to_numpy()
        if len(set(ids)) < 2: continue
        base = X_obj[idxs[0]]
        if any((base != X_obj[j]).nnz > 0 for j in idxs[1:]): return True
    return False


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--index", required=True, type=Path); ap.add_argument("--folds", required=True, type=Path); ap.add_argument("--m0-session-features", required=True, type=Path); ap.add_argument("--m1-cal-oof", required=True, type=Path); ap.add_argument("--transcripts-root", action="append", required=True, type=Path); ap.add_argument("--config", required=True, type=Path); ap.add_argument("--output-dir", required=True, type=Path); ap.add_argument("--batch-size", type=int, default=128); ap.add_argument("--parent-runner", type=Path, default=None); args = ap.parse_args()
    cfg = yaml.safe_load(args.config.read_text());
    if cfg["experiment_id"] != "M2" or bool(cfg["cca_derived_features_allowed"]): raise AssertionError("invalid M2 config")
    parent_path = resolve_parent_runner(args.parent_runner); parent = load_parent(parent_path)
    fold_hash = parent.sha256_file(args.folds); parent_hash = parent.sha256_file(args.m1_cal_oof)
    if fold_hash != cfg["fold_sha256_required"]: raise AssertionError("fold mismatch")
    if parent_hash != cfg["parent_oof_sha256_required"]: raise AssertionError("parent OOF mismatch")
    index = pd.read_csv(args.index); folds = pd.read_csv(args.folds); m0 = pd.read_csv(args.m0_session_features); pf = pd.read_csv(args.m1_cal_oof)
    req = ["response_id","session_id","learning_objective_id","learning_objective","is_correct"]
    if any(c not in index for c in req): raise AssertionError("index fields missing")
    ordinary = list(cfg["ordinary_covariates"]); parent_col = cfg["parent_probability_column"]
    df = index[req].merge(folds, on="session_id", validate="many_to_one").merge(m0[["session_id",*ordinary]], on="session_id", validate="many_to_one").merge(pf[["response_id",parent_col]], on="response_id", validate="one_to_one")
    if df[[*req,"fold",parent_col]].isna().any().any(): raise AssertionError("missing values")
    id_text = df[["learning_objective_id","learning_objective"]].drop_duplicates().assign(learning_objective=lambda x:x["learning_objective"].map(normalize_objective))
    one_to_one = bool((id_text.groupby("learning_objective_id")["learning_objective"].nunique()==1).all() and (id_text.groupby("learning_objective")["learning_objective_id"].nunique()==1).all())
    sessions = sorted(df["session_id"].astype(str).unique()); paths = parent.transcript_path_map(args.transcripts_root)
    if set(paths) != set(sessions): raise AssertionError("transcript coverage")
    vec = parent.make_vectorizer(cfg["semantic_representation"]); Xs = parent.build_session_text_matrix(sessions, paths, vec, cfg["text_serialization"]["role_markers"], args.batch_size)
    sidmap={s:i for i,s in enumerate(sessions)}; ridx=np.fromiter((sidmap[str(s)] for s in df["session_id"]),dtype=np.int32); X_text=Xs[ridx].tocsr(); del Xs
    ot = df[["learning_objective_id","learning_objective"]].drop_duplicates("learning_objective_id").sort_values("learning_objective_id").reset_index(drop=True); ot["norm"]=ot["learning_objective"].map(normalize_objective)
    Xou=vec.transform(ot["norm"].tolist()).tocsr().astype(np.float32); omap={str(o):i for i,o in enumerate(ot["learning_objective_id"])}; oidx=np.fromiter((omap[str(o)] for o in df["learning_objective_id"]),dtype=np.int32); X_obj=Xou[oidx].tocsr(); del Xou
    X_inter=X_text.multiply(X_obj).tocsr().astype(np.float32); X_inter.eliminate_zeros()
    y=df["is_correct"].to_numpy(dtype=np.int8); groups=df["session_id"].astype(str).to_numpy(); fa=df["fold"].to_numpy(dtype=np.int16); Xsr=df[ordinary].to_numpy(dtype=float); parent_p=df[parent_col].to_numpy(dtype=float)
    _, cp, cf, cc = run_arm(parent,"M2_O",X_text,X_obj,X_inter,Xsr,y,groups,fa,cfg); _, fp, ff, fc = run_arm(parent,"M2",X_text,X_obj,X_inter,Xsr,y,groups,fa,cfg)
    pll=float(log_loss(y,parent_p)); cll=float(log_loss(y,cp)); fll=float(log_loss(y,fp)); pcal=parent.calibration_summary(y,parent_p); ccal=parent.calibration_summary(y,cp); fcal=parent.calibration_summary(y,fp); pbias=abs(pcal["mean_probability"]-pcal["observed_rate"]); fbias=abs(fcal["mean_probability"]-fcal["observed_rate"])
    boot=lambda a,b,seed: parent.paired_session_bootstrap(groups,parent.per_row_log_loss(y,a),parent.per_row_log_loss(y,b),int(cfg["uncertainty"]["replicates"]),int(seed))
    tu=boot(fp,parent_p,cfg["uncertainty"]["random_seed_total"]); iu=boot(fp,cp,cfg["uncertainty"]["random_seed_interaction"]); mu=boot(cp,parent_p,cfg["uncertainty"]["random_seed_main_effect"])
    ig={"objective_id_text_mapping_one_to_one":one_to_one,"objective_block_nonzero":bool(X_obj.nnz>0),"interaction_block_nonzero":bool(X_inter.nnz>0),"objective_feature_rows_differ_within_multiobjective_session":objective_variation_check(df,X_obj),"control_all_outer_and_inner_base_models_converged":bool(cc),"full_all_outer_and_inner_base_models_converged":bool(fc)}
    tg={"point_log_loss_improvement":bool(fll<pll),"bootstrap_ci95_upper_below_zero":bool(tu["ci95_upper"]<0)}; hg={"point_log_loss_improvement_over_main_effect_control":bool(fll<cll),"bootstrap_ci95_upper_below_zero":bool(iu["ci95_upper"]<0)}; cg={"brier_not_worse_than_parent":bool(fcal["brier_score"]<=pcal["brier_score"]),"ece_10_not_worse_than_parent":bool(fcal["ece_10_equal_width"]<=pcal["ece_10_equal_width"]),"absolute_mean_probability_bias_not_worse_than_parent":bool(fbias<=pbias)}
    ip=all(ig.values()); tp=all(tg.values()); hp=all(hg.values()); calp=all(cg.values()); passed=ip and tp and hp and calp
    args.output_dir.mkdir(parents=True,exist_ok=True); pd.DataFrame({"response_id":df["response_id"],"session_id":df["session_id"],"learning_objective_id":df["learning_objective_id"],"fold":fa,"is_correct":y,"m1_cal_probability":parent_p,"m2_o_probability":cp,"m2_probability":fp}).sort_values("response_id").to_csv(args.output_dir/"oof_predictions.csv",index=False,lineterminator="\n")
    env={"python":sys.version.split()[0],"platform":platform.platform(),"numpy":np.__version__,"pandas":pd.__version__,"scipy":scipy.__version__,"scikit_learn":sklearn.__version__}
    result={"schema_version":1,"experiment_id":"M2","hypothesis_id":"H_O","status":"DIAGNOSED_PASS" if passed else "DIAGNOSED_UNRESOLVED","cca_derived_features_present":False,"representation_audit":{"unique_objective_ids":int(df["learning_objective_id"].nunique()),"unique_objective_texts":int(df["learning_objective"].map(normalize_objective).nunique()),"objective_matrix_nnz":int(X_obj.nnz),"interaction_matrix_nnz":int(X_inter.nnz),"implementation_gates":ig},"comparison":{"m1_cal":{"log_loss":pll,"auc":float(roc_auc_score(y,parent_p)),"calibration":pcal,"absolute_mean_probability_bias":pbias},"m2_o_main_effect_control":{"log_loss":cll,"delta_log_loss_vs_m1_cal":cll-pll,"auc":float(roc_auc_score(y,cp)),"calibration":ccal,"folds":cf,"uncertainty_vs_m1_cal":mu},"m2_conditioned":{"log_loss":fll,"delta_log_loss_vs_m1_cal":fll-pll,"delta_log_loss_vs_m2_o":fll-cll,"auc":float(roc_auc_score(y,fp)),"calibration":fcal,"absolute_mean_probability_bias":fbias,"folds":ff,"uncertainty_vs_m1_cal":tu,"uncertainty_vs_m2_o":iu}},"gates":{"implementation":ig,"total_objective_information":tg,"H_O_objective_conditioning":hg,"calibration_preservation":cg},"diagnosis":{"implementation_gate":"PASS" if ip else "FAIL","total_objective_information_gate":"PASS" if tp else "FAIL","H_O_gate":"PASS" if hp else "FAIL","calibration_preservation_gate":"PASS" if calp else "FAIL","M2_baseline_gate":"PASS" if passed else "UNRESOLVED","cca_feature_families_authorized":bool(passed)},"authority":{"gained":["H_O_operationalization_predictively_supported","M2_objective_conditioned_baseline_passed","CCA_derived_feature_families_may_be_opened"] if passed else [],"conditional_local_findings":{"objective_main_effect_predictive":bool(cll<pll and mu["ci95_upper"]<0),"total_objective_information_predictive":bool(tp),"objective_conditioning_predictive_beyond_main_effect":bool(hp)},"not_gained":["CCA_support","CCA_refutation","causal_evidence","G1_evidence","PMC_evidence","repeated_correction_evidence","JT_evidence","C_improve_measurement"]},"environment":env}
    (args.output_dir/"m2_record.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n"); print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == "__main__": main()
