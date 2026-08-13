# M1 — Ordinary transcript-semantic baseline contract

## Status

**AUTHORIZED PROSPECTIVE EXPERIMENT — RESULT UNOBSERVED AT FREEZE**

M1 is the first substantive Trace the Ace prediction experiment after the M0 measurement-infrastructure gate.

It is not a CCA experiment and contains no CCA-derived feature family.

## Predictive object

M1 tests:

\[
\boxed{M_1=P(Y\mid T,X_{\mathrm{ordinary}})}
\]

against the already closed M0 apparatus:

\[
\boxed{M_0=P(Y\mid X_{\mathrm{simple}})}.
\]

The primary question is:

> Does a prospectively fixed generic transcript-semantic representation add held-out predictive information beyond M0 under the identical session-grouped validation apparatus?

## Authority ceiling

A successful M1 may support only:

> Under this operationalization and fixed validation regime, generic transcript semantics add predictive information beyond M0.

M1 does not test or support G1, PMC, repeated correction, JT, `C_improve`, causal tutoring effects, objective-conditioned relevance, or any CCA-derived representation.

## Objective-information exclusion

M1 must not consume the M2 structural hypothesis.

Explicitly forbidden from M1 inputs and feature construction:

```text
learning_objective
learning_objective_id
objective embeddings
objective-conditioned attention
transcript-objective similarity
objective-specific pooling
objective-specific feature selection
objective target encoding
```

`response_id` and `session_id` are permitted only for joins, grouping, and output identity. They are not predictive features.

## CCA-derived feature exclusion

M1 contains exactly zero features whose reason for existence depends uniquely on:

```text
evidence exposure / evidence-role labeling
learner-state diagnosis
correction-response linkage
post-intervention learner evidence
misconception localization
warrant / authority transfer
post-modification correctability
repeated correction
justified transformability
C_improve
```

If a proposed feature requires one of those interpretations to justify its construction, it belongs in a successor experiment after M2.

## Ordinary-feature allowlist

The complete predictive allowlist is frozen as:

### Transcript text `T`

All utterance `content` fields, in original utterance order, serialized with fixed role markers only:

```text
__ROLE_TUTOR__ <content>
__ROLE_STUDENT__ <content>
__ROLE_BACKGROUND__ <content>
```

No timestamp value, objective, response identifier, session identifier, filename, fold label, target, or evaluator-only field enters text.

Whitespace is normalized to one space within an utterance. No utterance is dropped based on semantic content.

### Ordinary structural covariates `X_ordinary`

Only the following already-defined transcript statistics are allowed:

```text
n_turns
n_student_words
numeric_turns_per_word
digit_chars_per_word
```

The last three are inherited from the M0 feature artifact; `n_turns` was already produced by the same M0 preprocessing pass but was not used by the M0 classifier.

No additional metadata or derived statistic may be added after result inspection under the same M1 identity.

## Semantic representation

M1 uses a conventional sparse lexical-semantic representation with no pretrained external model:

```text
HashingVectorizer
analyzer          = word
ngram_range       = (1, 2)
n_features        = 262144
alternate_sign    = false
binary            = false
norm              = l2
lowercase         = true
token_pattern     = (?u)\\b\\w+\\b
dtype             = float32
```

The hashing transform is stateless. It is applied once to each session transcript and therefore does not fit on validation text or test text.

Pretrained resources: **NONE**.

This choice is intentionally ordinary: it establishes a strong conventional lexical-semantic null without importing task-specific or CCA-specific pretrained semantics.

## Response weighting

The competition metric is response-level. If one session maps to multiple response/objective rows, the same M1 transcript representation is repeated for those response rows during fitting and scoring.

Thus M1 may produce identical predictions for multiple response rows from one session because objective information is excluded by construction. Response duplication is retained rather than session-averaged because the competition loss is defined over response rows.

## Model

Frozen classifier:

```text
SGDClassifier
loss              = log_loss
penalty           = l2
alpha             = 1e-5
max_iter          = 50
tol               = 1e-4
shuffle           = true
random_state      = 17
average           = true
fit_intercept     = true
class_weight      = null
early_stopping    = false
```

The four structural covariates are median-imputed from the outer-fold training partition, standardized from the outer-fold training partition, converted to float32, and horizontally appended to the hashed transcript representation.

No hyperparameter search occurs in M1. A later tuning proposal is a successor experiment.

## Calibration

No post-hoc calibrator is fitted in M1.

Primary probabilities are the classifier's native `predict_proba` outputs. Calibration is diagnostic only and is reported using Brier score and 10-bin equal-width ECE.

A future calibration step is a separately identified model stage; it does not retroactively change M1.

## Validation

M1 inherits the canonical M0 fold artifact **byte-for-byte**.

Required fold SHA-256:

```text
014df0fb893250dc15f106605109ca3b7e86460f98bece560582826cc8b20cb6
```

Grouping key: `session_id`.

Primary comparison: pooled OOF log loss on exactly the same response rows as M0.

Secondary diagnostics:

```text
fold log loss
pooled AUC
Brier score
10-bin equal-width ECE
mean predicted probability
fold dispersion
```

## Primary result and stopping rule

Define:

\[
\Delta LL_{10}=LL(M_1)-LL(M_0).
\]

M1 has incremental predictive gain iff:

\[
\boxed{\Delta LL_{10}<0}.
\]

The magnitude and fold stability are reported; no minimum effect threshold is invented after execution.

If M1 is weak or worse than M0, the result is diagnosed at the shallowest sufficient locus among preprocessing, representation, estimation/training, or predictive-hypothesis failure before M2 is opened.

## Experiment identity

\[
\mathcal I(M_1)=
(D_{\mathrm{index}},F_{\mathrm{fixed}},C_{\mathrm{text}},C_{\mathrm{ordinary}},C_{\mathrm{model}},E_{\mathrm{runtime}}).
\]

Changing any load-bearing element creates an explicit successor rather than rewriting this M1.

## Uncertainty

The M1-versus-M0 OOF log-loss difference uses a paired session-cluster bootstrap:

```text
cluster                 = session_id
replicates              = 2000
random_seed             = 1701
interval                = percentile 95%
within-session handling = preserve all response rows together
```

Each bootstrap replicate samples sessions with replacement and computes the response-weighted mean difference in per-response log loss between M1 and M0 over the sampled session blocks. This interval is diagnostic uncertainty for the fixed OOF comparison; it is not a causal confidence interval.
