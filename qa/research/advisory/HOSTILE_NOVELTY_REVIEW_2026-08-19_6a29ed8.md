# Hostile novelty and overclaim review — Pattern Map v16

**Reviewed source commit:** `6a29ed834bffa405942b8636a8a6b8e7b48cbf4f`
**Review date:** 2026-08-19
**Review type:** bounded hostile novelty, overclaim, provenance, and rendered-boundary review
**Review artifact:** this report only; no canonical source file was changed

## Verdict

**PASS on canonical claim containment; OPEN / NOT READY on the final integrated A07–A09 release gate.**

I found no material unsupported claim in the canonical manuscript, framework,
cases, research records, or site copy that the six-family arrangement is novel,
prevalent, causally effective, product-ready, provenance-correct, recurrence-
independent, or empirically validated. The owner-approved opening is still
editorial/conceptual framing, not a measured prevalence or model-internal
causality result. The case material remains illustrative. QA and validators are
described as integrity/implementation checks, not study results. The Echo
Problem remains subordinate, separate, preserved, unrun, and without results.

There is, however, a material rendered-output defect that a hostile review must
not overlook: the current standalone export and generated route output split
underscore-delimited operational identifiers with `<em>` tags. Examples include
`STOPPED_BUDGET`, `NOT_FOUND`, `LEARNING_PENDING_OUTCOME`,
`DECISION_BRIEF`, and Signal Foundry's status line. The canonical Markdown is
correct, but the rendered Apply, Examples, and History surfaces are not fully
faithful to it. This is a bounded renderer/content-fidelity defect, not evidence
of scientific overclaim; it blocks a clean final A07/A08/A09 certification until
fixed and re-audited.

The current repository already says that A07–A09 remain scheduled for a final
rendered-site/cross-link review. That limitation is correct and must remain
operative. Passing structural validators or prose assertions must not be
upgraded into live-agent compliance, product behavior, reader comprehension,
framework effectiveness, or a research result.

## Scope and explicit limitation

This review was deliberately hostile but bounded to repository evidence at the
pinned commit. I read the owner-locked contracts, thesis/audience contract,
artifact boundaries, source/claims ledger, acceptance criteria, decision log,
prior-art audit and dispositions, manuscript, framework, cases, Echo records,
research agenda/protocol, canonical source route, and rendered site/export.

I did **not** perform a new literature search, web browse, source-link
reverification, external citation check, provider call, model call, dataset
acquisition, participant activity, study, deployment, publication, or spend.
Existing prior-art links and references were read as repository text only. The
canonical source route itself says it is targeted rather than exhaustive and
that links must be reverified before any future public release
(`manuscript/SOURCES_AND_RESEARCH_ROUTE.md:26-33`). Accordingly, this report
does not certify prior-art completeness or current external-source validity.

The owner-intent checkpoint passed before review:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

The following bounded local checks passed, but their scope is structural or
artifact-level as documented by the repository:

```text
python3 qa/editorial/validate_content_interface.py
python3 qa/applied/validate_framework.py
python3 qa/site/audit_site.py
(cd site && node check.mjs)
git diff --check
```

The worktree was clean at the start and the only write authorized for this
review is this advisory report.

## Stable findings

Severity convention: **P1** is an owner-review/release gate; **P2** is a
bounded residual that should remain visible; **INFO/CLOSED** records a hostile
challenge that found no unsupported claim.

### HNR-01 — P1 OPEN: rendered operational identifiers are corrupted

**Finding.** The custom Markdown renderer applies underscore emphasis to plain
text after it has rendered code/link tokens. Its rule at
`site/build.mjs:104-109` includes the underscore rule `/_([^_]+)_/g`, and the
final pass is applied at `site/build.mjs:129-141`.
Source text that uses an operational identifier outside backticks can therefore
become an `<em>` span in the rendered HTML.

**Exact evidence.** The tracked standalone export at the reviewed commit shows:

- `site/exports/standalone/pattern-map-v16.html:797` —
  `STOPPED<em>BUDGET or STOPPED</em>DEADLINE`;
- `:829` — `NOT<em>FOUND, FAILED</em>CAPTURE`,
  `PARSER<em>ERROR, UNAVAILABLE, STALE, NOT</em>AUTHORIZED`, and
  `OUT<em>OF</em>SCOPE`;
- `:858` and `:894` — route/stop combinations split inside operational
  identifiers;
- `:896-897` — `LEARNING_PLANNED`, `LEARNING_PENDING_OUTCOME`,
  `DECISION_BRIEF`, `ACQUISITION_RECEIPTS`, and related receipt fields are
  split by `<em>` tags;
- `:918-920` and `:935` — preflight and decision-receipt vocabularies are
  similarly split;
- `:1050` — Signal Foundry's body status is rendered as
  `ILLUSTRATION<em>ONLY / READ</em>ONLY / NOT_VALIDATION`, even though its
  header and summary retain the exact boundary label;
- `:1112` — the product/process fixture states are rendered as
  `OBSERVED<em>MOTION</em>CANDIDATE` and `OBSERVED<em>GAP</em>CANDIDATE`;
- `:1418` — the historical verification command is rendered as
  `archive/verify<em>checkpoint</em>index.py`.

The same classes were present in the generated `site/dist/apply`,
`site/dist/examples`, and `site/dist/history` outputs captured during this
review. The canonical sources remain correct; for example
`cases/signal-foundry/README.md:1-15` has the exact status
`ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, and the applied vocabulary is
correct in `qa/applied/validate_framework.py:158-201`.

`site/check.mjs:61-79` checks selected words and malformed anchor start tags,
but it does not assert that identifiers survive rendering without an `<em>`
inside them. `qa/site/audit_site.py:145-184` checks vocabulary presence and
static route semantics, not token fidelity. Thus the current green checks do
not detect this defect.

**Governing requirements.** A07 requires inspectable implementation choices;
A08 requires observable agent behavior; A09 requires the Signal Foundry
boundary on every rendered surface; A11 prohibits claim/status language from
exceeding evidence (`docs/V16_ACCEPTANCE_CRITERIA.md:19-23`). The QA contract
also says rendered evidence establishes structure only, not live-agent
compliance or effectiveness (`qa/README.md:9-17,19-31`).

**Bounded recommendation.** Protect identifier-like tokens in the renderer or
require the affected source tokens to be code-delimited, regenerate the
standalone export and route output, and add a regression assertion that known
route/stop/learning/capture/status identifiers do not contain inline `<em>` or
`<strong>` splits. Re-run the rendered cross-link and Signal Foundry checks on
the resulting integrated commit. Do not edit the canonical sources as a
workaround in this review; the current evidence should remain marked **A07–A09
not finally closed** until the renderer/output is corrected.

All HNR-01 line citations are anchored to the exact reviewed commit blob (for
example, `git show 6a29ed8:site/exports/standalone/pattern-map-v16.html`), not
to any later uncommitted working-tree remediation. This keeps the finding
stable if a sibling task repairs and regenerates the output after this report.

### HNR-02 — P1 OPEN: structural QA does not certify A07–A09

**Finding.** The current evidence is appropriately scoped, but a release note
or future summary could accidentally read “all validators pass” as “A07–A09
pass.” That inference is explicitly disallowed by the repository's own
records, and the rendered-token defect makes the inference especially unsafe.

**Exact evidence.**

- `docs/DECISION_LOG.md:334-337` says the applied work establishes builder and
  agent artifact completeness for the pre-site scope, but **does not** establish
  live-agent compliance, Signal Foundry product behavior, reader
  comprehension, or framework effectiveness; A07–A09 remain scheduled for a
  final rendered-site/cross-link review.
- `docs/V16_ROADMAP.md:21` keeps the deliberate review loop in progress, with
  post-site A07–A09 and final novelty/accessibility/operator reviews still next.
- `docs/V16_ROADMAP.md:39-45` requires re-auditing A07/A08 after site
  integration, re-auditing A09 after every Signal Foundry cross-link/rendered
  surface, and citing the integrated commit rather than the manuscript-only
  snapshot.
- `qa/README.md:9-17` says manuscript/scaffold-only evidence cannot close the
  gates; `qa/README.md:26-31` limits current rendered evidence to structure and
  rendering, with physical keyboard and print residuals still open.
- `qa/site/SITE_QA_REPORT.md:1-5,44-53,99-104` explicitly calls the checks
  implementation/artifact QA, not comprehension, behavioral effectiveness,
  model quality, empirical, participant, or research evidence.
- `docs/DECISION_LOG.md:427-441` records that validators pass after a prior
  renderer correction while still describing screenshots/rendered PDF as
  implementation QA and preserving manual residuals. The current underscore
  defect shows why the validator pass cannot substitute for a hostile rendered
  inspection.

**Governing requirements.** A07–A09 and A11, plus the explicit QA containment
rules in `docs/V16_ACCEPTANCE_CRITERIA.md:19-23` and `qa/README.md:9-31`.

**Bounded recommendation.** Keep the final disposition as **Deferred / Accepted
with revision**, not “certified,” until (1) the renderer/token-fidelity issue is
fixed, (2) every Signal Foundry mention and cross-link is inspected in the
rendered routes and standalone export, and (3) the final verdict cites
`6a29ed8` or its corrected successor. Report only artifact completeness and
inspectability unless a separately authorized live-agent, product, reader, or
empirical evaluation occurs.

### HNR-03 — P2 WATCH, currently contained: PAOB-03 is editorial framing, but its
machine-readable status is not surfaced on the first screen

**Finding.** The “AI slop often begins before the model writes a word” framing
remains an owner-approved conceptual proposition. It is not currently written
as a measured prevalence, model-internal mechanism, or empirical result. The
residual is that the frozen claim-status field is recorded in the content
contract but not visibly emitted as a first-screen label by the site builder.
That is a future verification risk, not a present overclaim in the reviewed
copy.

**Exact evidence.**

- `docs/CONTENT_INTERFACE_V16.json:6-16` records the exact headline,
  standfirst, and `claim_status` value
  `owner-approved-conceptual-framing-not-measured-prevalence`.
- `docs/CONTENT_INTERFACE_FREEZE_V16.md:31-49` says the headline/standfirst
  are owner-approved conceptual framing, not measured prevalence or
  model-internal causality, and must not be presented as a research result.
- The rendered first screen at `site/dist/index.html:30-32` preserves the
  approved headline and standfirst and adds the bridge, “This is a broad
  proposal about the room before the answer.” It contains no prevalence number,
  model measurement, causal estimate, or result language.
- `site/build.mjs:432-434` emits the approved headline/standfirst/bridge; it does
  not visibly render the JSON `claim_status` string. The later Sources route
  does provide explicit claim control, including “not a literature-defense
  opening” and no outcome validation (`site/dist/sources/index.html:28,35-42`).
- `docs/DECISION_LOG.md:251-259` accepts PAOB-03 as owner-approved editorial
  framing and expressly says future site wording may not present it as an
  empirical technical fact.

**Governing requirements.** PAOB-03 disposition in D-013, the frozen content
interface, A01/A02 human-first ordering, and A11 scientific/novelty claim
containment.

**Bounded recommendation.** Preserve the approved headline and manuscript
framing; do not replace it with an unsupported “measured” or “AI causes” claim.
For a later public-release hardening pass, either keep the current broad-
proposal bridge and add a nonintrusive owner-approved conceptual-status cue, or
add a DOM regression assertion that the first screen contains no prevalence or
causal-result language. No manuscript softening is warranted on this review.

### HNR-04 — INFO/CLOSED: targeted prior-art route is present, not exhaustive

**Finding.** PAOB-02 remains correctly bounded. The canonical route names a
targeted wayfinding route, supplies an archived adjacent-fields map, a
classified reference list, and selected primary/official entry points. It does
not claim systematic coverage or prove novelty.

**Exact evidence.**

- `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:26-33` says “targeted,” “not a
  systematic or exhaustive literature review,” and “re-verify before any public
  release.”
- `:35-52` names selected Information Foraging, Metareasoning, W3C PROV-O,
  claim-provenance, Cochrane, retrieval-augmented generation, mixed-initiative,
  and human–AI interaction entry points, then states that these sources
  constrain claims and expose overlap but do not validate the six-family
  arrangement or establish improved outcomes.
- The rendered Sources route preserves the boundary at
  `site/dist/sources/index.html:28,34-38`; the standalone export preserves it
  at `site/exports/standalone/pattern-map-v16.html:1216,1222-1226`.
- PAOB-02's corrected route is therefore present in both canonical and rendered
  surfaces. The site maps source links to local route pages by design
  (`site/build.mjs:63-101`); this changes presentation routing, not the
  targeted/non-exhaustive claim.

**Governing requirements.** PAOB-02/D-013, the source-authority order, and
A11's prohibition on invented novelty or exhaustive-field-map language.

**Bounded recommendation.** Keep the route described as targeted and
non-exhaustive. Before any future authorized publication, reverify the existing
external links and update only through the project's documented source/decision
process. A new literature search was outside this review and is not implied by
this report.

## Hostile challenge matrix: claim classes checked

The following are explicit no-finding results, subject to the rendered fidelity
and final-gate findings above.

### Novelty and prevalence — contained

The manuscript says the strongest challenge is that this is “old work under a
new arrangement,” names prior fields, and rejects an empty-space/invention
claim (`manuscript/PATTERN_RECOGNITION_V16.md:272-280`). The claims ledger
classifies the broad premise/design as `OWNER_PREMISE`,
`CONCEPTUAL_SYNTHESIS`, or `DESIGN_HYPOTHESIS`, not measured prevalence or
novel architecture (`docs/CLAIMS_AND_SOURCE_LEDGER_V16.md:20-26,33-46`). The
six families are historical continuity and owner-locked scope, not scientifically
novel or empirically optimal (`C16-003`). The first-screen wording has no
measured denominator or prevalence estimate. No novelty or prevalence claim was
found to require downgrade beyond the HNR-03 visibility watch.

### Capability, causality, and effectiveness — contained

Implementation choices are presented as ordinary/lightweight/moderate/advanced
design options, not a mandatory stack or proof that more machinery works. The
manuscript calls for a future matched comparison under the same task, budget,
model, and human review and explicitly says no such study has run
(`manuscript/PATTERN_RECOGNITION_V16.md:315-337`). The research route states
`UNRUN / NO RESULTS / NO PROVIDER OR MODEL SELECTED` and calls validators and
fixtures integrity/inspectability only (`site/dist/research/index.html:28,35-39`).
No “improves,” “works,” “expert-grade,” “causes,” or product-readiness claim was
found standing without a boundary. HNR-02 records the important distinction
that clean implementation QA is not capability or effectiveness evidence.

### Provenance, recurrence, and independence — contained

The six-family source-weighing rules keep provenance, correctness, authority,
permission, recurrence, and independence distinct. The fictional “nine
reports, one announcement” example says the reports do not become false, but
repetition does not create new origins and independence remains unestablished
(`manuscript/PATTERN_RECOGNITION_V16.md:201-229`). The ledger rejects the
upgrades “provenance is correctness,” “recurrence is independent corroboration,”
and “access is permission” (`docs/CLAIMS_AND_SOURCE_LEDGER_V16.md:37,40`). The
neutral/product-process fixtures preserve `UNKNOWN`, `RECURRENCE`, missing
baseline, and permission boundaries. No provenance laundering or recurrence-
to-independence overclaim was found.

### Case-as-validation — contained, with rendered token defect

Signal Foundry's canonical case is explicit:
`ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, no runtime/data/credentials/
provider calls, every row illustrative, and no product/effectiveness/empirical
claim (`cases/signal-foundry/README.md:1-15,40-41`). It further says a bounded
packet does not prove that a product could create it reliably
(`cases/signal-foundry/README.md:135-144`) and repeats the boundary for every
link (`:183-194`). The rendered route keeps the exact boundary in the Examples
section heading and summary (`site/exports/standalone/pattern-map-v16.html:1049`),
but HNR-01 shows that the body status is malformed at `:1050`. This is a
rendering fidelity defect, not a conversion of the case into validation.

