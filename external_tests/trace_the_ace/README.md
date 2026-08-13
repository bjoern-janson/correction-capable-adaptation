# Trace the Ace external test

This directory is an external predictive test environment inside the Correction-Capable Adaptation (CCA) research repository.

It is **not** an empirical implementation of G1, Post-Modification Correctability (PMC), repeated correction, Justified Transformability (JT), or `C_improve`.

The governing authority chain is:

```text
CCA distinction
→ explicit modeling hypothesis
→ Trace the Ace representation
→ predictive evidence
→ local diagnosis
→ hypothesis update, if warranted
→ CCA update, only if independently warranted
```

Predictive evidence is not causal evidence.

## First engineering gate

The first checkpoint is deliberately restricted to measurement/comparison infrastructure:

```text
registry
→ data integrity
→ fixed grouped folds
→ M0
→ M0 diagnosis
```

M0 earns no authority about CCA. It can only establish that the Trace the Ace data/validation/baseline apparatus is sufficiently reproducible to open M1.

## Experiment identity

For M0, identity is conjunctive:

```text
I(M0) = (
  dataset index,
  fixed grouped folds,
  preprocessing configuration,
  model configuration,
  runtime environment
)
```

Changing a load-bearing component creates a successor experiment; it does not silently inherit the original M0 authority.

## Initial hypotheses

The prospective registry is in `hypotheses/registry.yaml`:

- `H_O` — objective-conditioned relevance (structural M2 hypothesis)
- `H_E` — evidence exposure
- `H_D` — learner-state diagnosis
- `H_C` — correction response
- `H_P` — post-intervention learner evidence

The CCA-derived families are hypothesis-generating operationalizations only. Their names do not establish construct validity.

## Data policy

Competition data, transcript contents, response/session identifiers, generated indices, folds, OOF predictions, and fitted model artifacts stay local and are ignored by Git.

Scripts write generated outputs beneath `artifacts/` by default. Do not commit that directory.

## Reproduce the first gate

Example using extracted transcript directories:

```bash
python data/build_index.py \
  --features /path/to/train_features.csv \
  --labels /path/to/train_labels.csv \
  --transcripts-root /path/to/train_transcripts_part1 \
  --transcripts-root /path/to/train_transcripts_part2 \
  --output artifacts/index.csv \
  --record artifacts/index_record.json

python validation/make_folds.py \
  --index artifacts/index.csv \
  --output artifacts/folds.csv \
  --record artifacts/folds_record.json \
  --n-splits 5 \
  --seed 3

python baselines/m0/train.py \
  --index artifacts/index.csv \
  --folds artifacts/folds.csv \
  --transcripts-root /path/to/train_transcripts_part1 \
  --transcripts-root /path/to/train_transcripts_part2 \
  --config baselines/m0/config.yaml \
  --output-dir artifacts/m0
```

`build_index.py` performs deep transcript integrity checks. `make_folds.py` creates one deterministic session-level fold assignment. `train.py` performs both the published M0 reference-holdout reproduction and the canonical multi-fold OOF evaluation.

## Reference M0

The published Trace the Ace reference uses three student-talk features:

```text
n_student_words
numeric_turns_per_word
digit_chars_per_word
```

with `MIN_STUDENT_WORDS = 100`, a standardized logistic regression, and a session-grouped 80/20 `GroupShuffleSplit(random_state=3)`.

The published rounded reference values are encoded prospectively in `baselines/m0/config.yaml`. Reproduction status is a deterministic check against those published rounded values; it is not determined by leaderboard feedback.
