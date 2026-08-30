# Scoped memory record

Use only when prior material may influence the current output. This is a
version link, not a universal memory service and not evidence that a correction
is true.

## Preserved version

- Memory ID:
- Lineage ID:
- Version:
- Canonical payload (`claim_id`, `statement`, and `scope` in the bounded JSON
  fixture):
- Content digest of canonical UTF-8 payload bytes:
- Separately frozen root-anchor reference:
- Source / evidence IDs:
- Task, source, time, and permission scope:
- Permission state: AUTHORIZED / UNKNOWN / NOT_AUTHORIZED / REVOKED
- Reuse scope:
- Status: CURRENT / SUPERSEDED
- Lineage mode: LINEAR
- Branch authorization reference: NOT_APPLICABLE

## Correction or supersession

- New memory ID:
- Lineage ID:
- New version:
- New canonical payload:
- New content digest of canonical UTF-8 payload bytes:
- Supersedes memory ID:
- Corrects memory ID:
- Prior content digest:
- Correction reason:
- Source / evidence IDs for the correction:
- Permission state: AUTHORIZED / UNKNOWN / NOT_AUTHORIZED / REVOKED
- Reuse scope:
- Human disposition: ACCEPTED
- Lineage mode: LINEAR
- Branch authorization reference: NOT_APPLICABLE

Append the corrected version and retain the prior record unchanged. The
`prior content digest` must match the preserved record, and every content
digest must recompute from canonical payload bytes. Bind the initial version to
a separately frozen root anchor so rewriting the old payload, its digest, and
the successor link together still fails the fixture contract.

The bounded template is linear: one successor per version and exactly one `CURRENT` record per lineage.
Branching is rejected unless a different
contract explicitly represents the branches and records scoped authorization;
do not convert `branch authorization reference` into a casual opt-in. A
missing target, changed prior digest, anchor mismatch, fork, absent reuse scope,
or unresolved permission prevents memory from influencing the output.

This accepted-correction fixture does not model a proposal queue. A correction
with `REJECTED`, `DEFERRED`, `OVERRIDDEN`, or `REQUEST_ENRICHMENT` disposition
cannot enter the current lineage under this shape; preserve it separately
until an explicit proposal/status contract applies.

Only a `CURRENT`, `AUTHORIZED` memory record within its reuse scope may be used
or selected. Keep each `SUPERSEDED` record intact and, if relevant to the
receipt, list it only as withheld history. This structural contract detects
the selected fixture mutations; it does not prove that storage is immutable,
that an operator told the truth, or that a correction is valid.
