# G1 Warrant-Origin Attack

## Status

**SCIENTIFIC DESIGN / ADVERSARIAL REVIEW — NO EMPIRICAL STATE TRANSITION — NO IMPLEMENTATION AUTHORIZED**

This artifact attacks one canonical primitive in the current G1 role:

> **warranted evidence acquiring causal control over a separable adaptive decision**

The canonical G1 decision already places an `independent warrant` step upstream of causal assignment. It does not freeze a warrant mapping, candidate ontology, uncertainty rule, weighting rule, threshold, model, benchmark, or experiment contract.

This attack therefore asks a narrower question than “how should G1 be measured?” and a more upstream question than “how should authority be transported across a later seam?”

> **What exactly makes a piece of evidence warranted for a claim or adaptive decision in the first place?**

No warrant function, score, probability threshold, oracle, graph, metric, candidate set, policy, or implementation is proposed here.

---

## Canonical target

The current G1 role is:

\[
\boxed{
G_1
=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

with the current operational instantiation:

\[
E\longrightarrow C_{\mathrm{selected}}.
\]

The canonical role can be read as containing at least two logically distinct burdens:

```text
WARRANT ORIGIN
Why is some evidence-authority relation scientifically licensed at all?

CAUSAL ACQUISITION
Does assignment of that evidence causally move the separable adaptive decision
in the direction licensed by that warrant relation?
```

This attack concerns the first burden.

It does **not** reopen the already-established causal-composition rule and does not import any noncanonical authority-transport formalism from later adversarial PRs.

---

# Attack 1 — warrant is not an intrinsic property of evidence

The phrase “warranted evidence” can be misread as if warrant were a property carried by an evidence object independently of a scientific question.

That interpretation fails.

The same observation can be highly reliable and still be irrelevant to one claim, decisive for another, and action-indeterminate for a third.

For example, suppose a diagnostic measurement reliably establishes that a model is miscalibrated on subgroup `A`.

That evidence may warrant:

- the claim that subgroup calibration is defective;
- further measurement of a suspected mechanism;
- a restricted deployment policy;
- no immediate parameter modification at all.

It does not by itself determine which modification should be applied.

Therefore:

\[
\boxed{
\text{evidence validity}
\not\Rightarrow
\text{decision warrant}.
}
\]

and:

\[
\boxed{
\text{admissible evidence}
\not\Rightarrow
\text{warranted action}.
}
\]

The scientific claim, decision scope, protected constraints, and relevant causal structure can change what the same evidence licenses.

So any future warrant semantics that treats `warrant(E)` as context-free is under-specified.

This does not yet imply a particular relational representation.

---

# Attack 2 — truth, correctness, and warrant are different objects

A correct decision can be unwarranted.

Suppose a selector ignores evidence and chooses candidate `c_1` uniformly at random from two candidates. In one realized case, `c_1` happens to be the uniquely beneficial candidate.

The outcome is correct, but the evidence did not warrant that choice.

Conversely, a decision can be warranted under the best available evidence and still turn out badly because the evidence was noisy, the environment changed, or a low-probability outcome occurred.

Therefore:

\[
\boxed{
\text{correct decision}
\not\Rightarrow
\text{warranted decision}
}
\]

and:

\[
\boxed{
\text{warranted decision}
\not\Rightarrow
\text{guaranteed success}.
}
\]

This blocks a retrospective definition of warrant in which whatever action succeeded is declared to have been warranted.

Outcome success may challenge, calibrate, or revise a warrant relation prospectively. It cannot by itself manufacture the historical warrant under which the action was supposedly justified.

---

# Attack 3 — a positive G1 effect cannot validate its own warrant relation

Consider an experiment that prospectively defines an arbitrary mapping from evidence states to “warranted” candidates:

```text
E = e1 -> c1
E = e2 -> c2
```

The tested selector perfectly follows this mapping.

Then the causal response of selection to evidence may be very strong.

But if the mapping itself has no independent scientific basis, the experiment has established only:

> evidence assignment controls selection according to the declared mapping.

It has not established:

> the mapping was warranted.

Thus:

\[
\boxed{
G_1>0
\not\Rightarrow
\text{warrant relation valid}.
}
\]

The converse also fails.

A scientifically justified warrant relation can exist while a tested system ignores the evidence completely:

\[
\boxed{
\text{warrant relation valid}
\not\Rightarrow
G_1>0.
}
\]

This is an important asymmetry.

The warrant relation or orientation is part of the upstream scientific constitution required to interpret G1. The G1 assay tests causal acquisition of control relative to that constitution; it cannot use its own positive result as evidence that the constitutive warrant was correct.

This is the warrant-origin analogue of the broader CCA rule that a downstream successful result cannot retroactively validate an unvalidated relation it crossed.

---

# Attack 4 — unique-oracle semantics are too strong

A tempting simplification is:

```text
for each admissible evidence state E
there is exactly one warranted candidate C*(E)
```

This fails in ordinary decision problems.

Two or more modifications may be equally supported under the current scientific objective. They may differ only along dimensions declared irrelevant to the claim, or both may satisfy the same target/protection constraints.

A valid evidence state can therefore support multiple scientifically acceptable decisions.

Examples include:

- two parameter changes with indistinguishable expected target/protection profiles inside the declared tolerance;
- two interventions that are scientifically equivalent under the current claim but differ operationally;
- a family of conservative actions all justified by the same uncertainty set;
- multiple candidate repairs whose differences are not identified by the available evidence.

Therefore:

\[
\boxed{
\text{warranted}
\not\Rightarrow
\text{unique action}.
}
\]

A set-valued warrant correspondence is one possible future representation, but this attack does **not** freeze that representation.

The negative result is enough: G1 cannot assume a unique oracle unless uniqueness is itself prospectively justified for the scoped scientific object.

---

# Attack 5 — abstention can be the warranted decision

Suppose available evidence establishes that the current system is likely defective but does not identify a safe correction.

Forcing a modification merely because “correction” is expected would be epistemically backwards.

A warranted response can be:

- abstain;
- preserve the current state;
- request additional evidence;
- run a diagnostic intervention;
- defer until a protection condition is measurable.

Therefore:

\[
\boxed{
\text{valid evidence of a problem}
\not\Rightarrow
\text{warrant for immediate modification}.
}
\]

and:

\[
\boxed{
\text{abstention}
\text{ can be a warranted adaptive decision}.
}
\]

A G1 contract that counts only movement toward a non-null modification can misclassify correct evidence-sensitive abstention as failure.

No abstention semantics are frozen here.

---

# Attack 6 — information gathering can be warranted without warranting a final modification

Evidence may warrant an information-acquisition action rather than a terminal correction.

Suppose two causal explanations remain live:

```text
H1 -> modification m1 is safe
H2 -> modification m1 damages protected behavior
```

Current evidence does not distinguish them.

The warranted next decision may be to run a discriminating test.

So:

\[
\boxed{
\text{evidence can warrant a diagnostic action}
\not\Rightarrow
\text{evidence warrants a final modification}.
}
\]

This matters because G1 is role-level language about a separable adaptive decision, not necessarily a terminal change.

The warrant object must therefore be scoped to **which decision is actually being licensed**, not merely whether the system eventually changes.

---

# Attack 7 — joint evidence can warrant what no component warrants alone

Let `D_a` and `D_b` be two measurements.

Suppose neither measurement alone distinguishes two live hypotheses:

\[
D_a\not\Rightarrow Q,
\qquad
D_b\not\Rightarrow Q,
\]

but their joint pattern does:

\[
(D_a,D_b)\Rightarrow Q.
\]

The same can occur at the decision level: neither source alone warrants modification `m`, while the joint evidence does.

Therefore:

\[
\boxed{
\text{warrant need not decompose into independent evidence tokens}.
}
\]

A future warrant formalism cannot assume simple additivity or componentwise sufficiency.

The dependency structure matters.

This also prevents a naive ledger from recording only independent per-source “authority scores” and then summing them.

No additive or non-additive algebra is proposed here.

---

# Attack 8 — apparently independent evidence can share one failure mode

The converse joint-evidence problem also matters.

Two evidence channels may appear to provide separate support while sharing the same upstream measurement defect, training corpus, calibration artifact, simulator assumption, or preprocessing transformation.

Counting them as two independent warrants can silently amplify one evidential basis.

Thus:

\[
\boxed{
\text{two evidence sources}
\not\Rightarrow
\text{two independent warrant sources}.
}
\]

Statistical independence is not the only issue. The relevant question is whether the claimed evidential authority has genuinely distinct identification support or whether the branches inherit the same unvalidated assumption.

No universal independence criterion is frozen here.

---

# Attack 9 — conflicting valid evidence does not imply one source is invalid

Suppose two prospectively valid measurements support different decisions.

That can happen because they identify different dimensions:

- one identifies target efficacy;
- one identifies protected-behavior risk;
- one applies to population `A`;
- one applies to population `B`;
- one concerns short-horizon behavior;
- one concerns long-horizon behavior.

The conflict can be scientifically real rather than a measurement failure.

Therefore:

\[
\boxed{
\text{conflicting evidence}
\not\Rightarrow
\text{one evidence source is invalid}.
}
\]

A warrant rule must eventually say how such conflicts affect the scoped decision authority.

But choosing weights after seeing which decision succeeds would make the conflict rule outcome-dependent and therefore self-authorizing.

No weighting or aggregation rule is frozen here.

---

# Attack 10 — evidence can warrant a claim without warranting an action

There is a deeper distinction between epistemic and decisional authority.

Evidence may warrant the claim:

> the current model is miscalibrated.

That does not imply it warrants:

> apply modification `m_7`.

Moving from a supported descriptive/causal claim to a modification can require additional structure:

- the decision objective;
- protected constraints;
- a causal action model;
- uncertainty about intervention effects;
- resource/risk considerations;
- admissibility of abstention.

Therefore:

\[
\boxed{
\text{warrant for }Q
\not\Rightarrow
\text{warrant for modification }m.
}
\]

This is not yet another CCA gate.

It is a warning that “evidence is warranted” and “the evidence warrants this adaptive decision” are different claims.

A future G1 contract must make clear which one it needs.

---

# Attack 11 — action warrant can exist without complete state identification

The reverse reduction also fails.

Suppose evidence leaves two states live:

```text
s1
s2
```

but the same conservative action `m` is justified under both states.

Then the evidence may fail to identify which state is true while still being sufficient for the scoped decision.

Therefore:

\[
\boxed{
\text{decision warrant}
\not\Rightarrow
\text{complete epistemic identification}.
}
\]

A warrant theory that requires a uniquely identified world-state before any action is permitted would be too strong.

This also reinforces that warrant is claim-relative: the information sufficient for one decision may be insufficient for a stronger mechanistic or ontological claim.

---

# Attack 12 — warrant is scope- and context-relative

The same evidence can legitimately warrant different decisions under different prospectively declared contexts.

Examples:

- different protected-behavior constraints;
- different system states;
- different intervention availability;
- different resource envelopes;
- different deployment populations;
- different time horizons;
- different tolerance for reversible versus irreversible changes.

Therefore:

\[
\boxed{
E\text{ fixed}
\not\Rightarrow
\text{warranted decision fixed across contexts}.
}
\]

This does not mean context may be selected after observing which action worked.

The context or scope relevant to the claim must itself have legitimate scientific status.

A post-hoc context choice can manufacture apparent warrant in exactly the same way a post-hoc outcome definition can manufacture apparent success.

---

# Attack 13 — benchmark authority is bounded by benchmark constitution

Suppose a benchmark provides a gold label `c*` for every evidence item.

A system that follows those labels can exhibit strong evidence-controlled selection.

But the benchmark label only has the authority earned by the benchmark's scientific constitution.

If the benchmark's label encodes:

- a synthetic shortcut;
- an arbitrary designer preference;
- a simulator artifact;
- an underspecified objective;
- a scope narrower than deployment;

then benchmark agreement does not create broader warrant.

Thus:

\[
\boxed{
\text{benchmark label}
\not\Rightarrow
\text{general scientific warrant}.
}
\]

This is especially important for G1 because a candidate oracle can otherwise become a hidden authority source whose validity is assumed rather than identified.

---

# Attack 14 — externality is not the same as independent warrant

A possible reaction to circularity is to require every warrant source to be external to the tested system.

That rule is too strong.

Legitimate adaptive systems can generate evidence through their own interventions, sensors, error signals, or internal consistency checks.

A self-generated observation is not invalid merely because the system helped produce it.

Conversely, an external human label or benchmark is not automatically authoritative merely because it is external.

Therefore:

\[
\boxed{
\text{external source}
\not\Rightarrow
\text{independent warrant}
}
\]

and:

\[
\boxed{
\text{endogenous source}
\not\Rightarrow
\text{invalid warrant}.
}
\]

The relevant independence is epistemic/identificational: the authority used to orient the G1 claim must not be manufactured by the same tested outcome whose success it is used to certify.

This statement remains adversarial and does not freeze a formal independence condition.

---

# Attack 15 — prospectivity is useful but not sufficient

A prospectively declared warrant rule can still be scientifically empty.

For example:

```text
Before the experiment:
Whatever candidate produces the highest observed downstream score
will be deemed the warranted candidate.
```

The rule is prospective in the documentary sense, but it delegates warrant to the same outcome later used to establish success.

Therefore:

\[
\boxed{
\text{prospectively specified}
\not\Rightarrow
\text{scientifically warranted}.
}
\]

The update or warrant rule itself must have a scientific interpretation capable of being challenged.

This is consistent with the broader CCA distinction between legitimate adaptive revision and unaccounted self-authorization, but this PR does not import any later candidate law into canonical G1.

---

# Attack 16 — a permanently fixed warrant mapping is also too strong

The opposite rule fails as well.

Scientific warrant can legitimately change when:

- new calibration evidence arrives;
- a causal model is falsified;
- a protected constraint is discovered;
- a previously hidden subgroup is identified;
- the system state changes in a way relevant to the decision;
- a licensed adaptive inference procedure updates the evidential interpretation.

Therefore:

\[
\boxed{
\text{warrant can be revisable}
}
\]

without implying that historical decisions may be relabeled retrospectively.

A revised warrant relation can govern future claims while the authority of prior claims remains attached to the scientific constitution under which it was originally earned, unless new information establishes a contemporaneous contract failure.

No versioning rule is frozen here.

---

# Attack 17 — downstream success cannot be used to choose among competing warrant rules

Suppose two warrant rules are plausible before the experiment:

```text
W1 -> choose c1 under evidence e
W2 -> choose c2 under evidence e
```

The experiment runs, `c2` happens to produce the better downstream result, and the researcher then declares `W2` to have been the correct warrant rule all along.

That inference is not licensed without an independent relation connecting downstream performance to the scientific question that `W1` and `W2` were supposed to answer.

Otherwise:

```text
outcome
-> choose warrant rule
-> reinterpret evidence
-> claim evidence-controlled warranted decision
```

is a closed evidential loop.

Therefore:

\[
\boxed{
\text{successful consequence}
\not\Rightarrow
\text{historical warrant origin}.
}
\]

Downstream results may motivate revision or provide new evidence under a valid protocol. They may not retroactively manufacture the original authority relation.

---

# Attack 18 — causal availability and efficacy do not create warrant

A candidate modification can be executable and effective without being warranted by the evidence.

Likewise, evidence can warrant a decision that is not currently executable.

Therefore:

\[
\boxed{
\text{causal availability}
\not\Rightarrow
\text{warrant}
}
\]

and:

\[
\boxed{
\text{warrant}
\not\Rightarrow
\text{causal availability}.
}
\]

The same applies to efficacy:

\[
\boxed{
\text{effective modification}
\not\Rightarrow
\text{evidence warranted that modification}.
}
\]

This keeps warrant origin distinct from G2 and from later authority transport.

---

# Attack 19 — causal control in the “warranted direction” depends on warrant constitution

G1 is an oriented causal object.

Evidence merely changing candidate probabilities is not enough. The movement must be interpreted as movement in a warranted direction.

But if the warrant orientation is malformed, then an otherwise well-estimated causal response matrix can instantiate the wrong scientific object.

This is not merely estimator failure.

The warrant relation partly constitutes what counts as a positive G1 effect.

Therefore:

\[
\boxed{
\text{reliable causal estimation}
\not\Rightarrow
\text{valid G1 object}
}
\]

when the warrant constitution is invalid.

This mirrors CCA's broader measurement discipline: invalid measurement structure can change the identity of the object being estimated rather than merely add noise around a fixed object.

---

# Attack 20 — multiple valid actions stress the current response-matrix intuition

Earlier G1 adversarial work used fixed candidate-choice coordinates and an independently oriented response matrix to distinguish causal control from raw accuracy.

That remains useful, but multiple-valid-action cases expose a future problem.

If two candidate choices are simultaneously warranted under the scoped evidence state, then a scalar “probability of selecting the uniquely correct candidate” is malformed.

Similarly, if abstention is warranted, movement away from all non-null candidates can be positive rather than negative.

Therefore:

\[
\boxed{
\text{fixed candidate coordinates}
\not\Rightarrow
\text{unique warranted coordinate}.
}
\]

The parent G1 role survives because it is stated in terms of a separable adaptive decision rather than a frozen unique-candidate oracle.

But any future G1 measurement charter must survive these cases before freezing its estimand.

---

# Attack 21 — conflict resolution can itself become the hidden warrant source

Suppose two valid evidence streams conflict and a downstream decision rule combines them with weights:

```text
score = alpha * E1 + beta * E2
```

If `alpha` and `beta` are tuned after observing which choices perform well, then the weighting layer has become the true warrant-generating mechanism.

The evidence sources did not independently authorize the final decision; the post-hoc conflict resolver did.

Thus:

\[
\boxed{
\text{valid evidence components}
\not\Rightarrow
\text{valid combined warrant}.
}
\]

The combination rule must earn its own scientific authority for the claim being made.

This is a composition issue inside warrant generation itself, not an authority-transport claim across a later system seam.

---

# Attack 22 — no universal source of warrant is established

The attack does not identify one privileged source from which all legitimate warrant must originate.

Depending on the scientific object, warrant might eventually be grounded in some combination of:

- direct measurement;
- a validated causal contrast;
- a formal constraint or proof;
- a calibrated predictive model;
- externally supplied labels within a declared scope;
- a prospectively valid sequential decision procedure;
- independently replicated empirical regularity;
- a robust action criterion under uncertainty.

This list is illustrative, not exhaustive, and none of these sources is automatically authoritative by category.

Therefore the attack rejects both extremes:

```text
one universal oracle determines warrant
```

and:

```text
anything called evidence can supply warrant.
```

---

# Attack 23 — warrant origin and authority transport are different scientific questions

Later CCA work has separately stressed whether authority survives changes in configuration, claim, protocol, or implementation.

This attack must not collapse warrant origin into that transport problem.

The two questions are:

```text
WARRANT ORIGIN
Why is evidence authoritative for this claim or decision here?

AUTHORITY TRANSPORT
Why does authority already earned here remain valid after a consequential relation or transformation?
```

A schematic decomposition is:

\[
E
\xrightarrow{\text{warrant}}
A(Q,Z)
\xrightarrow{\text{licensed relation}}
A(Q',Z').
\]

This notation is illustrative only.

The first arrow cannot be justified merely because the second arrow is valid, and the second cannot create authority absent on the first side.

Therefore:

\[
\boxed{
\text{warrant generation}
\neq
\text{authority propagation}.
}
\]

This distinction is the central boundary of the present attack.

---

# Attack 24 — warrant revision and warrant inheritance must not be conflated

Suppose new evidence at time `t+1` shows that the previous scientific understanding was incomplete.

A revised warrant relation can legitimately govern future decisions.

But three cases must remain distinct:

1. the old warrant procedure violated its own contemporaneous contract;
2. a newly relevant dependency changes the scientific object prospectively;
3. new empirical evidence challenges the old claim under the same object.

Only the first case automatically threatens the historical authority as originally constituted.

Therefore:

\[
\boxed{
\text{warrant revision}
\not\Rightarrow
\text{retroactive warrant inheritance or erasure}.
}
\]

No temporal warrant ontology is introduced here.

---

# What the attack refutes

The following are **not sufficient substitutes for warrant**:

```text
information availability
admissibility alone
measurement reliability alone
correctness of the realized choice
downstream success
causal efficacy of the modification
causal availability of the modification
benchmark labels by themselves
external provenance by itself
prospective documentation by itself
unique-action assumptions
raw evidence-source count
simple additive evidence scores
positive G1 causal control itself
```

The attack also rejects these universal rules:

```text
warrant must always be externally supplied
warrant must always be fixed forever
warrant must always select one unique action
warrant requires complete world-state identification
conflicting evidence means one source is invalid
abstention is necessarily G1 failure
```

---

# Strongest surviving candidate interpretation

The canonical G1 role is not refuted by this attack.

The strongest interpretation surviving the counterexamples is approximately:

> **For G1, “warranted” should be treated as a scientifically justified, claim- and decision-relative orientation of admissible evidence whose authority is not manufactured by the tested selector behavior or by downstream success.**

This is **not** a canonical definition.

It does not freeze whether warrant is represented as a relation, correspondence, partial order, decision rule, posterior decision criterion, constraint system, or something else.

The important negative constraints are:

\[
\boxed{
\text{warrant is not an intrinsic scalar property of evidence}
}
\]

\[
\boxed{
\text{warrant need not identify one unique action}
}
\]

\[
\boxed{
\text{warrant can depend on joint evidence, scope, context, and uncertainty}
}
\]

\[
\boxed{
G_1\text{ cannot validate the warrant relation used to score }G_1
}
\]

and:

\[
\boxed{
\text{warrant origin}
\neq
\text{authority transport}.
}
\]

---

# Future warrant constitution must survive these cases

Before any G1 measurement charter can be frozen, a proposed warrant constitution should survive at least the following adversarial cases:

```text
MULTIPLE VALID ACTIONS
More than one decision is scientifically acceptable.

ABSTENTION
The warranted decision is not to modify.

INFORMATION GATHERING
Evidence warrants a diagnostic action rather than a terminal change.

JOINT EVIDENCE
No evidence component is sufficient alone; the combination is.

DEPENDENT EVIDENCE
Apparently separate sources inherit one hidden failure mode.

CONFLICT
Valid evidence identifies different dimensions or populations and points toward different decisions.

CONTEXT DEPENDENCE
The same evidence warrants different decisions under prospectively distinct scopes or constraints.

EPISTEMIC / DECISIONAL SEPARATION
Evidence warrants a claim but not a modification, or warrants an action without identifying the full world state.

ENDOGENOUS EVIDENCE
The system helps generate the evidence without thereby self-authorizing it.

ADAPTIVE REVISION
The warrant relation can change legitimately without rewriting historical authority.

SELF-AUTHORIZATION
Tested behavior or downstream success cannot define the warrant relation used to certify that behavior as warranted.
```

This list is an adversarial burden, not a schema.

---

# Relation to canonical G1

The current canonical sequence remains:

```text
prospectively admissible evidence
        ↓
independent warrant
        ↓
causal assignment
        ↓
separable adaptive decision
        ↓
G1
```

This attack strengthens the interpretation of the second line only by showing what it cannot safely mean.

It does **not** change G1's canonical role.

In particular:

```text
G1 ROLE                    UNCHANGED / PROVISIONALLY FIXED
G1 EMPIRICAL RESULT        UNOBSERVED
G1 CONTRACT                UNFROZEN
G1 IMPLEMENTATION          NOT AUTHORIZED
```

---

# Relation to G2

No G2 object is changed here.

The attack instead sharpens a prerequisite for a later joint G2 analysis.

Evidence that warrants belief in a problem does not automatically warrant modification `m`, and an effective modification does not retroactively prove that evidence warranted it.

Therefore a future end-to-end claim will need to distinguish:

```text
warrant for a decision
causal assignment of that decision
modification assignment / execution
joint target and protection consequences
```

No new bridge gate is introduced.

---

# Relation to later noncanonical authority-transport attacks

PRs #15 and #16 contain adversarial material about evidential self-authorization, claim identity, and authority transport.

Those PRs are not canonical authority and are not imported as laws here.

Their relevance is only diagnostic: they motivate testing whether the **origin** of a warrant can be made non-circular before asking how already-earned authority is transported across later seams.

This PR therefore remains grounded in canonical G1 and treats later attack material as provenance only.

---

# Authority boundary

```text
EMPIRICAL AUTHORITY CHANGE                 NONE
RESEARCH STATE TRANSITION                  NONE
G1 SCIENTIFIC ROLE                         UNCHANGED
G1 WARRANT SEMANTICS                       UNFROZEN / UNDER ADVERSARIAL REVIEW
G1 WARRANT SOURCE                          NOT FROZEN
G1 MULTIPLE-VALID-ACTION SEMANTICS         NOT FROZEN
G1 ABSTENTION SEMANTICS                    NOT FROZEN
G1 CONFLICT RULE                           NOT FROZEN
G1 JOINT-EVIDENCE RULE                     NOT FROZEN
G1 UNCERTAINTY / WEIGHTING RULE            NOT FROZEN
G1 EVIDENCE SET                            NOT FROZEN
G1 INTERFACE / REALIZATION POLICY          NOT FROZEN
G1 ESTIMAND / THRESHOLD                    NOT FROZEN
G1 EXPERIMENT CONTRACT                     UNFROZEN
AUTHORITY-TRANSPORT FORMALISM              NONE
G2 JOINT ESTIMAND                          NONE
PMC / REPEATED-CORRECTION / JT             UNCHANGED
C_improve                                  NOT CANONICALIZED
IMPLEMENTATION / EXECUTION                 NOT AUTHORIZED
```

No repository-wide governance change follows from this attack.

---

# Stopping criterion for this attack

Before CCA freezes any G1 measurement charter, it should be able to answer the following without using realized selector behavior or downstream success to manufacture the answer:

> **Can warrant for the scoped G1 decision be prospectively or otherwise validly constituted in a way that handles multiple valid actions, abstention, joint and conflicting evidence, context dependence, endogenous evidence generation, uncertainty, and legitimate adaptive revision while keeping the warrant's authority distinct from the G1 causal effect it is used to orient?**

The desired result is not a universal warrant formula.

The desired result is a scientific boundary strong enough that a later G1 experiment cannot make its own success count as proof that its evidence-to-decision orientation was warranted.

Until that survives adversarial review:

```text
NO WARRANT FORMALISM
NO G1 CHARTER FREEZE
NO G1 EXPERIMENT
NO G2 COMPOSITION CLAIM
NO IMPLEMENTATION
```
