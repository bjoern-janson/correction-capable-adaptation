# Trace-the-Ace deployment-realization audit

## Status

**PHASE-0 STOP — `BLOCKED_MISSING_INPUT`**

```text
D_deployment = UNIDENTIFIED_INPUT_BLOCKED
```

This packet executes the availability and identity gate required by [GitHub
issue #48](https://github.com/bjoern-janson/correction-capable-adaptation/issues/48).
It is based on the exact head of draft PR #47:
`4d02c557e234772ed28319fd4cf67098341318fd`.

The gate stopped before score extraction or comparison. No model was fit, no
split or score vector was regenerated, no public or hidden test information was
used, and no competition data are committed here.

## Observed fact

The following Phase-0 inputs are locally available and identity-valid:

- 35,072 training feature rows and 35,072 labels, with unique and identically
  ordered `response_id` values;
- 22,821 training sessions, with one matching transcript across the two frozen
  transcript archives;
- the frozen Submission 01 ZIP, whose archive and four internal artifact hashes
  match the frozen manifest;
- the historical M2-S research implementation and frozen configuration recorded
  in the PR #47 ancestry.

The primary paired audit nevertheless cannot be constituted. These required
objects are absent from the audited repository and local artifact scope:

1. the immutable historical M2-S OOF row artifact with SHA-256
   `64679b828af9737e5245dd1348f2c8e0cf5a38e013eefaee02266de7277e096f`;
2. the historical outer-fold assignment artifact with SHA-256
   `014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6`;
3. the row-level deployment-crossfit raw scores `z_deploy_CF`, including row
   identities and fold identities;
4. the exact deployment cross-fit/full-fit fitting implementation and its
   fold-specific fitted objects; and
5. the deployment cross-fit Platt geometry needed to distinguish the
   fold-specific research and deployment mappings.

The frozen ZIP contains final inference code and final fitted assets. It does
not contain the missing deployment training/cross-fit implementation or
row-level deployment-crossfit object. A recorded scalar cross-fit log loss does
not identify a score vector, its row order, its folds, or its calibration maps.
Likewise, the recorded hash of the historical OOF file cannot substitute for
the absent rows.

## Measurement-realization diagnosis

The contract's primary object is a paired, identical-row comparison:

```text
z_research_OOF <-> z_deploy_CF
```

Neither member of that pair is available as an immutable row-level artifact.
Their identical row identity and order therefore cannot be verified. The audit
cannot lawfully reach raw-score comparison, fixed-family Platt comparison,
packaged-inference equivalence, or the secondary full-fit diagnostic.

This is an input/provenance block, not evidence of deployment mismatch or
agreement. Reconstructing the missing vectors would require a new split,
emulation, or refitting from incomplete provenance. Issue #48 expressly forbids
all three.

The final full-fit `model.npz` and packaged `main.py` cannot stand in for
`z_deploy_CF`. The packaged model's single full-training Platt map also cannot
stand in for the absent fold-specific research and deployment maps.

## Authorized interpretation

The only authorized conclusion is:

```text
STOP = BLOCKED_MISSING_INPUT
D_deployment = UNIDENTIFIED_INPUT_BLOCKED
```

Phase 0 establishes that the available training corpus and frozen submission
package are internally identity-valid, while the exact primary comparison is
not constructible from the available objects. This is apparatus/input
diagnosis only. It is not negative scientific evidence.

The accompanying [`run_audit.py`](run_audit.py) is deliberately Phase-0-only.
It validates the allowlisted training inputs, Submission 01 archive, and
research-source identities, then reproduces the fail-closed result. The tests
cover this gate and its authority ceiling; they do not synthesize substitutes
for tests that the missing objects prevent.

## Not authorized

This packet does **not** authorize or establish:

- `DEPRIORITIZED` or `LOCATED_CANDIDATE`;
- any raw-score, probability, residual, calibration-map, fold-wise, or
  direct-versus-packaged comparison;
- a cause of any public or hidden-test performance;
- deployment implementation equivalence or mismatch;
- regeneration of historical OOF rows, folds, semantic caches, deployment
  cross-fit rows, or calibration geometry;
- use of the final full-fit score as a substitute for either cross-fit object;
- model search, feature changes, calibration-family selection, score repair,
  objective portability, or CCA-derived features;
- Submission 02 or any leaderboard submission;
- an update to CCA, G1, PMC, repeated correction, JT, or canonical authority;
- modification or merger of draft PR #47; or
- merger of this diagnostic PR.

Phases 1 through 4 and their score/equivalence tests are
`NOT_RUN_BLOCKED_MISSING_INPUT`. The modeling branch, calibration-transfer
branch, CCA-feature branch, and Submission 02 remain closed unless separately
authorized.

## Machine-readable records

- [`manifest.json`](manifest.json) records the exact Phase-0 inventory and
  immutable identities without raw data or machine-local paths.
- [`result.json`](result.json) records the terminal stop, unavailable scientific
  object, and untouched downstream phases.
- [`tests/test_run_audit.py`](tests/test_run_audit.py) checks the fail-closed
  behavior with standard-library fixtures only.

The historical research statements remain in [M2-S results](../../baselines/m2_sem/RESULTS.md)
and its [frozen configuration](../../baselines/m2_sem/config.yaml). This packet
does not revise either ancestor.
