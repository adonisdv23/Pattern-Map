# Applied post-revision verification

Status: **ADVISORY / READ-ONLY REVIEW / NOT EVIDENCE OF EFFECTIVENESS**

Target snapshot: `cd8a7562437116af097f54d0e71de5cce37727e7` (short form
`cd8a756`), committed 2026-08-19 as “Tighten applied playbook after advisory
audits”. All target-file evidence below was read checkout-independently with
`git show cd8a756:<path>`; the target was not checked out or modified. No
provider, model, external system, private Signal Foundry material, paid
retrieval, or empirical work was used.

The focused QA command was also run against the unchanged applied-framework
tree and returned:

```text
PASS  six-family JSON and schema contract
PASS  artifact inventory and boundary language
PASS  receipt fixtures through preflight/stop logic
PASS  focused applied QA complete (structural/procedural only)
```

The validator’s own scope is structural and procedural only: it explicitly says
it does not execute a model, provider, study, or external action
(`qa/applied/validate_framework.py:1-7`), and the QA README says its checks do
not show that the framework improves decisions or that a case works in
production (`qa/applied/README.md:1-26`). The pass above is therefore not an
effectiveness result.

## Overall gate recommendation

**PASS WITH ONE BOUNDED REVISION.**

APP-01, APP-03, APP-04, and V13-05 are resolved at the target snapshot. The
agent entry points, canonical route/stop/learning definitions, receipt fixtures,
and structural validator now agree. The only remaining issue is a narrow,
literal APP-02 interoperability residue: two changed conceptual/case artifacts
still use local labels (`provisional packet`, `packet`, and `escalation`) under a
`Route` heading without mapping them to the canonical route values. This does
not introduce a new workflow, product claim, validation claim, or bureaucracy,
but it prevents a clean “all changed canonical artifacts” pass until the labels
are mapped or explicitly marked as output labels rather than route values.

The acceptance-gate reading is therefore:

| Gate | Recommendation | Reason |
| --- | --- | --- |
| A07 — concrete implementation paths | **Pass** | The implementation spectrum has bounded inputs, outputs, cost, stop, risks, and when-not-to-use guidance; the V13 continuity sentence is now explicit. |
| A08 — observable agent behavior | **Pass with APP-02 revision** | Quickstart learning close-out, inspectable preflight groups, canonical core vocabulary, receipt semantics, and fixture checks are present; the relationship diagram and Signal Foundry procedure retain two local route-label aliases. |
| A09 — Signal Foundry bounded, not validation | **Pass** | The case now has a concrete fixture-only cost/stop/resume envelope and retains explicit read-only, illustrative, and non-validation boundaries. |

The recommended disposition is **Accepted with revision** for APP-02 only;
the other findings can be marked **Accepted** under the controlled dispositions
in `docs/REVIEW_AND_DISPOSITION_PROTOCOL.md:25-36`. The remaining revision is a
copy-level mapping, not an architecture or product decision.

## Verdict summary

| ID | Severity | Verdict at `cd8a756` | Acceptance gate | Short reason |
| --- | --- | --- | --- | --- |
| APP-01 | Medium | **Resolved** | A08; owner learning requirement | Quickstart now tells the operator how to preserve, compare, update, and disposition a later outcome, while allowing ordinary tasks to omit learning. |
| APP-02 | Medium | **Unresolved — narrow residual** | A08; agent-companion firebreak | Core playbook, templates, fixtures, and validator interoperate, but `RELATIONSHIP_MAP.md` and Signal Foundry Step 10 still use unmapped local route labels. |
| APP-03 | Medium | **Resolved** | A08; inspectability | Every P-group has a visible status/evidence/reason shape, and the receipt preserves grouped status evidence and NOT_APPLICABLE reasons. |
| APP-04 | Medium | **Resolved** | A07 and A09 | Signal Foundry now states material, acquisition, work, reviewer, disclosure, latency, hard-stop, soft-stop, and resume limits, explicitly as fixture controls. |
| V13-05 | Low | **Resolved** | A07; v13 continuity recommendation | `IMPLEMENTATION_CHOICES.md` explicitly maps levels to team process, intermediary context/evidence workflow, and optionally approved model adaptation without hierarchy. |

