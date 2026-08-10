# Level-0 Attack: Is Total Causal Warranted-Evidence Control the Right Foundational Primitive for CCA?

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO IMPLEMENTATION**

This document attacks the proposed scientific role of candidate `G1` after the measurement and causal-identification work of PRs #3–#7.

The candidate object is:

> **Total causal warranted-evidence control:** prospectively constituted admissible evidence-assignment regimes causally change fixed candidate-choice probabilities in the direction specified by an independent warrant mapping.

Schematically:

\[
G_1:
\mathcal G_s
\xrightarrow{do}
C_{\mathrm{selected}},
\]

with warrant mapping

\[
C^*(s)
\]

used to orient which treatment-induced shifts count as warranted.

The attack is no longer about constructing this object.

It asks:

> **Can this object legitimately serve as the foundational Level-0 primitive for Correction-Capable Adaptation, or is it only a useful assay of one evidence-controlled selection pathway?**

This analysis does **not**:

- canonicalize `G1`;
- modify `research_state.json`;
- select an ontology;
- freeze an evidence set;
- freeze an interface contract;
- freeze a realization policy;
- freeze an estimand or threshold;
- select a model or prompt;
- construct a benchmark;
- implement ECIM;
- authorize execution;
- merge or canonicalize PRs #3–#7.

The purpose is destructive:

> **Try to construct systems or causal architectures that satisfy or violate G1 in ways that break its proposed interpretation as the first primitive of the entire CCA program.**

---

# 1. What has already been subtracted from G1

The preceding attacks have progressively ruled out several tempting substitutions.

The scientific object is not:

\[
\text{codebook construction},
\]

not:

\[
\text{relational sensitivity},
\]

not:

\[
\text{representation invariance},
\]

not:

\[
\text{access robustness},
\]

not:

\[
\text{candidate accuracy},
\]

and not:

\[
\text{mechanism attribution}.
\]

The candidate object surviving those attacks is narrower:

\[
\boxed{
\text{admissible evidence assignment}
\xrightarrow{do}
\text{candidate choice in the warranted direction}
}
\]

under a prospectively constituted treatment regime.

That is a coherent causal object in principle.

The present question is whether it occupies the right **scientific role**.

---

# 2. Two different claims must be separated

The phrase “foundational Level-0 primitive” can mean at least two different things.

## 2.1 Universal logical primitive

A universal claim would say:

> Any correction-capable adaptive system must instantiate something equivalent to G1 candidate selection.

Formally, if

\[
CCA(x)=1
\]

denotes that system \(x\) exhibits correction-capable adaptation, the universal claim would imply:

\[
CCA(x)=1
\Rightarrow
G_1(x)>0
\]

for the candidate-selection object as currently formulated.

This is a very strong claim.

## 2.2 First empirical gate in a chosen decomposition

A weaker claim would say:

> In the CCA decomposition currently being developed, G1 is the first empirically separable gate in the specific pathway from evidence to modification.

Then the structure is:

\[
G_1
\prec
G_2
\prec
\text{repeated correction}
\prec
\text{justified transformability}
\prec
\text{adaptive viability},
\]

without asserting that every possible correction-capable architecture must expose an explicit candidate-selection node.

These two roles are not equivalent.

The attack therefore asks separately:

1. Is G1 **sufficient** for any meaningful correction-capable property?
2. Is G1 **necessary** for correction-capable adaptation in general?
3. Is G1 nevertheless a valid **first gate** for the present empirical decomposition?

---

# 3. Attack 1: G1 can be positive while the system is not correctable

Construct a system with a valid evidence-controlled selection mechanism.

Let two evidence states warrant different candidates:

\[
C^*(s_1)=c_1,
\qquad
C^*(s_2)=c_2.
\]

Suppose randomized admissible evidence regimes produce:

\[
P(C=c_1\mid do(\mathcal G_{s_1}))
\gg
P(C=c_1\mid do(\mathcal G_{s_2})),
\]

and symmetrically for \(c_2\).

So:

\[
G_1>0.
\]

Now stipulate that candidate selection has no causal path to any effective system change:

\[
C_{\mathrm{selected}}
\not\rightarrow
M_{\mathrm{effective}}.
\]

The selector can identify what should change but cannot instantiate it.

Then:

\[
G_1>0
\quad\land\quad
G_2=0.
\]

The system is evidence-responsive at selection but not correction-capable in any operational modification sense.

Therefore:

\[
\boxed{
G_1>0
\not\Rightarrow
\text{effective correction}
}
\]

This is not a defect in G1 if G1 is intended as an upstream gate.

It is fatal only if G1 is interpreted as a proxy for correction-capable adaptation itself.

---

# 4. Attack 2: G1 can be positive while correction is destructive

Now allow candidate selection to instantiate a modification.

Suppose:

\[
G_1>0
\]

and the selected modification produces the intended target effect:

\[
\Delta Y_T>0.
\]

But the modification also causes catastrophic protected interference:

\[
|\Delta Y_P|\gg\epsilon_P.
\]

The system correctly selects and applies a warranted change, but destroys unrelated or still-justified structure.

Then:

\[
\boxed{
G_1>0
\land
\text{target efficacy}
\not\Rightarrow
\text{isolated correction}
}
\]

and:

\[
\boxed{
G_1>0
\not\Rightarrow
\text{preservation of legitimate structure}
}
\]

Again, this supports a gate interpretation rather than a global construct interpretation.

---

# 5. Attack 3: G1 can be positive once and then disappear

Consider a system that responds correctly to one evidence intervention but permanently loses the ability to respond to subsequent corrections.

At time \(t=0\):

\[
G_1^{(0)}>0.
\]

A warranted modification is then applied.

At time \(t=1\):

\[
G_1^{(1)}=0.
\]

The first change may even improve task capability.

Yet the transformation destroys the pathway by which later valid evidence can govern selection.

Then:

\[
\boxed{
G_1^{(0)}>0
\not\Rightarrow
\text{persistent correction capacity}
}
\]

and:

\[
\boxed{
\text{one-shot evidence control}
\neq
\text{repeated correctability}
}
\]

This directly protects the CCA mission from collapsing into a one-shot selection benchmark.

---

# 6. Attack 4: G1 and G2 can both be positive while repeated correction fails

Construct a system satisfying both one-shot gates.

Evidence causally controls warranted selection:

\[
G_1>0.
\]

Directly assigned modifications are effective and isolated:

\[
G_2>0.
\]

Suppose the first selected modification is applied successfully.

However, the modification changes the system so that the next evidence regime cannot be interpreted, or the next modification cannot be integrated without violating previously protected structure.

Thus:

\[
G_1^{(0)}>0,
\qquad
G_2^{(0)}>0,
\]

but repeated correction fails:

\[
R=0.
\]

Therefore:

\[
\boxed{
G_1>0\land G_2>0
\not\Rightarrow
\text{repeated correction}
}
\]

This is exactly why the later dynamic layers cannot be inferred from one-shot mechanism success.

---

# 7. Attack 5: high G1 can coexist with declining transformability

Suppose a system repeatedly exhibits strong evidence-controlled candidate selection.

At each step:

\[
G_1^{(t)}\approx 1.
\]

But each accepted modification narrows the future set of admissible transformations.

Let

\[
\mathcal V_t
\]

denote a future set of viable, justifiably reachable states under the eventual theory of justified transformability.

It is possible that:

\[
G_1^{(t)}\text{ remains high}
\]

while:

\[
|\mathcal V_{t+1}|<|\mathcal V_t|.
\]

The system remains locally evidence-responsive while becoming globally less transformable.

Therefore:

\[
\boxed{
G_1\text{ growth or stability}
\not\Rightarrow
\text{justified transformability growth}
}
\]

and certainly not:

\[
G_1>0
\Rightarrow
\Delta V_{\mathrm{future}}>0.
\]

This protects the downstream MAGIKARP / `C_improve` questions from authority leakage.

