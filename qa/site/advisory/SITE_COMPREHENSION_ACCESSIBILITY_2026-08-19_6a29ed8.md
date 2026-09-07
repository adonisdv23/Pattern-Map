# Site comprehension and accessibility advisory

Reviewed commit: `6a29ed834bffa405942b8636a8a6b8e7b48cbf4f` (`codex/pattern-map-v16-foundation`), including its site parent `932366a`.

Review date: 2026-08-19

Review mode: bounded read-only proxy audit. This report is advisory implementation evidence, not a cold-reader result, participant study, screen-reader certification, or evidence that the framework improves outcomes.

## Scope and evidence boundary

I read the repository instructions and locked governing documents before inspection, including the owner-intent contract, thesis/audience contract, artifact boundaries, source lineage, acceptance criteria, decision log, and review/disposition protocol. The owner-intent checkpoint passed before review:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

Inspected directly:

- `site/build.mjs`, `site/check.mjs`, `site/src/site.css`, `site/src/site.js`, `site/README.md`, and `site/scripts/generate_review_pdf.py`;
- the committed `site/exports/standalone/pattern-map-v16.html` and `site/exports/pattern-map-v16-owner-review.pdf`;
- `docs/CONTENT_INTERFACE_FREEZE_V16.md` and `docs/CONTENT_INTERFACE_V16.json`;
- `qa/site/SITE_QA_REPORT.md`, `qa/site/audit_site.py`, `qa/visual/VISUAL_QA_REPORT.md`, and `qa/visual/VISUAL_NEEDS.md`;
- the committed responsive screenshots and all six rendered PDF pages; and
- the actual local routes served from the committed `site/dist/` output at 390×844 and 1440×1000 browser viewports.

Read-only checks run during this review:

```text
cd site && npm run check                         PASS
python3 qa/site/audit_site.py                    PASS
python3 qa/editorial/validate_content_interface.py PASS
pdfinfo site/exports/pattern-map-v16-owner-review.pdf  6 pages; Tagged: no
```

I also ran local, non-mutating checks for standalone duplicate IDs and fragment targets, route-local fragment targets, viewport overflow, and nominal CSS color contrast. No external source was opened or reverified, no provider or model was called, and no deployment, publication, study, or participant activity occurred.

## Overall assessment

The integrated site is substantively human-first at the opening. The desktop capture shows the approved headline and standfirst before protocol, research status, or Echo material, followed by all three principal doors. The home short entry contains the broad thesis, the six-family map names are present in order, and the current relationship view is visibly separate from the labeled historical v13 diagram. The local route and static no-script checks pass, and the PDF render is visually legible across all six pages.

The review does not support a final A13 acceptance yet. Four implementation findings need bounded correction or explicit owner disposition: mobile header navigation hides the principal links, several small text/focus colors are below common contrast thresholds, the standalone export is not a clean single-document accessibility surface, and standalone/source link resolution has dead or non-specific destinations. A lower-severity comprehension risk is that the map's first visible card copy introduces specialist vocabulary before the glossary. Physical keyboard traversal, screen-reader review, print preview, and real-reader comprehension remain owner residuals rather than claimed passes.

## Findings

### SITE-MOB-001 — Principal route navigation disappears from narrow-route headers

Severity: **Medium (P2)**

Type: accessibility/usability defect; static and browser evidence

Evidence:

- At `site/src/site.css:154-155`, `.secondary-nav-wrap` is `display: none` until JavaScript adds `.is-open`.
- At `site/src/site.css:450-452`, the ≤760px media rule sets `.primary-nav a { display: none; }` while leaving only `.nav-more` visible.
- The only corresponding behavior in `site/src/site.js:32-39` toggles the secondary routes; it never reveals the three principal links.
- In the actual 390×844 browser DOM for `/apply/`, the principal navigation contained `Read the idea`, `Explore the map`, and `Apply it` with computed `display: none`; `More` was visible and collapsed. Opening `More` exposed only `Examples`, `Boundaries`, `Sources`, `Research`, and `History`.

Impact:

On a nested route, a mobile keyboard or touch user cannot move directly among the three principal doors from the header. They must return to the wordmark/home and use the door cards, or rely on links later in the page. With JavaScript disabled, the More button cannot open the secondary menu either. The home page remains reachable and the principal doors remain in the document, so this is not a total content loss, but the responsive header does not provide complete route operation.

