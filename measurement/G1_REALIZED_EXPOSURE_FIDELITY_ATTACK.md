# G1 Realized Exposure Fidelity Attack

## Status and stopping boundary

**NONEXECUTABLE CANDIDATE VALIDATION SPECIFICATION — ADVERSARIAL REVIEW — \(S_{\mathrm{specified}}\rightarrow S_{\mathrm{realized}}\) VALIDATION DESIGN ONLY — REALIZED EXPOSURE FIDELITY BLOCKED BY AUTHORITY — UPSTREAM OBJECTS PRESERVED — \(S_{\mathrm{realized}}\rightarrow D\) UNOPENED — NO G1 EMPIRICAL RESULT — CONTRACT UNFROZEN — NO IMPLEMENTATION OR EXECUTION AUTHORIZED**

This artifact attacks one boundary only:

\[
\boxed{
S_{\mathrm{specified}}
\longrightarrow
S_{\mathrm{realized}}
}
\]

The protected lineage is:

```text
X → R
  candidate evidence object
  SURVIVED declared constitution attacks

R → S_specified
  prospective exposure specification
  SURVIVED declared integrity attacks

S_specified → S_realized
  actual realization / apparatus fidelity
  BLOCKED BY CURRENT IMPLEMENTATION AUTHORITY

S_realized → D
  causal response
  NOT OPEN
```

The distinction governing this pass is:

\[
\text{prospectively valid exposure specification}
\neq
\text{validated realization}
\neq
\text{positive system response}.
\]

No concrete renderer, generator, platform, API, harness, model, or response interface is selected. No payload is executed, no decision is collected, and no causal effect is estimated.

The local design adjudication is:

```text
CANDIDATE REALIZATION-VALIDATION SPECIFICATION:
  SURVIVED DECLARED DESIGN ATTACKS

REALIZED EXPOSURE FIDELITY:
  BLOCKED_BY_AUTHORITY

LIFECYCLE STATE:
  ADVERSARIAL_REVIEW

MEASUREMENT_VALID:
  NO
```

The first line applies only to the nonexecuting validation specification. It is not a fidelity result for an apparatus.

## A. Boundary

The scientific question is:

\[
\boxed{
\text{Can a future authorized realization establish that the exact specified}
\text{ exposure reached the complete system-facing boundary unchanged?}
}
\]

The target is transformation fidelity. It is not whether a system interprets equality, follows the warrant, chooses \(\alpha\) or \(\beta\), or changes any adaptive decision.

The following edge remains outside scope:

\[
\boxed{S_{\mathrm{realized}}\rightarrow D\text{ is not opened}.}
\]

Correct behavior could not validate a contaminated realization. Incorrect behavior could not falsify a faithful realization.

## B. Authority gate

The current machine-readable state in [`../research_state.json`](../research_state.json) records:

```text
G1 empirical status:       UNTESTED
G1 contract state:         UNFROZEN
implementation_authorized: false
```

The implementation gate in [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md) requires all of:

```text
measurement_state = MEASUREMENT_VALID or later
contract_state    = CONTRACT_FROZEN or later
execution_state   = AUTHORIZED
implementation_authorized = true
```

The contract discipline in [`../contracts/README.md`](../contracts/README.md) forbids code or apparatus convenience from silently deciding an unfrozen scientific object.

Those conditions are not met. Therefore:

```text
EXECUTABLE SCIENTIFIC IMPLEMENTATION:
  BLOCKED BY CURRENT AUTHORITY
```

This artifact does not change the gate, promote lifecycle state, freeze a contract, or infer authorization from the existence of a plausible design. Permitted work ends at a static prospective validation specification.

## C. Realization architecture

### C.1 Current architecture status

```text
CONCRETE REALIZATION PATH:
  NOT SELECTED

ACTUAL S_realized:
  DOES NOT EXIST AS AN AUTHORIZED SCIENTIFIC RECORD

REASON:
  IMPLEMENTATION AND EXECUTION ARE NOT AUTHORIZED
```

Inventing generic generator, template, or platform nodes would create another specification, not validate reality. This artifact therefore asserts no intermediate component.

### C.2 Required future transformation record

If authority is independently granted later, a successor must enumerate only the components that actually exist between \(S_{\mathrm{specified}}\) and the final accessible boundary. For every separable transformation, it must record:

| Required field | Prospective meaning |
|---|---|
| Component identity and revision | The exact real component that performs the transformation |
| Input | The complete object received by that component |
| Output | The complete object emitted by that component |
| Transformation | The actual mapping, not a functional nickname |
| Fields added | Every content, schema, role, metadata, routing, or envelope field introduced |
| Fields removed | Every field discarded, hidden, truncated, or normalized away |
| Fields reordered | Every order change at both semantic and serialized levels |
| Hidden state consulted | Randomness, cache, environment, scheduler, history, configuration, or external state |
| System-accessible side effects | Any timing, routing, tool, file, retrieval, permission, or context consequence |
| Validation evidence | Independent or mechanical evidence that the arrow preserves the claimed object |

The actual chain must terminate at the last transformation before the complete system-accessible pre-decision state. Capturing an earlier client request is insufficient if a later platform transformation can add or alter accessible information.

## D. Complete system-facing boundary

### D.1 Classification rule

Every actual field and channel must be classified prospectively as exactly one of:

```text
SYSTEM_ACCESSIBLE
SYSTEM_INACCESSIBLE
UNKNOWN
```

`UNKNOWN` is not evidence of inaccessibility. Any target-relevant unknown channel prevents an actual fidelity pass.

### D.2 Required boundary inventory

A future authorized successor must inventory at least:

| Boundary element | Required classification | Current status |
|---|---|---|
| Intended labeled register observations | `SYSTEM_ACCESSIBLE` | Specified; not realized |
| Fixed scientific task and candidate semantics | `SYSTEM_ACCESSIBLE` | Specified; not realized |
| Message roles, names, and ordering | Explicitly classified | No platform selected |
| Human-readable content, prefix, and suffix | Explicitly classified | No renderer selected |
| Field names, object schema, encoding, punctuation, and whitespace | Explicitly classified | No serializer selected |
| Candidate presentation and action availability | `SYSTEM_ACCESSIBLE` and arm-independent if present | No interface selected |
| System, developer, user, or equivalent scaffolding | Explicitly classified | No platform selected |
| Tools, schemas, permissions, attachments, and retrieval context | Explicitly classified | No tool envelope selected |
| Source identity, paths, filenames, and object provenance | Explicitly classified | No source selected |
| Case, trial, request, conversation, batch, and tool-call identifiers | Explicitly classified | No apparatus selected |
| Timestamp, latency, schedule, seed, and randomization artifacts | Explicitly classified | No apparatus selected |
| Conversation, session, cache, file, environment, and prior-task state | Explicitly classified | No isolation mechanism selected |
| Routing, hidden prefix, provider context, and undocumented channels | `SYSTEM_INACCESSIBLE` with evidence, or `UNKNOWN` | Unknown for every unselected platform |
| Evaluator arm, expected direction, audit identity, and scoring state | `SYSTEM_INACCESSIBLE` except through licensed evidence semantics | No evaluator path selected |

The current adjudication is therefore:

```text
BOUNDARY COVERAGE:
  NOT ESTABLISHED FOR ANY ACTUAL APPARATUS
```

This is an authority-and-instantiation residual, not evidence that a particular platform is contaminated.

## E. Fidelity invariants

A later authorized realization may pass only if all of the following hold over all four states and both arms.

### E.1 Register-state fidelity

There must be an independently inspectable decoder satisfying:

\[
\delta(S_{\mathrm{realized}})=x
\]