---

# 8. Interim verdict on sufficiency

The first five attacks jointly establish:

\[
\boxed{
G_1\text{ is not sufficient for correction-capable adaptation.}
}
\]

More specifically:

\[
G_1
\not\Rightarrow
G_2,
\]

\[
G_1
\not\Rightarrow
\text{protected preservation},
\]

\[
G_1
\not\Rightarrow
\text{persistence},
\]

\[
G_1\land G_2
\not\Rightarrow
\text{repeated correction},
\]

and:

\[
G_1
\not\Rightarrow
\text{justified transformability or viability}.
\]

This is not evidence against using G1 as an upstream gate.

It is evidence against treating it as a summary measure of the entire CCA phenomenon.

---

# 9. Attack 6: can correction-capable adaptation exist with G1 = 0?

This is the harder attack because it tests necessity.

The current G1 object explicitly contains a **candidate-selection stage**:

\[
E
\rightarrow
C_{\mathrm{selected}}.
\]

Is that stage logically necessary for every possible correction-capable architecture?

Not obviously.

Several counterarchitectures are conceivable.

---

# 10. Counterarchitecture A: direct evidence-to-modification mapping

Suppose a system has no explicit candidate-selection variable.

Instead, evidence directly parameterizes a modification operator:

\[
E
\rightarrow
M_{\mathrm{effective}}.
\]

For example, a continuous controller may update parameters according to a prospectively warranted evidence-conditioned rule without choosing among a discrete candidate set.

If the resulting modification is:

- warranted by evidence;
- causally effective;
- protected in scope;
- repeatable;
- still correctable;

then the system may exhibit a legitimate correction pathway despite lacking the current discrete candidate-selection object.

One could artificially define each realized modification as a “candidate” after the fact.

But that would risk making G1 tautological by redefining candidate selection to mean any adaptive action.

Therefore:

\[
\boxed{
\text{explicit discrete candidate selection is not obviously logically necessary}
}
\]

for correction-capable adaptation in general.

---

# 11. Counterarchitecture B: external correction authority

Suppose the adaptive system itself does not select a modification.

An external validated controller interprets evidence and imposes the warranted modification:

\[
E
\rightarrow
A_{\mathrm{external}}
\rightarrow
M.
\]

The system is constructed to accept legitimate corrections and preserve future correctability.

Depending on the scientific boundary around “system,” this may count as correction-capable adaptation of a larger coupled system even though the internal agent has:

\[
G_1^{\mathrm{internal}}=0.
\]

This exposes a boundary issue:

\[
\boxed{
G_1\text{ necessity depends on where the adaptive-system boundary is drawn.}
}
\]

That boundary is scientific, not merely implementation detail.

---

# 12. Counterarchitecture C: deterministic evidence-indexed policy

Imagine a system with a hard-coded, prospectively valid evidence-to-action mapping.

It does not “select” among candidates in a deliberative sense.

For every admissible evidence state \(s\), the update is mechanically specified:

\[
M=m^*(s).
\]

If interventions on evidence causally change the applied update in the warranted direction, then there is clearly evidence control.

Whether this satisfies G1 depends entirely on whether the term

\[
C_{\mathrm{selected}}
\]

is interpreted functionally or architecturally.

If “selection” simply means an observable decision variable before modification, the object may be general enough.

If it means a literal candidate-choice procedure, the system is a counterexample.

Thus the attack exposes an ambiguity:

\[
\boxed{
\text{functional selection}
\neq
\text{architectural candidate search}.
}
\]

The scientific object should not accidentally require the latter unless CCA means to study it specifically.

---

# 13. Counterarchitecture D: correction through constraint activation

A system may respond to evidence by activating or deactivating constraints rather than choosing a modification candidate.

For example:

\[
E
\rightarrow
\Lambda
\rightarrow
\text{allowed transition set},
\]

where \(\Lambda\) changes which future updates are permitted.

The immediate effect is not selection of a candidate but a change in authority or admissibility structure.

