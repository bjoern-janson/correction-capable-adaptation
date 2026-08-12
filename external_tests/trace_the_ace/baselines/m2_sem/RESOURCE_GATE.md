# M2-SEM external resource gate

## Current state

**SCIENTIFIC CONTRACT FROZEN — EXTERNAL RESOURCE IDENTITY NOT YET MATERIALIZED — EXECUTION NOT AUTHORIZED**

M2-SEM prospectively selects exactly one external semantic resource:

```text
Stanford GloVe 2024 Wikipedia + Gigaword 5, 50 dimensions
glove.2024.wikigiga.50d.zip
https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
```

No alternative embedding family, release, dimensionality, or source may be substituted under the same experiment identity.

## Acquisition rule

Before any M2-SEM model score, fold loss, calibration result, or outcome-bearing prediction may be inspected, record and commit:

```text
archive SHA-256
archive byte size
archive member listing
selected vector-member name
selected vector-file SHA-256
vector dimension validation = 50
```

Then update both `config.yaml` and `evidence_ledger/m2_sem.yaml` with those exact identities.

The acquisition step may verify the already-selected apparatus. It may not use Trace the Ace labels or model outcomes to choose among semantic resources.

## Failure semantics

Download failure, unavailable storage, or inability to materialize the selected archive is an execution/apparatus-access failure only.

It is not evidence for or against:

```text
H_O_SEM
semantic objective conditioning
objective main effects
CCA
```

A different semantic resource requires a separately identified successor proposal.
