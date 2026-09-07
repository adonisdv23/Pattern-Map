# Domain-neutral case B — deciding whether to change an intake process

Status: ILLUSTRATIVE FIXTURE / NOT EMPIRICAL / NOT A PRODUCT CLAIM

This case uses a generic team intake process rather than a named product or
vendor. The values are invented fixtures. It demonstrates motion, expected
absence, source roles, comparison, permission, stopping, and a later learning
loop without claiming that the proposed change would work.

## Decision brief

- Decision: decide whether to add one required field and one review step to an
  internal intake form.
- Intended use: advise the process owner.
- Consequence: MEDIUM; change is reversible but may affect staff workload.
- Human authority: the process owner decides whether a required field or review
  step is authorized.
- Default path: inspect the latest completion dashboard and recent support
  notes.
- Peripheral route: compare the prior process version and a less-visible
  rejection category.
- Permission: supplied internal records only; no user outreach or export.
- Cost boundary: 30 minutes; no new instrumentation; one process-owner review.
- Hard stop: do not recommend a required field if its purpose, privacy impact,
  or owner authority is unknown.
- Outcome: if the change is authorized, compare completion, rework, and
  correction time for a defined window.

## Fixture observations

| ID | Observation | Source role | State | Boundary |
| --- | --- | --- | --- | --- |
| PP-A-001 | Latest dashboard shows more incomplete submissions than the prior snapshot | Dashboard record | OBSERVED_MOTION_CANDIDATE | Collection and denominator change are not yet checked |
| PP-A-002 | Support note says several submitters were unsure which attachment was needed | Support context | QUALIFIES | Notes may be selective and do not establish prevalence |
| PP-A-003 | Prior form version had an instruction that no longer appears | Versioned process record | OBSERVED_GAP_CANDIDATE | The missing instruction may reflect an intentional change |
| PP-A-004 | A rejection category is absent from the latest export | Expected field | GAP / UNKNOWN | Export failure is not proof that no rejection occurred |
| PP-A-005 | Two support notes use similar wording | Support context | RECURRENCE | Shared template or shared case origin is unknown |

All rows are invented procedure fixtures.

## Six-family route

| Family | Applied action | Stop / boundary |
| --- | --- | --- |
| F1 Peripheral signal | Inspect the prior form version and rejection category beyond the latest dashboard | Do not add a field solely because it is less visible |
| F2 Source weighing | Treat dashboard as a count record, support notes as context, and form version as direct process evidence | None is a universal trust source |
| F3 Velocity / motion | Require comparable snapshots and check denominator, export, and workflow changes | One before/after snapshot is not velocity |
| F4 Absence + memory | Record the absent rejection category as export/memory uncertainty and preserve old form history | Missing export is not zero rejections |
| F5 Structured patterns | Compare versions, categories, attachment definitions, and support notes; keep shared origin unknown | Similar support wording is not independent evidence |
| F6 Learning loop | Predeclare completion, rework, correction time, and privacy review outcomes | No silent policy update |

## Bounded comparison

| Dimension | Current process fixture | Prior process fixture | What it can show |
| --- | --- | --- | --- |
| Instruction | Missing in latest snapshot | Present in prior version | A version difference to inspect |
| Incomplete submissions | Higher in latest snapshot | Lower in prior snapshot | A motion candidate if measurements align |
| Rejection category | Absent from export | Present in older structure | A gap in the current observation boundary |
| Support wording | Two similar notes | Unknown | Recurrence, not independent prevalence |
| Privacy impact | New required field not specified | Not applicable | Must be reviewed before recommendation |

## Disconfirmation

- Leading interpretation: the missing instruction may contribute to incomplete
  submissions.
- Contrary possibilities: the dashboard definition changed; the export dropped
  a category; the support notes share one origin; workload or policy changed.
- Checks: compare definitions and denominators; inspect the form version; check
  export receipt; inspect the absent category; ask the process owner about the
  purpose and privacy of a required field.
- Current route: HOLD until the observation boundary and permission for a
  required field are clarified.
- Provisional wording if the owner needs an immediate summary: “The supplied
  fixtures show a version difference and a motion candidate, but they do not
  establish causation, prevalence, or a safe process change.”

## Learning loop if authorized

Record before any change:

- expected direction and measurement definitions;
- completion, rework, and correction-time thresholds;
- privacy or burden guardrail;
- comparison window and rollback owner;
- stop condition for harmful or low-value effects.

Later, compare the observed outcome with the expectation and actual cost. Propose
one bounded update to the intake rule or measurement definition, preserve the
original process version, and ask the process owner to disposition it.

## Why this case is useful

It makes a common failure visible: a dashboard movement and a missing category
can invite a fluent causal story. The applied route keeps motion, absence,
source role, recurrence, permission, and outcome learning separate. It also
shows when not to use advanced machinery: the supplied fixture can be handled
with a brief, two version snapshots, a gap note, and a human review.
