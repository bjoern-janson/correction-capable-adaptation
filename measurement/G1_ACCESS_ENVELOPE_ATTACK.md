# Level-0 Attack: Can the Realization / Access Envelope Be Specified Without Baking In the Tested System?

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO IMPLEMENTATION**

This document attacks the remaining Level-0 realization/access question exposed by PR #5:

> **Can a representation/access envelope be specified prospectively, independently of tested-system behavior, such that variation in realization does not silently redefine the scientific evidence treatment?**

The target is only the candidate `0A-R` layer.

This analysis does **not**:

- select an ontology;
- freeze an evidence intervention space;
- select a model or prompt;
- construct a benchmark;
- choose statistical thresholds;
- implement ECIM;
- modify `research_state.json`;
- authorize execution;
- merge or canonicalize PR #3, #4, or #5.

The purpose is destructive:

> **Try to show that the realization/access envelope cannot be constituted prospectively without becoming either arbitrary, model-relative, capability-contaminated, or scientifically trivial.**

---

# 1. Starting point

The strongest candidate decomposition surviving the preceding attacks is:

```text
0A-S  semantic constitution
      define the scientific evidence semantics
      and the independently warranted candidate C*(S)

0A-R  realization / access constitution
      define how semantic evidence may be rendered,
      what access conditions are held fixed,
      and what realization policy is admissible

0B    total warranted evidence control
      does admissible evidence causally move selection
      toward C*(S)?

0C    channel / mechanism attribution
      what information-processing route carries that control?
```

PR #5 rejected the naive equivalence:

\[
\text{semantic equivalence}
\Rightarrow
\text{behavioral invariance}.
\]

The current attack asks whether `0A-R` can itself be made scientifically legitimate.

---

# 2. Minimal notation

Let

\[
S
\]

denote the **semantic evidence state**.

Let

\[
C^*(S)
\]

denote the candidate independently warranted by that semantic evidence.

Let

\[
R
\]

denote a **realization variable**: the concrete representation through which the semantic evidence is made available.

Let

\[
K
\]

denote an **externally declared interface contract** specifying the experimental access environment.

Examples of components of \(K\) may include, when relevant:

```text
input modality available
allowed syntax / encoding conventions
available tools or decoders
context / memory interface
interaction protocol
number of turns
candidate presentation interface
response interface
```

Let the concrete delivered evidence be

\[
E_{\mathrm{raw}}=h(S,R;K).
\]

A realization policy may be written as

\[
R\sim Q_R(\cdot\mid S,K).
\]

The candidate scientific question at `0B` is then not abstractly

\[
S\rightarrow C_{\mathrm{selected}}
\]

without operationalization.

It is closer to:

\[
S
\xrightarrow[\ R\sim Q_R,\ K\ \text{fixed}\ ]{}
E_{\mathrm{raw}}
\rightarrow
C_{\mathrm{selected}},
\]

with success judged relative to \(C^*(S)\).

The attack is whether \(K\) and \(Q_R\) can be frozen without turning them into hidden model tuning.

---

# 3. First target: the envelope may be too broad

Suppose two realizations encode the same semantic evidence:

\[
R_1\sim_S R_2.
\]

But they impose radically different operational demands.

For example:

```text
R1  plain-language text
R2  encrypted or encoded text with no decoder supplied
```

or:

```text
R1  short textual table
R2  equivalent information distributed across a representation
    far beyond the declared context-access mechanism
```

or:

```text
R1  text
R2  audio waveform
```

when the tested interface exposes only text input.

In each case the semantic content may be recoverably equivalent **for an external ideal observer**.

But the realized treatment is not equivalent relative to the experimental access environment.

Therefore:

\[
\boxed{
\text{semantic recoverability in principle}
\not\Rightarrow
\text{admissible realization under }K
}
\]

A realization envelope that includes all semantically equivalent encodings is too broad.

It confounds at least two questions:

1. whether the evidence warrants a candidate;
2. whether the tested system has the interface/access capability needed to recover that evidence from the realization.

This does **not** mean the second question is unscientific.

It means it is a different scientific property.

If the envelope silently treats both as nuisance-equivalent, the measurement object is malformed.

### Verdict on the too-broad attack

The attack succeeds against the proposition:

> Every semantics-preserving realization belongs to the same primary G1 treatment class.

That proposition is false.

---

# 4. Second target: the envelope may be too narrow

The opposite response is to choose one canonical realization:

\[
Q_R(R=r_0)=1.
\]

For example:

```text
all evidence uses exactly one textual template
fixed ordering
fixed punctuation
fixed notation
fixed input protocol
```

This makes the operational treatment clear.