## APP-01 — Quickstart learning close-out

**Verdict: RESOLVED.**

**Acceptance gate:** A08 requires the Quickstart and full guide to define
observable artifacts/actions for learning (`docs/V16_ACCEPTANCE_CRITERIA.md:19-21`).
The owner contract also requires comparing later outcomes with expectations and
proposing bounded updates (`docs/OWNER_INTENT_V16.md:122-143`).

**Evidence:**

- The Quickstart minimum output now distinguishes a locked future outcome from a
  proposed route and from no applicable outcome: it requires an outcome window
  and `LEARNING_PENDING_OUTCOME`, reserves `LEARNING_PLANNED` for an unlocked
  proposal, and allows `LEARNING_NOT_APPLICABLE` with a reason
  (`framework/agent-playbook/QUICKSTART.md:43-56`).
- The Quickstart-only operator is explicitly told what happens after the window:
  preserve the expectation; compare observed outcome, actual cost, corrections,
  and context; propose one bounded update; request human disposition; record
  `LEARNING_REVIEWED`; and use `OUTCOME_REVIEW.md`
  (`framework/agent-playbook/QUICKSTART.md:58-64`). It also explicitly says
  learning is not mandatory for an ordinary-path task (`:63-64`).
- The full guide defines the four learning states and their transitions: planned
  before the expectation/window is locked, pending once they are recorded,
  reviewed only after outcome review and disposition, and not-applicable when
  there is no defined later outcome (`framework/agent-playbook/FULL_OPERATING_GUIDE.md:281-307`).
- The outcome template links the original route and influence receipts, records
  the predeclared expectation and observed outcome/cost/context, and requires a
  proposed bounded update plus `LEARNING_REVIEWED` after disposition
  (`framework/templates/OUTCOME_REVIEW.md:5-14`, `:23-52`).
- The validator checks both the Quickstart close-out text and its outcome-review
  link (`qa/applied/validate_framework.py:218-223`). Its fixture validator
  requires a canonical learning status and prevents a fixture from silently
  applying a learning update (`qa/applied/validate_framework.py:338-358`).

**Recommended bounded change:** None required for this finding. Preserve the
current ordinary-path escape hatch and the rule that a learning update is
proposed and dispositioned rather than silently applied. Do not make every
short task carry a future outcome merely to satisfy the template.

## APP-02 — Route, stop, and learning vocabulary

**Verdict: UNRESOLVED — narrow residual.**

**Acceptance gate:** A08 requires observable agent behavior and inspectable
examples (`docs/V16_ACCEPTANCE_CRITERIA.md:19-21`); the artifact firebreak
specifically names route, cost, stop, receipts, and outcome learning for the
agent companion (`docs/ARTIFACT_BOUNDARIES.md:11-16`). The original APP-02
recommendation was a single vocabulary alignment, not workflow machinery
(`qa/applied/advisory/AGENT_PLAYBOOK_AND_SIGNAL_FOUNDRY_AUDIT_2026-08-19_223d190.md:99-137`).

### What is resolved

The core canonical vocabulary is now explicit and interoperable:

- `MECHANISMS.md` defines the nine route values, the five separate stop values,
  and the four separate learning states. It explicitly rejects using budget or
  deadline as a route and maps plain-language abstention to `HOLD`, `DEFER`, or
  `REFUSE` (`framework/MECHANISMS.md:160-185`, `:199-200`).
- `GLOSSARY.md` repeats the same three vocabularies and states that one record
  can carry one state in each relevant vocabulary
  (`framework/GLOSSARY.md:30`, `:43-46`, `:59-70`).
- The Quickstart now names all nine routes, all five stop statuses, and the
  learning close-out (`framework/agent-playbook/QUICKSTART.md:35-64`). The full
  guide makes route, stop, and learning three separate fields and explicitly
  disallows an untyped `ABSTAIN` route
  (`framework/agent-playbook/FULL_OPERATING_GUIDE.md:213-240`).