This may later induce a warranted modification.

Such an architecture could be central to correction-capable adaptation because it changes **which transformations have authority** rather than directly selecting one.

If the present G1 cannot represent that without artificial re-description, then G1 is not a universal primitive of correction in the strongest sense.

---

# 14. Necessity verdict

The counterarchitectures are enough to refute the strongest universal claim unless “candidate selection” is defined so abstractly that it includes any evidence-governed adaptive decision.

Therefore:

\[
\boxed{
G_1\text{ as explicit candidate selection is not yet established as logically necessary for all CCA architectures.}
}
\]

This is a scoped negative result.

It does **not** imply G1 is a bad scientific object.

It implies the program must distinguish:

```text
UNIVERSAL THEORY CLAIM
all correction-capable adaptation requires this exact node

from

EMPIRICAL PROGRAM DECOMPOSITION
this is the first isolated gate in the pathway currently being studied
```

---

# 15. Could G1 be generalized until it becomes necessary?

One response would be to broaden G1 from candidate selection to something like:

\[
\text{evidence}
\rightarrow
\text{adaptive authority / action}
\]

or:

\[
\text{valid evidence}
\rightarrow
\text{warranted adaptive decision}.
\]

That might subsume discrete selection, continuous updates, constraint activation, and externally mediated correction.

But this move carries a serious risk.

If the object is broadened too far, it may become difficult to measure independently of later modification and correction stages.

For example:

\[
E\rightarrow M
\]

could collapse selection and modification back into one causal object, undoing the separation learned from ASI-0.

The program would then lose the ability to distinguish:

\[
\text{evidence failed to govern the decision}
\]

from:

\[
\text{the decision was warranted but the modification failed}.
\]

Therefore a more universal parent primitive is not automatically superior.

A narrow G1 may have greater **diagnostic separability** even if it has less architectural universality.

This creates a real scientific tradeoff:

\[
\boxed{
\text{architectural generality}
\quad\text{vs}\quad
\text{causal decomposability}.
}
\]

The present attack does not choose between them.

---

# 16. Attack 7: is G1 merely an evidence-responsiveness assay?

Suppose a benchmark produces a strong positive G1 result.

What exactly has been established?

At most:

> Under the frozen evidence-treatment regime and selection environment, admissible evidence causally changed candidate-choice probabilities in the independently warranted direction.

That is stronger than generic responsiveness.

It excludes:

- static candidate priors;
- accidental accuracy;
- selection changes in the wrong direction;
- arbitrary treatment-byte sensitivity;
- mechanism assumptions.

So calling G1 merely an “evidence responsiveness assay” is too weak.

It is specifically an assay of **warranted causal control over an adaptive decision variable**.

This matters because CCA is centrally concerned with whether valid correction can acquire causal authority.

Thus G1 has a direct conceptual link to the program mission even though it does not measure the whole phenomenon.

The strongest scoped statement is:

\[
\boxed{
G_1\text{ measures one necessary causal ingredient of the selected CCA pathway, not CCA itself.}
}
\]

Whether it is universally necessary across all architectures remains unresolved.

---

# 17. Relation to the CCA mission

CCA asks whether adaptive systems can undergo justified change while preserving future correctability.

A minimal conceptual chain includes some point at which valid evidence acquires causal authority over what happens next.

Without any such authority transfer, correction cannot be said to govern adaptation.

The current G1 object operationalizes one clean version of that point:

\[
\text{evidence}
\rightarrow
\text{warranted selection}.
\]

This gives G1 a strong **mission relevance**.

But mission relevance is weaker than universal ontological necessity.

The attack therefore supports:

\[
\boxed{
\text{CCA requires some evidence-to-adaptive-authority pathway,}
}
\]

while leaving open whether:

\[
\boxed{
\text{that pathway must always be represented as }C_{\mathrm{selected}}.
}
\]

This is the deepest remaining role question.

---

# 18. Relation to the authority gate A0

A more abstract description of correction requires evidence to alter the authority of future hypotheses, policies, actions, or modifications.