Governing gate: **A13** (complete keyboard operation and mobile behavior), with **A06** (no-script reading/navigation path); `docs/CONTENT_INTERFACE_FREEZE_V16.md:176-193`.

Bounded correction:

Keep the principal links available at narrow widths, either outside the disclosure or inside one disclosure that contains all eight route links. If a single disclosure is used, update its accessible name/state and focus handoff, provide a no-script-visible fallback, and verify that keyboard and touch users can reach Read, Explore, and Apply from every route. Add `aria-current="page"` to the active route while making the visual state remain non-color-only.

### SITE-A11Y-002 — Small text and focus indicator colors are too low-contrast on the paper surface

Severity: **Medium (P2)**

Type: accessibility defect; static CSS calculation plus browser-computed style evidence

Evidence:

- The token definitions are at `site/src/site.css:2-19`; the focus indicator is `site/src/site.css:55-58` (`outline: 3px solid #efb24e`).
- Against the nominal `--paper: #f4f0e8` background, the calculated contrast ratios are approximately: `--muted #6c7779` 4.06:1; F1 teal `#277f7e` 4.18:1; F2 green `#5d8554` 3.73:1; F3 purple `#8066a3` 4.25:1; F4 orange `#c66c3e` 3.29:1; F5 ochre `#ae8a37` 2.85:1; and F6 blue `#4b7591` 4.34:1.
- These colors are used for small text, not only decoration: `.family-id` and family detail terms at `site/src/site.css:300-308`, topology family IDs at `site/src/site.css:321-322`, `.node-kicker` at `site/src/site.css:316`, `.lineage-step` at `site/src/site.css:436`, small metadata, and muted explanatory text. They are below the usual 4.5:1 normal-text target on one or more family cards.
- The browser computed the active family button focus style as `rgb(239, 178, 78) solid 3px`; `#efb24e` is approximately 1.66:1 against `--paper`, below a robust 3:1 focus-indicator contrast target.

Impact:

Family names and the prose boundaries remain dark and readable, so the map's meaning is not solely color-dependent. However, the family IDs, state/metadata labels, and focus ring are the cues most likely to be used while navigating the map; low contrast makes those cues difficult to perceive, especially for low-vision users and in the small monospace sizes used here. The current forced-colors rules help when forced colors are enabled but do not correct ordinary-mode contrast.

Governing gate: **A13** (visible focus and basic accessibility; non-color-only state communication), `docs/CONTENT_INTERFACE_FREEZE_V16.md:176-185`.

Bounded correction:

Choose darker muted and family text tokens that meet the target on the actual card/paper backgrounds. Give the focus ring a high-contrast neutral or dual-ring treatment that remains visible against both paper and card borders. Recheck every text use separately from border/dot decoration, and rerun ordinary, forced-colors, and focus-state screenshots.

### SITE-STANDALONE-003 — The standalone export is a multi-route bundle with duplicate IDs and ten level-one headings

Severity: **Medium (P2)**

Type: standalone semantic/accessibility defect; static evidence

Evidence:

- `site/build.mjs:643-656` extracts each route's `<main>` and concatenates the bodies into one outer standalone document without route-specific ID or heading normalization.
- The committed `site/exports/standalone/pattern-map-v16.html` contains **10 `<h1>` elements**: the standalone title plus the nine route titles.
- A local ID audit found duplicate IDs: `short-pattern-recognition-the-discrimination-layer` appears twice, while `ordinary-ordinary-path-illustration` and `ordinary-discrimination-layer-illustration` each appear three times.
- The existing semantic audit checks the nine routed documents (`qa/site/audit_site.py` and `qa/site/SITE_QA_REPORT.md:44-52`) but does not run the same heading/ID checks against the standalone export.

Impact:

The export opens directly and its visible content is present, but assistive-technology heading navigation and fragment targeting are ambiguous in a single document. A reader opening the standalone file encounters repeated top-level route headings, and a hash target can resolve to the first of several duplicate IDs. This is particularly relevant because the standalone export is an explicit required output, not merely a build scratch file.

Governing gate: **A13** (semantic heading order and standalone export), **A06** (print/no-script progressive disclosure); `docs/CONTENT_INTERFACE_FREEZE_V16.md:130-145` and `176-193`.

