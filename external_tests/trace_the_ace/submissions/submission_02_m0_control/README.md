# Trace the Ace Submission 02 M0 engineering control

**SUBMISSION STATUS: PREPARATION TOOLING ONLY / NOT SUBMITTED**

This directory contains the minimum reusable tooling for the frozen Submission 02
M0 engineering control. It reproduces the historical M0 object, fits that exact
object on all eligible training responses, builds an offline package, and verifies
the extracted package against direct numerical inference. It does not upload a
submission or select, tune, calibrate, repair, or compare predictive candidates.

The implementation is descended from source-admissibility head
`4d02c557e234772ed28319fd4cf67098341318fd`. The historical M0 implementation,
configuration, and canonical fold generator are read-only inputs and are checked
before fitting. Generated competition-derived assets, fixtures, predictions,
verification records, and ZIP files remain outside the repository.

## Frozen predictive object

The model uses exactly these student-only response features, in this order:

1. `n_student_words`
2. `numeric_turns_per_word`
3. `digit_chars_per_word`

Eligibility is `n_student_words >= 100`. Medians are learned from eligible training
responses only, followed by `StandardScaler` and
`LogisticRegression(max_iter=1000)` with otherwise historical/default settings.
Quiet test sessions receive the all-eligible full-training response base rate.
`n_turns`, Submission 01 predictive assets, hidden/public-test information, and a
calibration layer are not part of this object.

## Files

- `build_submission.py` enforces source/input identity, validates Phase 0, fits the
  frozen M0, proves sklearn/direct-numeric agreement, and builds deterministic
  local artifacts.
- `runtime_main.py` is copied to package root as `main.py`; it provides offline,
  direct NumPy inference through the preserved Submission 01 external I/O shell.
- `verify_submission.py` validates the archive, runs the extracted package from a
  foreign working directory, compares directory/ZIP transcript realizations,
  checks direct/package equivalence, and verifies deterministic reruns.
- `tests/test_submission_02_m0_control.py` tests the fixed feature, inference,
  packaging, ordering, and fail-closed contracts without competition data.

## Execution order

Run the historical M0 reproduction first. Its fold artifact must have SHA-256
`014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6`,
and all published and grouped-OOF gates must pass before invoking the builder.

The builder requires explicit local paths and performs no discovery:

```text
python build_submission.py \
  --repo-root <repository> \
  --features <train_features.csv> \
  --labels <train_labels.csv> \
  --transcripts-zip <part1.zip> \
  --transcripts-zip <part2.zip> \
  --submission-01 <frozen-submission-01.zip> \
  --index <canonical-index.csv> \
  --folds <canonical-folds.csv> \
  --session-features <phase0-session-features.csv> \
  --phase0-record <phase0-m0-record.json> \
  --output-dir <local-output-directory>
```

Then verify the generated ZIP through its normal extracted runtime path:

```text
python verify_submission.py \
  --zip <local-output-directory>/trace_the_ace_submission_02_m0_control.zip \
  --fixture-dir <local-output-directory>/fixture/data \
  --direct-predictions <local-output-directory>/fixture/direct_predictions.csv \
  --transcripts-zip <part1.zip> \
  --transcripts-zip <part2.zip> \
  --manifest <local-output-directory>/submission_02_m0_manifest.json \
  --output-record <local-output-directory>/verification.json
```

Targeted tests use only the standard unittest runner:

```text
python -m unittest discover \
  -s external_tests/trace_the_ace/submissions/submission_02_m0_control/tests \
  -p 'test_submission_02_m0_control.py' -v
```

## Stop conditions and authority ceiling

Every gate fails closed at its shallowest locus: input/source identity, historical
reproduction, full fit, packaged equivalence, runtime contract, or output schema.
No failure authorizes a replacement feature, model, solver, threshold, calibrator,
split, seed, or probability patch.

`READY_FOR_HUMAN_SUBMISSION_REVIEW` means only that a local engineering control was
prepared and verified. It is not competition submission authority, a CCA result,
an explanation of Submission 01's public gap, transport evidence, or authorization
for Submission 03. Human review remains outside this tooling, and this directory
contains no upload path.
