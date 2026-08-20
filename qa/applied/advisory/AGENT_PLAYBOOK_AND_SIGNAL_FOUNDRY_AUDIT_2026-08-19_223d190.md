# Agent playbook and Signal Foundry audit

Status: ADVISORY / READ-ONLY REVIEW / NOT EVIDENCE OF EFFECTIVENESS

Reviewed snapshot: `223d19069a3d61069c3eedec64e6ccdd38852dff` (`223d190`),
committed 2026-08-19 as “Build v16 applied framework and agent playbook”.

Scope: `framework/**`, `cases/**`, the locked v16 contracts, and the
manuscript passages needed to check consistency. This review used
checkout-independent reads of the named snapshot. It did not call a provider,
inspect private Signal Foundry material, run a study, or treat fixtures,
procedures, or structural QA as empirical evidence.

## Overall verdict

**PASS WITH REVISIONS.**

The snapshot is substantively useful and is close to satisfying the applied
lane. The full operating guide, templates, two domain-neutral fixtures, and
ordinary-versus-layered examples give an agent observable ways to acquire,
compare, challenge, preserve uncertainty, escalate, stop, record influence,
and learn. The implementation spectrum is stack-neutral and explicitly tells
operators when to stay ordinary or lightweight. Signal Foundry is clearly
marked as read-only, illustrative, and not validation; it is serious enough to
serve as a translation case.

Acceptance is not yet clean because four small but material execution gaps
remain. The Quickstart records a future expectation but does not tell a
Quickstart-only operator how to close the learning loop. Route and stop
vocabulary differs between the Quickstart, full guide, preflight, and receipt
templates. The preflight says to mark statuses but its checkbox form does not
capture those statuses in an inspectable way. Signal Foundry refers to a cost
boundary without defining the illustrative cost, stop, or resume envelope.
These are bounded documentation/template revisions, not a request for a new
architecture or a change to owner intent.

## Governing gates checked

| Gate | Assessment | Evidence and consequence |
| --- | --- | --- |
| A07 — concrete implementation paths | Pass with APP-04 revision | `framework/IMPLEMENTATION_CHOICES.md:1-13` names lightweight, moderate, and advanced paths with inputs, outputs, cost, stop, and risks; `:15-34` supplies a minimum lightweight route; `:86-94` and `framework/BOUNDARIES_AND_FAILURES.md:104-122` say when not to use the full framework. The general implementation choices pass. Signal Foundry’s applied route is the remaining cost/stop completeness issue. |
| A08 — observable agent behavior | Pass with APP-01–APP-03 revisions | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:97-286` and the templates provide the required procedures and records. The Quickstart and preflight are the intended low-friction entry points, so their learning and status omissions matter even though the full guide is complete. |
| A09 — Signal Foundry bounded, not validation | Pass on claim boundary; revise bounded procedure | `cases/signal-foundry/README.md:1-15` explicitly says `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, no runtime/data/provider work was performed, and all rows are fixtures. `:159-168` repeats the boundary that must travel with links. APP-04 concerns whether the case is operationally bounded, not whether it overclaims validation. |

The governing requirements are `docs/V16_ACCEPTANCE_CRITERIA.md:19-21`,
`docs/OWNER_INTENT_V16.md:116-142`, and the agent-companion firebreak in
`docs/ARTIFACT_BOUNDARIES.md:14-15`.

## Procedure execution audit