for \(x\in\{00,01,10,11\}\), with the persistent meanings of \(s_1\), \(s_2\), \(\alpha\), \(\beta\), and \(\bot\) preserved. No register may be swapped, omitted, duplicated, truncated, or reinterpreted.

### E.2 Controlled difference set

After accounting for the prospectively licensed encoding of the two register values, every other system-accessible coordinate must be invariant across arms and states. A full structural diff must trace each realized difference to the licensed value fields through the recorded transformation chain.

Literal byte identity across all states is neither required nor sufficient. Lawful value encoding changes bytes; an identical visible string can coexist with contaminated hidden fields.

### E.3 Envelope fidelity

Wrapper, roles, names, schema, order law, candidate presentation, source, tools, permissions, and scaffolding must either be identical or differ only through a prospectively licensed transformation that does not introduce an independent direction path or alter the scientific object.

### E.4 Pre-treatment closure

For matched worlds that differ only in the forthcoming randomized arm:

\[
S_{\mathrm{pre}}(W_\alpha)
=
S_{\mathrm{pre}}(W_\beta)
\]

with respect to every target-relevant accessible distinction. Current arm, seed, schedule, request identity, routing, and evaluator state must not cross before the intended evidence.

### E.5 Complete-boundary fidelity

Validation must capture or otherwise independently establish the final accessible object, not merely the human-readable prompt or a pre-platform request. If the last accessible transformation cannot be audited, fidelity remains unresolved.

### E.6 Behavior independence

No system output, selected action, downstream success, or model behavior may enter the validation rule. Fidelity must be adjudicable even if the eventual system emits no usable response.

## F. Assignment mechanism

The specified exposure law remains:

\[
P(A_t=\alpha\mid S_{\mathrm{pre}})
=
P(A_t=\beta\mid S_{\mathrm{pre}})
=\frac12,
\]

with an independent fair within-arm nuisance bit, yielding:

\[
P(00)=P(01)=P(10)=P(11)=\frac14.
\]

A future actual generator must record and validate:

- the exact assignment mechanism and revision;
- how random state is obtained and stored;
- the arm and nuisance-state mapping;
- every input or hidden state consulted;
- whether any accessible pre-state predicts the draw;
- where seed, scheduler, block, and audit state travel;
- an independent mechanism-conformance record.

Three objects remain distinct:

```text
specified probability law
randomization-mechanism correctness
realized finite-sample frequencies
```

Uniform observed counts do not establish a fair conditional mechanism. Random finite imbalance does not by itself establish mechanism failure. No sample size, test, estimator, or finite-sample acceptance rule is selected here.

Current status:

```text
ASSIGNMENT-LAW FIDELITY:
  PROSPECTIVE OBLIGATION SPECIFIED
  ACTUAL GENERATOR UNVALIDATED
```

## G. Isolation model

The prospective object requires a fresh causally isolated instance for each exposure. In a future actual apparatus, that must mean that every experimentally controlled source of pre-decision persistence is recreated from one arm-independent baseline or proven irrelevant and inaccessible.

The isolation record must cover:

```text
conversation and message history
process and session state
model-side memory exposed to the experimental boundary
tool state and permissions
cache and retrieval state
environment variables
files and persistent storage
previous trial content and assignments
batch and scheduler context
provider or wrapper state under experimental control
```

An empty visible conversation is not sufficient. A new request identifier is not sufficient. A nominal reset command is not sufficient.

Opaque internal state is not declared controlled merely because it is unknown. If such state can carry target-relevant information across the chosen boundary and its behavior cannot be excluded or validated, the actual platform remains unresolved or unsuitable for this claim.

Current status:

```text
RESET / ISOLATION:
  PROSPECTIVE OBLIGATION SPECIFIED
  ACTUAL CONTROL UNVALIDATED
```

## H. Evaluator separation

Let \(M_{\mathrm{eval}}\) contain arm, state, warranted direction, randomization state, validation data, audit identity, and scoring information. A later apparatus must establish a data-flow and access boundary under which evaluator-only encodings do not enter \(S_{\mathrm{realized}}\).

After exposure, deriving arm, nuisance bit, or warranted direction solely from the licensed labeled register pair is intended. The prohibited path is a separate evaluator field, metadata value, routing consequence, shared state, or side effect that conveys the same information independently of the constituted evidence.

A future separation record must identify:

- every store, process, message builder, environment, tool, and interface shared by evaluator and exposure path;
- every evaluator field and its access classification;
- every transformation that can consult evaluator state;
- evidence that fields called `private` are causally inaccessible rather than merely conventionally hidden;
- matched pre-treatment captures for upcoming \(\alpha\) and \(\beta\) assignments.

Current status:

```text
EVALUATOR SEPARATION:
  PROSPECTIVE OBLIGATION SPECIFIED
  ACTUAL SEPARATION UNVALIDATED
```

### H.1 Prospective validation evidence bundle

The 15% discretionary addition is one evidence-bundle schema inside this artifact, not an executable fixture. A future authorized validation must preserve:

| Record | What it must establish |
|---|---|
| Specification manifest | Exact parent exposure object and allowed differences |
| Component and transformation manifest | Every actual node and arrow from specification to final boundary |
| Pre-transform capture | Exact object entering each actual transformation |
| Post-transform capture | Exact object leaving each transformation |
| Final-boundary capture or independent guarantee | The complete state actually accessible before decision |
| Structured-field and serialization inventory | Roles, names, schemas, bytes, ordering, encoding, scaffolding, and metadata |
| Boundary access matrix | `SYSTEM_ACCESSIBLE`, `SYSTEM_INACCESSIBLE`, or `UNKNOWN` for every channel |
| Controlled pre-state manifest | Complete matched baseline for the two forthcoming-arm worlds |
| Reset/isolation manifest | What is recreated, cleared, retained, opaque, and independently checked |
| Assignment-mechanism record | Exact mechanism, hidden inputs, mapping, state flow, and law-conformance evidence |
| Evaluator-separation record | Private fields, stores, processes, interfaces, and absence of independent crossings |
| Exact-content digest | A prospectively chosen content digest over each complete captured object; no digest alone proves boundary completeness |
| Independent adjudication record | Validation that does not consult system behavior or expected behavioral success |

No such bundle is produced here. Static examples would remain specification illustrations, not \(S_{\mathrm{realized}}\), apparatus output, or fidelity evidence.

## I. Countermodel results

| Countermodel | Held fixed | Varied | Failure it would establish | Prospective validation that detects it | Result |
|---|---|---|---|---|---|
| Renderer adds a message name, zero-width marker, extra field, or different role while preserving visible register prose | Scientific state and intended record | Post-specification rendering | Realized object contains an unlicensed direction path or altered content | Final-boundary structured capture, decoder, and full structural diff | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Human-readable content is clean while `arm=alpha`, `expected_answer`, source path, or custom ID is accessible | Visible prompt and register values | Hidden metadata | Prompt-only validation passes contamination | Complete boundary inventory and accessibility matrix | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Arms use different templates, roles, schemas, ordering, or encoding branches | Evidence semantics | Serialization path | Apparatus changes more than licensed values | Per-arrow component record and cross-arm full-object comparison | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Exact uniform arm counts come from an accessible alternating index or without-replacement schedule | Marginal frequencies | Conditional assignment given pre-state | Arm is known before evidence despite perfect balance | Mechanism audit plus matched pre-state capture; counts alone cannot pass | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| New visible conversation shares `LAST_ARM` through cache, tool state, file, retrieval store, environment, or provider session | Visible history | Hidden persistence | Fresh-instance premise is false | Operational reset manifest and controlled-state comparison | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Scorer and renderer share state that enters a tool description, retrieval context, wrapper branch, or exception path | Intended content and scoring need | Evaluator data flow | Evaluator-only direction bypasses evidence | Evaluator access graph, shared-store inventory, and final-boundary capture | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Generator gives `00,11,01,10` probabilities `.49,.01,.01,.49` | Valid support | Assignment mechanism | Support is correct but exposure law is false | Independent mechanism-conformance validation, not support inspection | Design **SURVIVES**; actual apparatus **UNRESOLVED** |
| Logged client payload is exact, but a platform later adds a hidden prefix, role/name field, tool schema, attachment, retrieval context, or route | Client request and visible content | Unlogged final boundary | Partial-boundary validator produces a false pass | Completeness gate requires final-boundary access or independent apparatus guarantee | Design **SURVIVES**; actual platform **FAILS OR REMAINS UNKNOWN** |
| Platform defect is followed by redefining allowed metadata, reset, or representation to make it pass | Observed platform and desired result | Scientific specification after inspection | Post-hoc repair overwrites the ancestor | Kintsugi lineage check requires an explicit successor; original failure remains | Design **SURVIVES**; repaired same-object claim **FAILS** |
| Composite false-clean: batch index determines arm, leaks only through message name, prior state persists in a tool cache, and validator hashes only prose | Intended values, visible wrapper, uniform table | Multiple hidden channels | Every surface check passes while history and metadata bypass evidence | Full boundary, mechanism, reset, and evaluator checks are conjunctive | Design **SURVIVES**; partial validator **FAILS** |

