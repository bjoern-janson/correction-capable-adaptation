# ECE efficiency diagnostic V3 — two-parameter fixture constitution

## Status

**PROSPECTIVE VALIDATION-APPARATUS SUCCESSOR — RESULT UNOBSERVED**

V3 changes only the synthetic candidate family used to validate the already frozen paired session-cluster influence-function/sandwich uncertainty estimator.

Unchanged:

```text
fixed equal-width ECE-10 target
paired session-cluster IF/sandwich candidate method
regularity guard
epsilon_ECE = 0.003997462025
historical M1-cal and M2-S OOF identities
historical adjudication rules
```

## Repaired candidate family

The frozen V2 synthetic population is preserved:

- deterministic reference probabilities spanning 0.15 to 0.85 by session rank;
- known reference residual magnitude 0.03 with alternating sign by fixed reference ECE bin;
- known synthetic outcome probability `q = p_reference - residual`.

V3 replaces the insufficient one-parameter shift with:

\[
p_c=p_r+a+b\,s_{bin},
\]

where `s_bin` is +1 for even reference bins and -1 for odd reference bins.

The deterministic label-free search grid is frozen as:

```text
a in [-0.05, 0.05], 81 equally spaced values
b in [-0.08, 0.08], 121 equally spaced values
```

Candidates outside `(0.001, 0.999)` are inadmissible. For each required population target (`0`, `0.5 epsilon`, `epsilon`, `2 epsilon`), choose the lexicographically first `(a,b)` among candidates minimizing absolute population-target error. Required target error is <= `5e-5` and every nonzero target must change fixed-bin membership for at least 1% of sessions.

This geometry was checked before freeze using only the known synthetic population and label-free canonical session-size distribution; no sampled outcomes or historical prediction vectors were used.

## Validity and historical order

Only after all fixture identities are constituted are the prospectively fixed synthetic outcomes sampled. The same V2 coverage, non-inferiority, regularity, nonregular-control, and minimum-width gates apply.

Historical OOF vectors remain forbidden unless all synthetic gates pass.

## Authority ceiling

V3 can only validate or reject the same IF efficiency candidate within this declared scope. It cannot change the ECE target, tolerance, calibration treatment, evidence source, or authorize CCA-derived features.