| Required procedure | Mental execution result | Snapshot evidence |
| --- | --- | --- |
| Acquisition | **Pass.** An agent can name the gap, default-route reason, permission, source/artifact identity, version, exact span, result/failure, cost, remaining budget, and next route. Failed capture is kept separate from absence. | `framework/agent-playbook/QUICKSTART.md:17-29`; `framework/agent-playbook/FULL_OPERATING_GUIDE.md:97-112`; `framework/templates/ACQUISITION_RECEIPT.md:14-54` |
| Comparison | **Pass.** The guide requires a declared peer/period/attribute/structure/origin unit, aligned definitions and denominators, and visible `INCOMPARABLE`/`UNKNOWN` states. The examples show how recurrence and common origin alter interpretation without erasing observations. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:131-146`; `framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md:36-63`; `cases/general-research/README.md:42-61` |
| Disconfirmation | **Pass.** The leading interpretation, weakening condition, contrary route, missing perspective, alternative explanation/measurement change, shared origin, result, and remaining uncertainty are all specified. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:174-186`; `framework/templates/DISCONFIRMATION_LOG.md:1-29`; `cases/product-and-process/README.md:62-75` |
| Uncertainty | **Pass.** The guide has typed states such as `UNKNOWN`, `INSUFFICIENT_SUPPORT`, `UNKNOWN_ORIGIN`, `MISSING_BASELINE`, `FAILED_CAPTURE`, `NOT_AUTHORIZED`, and `OUTCOME_MISSING`, and says what could reduce each uncertainty. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:188-206`; `framework/agent-playbook/PREFLIGHT_CHECKLIST.md:61-69` |
| Escalation and human authority | **Pass.** Permission ambiguity, critical gaps, conflicts, identity/provenance problems, policy/memory changes, and external consequences route to hold/escalation. The escalation record asks the human a concrete question and names the no-action and resume conditions. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:44-56`, `:208-225`, `:251-264`; `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:123-132`; `cases/signal-foundry/README.md:55-68` |
| Cost | **Pass for the core framework.** The implementation levels and full guide name time, money, tokens/compute, reviewer attention, privacy/retention/disclosure, latency, route count/retries, and consequence. Qualitative benefit bands avoid invented precision. | `framework/IMPLEMENTATION_CHOICES.md:7-13`, `:54-71`; `framework/BOUNDARIES_AND_FAILURES.md:72-102`; `framework/agent-playbook/FULL_OPERATING_GUIDE.md:58-73` |
| Stop and resume | **Pass with APP-02 vocabulary revision.** Hard stops, soft stops, remaining uncertainty, no-action boundaries, and resume conditions are concrete. The route names are not consistently shared by the Quickstart, full guide, preflight, and templates. | `framework/BOUNDARIES_AND_FAILURES.md:30-70`; `framework/agent-playbook/FULL_OPERATING_GUIDE.md:208-225`; `framework/agent-playbook/QUICKSTART.md:33-37`, `:58-68` |
| Influence recording | **Pass.** Selected and withheld items, exact spans, claim roles, admission reasons, limits, permission, disclosure, and reviewer disposition are explicit. The output must separate observation, interpretation, recommendation, unknown, and human action. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:227-249`; `framework/templates/INFLUENCE_RECEIPT.md:1-45`; `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:86-110` |
| Learning | **Pass in the full guide and cases; Quickstart needs APP-01.** The full guide preserves the original receipt, compares expected and observed outcomes, records cost/corrections/context/confounders, proposes one bounded update, and requests disposition. The Quickstart’s minimum output stops at recording an expectation. | `framework/agent-playbook/FULL_OPERATING_GUIDE.md:266-286`; `framework/templates/OUTCOME_REVIEW.md:1-50`; `framework/agent-playbook/QUICKSTART.md:41-56`; `cases/general-research/README.md:77-89` |

## Findings

### APP-01 — Quickstart does not close the learning loop

Severity: **Medium**

Type: factual acceptance gap / usability risk

Evidence:

- The Quickstart’s minimum output asks for “an outcome expectation when later
  learning is possible” (`framework/agent-playbook/QUICKSTART.md:41-52`) but
  does not instruct the operator to capture the later outcome, compare it with
  the expectation, propose an update, or obtain disposition.
- The full guide does specify those actions, including preserving the original
  brief, packet, and receipt (`framework/agent-playbook/FULL_OPERATING_GUIDE.md:266-286`),
  and the outcome template provides the fields (`framework/templates/OUTCOME_REVIEW.md:22-50`).

Why it matters: A user who follows the advertised short path can leave a
forward-looking expectation with no defined close-out action. That fails the
literal A08 requirement that the Quickstart and full guide define artifacts and
actions for learning (`docs/V16_ACCEPTANCE_CRITERIA.md:20`). It also makes a
future outcome harder to compare without hindsight, despite the owner contract
requiring comparison with expectations and bounded updates
(`docs/OWNER_INTENT_V16.md:124-142`).

Recommended bounded change: add one sentence to the Quickstart’s minimum output
or Step 10: “If a later outcome is defined, preserve the original expectation,
compare observed outcome/cost/corrections/context with it after the outcome
window, propose one bounded update, and request human disposition; otherwise
record `LEARNING_NOT_APPLICABLE`.” Point to `OUTCOME_REVIEW.md`. This adds no
new artifact class and does not make learning mandatory for ordinary tasks.

Suggested disposition: **Accepted with revision**. A re-read of the Quickstart
and one fixture should verify that the close-out is visible.

### APP-02 — Route and stop vocabulary is not interoperable across artifacts

Severity: **Medium**

Type: factual consistency defect / observability risk

Evidence:

- Quickstart Step 9 says “answer, provisional answer, hold, defer, escalate,
  refuse, or one more bounded action” (`framework/agent-playbook/QUICKSTART.md:33-37`);
  it does not name `ACQUIRE`, `COMPARE`, or `CLARIFY`, and “one more bounded
  action” is not a reviewable route value.
- The full guide’s route table names `ACQUIRE`, `COMPARE`, `CLARIFY`,
  `ANSWER`, `ANSWER_PROVISIONALLY`, `HOLD`, `DEFER`, `ESCALATE`, `REFUSE`,
  `STOPPED_BUDGET`, and `STOPPED_OTHER` (`framework/agent-playbook/FULL_OPERATING_GUIDE.md:208-225`).
- The decision receipt instead offers `STOPPED_BUDGET` and
  `STOPPED_DEADLINE`, but not `STOPPED_OTHER` (`framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:75-84`);
  the acquisition receipt has `STOPPED_OTHER` and a `STOP` next-route value
  (`framework/templates/ACQUISITION_RECEIPT.md:33-54`). The relationship map
  also uses `abstain` as a route label (`framework/RELATIONSHIP_MAP.md:30-39`),
  while the full guide does not define it as a route.

Why it matters: An agent can follow the prose and produce a route that cannot
be recorded consistently in the prescribed receipt. That undermines the
agent-observability firebreak, even though the underlying stop logic is sound.
It also makes “cost/stop” harder to compare across cases and QA fixtures.

Recommended bounded change: establish one canonical route vocabulary and one
separate stop-status vocabulary. For example, use routes
`ACQUIRE | COMPARE | CLARIFY | ANSWER | ANSWER_PROVISIONALLY | HOLD | DEFER |
ESCALATE | REFUSE`, and statuses `STOPPED_BUDGET | STOPPED_DEADLINE |
STOPPED_OTHER | LEARNING_NOT_APPLICABLE`; map `abstain` to an explicitly chosen
route or remove the alias. Update the Quickstart, full guide, preflight route
table, decision receipt, acquisition receipt, relationship map, and fixture
references together. Keep “one more bounded action” only as explanatory prose,
not as an untyped output.

Suggested disposition: **Accepted with revision**. This is a vocabulary
alignment, not a request to add workflow machinery.

### APP-03 — Preflight status instruction is not captured by the checklist shape

Severity: **Medium**

Type: observability/usability risk

Evidence:

- The preflight says to mark every item `PASS`, `FAIL`, `UNKNOWN`, or
  `NOT_APPLICABLE` (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:1-5`).
