# Evidence register

Keep observations, interpretations, and dispositions in separate columns.
Duplicate rows can represent repeated observations; origin and independence
must be recorded separately.

For any record used in a motion claim, make `time_bearing` an actual boolean,
record a UTC `observed_at` value, and record a string `alignment_key`. A motion
baseline names at least two distinct authorized evidence IDs sharing that key,
whose timestamps parse as real UTC-Z instants and include at least two distinct
instants; a separate integer count is not a substitute for the references.

| ID | Claim ID | Source ID | Artifact ID | Version / time | Exact span or pointer | Observed metadata | Source role | Relevant track-record evidence | Claim-scoped authority | Support state | Origin state | Recurrence state | Relevance | Permission | Uncertainty | Disposition | Influence role | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E-001 | C-001 | S-001 | A-001 |  |  |  | PRIMARY / SECONDARY / SPECIALIST / AGGREGATOR / OTHER / UNKNOWN | Exact prior record scoped to the claim, domain, and time—or UNKNOWN; never a universal score | What this source may establish for C-001—and what it may not | SUPPORTED / CONTRADICTED / QUALIFIED / INSUFFICIENT / UNKNOWN | INDEPENDENT / RELATED / COMMON_ORIGIN / UNKNOWN | RECURRENT / NOT_RECURRENT / UNKNOWN | HIGH / MEDIUM / LOW / UNKNOWN | AUTHORIZED / NOT_AUTHORIZED / UNKNOWN / REVOKED |  |  | SUPPORTS / QUALIFIES / CONTRADICTS / FRAMES / ROUTES / NONE |  |

## Machine-receipt mapping

An executable layered receipt keeps the F2 dimensions as separate fields; it
must not compress them into a source score or a single trust label:

- `source_role`;
- `track_record_evidence`, either a resolvable claim/domain/time-scoped pointer
  or `UNKNOWN`;
- `claim_scoped_authority`;
- `support_state`;
- separate `origin_state` and `recurrence_state`;
- `relevance`;
- `provenance_ref`; and
- `permission_state`.

The record also retains `exact_pointer`, `claim_ids`, and the time/alignment
fields. A valid permission does not supply authority, support, provenance, or
relevance, and none of those fields may be inferred from source role alone.

## Claim ledger

| Claim ID | Narrow claim | What would support it? | What would contradict or qualify it? | Current state | Unknowns |
| --- | --- | --- | --- | --- | --- |
| C-001 |  |  |  |  |  |

## Source-role and authority notes

For each source that appears influential, record its role, relevant
track-record evidence, and what it is authoritative for—and not authoritative
for—on the named claim as separate fields. Track record is scoped by claim,
domain, and time; origin, institutional role, or technical availability does
not supply claim support automatically.
