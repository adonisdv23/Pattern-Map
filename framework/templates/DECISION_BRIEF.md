# Decision brief

Status: fill before nontrivial acquisition or enrichment.

## Identity

- Decision ID:
- Brief version:
- Date/time and timezone:
- Decision owner:
- Operator or agent:
- Reviewer / escalation destination:

## Decision

- Real question:
- Intended use:
- Audience:
- Consequence level: LOW / MEDIUM / HIGH / UNKNOWN
- Reversibility:
- Deadline:
- What a useful answer must contain:
- What would require abstention or escalation:

## Permission envelope

| Operation | Technical access | Permission state | Scope | Reason code | Reason | Resume condition |
| --- | --- | --- | --- | --- | --- | --- |
| Read supplied material |  |  |  |  |  |  |
| Acquire public material |  |  |  |  |  |  |
| Acquire private, paid, or sensitive material |  |  |  |  |  |  |
| Transform, summarize, or classify |  |  |  |  |  |  |
| Retain or reuse as memory |  |  |  |  |  |  |
| Disclose in answer or packet |  |  |  |  |  |  |
| Act on an external system or person |  |  |  |  |  |  |

Technical access is not permission. Use `AUTHORIZED`, `UNKNOWN`,
`NOT_AUTHORIZED`, or `REVOKED`; do not collapse an unestablished permission, an
absent/denied permission, and a revoked prior permission. Every blocked state
needs its own reason and resume condition. Unknown, absent, or revoked
permission routes to HOLD or ESCALATE for consequential work.

An executable permission object has exactly `technical_access`, `state`,
`scope`, `reason_code`, `reason`, and `resume_condition`. Reject extra legacy
authorization booleans. In this template's single-global-permission form, a
blocked state means no evidence, baseline, comparison, disconfirmation,
memory, or influence record is populated and memory remains `NOT_USED`.

## Baseline and expected coverage

- Default information path:
- Expected sources, perspectives, fields, or periods:
- Comparison set:
- Expected baseline for motion:
- Expected baseline for absence:
- Known exclusions or observation limits:

## Cost boundary

- Time:
- Money / paid retrieval:
- Model tokens / compute:
- Reviewer attention:
- Privacy / security exposure:
- Latency:
- No-action boundary:

## Route policy

- Allowed routes: ACQUIRE / COMPARE / CLARIFY / ANSWER /
  ANSWER_PROVISIONALLY / HOLD / DEFER / ESCALATE / REFUSE
- Hard stop conditions:
- Soft stop conditions:
- Resume condition, if held or deferred:

## Outcome plan

- Learning status: LEARNING_PLANNED / LEARNING_PENDING_OUTCOME /
  LEARNING_NOT_APPLICABLE
- Expected outcome or abstention condition:
- Measurement window:
- Attribution boundary:
- Missing-outcome state:

## Change log

- Version:
- Changed field:
- Reason:
- Disposition:
