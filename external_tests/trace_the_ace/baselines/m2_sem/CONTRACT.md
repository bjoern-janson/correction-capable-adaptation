# M2-SEM — Semantic objective-conditioning successor

## Status

**AUTHORIZED PROSPECTIVE SUCCESSOR — RESULT UNOBSERVED**

M2-SEM is a successor to the closed historical M2 experiment. It opens only the objective-conditioning representation boundary implicated by M2's failed sparse lexical interaction.

Historical M2 established:

```text
objective information main effect     PASS
Z_T * Z_O lexical interaction         FAIL
calibration preservation              FAIL
CCA-derived feature authority         FALSE
```

M2-SEM does not rewrite or repair historical M2.

## Predictive question

The successor asks:

> Does an objective-conditioned semantic relevance representation add held-out predictive information beyond an objective-independent semantic representation built with the same frozen semantic encoder?

The scientific comparison is therefore mechanism-specific.

## Locked parent apparatus

The following remain unchanged from the mature M2 lineage:

```text
fixed session-grouped outer folds
M2_O objective-main-effect block [Z_T, Z_O, X_ordinary]
transcript serialization used for Z_T
hashed transcript representation Z_T
hashed objective main-effect representation Z_O
ordinary structural covariates X_ordinary
SGD classifier family and hyperparameters
five-fold session-grouped inner cross-fitting
Platt calibration procedure
response-level log loss
paired session-cluster bootstrap
CCA-derived feature exclusion
```

No `Z_E`, `Z_D`, `Z_C`, or `Z_P` feature is opened.

## Frozen external semantic resource

The semantic encoder is a frozen external word-vector resource:

```text
resource family: Stanford GloVe
resource: glove.2024.wikigiga.50d.zip
source: https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
vector dimension: 50
case: uncased
training corpus: 2024 Wikipedia + Gigaword release
```

The resource itself is not trained or adapted on Trace the Ace data.

**Execution is prohibited until the exact downloaded archive SHA-256, extracted vector-member name, and extracted vector-file SHA-256 are committed prospectively.** Materializing and hashing that already-selected resource may finalize apparatus identity; changing the resource family, release, dimension, or source creates a different successor.

## Semantic tokenization

For this semantic block only:

```text
input: utterance content or learning-objective text
lowercase: true
token regex: (?u)\b\w+\b
role markers: excluded
OOV tokens: ignored
```

For text `x`, let `W(x)` be the in-vocabulary tokens. Define the text embedding

\[
e(x)=\frac{1}{|W(x)|}\sum_{w\in W(x)}v(w)
\]

when `W(x)` is nonempty, followed by L2 normalization. Empty/OOV-only embeddings are represented as zero and handled by the validity rules below.

## Objective-independent semantic control

For transcript utterances `u_1,...,u_n`, let `q_t` be the L2-normalized GloVe mean embedding for utterance `t` whenever nonzero.

The objective-independent semantic transcript summary is

\[
Z_S=\frac{1}{|A|}\sum_{t\in A}q_t,
\]

where `A` is the set of utterances with nonzero semantic embeddings.

This block contains no objective information.

The matched semantic-capacity control is

\[
\boxed{M_{2,S}=[Z_T,Z_O,X_{ordinary},Z_S]}.
\]

Its purpose is to absorb any predictive gain caused merely by adding the frozen semantic encoder.

## Objective-conditioned semantic residual

Let `q_O` be the normalized GloVe mean embedding of the learning objective. For each nonzero utterance embedding:

\[
c_t=q_t^\top q_O.
\]

Freeze the attention temperature at

\[
\boxed{\beta=5.0}.
\]

No temperature search is permitted under this experiment identity.

Define objective-conditioned attention:

\[
a_t(O)=\frac{\exp(\beta c_t)}{\sum_{j\in A}\exp(\beta c_j)}.
\]

The objective-conditioned semantic pool is

\[
Z_C(O)=\sum_{t\in A}a_t(O)q_t.
\]

The new conditioning-only block is the residual

\[
\boxed{R_{TO}=Z_C(O)-Z_S}.
\]

The successor model is

\[
\boxed{M_{2,SC}=[Z_T,Z_O,X_{ordinary},Z_S,R_{TO}]}.
\]

Because both arms contain the same `Z_S`, incremental credit in the primary comparison can be assigned to objective-conditioned semantic reweighting rather than to the semantic encoder itself.

## Primary hypothesis

Define the successor operationalization:

\[
H_O^{SEM}: LL(M_{2,SC})<LL(M_{2,S}).
\]

The primary gate passes iff both are true on the frozen outer OOF rows:

```text
point estimate: LL(M2_SC) - LL(M2_S) < 0
paired session-cluster bootstrap 95% CI upper bound < 0
```

No minimum effect-size threshold is invented after execution.

## Secondary comparisons

The following are diagnostic and do not substitute for the primary gate:

```text
M2_S  vs historical M2_O   # generic semantic-capacity increment
M2_SC vs historical M2_O   # total semantic-successor increment
```

A large `M2_S` gain does not support `H_O^SEM` unless `M2_SC` also beats `M2_S` under the primary rule.

## Implementation-validity gates

Before interpreting predictive results, execution must establish:

```text
exact frozen GloVe archive SHA recorded prospectively
exact extracted vector-file SHA recorded prospectively
all 398 objective texts have nonzero semantic embeddings
all sessions contain at least one nonzero utterance embedding
Z_S is exactly identical across response rows within a session
R_TO is nonzero on at least one response
R_TO differs across objectives in at least one multi-objective session
no objective information enters Z_S
outer session isolation is exact
inner calibration session isolation is exact
all outer and inner base-model fits converge below max_iter=500
```

Failure of an implementation-validity gate blocks hypothesis interpretation.

## Calibration separation

M2-SEM preserves the same leakage-safe Platt calibration procedure so the predictive comparison remains apples-to-apples.

However, historical M2's calibration-preservation failure is a **separate unresolved branch**. M2-SEM reports Brier score, ECE-10, and absolute mean-probability bias, but those diagnostics do not retroactively repair historical M2 and are not substituted for the conditioning gate.

Even if `H_O^SEM` passes:

\[
\operatorname{AUTH}(Z_E,Z_D,Z_C,Z_P)=\mathrm{FALSE}
\]

until the separately identified M2 calibration successor also closes cleanly.

## Uncertainty

Primary and diagnostic log-loss differences use the inherited paired session-cluster bootstrap:

```text
cluster: session_id
replicates: 2000
interval: percentile 95%
preserve all response rows from a sampled session together
```

The random seeds are frozen in `config.yaml` before execution.

## Authority ceiling

A successful M2-SEM may support only:

> Under this frozen semantic operationalization, objective-conditioned semantic reweighting adds held-out predictive information beyond an objective-independent semantic representation using the same encoder.

It does not establish causation, G1, PMC, repeated correction, JT, `C_improve`, or CCA generally.

A failed result reaches only this operationalization unless independent evidence warrants a deeper revision.
