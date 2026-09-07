# Applied/rendered post-revision verification

**Reviewed commit:** `8aa5f949e9fffed0e4b8bc14c7f71887d3adb842` (`8aa5f94`)

**Comparison:** exact integrated remediation diff `6a29ed834bffa405942b8636a8a6b8e7b48cbf4f..8aa5f94`

**Review date:** 2026-08-19

**Scope:** bounded BOP-01/BOP-02 remediation; the integrated
`framework/**` and `cases/**`; rendered Apply, Examples, History, and
standalone surfaces; canonical route/stop/learning/capture/status labels;
source-route semantics; same-document/local fragments; Signal Foundry
containment; and prior applied QA relevant to A07, A08, and A09.

**Overall verdict for the requested A07/A08/A09 acceptance:** **PASS**.

The two rendered-output defects identified at `6a29ed8` are resolved at
`8aa5f94`. The canonical implementation and agent artifacts remain intact,
the two neutral fixtures remain inspectable, and Signal Foundry remains a
fixture-only bounded illustration. The residuals recorded below are
standalone semantic/accessibility or owner-review follow-ups outside the
requested A07–A09 acceptance; they are not converted into live-compliance,
reader-effectiveness, agent-behavior, or product-effectiveness claims.

## Evidence boundary and exact-commit control

This is implementation and procedural QA only. No provider, model, agent,
participant, product, Signal Foundry runtime, private/runtime data, study,
external dataset, paid retrieval, deployment, publication, or external action
was used. Fixtures, source inspection, local validators, generated HTML, and
the fragment/route audit establish artifact integrity and inspectability only.

The shared checkout acquired unrelated uncommitted sibling changes while this
review was in progress. I did not edit, stage, revert, or include them. To
ensure that regenerated output represented the requested commit rather than
the dirty shared checkout, the final build and audits were rerun in a clean
detached worktree at exactly `8aa5f94`.

The repository controls remained intact:

- `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — `OWNER_INTENT_V16.md: OK`;
- `git diff --check 6a29ed8..8aa5f94` — pass;
- the target commit is the direct parent integration of `6a29ed8`, with the
  remediation diff limited to the prior advisory/QA records, renderer and
  checker changes, and the regenerated standalone export;
- the target commit's seven changed paths are the two prior advisory records,
  `qa/site/SITE_QA_REPORT.md`, `qa/site/audit_site.py`, `site/build.mjs`,
  `site/check.mjs`, and `site/exports/standalone/pattern-map-v16.html`.

The exact diff adds the explicit source-route map and unmapped-link failure in
`site/build.mjs:63-112`, replaces underscore emphasis with asterisk-only
emphasis in `site/build.mjs:114-120`, adds representative state/status and
fragment assertions in `site/check.mjs:95-109` and
`qa/site/audit_site.py:187-198`, and regenerates the standalone export.

## Regenerated output and local checks

In the clean exact-commit worktree:

```text
cd site && npm run build
Built 9 routes to site/dist
Built standalone export to site/exports/standalone/pattern-map-v16.html

sha256(site/exports/standalone/pattern-map-v16.html)
874d8059c91f4a38ae7292d54b27b6edb01179f6313a94e54e5608cd0ca32889

sha256(git show 8aa5f94:site/exports/standalone/pattern-map-v16.html)
874d8059c91f4a38ae7292d54b27b6edb01179f6313a94e54e5608cd0ca32889
```

The regenerated standalone bytes are identical to the committed
`8aa5f94` export. The following local checks all passed:

```text
cd site && npm run check
PASS routes: 9
PASS exact first-screen framing, non-result boundary, and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS external Markdown links preserve URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragments
PASS standalone export exists

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names: all 9 routes
PASS no-script essential meaning is present in static HTML
PASS Apply route exposes ordinary/lightweight/moderate/advanced and route/stop/learning vocabularies
PASS reduced-motion, forced-colors, 200%-friendly reflow, and print hooks present
PASS no-script simulation retains first-screen, map, and application essentials
PASS synthetic Echo-removal simulation leaves Read/Explore/Apply meaning coherent
PASS historical diagram label/current-topology distinction and hash
PASS standalone HTML is self-contained for direct local opening
PASS external Markdown links preserve URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragment integrity
NOTE structural QA is not reader comprehension or effectiveness evidence

python3 qa/editorial/validate_content_interface.py
PASS immutable owner-intent checkpoint and content-interface JSON
PASS exact three-door, secondary-route, and source manifests
PASS locked six-family identity, questions, boundaries, and invariants
PASS human-problem first screen, examples, and late Echo placement
PASS claim, no-script, visual, output, and external-action obligations
PASS manuscript lengths: essay=3289 raw words; short=288 raw words
NOTE rendered site, accessibility, print, removal, and reader gates are outside this source-contract validator

python3 qa/applied/validate_framework.py
PASS six-family JSON and schema contract
PASS artifact inventory and boundary language
PASS receipt fixtures through preflight/stop logic
PASS focused applied QA complete (structural/procedural only)
```

The applied validator's own scope is explicit at
`qa/applied/validate_framework.py:1-7`: it does not execute a model, provider,
study, or external action. `qa/applied/README.md:1-26` likewise says that
these checks do not show that the framework improves decisions or that a case
works in production.

## A07 — concrete implementation paths

**Verdict: PASS.**

The canonical builder framework meets the gate independently of the concise
site rendering:

- `framework/IMPLEMENTATION_CHOICES.md:7-13` names lightweight, moderate, and
  advanced paths with best fit, inputs, outputs, typical cost, stop condition,
  and main risk. `:15-20` keeps the paths stack-neutral, maps them to team
  process/intermediary workflow/optionally approved model adaptation, and
  rejects any inherent hierarchy. `:22-78` gives route steps and concrete
  records; `:80-101` gives the selection and when-not-to-use escape hatches.
- `framework/BOUNDARIES_AND_FAILURES.md:7-28` names observable failure modes
  and recovery; `:30-70` gives hard stops, soft stops, and resume conditions;
  `:72-102` gives time, money, tokens/compute, reviewer, privacy,
  disclosure, latency, consequence, and permission boundaries; and
  `:104-136` states when not to use the full framework and preserves the
  non-negotiable boundaries.
- The rendered Apply route presents ordinary, lightweight, moderate, and
  advanced proportionate choices at `site/build.mjs:498-507`, then exposes
  the operator path, state vocabulary, agent documents, receipts, and
  templates at `site/build.mjs:509-554`. The site is a progressive summary;
  the canonical files carry the full implementation contract.
- The two domain-neutral cases are concrete, non-product fixtures. The weekly
  session case (`cases/general-research/README.md:1-98`) records a decision,
  supplied-only permission, a time/attention boundary, evidence roles,
  baseline/gap and recurrence uncertainty, disconfirmation, a provisional
  route, owner escalation, and a bounded outcome plan. The generic intake
  process case (`cases/product-and-process/README.md:1-97`) records motion,
  expected absence, versioned memory, comparison, permission, a hard stop,
  HOLD, and a later learning loop. Both explicitly say their values are
  invented fixtures, not recommendations, studies, forecasts, or evidence of
  improvement.

This is sufficient for A07. No implementation path is presented as a
mandatory architecture, product claim, or evidence that the route works in
the world.

## A08 — observable agent behavior

**Verdict: PASS.**

The canonical agent companion and rendered Apply surface specify observable
artifacts/actions for the full requirement:

- `framework/agent-playbook/QUICKSTART.md:13-64` covers decision framing,
  authority/permission, cost, default and peripheral acquisition, evidence
  registration, explicit comparison, disconfirmation, route/stop, influence,
  and the later outcome-review close-out. `:70-94` gives hard-stop behavior,
  typed failure states, and the smallest safe response shape without making
  the full framework mandatory for ordinary work.
- `framework/agent-playbook/FULL_OPERATING_GUIDE.md:97-113` specifies
  acquisition receipts and failure classes; `:115-147` source weighing and
  comparison; `:149-207` motion, absence, memory, disconfirmation, and typed
  uncertainty; `:209-240` separate route, stop, and learning fields with
  cost/permission/resume semantics; `:242-279` influence, output boundaries,
  escalation, and human authority; and `:281-323` outcome learning and
  completion conditions.
- The preflight and receipt artifacts are inspectable, not merely exhortatory:
  `framework/agent-playbook/PREFLIGHT_CHECKLIST.md:1-9` defines group status,
  evidence IDs, and the ordinary-path escape hatch; `:11-118` covers scope,
  permission, cost/stop, information, comparison, disconfirmation,
  uncertainty, influence, and learning; `:120-150` preserves the canonical
  route/stop/learning fields and no-action/resume fields. The decision receipt
  repeats these fields at `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:75-88`.
- The prior applied records remain consistent with the current source. The
  older `APPLIED_POST_REVISION_VERIFICATION_2026-08-19_cd8a756.md` recorded a
  narrow APP-02 residue at its earlier target; current
  `framework/RELATIONSHIP_MAP.md:30-46` explicitly says edge labels are
  canonical route values and that packet/provisional-packet are output
  descriptions, while `cases/signal-foundry/README.md:163-166` makes the same
  mapping explicit. `docs/ADVISORY_REVIEW_DISPOSITIONS.md` records APP-02 as
  resolved after the follow-up. The exact-commit applied validator checks the
  current relationship map, Signal Foundry route values, Quickstart outcome
  close-out, eight preflight groups, and fixture stop/learning semantics at
  `qa/applied/validate_framework.py:179-245` and `:328-370`.

### Exact rendered vocabulary audit

The canonical route values are:
`ACQUIRE`, `COMPARE`, `CLARIFY`, `ANSWER`, `ANSWER_PROVISIONALLY`, `HOLD`,
`DEFER`, `ESCALATE`, and `REFUSE`. The canonical stop values are `CONTINUE`,
`COMPLETE`, `STOPPED_BUDGET`, `STOPPED_DEADLINE`, and `STOPPED_OTHER`. The
canonical learning values are `LEARNING_PLANNED`,
`LEARNING_PENDING_OUTCOME`, `LEARNING_REVIEWED`, and
`LEARNING_NOT_APPLICABLE`. Capture/failure values include `CAPTURED`,
`PARTIAL`, `NOT_FOUND`, `FAILED`, `NOT_AUTHORIZED`, and `FAILED_CAPTURE`,
with typed uncertainty including `NOT_AUTHORIZED_OR_AMBIGUOUS`,
`INSUFFICIENT_SUPPORT`, and `MISSING_BASELINE`.

An independent visible-text and markup audit of the exact regenerated output
found:

- Apply contains every route, stop, learning, capture/failure, and selected
  uncertainty token as a contiguous visible string; it contains no `<em>`
  element at all around machine-like state text.
- Examples contains the route values used by the case procedure,
  `FAILED_CAPTURE`, and the exact Signal Foundry status. It contains no
  underscore-bearing token split by an emphasis element.
- History preserves its own exact historical status,
  `HISTORICAL ORIGIN / PARTIAL RECOVERY / NOT CURRENT TOPOLOGY`, and its
  current/historical distinction. Route/stop/learning/capture vocabularies are
  not required fields of that lineage route and are not silently introduced or
  mutated there.
- The standalone export contains the combined exact vocabulary and the exact
  historical status. Its only two `<em>` elements are the intended plain-word
  emphasis for “discrimination” and “layer”; neither contains an underscore.

This closes BOP-01 for the requested rendered surfaces. It is an output
fidelity check, not a test of whether a live agent follows the vocabulary.

## A09 — Signal Foundry bounded, not validation

**Verdict: PASS.**

The source case remains explicitly fixture-only and bounded:

- `cases/signal-foundry/README.md:1-15` states
  `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, denies product
  implementation/effectiveness/study claims, says no runtime code/data/
  credentials/provider calls/external content were imported, and identifies
  every row as an illustrative fixture rather than an observed runtime result.
