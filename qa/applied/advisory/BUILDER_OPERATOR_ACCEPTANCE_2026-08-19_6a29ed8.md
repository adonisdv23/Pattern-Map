# Builder/operator acceptance review

**Reviewed commit:** `6a29ed834bffa405942b8636a8a6b8e7b48cbf4f` (`6a29ed8`)

**Review date:** 2026-08-19

**Scope:** `framework/**`, `cases/**`, the rendered site Apply and Examples
surfaces, `site/exports/standalone/pattern-map-v16.html`, and the prior applied
and site QA records relevant to A07, A08, and A09.

**Overall verdict: PASS WITH REVISIONS.**

The canonical builder framework, agent companion, two neutral fixture cases,
and Signal Foundry fixture satisfy the substantive A07–A09 requirements. The
integrated site is structurally healthy and preserves the human-first hierarchy,
but two rendered-output defects remain before the applied/site package should be
called clean: the Markdown renderer mutates bare underscore-bearing state
vocabulary in the visible Apply/Examples/standalone content, and the standalone
export contains 13 dead source-fragment links (while the multi-page build
silently routes several of the same unresolved source links to the home page).
These are bounded site-rendering and navigation repairs, not owner-intent or
framework-architecture changes.

No model, agent, provider, participant, product, or Signal Foundry runtime was
run. Fixtures, validators, screenshots, PDF pages, and advisory reviews are
treated as implementation/procedural evidence only, not effectiveness results.

## Explicit A07/A08/A09 verdict at `6a29ed8`