Bounded correction:

Give each standalone route section a unique, named section heading structure under the export title, prefix all route-derived IDs (including repeated short/example IDs), and add a standalone semantic/duplicate-ID audit to `site/check.mjs` or `qa/site/audit_site.py`. Preserve the visible route hierarchy and all existing local hash destinations.

### SITE-LINK-004 — Thirteen standalone source links resolve to missing fragments

Severity: **Medium (P2)**

Type: link-integrity defect; static evidence

Evidence:

- `site/build.mjs:94-101` deliberately falls back to `#source-${slug}` in standalone mode when a Markdown source path is not mapped to a site route.
- A local audit of every `href="#..."` in the committed standalone export found 13 unique fragment targets with no matching `id`: `source-docs-owner-intent-v16-md`, `source-docs-thesis-and-audience-contract-v16-md`, `source-future-execution-plan-md`, `source-preserved-v15-2-index-md`, `source-qa-ep-v0-1-qa-md`, `source-relation-to-v16-md`, `source-status-and-boundaries-md`, `source-templates-outcome-review-md`, `source-transfers-v14-complete-2026-08-18-05-historical-v13-live-site-reference-manifest-json`, `source-transfers-v14-complete-2026-08-18-05-historical-v13-live-v13-rendered-dom-snapshot-html`, `source-transfers-v14-complete-2026-08-18-05-historical-v13-pattern-recognition-diagram-v12-png`, `source-transfers-v14-complete-2026-08-18-05-historical-v13-v13-recovery-and-intent-memo-md`, and `source-version-history-md`.
- `site/check.mjs` and the current QA report's “local route/assets link integrity” pass check file targets and external-anchor syntax, but do not validate same-document fragment existence. The nine routed documents had no missing local fragments in the same audit.

Impact:

In the standalone HTML, selecting one of these source links changes the hash without moving the reader to any content. This weakens the requested direct-open/source wayfinding while leaving the canonical source manifest visible. It is a standalone export defect, not evidence that the underlying source files are absent.

Governing gate: **A13** (standalone export and link operation), **A06** (progressive disclosure/source route), and the site link-integrity obligation; `docs/CONTENT_INTERFACE_FREEZE_V16.md:176-193`.

Bounded correction:

For every source link, either include a corresponding labeled section/anchor in the standalone export, resolve it to an existing route anchor such as `#sources`, `#research`, or `#history`, or render an explicitly non-linking source label when the source is not bundled. Add a fragment-target check for both routed pages and standalone output so this cannot regress.

### SITE-ECHO-005 — The Echo source link returns to Research top rather than the Echo section

Severity: **Low (P3), owner confirmation useful**

Type: separation/navigation clarity risk; static/browser evidence

Evidence:

- The canonical source `research/README.md:19` links `the-echo-problem/README.md` as Research Track 01 / ECHO-01.
- `site/build.mjs:84-86` maps any `the-echo-problem` path to the generic `research` route. In the rendered routed page this becomes `<a href="../research/index.html"><code>the-echo-problem/README.md</code></a>`; in standalone mode it becomes a generic `#research` target.
- `renderResearch` at `site/build.mjs:580-590` gives the Echo section a heading and status text but no stable `id="echo"` fragment. Browser inspection found the only Echo-named anchor on the Research page is the source-path link above; it lands at the Research route top, not directly on the Echo callout.

Impact:

The page does visibly label “The Echo Problem — separate project — unrun — no results,” and synthetic Echo removal leaves the three principal routes coherent. The issue is narrower: a reader following the promised separate-project source link does not jump to the Echo identity/status section, and the link itself is a path-like label rather than a clear project destination.

Governing gate: **A10** (separate, preserved, no-results project and clear link), plus `docs/CONTENT_INTERFACE_FREEZE_V16.md:146-160` and acceptance criteria A10/site deliverable at `docs/V16_ACCEPTANCE_CRITERIA.md:67-76`.

Bounded correction:

Give the Echo section a stable `id="echo"`, resolve `the-echo-problem/...` links to the Research route's `#echo` fragment (and the equivalent standalone fragment), and present a plain-language link label such as “The Echo Problem — separate project — unrun — no results.” Keep the existing subordinate placement and no-results wording intact.

### SITE-COMP-006 — Map lead copy introduces specialist vocabulary before the plain-language translation

Severity: **Low (P3) / proxy comprehension risk**

Type: progressive-disclosure and general-reader friction; static/browser evidence, not reader evidence

Evidence:

- At the actual `/map/` route with details closed, the first two visible cards read:
  - F1: “Widen a **task-scoped information aperture** beyond the obvious route while treating every result as a candidate for inspection.”
  - F2: “Keep source role, **claim-scoped authority**, support, relevance, recurrence, origin, provenance, and permission distinct.” The visible “How it works” line then adds “typed relationships and explicit source roles.”
- The question lines are plain and useful (“What might the default path have overlooked?” and “What role does each source play for this exact claim?”), but the explanatory sentence immediately beneath each question contains several specialist labels before a reader reaches the optional glossary.
- The contract requires essential sentences to work without popovers and says technical state/detail should not replace plain language: `docs/CONTENT_INTERFACE_FREEZE_V16.md:130-145`; the acceptance gate is **A06**, with a secondary A01/A04 comprehension concern.

Impact:

This is a proxy risk, not a claim that a real reader failed. A thoughtful general reader can use the questions and dark family names, and the technical details are mostly closed. Nevertheless, the first explanatory sentence for the map currently makes jargon the price of understanding what F1/F2 do, which can make the map feel more like an architecture catalog than a continuation of the human idea.

Bounded correction:

Rewrite the visible lead sentences in ordinary language while retaining every boundary; for example, “Look beyond the obvious path, but treat what you find as something to inspect,” and “Ask what role each source plays for this claim; keep support, relevance, origin, and permission separate.” Move labels such as `task-scoped information aperture`, `claim-scoped authority`, and `typed relationships` into the closed implementation detail/glossary, where they can remain available without carrying the reader-facing sentence.

### SITE-PDF-007 — PDF companion is visually clear but not tagged for assistive technology

Severity: **Low (P3), owner decision required if PDF is reader-facing**

Type: print/PDF accessibility residual; static evidence

Evidence:

- `pdfinfo site/exports/pattern-map-v16-owner-review.pdf` reports six letter-sized pages, no JavaScript/forms, and `Tagged: no`.
- All six committed Poppler renders were visually inspected: no clipping, overlap, or unreadable glyphs was observed; the PDF contains the opening, doors, six-family table, examples, application choices, history label, and QA boundary.
- The PDF is generated with ReportLab's `BaseDocTemplate` in `site/scripts/generate_review_pdf.py`; no tagged-PDF structure is produced by that script.

Impact:

The PDF works as a visual owner-review companion, but a screen reader cannot rely on a tagged reading order, table semantics, or document structure. The standalone HTML is the stronger semantic/accessibility route; the current package does not explicitly state that the PDF is visual-only.

Governing gate: **A13** and the required visually inspected PDF companion in `docs/CONTENT_INTERFACE_FREEZE_V16.md:176-193`.

Bounded correction:

Either produce a tagged PDF with a checked reading order and table headings, or state in the handoff/PDF cover that it is a visual review companion and direct assistive-technology readers to the semantic standalone HTML. If the PDF remains in scope for screen-reader use, add a tag/structure verification to the release checklist.

## Explicit owner-review residuals

These are not presented as completed passes or as defects proven by participant evidence. They are the remaining manual checks required by A13 or by the comprehension contract.

### OWNER-RESIDUAL-008 — Physical keyboard traversal

Severity: **Medium (A13 follow-up)**

The site QA report records static order, focus target, accessible names, and More-menu focus handoff, but also states that synthetic Tab events did not advance reliably and that end-to-end physical traversal remains unverified (`qa/site/SITE_QA_REPORT.md:87-91, 99-102`; `qa/visual/VISUAL_QA_REPORT.md:31-35, 51-55`). An owner should traverse Home, Read, Explore, Apply, and at least one secondary route at desktop and narrow width using a physical keyboard: skip link, all route links, More open/close, focus return, family focus buttons, Show all, summaries/details, and all local links.

### OWNER-RESIDUAL-009 — Supported screen-reader review

Severity: **Medium (A13 follow-up)**

The recorded evidence is a static landmark/heading/name audit (`qa/site/SITE_QA_REPORT.md:79-85`), not a supported screen-reader pass. No reviewed artifact records VoiceOver, NVDA, or another screen-reader traversal. The owner should verify the first-screen reading order, the three door names/promises, map family questions and `aria-live` focus status, Details/Summary announcements, hidden mobile navigation, historical image alt/caption, and the no-script/standalone route reading order. Record the result separately; do not convert this proxy report into screen-reader evidence.

### OWNER-RESIDUAL-010 — Browser print preview

Severity: **Medium (A13 follow-up)**

The static print hooks and PDF renders pass, but the site QA reports that browser print-media emulation was blocked and that a manual print-preview check remains open (`qa/site/SITE_QA_REPORT.md:83-85, 99-103`; `qa/visual/VISUAL_QA_REPORT.md:37-45, 51-55`). The owner should inspect the Home, Read, Explore, Apply, Examples, Sources, Research, and History print previews for retained thesis/family/example/boundary/source text, useful URLs, page breaks, expanded details, and absence of clipped tables or the historical diagram.

### OWNER-RESIDUAL-011 — Cold-reader comprehension and technical density

Severity: **Advisory / not a measured result**

The browser and screenshot evidence establish composition, not comprehension. The opening is structurally aligned with A01-A04, while `SITE-COMP-006` identifies a sentence-level jargon risk on the map. The contract's 60–90-second and 10–15-minute timing language remains an editorial estimate, not an observed reading result. A separately authorized cold-reader/mentor review is still needed to determine whether the broad idea can be restated without reducing v16 to Echo/origin accounting, and whether the map/apply routes remain proportionate for a thoughtful general reader.

### OWNER-RESIDUAL-012 — External source-link re-verification before publication

Severity: **Low (release follow-up)**

Local route/link syntax and the parenthesized DOI regression pass. The QA report explicitly says existing targeted source links are pointers, not newly reverified evidence, and that no external source read occurred (`qa/site/SITE_QA_REPORT.md:99-104`). Before any future authorized publication, re-verify the external destinations and their wording. This review intentionally did not browse them.

## Acceptance-gate snapshot

This snapshot is a review disposition, not final owner acceptance.

| Gate | Proxy result at this commit | Reason / remaining action |
| --- | --- | --- |
| A01 | **Structural pass; cold-reader residual** | First screen and short entry state upstream choices, inspectability/correction, human judgment, and breadth beyond origin counting. No real 90-second comprehension result was run. |
| A02 | **Pass in inspected desktop/browser evidence** | Human problem, approved headline/standfirst, and doors precede protocol/research/Echo. Narrow doors stack immediately after the standfirst without decorative media. |
| A03 | **Pass (static/browser)** | F1-F6 names/questions and current relationship view are visible in order. |
| A04 | **Not adjudicated by this proxy** | Voice is consistent with the earlier editorial evidence, but this lane did not run a mentor/cold-reader review. |
| A05 | **Estimate only** | Canonical essay timing remains the recorded editorial estimate; this review did not observe readers. |
| A06 | **Partial / bounded corrections recommended** | No-script/closed-details meaning is present, but map lead jargon and standalone fragment/heading issues weaken progressive disclosure. |
| A10 | **Status/separation pass; link correction recommended** | Echo is late, labeled separate/unrun/no results, and removal leaves principal routes coherent; the source link does not jump directly to the Echo section. |
| A13 | **Partial / owner residuals and findings open** | Responsive screenshots, static semantics, no-script, reduced motion, forced colors, and PDF rendering have evidence; mobile header navigation, contrast, standalone semantics, physical keyboard, screen reader, and print preview need follow-up. |
| A16 | **Pass for this review** | Owner-intent hash passed; no research-driven thesis substitution was observed. |
| A17 | **Pass for this review** | No locked owner-intent file was edited; this report proposes bounded implementation/copy corrections only and does not alter canonical intent. |

## Disposition guidance for the integrator

The findings should be entered into the controlled disposition ledger as `Accepted`, `Accepted with revision`, `Deferred`, or `Rejected` after owner review. The report itself does not authorize changing the locked headline, standfirst, six-family identity/order/questions, Echo separation, historical label, or action boundaries. Any copy correction for `SITE-COMP-006` should preserve the same family meaning and boundaries; any decision to leave the PDF untagged should explicitly record the PDF's visual-only status and the semantic HTML as the accessible route.