- `:43-68` limits the decision to supplied, already-authorized evidence
  pointers and distinguishes technical access from permission.
- `:70-90` bounds material, acquisition, work passes, reviewer attention,
  repository-only retention/disclosure, latency, hard stops, soft stop, and
  human resume conditions. These are explicitly fixture controls, not product
  requirements.
- `:104-113` maps all six families to required records and boundaries;
  `:115-144` labels the packet trace and influence receipt as illustrative;
  `:146-170` gives the read-only procedure with canonical route values and
  separate stop/learning semantics; and `:183-194` repeats the boundary that
  must travel with every link.

### Every rendered Signal Foundry mention and cross-link

The exact regenerated `site/dist/**` and standalone output were searched
case-insensitively for every rendered `Signal Foundry` mention and then
checked for anchors whose text or destination names Signal Foundry.

- There are no rendered Signal Foundry anchors or Signal Foundry-target hrefs.
  The case is embedded in the bounded Examples route, so no cross-link can
  detach the case from its footer boundary.
- The Examples route and standalone export each contain the human-readable
  header/summary `ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION` and the exact
  machine-readable body line `Status: ILLUSTRATION_ONLY / READ_ONLY /
  NOT_VALIDATION` (`site/dist/examples/index.html:44-46` and
  `site/exports/standalone/pattern-map-v16.html:1049-1051`).
- The rendered body keeps the fixture-only and non-runtime language,
  illustrative cost/stop language, no-private-data/no-provider boundaries,
  and “no row grants permission” footer. The Examples route repeats the
  non-validation line at `site/dist/examples/index.html:80`; the standalone
  repeats it at `site/exports/standalone/pattern-map-v16.html:1085`.