- The copyable brief and decision-receipt template expose the same fields
  (`framework/agent-playbook/COPYABLE_AGENT_BRIEF.md:79-118`;
  `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:75-88`). The operator
  playbook now also separates route from stop status and uses canonical route
  values in its decision table (`framework/OPERATOR_PLAYBOOK.md:99-112`,
  `:141-152`).
- The preflight route table and receipt now carry a canonical route, separate
  stop status, and learning status (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:120-150`).
- The fixture JSON contract requires `route`, `stop_status`, and `stop_reason`,
  validates route and stop values, prevents more acquisition/comparison after
  exhausted budget, and requires a canonical learning state with valid
  pending/reviewed semantics (`qa/applied/validate_framework.py:238-358`). The
  four target fixtures were checked by the structural validator.

The specialized templates are not internally contradictory. Their different
field subsets are intentional record shapes: the templates README says to copy
only fields needed for the implementation level and that a template does not
claim every task needs every field (`framework/templates/README.md:1-19`). For
example, the acquisition receipt has capture status plus canonical stop and
next-route fields (`framework/templates/ACQUISITION_RECEIPT.md:33-55`); the
decision brief carries a pre-outcome learning plan
(`framework/templates/DECISION_BRIEF.md:59-74`); disconfirmation carries route
and stop (`framework/templates/DISCONFIRMATION_LOG.md:19-31`); and outcome review
links the original route receipt while carrying the before/after learning
states (`framework/templates/OUTCOME_REVIEW.md:5-14`, `:40-52`). These are
role-scoped omissions, not alternate vocabularies.

### Residual strict-scope issue

Two changed canonical artifacts still put local labels under a `Route` concept
without a canonical mapping:

- The revised relationship diagram routes to “`acquire / compare / clarify`”,
  “`hold / defer / escalate / refuse`”, and “`answer / provisional packet`”
  (`framework/RELATIONSHIP_MAP.md:30-39`). The first two groups are recognizable
  lower-case renderings of canonical values, but “provisional packet” is not the
  canonical `ANSWER_PROVISIONALLY` route.
- Signal Foundry’s read-only procedure says “Choose packet, provisional packet,
  hold, or escalation” under `Route` (`cases/signal-foundry/README.md:146-168`).
  In the case’s bounded context these are understandable packet dispositions,
  but they are not mapped to `ANSWER`, `ANSWER_PROVISIONALLY`, `HOLD`, and
  `ESCALATE`.

The validator deliberately checks canonical vocabulary only across its
`vocabulary_files` list (`qa/applied/validate_framework.py:179-216`), which
contains the core mechanisms, glossary, agent entry points, and decision receipt
but not `framework/RELATIONSHIP_MAP.md` or the Signal Foundry case. It does
check the case’s containment and cost/stop phrases (`qa/applied/validate_framework.py:163-171`),
but that is not a route-label check. Therefore the passing validator is strong
evidence for the agent/fixture contract, but it cannot establish literal route
interoperability across every changed canonical artifact.

**Recommended bounded change:** In the relationship diagram and Signal Foundry
Step 10, either use the canonical values directly or parenthetically map the
local packet labels, for example: `ANSWER (packet)`,
`ANSWER_PROVISIONALLY (provisional packet)`, `HOLD`, or `ESCALATE`. Keep
“packet” as a case output description if desired, but do not leave it as an
untyped route value. If the diagram is intentionally conceptual, add one short
legend saying that its local labels map to the canonical route field and that
stop and learning statuses remain separate. Extend the structural vocabulary
scan only if the project wants diagrams/cases to be machine-checked; adding a
new workflow or receipt field is not warranted.

This is a small consistency repair. It does not require adding a mandatory
preflight, a new database, a new case, or a product implementation claim.

## APP-03 — Inspectable preflight statuses

**Verdict: RESOLVED.**

**Acceptance gate:** A08 requires observable, inspectable agent behavior
(`docs/V16_ACCEPTANCE_CRITERIA.md:19-21`), and the prior finding accepted a
group-level status as the smallest short-form fix
(`qa/applied/advisory/AGENT_PLAYBOOK_AND_SIGNAL_FOUNDRY_AUDIT_2026-08-19_223d190.md:139-171`).

**Evidence:**

- The checklist now says every P-group records `PASS`, `FAIL`, `UNKNOWN`, or
  `NOT_APPLICABLE`, together with evidence/receipt IDs; NOT_APPLICABLE requires
  a reason, UNKNOWN is not a silent pass, and an explicitly recorded ordinary
  path may bypass preflight only under a bounded condition
  (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:1-9`).