Schematically:

\[
\Delta E_t
\rightarrow
\Delta W_{t+1}.
\]

The current G1 can be read as one operational instantiation of such an authority transfer:

\[
\Delta E
\rightarrow
\Delta P(C_{\mathrm{selected}}).
\]

with the warrant mapping determining whether the transfer is legitimate.

This suggests a possible hierarchy:

```text
abstract correction requirement
valid evidence must causally acquire appropriate adaptive authority

        ↓ one operationalization

G1 selection object
valid evidence causally changes candidate-choice probabilities
in the independently warranted direction
```

This is analytically useful because it prevents the empirical selection assay from being mistaken for the whole theory of authority transfer.

However, this document does not canonicalize that hierarchy.

---

# 19. Relation to G2

The ASI-0 lineage already established why selection and modification must remain separated.

A system may have:

\[
G_1>0
\]

while selected changes never become effective modifications.

Conversely, direct modification efficacy can be studied under:

\[
do(M=m)
\]

without conditioning on selected candidates.

Therefore the program gains diagnostic power from maintaining:

\[
\boxed{
G_1\neq G_2.
}
\]

If G1 is retained as the first empirical gate, its strongest justification is not that it equals correction.

It is that it isolates the first causal link in a decomposed correction pathway:

\[
\text{evidence authority}
\rightarrow
\text{warranted adaptive decision}
\rightarrow
\text{effective modification}.
\]

---

# 20. Relation to repeated correction

Correction-capable adaptation is fundamentally dynamic.

Even perfect one-shot G1 says nothing about whether the pathway survives transformation.

A later repeated-correction object would need to ask whether, after an accepted change,

\[
G_1^{(t+1)}
\]

remains valid under newly relevant evidence and state conditions.

Thus one possible dynamic requirement is not merely:

\[
G_1^{(0)}>0,
\]

but persistence or recoverability of the evidence-control pathway across transitions.

The exact object is not defined here.

The present attack only establishes that one-shot G1 must not be granted authority over this later property.

---

# 21. Relation to justified transformability

A system can retain high G1 while the set of safe, justified future transformations shrinks.

Therefore justified transformability must remain an independent downstream object.

G1 can contribute one local ingredient:

> future evidence can influence warranted adaptive decisions.

But transformability additionally depends on:

- modification availability;
- preservation constraints;
- state-dependent accessibility;
- reversibility or repairability;
- persistence of correction channels;
- interactions among accumulated modifications.

Thus:

\[
\boxed{
G_1\text{ is at most a component of justified transformability, not its measure.}
}
\]

---

# 22. Relation to C_improve and viability

The provisional program hypothesis `C_improve` concerns the capacity to convert valid feedback into increased future viability while preserving further correctability.

G1 addresses only the first causal acquisition of warranted control over an adaptive decision.

Even a maximally strong G1 cannot establish:

\[
\Delta V_{\mathrm{future}}>0.
\]

Nor can it establish that future correction remains possible.

Therefore:

\[
\boxed{
G_1\text{ is upstream evidence for a possible }C_{\mathrm{improve}}\text{ pathway, not evidence for }C_{\mathrm{improve}}\text{ itself.}
}
\]

This preserves the noncompensatory hierarchy.

---

# 23. A useful necessary/sufficient table

The attack supports the following provisional logical classification.

| Property | Does G1 establish it? |
|---|---|
| Evidence causally changes candidate choice in warranted direction | **Yes, by definition if validly identified** |
| Candidate accuracy | Not necessarily as a standalone rate; separate fidelity property |
| Internal reasoning mechanism | **No** |
| Effective modification | **No** |
| Protected preservation | **No** |
| Persistence | **No** |
| Repeated correction | **No** |
| Justified transformability | **No** |
| Future viability | **No** |
| General correction capacity across all architectures | **Not established** |
| First causal gate in the current selection→modification decomposition | **Plausibly yes; this is the role under attack** |

The table is not a canonical state change.

