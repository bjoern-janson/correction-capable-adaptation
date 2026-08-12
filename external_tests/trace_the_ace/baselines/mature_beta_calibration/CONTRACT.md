# Mature non-CCA beta-calibration successor

## Status

**PROSPECTIVE CONTRACT FROZEN — RESULT UNOBSERVED**

This is the minimal successor to the diagnosed isotonic calibration experiment. The isotonic map repaired the ECE-10 defect but did not earn robust log-loss authority over Platt. The implicated boundary is therefore calibration shape-flexibility versus estimation variance, not the base predictive representation.

The predictive object remains exactly:

\[
M_{2,S}=[Z_T,Z_O,X_{ordinary},Z_S].
\]

No base-model fit, feature block, semantic resource, fold, conditioning operator, or CCA-derived distinction may change.

## Minimal shape successor

Let the frozen raw outer/inner decision score be `s` and define

\[
p_0=\sigma(s).
\]

The successor calibrator is the monotone three-parameter beta map

\[
\hat p=\sigma\left(a\log p_0-b\log(1-p_0)+c\right),
\qquad a\ge 0,\; b\ge 0.
\]

Platt scaling is the restricted subfamily `a=b`; beta calibration therefore adds one asymmetric shape degree of freedom while remaining far lower-variance than unconstrained isotonic regression.

For each canonical outer fold, `(a,b,c)` is fit only on the same frozen five-fold inner grouped OOF raw scores used by the preceding calibration experiments. Outer validation labels never enter calibration fitting.

Frozen optimizer:

```text
scipy.optimize.minimize
method = L-BFGS-B
initial = (1, 1, 0)
bounds = [(0, None), (0, None), (None, None)]
maxiter = 1000
ftol = 1e-12
gtol = 1e-8
analytic gradient = yes
```

Raw sigmoid probabilities are clipped to `[1e-12, 1-1e-12]` only before logarithms.

## Primary gate

Beta calibration earns the mature probability treatment only if all gates pass:

```text
ECE-10 <= historical M1-cal ECE-10 = 0.015989848091338636
log loss < parent M2-S Platt log loss = 0.5359576099804155
paired session-cluster bootstrap 95% CI upper bound for
  LL(beta) - LL(parent Platt) < 0
Brier <= parent M2-S Platt Brier = 0.1790775429407408
absolute mean-probability bias <= historical M1-cal bias = 0.01053592989423624
all five optimizer fits converge successfully
```

The prior isotonic result is diagnostic lineage only; it is not a comparator gate and cannot grant authority to beta calibration.

## Authority ceiling

A pass earns only the independently validated probability treatment for the mature non-CCA baseline. It does not resolve conditioning, support broad `H_O`, or itself authorize any CCA-derived feature family.

A failure leaves calibration unresolved and triggers diagnosis at the calibration-map boundary. No gate may be relaxed after observing the result.
