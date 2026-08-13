# Decision-gate validity successor

## Status

**PROSPECTIVE METHODOLOGICAL SUCCESSOR — RESULT UNOBSERVED**

This successor opens only the decision-gate validity boundary diagnosed by PR #44. It does not change the calibration construct, the 25% practical NI boundary, NI semantics, the oracle statistic, the bootstrap family, the information multiplier grid, the scale sentinels, or any historical model vector.

The predecessor raw result remains immutable:

```text
PR #44 raw full-gate verdict = NONE_IDENTIFIED_WITHIN_GRID
```

Authority from that raw verdict was withheld because the universal coverage gate treated an analytically degenerate exact-null interval as invalid when its empirical coverage reached 1.00.

## Governing question

> What should coverage validity mean when the target statistic is analytically degenerate under the declared paired contrast, and how should that differ from stochastic coverage validity?

The successor changes only **coverage-adjudication semantics**.

## Structural classification before outcomes

Each decision cell must be classified prospectively as either `STRUCTURALLY_DEGENERATE` or `STOCHASTIC`.

A cell is `STRUCTURALLY_DEGENERATE` only if the experiment definition proves, before any outcome is generated, that for every admissible outcome vector and every admissible bootstrap resample with a valid denominator, the paired decision statistic is constant at the true value:

```text
R_hat(w,Y) = R_true  for all admissible (w,Y).
```

Observed zero variance, narrow intervals, favorable empirical behavior, or a realized coverage of 1.00 cannot create this classification after the fact.

For the frozen oracle information-scaling construction, `R=0` satisfies the structural condition because `P_C=P_R`, hence `C_hat_C=C_hat_R` and `R_hat=0` exactly whenever the denominator is valid.

All other ratio cells remain `STOCHASTIC`.

## Degenerate coverage-validity gate

For a `STRUCTURALLY_DEGENERATE` cell, nominal repeated-sampling coverage is not the relevant validity test. The cell passes uncertainty validity only if all of the following hold:

```text
1. every valid dataset has interval lower == R_true within 1e-12;
2. every valid dataset has interval upper == R_true within 1e-12;
3. empirical coverage == 1.00;
4. the inherited denominator guard passes;
5. the inherited invalid-bootstrap-fraction guard passes;
6. the inherited NI operating-characteristic requirement for that ratio cell passes.
```

A point-mass interval at the wrong value fails. A nonzero-width interval is not treated as exact degeneracy. Structural degeneracy is therefore not an exemption from uncertainty validation; it has a stronger exactness requirement.

## Stochastic coverage-validity gate

For a `STOCHASTIC` cell, retain the predecessor lower protection against undercoverage:

```text
empirical coverage >= 0.90
```

The predecessor upper coverage cap `<=0.99` is removed from the validity gate.

Coverage above nominal is recorded as `CONSERVATIVE_COVERAGE` but does not by itself constitute invalidity. Decision usefulness is adjudicated independently by the already-frozen NI operating-characteristic gates:

```text
R=0,0.125 -> NI pass rate >= 0.80
R=0.25,0.50 -> NI pass rate <= 0.10
```

Thus a vacuous, excessively wide interval cannot acquire authority merely through high coverage: it must still support the required decision behavior.

The denominator and invalid-bootstrap guards remain unchanged.

## Monte Carlo reporting

Every stochastic coverage estimate must additionally report its Monte Carlo standard error

```text
MCSE_cov = sqrt(p_hat * (1-p_hat) / N_sim)
```

and `N_sim`.

This reporting requirement does not alter the inherited `>=0.90` lower gate inside this successor; it makes finite-simulation uncertainty visible and prevents a point estimate of coverage from being mistaken for an exact property.

## Full successor decision gate

For each ratio cell:

```text
G_cov(cell) =
  G_exact_degenerate(cell),  if STRUCTURALLY_DEGENERATE
  G_stochastic_coverage(cell), otherwise
```

The existing cell-level decision gate becomes:

```text
G_cell = G_cov & G_NI & G_denominator & G_invalid_bootstrap
```

The sentinel and joint gates remain conjunctive exactly as before.

No compensation across cells is allowed.

## Prospective methodological validation suite

No PR #44 information-response cell may be re-adjudicated until this successor itself passes a sealed gate-validity suite.

The suite is deterministic and result-independent. It tests adjudication logic, not calibration performance.

### V0 — correct exact degeneracy

```text
classification = STRUCTURALLY_DEGENERATE
R_true = 0
100/100 valid intervals = [0,0]
coverage = 1.00
NI pass rate = 1.00
expected = PASS
```

### V1 — wrong point-mass degeneracy

```text
classification = STRUCTURALLY_DEGENERATE
R_true = 0
100/100 valid intervals = [0.01,0.01]
expected = FAIL exactness/coverage
```

### V2 — nominal stochastic cell

```text
classification = STOCHASTIC
coverage = 0.95
NI/denominator/invalid-bootstrap gates = PASS
expected = PASS
```

### V3 — stochastic undercoverage

```text
classification = STOCHASTIC
coverage = 0.89
all other gates = PASS
expected = FAIL coverage
```

### V4 — conservative but vacuous stochastic cell

```text
classification = STOCHASTIC
coverage = 1.00
R_true = 0.125
NI pass rate = 0.00
expected = FAIL decision usefulness
```

### V5 — conservative and decision-capable stochastic cell

```text
classification = STOCHASTIC
coverage = 1.00
R_true = 0.125
NI pass rate = 0.90
all other gates = PASS
expected = PASS
```

The successor earns local methodological authority only if all six fixtures return their prospectively declared outcomes.

## Successor authority gate

```text
AUTH(Gamma_decision_gate') = V0 & V1 & V2 & V3 & V4 & V5
```

This authority is local to the declared decision-gate semantics. It does not authorize a calibration measurement, change the practical margin, change the decision object, or establish information sufficiency.

## Re-adjudication rule if the successor earns authority

Only after `AUTH(Gamma_decision_gate')=TRUE` may the already-generated PR #44 information-response record be **successor-adjudicated** under the new gate.

This does not rewrite PR #44. The original raw verdict remains historical. The successor produces a new adjudication record with separate provenance and authority.

No synthetic outcomes, bootstrap draws, thresholds, multipliers, sentinels, construct values, or NI results may be regenerated or changed for that re-adjudication.

## Hard prohibitions

This successor may not:

```text
change 0.25 practical materiality
change NI semantics
change C_R=0.010
change ratio cells
change bootstrap B=2000 or percentile-bootstrap family
change the information multiplier grid
change scale sentinels
select a replacement calibration operator
inspect historical M1-cal/M2-S vectors
open Z_E/Z_D/Z_C/Z_P
```

The diagnosed gate contradiction grants authority only to repair the gate dimension it identifies.

## Authority ceiling

Maximum possible authority:

```text
local decision-gate methodological validity
permission to successor-adjudicate the frozen PR #44 information-response record
```

Not possible from this successor:

```text
D_additional_evidence support by itself
replacement-measurement authority
AUTH(Gamma'_cal)
historical calibration closure
M_mature
CCA / G1 / PMC / JT / C_improve
Z_E / Z_D / Z_C / Z_P
```

## Reachability

```text
PR #44 gate-validity diagnosis
-> decision-gate methodological successor
-> synthetic gate-validity suite
-> AUTH(Gamma_decision_gate') if all fixtures pass
-> successor adjudication of frozen PR #44 evidence
```

Everything downstream remains blocked until that sequence is completed.
