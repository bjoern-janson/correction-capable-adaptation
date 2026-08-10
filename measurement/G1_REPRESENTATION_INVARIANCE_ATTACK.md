# Level-0 Attack: Representation Invariance Without Semantic Drift

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO IMPLEMENTATION**

This document attacks the remaining Level-0 boundary between treatment constitution and total warranted-selection control:

\[
0A\rightarrow0B.
\]

The proposition under attack is:

> **Semantic equivalence, licensed representation transformations, and total warranted-selection control can be defined independently enough that representation invariance is a legitimate scientific requirement rather than an arbitrary robustness preference.**

This document does **not**:

- select a canonical definition of \(G_1\);
- select a candidate ontology;
- freeze an evidence intervention space;
- modify `research_state.json`;
- implement ECIM;
- select a model, prompt, benchmark, estimator, or compute substrate;
- authorize execution;
- alter ASI-0.

The analysis is restricted to the measurement layer.

---

# 1. Starting architecture

The strongest candidate decomposition surviving the preceding attacks is:

```text
0A  scientific treatment constitution
    define admissible evidence and warrant

0B  total warranted evidence control (G1)
    does intervention on admissible evidence move selection toward C*(E)?

0C  mechanism / channel attribution (M1)
    which information structure carries that control?
```

The current attack asks whether \(0A\) can define an evidence treatment stable enough to support \(0B\) without silently defining a robustness benchmark or privileging a particular information-processing mechanism.

---

# 2. Raw evidence, semantic evidence, and representation

Let

\[
\mathcal E_{\mathrm{raw}}
\]

be the space of physically presented evidence objects: strings, tables, paired examples, serialized records, images, or other concrete realizations.

A raw presentation is denoted

\[
e\in\mathcal E_{\mathrm{raw}}.
\]

The desired scientific object is not automatically the byte sequence or token sequence itself.

Introduce a prospective semantic map

\[
\pi_{\mathrm{sem}}:\mathcal E_{\mathrm{raw}}\rightarrow\mathcal S,
\]

where \(\mathcal S\) is the declared semantic evidence space.

Define semantic equivalence by