The strongest attack is partial-boundary validation. If an actual platform does not expose an auditable final system-facing boundary, a perfect pre-platform payload cannot establish realized fidelity. The correct result is `UNKNOWN` or failure, never a pass with caveats.

## J. Authority gained if the validation design survives

The maximum conclusion currently earned is:

> A non-executable prospective validation specification can state what a future authorized apparatus must expose, capture, compare, reset, and keep private to determine realized exposure fidelity.

The stronger conclusion supplied for an actual concrete path is not earned:

> A concrete realization path has a prospectively specified validation procedure capable of establishing whether it preserves the already constituted G1 exposure object without introducing the declared alternative channels.

No concrete path exists under current authority, so this artifact establishes only the schema and stopping conditions needed before that stronger sentence could become available.

## K. Authority not gained

This artifact supplies:

```text
no realized exposure fidelity result
no complete platform-boundary result
no assignment-generator validation
no reset or isolation validation
no evaluator-separation validation
no system decision result
no S_realized→D causal result
no G1 empirical effect
no evidence-controlled adaptation result
no response mapper or parser
no causal estimand
no effect threshold
no sample-size or statistical procedure
no selected platform, API, model, benchmark, or dataset
no implementation validation
no empirical execution
no frozen G1 contract
no MEASUREMENT_VALID transition
no G2
no PMC
no JT
no adaptive viability
no AGI or ASI authority
```

## Death and blocking conditions

A future concrete candidate must be recorded as:

```text
CANDIDATE REALIZED EXPOSURE:
  FAILED FIDELITY VALIDATION
```

if:

- complete system-facing boundary coverage cannot be established;
- intended evidence is swapped, omitted, altered, truncated, duplicated, or reinterpreted;
- arm-correlated metadata or another independent direction cue reaches the system;
- target-relevant arm information becomes accessible before intended exposure;
- the required reset/isolation boundary cannot be instantiated or validated;
- evaluator-private state leaks through any independent route;
- the realized assignment mechanism does not match the prospective law;
- validation observes only a proper subset of the accessible input;
- an unknown channel is treated as inaccessible without evidence;
- the apparatus requires changing an upstream object to pass.

The failure must be preserved. Model success, expected decisions, balanced data, downstream utility, or post hoc filtering cannot rescue it.

This current artifact is not a failed apparatus result because no apparatus was authorized or instantiated. Its realized-fidelity status is blocked.

## Provenance and preserved authority

The exact stacked candidate lineage is:

```text
0ffdf60   canonical authority baseline
    ↓
d9639d3 / PR #19   X→R object-constitution ancestor
    ↓
f62944c / PR #20   R→S_specified exposure-integrity ancestor
    ↓
this artifact      S_specified→S_realized validation-design successor
```

Immediate scientific ancestors:

- [`G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md`](G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md) — the protected prospective exposure parent;
- [`G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md`](G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md) — the protected evidence-object ancestor;
- [`../lineage/decisions/G1_LEVEL0_ROLE.md`](../lineage/decisions/G1_LEVEL0_ROLE.md) — the scoped G1 role and authority ceiling;
- [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md) — the authority requirement for the separable realization edge.

Governing authority and method:

- [`../research_state.json`](../research_state.json);
- [`../RESEARCH_STATE.md`](../RESEARCH_STATE.md);
- [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md);
- [`../contracts/README.md`](../contracts/README.md);
- [`../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md`](../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md);
- [`../KINTSUGI.md`](../KINTSUGI.md).

The two upstream artifacts remain byte-preserved and reconstructible. Canonical `main`, both draft PRs, `research_state.json`, state summaries, contracts, ledgers, decisions, experiments, implementation flags, and execution authority remain unchanged.

## Terminal report

```text
REALIZED EXPOSURE FIDELITY:
  BLOCKED_BY_AUTHORITY

UPSTREAM X→R:
  PRESERVED

UPSTREAM R→S_SPECIFIED:
  PRESERVED

EXECUTABLE IMPLEMENTATION AUTHORITY:
  NOT AUTHORIZED

REALIZATION PATH:
  NO AUTHORIZED CONCRETE PATH;
  NONEXECUTABLE VALIDATION SCHEMA ONLY

COMPLETE SYSTEM-FACING BOUNDARY:
  NOT ESTABLISHED FOR ANY ACTUAL APPARATUS

ASSIGNMENT-LAW FIDELITY:
  PROSPECTIVE OBLIGATION SPECIFIED;
  ACTUAL GENERATOR UNVALIDATED

RESET / ISOLATION:
  PROSPECTIVE OBLIGATION SPECIFIED;
  ACTUAL CONTROL UNVALIDATED

EVALUATOR SEPARATION:
  PROSPECTIVE OBLIGATION SPECIFIED;
  ACTUAL SEPARATION UNVALIDATED

AUTHORITY GAINED:
  ONE NONEXECUTABLE CANDIDATE FIDELITY-VALIDATION SPECIFICATION
  CAN STATE WHAT A FUTURE AUTHORIZED APPARATUS MUST EXPOSE, CAPTURE,
  COMPARE, RESET, AND KEEP PRIVATE

AUTHORITY NOT GAINED:
  NO REALIZED FIDELITY, IMPLEMENTATION VALIDATION, MEASUREMENT-VALID
  STATUS, CONTRACT, EXECUTION, SYSTEM RESPONSE, G1 EFFECT, OR
  DOWNSTREAM AUTHORITY

LIVE RESIDUAL:
  CURRENT AUTHORITY GATE PLUS EVERY ACTUAL APPARATUS TRANSFORMATION,
  ACCESSIBLE CHANNEL, RANDOMIZER, RESET, AND EVALUATOR-SEPARATION CLAIM

NEXT BOUNDARY IF SURVIVED:
  S_realized → D response-object constitution;
  NOT REACHED WHILE REALIZATION FIDELITY REMAINS BLOCKED

EMPIRICAL AUTHORITY MOVEMENT:
  0

CANONICAL MAIN:
  UNCHANGED

PR #19:
  DRAFT / UNMERGED

PR #20:
  DRAFT / UNMERGED
```

The authority gate is itself the stopping condition. No concrete realization may be constructed to close the residual in this task:

\[
\boxed{\text{BLOCKED BY AUTHORITY}\Rightarrow\text{STOP}.}
\]

Do not test \(D\). Do not select a system or platform. Do not merge anything.
