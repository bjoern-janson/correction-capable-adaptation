# M2-SEM resource materialization status

## Status

**R_selected = PASS**  
**R_materialized = BLOCKED_BY_LOCAL_RUNTIME**  
**R_hashed = NOT REACHED**  
**R_validated = NOT REACHED**  
**AUTH(execution) = FALSE**

No M2-SEM model score, fold loss, calibration diagnostic, or prediction was produced or inspected during this resource-constitution attempt.

## Publisher verification

The selected resource was independently verified on Stanford's official GloVe surfaces as:

```text
resource family: Stanford GloVe
release: 2024 Wikipedia + Gigaword 5
corpus size: 11.9B tokens
vocabulary: 1.2M
case: uncased
vector dimension: 50
archive: glove.2024.wikigiga.50d.zip
publisher URL: https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
```

Stanford's project page and official GloVe repository both identify that exact archive as the selected 50-dimensional 2024 Wikipedia+Gigaword resource.

## Materialization attempts

Two attempts were made to acquire the exact publisher bytes in the current execution environment:

1. the runtime download helper failed to retrieve the Stanford ZIP;
2. direct `curl` from the local container failed because the container has no DNS/network path to `nlp.stanford.edu`.

The browser/web retrieval layer can resolve the publisher URL and metadata but does not expose the `application/zip` bytes to the local filesystem for hashing.

No local file matching `glove*` or `*wikigiga*` was already present in `/mnt/data`.

## Checksum search

A web search for an authoritative published SHA-256/checksum for `glove.2024.wikigiga.50d.zip` found no Stanford-published checksum. A third-party configuration names the corresponding 50d vector basename, but third-party metadata is not accepted as apparatus identity evidence and was not used to populate any hash field.

Therefore the following remain deliberately unset:

```text
archive_sha256 = null
archive_byte_size = null
archive_member_listing = null
selected_vector_member_name = null
selected_vector_sha256 = null
vector_dimension_validation_from_materialized_bytes = null
```

## Epistemic status

This is an apparatus-access failure only.

It provides zero evidence for or against:

```text
H_O_SEM
semantic objective conditioning
semantic capacity
objective main effects
calibration
CCA
```

The frozen resource selection must not be replaced by a convenient mirror, older GloVe release, different dimension, or other embedding family under the same experiment identity.

The next legitimate event is acquisition of the exact selected Stanford-hosted archive bytes in an environment that can materialize them, followed by archive hashing, member enumeration, extracted-vector hashing, and 50-dimensional format validation before `AUTH(execution)` can become true.
