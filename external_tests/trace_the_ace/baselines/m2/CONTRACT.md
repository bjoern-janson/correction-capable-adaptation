# M2 — Objective-conditioned relevance contract

## Status

**AUTHORIZED PROSPECTIVE EXPERIMENT — RESULT UNOBSERVED AT FREEZE**

M2 is opened only because the frozen ordinary semantic baseline has passed prediction, convergence, calibration, objective-exclusion, and fixed-fold apparatus gates.

M2 is a task-structure experiment. It is not a CCA experiment and contains no CCA-derived feature family.

## Predictive objects

Frozen parent:

\[
M_1^{\mathrm{cal}}=P(Y\mid T,X_{\mathrm{ordinary}}).
\]

Objective-main-effect control:

\[
M_{2,O}=P(Y\mid Z_T,Z_O,X_{\mathrm{ordinary}}).
\]

Objective-conditioned model:

\[
M_2=P(Y\mid Z_T,Z_O,Z_T\odot Z_O,X_{\mathrm{ordinary}}).
\]

The primary hypothesis is `H_O`: objective-conditioned relevance adds predictive information beyond a model that already knows the objective as a main effect.

Thus the primary mechanism comparison is:

\[
\boxed{M_2\;\text{vs}\;M_{2,O}}.
\]

The total objective-information comparison \(M_2\) versus \(M_1^{\mathrm{cal}}\) is necessary but not sufficient for `H_O`, because it can be won by an objective main effect alone.

## Locked parent structure

M2 preserves exactly:

- the canonical session-grouped fold artifact and its SHA-256;
- transcript serialization and role markers;
- the frozen transcript representation `Z_T`;
- the four ordinary structural covariates;
- structural imputation/scaling policy;
- `SGDClassifier` family and all training hyperparameters;
- five-fold session-grouped inner cross-fitting;
- leakage-safe Platt scaling;
- primary response-level log loss;
- session-clustered paired bootstrap uncertainty.

No CCA-derived feature is permitted.

## Objective representation `Z_O`

The only new source field is the provided `learning_objective` text. `learning_objective_id` is used only to validate stable objective identity and the one-to-one ID/text mapping.

Objective text is normalized only by collapsing internal whitespace. It is transformed using the **same frozen HashingVectorizer configuration** as `Z_T`, but without transcript role markers.

No target encoding, objective prevalence statistic, label-conditioned objective representation, pretrained model, manually authored objective category, or objective-specific parameter is allowed.

## Main-effect control

`M2_O` appends `Z_O` to the frozen M1 feature blocks:

```text
[Z_T, Z_O, X_ordinary]
```

This control asks whether objective identity/content has predictive value even without changing how transcript features are interpreted.

A positive `M2_O` result does **not** establish objective-conditioned relevance.

## Conditioning mechanism

M2 adds one prospectively fixed interaction block:

\[
\boxed{Z_{T\times O}=Z_T\odot Z_O}
\]

where `*` is sparse elementwise multiplication in the common hashed unigram/bigram feature space.

The full block structure is:

```text
[Z_T, Z_O, Z_T * Z_O, X_ordinary]
```

This mechanism acts as lexical relevance gating: a transcript feature receives an explicit interaction coordinate only when the objective representation occupies the same hashed lexical coordinate.

Hash collisions are a known representation limitation. They are not repaired after observing the result.

## Validation and calibration

Outer validation remains the exact canonical five session-grouped folds.

For each outer fold and each arm (`M2_O`, `M2`):

1. fit the frozen base classifier on the outer training partition;
2. obtain raw outer-validation scores;
3. generate five-fold session-grouped inner OOF raw scores within the outer training partition using the identical feature construction;
4. fit the frozen Platt map only on those inner OOF scores and outer-training labels;
5. apply that map to the outer-validation raw scores.

No outer-validation label trains its own predictor or calibrator.

## Primary `H_O` adjudication

Let

\[
\Delta LL_{\mathrm{int}}=LL(M_2)-LL(M_{2,O}).
\]

`H_O` earns predictive support under this operationalization only if both hold prospectively:

\[
\Delta LL_{\mathrm{int}}<0
\]

and the paired 95% session-cluster bootstrap interval for the per-response log-loss difference has upper bound strictly below zero.

This is evidence for the **specified objective-conditioned interaction representation**, not a universal claim that all objective conditioning is useful.

## Total objective-information adjudication

Also report:

\[
\Delta LL_{\mathrm{total}}=LL(M_2)-LL(M_1^{\mathrm{cal}}).
\]

The point estimate must be negative and its paired session-cluster bootstrap CI must lie strictly below zero for total objective information to be declared incrementally predictive.

`M2_O` versus `M1^{cal}` is retained as a diagnostic main-effect comparison.

## Calibration preservation

Because M2 is intended to become the comparison surface for later feature-family tests, the full M2 calibrated probabilities must not degrade the frozen parent's:

- Brier score;
- ECE-10;
- absolute mean-probability bias.

A predictive `H_O` result can therefore coexist with an unresolved M2 baseline gate if probability quality degrades. Such a residual would open only a calibration successor, not CCA-derived features.

## Implementation validity

The result cannot validate its own feature construction. Before behavioral interpretation, execution must establish independently that:

- objective ID maps one-to-one to objective text;
- the objective block is nonzero;
- the interaction block is nonzero;
- objective feature rows differ in at least one session with multiple distinct objectives;
- every outer and inner base-model fit terminates before the frozen 500-iteration ceiling.

Failure of these conditions is an implementation/representation failure, not a scientific zero.

## Authority ceiling

Even a complete M2 pass may support only:

> Under this frozen operationalization and validation regime, objective-conditioned lexical relevance adds predictive information beyond the ordinary semantic baseline and beyond an objective-main-effect control.

M2 cannot establish or refute G1, PMC, repeated correction, JT, `C_improve`, causal tutoring effects, or any CCA-derived representation.

Only after M2's predictive, implementation, and baseline-calibration gates are diagnosed as passed may the first CCA-derived feature-family experiments be opened.
