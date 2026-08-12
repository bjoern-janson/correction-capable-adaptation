# M1 — Results and diagnosis

## Historical identity

This result belongs to the prospectively frozen M1 contract and configuration on the stacked branch `agent/trace-the-ace-m1-ordinary-semantic`.

No objective information and no CCA-derived feature family entered M1.

## Primary result

Canonical five-fold session-grouped OOF:

```text
M0 pooled log loss     0.6045154928
M1 pooled log loss     0.5790941375
Delta LL (M1 - M0)   -0.0254213554
M1 pooled AUC          0.6763607524
```

The paired session-cluster bootstrap for the OOF log-loss difference was:

```text
point estimate        -0.0254213554
95% percentile CI     [-0.0291437679, -0.0216852872]
replicates             2000
clusters               22,821 sessions
```

All five folds improved over M0:

| Fold | M0 LL | M1 LL | Delta LL | M1 AUC | SGD iterations |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.6050549518 | 0.5802745402 | -0.0247804117 | 0.6726306130 | 50 |
| 1 | 0.6036818295 | 0.5743590038 | -0.0293228257 | 0.6801361800 | 50 |
| 2 | 0.6029511924 | 0.5825950483 | -0.0203561441 | 0.6798810307 | 36 |
| 3 | 0.6068992251 | 0.5795159310 | -0.0273832941 | 0.6760385383 | 50 |
| 4 | 0.6039905030 | 0.5787275144 | -0.0252629886 | 0.6743773905 | 50 |

## Objective-exclusion validation

M1 is session-only by construction. Among the 8,364 sessions with multiple response rows, the maximum within-session range of M1 probabilities was exactly:

```text
0.0
```

This confirms that response/objective multiplicity did not create objective-conditioned predictions in M1.

## Calibration diagnostics

```text
Brier score                 0.1951913729
ECE-10                      0.0580493570
mean predicted probability  0.7578927043
observed rate               0.7024692062
```

Discrimination and Brier score improved substantially relative to M0, but the frozen M1 probabilities are systematically high and ECE is materially worse than M0.

## Diagnosis

### Predictive-information gate

**PASS.**

The result supports the narrow claim:

> Under the frozen M1 operationalization and validation regime, generic transcript semantics contain predictive information not captured by M0.

The evidence is not confined to one fold: every fold has lower log loss, and the paired session-cluster bootstrap interval for `Delta LL = LL(M1) - LL(M0)` is wholly below zero.

### Strongest-ordinary-baseline gate

**UNRESOLVED.**

Four of five outer-fold `SGDClassifier` fits terminated at the prospectively frozen `max_iter = 50` rather than the tolerance stopping condition. This is an estimator/training residual. The raw M1 model is also undercalibrated under the frozen no-calibrator policy.

Neither residual invalidates the historical M1 result: the exact frozen estimator executed and yielded the result above. But they prevent this M1 identity from being treated as the final strongest ordinary semantic baseline for the M1->M2 transition.

The shallowest next boundary is therefore an **M1 estimator/calibration successor**, not M2.

## Authority gained

M1 gains only:

```text
generic transcript semantics add predictive information beyond M0
under this operationalization and fixed grouped-validation regime
```

## Authority not gained

M1 does not establish:

```text
CCA support or refutation
causal tutoring effects
objective-conditioned relevance / H_O
G1
PMC
repeated correction
JT
C_improve
```

M2 is not opened by this result because the requirement that M1 serve as the strongest ordinary semantic comparison remains unresolved at the estimator/calibration layer.