It summarizes the authority boundaries exposed by the attack.

---

# 24. What would falsify G1's proposed program role?

The strongest reason to reject G1 as the first parent gate would be if the program cannot articulate why candidate selection is scientifically prior to modification except by benchmark convenience.

For example, if every realistic future CCA experiment necessarily collapses evidence interpretation and modification into an inseparable continuous process, then the candidate-selection object may be an artifact of the toy architecture.

Another reason would be if positive G1 has no predictive or explanatory relevance to any downstream correction property even after G2 is controlled.

These are future empirical/theoretical questions.

The present analysis cannot resolve them without implementing downstream objects, which remains unauthorized.

Therefore the correct current claim is limited:

\[
\boxed{
G_1\text{ has survived as a coherent, causally separable, mission-relevant first gate for one explicit CCA pathway.}
}
\]

It has **not** yet been established as the unique universal primitive of all correction-capable adaptation.

---

# 25. What would support G1's proposed program role?

The role would be strengthened if the following conceptual requirements are accepted prospectively:

1. CCA needs an observable stage at which evidence acquires warranted causal authority over a prospective adaptive action.
2. Separating that stage from modification is scientifically valuable because selection competence and modification competence can fail independently.
3. Candidate choice is a sufficiently general operational decision variable for the first empirical program, without claiming architectural universality.
4. Later gates remain independently identified and cannot be inferred from G1.
5. Alternative correction architectures remain scientifically admissible descendants or parallel objects rather than being declared impossible by definition.

Under those conditions, G1 functions as a **program primitive in the methodological sense**:

> the earliest independently testable causal prerequisite in the chosen research decomposition.

That is weaker, and more defensible, than saying it is a universal ontological primitive.

---

# 26. Strongest negative result

The attack refutes the strongest possible interpretation:

\[
\boxed{
\text{Every correction-capable adaptive system must instantiate the current explicit candidate-selection G1 object.}
}
\]

That claim is not earned.

Direct evidence-to-modification, constraint-mediated, externally governed, or continuous update architectures provide plausible counterexamples unless “candidate selection” is generalized so far that the distinction loses content.

Therefore:

\[
\boxed{
\text{G1 candidate selection is not established as a universal necessary condition for CCA.}
}
\]

---

# 27. Strongest positive result

The attack also rejects the opposite dismissal that G1 is merely generic responsiveness.

Because G1 requires:

- prospectively valid evidence treatments;
- independent warrant semantics;
- causal reassignment;
- fixed candidate-choice coordinates;
- movement in the warranted direction;
- no mechanism assumptions;

it measures a specific and important property:

\[
\boxed{
\text{valid evidence acquires causal control over a prospective adaptive decision in a warranted direction.}
}
\]

That property is directly relevant to correction-capable adaptation.

It is therefore more than a generic responsiveness assay.

---

# 28. Candidate role surviving the attack

The strongest role for G1 that survives is:

> **G1 is the earliest independently testable causal gate in the current CCA evidence→selection→modification decomposition, measuring whether admissible evidence acquires warranted causal control over a prospective adaptive decision.**

This role has four explicit limits:

1. G1 is **not CCA itself**.
2. G1 is **not sufficient** for effective, isolated, persistent, repeated, or viable correction.
3. The current candidate-selection form of G1 is **not established as universally necessary** for every possible correction architecture.
4. G1's empirical success grants authority only to proceed to separately defined downstream gates under a new prospective contract.

This is a candidate conclusion only.

It is **not canonicalized** by this PR.

---

# 29. Implication for the maturity ladder

If this candidate role were later accepted, the maturity ladder would become conceptually cleaner.

Level 0 would no longer mean “all of correction capacity.”

It would mean:

> **Can a valid evidence treatment be constituted and shown to acquire warranted causal control over a prospective adaptive decision?**

Then later levels would remain noncompensatory:

```text
Level 0  warranted evidence control
    ↓
Level 1  effective / isolated modification
    ↓
Level 2  evidence-governed modification pathway
    ↓
Level 3  repeated correction
    ↓
Level 4  justified transformability
    ↓
Level 5  adaptive viability / capability
    ↓
ASI      extreme-system stress test
```