But the earned claim becomes correspondingly narrow:

> Under realization \(r_0\) and interface contract \(K\), assigned semantic evidence causally controlled warranted selection.

This may be perfectly valid.

What it does **not** establish is:

- representation-stable evidence control;
- interface-independent correction;
- transfer to alternative realizations;
- general accessibility of the semantic evidence;
- robustness to presentation changes.

Therefore a narrow envelope is not automatically a measurement defect.

It is a **scope limitation**.

This distinction matters because the program must not repair narrow external validity by pretending a broader claim was measured.

### Verdict on the too-narrow attack

The attack does **not** refute narrow realization-specific G1.

It refutes only any unearned generalization from it.

Thus:

\[
\boxed{
\text{narrow envelope}
\neq
\text{invalid measurement}
}
\]

but

\[
\boxed{
\text{narrow envelope}
\Rightarrow
\text{narrow claim ceiling}.
}
\]

---

# 5. Third target: model-relative envelope construction

A dangerous procedure would be:

```text
1. generate many realizations;
2. probe the tested model;
3. observe which forms it parses successfully;
4. discard hard forms;
5. call the survivors the “licensed representation envelope”;
6. estimate G1 only there.
```

That is not prospective measurement constitution.

It is outcome-informed treatment selection.

The realized scientific object has been shaped by tested-system behavior.

The problem remains even if the filtering uses an apparently innocuous auxiliary task rather than the final primary outcome, because model behavior still determines which evidence realizations enter the target population.

This can produce a form of circular measurement:

\[
\text{model behavior}
\rightarrow
\text{admissible }R
\rightarrow
\text{measured model behavior}.
\]

Therefore:

\[
\boxed{
Q_R\text{ may not be selected by post-hoc tested-model success}
}
\]

if the aim is to estimate an independently constituted G1 object.

---

# 6. Prospective does not mean system-blind

The previous section creates an important asymmetry.

It is too strong to require the realization envelope to ignore all properties of the target system class.

An experiment may prospectively declare that its target population consists of systems with a specific public interface contract.

For example:

```text
text input is available
no image input is available
no external decoder tool is available
maximum delivered context is prospectively bounded
interaction is single-turn
```

Conditioning on such an **ex ante interface specification** is not the same as tuning to observed behavioral competence.

The relevant distinction is:

```text
ALLOWED FOR CONSTITUTION
known interface / protocol facts declared before testing

NOT ALLOWED FOR CONSTITUTION
behavioral filtering based on which realizations the tested system
actually solves, parses, or prefers
```

So `0A-R` can be system-class-relative in a legitimate sense while remaining behavior-independent.

Formally, the envelope may depend on \(K\):

\[
\mathcal R_{\mathrm{adm}}(S;K),
\]

provided \(K\) is declared independently of the experimental behavior used to evaluate G1.

This yields a scoped object:

\[
G_1(K,Q_R).
\]

The dependence on \(K\) is part of the estimand's scope, not an embarrassment to be hidden.

---

# 7. Fourth target: capability contamination

Now consider the hardest case.

Semantic evidence is fixed:

\[
S=s.
\]

Two realizations are both admitted under the frozen envelope:

\[
R_1,R_2\in\mathcal R_{\mathrm{adm}}(s;K).
\]

The oracle is unchanged:

\[
C^*(s,R_1)=C^*(s,R_2)=C^*(s).
\]

But observed warranted-selection performance differs:

\[
G_1(s,R_1)\neq G_1(s,R_2).
\]

What happened?

There are at least three scientifically different possibilities.

## 7.1 Measurement defect

The discrepancy is a measurement defect if one of the supposed realizations violates the frozen treatment contract.

Examples:

- semantic content was not actually preserved;
- oracle invariance fails;
- a realization includes extra candidate-identifying information not licensed by the semantics;
- the realization violates the declared interface contract \(K\);
- assignment or rendering was corrupted;
- the intended realization policy was not followed.

Then the affected contrast is invalid/unobserved, not evidence of G1 failure.

## 7.2 Legitimate access-capability effect

If both realizations satisfy the frozen semantic and interface contract, then the difference may be a real property of the tested system:

> The same semantic evidence is more effectively accessible through one licensed realization than another.

That is not automatically nuisance.

It may reflect:

- parsing competence;
- representation sensitivity;
- memory organization;
- modality handling;
- compression costs;
- tokenization effects;
- salience allocation;
- learned conventions;
- architectural priors;
- other access-related capability.

If \(R\) was prospectively included as a design factor or sampled under a frozen \(Q_R\), this heterogeneity is scientifically legitimate.