- The actual P0–P7 items are bare checkboxes (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:7-85`),
  so `[x]` records only that a box was touched; it does not distinguish a
  passing check from an unknown, failed, or not-applicable check.
- The preflight receipt records only “failed or unknown checks,” route,
  boundary, resume condition, and reviewer (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:100-109`);
  it does not preserve the status/evidence for all required checks.

Why it matters: A reviewer cannot reliably tell whether an omitted status was a
pass, a deliberate `NOT_APPLICABLE`, or an unexamined field. The full guide and
decision receipt are inspectable, but the required preflight artifact is the
entry point for the agent companion and is explicitly expected to expose
observable behavior under A08 (`docs/V16_ACCEPTANCE_CRITERIA.md:20`).

Recommended bounded change: give each check (or each P-group, if keeping the
short form) a compact `Status: PASS | FAIL | UNKNOWN | NOT_APPLICABLE` field and
an optional evidence/receipt ID. Add a `NOT_APPLICABLE reason` field and a
`PASS checks / evidence` summary to the preflight receipt. Keep the existing
hard-stop rule and allow the ordinary path to bypass preflight when the
ordinary-path condition is explicitly recorded.

Suggested disposition: **Accepted with revision**. The smallest fix is a
status column or status token beside each existing checkbox; no new database or
workflow is needed.

### APP-04 — Signal Foundry invokes a cost boundary without defining it

Severity: **Medium**

Type: bounded-translation completeness risk; not a validation claim

Evidence:

- The case is commendably explicit that it is a fixture-only, read-only,
  non-validation translation and that no runtime code, data, credentials,
  provider calls, or external content are present (`cases/signal-foundry/README.md:1-15`).
