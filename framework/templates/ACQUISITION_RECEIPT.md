# Acquisition receipt

One receipt records one route, query, capture attempt, or bounded stop.

## Identity

- Receipt ID:
- Decision ID / brief version:
- Route type: DEFAULT / PERIPHERAL / GAP-FILL / DISCONFIRMATION /
  COMPARISON / MEMORY
- Operator / tool:
- Started / ended:

## Proposal

- What uncertainty or baseline gap could this reduce?
- Why the default path was insufficient:
- Source or route targeted:
- Query / operation:
- Expected information benefit: HIGH / MEDIUM / LOW / UNKNOWN
- Expected cost:
- Stop condition:

## Permission

- Technical access:
- Permission state: AUTHORIZED / UNKNOWN / NOT_AUTHORIZED / REVOKED
- Permission scope:
- Permission reason code: AUTHORIZED_FOR_PURPOSE / PERMISSION_NOT_ESTABLISHED /
  PERMISSION_ABSENT / PERMISSION_REVOKED
- Permission reason:
- Resume condition if unresolved, absent, or revoked:
- Sensitive or paid material involved:
- Retention and disclosure allowed:
- Human approval required:
- Approval reference:

The executable permission object uses only `technical_access`, `state`,
`scope`, `reason_code`, `reason`, and `resume_condition`. Do not add an
`authorized`, `permission_granted`, or similar boolean that can contradict the
typed state. Approval metadata belongs outside that object.

## Result

- Capture status: CAPTURED / PARTIAL / NOT_FOUND / FAILED / NOT_AUTHORIZED /
  PERMISSION_UNKNOWN / PERMISSION_REVOKED
- Stop status: CONTINUE / COMPLETE / STOPPED_BUDGET / STOPPED_DEADLINE /
  STOPPED_OTHER
- Source ID:
- Artifact ID:
- Version or digest:
- Capture time:
- Event time:
- Exact pointer or span:
- Transformation / parser / tool version:
- Failure class, if any:
- What this result does not establish:

## Route decision

- Remaining budget:
- Next route: ACQUIRE / COMPARE / CLARIFY / ANSWER /
  ANSWER_PROVISIONALLY / HOLD / DEFER / ESCALATE / REFUSE
- Reason:
- Uncertainty preserved:
- Reviewer / disposition:
