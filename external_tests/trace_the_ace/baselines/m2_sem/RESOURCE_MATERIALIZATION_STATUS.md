# M2-SEM resource materialization status

## Status

**R_selected = PASS**  
**R_materialized = PASS**  
**R_hashed = PASS**  
**R_validated = PASS**  
**AUTH(execution) = TRUE**  
**H_O_SEM = UNOBSERVED**

No M2-SEM model score, fold loss, calibration diagnostic, or prediction was produced or inspected before this resource-constitution state was committed.

## Selected object

```text
resource family: Stanford GloVe
release: 2024 Wikipedia + Gigaword 5
case: uncased
vector dimension: 50
archive: glove.2024.wikigiga.50d.zip
publisher URL: https://nlp.stanford.edu/data/wordvecs/glove.2024.wikigiga.50d.zip
```

## Materialized archive

The prospectively selected archive was transferred into the analysis environment and inspected directly.

```text
archive byte size: 301036094
archive SHA-256:   afa5e258ee38272db6394547c4b075ecbb7b2164e98542c8d1237b6029b35a65
ZIP integrity:     PASS
member count:      1
```

Sole member:

```text
wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt
```

ZIP member metadata:

```text
uncompressed bytes: 842192707
compressed bytes:   301035796
CRC-32:             1fd70796
compression method: deflate
```

## Materialized vector file

The sole member was extracted to a standalone local vector file.

```text
vector byte size: 842192707
vector SHA-256:   16c4253cb9a19045dcdc758b6a1eda52d3c37b894dea2601a45046b4300a8d10
```

The SHA-256 computed over the decompressed ZIP-member stream and the SHA-256 computed after standalone extraction were identical.

## Full dimension validation

The complete vector file was scanned.

```text
rows / vocabulary entries: 1291147
blank rows:                0
minimum fields per row:    51
maximum fields per row:    51
wrong-dimension rows:      0
numeric parse failures:    0
non-finite values:         0
first token:               the
last token:                <unk>
validated dimension:       50
```

Every vocabulary row therefore contains exactly one token plus fifty finite numeric coordinates.

## Checksum provenance

Stanford did not publish a checksum for this archive on the official surfaces previously inspected. The hashes in this record constitute the byte identity of the transferred apparatus object used for this experiment; they are not represented as a separately publisher-signed checksum.

## Authority

Resource constitution now authorizes execution of the already-frozen M2-SEM experiment:

```text
AUTH(M2_SEM execution) = TRUE
```

It does not itself provide evidence for or against:

```text
H_O_SEM
semantic objective conditioning
semantic capacity
objective main effects
calibration
CCA
```

No model, calibration, or CCA-feature decision was changed by this materialization event.