- Its bounded decision and permission envelope define allowed/unavailable
  operations (`cases/signal-foundry/README.md:43-68`), and the read-only
  procedure says to route “under the cost boundary” (`cases/signal-foundry/README.md:124-146`).
- However, the case has no cost-boundary section or field: no limit for
  enrichment attempts, reviewer attention, paid retrieval (beyond the general
  no-provider statement), pointer/fixture handling, or latency; and no explicit
  hard/soft stop or resume condition for the packet route. This is notable
  because the case workspace promises that every case states evidence,
  permission, and stop logic (`cases/README.md:16-17`).

Why it matters: The six-family translation and packet trace are serious, and
the non-validation boundary is clear, but an operator cannot actually decide
when to stop a future enrichment/compare route or what cost is authorized from
this case alone. The omission weakens the “bounded applied illustration” and
the builder-facing cost/stop requirement (`docs/V16_ACCEPTANCE_CRITERIA.md:19-21`)
without implying any product fact.

Recommended bounded change: add an explicitly illustrative “Cost and stop
envelope” after the permission table. It can remain fixture-scoped, for
example: supplied case rows only; zero provider calls or paid retrieval; one
bounded packet pass; one accountable reviewer; no external disclosure or
runtime change; hard-stop on missing/ambiguous permission, identity/capture
failure, or external action; soft-stop after the declared packet/alternate
route pass; resume only on a named human authorization or a supplied pointer.
State that these are case controls, not Signal Foundry product requirements.
Then reference the envelope from Step 10 and the footer/link boundary.

Suggested disposition: **Accepted with revision**. This preserves the case’s
strong non-validation language and adds only the missing execution boundary.

## What passes without revision

### Implementation options remain bounded and non-bureaucratic

The implementation table gives each level a best-fit use, inputs, outputs,
typical cost, stop condition, and main risk (`framework/IMPLEMENTATION_CHOICES.md:7-13`).
The lightweight route is explicitly documents/no-new-software and requires
only a small set of records (`framework/IMPLEMENTATION_CHOICES.md:15-34`).
Moderate and advanced paths are described as choices rather than a mandatory
stack, and the selection rubric explicitly says to stay lightweight or not use
the framework for creative transformations, disposable work, supplied-context
formatting, or cases where recording costs more than the consequence
(`framework/IMPLEMENTATION_CHOICES.md:36-94`). The failure document reinforces
that the framework should improve proportion rather than become mandatory
bureaucracy (`framework/BOUNDARIES_AND_FAILURES.md:104-122`).

### Ordinary-versus-layered examples teach observable differences

The side-by-side table distinguishes default search, source identity, repeated
reports, gaps, motion, uncertainty, stopping, influence, and later learning
(`framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md:8-21`). The four
examples then show when the ordinary path is correct, how a repeated-claim
route traces origin, how a motion/absence route preserves baseline uncertainty,
and how permission blocks a private-list/external-send request
(`framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md:23-114`). The
general-research and product/process fixtures reinforce these distinctions with
invented, non-empirical records and human authority boundaries
(`cases/general-research/README.md:1-9`, `:42-89`; `cases/product-and-process/README.md:1-8`,
`:41-89`). These are illustrations, not claims that the procedures improve
decisions.

### Signal Foundry is serious and explicitly not validation

The case maps all six families to concrete evidence classes, required records,
and boundaries (`cases/signal-foundry/README.md:70-91`), then supplies an
inspectable packet trace with selected, qualified, withheld, and held items
(`cases/signal-foundry/README.md:93-122`). Its final boundary section says the
case does not establish an implemented handoff or runtime behavior and that no
row grants permission to scrape, disclose, purchase, contact, deploy, or act
(`cases/signal-foundry/README.md:159-168`). The residual risks even name
overfitting the transcript-first case at `:170-179`, which helps preserve the
broader six-family scope. APP-04 is therefore a boundedness-completeness fix,
not a concern that the case is pretending to be product evidence.

## Handoff note

The primary integrator should disposition APP-01 through APP-04 using the
controlled categories in `docs/REVIEW_AND_DISPOSITION_PROTOCOL.md:25-36`, then
re-run the narrow artifact/receipt checks and re-read the changed Quickstart,
preflight, route vocabulary, and Signal Foundry case. No owner-intent change is
needed or proposed. This report itself is advisory work product and must not be
used as evidence that the playbook, Signal Foundry, or any case improves
decisions.
