# Project-use cold-start QA

Status: **STRUCTURAL / PROCEDURAL QA ONLY — NOT A TRANSFER, LIVE-AGENT, OR
EFFECTIVENESS RESULT**

## Reviewed state and scope

| Field | Value |
| --- | --- |
| Starting baseline | `d05aca58910b4463e5afb69b10558b662a446278` (`plan: define next-level opportunity loops`) |
| Working branch | `codex/pattern-map-v16-loop-agent` |
| Scope | `framework/**` and `qa/applied/**` only |
| Owner-intent checkpoint | `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — PASS (`OWNER_INTENT_V16.md: OK`) |
| External work | No Signal Foundry checkout, provider, model, corpus, participant, product, or external system was used |

This report audits whether a materially different future project can enter the
existing v16 contracts without reading the whole repository or manufacturing a
six-family completion ritual. It records a synthetic cold-start contract test,
not a transfer to a real project. Signal Foundry and the two existing neutral
cases remain bounded illustrations and are not evidence that the starter
transfers or improves decisions.

## Baseline composition and likely translation seam

The first pass attempted composition from the existing Quickstart, copyable
brief, preflight, implementation choices, and template index. At the exact
baseline, the relevant entry points were already internally bounded and the
focused applied validator passed. A static composition probe still indicated a
likely cold-start seam:

| Existing composition element | Baseline observation | Friction for a new receiver |
| --- | --- | --- |
| `framework/agent-playbook/QUICKSTART.md` | 140 lines / 1,130 words; starts with Stage 0 and then asks the operator to define the decision and authority | No single project-context block says which local facts must be supplied before the operator selects a record or family |
| `framework/agent-playbook/COPYABLE_AGENT_BRIEF.md` | 203 lines / 1,261 words; self-contained copied prompt with Stage 0 and all canonical records | A receiving project must translate its local decision, permission, baseline, budget, and family relevance into the generic return shape by hand |
| `framework/agent-playbook/PREFLIGHT_CHECKLIST.md` | 176 lines / 1,248 words; status groups are observable | It is a verification checklist after intake, not a cold-start adapter or a route-to-template map |
| `framework/IMPLEMENTATION_CHOICES.md` | 146 lines / 1,292 words; levels and stopping rules are complete | It explains proportionality but does not tell a new project which minimum fields and records to carry forward |
| `framework/templates/README.md` | Nine templates listed with separate uses | The index says to copy only what is needed, but does not map a project fact to a template or say what to do before that choice |

The likely seam was probed with a QA-only cold-start question: “A future
project has supplied records and may need to decide whether to change a local
practice; what must it hand to the v16 route before it can select records?”
The existing composition can answer the framework questions, but it requires
the receiver to reconstruct a project intake and choose among nine templates.
There is no evidence of a runtime failure, and no real project was contacted.

The missing seam is therefore translation and wayfinding, not a missing family,
route, receipt schema, or mechanism. A small adapter can resolve it if it
terminates ordinary work first and points to existing artifacts rather than
repeating their procedures.

## Candidate alternatives and dispositions

| ID | Candidate | Disposition | Reason and governing boundary |
| --- | --- | --- | --- |
| PU-01 | Document composition only; leave the existing entry points unchanged | Rejected | A static composition probe found that the composition remains semantically usable, but a receiver would need to construct a project-context handoff and template mapping. This indicates a plausible wayfinding seam; it does not establish measured transfer friction. The existing contracts remain the source of truth. |
| PU-02 | Generic adoption brief or conformance dictionary | Deferred | D-031 and D-042 defer a generic adoption layer until repeated friction appears across Signal Foundry and a materially different real project. This QA fixture does not establish that condition. A future candidate would still need an owner-reviewed abstraction, not a generality claim. |
| PU-03 | New deterministic intake/route helper or machine-readable receipt profile | Rejected | A second runtime router or receipt schema would create a new contract, risk implied authority, and duplicate the existing Stage 0 and receipt fixtures. No new mandatory route, score, ledger, or autonomous authority is justified by the likely translation seam. |
| PU-04 | Second domain-neutral worked case | Rejected | The existing general-research and product-and-process fixtures already demonstrate sparse family use, permission, comparison, motion/absence, stopping, and bounded learning. A new invented case would add narrative weight without real-project evidence. |
| PU-05 | Seventh family, universal conformance or source-reputation score, or second ledger | Rejected | These conflict with the six-family lock, source-role/support separation, and anti-bureaucracy boundary. They do not resolve cold-start translation. |
| PU-06 | One project-use starter as a context adapter and wayfinding sheet | Accepted with revision | `framework/agent-playbook/PROJECT_USE_STARTER.md` gives one ordered handoff after Stage 0, maps project facts to existing templates, names only material family questions, and preserves typed permission, human action, cost/stop, uncertainty, and non-applicability boundaries. The lane's retained form was 135 lines / 897 words versus the 140-line / 1,130-word Quickstart. Loop 1 permission/completeness clarifications produced 147 lines / 991 words; Loop 2 removed repeated vocabulary/procedure while retaining the unique adapter, leaving 112 lines / 721 words. Size is descriptive only. It explicitly disclaims conformance and transfer proof. |

## Accepted addition

The accepted shape is intentionally a thin adapter over existing sources:

- `framework/agent-playbook/PROJECT_USE_STARTER.md` is an optional internal
  cold-start page. It asks the complete Stage 0 question before any project
  packet.
- A Stage 0 `NO` returns only the existing four-field ordinary record and
  stops before evidence, route, stop, outcome, learning, influence, or family
  records.
- A Stage 0 `YES` exposes one project-context handoff with the real question,
  intended use, owner/reviewer, consequence/reversibility, permission scope and
  state, baseline, cost/no-action boundary, human-action boundary,
  unknowns/non-applicability, and resume/escalation condition.
- The adapter maps those facts to the existing decision, acquisition,
  evidence, comparison, disconfirmation, influence, memory, and outcome
  templates. It does not create a second record shape.
- It names F1–F6 as optional questions. An inactive family receives one bounded
  reason and no placeholder artifact; the family map is not a completion
  checklist.
- It carries the existing canonical permission, route, stop, and learning
  vocabularies and keeps external action with the explicitly authorized human.
- `framework/README.md` links the page from the existing framework start list;
  this is wayfinding, not a new artifact boundary.

## Proportionality self-challenge and final revision

The first draft of the starter was 151 lines / 1,216 words and repeated more
of the Quickstart's operating prose than the cold-start seam required. The
first validator addition also used a larger exact-text assertion block. That
version was not retained. The lane revision was 135 lines / 897 words. Loop 1
then added repository-local/non-portable labeling, operation-level permission
and blocked-state semantics, complete level-fit wording, and canonical
useful-answer/abstention pointers, producing 147 lines / 991 words. Loop 2 then
removed repeated family labels, route/stop/learning vocabulary, and duplicated
validator logic while retaining the complete Stage 0 gate, one project-context
block, fact-to-record mapping, permission/human-action boundary, proportional
route rule, and canonical pointers. The current form is 112 lines / 721 words,
but is not claimed to be easier on that basis. Detailed acquisition, evidence,
comparison, disconfirmation, memory, influence, and learning procedures remain
in their existing canonical files.

The validator coupling was narrowed at the same time. It checks only the
adapter's stable contract seams: Stage 0 ordering and terminal language,
existing-path resolution, the ordered context fields, six-family labels,
canonical state vocabulary, explicit expansion prohibitions, and a five-row
QA-only Stage 0 truth table. It does not duplicate the receipt schema or parse
free-form operator prose. The remaining exact phrases are locked boundary
sentences or stable headings/field names whose drift should fail closed and be
reviewed with the adapter.

An alternative of inserting the context block into the Quickstart was
considered and rejected: it would make the universal short operator entry
point carry project-transfer fields even for operators who already know their
context, while still providing no distinct first-contact wayfinding target.
An alternative of placing the block only in the template index was rejected
because Stage 0 must terminate before any layered template selection. The
standalone starter therefore passes the static removal test narrowly: remove
it and the existing procedure still works, while the project-context
translation step again has no single wayfinding page. This is evidence of
composition and compactness, not measured ease or successful transfer.

## Signal Foundry packet recommendation

Keep `PROJECT_USE_STARTER.md` **repo-only** for this checkpoint; do not add it
to the existing Signal Foundry portable selection by default. The starter is a
Pattern Map wayfinding adapter, not a Signal Foundry implementation input. It
points at the full Pattern Map template and entry-point paths, contains
owner-repository review guidance, and has not been exercised by a real
downstream project. Adding it to the packet would add dead weight or imply
that Signal Foundry is evidence of generic transfer, contrary to D-034 and
D-042. A future owner-approved receiver packet may include it as the first
entry point only if its selected-subset links and receiving-repository
capabilities are explicitly regenerated and verified; this commit makes no
such packet change or transfer claim.

## Focused validator and cold-start controls

`qa/applied/validate_framework.py` now checks the accepted adapter without
turning it into a runtime router. These static repository controls require:

1. the exact Stage 0 eligibility, terminal ordinary-record, human-authority,
   budget/complexity, and three-condition Advanced contracts;
2. Stage 0 ordering before context intake and layered route selection;
3. links to existing canonical templates and entry points, all of which must
   resolve in the checkout;
4. exactly one ordered project-context block, with no extra receipt shape;
5. all six family orientation rows, canonical route/stop/learning values, and
   all four typed permission states;
6. explicit rejection of conformance, reputation-score, extra-ledger,
   seventh-family, autonomous-authority, and general-validation language; and
7. a QA-only Stage 0 matrix in which an exact supplied reformat is ordinary,
   while a selective supplied summary, new acquisition, unresolved permission,
   and a separate human action gate all leave the ordinary path.

The matrix is a structural truth-table check. It is not an executable
downstream router, a project transfer, or evidence that any agent follows the
page.

## Removal and proportionality tests

| Test | Result | Evidence boundary |
| --- | --- | --- |
| Remove the starter and compose only the existing entry points | No single project-context handoff or fact-to-template map remains; a receiver would have to compose that step | This indicates a plausible wayfinding seam, not measured friction or a new framework layer |
| Remove the adapter's family-orientation sentence | Existing Quickstart still runs, but the receiver loses the compact “use only what can change the decision” bridge; no family is required by the validator | The six-family map remains canonical and optional by materiality |
| Stage 0 exact reversible supplied-material transformation | Classified as ordinary by the static QA matrix; the starter instructs a four-field terminal return | The check does not execute a receiver or create a record |
| Stage 0 supplied-material judgment/selection | Rejected from ordinary by the QA matrix | Selection and judgment inside supplied input still require the layered path |
| Missing/unclear/revoked permission | Starter points to typed operation-level state and canonical stop semantics; existing blocked fixtures keep evidence, baseline, comparison, disconfirmation, memory, and influence empty and memory `NOT_USED` under the global-permission contract | The static matrix exercises unresolved permission eligibility only; no access-to-permission inference or external-action authority |
| Missing baseline, unresolved item, or non-applicable check | Starter says no unsupported motion or absence claim, keeps unresolved material out of influence, and permits one bounded `NOT_APPLICABLE`/`SKIPPED` reason only when genuinely inactive | Unknown remains unknown; the page does not execute or fabricate a `MISSING_BASELINE` state |
| Larger budget or repeated project use | Starter preserves the three-condition Advanced rule and says a higher level is not better | Budget is capacity/constraint, not an independent complexity selector |
| Remove the starter after an operator has chosen a route | Existing canonical templates and receipts remain sufficient; the adapter is not a dependency or replacement | The addition is removable and does not change the six-family framework |

## Verification

Commands run from the repository root:

| Command | Result |
| --- | --- |
| `python3 -m py_compile qa/applied/validate_framework.py` | PASS |
| `python3 qa/applied/validate_framework.py` | PASS — six-family, inventory, Stage 0, project-use adapter, receipt, and fail-closed mutation groups |
| `for f in qa/applied/receipts/*.json; do python3 -m json.tool "$f" >/dev/null; done` | PASS — all receipt fixtures parse |
| `python3 -m json.tool qa/applied/memory_anchor_registry.json >/dev/null` | PASS |
| `git diff --check` | PASS |
| `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` | PASS — `OWNER_INTENT_V16.md: OK` |

These checks establish artifact presence, exact text/field contracts, canonical
vocabulary, and selected fail-closed mutations only. They do not establish
that a new project can use v16 successfully, that an agent follows the
starter, that permission assertions are legally valid, that any case is
effective, or that the framework has been validated. No live agent, provider,
model, study, external dataset, Signal Foundry runtime, publication, or
deployment was performed.

## Residual owner and downstream gates

The starter is a local owner-review candidate. A real receiving project must
resolve its own authority, permissions, baselines, data/retention rules,
implementation choices, and human action gates. Owner/mentor judgment,
downstream-repository authority, and any publication or research decision stay
outside this branch and require their existing explicit gates.
