# Lineage

This directory is the program's provenance spine.

The purpose is to preserve one cumulative scientific lineage without pretending that every historical experiment tested the same estimand.

## Rule

```text
ancestor result
→ authority gained or lost
→ mechanism diagnosis
→ descendant authorization
```

A descendant may inherit a question or failure boundary. It does **not** inherit authority that the ancestor failed to earn.

## Canonical ledger

[`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md) is the human-readable program ledger.

Each entry records:

```text
object
status
observation
claim earned
claim not earned
consequence for the next gate
```

Historical implementation details may live elsewhere, but the public program should be understandable from this ledger plus the experiment contracts and results.
