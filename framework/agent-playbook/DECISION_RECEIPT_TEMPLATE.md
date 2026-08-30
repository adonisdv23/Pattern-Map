# Layered decision receipt template

Use this after the preflight and again when the answer or route is complete.
It is a compact audit trail, not a claim that the answer is correct.
A Stage-0 ordinary transformation does not use this receipt. Use repository
template `framework/templates/ORDINARY_RECORD.md` and stop before route, stop,
outcome, learning, influence, or family records.

## Header

- Receipt ID:
- Decision ID / brief version:
- Receipt version:
- Started / ended:
- Operator / agent:
- Operating level: LIGHTWEIGHT / MODERATE / ADVANCED
- Reviewer / authority:

## Decision and consequence

- Real question:
- Intended use:
- Audience:
- Consequence: LOW / MEDIUM / HIGH / UNKNOWN
- Reversibility:
- Deadline:
- Human action boundary:

## Permission

| Operation | Technical access | Permission state | Scope | Reason code | Reason | Resume condition |
| --- | --- | --- | --- | --- | --- | --- |
| Acquire |  |  |  |  |  |  |
| Transform |  |  |  |  |  |  |
| Retain / memory |  |  |  |  |  |  |
| Disclose |  |  |  |  |  |  |
| Act |  |  |  |  |  |  |

Use exactly `AUTHORIZED`, `UNKNOWN`, `NOT_AUTHORIZED`, or `REVOKED` for
permission state. Unknown, absent/denied, and revoked permission have different
reasons and resume conditions; none may appear in selected influence. An
executable permission object contains only `technical_access`, `state`,
`scope`, `reason_code`, `reason`, and `resume_condition`. Reject legacy
booleans such as `authorized` or `permission_granted` rather than allowing two
permission answers in one record. Reject the same fields if repeated at the
receipt top level.

For the current single-global-permission receipt, an `UNKNOWN`,
`NOT_AUTHORIZED`, or `REVOKED` state leaves evidence, baseline, comparison,
disconfirmation, memory, and influence empty and records memory as `NOT_USED`.

## Cost and stop envelope

- Time used / limit:
- Money used / limit:
- Tokens or compute used / limit:
- Reviewer attention used / limit:
- Privacy / security exposure:
- Remaining budget:
- Hard stop:
- Soft stop:
- Resume condition:

## Family record

| Family | Used / skipped | Artifact or receipt | What it exposed | Boundary preserved |
| --- | --- | --- | --- | --- |
| F1 Peripheral signal |  |  |  | Candidate, not truth |
| F2 Source weighing |  |  |  | Authority/support/origin/permission distinct |
| F3 Velocity / motion |  |  |  | Baseline and repeated observations |
| F4 Absence + memory |  |  |  | Expected baseline and versioned memory |
| F5 Structured patterns |  |  |  | Comparison and unknown relations |
| F6 Learning loop |  |  |  | Outcome update proposed, history preserved |

An inactive family receives one concise skip reason and no artifact. The table
is a proportionality record, not a requirement to activate all six families.

## Evidence and comparison

- Default path:
- Peripheral route:
- Acquisition receipts:
- Source and artifact IDs:
- Claim IDs and exact spans:
- Support / contradiction / qualification:
- Origin / recurrence / independence:
- Comparison frame:
- Motion baseline, shared alignment key, and two or more authorized
  time-bearing observation IDs resolving to at least two distinct real UTC-Z
  instants:
- Absence baseline and observation boundary:
- Memory links:
- Disconfirmation log:
- Typed uncertainty:

- Comparison disposition: PERFORMED / NOT_APPLICABLE
- Comparison inactive reason (one bounded line; no placeholder record):
- Disconfirmation disposition: PERFORMED / SKIPPED
- Disconfirmation inactive reason (one bounded line; no placeholder record):

