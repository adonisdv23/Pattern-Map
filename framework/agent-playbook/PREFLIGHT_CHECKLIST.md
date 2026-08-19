# Agent preflight checklist

Run this checklist before acquisition, enrichment, or a consequential answer.
Mark PASS, FAIL, UNKNOWN, or NOT_APPLICABLE. An UNKNOWN required field is not a
silent pass.

## P0. Scope and decision

- [ ] The real decision is stated in one sentence.
- [ ] Intended use and audience are stated.
- [ ] Consequence and reversibility are stated.
- [ ] Decision owner and required reviewer are named.
- [ ] Deadline and outcome window are stated or marked NOT_APPLICABLE.
- [ ] Answer, abstention, hold, and escalation conditions are stated.

## P1. Permission

- [ ] Technical access is listed separately from operational authorization.
- [ ] Acquisition permission is explicit for each source class.
- [ ] Transformation, retention, disclosure, and reuse permissions are explicit.
- [ ] Paid, private, sensitive, or external operations have named authority.
- [ ] External action is outside the agent’s authority unless explicitly
      delegated and still has a human boundary.

FAIL or UNKNOWN on a consequential permission item means:
STOP — NOT_AUTHORIZED_OR_AMBIGUOUS. Do not acquire, disclose, or act. Record
the escalation destination and the condition needed to resume.

## P2. Cost and stop

- [ ] Time and deadline are bounded.
- [ ] Money and paid retrieval are bounded.
- [ ] Model, token, and compute use are bounded.
- [ ] Reviewer attention and privacy exposure are bounded.
- [ ] One-more-action benefit is described qualitatively.
- [ ] Hard and soft stop rules are written.
- [ ] Budget exhaustion will be recorded as STOPPED_BUDGET, not sufficiency.

## P3. Information boundary

- [ ] Default query, source set, vocabulary, and time window are recorded.
- [ ] At least one bounded alternate route is planned when the decision needs
      breadth.
- [ ] Expected perspectives, fields, peers, or periods are listed.
- [ ] A failed capture will not be treated as absence.
- [ ] Source, artifact, version, event time, capture time, and exact span can be
      recorded, or their absence is explicitly acknowledged.

## P4. Comparison and claims

- [ ] The answer is decomposed into narrow claims.
- [ ] Each influential claim has an exact evidence pointer or is marked
      unsupported/provisional.
- [ ] Source role and claim-scoped authority are separate from support.
- [ ] Recurrence and origin are separate from independence.
- [ ] A comparison unit and baseline are stated where needed.
- [ ] Motion has repeated comparable observations.
- [ ] Absence has an explicit expected baseline and observation boundary.
- [ ] Incomparable and unknown relations remain visible.

## P5. Disconfirmation and uncertainty

- [ ] The leading interpretation is written.
- [ ] The strongest contrary or limiting search is planned or completed.
- [ ] A missing perspective or field is checked.
- [ ] Alternative explanation, measurement change, or common origin is checked
      where applicable.
- [ ] Unknown, contested, stale, insufficient, failed, and unauthorized states
      are typed rather than collapsed into confidence.

## P6. Influence and human control

- [ ] Selected material and reasons for admission are listed.
- [ ] Withheld material and reasons are listed.
- [ ] The packet/output boundary is stated.
- [ ] Human disposition is recorded where required.
- [ ] The agent has not treated a disposition as a fact.
- [ ] External action remains with the authorized human or system.

## P7. Learning

- [ ] Expectation is recorded before the outcome window.
- [ ] Outcome and attribution boundary are defined.
- [ ] Missing outcome and confounder states are allowed.
- [ ] Any update will be proposed and dispositioned, not silently applied.

## Preflight route table

| Failed or unknown check | Route |
| --- | --- |
| Permission or disclosure | NOT_AUTHORIZED_OR_AMBIGUOUS → HOLD / ESCALATE |
| High consequence plus missing support or baseline | HOLD / ESCALATE |
| Identity or provenance broken | EXCLUDE_FROM_INFLUENCE → HOLD / ESCALATE |
| One observation only for motion | NO_MOTION_CLAIM → acquire another point or answer with limitation |
| No expected baseline for absence | NO_ABSENCE_CLAIM → state observation boundary |
| Budget or deadline reached | STOPPED_BUDGET or STOPPED_DEADLINE |
| No later outcome defined | LEARNING_NOT_APPLICABLE, not a failed result |
| Low consequence, reversible, supplied material only | LIGHTWEIGHT or ORDINARY_PATH |

## Preflight receipt

- Preflight ID:
- Decision ID / brief version:
- Operating level:
- Failed or unknown checks:
- Route:
- No-action boundary:
- Resume condition:
- Reviewer / escalation destination:
