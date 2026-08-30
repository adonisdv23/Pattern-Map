# Agent preflight checklist

Run this checklist before acquisition, enrichment, or a consequential answer.
For every P-group, record `PASS`, `FAIL`, `UNKNOWN`, or `NOT_APPLICABLE`, plus
the evidence/receipt IDs that justify the status. `NOT_APPLICABLE` requires a
reason. An `UNKNOWN` required field is not a silent pass.

Ordinary is valid only for a reversible transformation of user-supplied
material that requires no material claim judgment, comparison, selection or
withholding, permission resolution, memory reuse, new acquisition, or
externally consequential influence. Only that task bypasses this layered
preflight. The four-field ordinary record is terminal; it is not an ANSWER,
route, stop, learning, or influence receipt. Stage 0 grants no external-action
authority; externally consequential action remains with an explicitly
authorized human.

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
- Check: executable permission uses only `technical_access`, `state`, `scope`,
  `reason_code`, `reason`, and `resume_condition`; contradictory legacy
  authorization booleans are absent there and at receipt top level.

FAIL or UNKNOWN on a consequential permission item means a hard stop, then
route `HOLD` or `ESCALATE`. Record `NOT_AUTHORIZED` when permission is absent
or denied, `UNKNOWN` when it has not been established, and `REVOKED` when a
previous authorization no longer applies. Do not collapse those states,
acquire, disclose, reuse, or act. Record the state-specific reason, escalation
destination, and condition needed to resume. In the current global-permission
receipt, each blocked state also requires empty evidence, baseline, comparison,
disconfirmation, memory, and influence, with memory `NOT_USED`.

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
- Check: motion names at least two distinct authorized observation IDs whose
  timestamps parse as at least two distinct real UTC-Z instants under one
  alignment key; a count alone is insufficient.
- Check: absence has an explicit expected baseline and observation boundary.
- Check: incomparable and unknown relations remain visible.
- Check: an answer route has substantive linked comparison records or
  `NOT_APPLICABLE` plus one bounded reason and no placeholder record.

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
- Check: an answer route has substantive linked disconfirmation records or
  `SKIPPED` plus one bounded reason and no placeholder record.

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
- Check: selected memory is `CURRENT` and `AUTHORIZED`; superseded versions are
  preserved only as withheld history.

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
| Permission or disclosure absent or denied | NOT_AUTHORIZED | HOLD or ESCALATE |
| Permission or disclosure not established | UNKNOWN | HOLD or ESCALATE |
| Previous permission revoked | REVOKED | HOLD or ESCALATE |
| High consequence plus missing support or baseline | INSUFFICIENT_SUPPORT or MISSING_BASELINE | HOLD or ESCALATE |
| Identity or provenance broken | EXCLUDE_FROM_INFLUENCE | HOLD or ESCALATE |
| Fewer than two distinct authorized time-bearing refs share one motion alignment key | NO_MOTION_CLAIM | ACQUIRE, ANSWER_PROVISIONALLY, or HOLD |
| No expected baseline for absence | NO_ABSENCE_CLAIM and observation boundary | CLARIFY, ANSWER_PROVISIONALLY, or HOLD |
| Budget or deadline reached | STOPPED_BUDGET or STOPPED_DEADLINE | ANSWER_PROVISIONALLY, HOLD, or DEFER |
| No later outcome defined | LEARNING_NOT_APPLICABLE | Any otherwise permitted route |

The ordinary supplied-material path does not enter this table: it returns the
four-field ordinary record and stops before the layered route vocabulary.

## Layered preflight receipt

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