The two domain-neutral cases likewise state that values are invented fixtures,
not data, studies, forecasts, recommendations, product claims, or evidence that
the framework improves a decision (`cases/general-research/README.md:1-9`,
`cases/product-and-process/README.md:1-8`). Their “why useful” language is
mechanistic illustration, not a result, and their boundaries explicitly reject
independent corroboration, prevalence, causality, and general efficacy.

### QA-as-results — contained, but final gate remains open

The repository is unusually explicit that hashes, schemas, deterministic
fixtures, validators, site checks, screenshots, and PDF renders establish
artifact integrity or implementation structure only. The Echo status record
also says a passing hash or offline test is an integrity result, not a research
result (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:28-43`). The site QA
report says the same (`qa/site/SITE_QA_REPORT.md:1-5,53,99-104`). No QA result was
presented as a participant, model, reader, causal, or effectiveness outcome.
The hostile issue is not overclaiming in the prose; it is that HNR-01 shows the
current rendered output is not fully faithful, and HNR-02 prevents treating
green structural checks as final A07–A09 certification.

### Echo takeover — explicitly prevented

The Echo Problem is marked `ECHO-01`, `EP v0.1`, “preserved internal owner-
review successor; unrun; no results; not published” (`research/the-echo-problem/
README.md:1-5`). Its README states that it is not the opening or definition of
v16, not a completed paper, not a validation result, and not a claim that origin
accounting is novel (`:33-40`). The canonical source route and rendered Sources
route preserve this exact separation (`manuscript/SOURCES_AND_RESEARCH_ROUTE.md:
54-62`; `site/dist/sources/index.html:39-42`). The broader research route keeps
Research Track 01/ECHO-01 separate from Research Track 02/DL-PLAYBOOK-01 and
states that neither has results (`site/dist/research/index.html:28-42`).

The manuscript's removal test also passes: the Echo example is late and
subordinate, and removing it leaves the upstream-choice thesis, the other five
families, the learning loop, and human-judgment boundary coherent
(`manuscript/PATTERN_RECOGNITION_V16.md:224-229`). No Echo result, selected
model, discovered provenance, or origin-accounting definition of v16 was found
in the reviewed output.

## PAOB verification summary

| Item | Canonical evidence | Rendered evidence | Hostile result |
| --- | --- | --- | --- |
| PAOB-01: Echo source route | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:54-62` directly links EP v0.1 and its status/no-results record; it says unrun/no results and imports no result/model/discovered provenance. | `site/dist/sources/index.html:39-40` and standalone `:1228` retain the separate EP v0.1/status/no-results language; the research route exposes the status and all no-results boundaries at `site/dist/research/index.html:28-42,150-164`. | **Present and contained.** Local route mapping is intentional; no Echo takeover. |
| PAOB-02: targeted prior-art route | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:26-52` names the archived map/reference list and selected primary/official sources, explicitly targeted/non-exhaustive and non-validating. | `site/dist/sources/index.html:28,34-38` and standalone `:1216,1222-1226` retain the same boundary. | **Present and contained.** Not a new/exhaustive literature claim. |
| PAOB-03: “AI slop often begins…” | `docs/CONTENT_INTERFACE_V16.json:6-16` and `docs/CONTENT_INTERFACE_FREEZE_V16.md:31-44` classify it as owner-approved conceptual framing, not measured prevalence/model causality. | `site/dist/index.html:30-32` preserves headline/standfirst and “broad proposal” bridge with no metric/result language. | **Editorial framing confirmed.** HNR-03 is only a future status-visibility watch. |
| PAOB-04 / A07–A09 | D-013/D-016 and `docs/V16_ROADMAP.md:39-45` require final integrated rendered/cross-link re-audit; `qa/README.md:19-31` limits current evidence to structure/rendering. | Structural checks pass, but HNR-01 finds malformed operational tokens in standalone and generated Apply/Examples/History routes. | **Not falsely certified.** Keep final gate open; prose and green validators are insufficient. |

## Explicit no-results and two-project separation confirmation

No result is being claimed here for either project.

- **Broader v16 / DL-PLAYBOOK track:** the agenda and matched-budget protocol
  are future, unrun design materials. No task corpus, model, provider, sample,
  participant, empirical run, preregistration, or result exists in this review.
  The rendered status is `UNRUN · NO RESULTS · NO PROVIDER OR MODEL SELECTED`
  (`site/dist/research/index.html:28,35-39`).
- **Echo / ECHO-01 / EP v0.1:** the preserved successor is a separate
  origin-accounting track. Its explicit record says no model/empirical/pilot/
  participant study ran, no provider was called, no dataset was acquired, and
  the preserved package is a protocol-and-implementation checkpoint, not a
  result (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:8-18`). All
  unfavorable classes, including null, harmful, shortcut-driven, unstable,
  nontransfer, and stopped/quarantined, remain possible categories rather than
  observed outcomes (`:45-67`).
- **Firebreak:** Echo is one subordinate worked example and research track
  inside the broader history; it does not define the six-family v16 map. The
  two projects must remain separately named, separately statused, and
  separately reviewable.

## Disposition

1. **Accept** the core novelty/overclaim boundary: no unsupported novelty,
   prevalence, capability, causal/effectiveness, provenance, recurrence,
   independence, case-validation, QA-as-results, or Echo-takeover claim was
   found in canonical content.
2. **Accept with revision** PAOB-01 and PAOB-02: both corrected routes remain in
   canonical and rendered outputs, with targeted/non-exhaustive and separate/
   unrun/no-results language intact.
3. **Accept with monitoring** PAOB-03: the headline remains editorial/conceptual
   framing. Preserve the owner-approved wording and guard against future
   rendering that presents it as measured prevalence or technical causality.
4. **Defer final certification** of PAOB-04/A07–A09: repair the bounded
   renderer token-fidelity defect, regenerate the rendered surfaces, inspect all
   Signal Foundry mentions/cross-links, and issue the final verdict against the
   corrected integrated commit. Do not use “all validators pass” as a substitute
   for that verdict.
