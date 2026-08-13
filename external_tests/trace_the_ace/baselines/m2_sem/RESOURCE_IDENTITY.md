# M2-SEM external semantic resource identity

## Authority state

```text
R_selected       = PASS
R_materialized   = PASS
R_hashed         = PASS
R_validated      = PASS
AUTH(execution)  = TRUE
H_O_SEM          = UNOBSERVED
```

This record constitutes only the external semantic apparatus object selected prospectively by M2-SEM. No M2-SEM model score, fold loss, calibration diagnostic, prediction, or hypothesis-bearing result was produced or inspected before this identity was frozen.

## Acquisition provenance

The exact prospectively selected archive was transferred into the analysis environment as:

```text
glove.2024.wikigiga.50d.zip
```

The selected source remains:

```text
https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
```

Stanford does not publish a checksum for this archive on the official surfaces previously inspected, so the SHA-256 values below constitute the byte identity of the materialized apparatus used by this experiment. They are not claimed to be a separately publisher-signed checksum.

## Archive identity

```text
archive name:               glove.2024.wikigiga.50d.zip
archive byte size:          301036094
archive SHA-256:            afa5e258ee38272db6394547c4b075ecbb7b2164e98542c8d1237b6029b35a65
ZIP integrity test:         PASS
archive member count:       1
```

Archive member listing:

```text
wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt
```

ZIP metadata for the sole member:

```text
uncompressed bytes:         842192707
compressed bytes:           301035796
CRC-32:                     1fd70796
compression method:         deflate
```

## Vector-file identity

The sole archive member is therefore the prospectively required vector member without any post-result selection:

```text
selected vector member:
wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt

vector byte size:           842192707
vector SHA-256:              16c4253cb9a19045dcdc758b6a1eda52d3c37b894dea2601a45046b4300a8d10
```

The member was hashed once while streaming decompressed bytes directly from the ZIP and again after materializing those bytes as a standalone local vector file. The SHA-256 values were identical.

## Full format validation

The complete materialized vector file was scanned, not sampled.

```text
rows / vocabulary entries:  1291147
blank rows:                 0
minimum fields per row:     51
maximum fields per row:     51
expected fields per row:    1 token + 50 vector coordinates
rows with wrong dimension:  0
numeric parse failures:     0
non-finite vector values:   0
first token:                the
last token:                 <unk>
vector dimension:           50
vector-dimension gate:      PASS
```

Thus every parsed vocabulary row has exactly fifty finite numeric coordinates.

## Gate closure

The prospectively specified resource chain is now closed:

```text
R_selected
  -> R_materialized
  -> R_hashed
  -> R_validated
  -> AUTH(M2_SEM execution)
```

`AUTH(M2_SEM execution) = TRUE` authorizes execution of the already-frozen semantic-conditioning experiment only. It provides no evidence for `H_O_SEM`, CCA, causation, G1, PMC, repeated correction, JT, `C_improve`, or any CCA-derived feature family.