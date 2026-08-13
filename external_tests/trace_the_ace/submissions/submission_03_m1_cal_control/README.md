# Trace the Ace Submission 03 — M1-cal transport control

Status: reusable preparation code only. No competition submission is made by
this directory.

This package transports the frozen historical M1-cal model family: exact
role-marked transcript serialization, the exact 262,144-feature word
unigram/bigram `HashingVectorizer`, the four historical ordinary covariates,
training-partition median imputation and scaling, the frozen averaged
`SGDClassifier`, and the frozen leakage-safe Platt construction.

It does not use objective ID/text, CCA-derived features, embeddings, GloVe,
model search, blending, attenuation, or alternate calibration.

## Fast-track parent status

The historical M1-prime OOF identity remains
`a067828455a9d992023213a9d9bd113e1ec041c73f1178b6706961760f219484`.
It was not recovered byte-for-byte. Competition engineering is explicitly
authorized to use the numerically reproduced OOF
`d5f2c1ce4f8433de29c4cdd54834801ca20b24cbc885f6a485e15d02cef5c34a`
under the label `M1_PRIME_RECONSTITUTED`. The builder records both identities
and refuses to relabel the reconstituted parent as historical.

The historical M1-cal runner and config remain untouched. Phase A is supplied
as an explicit completed reconstitution input; the builder independently
recomputes the authorized numerical gates before any deployment fit.

## Repository surface

Only these five reusable files belong in the repository:

- `README.md`
- `build_submission.py`
- `runtime_main.py`
- `verify_submission.py`
- `tests/test_submission_03_m1_cal_control.py`

All fitted state, OOF predictions, fixtures, manifests, and ZIP files must stay
in a caller-supplied local output directory.

## Build

Run only after the separately executed Phase A has passed. The transcript ZIPs
are identity inputs; the two extracted roots provide the training/runtime file
view.

```text
python build_submission.py \
  --repo-root <repository-root> \
  --index <canonical-index.csv> \
  --folds <canonical-folds.csv> \
  --m0-session-features <session-features.csv> \
  --m1-prime-oof <reconstituted-m1-prime-oof.csv> \
  --m1-prime-record <reconstituted-m1-prime-record.json> \
  --m1-cal-oof <reconstituted-m1-cal-oof.csv> \
  --m1-cal-record <reconstituted-m1-cal-record.json> \
  --train-features <train-features.csv> \
  --train-labels <train-labels.csv> \
  --transcripts-root <extracted-part-1> \
  --transcripts-root <extracted-part-2> \
  --transcripts-zip <train-transcripts-part-1.zip> \
  --transcripts-zip <train-transcripts-part-2.zip> \
  --output-dir <local-output-directory>
```

The build fails closed on historical-source identity, raw-input identity,
Phase-A numerical drift, incomplete/leaking deployment crossfit scores,
nonconvergence, invalid Platt geometry, fitted-state mismatch, or
nondeterministic ZIP bytes.

The final archive has exactly three members:

```text
main.py
assets/m1_cal_model.npz
assets/model_manifest.json
```

The NPZ contains inference state only: the text and four structural
coefficients, base intercept, structural medians, scaler mean/scale, and Platt
slope/intercept.

## Verify

The verifier authenticates provenance and package bytes, runs the extracted
runtime twice from fresh foreign working directories, and compares its final
probabilities with the label-free fixture predictions produced directly by the
fitted sklearn classifier and calibrator. The permitted maximum final
difference is `1e-10`.

```text
python verify_submission.py \
  --zip <local-output-directory>/trace_the_ace_submission_03_m1_cal_control.zip \
  --manifest <local-output-directory>/submission_03_manifest.json \
  --fixture-dir <local-output-directory>/fixture \
  --runtime-python <competition-compatible-python> \
  --runtime-pythonpath <allowlisted-scientific-dependency-directory>
```

`--runtime-pythonpath` may be repeated. It is only for an explicit local
competition-compatible dependency environment containing NumPy, pandas,
SciPy, and scikit-learn. Repository and build directories must not be supplied.
The runtime performs no network access and no downloads.

Successful verification changes only the local manifest to
`PREPARED_NOT_SUBMITTED` and reports
`READY_FOR_HUMAN_SUBMISSION_REVIEW`. It does not upload or submit the ZIP.

## Tests

```text
python -m unittest discover \
  -s external_tests/trace_the_ace/submissions/submission_03_m1_cal_control/tests \
  -p "test_*.py" -v
```

The tests use synthetic data only. They do not fit the real competition corpus.