| Gate | Verdict | Evidence | Remaining condition |
| --- | --- | --- | --- |
| **A07 — concrete implementation paths** | **PASS** | `framework/IMPLEMENTATION_CHOICES.md:7-20` gives lightweight, moderate, and advanced choices with best fit, inputs, outputs, cost, stop condition, risk, stack-neutrality, and non-hierarchical selection guidance. `:22-78` supplies route details and human-authority boundaries; `:80-119` supplies selection and when-not-to-use guidance. `framework/BOUNDARIES_AND_FAILURES.md:7-136` supplies failure modes, hard/soft stops, resume conditions, cost dimensions, permission checks, and proportionate escape hatches. `cases/general-research/README.md`, `cases/product-and-process/README.md`, and `cases/signal-foundry/README.md:70-90` make the routes concrete with fixture-scoped cost/stop boundaries. | The site Apply cards are a concise presentation of the canonical choices; the two navigation/rendering findings below affect site usability but do not remove the complete canonical implementation paths. |
| **A08 — observable agent behavior** | **PASS WITH REVISIONS** | `framework/agent-playbook/QUICKSTART.md:1-94` and `FULL_OPERATING_GUIDE.md:1-325` define decision framing, acquisition, comparison, disconfirmation, typed uncertainty, escalation, cost, stop, influence, and outcome learning with named receipts. `COPYABLE_AGENT_BRIEF.md`, `PREFLIGHT_CHECKLIST.md`, `DECISION_RECEIPT_TEMPLATE.md`, the templates, and `ORDINARY_VS_DISCRIMINATION_LAYER.md` make behavior inspectable. Canonical route, stop, and learning vocabularies agree across the source artifacts after the prior APP-01–APP-04 revisions. The Apply route includes the Quickstart, deeper guide, receipt materials, and state vocabulary. | **BOP-01** corrupts bare underscore-bearing examples/status labels in rendered Apply/Examples HTML; **BOP-02** breaks the standalone Quickstart link to `OUTCOME_REVIEW.md` and other source links. Repair the renderer and link resolver, then rerun the site checks. |
| **A09 — Signal Foundry bounded, not validation** | **PASS WITH REVISIONS** | The source case header/footer and procedure are explicit: `cases/signal-foundry/README.md:1-15` says `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, no runtime/data/credential/provider work occurred, and rows are fixtures; `:70-90` defines an illustrative material/acquisition/work/reviewer/disclosure/latency envelope with hard stops, soft stop, and resume conditions; `:163-170` maps packet descriptions to canonical route values and keeps stop/learning separate; `:183-193` states the boundary that must travel with links. `site/build.mjs:560` labels the Examples surface and case summary; the structural check confirms the header/footer boundary is present. No generated `<a>` target points to a separate Signal Foundry artifact that lacks the boundary. | **BOP-01** renders the case’s body status line as `ILLUSTRATION<em>ONLY / READ</em>ONLY / NOT_VALIDATION`, so the visible header should be repaired for exact status readability. The case’s summary, boundary copy, and non-validation claims remain visible; this is a revision condition, not a validation or permission overclaim. |

## What passes in the canonical framework and cases

### Builder/operator routes (A07)

The implementation spectrum is concrete and proportionate:

- Lightweight work names bounded evidence, a permission note, a time limit,
  decision/evidence/disconfirmation/influence outputs, a bounded stop, and the
  risk of insufficient traceability.
- Moderate work adds stable identity, typed relationships, versioned packets,
  human disposition, capture/failure receipts, and outcome review, with setup
  and review overhead stated as cost.
- Advanced work adds lineage, time-series/baseline views, access policy,
  route planning, replay, review queues, and approved evaluation while naming
  engineering/privacy/security/evaluation cost and automation/false-precision
  risks. It explicitly does not imply autonomy.
- The framework says when to stay ordinary or lightweight, including supplied
  transformations, disposable/easily corrected work, no-new-acquisition tasks,
  and cases where recordkeeping costs more than the consequence of error.

The two domain-neutral cases are genuinely neutral, invented fixture cases:
the weekly-session case separates repeated requests, accessibility context,
capacity, authorization, and a future outcome plan; the intake-process case
separates motion candidate, expected absence, version change, permission, and
learning. Neither presents a runtime result, recommendation, or product claim.

Signal Foundry is a serious but bounded fixture translation. It is read-only,
contains no runtime code/data/credentials/provider calls, and gives an explicit
zero-provider-call, supplied-rows-only, one-pass/two-pass, one-reviewer,
repository-only disclosure envelope. Its procedure uses `ANSWER`,
`ANSWER_PROVISIONALLY`, `HOLD`, and `ESCALATE` as route fields rather than
inventing packet labels, and its footer repeats that it is not validation.

### Observable agent behavior (A08)

The agent artifacts meet the required observable procedure contract:

- decision framing records the real question, intended use, audience,
  consequence, owner/reviewer, deadline, and useful-answer condition;
- acquisition records the default-path gap, bounded peripheral route,
  permission, source/artifact/version/span, capture or failure status, cost,
  remaining budget, and next route;
- comparison requires a declared peer/period/attribute/structure/origin unit,
  aligned definitions, and visible `UNKNOWN`/`INCOMPARABLE` states;
- disconfirmation asks for contrary/limiting material, missing perspective,
  alternative explanation or measurement change, and common origin where
  relevant;
- uncertainty stays typed (`UNKNOWN`, `INSUFFICIENT_SUPPORT`,
  `FAILED_CAPTURE`, `NOT_AUTHORIZED`, `MISSING_BASELINE`, and related states);
- route, stop, and learning are separate canonical fields;
- escalation names the human question, cost already spent, no-action boundary,
  and resume condition;
- influence receipts list selected and withheld items, reasons, claims,
  limits, permission, and disposition; and
- learning preserves the original expectation/receipt, compares a later
  outcome and actual cost/context, proposes one bounded update, and requests
  human disposition rather than silently changing policy.

The ordinary-vs-layered examples make the distinction inspectable without
claiming that either path is effective. The prior applied audits
`AGENT_PLAYBOOK_AND_SIGNAL_FOUNDRY_AUDIT_2026-08-19_223d190.md` and
`APPLIED_POST_REVISION_VERIFICATION_2026-08-19_cd8a756.md` correctly identify
APP-01–APP-04 as resolved in the canonical source artifacts; this review finds
the residuals below only in the site renderer/link presentation.

### Signal Foundry containment (A09)

The source case does not grant access, permission, product readiness, or
external authority. It explicitly distinguishes transcript evidence, visual
context, comments, related context, provider receipts, derived analysis, and
gap/failure records. It states that a fixture row is not an observed run, that
the illustrative cost/stop envelope is not a product requirement, and that no
row grants permission to scrape, disclose, purchase, contact, deploy, or act.
The Examples route repeats the status in its section introduction and case
summary. A search of the generated site found no separate Signal Foundry anchor
link whose destination omits the boundary; the case is embedded in the bounded
Examples surface.

## Findings

### BOP-01 — Renderer mutates visible underscore-bearing state vocabulary

**Severity:** Medium

**Type:** Factual rendered-content defect; agent-observability and boundary
readability risk.

**Gates:** A08 and A09 (rendered Apply/Examples surfaces; standalone export).

**Evidence:**

- `site/build.mjs:104-109` applies `_([^_]+)_` emphasis to every ordinary text
  string. `site/build.mjs:129-141` protects backtick code spans and links, but
  leaves ordinary prose/status lines exposed to that regex.
- The fresh build renders the Quickstart hard-stop line as
  `STOPPED<em>BUDGET or STOPPED</em>DEADLINE` in
  `site/dist/apply/index.html:60`, and renders the Full Guide route/stop/learning
  prose and copyable return shape with the same mutation at
  `site/dist/apply/index.html:121,157-160`.
- The Signal Foundry source status at
  `cases/signal-foundry/README.md:3` is exact, but the rendered case body is
  `Status: ILLUSTRATION<em>ONLY / READ</em>ONLY / NOT_VALIDATION` at
  `site/dist/examples/index.html:45` and
  `site/exports/standalone/pattern-map-v16.html:1050`.
- The canonical tokens shown inside backticks remain intact, which is why
  `npm run check`, `qa/site/audit_site.py`, and the applied validator pass; the
  checks do not assert that bare prose/status tokens survive rendering.

**Impact:** The canonical framework and case source remain correct, and the
case summary still says `ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION`, but a
reader of the rendered procedure sees state labels with underscores removed or
split by italic markup. That weakens exact receipt copying and makes the
Signal Foundry body header less precise. It must not be treated as a live
agent-compliance or effectiveness result.

**Fix:** Protect machine-like identifiers containing underscores before
emphasis parsing (or narrow/remove the bare-underscore emphasis rule), while
preserving intended Markdown emphasis. Add a generated-output assertion for
representative bare tokens such as `STOPPED_BUDGET`,
`LEARNING_NOT_APPLICABLE`, `NOT_AUTHORIZED_OR_AMBIGUOUS`, and the exact Signal
Foundry status line in Apply, Examples, and the standalone export. Rebuild and
rerun the site and content QA. Do not alter the canonical case status or owner
intent to accommodate the renderer.

**Recommended disposition:** **Accepted with revision** — bounded site
renderer/test correction; no framework architecture or claim change.

### BOP-02 — Standalone source fragments are dead; multi-page fallbacks lose route accuracy

**Severity:** Medium

**Type:** Cross-link integrity/usability defect affecting direct-open export
and builder/operator navigation.

**Gates:** A08 and the required standalone/cross-link deliverable; A07’s
builder discoverability is substantively passed by the canonical files but is
weakened at the site presentation layer. This finding does not change A09’s
Signal Foundry containment verdict.

**Evidence:**

- `site/build.mjs:94-101` maps an unrecognized Markdown source path to
  `#source-<slug>` in standalone mode, and to the route’s `index.html` in the
  multi-page build. This is a safe file target but not a semantically accurate
  source destination.
- The Apply Quickstart link to `../templates/OUTCOME_REVIEW.md` becomes
  `href="../index.html"` in `site/dist/apply/index.html:57`, sending a builder
  to the home page instead of the Apply/template route.
- In the standalone export, the corresponding link is
  `href="#source-templates-outcome-review-md"` at
  `site/exports/standalone/pattern-map-v16.html:794`, but no element has that
  ID. The same unresolved-fragment pattern appears in the Sources, Research,
  and History source routes at `:1220`, `:1369`, and `:1421`.
- An independent post-build fragment audit found **13 missing standalone
  fragments**: `source-templates-outcome-review-md`,
  `source-docs-owner-intent-v16-md`,
  `source-docs-thesis-and-audience-contract-v16-md`,
  `source-relation-to-v16-md`, `source-status-and-boundaries-md`,
  `source-version-history-md`, `source-preserved-v15-2-index-md`,
  `source-future-execution-plan-md`, `source-qa-ep-v0-1-qa-md`, and four
  `source-transfers-v14-complete-2026-08-18-05-historical-v13-*` fragments.
  All nine built route files pass existence checks, so the current
  `site/check.mjs` does not detect this fragment/semantic-target gap.

**Impact:** Direct-open reviewers cannot follow those source links. On the
multi-page site, the same links can appear to work while silently returning to
the home route, which is misleading for a builder trying to inspect a template,
Echo status record, or historical source. This is a navigation defect, not a
claim or research result.

