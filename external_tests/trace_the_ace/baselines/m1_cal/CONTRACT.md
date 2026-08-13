# M1-cal — Calibration-only successor contract

## Status

**AUTHORIZED PROSPECTIVE SUCCESSOR — RESULT UNOBSERVED AT FREEZE**

M1-cal is a calibration-only successor to historical M1-prime.

It does not reopen transcript representation, ordinary covariates, objective exclusion,
CCA-feature exclusion, outer folds, base-estimator family, or base-estimator training.

## Frozen parent object

The outer raw predictor remains exactly:

\[
M_1' = P(Y\mid T,X_{\mathrm{ordinary}})
\]

as recorded by the historical M1-prime OOF artifact.

No outer base model is retrained for this comparison. The historical M1-prime raw
probabilities are treated as the frozen parent output.

## Opened boundary

Only the probability interpretation is opened:

\[
\boxed{s_i \rightarrow \hat p_i}
\]

where the raw score is the logit of the frozen M1-prime probability:

\[
s_i=\operatorname{logit}(p_i^{M_1'}).
\]

The calibration map is prospectively fixed as Platt scaling:

\[
\boxed{g(s)=\sigma(a s+b)}.
\]

No alternative calibrator is compared inside this experiment.

## Leakage-safe calibration fitting

For outer fold k:

1. keep the historical M1-prime predictions for outer validation fold k frozen;
2. within the outer training sessions only, create five session-grouped stratified inner folds;
3. generate inner OOF raw scores using the exact frozen M1-prime semantic representation,
   ordinary covariates, preprocessing, and base classifier;
4. fit the two-parameter Platt map on those inner OOF scores and labels only;
5. apply that map to the historical raw scores of outer validation fold k.

Thus no outer-validation label trains its own calibrator, and calibrator-training scores are
not produced by models that were trained on the outer-validation fold.

Inner split:

```text
method       StratifiedGroupKFold
n_splits     5
shuffle      true
random_state 1703
group        session_id
```

## Frozen inherited structure

Unchanged from M1-prime:

```text
predictive object                P(Y|T,X_ordinary)
objective information            forbidden
CCA-derived features             forbidden
outer fold SHA-256               014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6
text serialization               unchanged
HashingVectorizer                unchanged
ordinary covariate allowlist     unchanged
structural imputation/scaling    unchanged
SGDClassifier family/parameters  unchanged
pretrained resources             none
outer raw predictions            historical/frozen
```

The base classifier used only to generate inner calibration-training scores is exactly the
M1-prime classifier, including `max_iter=500`.

## Platt calibrator

```text
LogisticRegression
input             one raw score s
penalty           none
solver            lbfgs
fit_intercept     true
max_iter          1000
tol               1e-8
class_weight      null
```

This is a two-parameter probability map, not a new semantic model.

## Primary question

> Can a leakage-safe calibration map improve the predictive consequence and materially
> repair probability calibration while preserving the already-earned semantic signal?

## Prospective gates

Let raw denote historical M1-prime and cal denote M1-cal.

M1-cal closes the calibration boundary only if all hold:

\[
LL_{cal}<LL_{raw}
\]

\[
Brier_{cal}\le Brier_{raw}
\]

\[
ECE_{cal}\le 0.75\,ECE_{raw}
\]

\[
|\bar p_{cal}-\bar y|\le0.75\,|\bar p_{raw}-\bar y|
\]

and objective exclusion remains exact, with every inner base-model fit terminating before the frozen 500-iteration ceiling.

The 25% ECE and mean-bias thresholds are inherited as the unresolved material-calibration
standard from M1-prime. They are not chosen after observing M1-cal.

Fold-wise raw/calibrated log loss, Brier, ECE, mean bias, Platt slope/intercept, and inner-model iteration counts are
reported diagnostically. No post-result fold-count threshold is introduced.

## Uncertainty

Primary log-loss difference uses the same paired session-cluster bootstrap family:

```text
comparison   M1-cal minus M1-prime
cluster      session_id
replicates   2000
seed         1704
interval     percentile 95%
```

## Authority ceiling

If all gates pass, authority gained is limited to:

> Under this frozen ordinary-semantic baseline and validation regime, the residual
> probability-calibration defect can be repaired by the specified training-side
> cross-fitted Platt map without sacrificing held-out log loss.

Only then may the ordinary-baseline gate close and M2 be considered for authorization.

No result from this experiment supports or refutes CCA, causation, H_O, G1, PMC, repeated
correction, JT, or C_improve.
