# M2 objective-main-effect suppression diagnostic

## Status

**PROSPECTIVE DIAGNOSTIC CONTRACT FROZEN — RESULT UNOBSERVED**

This experiment does not create M2-III. It probes only the live explanation `D_main` from the frozen objective-conditioning diagnostic map:

> objective-conditioned transcript information may be largely exhausted once explicit objective main-effect capacity is available.

## Why this is the shallowest diagnostic

The experiment introduces no new conditioning representation. It reuses the already-failed semantic residual:

\[
R_{TO}=Z_C(O)-Z_S.
\]

To prevent `R_TO` from acting merely as a surrogate objective main effect when `Z_O` is removed, the diagnostic uses outer-training-fold objective centering:

\[
\widetilde R_{TO}=R_{TO}-E_{train}[R_{TO}\mid O].
\]

The mean is computed from the outer training partition only and applied to both training and validation rows. No validation outcome is used. Objectives without outer-training support are excluded by a prospectively frozen, label-free support rule: objective present in at least two canonical outer folds. This retains 319 objectives, 34,978 responses, and 22,783 sessions.

## Frozen arms

No explicit objective main effect:

\[
B_0=[Z_T,X_{ordinary},Z_S],
\qquad
C_0=B_0+\widetilde R_{TO}.
\]

Explicit objective main effect restored:

\[
B_1=[Z_T,Z_O,X_{ordinary},Z_S],
\qquad
C_1=B_1+\widetilde R_{TO}.
\]

Every other estimator, representation, fold, structural-preprocessing, and semantic-resource choice remains inherited.

## Primary discriminator

Define

\[
\Delta_0=LL(C_0)-LL(B_0),
\qquad
\Delta_1=LL(C_1)-LL(B_1),
\]

and

\[
\Psi=\Delta_0-\Delta_1.
\]

`D_main` predicts that centered conditioning should become useful when the explicit objective main effect is absent and should be attenuated when it is restored.

Primary measurement uses raw outer decision scores mapped by the fixed sigmoid before any calibration. This keeps the diagnostic independent of the unresolved calibration branch.

`D_main` receives positive diagnostic weight only if:

```text
Delta_0 < 0 and its paired session-cluster bootstrap 95% CI upper bound < 0
Psi     < 0 and its paired session-cluster bootstrap 95% CI upper bound < 0
```

It is weighed against only under the strong opposite exclusion:

```text
Delta_0 CI lower >= 0
and
Psi CI lower >= 0
```

All other outcomes remain unresolved. Ordinary nulls do not establish redundancy.

## Authority ceiling

A positive result supports only the local explanation that explicit objective main-effect capacity suppresses incremental value of this already-specified semantic-conditioning residual under this task and apparatus.

A negative or unresolved result does not globally refute `D_main`, `H_O`, or objective-conditioned interpretation. It only changes weight for this diagnostic probe.

No result from this experiment authorizes a third conditioning operator or any CCA-derived feature family.
