# Scientific change

> **Maximum ambition; minimum unearned authority.**

## Scientific object

What scientific, measurement, methodological, provenance, or communication object does this change address?

## Program maturity level

Choose one:

- [ ] Level 0 — Measurement / scientific-object validity
- [ ] Level 1 — Evidence-controlled adaptive decision
- [ ] Level 2 — Isolated modification
- [ ] Level 3 — Evidence → justified modification
- [ ] Level 4A — Post-Modification Correctability
- [ ] Level 4B — Repeated correction
- [ ] Level 5 — Justified Transformability
- [ ] Level 6 — Adaptive viability / capability
- [ ] Level 7 — Extreme adaptive-system stress test
- [ ] Cross-level methodological / composition work
- [ ] Non-empirical infrastructure / documentation

## Lifecycle transition

**Before:** `PROPOSED | ADVERSARIAL_REVIEW | MEASUREMENT_VALID | CONTRACT_FROZEN | AUTHORIZED | EXECUTED | ANALYZED | CLOSED | N/A`

**After:** `PROPOSED | ADVERSARIAL_REVIEW | MEASUREMENT_VALID | CONTRACT_FROZEN | AUTHORIZED | EXECUTED | ANALYZED | CLOSED | N/A`

Explain why the transition is warranted. If no state changes, say so explicitly.

## Failure localization

If this PR is a correction or reopening:

**Shallowest sufficient failure locus:**

`observation/measurement | inference | mechanism | representation/interface | implementation/estimator | scientific proposition | methodological rule | N/A`

What discriminating evidence or surviving residual warrants reopening this boundary?

If the change is only a deeper redescription of an already successful localization, it should not reopen the object.

\[
\boxed{\text{redescription}\neq\text{re-localization}}
\]

## Authority change

What new authority, if any, does this PR claim to establish, withdraw, narrow, or transfer?

If none:

```text
AUTHORITY CHANGE: NONE
```

## Upstream prerequisites

List every upstream prerequisite required by this change and its current status.

- [ ] I checked [`RESEARCH_STATE.md`](../RESEARCH_STATE.md).
- [ ] I checked [`research_state.json`](../research_state.json).
- [ ] I checked [`lineage/EVIDENCE_LEDGER.md`](../lineage/EVIDENCE_LEDGER.md).
- [ ] I checked the relevant decision record(s).
- [ ] This PR does not bypass an unresolved upstream prerequisite.

## Lineage / Kintsugi impact

What ancestor, prior rule, result, or interpretation does this change touch?

- [ ] No prior scientific authority state is affected.
- [ ] A current conceptual/methodological rule is being reopened under new discriminating evidence.
- [ ] A frozen contract is preserved and an explicit successor/amendment is created.
- [ ] A closed empirical result is touched only as historical provenance; its recorded result is unchanged.
- [ ] A descendant object is created with a new scientific identity.

Explain the seam:

```text
old state
→ reason for reopening
→ discriminating evidence / residual
→ explicit repair
→ new scoped authority
→ preserved ancestor
```

## Frozen / closed objects

Does this change touch a frozen or closed empirical object?

- [ ] No
- [ ] Yes — documentation/provenance only; the historical result remains unchanged
- [ ] Yes — an explicit successor or amendment is created with a distinct prospective identity

A frozen contract may be superseded prospectively. It may not be silently rewritten after outcome observation.

A closed result may be reinterpreted or generate descendants. Its historical identity and recorded outcome remain fixed.

## Nonclaims

What does this PR deliberately **not** establish or authorize?

## Implementation authorization

For empirical implementation only:

- [ ] `measurement_state` is `MEASUREMENT_VALID` or later
- [ ] `contract_state` is `CONTRACT_FROZEN` or later
- [ ] `execution_state` is `AUTHORIZED`
- [ ] `implementation_authorized` is `true`

If these are not all true, explain why the change cannot silently choose unresolved scientific decisions through code, prompts, data, models, or apparatus convenience.

## Validation

What was checked, and what evidence supports this PR's claimed scope?

## Final audit

- [ ] The claim is no larger than the evidence.
- [ ] Historical provenance is preserved.
- [ ] Any reopening is localized to the smallest evidence-implicated boundary.
- [ ] No deeper escalation is claimed if the relevant residual is already zero.
- [ ] No empirical execution is implied unless explicitly authorized.

> **Commit hard. Preserve lineage. Reopen on evidence.**
