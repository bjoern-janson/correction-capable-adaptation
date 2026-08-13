# Calibration resolution diagnostic result

**Status: EXECUTED — candidate-neutral oracle resolution topology observed**

Historical M1-cal/M2-S vectors were not read. No replacement operator was selected.

## Resolution object

```text
h_min_detect   4.8828125e-05
h_min_decision NONE_IDENTIFIED
```

All twelve frozen detection scales passed. No frozen scale passed the practical decision-identifiability gate.

Interpretation: the declared oracle can detect a C_cal,L1=0.010 sign-changing defect through the finest tested scale, but even with the sign pattern supplied it cannot support the inherited practical 25% relative-NI decision at any declared scale.

## Fixture constitution

All 12 scales and all required construct magnitudes passed bounds, injectivity (>1e-12), and construct-error (<=1e-12) checks. No clipping was used.

## Detection topology

| h | FPR | power | pass |
|---:|---:|---:|:---:|
| 0.1 | 0.04 | 1.00 | PASS |
| 0.05 | 0.06 | 1.00 | PASS |
| 0.025 | 0.06 | 0.98 | PASS |
| 0.0125 | 0.03 | 0.99 | PASS |
| 0.00625 | 0.05 | 1.00 | PASS |
| 0.003125 | 0.02 | 1.00 | PASS |
| 0.0015625 | 0.02 | 1.00 | PASS |
| 0.00078125 | 0.02 | 1.00 | PASS |
| 0.000390625 | 0.05 | 0.98 | PASS |
| 0.0001953125 | 0.08 | 1.00 | PASS |
| 9.765625e-05 | 0.04 | 0.99 | PASS |
| 4.8828125e-05 | 0.05 | 0.98 | PASS |

Detection pass vector:

```text
[True, True, True, True, True, True, True, True, True, True, True, True]
```

Because the finest declared scale also passes, this experiment does **not** locate a detection-resolution floor inside the frozen grid. The reported `h_min_detect` is the finest tested passing scale, not evidence that the true information floor equals that value.

## Decision topology

Every scale fails the conjunctive decision gate. The scale-invariant discriminator is the sub-margin `R=0.125` cell: NI pass rates range only from 0.52 to 0.67, below the frozen >=0.80 requirement at every scale.

| h | cov(R=.125) | NI(R=.125) | median CI width R | decision scale |
|---:|---:|---:|---:|:---:|
| 0.1 | 0.95 | 0.67 | 0.130861 | FAIL |
| 0.05 | 0.89 | 0.57 | 0.134011 | FAIL |
| 0.025 | 0.93 | 0.57 | 0.142320 | FAIL |
| 0.0125 | 0.96 | 0.64 | 0.130492 | FAIL |
| 0.00625 | 0.95 | 0.67 | 0.126763 | FAIL |
| 0.003125 | 0.97 | 0.54 | 0.139400 | FAIL |
| 0.0015625 | 0.93 | 0.54 | 0.139560 | FAIL |
| 0.00078125 | 0.96 | 0.57 | 0.150672 | FAIL |
| 0.000390625 | 0.94 | 0.52 | 0.148078 | FAIL |
| 0.0001953125 | 0.90 | 0.59 | 0.141473 | FAIL |
| 9.765625e-05 | 0.96 | 0.60 | 0.127603 | FAIL |
| 4.8828125e-05 | 0.97 | 0.67 | 0.134014 | FAIL |

Decision pass vector:

```text
[False, False, False, False, False, False, False, False, False, False, False, False]
```

The supra-margin direction is generally discriminated correctly (`R=0.25` NI pass 0.01–0.05; `R=0.50` NI pass 0.00 throughout), but the oracle does not establish non-inferiority reliably enough at true `R=0.125`. Thus the limiting boundary is practical decision precision, not defect detectability.

## Diagnosis

```text
D_resolution detection: identifiable through full frozen scale grid
D_resolution decision: NONE_IDENTIFIED
shallowest live boundary: practical relative-NI precision at C_R=0.010
```

This result separates the two questions that the prior F5 challenge confounded. Fine sign-changing calibration structure is detectable under the oracle; the same information regime does not support the frozen practical NI burden even at the coarsest scale.

## Authority

Gained:

- local oracle upper-bound evidence about detection and decision resolution;
- `R_res = (4.8828125e-05, NONE_IDENTIFIED)` within the declared grid;
- evidence constraining `R3_star`: detection scale is not the blocking boundary, while no decision-admissible scale is earned.

Not gained:

- replacement-measurement authority;
- `AUTH(Gamma_cal_replacement)`;
- historical calibration closure;
- `M_mature`;
- any `Z_E / Z_D / Z_C / Z_P` authority.

## Execution provenance

The exact execution mechanics were prospectively committed before result observation in commit `f6874e31bcd36581a7cf504892b7d2e948ae4c70`. Session IDs were lexicographically indexed; RNG streams used `SeedSequence([base_seed,*coordinates])`; the paired cluster bootstrap used a prospectively seeded common-random-number 2000x22821 cluster-count matrix.

The local first-run fixture helper redundantly computed the same deterministic minimum-gap value twice; a post-run apparatus-only rerun with the committed single-computation form produced an identical substantive result object (excluding elapsed time). No scientific quantity, RNG stream, threshold, or result changed.

Local artifact hashes:

```text
final.json  46b1ab44416cb30cdb000787981f2e762c0cc9cf2df500dd9d31c3a0b0bfe007
console.log  04f2f4cf6ed38bf6e35d7841a855eaaae37dea20bad392881361763005109b50
substantive_result_canonical_json  43f9b89ddfdb562ba7f7e9932fbade4fa15fedacae6ff10fdbf3cdee3a152772
```

Generated synthetic result arrays remain local; this record, hashes, and authority ledger are committed.
