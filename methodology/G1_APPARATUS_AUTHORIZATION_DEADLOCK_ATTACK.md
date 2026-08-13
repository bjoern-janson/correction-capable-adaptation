# G1 Apparatus-Authorization Deadlock Attack

## Status and boundary

**METHODOLOGICAL AUTHORIZATION-DEPENDENCY ATTACK — NO LIFECYCLE DEFECT ESTABLISHED — NO GOVERNANCE CHANGE — PR #21 REMAINS BLOCKED AT ITS CURRENT STATE — NO APPARATUS IMPLEMENTATION OR EXECUTION AUTHORIZED**

This artifact attacks one question only:

\[
\boxed{
\text{Can the current authority graph legally generate the evidence required to validate }
S_{\mathrm{specified}}\rightarrow S_{\mathrm{realized}}
\text{ without presupposing that validation?}
}
\]

It reconstructs the current graph rather than treating repeated use of the words
"measurement," "validation," or "implementation" as proof of a cycle.

The adjudication is:

```text
AUTHORIZATION DEADLOCK:
  NOT_ESTABLISHED

MEASUREMENT-VALIDITY CYCLE:
  NOT ESTABLISHED

SHALLOWEST FAILURE LOCUS:
  NONE IN THE CANONICAL LIFECYCLE;
  THE ALLEGED CYCLE IMPORTS AN UNSUPPORTED
  APPARATUS-FIDELITY → MEASUREMENT_VALID EDGE

NONBLOCKING WORDING AMBIGUITY:
  THE SCOPE AND GRANT PROCEDURE OF implementation_authorized
  ARE NOT EXHAUSTIVELY ENUMERATED

GOVERNANCE REPAIR:
  NONE ADOPTED

EMPIRICAL AUTHORITY MOVEMENT:
  0
```

The current snapshot grants no apparatus permission. The absence of current permission is
not evidence that the ordinary lifecycle can never grant it.

## A. Observed residual

The candidate lineage currently records:

```text
X → R
  candidate object survived declared constitution attacks

R → S_specified
  candidate exposure specification survived declared integrity attacks

S_specified → S_realized
  prospective fidelity-validation design survived
  actual realized fidelity BLOCKED_BY_AUTHORITY

S_realized → D
  unopened
```

PR #21 attempted no apparatus execution. It stopped because current G1 state is
empirically untested, contract-unfrozen, and implementation-unauthorized. Its required
future evidence includes:

- a concrete transformation path;
- complete system-facing boundary capture;
- renderer and serialization inspection;
- assignment-generator validation;
- reset and isolation validation;
- evaluator-separation validation.

That blockage is an observed current-state fact. It is not by itself a lifecycle defect.

## B. Canonical source order and controlling definitions

This attack gives priority to the machine-readable state and canonical lifecycle rules:

1. [`../research_state.json`](../research_state.json) records current authority and the
   conjunctive implementation gate.
2. [`RESEARCH_STATE_MACHINE.md`](RESEARCH_STATE_MACHINE.md) defines lifecycle states.
3. [`../contracts/README.md`](../contracts/README.md) and
   [`../contracts/EXPERIMENT_RECORD_TEMPLATE.md`](../contracts/EXPERIMENT_RECORD_TEMPLATE.md)
   define prospective contract and implementation-validity obligations.
4. [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md)
   governs apparatus-mediated causal composition.
5. [`../CARS.md`](../CARS.md) and
   [`RESEARCH_RETURNABILITY.md`](RESEARCH_RETURNABILITY.md) govern localization,
   minimal revision, provenance, and stopping.

The controlling lifecycle definition is:

> `MEASUREMENT_VALID` means that the intended object can, in principle, be distinguished
> from relevant alternatives under the declared measurement structure.

The state machine also says that this status does not imply that adjacent transformations
are valid. Therefore actual realized-apparatus fidelity is not definitionally required to
earn `MEASUREMENT_VALID`.

The separate composition rule remains strict:

> A causal claim may not cross a separable apparatus transformation unless that
> transformation is independently identified, prospectively specified and
> validated/verified as an apparatus guarantee, or excluded from the claim.

These rules concern different authority questions. In-principle identification of an
object does not validate an actual apparatus, while apparatus failure does not
retroactively make the object conceptually unidentified.

## C. Current canonical graph

The lifecycle is:

```text
PROPOSED
   ↓  candidate object; conceptual decomposition
ADVERSARIAL_REVIEW
   ↓  in-principle discrimination from relevant alternatives
MEASUREMENT_VALID
   ↓  prospective empirical identity and implementation-validity criteria frozen
CONTRACT_FROZEN
   ↓  explicit authorization under the frozen rule
AUTHORIZED
   ↓  outcome-bearing execution or explicit implementation failure
EXECUTED
   ↓  frozen analysis
ANALYZED
   ↓  historical closure
CLOSED
```

The machine-readable implementation gate is a conjunction alongside that lifecycle:

```text
EMPIRICAL IMPLEMENTATION PERMITTED ONLY IF:

  measurement_state = MEASUREMENT_VALID or later
  contract_state = CONTRACT_FROZEN or later
  execution_state = AUTHORIZED
  implementation_authorized = true
```

`implementation_authorized` is not listed as a lifecycle state. It is a separate,
object-specific permission conjunct. No canonical source defines it as an automatic
consequence of `AUTHORIZED`, specifies a universal grant procedure, or exhaustively
enumerates every executable activity it covers. None makes successful apparatus fidelity
a prerequisite for changing the bit.

### C.1 Transition audit

| Source | Target | Required evidence or authority | Evidence type | Executable work required? | Currently authorized? | Can evidence exist before target? |
|---|---|---|---|---:|---:|---:|
| `PROPOSED` | `ADVERSARIAL_REVIEW` | Candidate object, countermodels, competing formulations, non-model feasibility analysis | Conceptual / documentary | No | Yes | Yes |
| `ADVERSARIAL_REVIEW` | `MEASUREMENT_VALID` | Measurement structure that distinguishes the intended object in principle under declared transformations and nuisance channels | Conceptual / documentary; formal or static mechanical support may contribute | Not required by the canonical definition | The work is allowed; G1 has not earned the transition | Yes |
| `MEASUREMENT_VALID` | `CONTRACT_FROZEN` | Frozen proposition, claimed path, transformation statuses, intervention, warrant, outcomes, nulls, estimands, inference, randomization, authorization rule, and implementation-validity criteria | Documentary / prospective | No result from the target relation is required | No for current G1 | Yes |
| `CONTRACT_FROZEN` | `AUTHORIZED` | Frozen empirical identity, resolved prerequisites, and an explicit authorization decision | Documentary / governance | No outcome-bearing work required | No | Yes |
| `AUTHORIZED` | `EXECUTED` | Outcome-bearing execution or an explicit implementation failure | Executable / empirical; may be system-response-dependent | Yes | No | No |
| `implementation_authorized: false` | `true` | Explicit object-specific implementation permission; no universal grant rule is specified | Permission / governance | No scientific outcome is required by any stated rule | No | No rule conditions a later explicit grant on successful fidelity; the grant procedure is otherwise underspecified |

### C.2 Apparatus-guarantee path

The composition rule separately requires:

```text
prospective apparatus specification
  + independent validation or mechanical verification over the claimed domain
  → validated apparatus guarantee
  → authority to cross that transformation in the scoped causal claim
```

The evidence for the middle step is ordinarily mechanical and executable. It cannot be
validated by \(D\), expected G1 behavior, or a favorable causal estimate. Platform-specific
diagnostic interaction, if required to test reset, isolation, or final-boundary coverage,
remains subject to the frozen fidelity contract and explicit authorization. The already-open
PR #21 candidate fidelity object can traverse the ordinary lifecycle and generate that
evidence before a later G1 claim treats the relation as a validated apparatus guarantee.

## D. Scientific-object constitution, apparatus validation, and execution

The canonical sources already distinguish the three activities scientifically:

### D.1 Scientific-object constitution

`PROPOSED`, `ADVERSARIAL_REVIEW`, and the in-principle definition of
`MEASUREMENT_VALID` govern the proposition and measurement structure. This work can be
nonexecuting.

### D.2 Apparatus / measurement-channel validation

The causal-composition principle requires independent validation or mechanical
verification of any apparatus relation crossed by a claim. Implementation-validity
criteria must be frozen prospectively, and their failure must remain an implementation
failure rather than a scientific zero.

### D.3 Experimental execution

`AUTHORIZED` permits execution of the frozen object. `EXECUTED` records either
outcome-bearing execution or explicit implementation failure. Tested-system response,
\(D\), and causal estimation belong here, not to object constitution.

Thus the scientific distinctions are already present:

\[
A\neq B\neq C.
\]