- P0 through P7 each have a visible `Group status`, evidence/receipt field, and
  NOT_APPLICABLE reason field. P7 additionally carries all four learning states
  (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:11-20`, `:23-39`, `:41-53`,
  `:55-94`, `:96-118`). A reviewer can now distinguish an explicit group pass,
  failure, unknown, or justified non-applicability from an untouched checkbox.
- The route table keeps required records separate from canonical route values,
  including the budget/deadline and no-outcome cases
  (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:120-131`). The preflight
  receipt preserves PASS/FAIL/UNKNOWN/NOT_APPLICABLE groups with evidence or
  reasons, then records route, stop status, learning status, no-action boundary,
  resume condition, and reviewer destination
  (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:133-150`).
- The validator counts all eight group-status fields and checks that the receipt
  preserves status evidence and NOT_APPLICABLE reasons
  (`qa/applied/validate_framework.py:224-229`). The target QA run passed the
  receipt/preflight/stop check.

**Recommended bounded change:** None required for APP-03. Keep the group-level
short form as the documented minimum and allow a higher implementation level to
add per-check statuses when the decision warrants that cost. Do not turn the
checklist into a mandatory form for an explicitly recorded ordinary path.

## APP-04 — Signal Foundry cost, stop, and resume envelope

**Verdict: RESOLVED.**

**Acceptance gate:** A07 requires cost and stop guidance in concrete
implementation paths, and A09 requires Signal Foundry to remain a bounded
illustration rather than validation (`docs/V16_ACCEPTANCE_CRITERIA.md:19-21`).
The case is in the builder `cases/**` boundary, not an empirical product
artifact (`docs/ARTIFACT_BOUNDARIES.md:11-16`).

**Evidence:**

- The case now labels its section “Illustrative cost and stop envelope” and
  explicitly says the controls bind the fixture, not a Signal Foundry product
  (`cases/signal-foundry/README.md:70-73`).
- The table bounds material to supplied rows/pointers; acquisition to zero
  provider calls, paid retrieval, scraping, private-data access, or new external
  content; work to one packet-composition pass and one comparison/peripheral
  pass; human attention to one reviewer and one correction round; disclosure to
  the repository fixture; and latency to disposition of declared rows
  (`cases/signal-foundry/README.md:75-83`).
- The prose defines hard stops for missing/ambiguous permission, packet-affecting
  identity/capture failure, paid/private acquisition, and proposed external
  action. It defines a soft stop after the two declared passes, requires the
  remaining gap to be recorded without fixture expansion, and permits resume
  only after a named human supplies an authorized pointer, corrects a record, or
  authorizes a separately scoped next step (`cases/signal-foundry/README.md:84-90`).
- The case procedure points to the envelope and the boundary footer states that
  it is a case control rather than a product requirement or runtime evidence
  (`cases/signal-foundry/README.md:146-168`, `:181-192`).
- The validator checks the case’s illustration/non-validation/unperformed
  operation language plus the cost/stop/resume phrases
  (`qa/applied/validate_framework.py:163-171`).

**Recommended bounded change:** None required for APP-04. Preserve the fixture
scope and the explicit statement that the envelope is not a product
requirement. The APP-02 route-label mapping should reference this envelope but
must not broaden it into a Signal Foundry runtime specification.

## V13-05 — Implementation-path continuity sentence

**Verdict: RESOLVED.**

**Acceptance gate:** A07 requires concrete implementation choices
(`docs/V16_ACCEPTANCE_CRITERIA.md:19`); the prior V13 continuity review called
for one sentence mapping the practical range to process, intermediary workflow,
and optional model adaptation, while rejecting hierarchy and mandatory use
(`qa/editorial/advisory/V13_CONTINUITY_AND_INTENT_FIDELITY_2026-08-19_223d190.md:271-323`).

**Evidence:**

- The target implementation table still gives lightweight, moderate, and
  advanced paths with best fit, inputs, outputs, typical cost, stop condition,
  and main risk (`framework/IMPLEMENTATION_CHOICES.md:7-13`). Its introduction
  remains stack-neutral and says no provider, model, graph, database, or service
  is mandatory (`:1-5`).
- The added continuity sentence states that the levels may be realized as a
  team process, an intermediary reasoning/context or evidence workflow, or—only
  with separately approved data, budget, governance, and evaluation—model
  adaptation. It explicitly says no path is inherently deeper, more defensible,
  or required and allows combination when warranted
  (`framework/IMPLEMENTATION_CHOICES.md:15-20`).
- The surrounding lightweight route and selection rubric preserve the
  non-bureaucratic escape hatches: no new software is required for lightweight
  work (`framework/IMPLEMENTATION_CHOICES.md:22-41`), and the framework may stay
  lightweight or not be used for creative transformations, disposable outputs,
  supplied-context formatting/translation, no-new-evidence tasks, or cases
  where recording costs more than the consequence (`:93-101`).
- The validator checks for team-process/model-adaptation continuity and the
  anti-hierarchy sentence (`qa/applied/validate_framework.py:173-177`).

**Recommended bounded change:** None required for V13-05. Keep model adaptation
conditional on separately approved data, budget, governance, and evaluation;
do not turn the continuity sentence into a model recommendation or move it into
the human essay’s opening.

## Bureaucracy, validation, and product-claim check

The revision does not create a new mandatory operating bureaucracy:

- The Quickstart states that its smallest safe response shape is intentionally
  lightweight and should not turn every trivial task into a compliance ritual
  (`framework/agent-playbook/QUICKSTART.md:82-94`).
- The preflight explicitly allows a recorded ordinary path to bypass the
  checklist when no new evidence, comparison, memory reuse, permission
  decision, or external influence is required
  (`framework/agent-playbook/PREFLIGHT_CHECKLIST.md:3-9`).
- Implementation choices remain stack-neutral, provide a no-new-software
  lightweight path, and say when not to use the framework
  (`framework/IMPLEMENTATION_CHOICES.md:1-5`, `:22-41`, `:93-101`).
- Signal Foundry’s reviewer/pass limits are explicitly fixture controls, not
  product requirements (`cases/signal-foundry/README.md:70-90`, `:181-188`).

No new validation or product claim was introduced:

- Signal Foundry remains marked `ILLUSTRATION_ONLY / READ_ONLY /
  NOT_VALIDATION`, contains no runtime/data/credentials/provider/external
  content, and calls every row an illustrative fixture
  (`cases/signal-foundry/README.md:1-15`). It expressly denies detection,
  scoring, model analysis, runtime integration, product readiness, and empirical
  validity (`:40-41`).
- The case’s footer says it does not establish an implemented handoff or runtime
  behavior, and no row grants permission to act
  (`cases/signal-foundry/README.md:181-192`).
- The QA artifacts distinguish structural/procedural checks from effectiveness,
  production behavior, and research results (`qa/applied/validate_framework.py:1-7`;
  `qa/applied/README.md:23-26`).
- The V13 continuity sentence describes an optional implementation path subject
  to separate approvals; it does not claim that model adaptation works or has
  been evaluated (`framework/IMPLEMENTATION_CHOICES.md:15-20`).

## Handoff

The post-revision result is suitable for owner review with one clearly bounded
APP-02 copy repair outstanding. Mark APP-01, APP-03, APP-04, and V13-05
**Accepted**; mark APP-02 **Accepted with revision** until the relationship-map
and Signal Foundry route labels are mapped to the canonical route field. This
report is advisory work product only and must not be cited as evidence that the
playbook, Signal Foundry, or any case improves decisions.
