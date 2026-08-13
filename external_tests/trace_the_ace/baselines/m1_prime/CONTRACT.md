# M1′ — Ordinary semantic estimator-repair successor

## Status

**AUTHORIZED PROSPECTIVE SUCCESSOR — RESULT UNOBSERVED AT FREEZE**

M1′ is a successor to the closed historical M1 experiment. It does not rewrite M1.

The only opened boundary is the estimator/convergence layer diagnosed after M1.

## Parent result

Historical M1 established, under its frozen identity:

```text
D1_information = PASS
D1_baseline    = UNRESOLVED
```

with pooled OOF log loss `0.5790941374560221`, but four of five outer-fold SGD fits terminated at the frozen `max_iter = 50` ceiling and raw ECE-10 was `0.0580493569617112` with mean predicted probability `0.7578927042603452` versus observed rate `0.7024692062043796`.

These observations motivate this successor. They do not alter the M1 result.

## Predictive object

M1′ preserves exactly:

\[
\boxed{M_1'=P(Y\mid T,X_{\mathrm{ordinary}})}
\]

The predictive question is deliberately narrow:

> Can the same generic transcript-semantic representation and the same ordinary covariates achieve stable estimation and materially reduced calibration residuals when the demonstrated iteration ceiling is removed?

## Locked parent structure

The following are unchanged from M1:

```text
T transcript contents and role-marker serialization
X_ordinary allowlist
objective-information exclusion
CCA-derived feature exclusion
HashingVectorizer family and all representation parameters
response weighting
SGDClassifier family
loss, penalty, alpha, tol, shuffle, random_state, average,
fit_intercept, class_weight, early_stopping
structural imputation and scaling
canonical session-grouped fold artifact
primary metric and diagnostics
```

Required fold SHA-256 remains:

```text
014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6
```

No objective field, objective embedding, objective-conditioned feature, CCA-derived feature, pretrained resource, new metadata feature, lexical feature change, or hyperparameter search is authorized.

## Sole estimator repair

The only classifier change is:

```text
M1:   max_iter = 50
M1′:  max_iter = 500
```

`tol = 1e-4` remains unchanged. The larger ceiling is not a tuning search; it permits the already-frozen stopping rule to operate instead of forcing four fits to terminate at the historical ceiling.

## Calibration

M1′ adds **no post-hoc calibrator**.

This is intentional. The first shallow repair tests whether proper estimator convergence itself resolves enough of the calibration residual. If it does not, calibration remains a separate successor layer rather than being bundled into this experiment.

Historical M1 calibration anchors are frozen as:

```text
M1 ECE-10                         = 0.0580493569617112
M1 absolute mean-probability bias = 0.0554234980559656
M1 Brier score                    = 0.19519137289395985
M1 pooled log loss                = 0.5790941374560221
```

For this successor, "materially reduced calibration residual" is prospectively defined as both:

```text
ECE-10 <= 0.75 * historical M1 ECE-10
absolute mean-probability bias <= 0.75 * historical M1 absolute bias
```

while preserving:

```text
M1′ pooled log loss <= historical M1 pooled log loss
M1′ Brier score <= historical M1 Brier score
```

The 25% reduction threshold is a diagnostic engineering gate, not a causal or theoretical significance threshold.

## Convergence gate

Estimator convergence passes only if every outer-fold fit terminates before the new ceiling:

\[
\boxed{\max_f n\_iter_f < 500}
\]

A fit that again reaches `max_iter` leaves the estimator boundary unresolved.

## Validation

M1′ inherits M1 validation byte-for-byte:

```text
grouping key = session_id
fold artifact = identical M0/M1 artifact
response rows = identical
primary metric = pooled OOF log loss
```

Objective-exclusion validation is repeated: predictions must be identical across response rows belonging to the same session.

## Comparison

Primary successor comparison:

\[
\Delta LL_{1'1}=LL(M_1')-LL(M_1).
\]

Paired session-cluster bootstrap:

```text
cluster                 = session_id
replicates              = 2000
random_seed             = 1702
interval                = percentile 95%
within-session handling = preserve all response rows together
```

This is predictive uncertainty only.

## Closing rule

M1′ closes the ordinary-baseline residual only if all of the following pass:

```text
1. every outer estimator terminates before max_iter=500
2. pooled log loss is no worse than historical M1
3. Brier score is no worse than historical M1
4. ECE-10 is reduced by at least 25% relative to historical M1
5. absolute mean-probability bias is reduced by at least 25%
6. objective exclusion remains exact
```

If all pass:

```text
D1_information = PASS
D1_baseline    = PASS
AUTH(M2)       = TRUE
```

If convergence passes but the calibration gate fails, the next shallowest successor is calibration only. M2 remains unauthorized.

## Authority ceiling

M1′ can earn only that the ordinary semantic baseline is sufficiently stable/calibrated to serve as the comparison model for M2 under this validation regime.

It cannot establish CCA support or refutation, causal tutoring effects, H_O, G1, PMC, repeated correction, JT, or `C_improve`.