The exact numbering is not changed here.

`research_state.json` remains authoritative and unchanged.

---

# 30. Should alternative correction pathways invalidate the current program?

No.

A scientific program can choose a causally decomposable pathway without claiming it exhausts all possible architectures.

For example, CCA may study:

\[
E
\rightarrow
C_{\mathrm{selected}}
\rightarrow
M
\rightarrow
(Y_T,Y_P)
\]

because this pathway supports clean interventions and failure localization.

If later evidence shows another architecture achieves correction-capable adaptation without an explicit selection node, that would motivate a new scientific object or generalization.

It would not retroactively invalidate a correctly scoped G1 result.

This follows the program's own revision discipline:

\[
\boxed{
\text{preserve valid local authority; generalize only when independently earned.}
}
\]

---

# 31. Central classification

The exact adversarial question was:

> Is G1 a valid Level-0 primitive for correction-capable adaptation, or merely a useful assay of evidence responsiveness?

The attack yields a three-part answer.

## 31.1 Not a complete CCA primitive

G1 is neither sufficient for CCA nor established as universally necessary across all conceivable correction architectures.

Therefore:

\[
\boxed{
G_1\neq\text{correction-capable adaptation}.
}
\]

## 31.2 More than generic responsiveness

G1 identifies warranted causal control over an adaptive decision, not merely sensitivity or accuracy.

Therefore:

\[
\boxed{
G_1>\text{generic evidence responsiveness assay}
}
\]

in scientific specificity.

## 31.3 Viable first gate in the chosen decomposition

The strongest surviving interpretation is:

\[
\boxed{
G_1
=\text{first independently testable causal gate in the current evidence→selection→modification pathway.}
}
\]

This is a **methodological/program decomposition claim**, not yet a universal theory claim.

---

# 32. Remaining decision after this attack

The destructive work now leaves a precise scientific-object decision.

CCA must decide whether it wants to adopt the following scoped commitment:

> **The first empirical pathway studied by CCA will operationalize justified correction as admissible evidence acquiring causal control over a prospectively separable adaptive decision, represented initially as warranted candidate selection.**

If accepted later, this would justify treating the current G1 as the parent empirical gate **without claiming that every possible correction-capable system must literally contain a candidate-selection node**.

A stronger universal claim would require additional theoretical work.

A broader evidence→authority primitive could also be investigated, but broadening must not erase the selection/modification separation learned from ASI-0.

No choice is made here.

---

# 33. What this attack does not authorize

This analysis does not authorize:

- canonicalizing G1;
- changing the Level-0 lifecycle state;
- changing `research_state.json`;
- choosing the candidate ontology;
- freezing semantic evidence;
- freezing the interface contract;
- freezing the realization policy;
- choosing a causal estimand or threshold;
- selecting a model;
- writing prompts;
- constructing the benchmark;
- implementing ECIM;
- executing G1;
- inferring correction capacity, transformability, viability, capability, AGI, RSI, or ASI.

The state remains `ADVERSARIAL_REVIEW`.

---

# 34. Final compression

The attack supports the following distinction:

\[
\boxed{
\textbf{G1 is not the phenomenon. It is a candidate first causal prerequisite in one explicit decomposition of the phenomenon.}
}
\]

and:

\[
\boxed{
\textbf{G1 success would establish warranted evidence control over selection, not correction-capable adaptation.}
}
\]

The strongest surviving lineage is therefore:

```text
CCA theory
valid evidence must be able to acquire appropriate adaptive authority
        ↓
empirical pathway under study
G1: warranted causal control over a prospective adaptive decision
        ↓
G2: independently identified modification efficacy / isolation
        ↓
repeated correction
        ↓
justified transformability
        ↓
adaptive viability
```

Whether CCA should now adopt that scoped empirical role for G1 is the next scientific-object decision.

No implementation follows from this document.
