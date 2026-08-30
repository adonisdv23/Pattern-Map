# Project-use starter

Status: **optional internal agent/operator cold-start wayfinding aid; not an
adoption or conformance standard, or proof of transfer**

Use this repository-local page when a materially different project needs to
enter v16 without first reading the whole repository. It is a thin wayfinding
adapter over the existing Quickstart, preflight, implementation choices, and
templates—not a portable packet or self-contained procedure. It adds no
family, route, score, ledger, permission, or authority.

## 1. Run Stage 0 first

Ask:

> Does the task require any material claim judgment, comparison, selection or
> withholding, permission resolution, memory reuse, new acquisition, externally
> consequential influence, or a separate human action gate, rather than only a
> reversible transformation of user-supplied material?

Ordinary is valid only for a reversible transformation of user-supplied
material that requires no material claim judgment, comparison, selection or
withholding, permission resolution, memory reuse, new acquisition, externally
consequential influence, or a separate human action gate.

**NO:** perform the reversible transformation and return only the four fields
in `framework/templates/ORDINARY_RECORD.md`: supplied scope, material
assumptions, unchecked boundaries, and output. The four-field ordinary record
is terminal; it is not an ANSWER, route, stop, learning, or influence receipt.
Do not fill the project context or create evidence/family records. Stage 0
grants no external-action authority; externally consequential action remains
with an explicitly authorized human.

**YES:** fill the context block below and choose the smallest layered route. A
single disqualifier is enough, including judgment or selection inside supplied
material. Do not promote a routine transformation merely because this page
exists.

## 2. Fill one context block (YES only)

These prompts map local facts to existing records; they are not a new receipt
shape. If a fact is missing, preserve its typed unknown or stop condition.

| Settle locally | Existing record | If missing |
| --- | --- | --- |
| Question, use, audience, consequence, reversibility, owner, reviewer, deadline, human action/disclosure gate | `framework/templates/DECISION_BRIEF.md` | `CLARIFY`, `HOLD`, or `ESCALATE`; a recommendation is not an action |
| Technical reach versus allowed read/transform/retain/disclose/act | Decision brief permission envelope | Preserve `UNKNOWN`, `NOT_AUTHORIZED`, or `REVOKED` with reason and resume condition |
| Default path, expected perspectives/fields/periods, baseline, cost, privacy, latency, reviewer attention, no-action boundary | Decision brief plus `framework/templates/ACQUISITION_RECEIPT.md` | No unsupported motion or absence claim; stop or narrow at the bound |
| Candidates, pointers, comparison, challenge | `framework/templates/EVIDENCE_REGISTER.md`, `framework/templates/COMPARISON_MATRIX.md`, `framework/templates/DISCONFIRMATION_LOG.md` | Keep unresolved material out of influence; use one bounded `NOT_APPLICABLE`/`SKIPPED` reason only when genuinely inactive |
| Selected/withheld material, memory, later outcome | `framework/templates/INFLUENCE_RECEIPT.md`, `framework/templates/MEMORY_RECORD.md`, `framework/templates/OUTCOME_REVIEW.md` | Keep unknown, unauthorized, stale, or superseded material from influence; use `LEARNING_NOT_APPLICABLE` when no outcome is defined |

Use only `AUTHORIZED`, `UNKNOWN`, `NOT_AUTHORIZED`, or `REVOKED` for
permission. The executable permission object uses only `technical_access`,
`state`, `scope`, `reason_code`, `reason`, and `resume_condition`; do not add
legacy authorization booleans. In the current single-global-permission
receipt, a blocked state leaves evidence, baseline, comparison,
disconfirmation, memory, and influence empty; records memory as `NOT_USED`;
and cannot acquire, disclose, reuse, or act through the blocked operation. It
routes to `HOLD`, `ESCALATE`, or the permitted refusal.

The context block's `permission_scope_and_state` is only a routing summary.
Before execution, complete the operation-level rows for read, acquire,
transform, retain/reuse, disclose, and act in the existing decision brief or
decision receipt. The complete useful-answer, abstention/escalation, and
level-fit fields also remain in `framework/templates/DECISION_BRIEF.md` and
`framework/IMPLEMENTATION_CHOICES.md`; this page does not replace them.

## 3. Choose the smallest layered route

Use the existing implementation choices; a higher level is not better. A
budget records capacity and constraint; it cannot independently justify
advanced machinery.

- `LIGHTWEIGHT`: bounded reversible work with only the minimum brief, alternate
  route, comparison/challenge, and influence record needed.
- `MODERATE`: work with high consequence or high uncertainty that does not
  meet the complete Advanced conjunction, including repeated or reviewed work
  needing stable IDs, versioning, correction, typed relationships, or a
  reproducible packet.
- `ADVANCED`: only the three-condition case below, with capabilities whose
  cost is justified.

Advanced is justified only when consequence is high, uncertainty is high, and
substantial capacity has been separately approved; volume, reuse, or longevity
may shape capabilities inside the chosen level but do not independently select
it.

## 4. Select only material family questions

The six-family map is orientation, not a completion checklist. Use a family
only when its question can change this decision; give one concise skip reason
and create no placeholder artifact when it cannot.

Use the records named above for only the material questions from F1 Peripheral
signal (default blind spots), F2 Source weighing (claim-scoped source roles),
F3 Velocity / motion (change against a baseline), F4 Absence + memory
(expected gaps and prior context), F5 Structured patterns (explicit
comparison), and F6 Learning loop (expectation, outcome, bounded update).

Keep recurrence, origin, support, authority, relevance, provenance, and
permission distinct. Peripheral is a candidate, recurrence is not independent
corroboration, and a failed capture is not absence.

## 5. Hand off to existing entry points

Copy this block into the existing Quickstart or decision brief after Stage 0
returns `YES`:

```text
PROJECT CONTEXT (fill after Stage 0 = YES)
project:
decision_question:
intended_use_and_audience:
consequence_and_reversibility:
decision_owner_and_reviewer:
human_action_boundary:
deadline_and_outcome_window:
supplied_material_refs:
default_path_and_expected_baseline:
permission_scope_and_state:
cost_and_no_action_boundary:
known_unknowns_and_non_applicable_checks:
likely_families_and_one_line_reasons:
resume_or_escalation_condition:
```

Then open only the records named by the chosen route. Use
`framework/agent-playbook/QUICKSTART.md` for the sequence,
`framework/agent-playbook/PREFLIGHT_CHECKLIST.md` for status evidence, and
`framework/IMPLEMENTATION_CHOICES.md` when level or stopping is unclear. Use
the full guide and decision receipt only when the decision warrants their
detail. Keep route (`ACQUIRE`, `COMPARE`, `CLARIFY`, `ANSWER`,
`ANSWER_PROVISIONALLY`, `HOLD`, `DEFER`, `ESCALATE`, `REFUSE`) separate from
stop (`CONTINUE`, `COMPLETE`, `STOPPED_BUDGET`, `STOPPED_DEADLINE`,
`STOPPED_OTHER`) and learning (`LEARNING_PLANNED`, `LEARNING_PENDING_OUTCOME`,
`LEARNING_REVIEWED`, `LEARNING_NOT_APPLICABLE`).

## 6. Fail closed and stop cleanly

- Missing or unclear authority is not permission; missing baseline is not
  motion or absence.
- A dangling evidence, comparison, disconfirmation, influence, or memory link
  stays out of the answer.
- External action remains with the explicitly authorized human.
- This page makes the first transfer legible; it does not establish that a
  future project, agent, case, or product will follow the procedure or improve
  a decision.
