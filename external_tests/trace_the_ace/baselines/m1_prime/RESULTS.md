# M1′ — Results and diagnosis

## Historical identity

This result belongs to the prospectively frozen M1′ estimator-repair successor. It does not modify historical M1.

The only scientific/engineering change from M1 was:

```text
SGDClassifier max_iter: 50 -> 500
```

Everything else remained frozen, including transcript representation, ordinary covariates, objective exclusion, fold artifact, and validation protocol.

## Primary result

Canonical five-fold session-grouped OOF:

```text
M1 pooled log loss       0.5790941375
M1′ pooled log loss      0.5765421662
Delta LL (M1′ - M1)    -0.0025519713
M1′ pooled AUC           0.6765416347
```

Paired session-cluster bootstrap:

```text
95% CI for Delta LL     [-0.0028688175, -0.0022150375]
clusters                 22,821 sessions
replicates                2,000
```

The convergence repair improves pooled log loss, and the paired interval remains strictly below zero.

Fold results:

| Fold | M1 LL | M1′ LL | Delta LL | M1′ AUC | M1′ iterations |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.5802745401 | 0.5731383797 | -0.0071361605 | 0.6740221318 | 81 |
| 1 | 0.5743590038 | 0.5743590038 | ~0 | 0.6801361800 | 50 |
| 2 | 0.5825950482 | 0.5825950483 | ~0 | 0.6798810307 | 36 |
| 3 | 0.5795159309 | 0.5758683366 | -0.0036475943 | 0.6766301660 | 62 |
| 4 | 0.5787275144 | 0.5767506850 | -0.0019768293 | 0.6746870870 | 56 |

All five fits terminate before the new `max_iter = 500` ceiling.

## Objective-exclusion validation

The maximum within-session M1′ prediction range remains exactly:

```text
0.0
```

Objective exclusion therefore remains exact.

## Calibration

Historical M1 versus M1′:

```text
                         M1                M1′
Brier score              0.1951913729      0.1944457863
ECE-10                   0.0580493570      0.0518984518
mean probability         0.7578927043      0.7517811924
observed rate            0.7024692062      0.7024692062
absolute mean bias       0.0554234981      0.0493119861
```

Prospectively required 25% reduction thresholds were:

```text
ECE-10 <= 0.0435370177
absolute mean bias <= 0.0415676235
```

Observed reductions were only:

```text
ECE-10 reduction         10.60%
absolute bias reduction  11.03%
```

Brier score and log loss both improve, but the frozen calibration-materiality gate does not pass.

## Diagnosis

```text
convergence gate          PASS
log-loss preservation     PASS
Brier preservation        PASS
objective exclusion       PASS
calibration gate          FAIL
baseline gate             UNRESOLVED
AUTH(M2)                  FALSE
```

The demonstrated convergence-boundary defect is resolved. The remaining shallowest residual is calibration only.

Therefore the next legitimate successor is a **calibration-only M1 successor** that preserves the now-converged M1′ representation and estimator.

M2 remains unopened.

## Authority gained

M1′ adds local evidence that:

> Allowing the frozen ordinary-semantic SGD estimator to converge improves held-out log loss relative to historical M1 and resolves the iteration-ceiling defect.

## Authority not gained

M1′ does not establish:

```text
CCA support or refutation
causal tutoring effects
H_O / objective-conditioned relevance
G1
PMC
repeated correction
JT
C_improve
```
