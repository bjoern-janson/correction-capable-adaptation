# ECE efficiency diagnostic V2 fixture-constitution result

## Status

**CLOSED — FIXTURE CANDIDATE FAMILY FAILED TO CONSTITUTE — NO OUTCOMES SAMPLED — HISTORICAL OOF UNTOUCHED**

V2 reopened only the synthetic validation fixture after V1's uniform-shift construction proved algebraically non-discriminating for uncertainty validation. The influence-function candidate method, ECE-10 target, practical margin, historical probability vectors, regularity guard, and historical decision rules remained frozen.

## Constitution failure

Before any synthetic outcomes could be sampled, the prospectively required population contrasts had to be reachable by the declared one-parameter candidate family:

```text
p_candidate = p_reference + lambda
lambda in [0, 0.03]
```

under the frozen deterministic alternating-bin-residual synthetic population.

The sub-margin target

```text
S1 = 0.5 * epsilon_ECE = 0.0019987310125
```

could not be reached within the prospectively required absolute target error `5e-5`.

The runner stopped with:

```text
target not reachable S1: err=0.001877266596441602
```

Therefore:

```text
synthetic fixture constituted    NO
sampled outcomes generated       NO
historical OOF read              NO
IF method adjudicated            NO
D_efficiency                     UNRESOLVED
```

## Failure localization

The shallowest implicated boundary is the **synthetic candidate family**. The one-dimensional uniform-shift family does not span the required positive sub-margin/boundary/supra-margin ECE contrasts under the declared population geometry.

This is not evidence against the influence-function estimator and not evidence about the historical M1-cal versus M2-S comparison.

## Authorized successor

A V3 successor may change only the label-free synthetic candidate family / deterministic population search used to constitute the validation fixture. It must demonstrate, before outcome sampling, that the family can prospectively realize all required population target contrasts within the same target-error tolerance and with nontrivial bin-membership changes.

It may not change:

```text
fixed-bin ECE-10 target
epsilon_ECE = 0.003997462025
paired session-cluster IF/sandwich candidate method
historical OOF identities
regularity guard
historical adjudication rules
```

## Authority ceiling

No mature-calibration, mature-baseline, CCA, or CCA-feature authority is gained. V2 identifies only a fixture-constitution failure.
