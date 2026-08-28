# Agent preflight checklist

Run this checklist before acquisition, enrichment, or a consequential answer.
For every P-group, record `PASS`, `FAIL`, `UNKNOWN`, or `NOT_APPLICABLE`, plus
the evidence/receipt IDs that justify the status. `NOT_APPLICABLE` requires a
reason. An `UNKNOWN` required field is not a silent pass. A recorded
`ORDINARY_PATH` may bypass this preflight only when no new evidence,
comparison, memory reuse, permission decision, or external influence is
required.

## P0. Scope and decision

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: the real decision is stated in one sentence.
- Check: intended use and audience are stated.
- Check: consequence and reversibility are stated.
- Check: decision owner and required reviewer are named.
- Check: deadline and outcome window are stated or marked NOT_APPLICABLE.
- Check: answer, hold, defer, refusal, and escalation conditions are stated.

## P1. Permission

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: technical access is listed separately from operational authorization.
- Check: acquisition permission is explicit for each source class.
- Check: transformation, retention, disclosure, and reuse permissions are
  explicit.
- Check: paid, private, sensitive, or external operations have named authority.
- Check: external action is outside the agent’s authority unless explicitly
  delegated and still has a human boundary.

FAIL or UNKNOWN on a consequential permission item means a hard stop, then
route `HOLD` or `ESCALATE`. Record `NOT_AUTHORIZED` when permission is absent
or revoked; record `UNKNOWN` when it has not been established. Do not collapse
those states, acquire, disclose, or act. Record the escalation destination and
the condition needed to resume.

## P2. Cost and stop

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: time and deadline are bounded.
- Check: money and paid retrieval are bounded.
- Check: model, token, and compute use are bounded.
- Check: reviewer attention and privacy exposure are bounded.
- Check: one-more-action benefit is described qualitatively.
- Check: hard and soft stop rules are written.
- Check: budget exhaustion will be recorded as stop status STOPPED_BUDGET,
  not sufficiency.

## P3. Information boundary

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: default query, source set, vocabulary, and time window are recorded.
- Check: at least one bounded alternate route is planned when the decision
  needs breadth.
- Check: expected perspectives, fields, peers, or periods are listed.
- Check: a failed capture will not be treated as absence.
- Check: source, artifact, version, event time, capture time, and exact span can
  be recorded, or their absence is explicitly acknowledged.

## P4. Comparison and claims

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: the answer is decomposed into narrow claims.
- Check: each influential claim has an exact evidence pointer or is marked
  unsupported/provisional.
- Check: source role, relevant track-record evidence, and claim-scoped
  authority are separate from support and from one another.
- Check: recurrence and origin are separate from independence.
- Check: a comparison unit and baseline are stated where needed.
- Check: motion has repeated comparable observations.
- Check: absence has an explicit expected baseline and observation boundary.
- Check: incomparable and unknown relations remain visible.

## P5. Disconfirmation and uncertainty

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: the leading interpretation is written.
- Check: the strongest contrary or limiting search is planned or completed.
- Check: a missing perspective or field is checked.
- Check: alternative explanation, measurement change, or common origin is
  checked where applicable.
- Check: unknown, contested, stale, insufficient, failed, and unauthorized
  states are typed rather than collapsed into confidence.

## P6. Influence and human control

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Check: selected material and reasons for admission are listed.
- Check: withheld material and reasons are listed.
- Check: the packet/output boundary is stated.
- Check: human disposition is recorded where required.
- Check: the agent has not treated a disposition as a fact.
- Check: external action remains with the authorized human or system.

## P7. Learning

- Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE
- Evidence / receipt IDs:
- NOT_APPLICABLE reason:
- Learning status: LEARNING_PLANNED / LEARNING_PENDING_OUTCOME /
  LEARNING_REVIEWED / LEARNING_NOT_APPLICABLE
- Check: expectation is recorded before the outcome window.
- Check: outcome and attribution boundary are defined.
- Check: missing outcome and confounder states are allowed.
- Check: any update will be proposed and dispositioned, not silently applied.

## Preflight route table

| Failed or unknown check | Required record | Canonical route |
| --- | --- | --- |
| Permission or disclosure absent or revoked | NOT_AUTHORIZED | HOLD or ESCALATE |
| Permission or disclosure not established | UNKNOWN | HOLD or ESCALATE |
| High consequence plus missing support or baseline | INSUFFICIENT_SUPPORT or MISSING_BASELINE | HOLD or ESCALATE |
| Identity or provenance broken | EXCLUDE_FROM_INFLUENCE | HOLD or ESCALATE |
| One observation only for motion | NO_MOTION_CLAIM | ACQUIRE, ANSWER_PROVISIONALLY, or HOLD |
| No expected baseline for absence | NO_ABSENCE_CLAIM and observation boundary | CLARIFY, ANSWER_PROVISIONALLY, or HOLD |
| Budget or deadline reached | STOPPED_BUDGET or STOPPED_DEADLINE | ANSWER_PROVISIONALLY, HOLD, or DEFER |
| No later outcome defined | LEARNING_NOT_APPLICABLE | Any otherwise permitted route |
| Low consequence, reversible, supplied material only | ORDINARY_PATH | ANSWER |

## Preflight receipt

- Preflight ID:
- Decision ID / brief version:
- Operating level:
- PASS groups / evidence:
- FAIL groups / evidence:
- UNKNOWN groups / evidence:
- NOT_APPLICABLE groups / reason:
- Route: ACQUIRE / COMPARE / CLARIFY / ANSWER / ANSWER_PROVISIONALLY / HOLD /
  DEFER / ESCALATE / REFUSE
- Stop status: CONTINUE / COMPLETE / STOPPED_BUDGET / STOPPED_DEADLINE /
  STOPPED_OTHER
- Learning status: LEARNING_PLANNED / LEARNING_PENDING_OUTCOME /
  LEARNING_REVIEWED / LEARNING_NOT_APPLICABLE
- No-action boundary:
- Resume condition:
- Reviewer / escalation destination:
