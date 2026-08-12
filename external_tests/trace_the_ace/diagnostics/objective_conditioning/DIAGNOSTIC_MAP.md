# Objective-conditioning diagnostic map

## Status

**DIAGNOSTIC MAP FROZEN — NO NEW CONDITIONING OPERATOR AUTHORIZED — NO CCA-DERIVED FEATURE FAMILY AUTHORIZED**

This artifact follows the closed historical M2 and M2-SEM experiments. It does not create `M2-III`, reopen calibration, or adjudicate the broad objective-conditioning proposition globally.

The preserved distinction is:

```text
tested operator != representation family != broader hypothesis
```

Current local authority:

```text
objective main effect                         SUPPORTED
generic transcript semantic capacity          SUPPORTED
H_O^lexical: Z_T * Z_O                       FAILED
H_O^SEM: R_TO = Z_C(O) - Z_S                 FAILED
broad H_O                                    OPEN / NOT GLOBALLY IDENTIFIED
historical calibration branch                 UNRESOLVED
Z_E, Z_D, Z_C, Z_P                           UNAUTHORIZED
```

The two conditioning failures are evidence about their frozen operationalizations. They are not licensed evidence that the broader interaction family is false.

## Diagnostic object

Let

\[
\mathcal D_O=\{D_{main},D_{temporal},D_{granularity},D_{identifiability},D_{redundancy}\}.
\]

These are competing explanations for why two materially different objective-conditioning operators failed to establish incremental predictive value beyond matched controls.

A diagnostic candidate may acquire weight only from evidence capable of distinguishing it from at least one competing candidate. Repeated null results under operators that share the same representational assumptions do not automatically discriminate among candidates.

## D_main — objective signal is mostly exhausted as a main effect

### Claim

Once the model knows the learning objective and has a strong objective-independent transcript representation, little additional predictive information remains in objective-dependent reinterpretation of the transcript.

### Discriminating observation

A prospective decomposition that varies the availability of objective main-effect information while holding transcript semantic capacity fixed should show that conditioning value grows materially when the objective main effect is removed or weakened, but collapses when the objective main effect is restored.

The key discriminator is not simply another interaction null. It is a **change in incremental conditioning value as objective-main-effect capacity is manipulated under a fixed validation apparatus**.

### Evidence against

A conditioning mechanism that adds stable held-out information beyond a fully expressive objective main effect and matched generic semantic control weighs against `D_main`.

### Authority ceiling

Support would justify only that the current target's objective-related predictive information is largely captured as an additive/main-effect contribution under the tested apparatus. It would not establish causal sufficiency of the objective or global absence of interactions.

## D_temporal — conditioning exists but is temporally localized

### Claim

Objective relevance may act at specific phases or events in the tutoring trajectory, while whole-session pooling dilutes the effect.

Candidate loci include, prospectively and without CCA authority:

```text
early elicitation
misconception expression
instruction/intervention
student reconstruction
terminal response preparation
```

These labels are descriptive temporal/task phases only unless independently operationalized; they must not import `Z_E`, `Z_D`, `Z_C`, or `Z_P` by name or construction.

### Discriminating observation

Under a prospectively frozen temporal partition independent of outcomes, objective-conditioned evidence should be concentrated in one or more windows and should beat a matched objective-independent representation of those same windows.

A valid temporal diagnostic requires:

```text
same mature parent information
same outer folds
same estimator/calibration policy unless the calibration branch has separately changed
matched generic-semantic control at the same temporal resolution
predeclared temporal segmentation independent of labels
```

### Evidence against

Tight nulls across independently motivated temporal partitions, with adequate information and matched controls, weigh against `D_temporal`.

### Authority ceiling

A positive diagnostic would support temporal localization of objective-conditioned predictive information only. It would not authorize CCA-derived feature families unless their separate prerequisites are satisfied.

## D_granularity — interaction exists below the current semantic unit

### Claim

Whole-utterance mean embeddings and pooled session summaries may be too coarse. Objective relevance may operate at phrase, token-span, equation step, discourse-act, or local turn-pair resolution.

### Discriminating observation

A prospectively defined finer-grained representation should recover objective-conditioned incremental information while a matched objective-independent representation at the **same fine granularity** controls for the added representational capacity.

The comparator must therefore have the form:

\[
M_{fine,S} \quad\text{vs}\quad M_{fine,SC},
\]

not coarse baseline versus fine conditioned model.

### Evidence against

Independent fine-grained operators with matched-capacity controls and tight null intervals weigh against `D_granularity`.

### Authority ceiling

A positive result would identify a useful interaction scale under that representation. It would not establish that the objective causally changes learning.

## D_identifiability — the available transcript interface cannot identify the interaction

### Claim

The relevant objective-conditioned distinction may not be recoverable from the recorded transcript/objective interface, even if such a distinction exists in the generating process.

Formally, the live possibility is analogous to:

\[
O_{obs}(s_a)=O_{obs}(s_b)\quad\text{while the interaction-relevant latent distinction differs}.
\]

If so, optimization over the current observation interface cannot recover the missing distinction.

### Discriminating observation

Evidence must come from an **independent challenge channel** not reducible to the same transcript representation assumptions. Examples of admissible diagnostic directions include prospectively collected annotations, external process measures, or other independent observations that distinguish cases the transcript representation treats as equivalent.

The diagnostic question is whether independently observed distinctions predict where objective relevance should differ despite near-equivalence under the current transcript interface.

### Evidence against

If richer independent observations add no interaction-relevant distinction and sufficiently expressive transcript-only representations repeatedly recover all available predictive structure, weight shifts away from `D_identifiability`.

### Authority ceiling

Support would identify an interface limitation, not prove any particular hidden mechanism.

## D_redundancy — objective-conditioned reinterpretation is genuinely redundant for this target

### Claim

Conditional on mature generic transcript semantics and objective information, objective-dependent reinterpretation contributes negligible additional predictive information for the target.

### Required evidence standard

`D_redundancy` cannot be established by accumulating ordinary nonsignificant tests.

Before a redundancy experiment is executed, prospectively define:

```text
an equivalence / practical-null region for incremental log loss
a validation design with adequate precision relative to that region
at least one conditioning operator whose representation is independently motivated
matched-capacity controls
```

Evidence for redundancy requires the uncertainty interval to lie inside the predeclared practical-null region, not merely to cross zero.

### Evidence against

Any independently validated conditioning operator with incremental value outside the practical-null region weighs against `D_redundancy`.

### Authority ceiling

Even strong redundancy evidence would be scoped to this target, dataset, measurement interface, mature baseline, and admissible operator class. It would not establish a universal absence of objective-conditioned interpretation.

## Cross-candidate discrimination matrix

| Candidate | What would raise its weight? | What would lower its weight? | What does **not** discriminate it? |
|---|---|---|---|
| `D_main` | conditioning emerges when objective main-effect capacity is prospectively reduced, then disappears when restored | conditioning survives a strong objective main effect | another null with unchanged main-effect structure |
| `D_temporal` | matched conditioned gain localized to prospectively defined temporal windows | precise nulls across independent temporal partitions | whole-session pooling null alone |
| `D_granularity` | fine-unit conditioned model beats matched fine-unit semantic control | precise matched nulls at finer units | adding a finer encoder without a capacity-matched control |
| `D_identifiability` | independent observations split transcript-equivalent cases in interaction-relevant ways | independent channels fail to expose missing distinctions | more optimization over the same observation interface |
| `D_redundancy` | CI contained inside a prospectively defined practical-null region across an admissible operator class | stable incremental conditioning outside the null region | p>0.05 / CI crossing zero |

## Selection rule for the next conditioning experiment

No third conditioning operator is authorized merely because two prior operators failed.

A new conditioning experiment may open only after a diagnostic argument identifies the **shallowest implicated boundary** and states:

```text
1. which D candidate(s) the experiment discriminates;
2. which competing candidate(s) it can distinguish;
3. what observation changes future weights;
4. what remains locked from the mature baseline;
5. what result would stop further escalation;
6. the authority ceiling of either outcome.
```

If the proposed experiment cannot discriminate among live explanations, it does not earn execution authority.

## Calibration independence

The conditioning diagnostic branch remains independent of the historical calibration branch:

\[
D_{conditioning}\perp D_{calibration}.
\]

The raw M2-SEM conditioning null was already present before Platt calibration, so calibration is not currently a sufficient explanation for the two conditioning failures. Nevertheless, the mature predictive baseline for any eventual CCA-derived feature test must use the calibration treatment that is independently earned by the calibration branch.

## Mature-baseline rule for eventual CCA tests

No CCA-derived family is opened by this diagnostic map.

If separate prerequisites are eventually satisfied, every first-pass component test must compare against the mature non-CCA baseline available at that time:

\[
M_{mature}=\text{generic transcript semantics}+\text{objective/task information}+\text{independently resolved calibration treatment}.
\]

Then, and only then, a component may be tested as

\[
M_{mature}+Z_k \quad\text{vs}\quad M_{mature},
\qquad k\in\{E,D,C,P\}.
\]

No large combined model may grant authority retrospectively to individual CCA-derived components.

## Current stopping rule

The current state is healthy and intentionally unresolved:

```text
objective main effect                  SUPPORTED
generic semantic capacity              SUPPORTED
H_O^lexical                            FAILED
H_O^SEM                                FAILED
broad H_O                              OPEN
conditioning generating explanation    UNRESOLVED
calibration                            UNRESOLVED
CCA-derived families                   UNAUTHORIZED
```

The next move is diagnosis. Escalation stops until discriminating evidence identifies a justified successor boundary.
