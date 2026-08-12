# Mature non-CCA calibration successor

## Status

**PROSPECTIVE CONTRACT FROZEN — RESULT UNOBSERVED**

This successor opens only the probability-map boundary of the already executed objective-independent semantic control:

\[
M_{2,S}=[Z_T,Z_O,X_{ordinary},Z_S].
\]

No transcript representation, objective representation, semantic resource, ordinary covariate, base-classifier fit, fold assignment, conditioning operator, or CCA-derived feature may change.

## Failure diagnosis being repaired

The inherited Platt map produced strong log loss and Brier performance, and its absolute mean-probability bias remained within the historical mature threshold. The unresolved gate is ECE-10 non-degradation relative to historical `M1-cal`.

This local pattern implicates the one-dimensional probability-map shape rather than the base representation or estimator. The minimal successor therefore replaces only the sigmoid Platt map with a monotone nonparametric isotonic map.

## Frozen calibration object

For each canonical outer fold:

1. use the already-frozen `M2_S` outer raw decision scores unchanged;
2. reconstruct the same five leakage-safe inner grouped OOF raw-score vector from frozen checkpoint artifacts;
3. fit `IsotonicRegression(y_min=1e-6, y_max=1-1e-6, increasing=True, out_of_bounds="clip")` on inner OOF score -> label;
4. transform the untouched outer raw scores;
5. concatenate all outer predictions exactly once.

No outer-validation label may enter calibrator fitting.

## Primary adjudication

The successor passes only if all gates hold:

```text
ECE-10 <= historical M1-cal ECE-10 = 0.015989848091338636
log loss < parent M2_S Platt log loss = 0.5359576099804155
paired session-cluster bootstrap 95% CI upper bound for
  LL(isotonic) - LL(parent Platt) < 0
Brier <= parent M2_S Platt Brier = 0.1790775429407408
absolute mean-probability bias <= historical M1-cal bias = 0.01053592989423624
```

No single metric can compensate for failure of another gate.

## Authority ceiling

A pass earns only the mature non-CCA probability treatment for `M2_S`. It does not adjudicate objective conditioning, repair historical conditioning failures, or authorize any CCA-derived feature family by itself.

A failure leaves calibration unresolved and triggers diagnosis of the calibration map; it does not reopen the base model automatically.
