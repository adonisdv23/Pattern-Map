# Public and transfer hardening — applied integrity QA

**Baseline:** `37c7c852ff406431454346eacc694ac04c5f57a5`

**Branch:** `codex/pattern-map-v16-applied-integrity`

**Date:** 2026-08-30

**Status:** implementation complete for the bounded applied lane; structural
and procedural evidence only

## Accepted corrections implemented

1. Stage 0 is inside the advertised copyable prompt before `FRAME`. A genuine
   supplied-material transformation returns only supplied scope, assumptions,
   unchecked boundaries, and output, then terminates.
2. The ordinary fixture and template contain no evidence, route, stop,
   outcome, learning, or six-family fields. Layered receipts begin only after
   Stage 0 selects an evidence-sensitive path.
3. Executable permission uses `AUTHORIZED`, `UNKNOWN`, `NOT_AUTHORIZED`, and
   `REVOKED`, with state-specific reason codes and resume semantics. Unknown,
   absent/denied, and revoked material cannot enter baseline, comparison,
   disconfirmation, memory, or selected influence.
4. Baseline, comparison, disconfirmation, selected-influence, and scoped-memory
   records now carry substantive fields and resolve every named ID. Empty
   status booleans and dangling IDs cannot satisfy the fixture contract.
5. The explicitly synthetic F4 fixture preserves an original record and its
   digest, appends a linked correction, scopes permission and reuse, and fails
   on target deletion, prior-digest drift, missing source, dangling use, or
   revoked reuse.
6. The existing general-research fixture uses F1, F2, F4, and F5 only. F3 and
   F6 are `NOT_USED` and produce `NONE` artifacts; no new case or generic
   adoption artifact was created.
7. The typed permission object now rejects contradictory legacy authorization
   keys. In the current global-permission fixtures, `UNKNOWN`,
   `NOT_AUTHORIZED`, and `REVOKED` require empty evidence, baseline,
   comparison, disconfirmation, memory, and influence, with memory `NOT_USED`.
   The same legacy authorization keys are rejected at receipt top level, where
   they could otherwise contradict the nested typed state.
8. Motion is no longer established by a self-asserted time-point count. A
   motion claim resolves to at least two distinct authorized evidence IDs whose
   timestamps parse as real UTC-Z datetimes, include at least two distinct
   instants, and share one alignment key. Boolean and string fields are
   type-checked.
9. Every answer route carries substantive comparison and disconfirmation
   records or an explicit proportional exception: comparison
   `NOT_APPLICABLE`, disconfirmation `SKIPPED`, one bounded reason each, and no
   placeholder records.
10. Only `CURRENT`, `AUTHORIZED` memory may be used or selected.
    `SUPERSEDED` versions remain preserved as withheld history. The synthetic
    linear F4 fixture binds each digest to canonical payload bytes, checks its
    root against a separately frozen anchor, permits one successor per version,
    and requires exactly one current record. This bounded schema does not
    represent branch authorization, so every fork fails closed pending a
    separate explicit, scoped, authorized branching contract.

## Verification

Run from the repository root:

```text
python3 -m py_compile qa/applied/validate_framework.py
for f in qa/applied/receipts/*.json; do python3 -m json.tool "$f" >/dev/null; done
python3 -m json.tool qa/applied/memory_anchor_registry.json >/dev/null
python3 qa/applied/validate_framework.py
python3 qa/editorial/validate_content_interface.py
git diff --check
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
```

The focused validator passes:

- six-family JSON and schema contract;
- artifact inventory and boundary language;
- ordinary and layered receipt contracts; and
- permission/reference/memory fail-closed mutations.

The frozen content-interface validator also passes, confirming that these
applied changes do not alter the locked three-door, six-family, human-opening,
Echo-separation, or source/action contracts.

The locked owner-intent checksum passes. All JSON fixtures parse with the
standard library, and patch whitespace checks pass.

## Fail-closed mutations exercised

- reviewed learning without an outcome review or human disposition;
- missing, empty, revoked, or dangling baseline/comparison/disconfirmation
  references;
- performed checks without records, inactive checks with records, multiline
  skip reasons, and a passing proportional answer control with typed inactive
  reasons;
- self-asserted motion counts, one or duplicate observation ref, misaligned or
  non-time-bearing refs, refs outside the baseline, missing aligned comparison,
  impossible or duplicate instants, revoked refs, and bool/string type
  confusion;
- dangling or permission-unknown selected influence;
- boolean authorization, contradictory legacy authorization extras inside the
  permission object or at receipt top level, mismatched permission reason code,
  and missing UNKNOWN resume condition;
- evidence, baseline, comparison, disconfirmation, memory, memory use, or
  influence under each blocked global permission state;
- evidence, route, stop, outcome, learning, or family fields added to the
  ordinary record; and
- missing prior memory, payload/digest drift, coordinated root rewrite against
  a frozen anchor, unauthorized fork, multiple current records, missing memory
  source, dangling memory use, revoked reuse, rejected correction, and
  superseded use or selection.

## Evidence ceiling and integration boundary

These checks prove selected document, fixture, vocabulary, reference, typing,
payload-digest, frozen-anchor, linear-lineage, and mutation invariants. The
anchor is a QA fixture boundary, not a claim of immutable storage or runtime
enforcement. Exact JSON keys are the smallest fixture contract exercised here,
not a universal downstream receipt architecture. The checks do not show that
an agent followed the playbook, that
the records are truthful, that a permission assertion is legally valid, that
an answer is correct or useful, that memory improves a decision, that the
general-research fixture transfers to a real project, or that the framework is
effective. No model, provider, participant, product, external system, or study
was run.

The primary integrator must regenerate any cross-lane package/manifest evidence
after merging all implementation lanes. This lane did not edit governing docs,
the site, manuscript, research, archives, Echo, or handoff files.
