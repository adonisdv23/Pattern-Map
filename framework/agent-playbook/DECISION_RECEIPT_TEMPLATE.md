# Decision receipt template

Use this after the preflight and again when the answer or route is complete.
It is a compact audit trail, not a claim that the answer is correct.

## Header

- Receipt ID:
- Decision ID / brief version:
- Receipt version:
- Started / ended:
- Operator / agent:
- Operating level: ORDINARY / LIGHTWEIGHT / MODERATE / ADVANCED
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

| Operation | Technical access | Operational authorization | Retention / disclosure | Result |
| --- | --- | --- | --- | --- |
| Acquire |  |  |  |  |
| Transform |  |  |  |  |
| Retain / memory |  |  |  |  |
| Disclose |  |  |  |  |
| Act |  |  |  |  |

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

## Evidence and comparison

- Default path:
- Peripheral route:
- Acquisition receipts:
- Source and artifact IDs:
- Claim IDs and exact spans:
- Support / contradiction / qualification:
- Origin / recurrence / independence:
- Comparison frame:
- Motion baseline:
- Absence baseline and observation boundary:
- Memory links:
- Disconfirmation log:
- Typed uncertainty:

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
