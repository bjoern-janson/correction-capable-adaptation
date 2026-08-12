# M2-SEM external resource gate

## Current state

**SCIENTIFIC CONTRACT FROZEN — EXTERNAL RESOURCE IDENTITY CONSTITUTED — EXECUTION AUTHORIZED — RESULT UNOBSERVED**

```text
R_selected       = PASS
R_materialized   = PASS
R_hashed         = PASS
R_validated      = PASS
AUTH(execution)  = TRUE
H_O_SEM          = UNOBSERVED
```

M2-SEM prospectively selected exactly one external semantic resource:

```text
Stanford GloVe 2024 Wikipedia + Gigaword 5, 50 dimensions
glove.2024.wikigiga.50d.zip
https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
```

No alternative embedding family, release, dimensionality, or source was substituted.

## Constituted archive identity

```text
archive byte size: 301036094
archive SHA-256:   afa5e258ee38272db6394547c4b075ecbb7b2164e98542c8d1237b6029b35a65
member count:      1
ZIP integrity:     PASS
```

Archive member:

```text
wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt
```

## Constituted vector identity

```text
vector byte size: 842192707
vector SHA-256:   16c4253cb9a19045dcdc758b6a1eda52d3c37b894dea2601a45046b4300a8d10
vocabulary rows:  1291147
vector dimension: 50
malformed rows:   0
nonfinite rows:   0
```

The vector member was hashed both while streaming decompressed bytes from the ZIP and after extraction to a standalone local file; the hashes matched exactly.

## Acquisition rule closure

The prospectively required fields are now frozen before any M2-SEM result-bearing execution:

```text
archive SHA-256                         PASS
archive byte size                       PASS
archive member listing                  PASS
selected vector-member name             PASS
selected vector-file SHA-256            PASS
vector dimension validation = 50        PASS
```

This gate closure authorizes execution of the already-frozen M2-SEM experiment only. It does not support `H_O_SEM`, CCA, causation, G1, PMC, repeated correction, JT, `C_improve`, or any CCA-derived feature family.