Every baseline, comparison, disconfirmation, influence, and memory ID named in
this receipt must resolve to a substantive preserved record. Empty status
booleans and dangling IDs do not establish that a check occurred. When memory
is material, use `framework/templates/MEMORY_RECORD.md`.
Only a `CURRENT`, `AUTHORIZED` memory record may be used or selected;
`SUPERSEDED` records remain preserved as withheld history.

Every `ANSWER` or `ANSWER_PROVISIONALLY` route needs a substantive comparison
and disconfirmation record, or the matching typed inactive status with one
bounded task-specific reason. `PERFORMED` requires resolvable records;
`NOT_APPLICABLE` or `SKIPPED` requires none.

## Route

- Route: ANSWER / ANSWER_PROVISIONALLY / ACQUIRE / COMPARE / CLARIFY /
  HOLD / DEFER / ESCALATE / REFUSE
- Stop status: CONTINUE / COMPLETE / STOPPED_BUDGET / STOPPED_DEADLINE /
  STOPPED_OTHER
- Learning status: LEARNING_PLANNED / LEARNING_PENDING_OUTCOME /
  LEARNING_REVIEWED / LEARNING_NOT_APPLICABLE
- Why this route:
- Expected benefit:
- Cost:
- Permission:
- Strongest unresolved issue:
- Why the route stopped or will stop:

## Influence

| Item | Claim / decision role | Why admitted | What it supports | What it cannot establish | Permission |
| --- | --- | --- | --- | --- | --- |
|  | SUPPORTS / QUALIFIES / CONTRADICTS / FRAMES / ROUTES |  |  |  |  |

| Withheld item | Reason | Could change conclusion? | Re-entry condition |
| --- | --- | --- | --- |
|  |  |  |  |

For memory, Selected material is limited to `CURRENT` + `AUTHORIZED` records.
List a `SUPERSEDED` version only in Withheld material with its lineage link; do
not treat preservation as current influence.

## Output boundary

- Observations:
- Interpretations:
- Recommendations:
- Unknowns and caveats:
- External action requiring human authority:

## Disposition

- ACCEPTED / REJECTED / DEFERRED / OVERRIDDEN / REQUEST_ENRICHMENT:
- Decision maker and authority:
- Reason:
- Correction or supersession link:

`ESCALATE` belongs in the route field above. After an accountable person acts,
record that person's disposition with the existing disposition vocabulary;
do not treat the act of routing as the human decision.

## Outcome learning

- Outcome review ID:
- Expectation recorded:
- Outcome definition and window:
- Attribution boundary:
- Observed outcome:
- Missing outcome or incomplete observation:
- Actual cost:
- Confounders or missingness:
- Bounded update proposed:
- Human disposition of proposed update: ACCEPTED / REJECTED / DEFERRED /
  OVERRIDDEN / REQUEST_ENRICHMENT
- Learning status after disposition: LEARNING_REVIEWED / LEARNING_NOT_APPLICABLE
- Update applied? YES / NO / DEFERRED

Do not record `LEARNING_REVIEWED` unless an outcome review is linked, an
observed outcome or explicit missing-outcome state is recorded, and an
accountable person has dispositioned the proposed update.

## Fast stop examples

### Example A — permission blocks acquisition

- Consequence: HIGH
- Technical access: YES
- Operational authorization: UNKNOWN
- Route: HOLD / ESCALATE
- Stop status: STOPPED_OTHER
- Stop reason: Access is not permission; no acquisition or disclosure occurred.
- Resume condition: Named authority records purpose-limited authorization.

### Example B — low-cost provisional answer

- Consequence: LOW
- Supplied evidence: authorized and bounded
- One expected comparison: completed
- Disconfirmation: one contrary route checked
- Route: ANSWER_PROVISIONALLY
- Stop status: COMPLETE
- Stop reason: remaining search is expected to add duplicates within the
  five-minute limit.
- Caveat: the answer is limited to the observed material and is not a claim of
  independent corroboration.
