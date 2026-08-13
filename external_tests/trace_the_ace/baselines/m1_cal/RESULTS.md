# M1-cal Results and Diagnosis

## Status

**EXECUTED — DIAGNOSED PASS — CALIBRATION BOUNDARY CLOSED — M2 AUTHORIZED BUT NOT OPENED**

M1-cal preserved the historical M1-prime raw predictor and changed only the probability mapping through leakage-safe, training-side cross-fitted Platt scaling.

## Primary result

```text
M1-prime pooled log loss   0.5765421662
M1-cal pooled log loss     0.5683582154
Delta LL (cal - raw)      -0.0081839508
raw pooled AUC             0.6765416347
calibrated pooled AUC      0.6765200311
```

Paired 2,000-replicate session-cluster bootstrap:

```text
95% CI for Delta LL        [-0.0100279869, -0.0062702495]
clusters                    22,821 sessions
```

All five outer folds improve in log loss.

## Calibration

```text
Brier                 0.1944457863 -> 0.1921277205
ECE-10                0.0518984518 -> 0.0159898481
absolute mean bias    0.0493119861 -> 0.0105359299
ECE relative reduction       69.19%
mean-bias relative reduction 78.63%
```

The prospectively frozen material-calibration threshold was 25% for both ECE and absolute mean-probability bias. Both thresholds pass.

## Fold diagnostics

| fold | ΔLL cal-raw | raw ECE | cal ECE | raw bias | cal bias | Platt slope | intercept | inner n_iter |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | -0.004397 | 0.0412 | 0.0104 | 0.0381 | 0.0038 | 0.8207 | -0.0508 | [63, 90, 103, 87, 81] |
| 1 | -0.007836 | 0.0508 | 0.0210 | 0.0487 | 0.0098 | 0.7499 | -0.0624 | [49, 63, 54, 75, 42] |
| 2 | -0.016544 | 0.0688 | 0.0139 | 0.0683 | 0.0018 | 0.7002 | -0.0403 | [113, 37, 36, 59, 34] |
| 3 | -0.005285 | 0.0491 | 0.0253 | 0.0440 | 0.0253 | 0.6921 | -0.0560 | [75, 39, 42, 35, 36] |
| 4 | -0.006858 | 0.0499 | 0.0191 | 0.0475 | 0.0156 | 0.7198 | -0.0516 | [59, 59, 32, 50, 56] |

Every inner base fit terminates before the frozen 500-iteration ceiling. Objective exclusion remains exact because the calibration map is applied to identical within-session parent scores; the measured maximum within-session prediction range is exactly `0.0`.

## Prospective gate adjudication

```text
absolute_mean_probability_bias_relative_reduction_minimum: PASS
brier_not_worse_than_parent: PASS
ece_relative_reduction_minimum: PASS
inner_base_models_converged: PASS
objective_exclusion_exact: PASS
pooled_log_loss_strictly_better_than_parent: PASS
```

Therefore:

```text
calibration gate   PASS
baseline gate      PASS
AUTH(M2)           TRUE
```

## Interpretation

Authority earned is limited to the ordinary semantic baseline: the residual probability-calibration defect is repaired by the specified leakage-safe Platt map while improving held-out log loss. Generic transcript semantics remain the source of the predictive representation; calibration repairs probability interpretation rather than adding objective or CCA-derived information.

M2 is now authorized as a successor experiment, but this artifact does not test `H_O` and does not implement objective conditioning.

## Authority not gained

No authority is gained for CCA support or refutation, causation, `H_O` support, G1, PMC, repeated correction, JT, or `C_improve`.
