# Concrete Binding Record — `g1-minimal-v0`

## Status

**CONCRETE APPARATUS REFERENT FROZEN — FIDELITY AUDIT NOT EXECUTED — NO EXECUTION AUTHORIZED — G1 UNTESTED**

\[
\boxed{
D_{\mathrm{g1\ minimal\ referent}}
=
\mathrm{CONCRETE\_APPARATUS\_REFERENT\_FROZEN}
}
\]

This record binds the exact implementation/configuration target to be submitted to the already-frozen G1 Apparatus Fidelity Audit Protocol. It does not assert `FIDELITY_PASS`; runtime realization of the declared boundary and isolation conditions remains an audit question.

## Binding identity

- Apparatus: `g1-minimal-v0`
- Implementation root: `measurement/g1_minimal_v0/`
- Frozen implementation commit: `4c947e2b7a4680cfcb162a929d81ef1fd1e42cc4`
- Load-bearing SHA-256 manifest root: `d1ceb2c185fb1eaca17c24d26d44aa5d783c6bda55b5f4762b4aea90708705d1`
- Machine-readable binding manifest: `measurement/g1_minimal_v0/binding_manifest.json`
- Binding-manifest SHA-256: `c002bbcbd65ced943ebd382ad42f869753b6d685d5d001ab46011185780fa253`

The manifest root is SHA-256 over canonical JSON mapping each load-bearing relative path to its SHA-256, with keys sorted and separators `(',', ':')`. Binding records and validation-only tests are excluded from that root.

## Frozen scientific and measurement values

- Domain: `X = ["x1", "x2", "x3", "x4"]`; candidates `c_A`, `c_B`.
- `O_C(X)`: exact deterministic table in `data/oc_table.py`.
- Evidence constructor: deterministic `g` in `src/evidence.py`.
- Adjudicator/reference: `q` and independent `r` are distinct implementations.
- Agreement estimator: exact set equality over all four `X` values, equally weighted; no ties.
- Pre-audit agreement on the frozen synthetic domain: `3/4 = 0.75`.
- Frozen threshold: `GAMMA_FROZEN = 0.75`; the criterion is met exactly.

## Frozen package and null rule

Both potential exposures are constructed before assignment. Treatment and control containers have identical top-level keys `evidence` and `direction`; the control sets `direction = None`. `N(E)` receives no direction input. Frozen matched coordinates are `noise` and `format`, with `noise = 0.0` tolerance and `format = exact`.

## Frozen assignment mechanism Q

Assignment is `int(SHA256(seed + ':' + unit_id), 16) mod 2`. This is a SHA-256-based prospective assignment rule, not a claim that a stream PRNG is used. All unit IDs are frozen and auditor-checkpointed before campaign-seed commitment; the seed is then frozen/checkpointed before any audit-unit package construction. Evidence, direction, candidate identity, selector prediction, and outcome-analysis state are forbidden inputs.

## Frozen transformation graph Gamma

Transport is canonical JSON over a process stdin/stdout pipe: UTF-8, sorted keys, separators `(',', ':')`, `ensure_ascii=True`, followed by `json.loads`. Licensed equivalence is exact structural equality after round-trip. Selector and adjudicator are separate subprocess entry points.

## Frozen selector boundary and runtime target

The declared selector environment is frozen in `config/selector_environment.txt`; process-isolation obligations are frozen in `config/process_isolation.txt`. The exact reference runtime used for pre-audit validation is CPython 3.13.5 on `Linux-6.18.35-x86_64-with-glibc2.41`, with Python executable SHA-256 `17b78e0a93175e86f9ac03141924fd7a7f0c0c52e66b34bfa0de20ffef989df1`.

These are bound target conditions, not a fidelity verdict. If the later running audit environment does not match the bound referent or cannot establish the declared selector-accessible boundary, the frozen audit protocol must return `FIDELITY_FAIL` or `INVALID/UNRESOLVED` as appropriate.

## Reset, isolation, and provenance

The harness creates fresh adjudicator and selector subprocesses per unit. Hash-chained audit records are implemented in `src/provenance.py`. The frozen checkpoint-genesis content is `g1-minimal-v0:auditor-checkpoint-genesis:v0` with SHA-256 `1625c3c679868846694a05032fcbf74817cb573e6c95e1139bb1eebc39b948e3`.

The checkpoint mechanism/genesis are bound here. No audit campaign has yet produced an auditor-owned external receipt; external custody is evidence to be created during the fidelity audit, not retroactively claimed by this binding record.

## Pre-audit validation only

The binding suite passed `7/7` tests on the exact prepared contents, covering domain identity, `q/r` agreement, structural null matching, exact transport round-trip, selector behavior, separate-worker harness execution, and deterministic binary assignment. This is implementation validation only. It is not the frozen fidelity audit and moves no apparatus-fidelity authority.

## Authority state

\[
\boxed{
\begin{aligned}
D_{\mathrm{g1\ minimal\ referent\ specification}}
&=\mathrm{REFERENT\_SPECIFICATION\_FROZEN},\\
D_{\mathrm{g1\ minimal\ referent}}
&=\mathrm{CONCRETE\_APPARATUS\_REFERENT\_FROZEN},\\
D_{\mathrm{G1\ apparatus}}
&=\mathrm{UNTESTED},\\
\text{Fidelity audit}
&=\mathrm{NOT\ EXECUTED},\\
\mathrm{AUTH(execution)}
&=\mathrm{FALSE},\\
G_1
&=\mathrm{UNTESTED}.
\end{aligned}
}
\]

The next legitimate action is to execute the already-frozen G1 Apparatus Fidelity Audit Protocol against this exact content-addressed referent. Any load-bearing file, runtime identity, configuration, boundary declaration, assignment policy, or provenance change constitutes referent drift and requires a new binding and audit.
