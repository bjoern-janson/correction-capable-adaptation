# ECE efficiency diagnostic V3 result

## Status

**CLOSED — REPAIRED FIXTURE VALID, IF EFFICIENCY ROUTE FAILS PROSPECTIVE METHOD GATES — HISTORICAL OOF UNTOUCHED**

V3 changed only the V2 synthetic candidate family. The paired session-cluster influence-function/sandwich method, fixed-bin ECE-10 target, practical margin, regularity guard, historical OOF identities, and historical adjudication rules remained unchanged.

## Fixture constitution

The two-parameter family

\[
p_c=p_r+a+b\,s_{bin}
\]

successfully constituted all required population targets on the prospectively frozen grid.

```text
S1 true delta   0.0020021337   target error 0.0000034027   bin change 35.27%
SB true delta   0.0039952003   target error 0.0000022617   bin change 42.12%
S2 true delta   0.0079982417   target error 0.0000033177   bin change 81.21%
```

The nonzero scenarios produced nondegenerate intervals.

## Synthetic method-validation result

```text
scenario   coverage   NI pass   regularity pass   median CI width
S1         0.93       0.09      0.55              0.0129218441
SB         0.94       0.04      0.85              0.0129540828
S2         0.93       0.00      0.07              0.0170993717
```

The separate perfectly calibrated nonregular control triggered the regularity guard in 100% of fixtures.

Prospective gates:

```text
coverage S1/SB/S2       PASS
boundary NI behavior    PASS
supra-margin rejection  PASS
nondegenerate width     PASS
target constitution     PASS
nonregular control      PASS
sub-margin NI power     FAIL
regularity on declared regular scenarios FAIL
```

Therefore the candidate method is not validated for historical use and the sealed OOF vectors were not read.

## Diagnosis

V3 removes the V1 algebraic-degeneracy problem and the V2 constitution problem. The remaining failure is therefore localized to the **same-target influence-function efficiency route under the fixed-bin absolute ECE object**.

The method has reasonable interval coverage in the repaired fixtures, but:

1. the fixed-bin absolute-value ECE contrast frequently approaches/crosses nonregular points when candidate probabilities move across bins; and
2. even at a true degradation of only `0.5 * epsilon_ECE`, the IF interval establishes non-inferiority in only 9% of datasets.

This is evidence against this IF/sandwich route as the shallow precision repair. It does not establish that no same-target estimator can ever be more efficient.

It does, however, increase local diagnostic weight on **measurement-object adequacy**, because the non-smooth absolute/binning structure is directly implicated by the failed regularity gate.

## Current calibration diagnostic state

```text
D_efficiency    NOT ESTABLISHED by the tested IF route
D_additional    UNOPENED
D_object        locally more implicated; replacement NOT authorized
```

No metric switch, tolerance relaxation, new calibration model, or additional evidence collection is authorized by this result.

## Authority ceiling

No mature-calibration, mature-baseline, CCA, or CCA-feature authority is gained.

Local record SHA-256:

```text
6a208a449b7ec0853de6df6d83f92f2a061e6ad225b51c6722438b7ccfa54d88
```