## 7.3 Underspecified estimand

If the original contract said only

> measure semantic evidence control

but never specified how realization is distributed or scoped, then the discrepancy reveals an underspecified scientific object.

The problem is not the system.

The problem is that

\[
G_1(S)
\]

was written as though realization had disappeared when in fact the operational outcome depends on it.

The estimand must then be made explicit prospectively in a new contract, for example as realization-specific, realization-averaged, or representation-stability-focused.

### Central classification rule

Thus the same empirical pattern

\[
G_1(s,R_1)\neq G_1(s,R_2)
\]

cannot be classified from the numbers alone.

Its meaning depends on the frozen `0A-R` contract.

---

# 8. Can realization affect measurement only through a declared “access burden”?

The strongest version of the proposed question asks whether realization variation can be made to affect the outcome only through a declared access burden.

Suppose one introduces

\[
B(R;K)
\]

as an access-burden variable and hopes for a structure such as

\[
R\rightarrow B\rightarrow C_{\mathrm{selected}}.
\]

This is generally too strong.

Representation changes can simultaneously alter many computational properties:

```text
sequence length
tokenization
ordering
locality
salience
redundancy
modality
symbol familiarity
memory demand
parsing depth
required composition
available cues
inductive bias
```

These properties may not admit a single model-independent ordering.

Two realizations can be easier for different systems for different reasons.

Even a vector-valued burden descriptor

\[
B=(B_1,\ldots,B_p)
\]

does not establish that all effects of realization on selection are mediated through the declared descriptors.

That would be a mechanism-identification claim requiring additional assumptions or interventions.

Therefore the following universal proposition is refuted:

\[
\boxed{
R\text{ affects G1 only through a prospectively declared access-burden variable}
}
\]

in general.

`0A-R` can define **admissibility and sampling policy** without claiming a complete causal decomposition of representation effects.

This is a critical subtraction.

The access envelope is not itself a mediation model.

---

# 9. What can be frozen independently of tested behavior?

The attack suggests a narrower but viable target.

Before observing tested-system performance, one can prospectively freeze:

## 9.1 Interface contract \(K\)

What channels and resources the experiment makes available.

This defines the experimental context.

## 9.2 Semantic-preservation rule

For every admitted realization:

\[
S(h(S,R;K))=S
\]

under an independent semantic validator or constructive rule.

The exact validator remains future contract work.

## 9.3 Oracle preservation

For admitted realizations:

\[
C^*(S,R)=C^*(S).
\]

This must follow from the semantics, not from model behavior.

## 9.4 Realization generator / admissibility algorithm

A model-independent procedure such as

\[
R\leftarrow\mathcal A_R(S,K,U),
\]

where \(U\) is a frozen random seed or prospectively specified source of variation.

The generator may use the declared interface contract.

It may not query tested-model outputs to decide whether a realization is admissible.

## 9.5 Realization policy \(Q_R\)

The distribution or counterbalancing policy over admitted realizations.

Changing \(Q_R\) changes the target population of realizations and may therefore change the scientific estimand.

This policy cannot be treated as an invisible implementation detail.

---

# 10. What cannot be guaranteed independently of tested behavior?

The following stronger properties generally cannot be established by measurement construction alone:

- equal effective accessibility across realizations;
- equal computational cost to the tested system;
- equal parsing difficulty;
- equal salience;
- equal internal representation;
- equal reasoning depth;
- equal behavioral performance;
- complete mediation by a declared access-burden variable.

These are system properties or mechanism claims.

Thus:

\[
\boxed{
\text{prospective realization admissibility}
\neq
\text{prospective equality of effective access}
}
\]

This is the strongest negative result of the attack.

---

# 11. Three legitimate G1 targets remain distinct

Once \(K\) and \(Q_R\) are explicit, at least three different scientific objects can be defined.

## 11.1 Realization-specific G1

For a fixed realization \(r\):

\[
G_1^{(r)}.
\]

Claim ceiling:

> Evidence control under this specific realization and interface contract.

## 11.2 Realization-policy G1

For

\[
R\sim Q_R,
\]

define a semantic treatment effect marginalized over the prospectively declared realization policy.

Schematically:

\[
G_1^{(Q)}
=
\mathbb E_{R\sim Q_R}[G_1^{(R)}].
\]

The exact causal estimand is not frozen here.

The important point is conceptual:

\[
\boxed{Q_R\text{ is part of the scientific target population}}
\]

rather than an incidental renderer setting.

## 11.3 Representation-stable G1

A stronger object asks whether warranted evidence control remains acceptably stable across a declared realization class.

This could involve prospectively specified heterogeneity bounds, worst-case criteria, or equivalence tests.

