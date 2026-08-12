# D_main exact materialized-cell apparatus successor

## Status

**APPARATUS VALIDATED LOCALLY — SCIENTIFIC OBJECT UNCHANGED — FULL RESULT STILL UNOBSERVED**

The frozen `M2_D_MAIN` experiment is unchanged. This successor changes only execution partitioning after profiling localized the runtime failure to the monolithic process/harness rather than the frozen SGD fit itself.

## Localization

For `B0 / outer fold 0`, stage profiling showed:

```text
training sparse hstack      ~2.43 s
validation sparse hstack    ~0.07 s
exact SGD fit                25.76 s
exact fitted n_iter          84
```

The exact fit therefore completes well inside the prior 900-second cell ceiling. The monolithic runner can nevertheless fail to terminate/seal reliably after or around the fit under the current container lifecycle.

A direct historical M2-S runner also exhibited the same current-container process-lifecycle problem despite having completed in earlier executions, further localizing the issue to apparatus/runtime state rather than the `D_main` representation.

## Successor mechanics

The apparatus successor partitions one frozen arm/fold cell into two fresh processes:

```text
1. materialize the exact frozen X_train, X_validation, y_train and validation row indices;
2. launch a fresh minimal process that loads only those sealed matrices, fits the exact frozen SGDClassifier, predicts, and writes the ordinary cell artifact.
```

The materializer uses the same hashes, cohort, fold indices, structural preprocessing, `Z_T`, optional `Z_O`, `Z_S`, optional centered `R_TO`, sparse `hstack`, row order, and float32 values as the frozen runner.

The fit process uses the same `make_classifier(config['base_classifier'])`; it does not change estimator family, hyperparameters, seed, averaging, stopping rule, or prediction transformation.

## Numerical equivalence validation

The successor was validated against an already produced exact frozen-runner `B0 / fold 0` cell.

```text
original exact cell:
  n_iter             84
  rows               6991
  NPZ SHA-256        880273c43169b17344fb77db884b92144512b66867042ba5c9fdce83ce37ebec

materialized successor:
  fit seconds        24.453715031
  n_iter             84
  rows               6991
  row indices        bitwise equal
  probabilities      bitwise equal
  max abs diff       0.0
  NPZ SHA-256        880273c43169b17344fb77db884b92144512b66867042ba5c9fdce83ce37ebec
```

This validates the execution partition as a numerically identity-preserving apparatus change for the tested cell.

## Authorized use

The two-process apparatus is authorized to execute the remaining frozen `B0,C0,B1,C1 × 5 outer folds` cells.

Each materialized cell must preserve the frozen config and required input hashes. Generated matrices and predictions remain local/uncommitted. The aggregate scientific result may be computed only after all required cells exist.

## Authority ceiling

This apparatus validation earns no scientific weight for or against `D_main`, broad `H_O`, calibration, CCA, or any CCA-derived feature family.

It only establishes that the previously blocked exact computation has an identity-preserving executable apparatus successor.