- The home late-context mention says “bounded Signal Foundry illustration”;
  the essay says a bounded design illustration cannot validate the framework;
  the Boundaries route says “bounded illustration, not validation”; the Sources
  claim ledger classifies the case as `ILLUSTRATIVE_CASE` and forbids upgrading
  it to runtime behavior, validation, or permission; and the Research route
  explicitly lists that a product case does not establish implementation or
  validation. These are boundary statements, not positive effectiveness
  claims.
- The two neutral cases remain visibly separate in the same bounded Cases
  section (`site/build.mjs:558-574`), and the source cases explicitly state
  that their values are invented fixtures rather than observations or
  recommendations.

The rendered Signal Foundry inspection therefore passes A09. It does not
establish Signal Foundry behavior, implementation, permission, or
effectiveness.

## BOP remediation register

These are the stable IDs from the prior applied/rendered review. They are
recorded here as resolved findings, with the bounded fix and acceptance gate
for traceability.

### BOP-01 — underscore-bearing identifiers were mutated by rendered emphasis

**Status:** Resolved at `8aa5f94`
**Severity at discovery:** Medium
**Gates:** A08; A09; rendered standalone fidelity

**Evidence at discovery:** The prior review found bare tokens such as
`STOPPED_BUDGET` and the Signal Foundry body status split by single-underscore
emphasis in rendered Apply/Examples/standalone HTML, even though backtick code
spans passed the older checks.

**Fix in the target diff:** `site/build.mjs:114-120` now supports asterisk
emphasis only and documents the reason: canonical route/status identifiers use
underscores and must remain exact in visible and copyable records. The target
checker and semantic audit assert representative bare tokens and the exact
Signal Foundry status in Apply, Examples, and standalone output.

**Acceptance evidence:** The exact regenerated output contains no underscore
inside an `<em>` element; all audited route/stop/learning/capture/status tokens
remain contiguous. No source artifact or owner contract was rewritten to
accommodate the renderer.

**Disposition:** Accepted — bounded renderer and regression-check correction;
not evidence of live agent compliance.

### BOP-02 — source links fell back to home or dead standalone fragments

**Status:** Resolved at `8aa5f94`
**Severity at discovery:** Medium
**Gates:** A07/A08 site discoverability and standalone/cross-link integrity;
source-route accuracy

**Evidence at discovery:** The prior review found 13 dead `#source-*`
fragments in standalone and silent home-route fallbacks for unresolved local
Markdown links in the multi-page build, including `OUTCOME_REVIEW`.

**Fix in the target diff:** `site/build.mjs:63-112` adds explicit mappings for
the source paths in scope and throws on any still-unmapped local Markdown link.
`site/check.mjs:31-47` validates target files and fragments, while
`:102-109` checks every built route and every standalone fragment and rejects
`#source-*`. `qa/site/audit_site.py:187-198` mirrors the exact-token and
standalone-fragment checks.

**Independent exact-commit fragment audit:** 201 local/fragment-bearing links
across the nine built routes and standalone were checked; missing target or
fragment count was zero. Every source-route fragment used by standalone
resolved to exactly one target ID. No `href="#source-` remains.

**Semantic source-route mapping audit:**

| Source/reference family | Multi-page destination | Standalone destination | Result |
| --- | --- | --- | --- |
| `framework/templates/OUTCOME_REVIEW.md` | `../apply/index.html` | `#apply` | Apply route |
| `docs/OWNER_INTENT_V16.md`, `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`, and claims ledger | `../sources/index.html` | `#sources` | Sources route |
| Echo `RELATION_TO_V16.md`, `STATUS_AND_BOUNDARIES.md`, `PRESERVED_V15_2_INDEX.md`, `FUTURE_EXECUTION_PLAN.md`, `qa/EP_V0_1_QA.md` | `../research/index.html` | `#research` | Research route |
| Echo `VERSION_HISTORY.md` and immutable v15.2 accession | `../history/index.html` | `#history` | Lineage/history route |
| v13 live manifest, recovery/intent memo, rendered DOM snapshot, and historical diagram | `../history/index.html` | `#history` | History route |

The route distinction is intentional: Echo status and relation remain in the
Research route, while version history/accession and recovered v13 material are
lineage/history wayfinding. The links are local source pointers, not claims
that the linked source was externally reverified.

**Disposition:** Accepted — explicit semantic route mapping and fragment QA;
no source, archive, or owner-intent content change.

## Residuals and non-blocking follow-ups

These are recorded precisely so the PASS verdict is not overread.

### RESID-01 — duplicate non-route IDs remain in concatenated standalone content