The lifecycle does not give (B) a separate named state, and the permission bit's scope is
not exhaustively enumerated. That wording gap does not make (B) unreachable: a fidelity
object can be constituted, frozen, and expressly authorized without treating its not-yet
observed result as a prerequisite.

## E. Deadlock test

### E.1 The proposed measurement-validity cycle

A proof of the proposed cycle would require all three edges:

```text
To reach MEASUREMENT_VALID:
  completed realized-apparatus evidence E_B is required.

To generate E_B:
  executable apparatus action A is required.

Current policy:
  A is permitted only after MEASUREMENT_VALID.
```

The first edge is contradicted by the canonical in-principle definition of
`MEASUREMENT_VALID`. The state machine expressly withholds validity for adjacent
transformations at that state.

Therefore:

```text
MEASUREMENT_VALID → A → E_B → MEASUREMENT_VALID

IS NOT A CANONICALLY ESTABLISHED CYCLE.
```

### E.2 The strongest failed contract-status attack

A later G1 contract may cross
\(S_{\mathrm{specified}}\rightarrow S_{\mathrm{realized}}\) only after that
relation carries independently warranted apparatus status. The contract vocabulary names
`VALIDATED_APPARATUS_GUARANTEE`, not a convenient promise to validate later.

That requirement still does not create a cycle. PR #21 has already separated fidelity as
its own candidate scientific object. The already-open PR #21 candidate fidelity object
can traverse its own ordinary lifecycle:

```text
fidelity question in ADVERSARIAL_REVIEW
→ in-principle fidelity measurement object reaches MEASUREMENT_VALID
→ concrete apparatus identity, validation procedure, and failure criteria freeze
→ explicit AUTHORIZED state and implementation_authorized = true
→ apparatus is instantiated and mechanically tested
→ fidelity succeeds or an implementation failure is recorded
```

Only a successful fidelity result may later supply
`VALIDATED_APPARATUS_GUARANTEE` to a G1 contract that crosses the relation. The fidelity
result is the target of that candidate object, not an upstream prerequisite that must be
assumed before that object can execute.

The repository does not exhaustively define which pre-authorization executable acts fall
inside `implementation_authorized`, or the universal procedure for changing that bit.
Those wording gaps are nonblocking here because the legal path places apparatus work
after the complete ordinary implementation gate. No early exception is needed.

## F. Competing hypotheses

### H1 — no deadlock

**SUPPORTED.** The specific measurement-validity cycle fails. The legal path is:

```text
PR #21 FIDELITY OBJECT:
  finish nonexecutive fidelity-measurement constitution
  → MEASUREMENT_VALID
  → FIDELITY CONTRACT_FROZEN
  → AUTHORIZED + implementation_authorized = true
  → APPARATUS VALIDATION
  → FIDELITY RESULT OR IMPLEMENTATION FAILURE

ONLY AFTER A SUCCESSFUL FIDELITY RESULT:
  later G1 contract may record VALIDATED_APPARATUS_GUARANTEE
  → separate G1 authorization
  → tested-system / D-bearing execution
```

The scientific burden before `MEASUREMENT_VALID` is the complete in-principle
measurement constitution and discrimination argument. This artifact does not define or
complete that burden for G1.

The apparatus-validation step occurs only after explicit authorization and the permission
bit is true. No canonical rule makes successful fidelity a prerequisite for either
earlier state.

### H2 — genuine dependency cycle

**REFUTED FOR THE CLAIMED GRAPH.** No canonical clause requires realized-apparatus
evidence to earn `MEASUREMENT_VALID`, and no clause makes successful fidelity a
prerequisite for granting implementation authority to the already-open PR #21 candidate
fidelity object.

An inferred-convenience edge has no authority to establish a lifecycle defect.

### H3 — terminological conflation

**PARTIALLY SUPPORTED BUT NONBLOCKING.** The repository distinguishes apparatus validity
from tested-system execution scientifically, while the permission bit lacks an exhaustive
activity list and universal grant procedure. But the ordinary post-authorization path
works under the broadest reading of "implementation." The wording gap therefore does not
establish unreachability or justify a new lifecycle state.

## G. Shallowest sufficient failure locus and repair adjudication

```text
SHALLOWEST FAILURE LOCUS:
  NONE IN THE CANONICAL LIFECYCLE;
  THE ALLEGED CYCLE IMPORTS AN UNSUPPORTED EDGE
```