\[
\boxed{
e\sim_E e'
\iff
\pi_{\mathrm{sem}}(e)=\pi_{\mathrm{sem}}(e').
}
\]

The equivalence class

\[
[e]_E
\]

contains raw presentations that instantiate the same prospectively declared evidence semantics.

This relation is scientifically usable only if \(\pi_{\mathrm{sem}}\) is defined independently of tested-model behavior.

It may depend on:

- a frozen ontology;
- frozen candidate semantics;
- a frozen evidence-generating process;
- explicit truth conditions;
- an independent oracle;
- declared admissible transformations.

It may not depend on:

- which presentation produces better model behavior;
- which presentation causes the desired selection;
- observed performance;
- discovered shortcuts after execution;
- post-hoc relabeling of failed conditions.

Thus the first necessary condition is:

\[
\boxed{
\text{semantic equivalence must be constituted before observing selector behavior.}
}
\]

---

# 3. Oracle factorization

Let the independently warranted candidate be

\[
C^*(e).
\]

If semantic equivalence is real, warrant must factor through the semantic object:

\[
\boxed{
C^*(e)=g(\pi_{\mathrm{sem}}(e))
}
\]

for some prospectively defined oracle \(g\).

Therefore:

\[
e\sim_E e'
\Rightarrow
C^*(e)=C^*(e').
\]

This is not a behavioral invariance claim about the tested system.

It is a **constitutive validity condition** for calling the two evidence realizations semantically equivalent for the scientific object.

If a proposed transformation \(T\) changes \(C^*\), then either:

1. \(T\) is not licensed as evidence-preserving; or
2. the semantic map / oracle is internally inconsistent.

Thus oracle invariance is hard:

\[
\boxed{
T\in\mathcal T_E
\Rightarrow
C^*(T(e))=C^*(e).
}
\]

But this does not yet imply equal selector behavior.

---

# 4. First destructive test: semantic equivalence does not imply equal accessibility

Consider two evidence presentations with the same declared proposition.

### Presentation A

```text
The warranted candidate is determined by the examples shown below in ordinary readable notation.
```

### Presentation B

The same evidence is losslessly encoded under a cipher, compression scheme, or representation requiring a decoder unavailable to the tested system.

An independent oracle with access to the decoding convention can establish:

\[
\pi_{\mathrm{sem}}(e_A)=\pi_{\mathrm{sem}}(e_B).
\]

Hence:

\[
e_A\sim_E e_B.
\]

But for the tested system:

\[
P(C=C^*\mid do(e_A))
\gg
P(C=C^*\mid do(e_B))
\]

may be entirely expected.

This difference does not necessarily mean the system has failed to use evidence appropriately.

It may mean the two representations impose different **access costs**.

Therefore:

\[
\boxed{
\text{semantic equivalence}
\not\Rightarrow
\text{behavioral invariance}.
}
\]

This refutes the strongest naive version of the proposed invariance principle.

---

# 5. Representation is not automatically nuisance

A representation can alter:

- token length;
- parsing complexity;
- memory burden;
- perceptual salience;
- decompression cost;
- required background conventions;
- syntactic ambiguity;
- ordering burden;
- context-window competition;
- computational difficulty.

These differences may be genuine properties of the evidence interface.

If the scientific question concerns whether a system can use evidence **under a particular access envelope**, those properties may be constitutive rather than nuisance.

Therefore the dichotomy

```text
semantic content
vs
mere representation
```

is generally too coarse.

The attack suggests a three-part object:

```text
semantic evidence
+
representation / access envelope
+
selector
```

rather than semantic evidence plus arbitrary nuisance.

---

# 6. A second prospective map is needed

Introduce an access/representation descriptor

\[
\pi_{\mathrm{acc}}:\mathcal E_{\mathrm{raw}}\rightarrow\mathcal A.
\]

This map describes scientifically relevant features of how the semantic evidence is made accessible.

It need not be a scalar difficulty score.

It may specify a declared equivalence class or admissible envelope such as:

```text
same modality
same language
same decoding conventions
same example count
same information-bearing fields
bounded length range
same candidate ontology exposure
same resource budget
same interaction opportunities
```

The exact contents remain experiment-specific and prospective.

The important point is structural:

\[
\boxed{
\pi_{\mathrm{sem}}(e)
\text{ and }
\pi_{\mathrm{acc}}(e)
\text{ are distinct scientific descriptions.}
}
\]

Two raw presentations may have the same semantics but different access envelopes.

---

# 7. Licensed transformations must declare what they preserve

A transformation

\[
T:\mathcal E_{\mathrm{raw}}\rightarrow\mathcal E_{\mathrm{raw}}
\]

cannot be called a nuisance transformation merely because an experimenter regards the underlying proposition as unchanged.

At minimum, a licensed transformation must satisfy:

\[
\pi_{\mathrm{sem}}(T(e))=\pi_{\mathrm{sem}}(e).
\]

But whether it must also satisfy

\[
\pi_{\mathrm{acc}}(T(e))=\pi_{\mathrm{acc}}(e)
\]

depends on the scientific object.

This yields two transformation classes.

## 7.1 Semantic-preserving transformations

\[
\mathcal T_{\mathrm{sem}}
=
\{T:\pi_{\mathrm{sem}}(T(e))=\pi_{\mathrm{sem}}(e)\}.
\]

These preserve declared meaning and warrant.

They may still alter accessibility.

## 7.2 Scientific-treatment-preserving transformations

If the scientific treatment includes an access envelope, define a narrower class:

\[
\mathcal T_{\mathrm{sci}}
=
\{T:
\pi_{\mathrm{sem}}(T(e))=\pi_{\mathrm{sem}}(e),
\pi_{\mathrm{acc}}(T(e))\equiv_{\mathcal A}\pi_{\mathrm{acc}}(e)
\}.
\]

where \(\equiv_{\mathcal A}\) is a prospectively declared access-equivalence relation.

Only transformations in the class relevant to the frozen scientific object can ground an invariance requirement.

Thus:

\[
\boxed{
\text{transformation validity is object-relative and must be declared prospectively.}
}
\]

---

# 8. Second destructive test: candidate-order permutation

Suppose candidate identifiers are opaque and candidate presentation order is permuted consistently.

Let \(T_\pi\) permute presentation slots and their opaque identifiers while preserving semantic candidate identity.

At the presentation-token level:

\[
C^*_{\mathrm{token}}(T_\pi(e))
=\pi(C^*_{\mathrm{token}}(e)).
\]

After mapping back to semantic candidate identity:

\[
C^*_{\mathrm{semantic}}(T_\pi(e))
=C^*_{\mathrm{semantic}}(e).
\]

If candidate position has no scientific authority and the transformation preserves all declared access conditions, then position permutation is a plausible member of \(\mathcal T_{\mathrm{sci}}\).

A selector whose success changes dramatically by candidate slot is presentation-sensitive.

But whether this **invalidates G1** still depends on the G1 estimand.

This is the next key distinction.

---

# 9. Exact behavioral invariance is not the only coherent G1 object

Let raw realization \(r\) instantiate semantic evidence state \(s\).

Write:

\[
e=(s,r)
\]

schematically, with

\[
\pi_{\mathrm{sem}}(e)=s.
\]

Define warranted-selection success:

\[
S=\mathbf 1[C_{\mathrm{selected}}=C^*(s)].
\]

There are at least three scientifically distinct candidate objects.

## 9.1 Realization-specific G1

\[
\theta_1(s,r)
=
P(S=1\mid do(S=s,R=r)).
\]

This makes the concrete representation part of the treatment.

No representation invariance is claimed.

This is narrow and potentially presentation-specific.

## 9.2 Semantic-class average G1

Prospectively define a licensed realization distribution

\[
Q(r\mid s).
\]

Then define a stochastic intervention:

\[
do(S=s),\qquad R\sim Q(\cdot\mid s).
\]

The semantic-class success quantity is

\[
\boxed{
\bar\theta_1(s;Q)
=
E_{R\sim Q(\cdot\mid s)}
[P(S=1\mid do(s,R))].
}
\]

A causal contrast can then compare warranted selection across semantic evidence conditions while averaging over prospectively licensed representations.

Under this object, exact equality

\[
\theta_1(s,r)=\theta_1(s,r')
\]

is **not required**.

Representation heterogeneity is allowed and can be reported separately.

The claim is scoped to the frozen realization policy \(Q\).

## 9.3 Representation-stable G1

A stronger object may require bounded heterogeneity or worst-case performance over a licensed class:

\[
\inf_{r\in\mathcal R_s}\theta_1(s,r)>\tau
\]

or

\[
\max_{r,r'\in\mathcal R_s}
|\theta_1(s,r)-\theta_1(s,r')|
<\epsilon_R.
\]

This is a distinct robustness / representation-stability claim.

It must not be silently folded into baseline G1.

Therefore:

\[
\boxed{
\text{representation-stable G1}
\text{ is stronger than }
\text{semantic-class average G1}.
}
\]

---

# 10. Third destructive test: exact invariance can erase a real system property

Suppose two licensed semantic-preserving representations differ only in notation complexity.

Both encode the same admissible evidence and preserve \(C^*\).

A tested system uses one notation reliably and another poorly.

If the project requires exact behavioral invariance by definition, then the system fails G1 even if it:

- reliably uses admissible evidence under the intended operating distribution;
- selects warranted modifications;
- remains fully correctable under the declared interface;
- merely lacks robustness to an alternative notation.

That would make G1 partly a notation-generalization benchmark.

This may be scientifically useful, but it is not forced by the CCA mission.

CCA's parent question concerns whether valid correction can govern adaptive change, not whether every semantically equivalent representation is equally accessible.

Thus:

\[
\boxed{
\text{behavioral invariance over all semantic equivalences}
\text{ is too strong as a default CCA requirement.}
}
\]

---

# 11. But raw-representation dependence cannot be ignored either

The opposite extreme also fails.

Suppose semantic evidence condition \(s_a\) is always presented in a privileged format \(r_a\), while \(s_b\) is always presented in a different format \(r_b\).

Then:

\[
S\rightarrow R\rightarrow C
\]

is perfectly confounded with semantic condition.

A positive contrast cannot distinguish:

- semantic evidence control;
- presentation control;
- their interaction.

Therefore semantic-class G1 requires a prospectively controlled realization policy.

At minimum, representations must be:

- matched;
- randomized;
- counterbalanced; or
- otherwise structured so that representation is not deterministically confounded with warrant.

Thus:

\[
\boxed{
\text{channel-agnostic G1 still requires representation-controlled treatment assignment.}
}
\]

---

# 12. The scientific treatment is not just the equivalence class

The attack therefore rejects a tempting compression:

\[
\text{scientific treatment}= [e]_E
\]

without further qualification.

A more defensible treatment object is:

\[
\boxed{
\text{scientific evidence intervention}
=
(\text{semantic state }s,
\text{prospectively frozen realization policy }Q)
}
\]

or, where representation stability is part of the claim:

\[
\boxed{
(s,\mathcal R_s,\epsilon_R)
}
\]

with the relevant access and transformation rules explicitly declared.

The treatment is therefore **semantic but operationally instantiated**.

---

# 13. Model-independent equivalence survives, but only prospectively and locally

Can \(e\sim_E e'\) be defined without reference to tested-model outputs?

Yes in principle, when the ontology supplies an independent semantic truth condition.

Examples include:

- logically equivalent statements under a frozen formal language;
- paired demonstrations generated by the same frozen function;
- candidate-preserving permutations with explicit semantic identity mapping;
- order permutations of examples where order is not semantically meaningful;
- serialization variants whose parser semantics are prospectively specified.

But no universal representation equivalence relation exists independently of the scientific object.

For natural-language evidence, visual evidence, compressed evidence, or interfaces with ambiguous conventions, equivalence may itself be contestable.

Therefore:

\[
\boxed{
\sim_E
\text{ is a local measurement contract, not a universal semantic relation.}
}
\]

That is acceptable if its scope is explicit.

---

# 14. Oracle invariance is stronger than semantic similarity

A common failure would be to label two presentations “equivalent” because they appear similar to a human evaluator.

That is insufficient.

For scientific treatment identity, the oracle must establish that the warranted candidate is preserved:

\[
C^*(T(e))=C^*(e).
\]

Ideally this follows mechanically from the frozen semantics.

If oracle invariance cannot be derived without consulting tested-model behavior, the transformation is not independently licensed.

Thus:

\[
\boxed{
\text{oracle invariance is constitutive evidence for transformation validity.}
}
\]

---

# 15. Invariance must be indexed to a declared claim

The phrase

> “G1 should be representation invariant”

is underspecified.

At least four invariance claims differ:

```text
I1  semantic invariance
    T(e) has the same declared evidence meaning

I2  warrant invariance
    C*(T(e)) = C*(e)

I3  treatment-envelope invariance
    T(e) remains inside the same frozen access/representation class

I4  behavioral invariance
    selector success is stable under T
```

The first three concern treatment constitution.

The fourth is a property of the tested system.

They must not be collapsed.

In particular:

\[
I1\land I2\land I3
\not\Rightarrow I4.
\]

A behavioral failure under a licensed transformation can therefore be a valid scientific observation rather than proof that the treatment was invalid.

---

# 16. When should behavioral invariance be required?

Behavioral invariance should be a hard G1 requirement only if the scientific claim explicitly says that the system's warranted-selection control is stable across the licensed representation class.

Examples:

```text
CLAIM A — average semantic evidence control
Under a prospectively frozen distribution of licensed representations,
semantic evidence causally controls warranted selection.

CLAIM B — representation-stable semantic evidence control
Across every representation in a prospectively frozen equivalence class,
semantic evidence controls warranted selection within a declared tolerance.
```

Claim B is stronger.

Claim A does not imply Claim B.

Therefore representation invariance is not merely a testing detail; it determines the claim ceiling.

---

# 17. A useful stochastic-intervention formulation

The attack suggests that a clean parent G1 may be formulated with two-stage assignment.

First choose the semantic evidence condition:

\[
S=s.
\]

Then independently draw a licensed representation:

\[
R\sim Q_R.
\]

where the representation policy is shared or prospectively matched across semantic conditions.

The observed raw treatment is generated by

\[
E_{\mathrm{raw}}=h(S,R).
\]

The causal object becomes:

\[
\boxed{
S
\xrightarrow{\text{randomized licensed realization }R}
C_{\mathrm{selected}}
}
\]

with success defined relative to

\[
C^*(S).
\]

This can identify semantic-class average warranted control while leaving representation heterogeneity measurable rather than confounded.

It also remains agnostic about the selector's internal channel.

The exact statistical estimand is not frozen by this document.

---

# 18. Representation heterogeneity becomes a secondary scientific object

Under the stochastic formulation, define realization-specific heterogeneity conceptually as:

\[
H_R(s)
=
\operatorname{Var}_{R\sim Q_R}[\theta_1(s,R)]
\]

or another prospectively justified measure.

A nonzero \(H_R\) does not automatically invalidate semantic G1.

It may reveal:

- interface brittleness;
- access-cost sensitivity;
- presentation dependence;
- missing background conventions;
- representational specialization.

Those properties can matter for transport and repeated correction.

But they carry additional authority rather than redefining the parent outcome retrospectively.

---

# 19. Nuisance versus meaningful intervention

The attack yields a sharper criterion.

A transformation should be treated as nuisance only when the scientific contract prospectively declares that the transformed dimension has **no authority to change the scientific treatment identity**.

If a change alters any of the following in a scientifically relevant way:

- evidence semantics;
- warrant;
- available information;
- access convention;
- resource demand outside the frozen envelope;
- modality when modality is part of the object;
- interaction opportunity;

then it is not automatically nuisance.

It may constitute a new treatment or a new interface condition.

Therefore:

\[
\boxed{
\text{representation}
\neq
\text{nuisance by default}.
}
\]

---

# 20. Relation to channel attribution

Nothing in this refined treatment structure identifies how the selector extracts the evidence.

Even after semantically controlled, representation-randomized G1 succeeds, the system may rely on:

- relational structure;
- output marginals;
- input statistics;
- symbolic rules;
- latent compression;
- interactions between channels.

Thus the preceding separation survives:

\[
\boxed{
\text{valid treatment constitution}
\rightarrow
\text{total warranted-selection effect}
\not\Rightarrow
\text{channel attribution}.
}
\]

Representation randomization helps prevent trivial treatment confounding; it does not identify the internal mechanism by itself.

---

# 21. Fourth destructive test: hidden semantic drift under paraphrase

Suppose a natural-language evidence statement is paraphrased.

A human evaluator judges the two forms equivalent.

But the paraphrase changes:

- quantifier scope;
- presupposition;
- temporal reference;
- implied certainty;
- exception handling.

Then the apparent transformation may alter the scientific evidence even though surface intent appears preserved.

If tested-model performance differs, one cannot distinguish:

1. representation sensitivity;
2. semantic drift.

Therefore natural-language paraphrase is not automatically licensed.

It needs independent semantic validation appropriate to the object.

This reinforces:

\[
\boxed{
\mathcal T_E
\text{ must be defined before behavior is observed.}
}
\]

---

# 22. Fifth destructive test: perfect invariance can be achieved trivially

A system that ignores evidence entirely may produce identical behavior under every licensed representation:

\[
P(C=c\mid e)=P(C=c\mid T(e)).
\]

It is perfectly representation invariant.

Yet warranted evidence control may be zero.

Therefore:

\[
\boxed{
\text{representation invariance}
\not\Rightarrow
G_1.
}
\]

Invariance is never a substitute for evidence-controlled warranted selection.

---

# 23. Sixth destructive test: strong G1 can coexist with representation sensitivity

Conversely, suppose each semantic evidence condition is represented under two licensed forms with a shared randomized representation policy.

The selector performs:

```text
representation r1: 95% warranted selection
representation r2: 70% warranted selection
```

while counterfactual evidence reassignment demonstrates a strong total semantic evidence effect under both forms.

Then:

- G1 semantic-class average control can be positive;
- representation heterogeneity is substantial;
- representation-stable G1 may fail.

This is not logically inconsistent.

It proves the two claims are distinct.

---

# 24. The surviving architecture

The strongest candidate architecture surviving the present attack is not merely

```text
0A -> 0B -> 0C
```

but a refined Level 0:

```text
0A-S — semantic constitution
       define evidence semantics and unique C*(S)

0A-R — realization / access constitution
       define licensed representation class,
       transformation rules, and realization policy Q

0B   — total warranted evidence control
       does intervention on semantic evidence,
       under the frozen realization policy,
       move selection toward C*(S)?

0C   — channel / mechanism attribution
       what information-processing route carries the control?
```

Conceptually:

\[
\boxed{
0A_S
\rightarrow
0A_R
\rightarrow
0B
\rightarrow
0C
}
\]

This decomposition is **not made canonical by this analysis**.

It is the strongest candidate structure surviving the attack.

---

# 25. What was refuted

The attack refutes several stronger claims.

## Refuted A

\[
\text{semantic equivalence}
\Rightarrow
\text{behavioral invariance}.
\]

False because equivalent semantics can differ in accessibility.

## Refuted B

\[
\text{all semantic-preserving transformations}
\text{ should be hard G1 invariances}.
\]

Too strong; this can turn G1 into an arbitrary representation-robustness benchmark.

## Refuted C

\[
\text{the semantic equivalence class alone fully specifies the intervention}.
\]

Incomplete; an operational realization policy or access envelope is needed.

## Refuted D

\[
\text{behavioral invariance}
\Rightarrow
\text{warranted evidence use}.
\]

False; an evidence-ignoring system can be perfectly invariant.

---

# 26. What survived

The following propositions survive in principle.

## Survived A — model-independent semantic equivalence

A local, prospectively declared semantic equivalence relation can be defined independently of tested-model behavior when the ontology supplies explicit truth conditions.

## Survived B — oracle invariance

Licensed treatment-preserving transformations must preserve the independently warranted candidate.

## Survived C — channel-agnostic total G1

A semantic evidence effect on warranted selection can be identified without identifying the internal information channel, provided representation is prospectively controlled rather than confounded with semantic treatment.

## Survived D — representation heterogeneity as separate authority

The selector may legitimately be more or less effective under different licensed realizations. Whether that heterogeneity invalidates G1 depends on the prospectively declared claim.

---

# 27. Implication for the parent G1 hypothesis

The attack strengthens the case for a mechanism-agnostic parent object, but with an important qualification.

A defensible parent object is not:

\[
\text{arbitrary raw }E\rightarrow C_{\mathrm{selected}}.
\]

It is closer to:

\[
\boxed{
\text{prospectively constituted semantic evidence}
\xrightarrow[\text{licensed realization policy}]{do}
\text{warranted selection}
}
\]

with

\[
C^*=g(S)
\]

and representation assignment controlled prospectively.

This remains broader than any specific relational mechanism.

---

# 28. Relation to CCA

CCA asks whether valid correction can govern adaptive change while preserving future correctability.

That parent property should not definitionally require the system to be indifferent to every alternate representation of the same proposition.

But it does require that scientific evidence interventions not obtain their authority from accidental presentation artifacts.

Thus CCA needs both:

```text
semantic legitimacy of the treatment
+
controlled operational realization
```

before asking whether evidence governs warranted selection.

This is consistent with the broader measurement principle:

\[
\boxed{
\text{measurement partly constitutes the scientific object.}
}
\]

The representation policy is part of that constitution when it determines which access differences are scientifically held fixed, randomized, or treated as meaningful.

---

# 29. Relation to C_improve

The provisional \(C_{\mathrm{improve}}\) hypothesis concerns the capacity to convert valid feedback into justified, validated transformation and future viability.

It should therefore be invariant to arbitrary experimental bookkeeping but need not be invariant to every change in evidence accessibility.

A system whose correction pathway works only under one highly privileged interface may have weaker transport or future correction capacity.

That is scientifically relevant later.

But the Level-0 parent object should first separate:

```text
valid semantic evidence control
from
representation robustness
from
channel mechanism
```

rather than conflating all three.

---

# 30. Candidate conclusion of the attack

The strongest conclusion supported by the present analysis is:

\[
\boxed{
\textbf{Semantic equivalence and oracle invariance can be constituted prospectively,}
}
\]

but:

\[
\boxed{
\textbf{semantic equivalence alone does not justify behavioral invariance.}
}
\]

A valid total warranted-selection object therefore requires a prospectively specified representation/access policy in addition to semantic treatment identity.

The candidate Level-0 architecture becomes:

\[
\boxed{
0A_S
\rightarrow
0A_R
\rightarrow
0B
\rightarrow
0C
}
\]

where:

```text
0A-S  semantic evidence + unique warrant
0A-R  licensed realization/access policy
0B    total warranted evidence control
0C    information-channel attribution
```

This architecture is not canonicalized by this document.

---

# 31. Remaining destructive question

The present attack leaves one especially important boundary unresolved:

> **Can a representation/access policy be specified prospectively without baking the tested system's capabilities into the measurement object?**

If the experimenter chooses the licensed representation class because a particular model can parse it, the measurement contract may become model-relative.

If the class is too broad, semantic equivalence may span radically different access burdens.

If it is too narrow, the experiment may establish only interface-specific correction.

So the next upstream attack, if pursued, should target:

\[
\boxed{
\text{model-independent constitution of the admissible access envelope}
}
\]

—not G2, not ECIM implementation, and not execution.

---

## Authority summary

```text
EMPIRICAL AUTHORITY CHANGE        NONE
RESEARCH STATE TRANSITION         NONE
G1 CANONICALIZATION               NONE
ONTOLOGY SELECTION                NONE
EVIDENCE INTERVENTION FREEZE      NONE
IMPLEMENTATION AUTHORIZATION      NONE
EXECUTION AUTHORIZATION           NONE
```

The document is an adversarial measurement analysis only.