**Severity:** Low (P3)
**Gates:** A13/standalone semantic quality; not an A07, A08, or A09 failure

An independent ID audit of the exact regenerated output found:

- `ordinary-ordinary-path-illustration` three times and
  `ordinary-discrimination-layer-illustration` three times in the Examples
  route and standalone;
- `short-pattern-recognition-the-discrimination-layer` twice in standalone.

All actual route/source fragments used by navigation and the BOP-02 repairs
(`main`, `top`, `read-idea`, `map`, `apply`, `examples`, `boundaries`,
`sources`, `research`, `history`, `family-F1` through `family-F6`) occur exactly
once in standalone, and the 201-link audit found no missing or multiply-targeted
fragment among those links. The duplicate IDs are generated content anchors
that are not currently navigation targets, but a future direct link to one
would be ambiguous.

**Bounded fix:** Prefix or otherwise uniquify route-derived IDs during
standalone concatenation, then add a duplicate-ID assertion. This belongs to
the broader A13/standalone semantic lane and was not part of BOP-01/BOP-02 or
the requested A07–A09 acceptance.

### RESID-02 — manual site behavior remains an owner-review residual

**Severity:** Medium (P2)
**Gates:** A13 only; not an A07, A08, or A09 finding

The tracked site QA record states that static focus order, focus target,
accessible names, and More-menu handoff were checked, but end-to-end physical
Tab traversal was not verified in the available automation surface
(`qa/site/SITE_QA_REPORT.md:97-101`). It also records that browser print-media
capture was blocked and manual print-preview review remains open
(`qa/site/SITE_QA_REPORT.md:89-95,109-112`). No screen-reader, live-agent, or
reader-comprehension result is inferred here. The owner should handle those
manual A13 checks separately if A13 acceptance is required.

### RESID-03 — source references are wayfinding pointers, not reverified evidence

**Severity:** Informational
**Gates:** Source-claim boundary; not A07–A09 failure

The rendered Sources/Research/History links point to local owner-review routes
and preserve the canonical source paths as visible labels. They do not claim
that external citations, source contents, product behavior, or research status
were newly verified. This is consistent with the source-route notice and the
tracked site QA limitation; no browse or external-source read was performed.

## Final A07/A08/A09 verdict

| Gate | Verdict at `8aa5f94` | Exact evidence | Remaining condition |
| --- | --- | --- | --- |
| **A07 — concrete implementation paths** | **PASS** | `framework/IMPLEMENTATION_CHOICES.md` gives lightweight/moderate/advanced inputs, outputs, trade-offs, failure risk, cost, stop, and when-not-to-use guidance; `framework/BOUNDARIES_AND_FAILURES.md` supplies failure/recovery, cost, permission, hard/soft stop, resume, and ordinary-path boundaries; two neutral fixtures and the bounded Signal Foundry envelope make the choices concrete. Apply renders the proportionate levels and operator path. | None for A07. The standalone duplicate-ID residual is A13/semantic quality, not missing implementation content. |
| **A08 — observable agent behavior** | **PASS** | Quickstart, full guide, preflight, receipts, templates, relationship map, ordinary-vs-layered examples, and current fixtures cover framing, acquisition, comparison, disconfirmation, typed uncertainty, escalation, cost, stopping, influence, and learning. Canonical route/stop/learning vocabularies agree, and exact rendered tokens survive in Apply/Examples/standalone. `OUTCOME_REVIEW` reaches Apply; all source route fragments resolve. | None for A08. This is a structural/procedural pass, not live-agent compliance. |
| **A09 — Signal Foundry bounded, not validation** | **PASS** | Source header/footer and fixture procedure state `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, fixture-only rows, no runtime/provider/private data, explicit cost/stop/resume envelope, no permission grant, and no effectiveness claim. Rendered Examples/standalone preserve both human-readable and underscore-bearing statuses; every rendered mention remains bounded and no Signal Foundry cross-link exists. | None for A09. This is containment/labeling QA, not product behavior or effectiveness evidence. |

## Handoff and disposition

The bounded remediation is accepted for A07–A09 at `8aa5f94`. BOP-01 and
BOP-02 are **Accepted** as resolved implementation findings. RESID-01 and
RESID-02 remain explicit owner/site follow-ups in their stated A13 scope; they
do not downgrade the requested A07/A08/A09 verdict. RESID-03 is an evidence
boundary note, not a defect.

This report is the only new file written for this review. No canonical
framework, case, site source, generated export, contract, archive, or QA
validator was edited by this review; no commit or push was made. The report
must not be cited as evidence that the framework, any agent, Signal Foundry,
or any route improves decisions or complies in live operation.