That is a separate robustness/accessibility claim.

It is not automatically required for basic G1.

---

# 12. A constructive separation witness

To test whether `0A-R` is logically necessary, consider two systems under the same semantic evidence conditions and realization policy.

System A performs well on all admitted realizations.

System B performs well only on one subset of admitted realizations but poorly on another.

Suppose both systems show the same realization-policy average warranted-selection effect:

\[
G_{1,A}^{(Q)}=G_{1,B}^{(Q)}.
\]

Then the parent G1 outcome is identical under the frozen policy.

But their representation-access profiles differ.

Therefore:

\[
\boxed{
\text{parent G1 under }Q_R
\text{ does not identify representation-stability capability}
}
\]

and

\[
\boxed{
\text{representation-stability capability}
\text{ is additional authority}
}
\]

rather than part of the definition by default.

This parallels the separation already established between G1 total evidence control and 0C channel attribution.

---

# 13. A constructive contamination witness

Now suppose the experimenter observes that a tested system fails on realization family \(\mathcal R_B\) but succeeds on \(\mathcal R_A\).

The experimenter then redefines

\[
\mathcal R_{\mathrm{adm}}:=\mathcal R_A
\]

and reports strong G1.

Even if every realization in \(\mathcal R_A\) is semantically valid, the target population was selected using tested-system behavior.

This can arbitrarily improve the apparent effect.

Thus:

\[
\boxed{
\text{post-hoc accessibility filtering}
\Rightarrow
\text{measurement contamination}
}
\]

unless explicitly treated as a new prospective scientific object.

A descendant contract could study \(\mathcal R_A\), but it cannot retroactively redefine the original envelope.

---

# 14. Does system identity itself contaminate the envelope?

Not necessarily.

Suppose the target scientific population is:

> text-interface language models under a single-turn text-only protocol.

Then text-only access is part of the population definition.

This is analogous to defining an experimental apparatus compatible with the entity being studied.

The problem arises when the envelope uses **empirical competence** rather than **declared interface compatibility**.

So:

\[
\boxed{
\text{system-relative interface scope}
\neq
\text{behavior-relative measurement tuning}
}
\]

This distinction is essential.

`0A-R` need not be universal across every adaptive system.

It must be prospectively reconstructible and independent of the outcome behavior used to evaluate the object.

---

# 15. The term “nuisance” is too strong by default

A variable is often called a nuisance when it is not scientifically central.

But realization \(R\) cannot automatically be treated as nuisance in the causal sense.

If changing \(R\) changes how effectively the system can extract admissible evidence, then \(R\) reveals a real property of system-environment interaction.

Therefore the safer terminology is:

```text
realization factor
access factor
representation context
```

until the scientific contract has earned a stronger invariance claim.

The program should not declare an observed representation effect “nuisance” merely because it complicates the desired interpretation.

---

# 16. The access envelope is part of external validity

The current attack reveals that `0A-R` has two roles that should not be conflated.

First, it is needed for **internal validity**:

- the semantic treatment must be operationally instantiated;
- assignments must be reconstructible;
- the interface must be compatible with the experimental protocol.

Second, it defines **external-validity scope**:

- which representations are in the target population;
- what forms of access the claim covers;
- whether the result is realization-specific or realization-averaged.

This means the envelope partly determines what population the G1 claim refers to.

That is legitimate if declared prospectively.

It is not legitimate if broadened after success or narrowed after failure without new lineage.

---

# 17. Refuted propositions

The attack refutes the following general claims:

## R1

\[
\boxed{
\text{all semantically equivalent realizations are interchangeable G1 treatments}
}
\]

False.

## R2

\[
\boxed{
\text{admitted realizations can always be made equal in effective accessibility prospectively}
}
\]

False in general.

## R3

\[
\boxed{
\text{realization effects can always be reduced to one declared access-burden mediator}
}
\]

False in general.

## R4

\[
\boxed{
\text{a narrow interface-specific G1 is scientifically invalid}
}
\]

False; it is narrow, not necessarily invalid.

## R5

\[
\boxed{
\text{the realization envelope must be blind to all facts about the tested system class}
}
\]

Too strong. Ex ante interface compatibility may legitimately define scope.

## R6

\[
\boxed{
\text{behavior-informed pruning of the envelope preserves the same G1 object}
}
\]

False.

---

# 18. Candidate structure surviving the attack

The strongest treatment architecture that survives is more explicit than `0A-R` alone:

```text
0A-S  semantic constitution
      What evidence state S is scientifically meant?
      What uniquely warrants C*(S)?

0A-I  interface contract
      What channels, tools, resource interfaces,
      and protocol are prospectively available?

0A-R  realization constitution
      Which realizations preserve S and C*(S)
      within 0A-I, and how are they sampled by Q_R?

0B    total warranted evidence control
      Under frozen (0A-I, 0A-R), does intervention on S
      causally move selection toward C*(S)?

0B-R  representation/access heterogeneity
      Does G1 vary across admitted realizations?
      This is an additional system property, not automatically failure.

0C    mechanism / channel attribution
      Which information-processing route carries the effect?
```

This decomposition is **not made canonical here**.

It is the strongest candidate surviving the present attack.

---

# 19. Central result

The exact destructive question was:

> Can a representation/access envelope be specified prospectively, independently of tested-system behavior, such that variation in realization affects measurement only through a declared access burden rather than silently redefining the scientific evidence treatment?

The answer is mixed.

## Survives

A realization/access envelope can be prospectively constituted **relative to an externally declared interface contract** using model-independent semantic/oracle-preservation rules and a frozen realization policy.

Therefore:

\[
\boxed{
0A\text{-R is feasible in principle as a treatment-scope layer.}
}
\]

## Fails

The stronger requirement that all admitted realization effects flow only through a predeclared model-independent “access burden” is not generally identifiable or true.

Therefore:

\[
\boxed{
0A\text{-R cannot guarantee access equivalence or single-mediator purity.}
}
\]

The clean compression is:

\[
\boxed{
\text{prospective realization envelope}
=
\text{admissibility + scope + sampling policy},
}
\]

not:

\[
\boxed{
\text{prospective realization envelope}
=
\text{proof that representation no longer matters}.
}
\]

---

# 20. Classification of the nasty case

For fixed semantic evidence \(S=s\), suppose:

\[
G_1(s,R_1)\neq G_1(s,R_2).
\]

The prospective contract should classify this as follows.

### Measurement defect

Only if \(R_1\) or \(R_2\) violates the frozen semantic/oracle/interface/assignment contract.

### Legitimate access-capability effect

If both are admissible and representation heterogeneity is within the target population.

### Estimand underspecification

If the realization target population or policy was never prospectively declared, so “G1” had no unique operational meaning across representations.

This triage prevents the experimenter from deleting genuine capability differences by labeling them nuisance after observation.

---

# 21. Relation to CCA

CCA asks whether valid correction can govern adaptive change.

That property must be tested through some interface, but it should not be silently identified with universal interface competence.

A valid result may therefore have the form:

> Under interface contract \(K\) and prospectively frozen realization policy \(Q_R\), admissible semantic evidence causally controlled warranted selection.

That is a meaningful CCA result at G1.

A stronger claim such as

> the system remains correction-capable across substantially different evidence realizations

requires additional evidence.

This preserves the broader CCA distinction:

\[
\boxed{
\text{functional correction under a declared interface}
\neq
\text{general representation robustness}
}
\]

while leaving representation robustness scientifically available as a later or parallel property.

---

# 22. Relation to C_improve

The provisional `C_improve` object concerns whether valid feedback can be converted into warranted, validated transformation and ultimately increased future viability.

A representation envelope is part of the environment through which valid feedback reaches the system.

Therefore eventual claims about `C_improve` will also require explicit scope over access conditions.

But `C_improve` should not be definitionally tied to one representation mechanism or to universal representation invariance.

The present attack therefore supports:

\[
\boxed{
C_{\mathrm{improve}}
\text{ is interface-scoped in measurement, but not interface-specific in theory.}
}
\]

This remains theoretical only.

---

# 23. What the attack does not authorize

This analysis does not authorize:

- choosing \(K\);
- choosing \(Q_R\);
- selecting a candidate ontology;
- freezing semantic evidence \(S\);
- freezing \(C^*(S)\);
- selecting a model;
- constructing prompts;
- selecting a benchmark;
- choosing thresholds;
- implementing ECIM;
- executing G1;
- changing Level-0 lifecycle state.

The current state remains `ADVERSARIAL_REVIEW`.

---

# 24. Next destructive target

The attack leaves a sharper upstream problem.

If a parent G1 is to be defined under a prospectively frozen realization policy, then the next question is:

> **Can the semantic treatment, interface contract, realization policy, and warrant mapping jointly define a causal G1 estimand whose intervention is independently manipulable and whose counterfactual contrast does not change other selection-relevant variables?**

In other words:

\[
\boxed{
\text{treatment constitution may now be conceptually separable,}
}
\]

but the causal identifiability of

\[
do(S=s)
\]

under frozen \((K,Q_R)\) has not yet been earned.

No implementation follows from this document.