**Fix:** For every canonical source link, either map it to a real local route
and existing fragment (for example the Apply, Research, or History route),
render it as non-link source text when no local target is intentionally exposed,
or add a deliberate standalone target section. Extend `site/check.mjs` or
`qa/site/audit_site.py` to validate same-document fragments and the expected
semantic route for Markdown source links, not only target-file existence. The
standalone export should have zero missing fragments after the fix.

**Recommended disposition:** **Accepted with revision** — bounded source-route
mapping and link-QA correction; no source-content or owner-intent change.

## Prior QA and local checks re-run

The review considered the prior records as procedural/implementation evidence,
not as proof of effectiveness:

- `qa/applied/PLAYBOOK_INTEGRATION_QA.md` — prior canonical integration check;
- `qa/applied/advisory/AGENT_PLAYBOOK_AND_SIGNAL_FOUNDRY_AUDIT_2026-08-19_223d190.md`;
- `qa/applied/advisory/APPLIED_POST_REVISION_VERIFICATION_2026-08-19_cd8a756.md`;
- `qa/site/SITE_QA_REPORT.md` and `qa/visual/VISUAL_QA_REPORT.md` — retained
  site/render QA, including the honest physical-keyboard and print-preview
  residuals; and
- the retained Apply/Examples/home/map/mobile/PDF captures, which show the
  intended hierarchy and composition. They do not establish reader
  comprehension or behavior.

Fresh checks at `6a29ed8`:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)  PASS
cd site && npm run build                                      PASS (9 routes)
cd site && npm run check                                      PASS
python3 qa/site/audit_site.py                                 PASS (structural only)
python3 qa/editorial/validate_content_interface.py            PASS
python3 qa/applied/validate_framework.py                      PASS
framework/SIX_FAMILIES.json + schema standard-library parse   PASS
git diff --check 6a29ed8^ 6a29ed8                            PASS
```

The fresh build produced the same tracked standalone export bytes as the
reviewed commit (`b9de4e4815a964a0a9b77f22d8a3e459a099c41352eb2c4a099c7110ef905dda`),
and the worktree remained clean before this report was created. The passing
validators are valuable structural checks, but they do not cover the two
rendered-output conditions documented above.

## Handoff

This report is advisory work product for owner review. It makes no change to
`framework/**`, `cases/**`, `site/**`, the standalone export, the contracts, or
the QA validators. The only permitted write in this review is this uniquely
named report. No commit, push, deployment, publication, provider call, study,
dataset acquisition, outreach, or external action was performed.