The nonblocking wording ambiguity does not reach a state-transition dependency,
implementation-policy overreach, or lifecycle-state defect. Escalation would violate the
research-returnability stopping discipline.

No governance repair is adopted here because a genuine deadlock has not been
established. In particular, this artifact does not:

- add a lifecycle state;
- create an apparatus-validation permission;
- change `implementation_authorized`;
- define how or when that bit changes;
- authorize an executable fixture, harness, generator, renderer, or randomizer;
- mark any transformation `VALIDATED_APPARATUS_GUARANTEE`;
- change `MEASUREMENT_VALID` or contract state.

No clarification is required to make the evidence reachable through the ordinary
post-authorization path. A future editorial change could enumerate the bit's scope or
grant procedure, but this attack supplies no scientific necessity or reopening authority
for that change.

## H. Countermodels against unsafe repair

Although no repair is adopted, each tempting broad permission fails the authority
ceiling.

| Proposed loosening | Countermodel | Result |
|---|---|---|
| Permit any work labeled "validation" | A harness invokes the tested system while calling the response a channel check | Early model execution and outcome leakage |
| Permit payload generation before the scientific object is fixed | Generator convenience chooses the treatment ontology, nuisance class, or warrant | Benchmark-defined measurement |
| Permit apparatus revision after response observation | Renderer or filter is tuned until \(D\) looks favorable | Outcome-dependent apparatus modification |
| Treat mechanical pass as `MEASUREMENT_VALID` | A faithful implementation of a malformed object is promoted | Permission/validity collapse |
| Treat apparatus pass as contract freeze | Unfrozen estimand, inference, or scope is silently supplied by code | Contract bypass |
| Permit response parsing during apparatus validation | Arm-relative parsing can manufacture the target coordinate | Premature \(S_{\mathrm{realized}}\rightarrow D\) opening |
| Let a failed validation be repaired in place without provenance | Failing transformations disappear from the scientific record | Post-hoc implementation rescue |
| Accept a harness-local reset test | Provider or model persistence remains outside the observed reset boundary | Fidelity remains `UNKNOWN` or fails |
| Validate evaluator separation only at the visible client payload | Shared hidden platform state can still reach the final boundary | Partial-boundary evidence cannot pass complete fidelity |
| Call tested-system invocation a "reset probe" | Apparatus validation silently becomes early subject execution | Authorization boundary violated |
| Validate renderer and randomizer while omitting later platform transformations | A partial chain is generalized to the complete exposure path | Fidelity remains `UNKNOWN` or fails |

Any optional future clarification would have to remain operationally enforceable at a boundary
that excludes tested-system invocation, scientific outcome collection, effect estimation,
and code-selected scientific semantics. This statement is a test for a future proposal,
not a permission granted by this artifact.

## I. Authority gained

The maximum conclusion is:

> The current lifecycle admits a noncircular path: advance the already-open PR #21
> candidate fidelity object through in-principle measurement validity, freeze its
> apparatus identity and validation/failure criteria, grant explicit implementation
> authority, and then generate the mechanical evidence. PR #21 is blocked because those
> prerequisite states are unearned, not because the evidence is unreachable.

The implementation bit's unenumerated wording remains a nonblocking documentation
ambiguity. It does not warrant governance change.

## J. Authority not gained

This artifact supplies:

```text
no apparatus-validation permission
no executable apparatus
no realized exposure fidelity result
no MEASUREMENT_VALID transition
no frozen contract
no implementation authorization
no tested system or model
no D
no S_realized→D result
no causal estimand or effect threshold
no empirical G1 result
no execution
no G2
no PMC
no JT
no adaptive viability
no AGI or ASI authority
```

## Provenance and preserved authority

The exact candidate lineage is:

```text
0ffdf60 / canonical main
    ↓
d9639d3 / PR #19   X→R candidate
    ↓
f62944c / PR #20   R→S_specified candidate
    ↓
1216119 / PR #21   S_specified→S_realized validation design;
                     actual fidelity BLOCKED_BY_AUTHORITY
    ↓
this artifact          authorization-dependency attack only
```

Immediate candidate ancestors:

- [`../measurement/G1_REALIZED_EXPOSURE_FIDELITY_ATTACK.md`](../measurement/G1_REALIZED_EXPOSURE_FIDELITY_ATTACK.md);
- [`../measurement/G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md`](../measurement/G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md);
- [`../measurement/G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md`](../measurement/G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md).

Canonical and governing sources:

- [`../research_state.json`](../research_state.json);
- [`../RESEARCH_STATE.md`](../RESEARCH_STATE.md);
- [`RESEARCH_STATE_MACHINE.md`](RESEARCH_STATE_MACHINE.md);
- [`RESEARCH_RETURNABILITY.md`](RESEARCH_RETURNABILITY.md);
- [`../contracts/README.md`](../contracts/README.md);
- [`../contracts/EXPERIMENT_RECORD_TEMPLATE.md`](../contracts/EXPERIMENT_RECORD_TEMPLATE.md);
- [`../CARS.md`](../CARS.md);
- [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md);
- [`../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md`](../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md).

Canonical `main`, every state file, both evidence ledgers, all decision records, every
contract and experiment, and PRs #19–#21 remain unchanged.

## Terminal report and stopping rule

```text
AUTHORIZATION DEADLOCK:
  NOT_ESTABLISHED

SHALLOWEST FAILURE LOCUS:
  NONE IN THE CANONICAL LIFECYCLE;
  THE PROPOSED CYCLE DEPENDS ON AN UNSUPPORTED
  APPARATUS-FIDELITY → MEASUREMENT_VALID EDGE

CURRENT GRAPH:
  PR #21 FIDELITY OBJECT:
    ADVERSARIAL_REVIEW
    → MEASUREMENT_VALID
    → FIDELITY CONTRACT_FROZEN
    → AUTHORIZED + implementation_authorized = true
    → APPARATUS VALIDATION
    → FIDELITY RESULT OR IMPLEMENTATION FAILURE

  ONLY AFTER A SUCCESSFUL FIDELITY RESULT:
    LATER G1 CONTRACT MAY RECORD VALIDATED_APPARATUS_GUARANTEE
    → SEPARATE G1 AUTHORIZATION
    → TESTED-SYSTEM / D-BEARING EXECUTION

REQUIRED APPARATUS-VALIDATION EVIDENCE:
  CONCRETE TRANSFORMATION INSPECTION, COMPLETE-BOUNDARY CAPTURE,
  RANDOMIZER VALIDATION, RESET / ISOLATION VALIDATION,
  AND EVALUATOR-SEPARATION VALIDATION;
  MECHANICAL / EXECUTABLE;
  INDEPENDENT OF G1 D AND BEHAVIORAL SUCCESS.
  PLATFORM-SPECIFIC DIAGNOSTIC INTERACTION, IF REQUIRED,
  REMAINS SUBJECT TO THE FROZEN FIDELITY CONTRACT
  AND EXPLICIT AUTHORIZATION

CAN CURRENT RULES GENERATE THAT EVIDENCE?
  YES AFTER ORDINARY LIFECYCLE AUTHORIZATION;
  NO UNDER THE CURRENT SNAPSHOT

MINIMAL REPAIR:
  NONE

WHAT THE REPAIR WOULD AUTHORIZE:
  NOTHING;
  NO REPAIR IS WARRANTED

WHAT REMAINS FORBIDDEN:
  APPARATUS IMPLEMENTATION UNDER CURRENT G1 STATE,
  TESTED-SYSTEM INVOCATION, D COLLECTION, EFFECT ESTIMATION,
  CONTRACT BYPASS, OUTCOME-DEPENDENT REPAIR, AND
  SCIENTIFIC-OBJECT SELECTION BY CODE

UPSTREAM X→R:
  PRESERVED

UPSTREAM R→S_SPECIFIED:
  PRESERVED

PR #21 FIDELITY OBJECT:
  PRESERVED

REALIZED EXPOSURE FIDELITY:
  STILL UNESTABLISHED

MEASUREMENT_VALID:
  UNCHANGED UNLESS SEPARATELY WARRANTED

EMPIRICAL AUTHORITY MOVEMENT:
  0

CANONICAL MAIN:
  UNCHANGED

PR #19:
  DRAFT / UNMERGED

PR #20:
  DRAFT / UNMERGED

PR #21:
  DRAFT / UNMERGED
```

The specific measurement-validity cycle has no surviving evidential edge. The current
state remains blocked, while the ordinary future path remains reachable without an early
permission exception:

\[
\boxed{
\text{required evidence is reachable after ordinary authorization}
\Rightarrow
r=0\Rightarrow\text{stop without governance change}
}
\]

Do not implement the apparatus. Do not open
\(S_{\mathrm{realized}}\rightarrow D\). Do not merge any draft PR.
