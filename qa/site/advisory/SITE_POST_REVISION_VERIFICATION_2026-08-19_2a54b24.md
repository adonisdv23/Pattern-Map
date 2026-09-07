# Pattern Map v16 site — post-revision verification

Status: bounded advisory verification of the exact committed tree; not owner
acceptance, participant testing, reader testing, screen-reader certification,
or evidence of comprehension/effectiveness.

Target commit: `2a54b24ec01707bb2a73032ab3f662cd995669ae`

Target subject: `Address final reader and accessibility findings`

Review date: 2026-08-19

## Scope and evidence boundary

This review re-checks every prior site finding from
`SITE_COMPREHENSION_ACCESSIBILITY_2026-08-19_6a29ed8.md` against the target
commit's source, committed standalone HTML, committed PDF, committed visual
renders, and the local generated route tree already present for QA. The prior
IDs are preserved: `SITE-MOB-001`, `SITE-A11Y-002`, `SITE-STANDALONE-003`,
`SITE-LINK-004`, `SITE-ECHO-005`, `SITE-COMP-006`, and `SITE-PDF-007`.

The target commit was verified as `HEAD` before this report was written. The
working tree also contains unrelated parent/orchestrator handoff changes; they
were not edited or treated as evidence. No canonical owner-intent file was
changed. The locked checkpoint passes:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

Evidence is separated below into:

- static/source/export evidence: deterministic checks of committed text and
  source, CSS calculations, HTML structure, fragment/reference audits, PDF
  metadata, and Poppler render reproducibility;
- recorded visual evidence: inspection of the committed PNG captures and PDF
  renders; and
- owner residuals: checks that require a physical keyboard, a supported
  screen reader, browser print preview, a fresh exact-target responsive render,
  external-source re-verification, or a real reader.

The in-app browser was unavailable when a fresh target-commit browser check was
attempted. Accordingly, this report makes no fresh browser-computed-style,
physical-focus, screen-reader, or browser-print claim. Existing committed QA
notes are quoted as repository records and are not upgraded into new evidence.

No external browsing, deployment, publication, provider/model call, spend,
study, participant activity, dataset acquisition, preregistration, or outreach
was performed.

## Disposition summary

“Resolved implementation” means that the correction is present in the target
source and is supported by local static/export checks. It does not mean that
an owner has accepted the finding or that a human-facing manual check has
occurred.

| Prior finding | Prior severity | Verification at `2a54b24` | Provisional disposition | Governing gate |
| --- | --- | --- | --- | --- |
| `SITE-MOB-001` | Medium / P2 | Source CSS keeps all three principal links visible at narrow widths and retains a separate five-route disclosure. The committed mobile screenshot is stale and still shows only `More+`; a fresh browser run was unavailable. | Implementation corrected; exact-target responsive evidence remains open. | A13, A06 |
| `SITE-A11Y-002` | Medium / P2 | Muted/family tokens and the dual focus ring now pass the target's static contrast thresholds. | Resolved implementation; keyboard/screen-reader/actual forced-colors review remains manual. | A13 |
| `SITE-STANDALONE-003` | Medium / P2 | Committed standalone export has one `h1`, 282 unique IDs, nine named route sections, and no heading/ID-reference defect found. | Resolved implementation. | A13, A06 |
| `SITE-LINK-004` | Medium / P2 | All 62 standalone same-document fragments target existing IDs; no `#source-*` fallback remains. | Resolved implementation. | A13, A06 |
| `SITE-ECHO-005` | Low / P3 | Routed and standalone Echo links now target stable Echo fragments and retain separate/unrun/no-results wording. | Resolved implementation; external source destinations remain unverified. | A10, A06 |
| `SITE-COMP-006` | Low / P3 | Reader-facing family copy is plain before technical details in the current route/export. The committed map screenshot still shows the pre-revision jargon copy. | Implementation corrected; exact-target visual evidence and cold-reader evidence remain open. | A06, A01, A04 |
| `SITE-PDF-007` | Low / P3 | PDF remains `Tagged: no`, but the artifact and handoff now explicitly call it an untagged visual companion and direct assistive-technology readers to standalone HTML. | Mitigated/documented; tagged-PDF decision remains owner residual if PDF accessibility is in scope. | A13 |

The implementation corrections are therefore present, but A13 is not a full
manual pass: the exact-target mobile/map captures need regeneration, physical
keyboard traversal and supported screen-reader review are not recorded, and
browser print preview remains open.

## Finding verification

### `SITE-MOB-001` — narrow navigation hid the principal doors

Prior condition: at the earlier revision, the `@media (max-width: 760px)`
rule hid `.primary-nav a`, leaving `More` as the only visible header control;
the disclosure script exposed only the five secondary routes. This was a
responsive navigation defect under A13 and a no-script concern under A06.

Target evidence:

- `site/src/site.css:143-159` defines the principal links as ordinary flex
  items and hides only `.secondary-nav-wrap` by default. There is no mobile
  rule hiding `.primary-nav a`.
- `site/src/site.css:453-471` changes the narrow header to one grid column,
  keeps `.primary-nav` visible and wrapping, leaves the principal links in
  place, and displays `More` as an additional control. The old
  `.primary-nav a { display: none; }` declaration is absent.
- `site/build.mjs:404-412` renders all three principal links before the
  `More` button and keeps the five secondary links in a separate labeled
  navigation container.
- `site/build.mjs:420-438` emits a `noscript` rule that displays the secondary
  navigation and hides `More` when script is unavailable. The three principal
  links remain ordinary links in the static HTML.
- `site/src/site.js:32-47` now centralizes open/close state, moves focus to
  `Examples` when the secondary disclosure opens, and returns focus to `More`
  on `Escape`.
- `npm run check` passes its `responsive/no-script navigation and active-route
  semantics` assertion. The generated route tree contains the three principal
  links on each inspected route and `aria-current="page"` on the active route.

Recorded-render discrepancy:

- The committed `qa/visual/screenshots/home-mobile-390x844.jpg` visibly shows
  `Pattern Map` and `More+` at the top, with no visible `Read the idea`,
  `Explore the map`, or `Apply it` links. It is the old rendered state, not
  evidence of the target source correction.
- The target commit did not modify `qa/visual/screenshots/*`; the image was
  carried from the earlier site build (`a3cd7c7`, 18:29) while the target
  source correction was committed later at 19:11. The current
  `qa/visual/VISUAL_QA_REPORT.md:11-18,22-29` and
  `qa/site/SITE_QA_REPORT.md:94-100` describe responsive coverage, but do not
  replace a fresh exact-target capture when the retained image visibly
  contradicts the revised CSS.

Disposition: **implementation corrected; exact-target responsive verification
open**. The prior defect is not present in the target CSS/build logic, but the
committed visual evidence package should not be marked fully closed for A13
until the mobile capture is regenerated from `2a54b24` and inspected. This is a
render-evidence residual, not a claim that a reader encountered the old state
in the target build.

Bounded correction/evidence action: regenerate the 390×844 (and, preferably,
the 1024×768 and 1440×1000) captures from the exact target build; confirm all
three principal links remain visible, `More` discloses only Examples,
Boundaries, Sources, Research, and History, no horizontal overflow occurs,
and the active route/focus state remains perceivable. Then update the visual QA
record. Physical keyboard traversal is a separate manual residual below.

### `SITE-A11Y-002` — muted/family text and focus colors were too weak

Prior condition: several muted/family colors and the yellow focus ring were
below robust normal-text/focus-indicator contrast thresholds against the paper
surface.

Target evidence:

- `site/src/site.css:1-21` replaces the earlier palette with darker
  `--muted`, `--teal`, `--green`, `--purple`, `--orange`, `--ochre`, and
  `--blue` tokens, and adds `--focus-dark` and `--focus-light`.
- `site/src/site.css:57-61` uses a dark 3px focus outline plus a light outer
  ring. `site/src/site.css:474-479` provides a forced-colors override using
  `Highlight` and removes the ordinary-mode shadow where forced colors are
  active.
- Independent relative-luminance calculations against `--paper: #f4f0e8`
  produce: muted **5.752:1**, teal **5.883:1**, green **5.427:1**, purple
  **6.275:1**, orange **5.243:1**, ochre **5.754:1**, and blue **6.039:1**.
  These exceed the target's 4.5:1 normal-text check in `site/check.mjs:158-162`.
- The dark focus ring `#0c5963` is **7.039:1** against paper. The light ring
  `#fff6dd` is **13.316:1** against the dark `--navy` surface. Both exceed the
  target's 3:1 focus-pair checks in `site/check.mjs:163-164`.
- `npm run check` passes `normal-text and dual-focus contrast thresholds`.
  The visible family cues are supplemented by borders, labels, and text, so
  the state is not communicated by color alone in the source structure.

Disposition: **resolved implementation** for the checked ordinary-mode token
and focus-pair calculations. The result is not a screen-reader certification,
physical keyboard result, or a claim that every composited browser background
has been manually sampled. Supported screen-reader, keyboard, and actual
forced-colors review remain owner residuals under A13.

Bounded correction/evidence action: retain the dark-token/dual-ring change;
have the owner inspect focused links, buttons, summaries, family controls, and
the `More` disclosure at desktop and narrow widths, including a real
forced-colors mode. Do not infer assistive-technology success from the static
ratio calculations.

### `SITE-STANDALONE-003` — standalone bundle had duplicate IDs and repeated `h1`s

Prior condition: the direct-open export concatenated nine route bodies without
route-specific ID or heading normalization. The prior export had ten `h1`
elements and duplicate IDs.

Target evidence:

- `site/build.mjs:52-57` uses route-prefixed fragments in standalone mode.
- `site/build.mjs:680-708` (`normalizeStandaloneMain`) prefixes each route's
  IDs, rewrites same-document `href` and ARIA/label references, and raises
  route-local heading levels by one so the outer export title is the only
  level-one heading.
- `site/build.mjs:733-747` wraps each extracted route body in a named
  `standalone-section` and emits a self-contained HTML document.
- The committed `site/exports/standalone/pattern-map-v16.html` independently
  audits to **1 `h1`**, **282 IDs / 282 unique IDs**, **nine** named route
  sections (`home`, `read`, `map`, `apply`, `examples`, `boundaries`,
  `sources`, `research`, `history`), and no heading-level jump in the static
  sequence. All `aria-labelledby`, `aria-describedby`, `aria-controls`, and
  `for` references inspected in the export resolve to an ID.
- The export contains **62** same-document fragments; every target exists.
  `site/check.mjs:121-131` and `qa/site/audit_site.py:170-183` repeat the
  one-h1, unique-ID, named-section, and hierarchy checks, and `npm run check`
  plus `python3 qa/site/audit_site.py` pass them.

Disposition: **resolved implementation**. The exact committed standalone
export no longer has the prior duplicate-ID or repeated-top-level-heading
defect. This static result does not certify a screen reader's navigation of the
file; the general supported-screen-reader residual remains open.

Bounded correction/evidence action: no further implementation correction is
indicated by this finding. Keep the standalone checks in the build gate and
have the owner include the direct-open export in the manual screen-reader and
keyboard pass.

### `SITE-LINK-004` — standalone source links had missing fragments

Prior condition: unmapped local Markdown links fell back to `#source-*` in the
standalone export, leaving 13 fragment targets with no matching IDs.

Target evidence:

- `site/build.mjs:63-101` now maps current local source paths to intentional
  routes and returns `null` for an unknown path.
- `site/build.mjs:117-125` throws on an unmapped local Markdown link instead of
  silently making a dead fallback. `sourceFragmentFor` supplies the stable
  `echo` fragment for Echo source paths.
- `site/check.mjs:51-66,146-153` checks local files and target fragments in
  routed pages and checks every standalone same-document fragment. It also
  rejects any remaining `href="#source-"` fallback.
- Independent inspection of the committed standalone export found **no**
  `href="#source-*"` links, **62** same-document links, and **no missing
  fragment targets**. The parenthesized DOI remains the exact external URL and
  passes the existing safe-anchor checks.

Disposition: **resolved implementation**. The prior 13-link standalone defect
is absent from the committed export and the current checks would fail on a
missing target.

Bounded correction/evidence action: keep the complete-fragment check in the
build gate. External destination validity is outside this local verification;
see `OWNER-RESIDUAL-012` below.

### `SITE-ECHO-005` — Echo source link landed at Research top

Prior condition: the Echo source path linked to the generic Research route,
while the rendered Echo callout had no stable fragment.

Target evidence:

- `site/build.mjs:104-125` recognizes Echo source paths and routes them to the
  `echo` fragment rather than a generic Research top.
- `site/build.mjs:640-647` renders the Echo section with `id="echo"`,
  `aria-labelledby="echo-heading"`, and the plain-language link label
  `The Echo Problem — separate project — unrun — no results`.
- The current routed `site/dist/research/index.html` contains both
  `id="echo"` and `href="../research/index.html#echo"`. The committed
  standalone export contains the corresponding normalized
  `id="research-echo"` and `href="#research-echo"`.
- The current route retains `UNRUN · NO RESULTS · NO PROVIDER OR MODEL
  SELECTED`; the Echo callout explicitly says it is separate and that V16 does
  not borrow results or let Echo define the map. Synthetic Echo removal still
  passes the principal-route meaning check in `qa/site/audit_site.py:159-162`.

Disposition: **resolved implementation**. The prior source-to-Echo navigation
defect is corrected in routed and standalone outputs. This does not reverify
the external source files or turn the no-results status into a research result.

Bounded correction/evidence action: retain the stable fragment and explicit
separation wording. Before any authorized publication, re-verify source
destinations and wording locally/externally under the owner's release process;
this review intentionally did not browse.

### `SITE-COMP-006` — specialist vocabulary appeared before the map translation

Prior condition: the visible first sentence of F1/F2 used `task-scoped
information aperture`, `claim-scoped authority`, and related mechanism terms
before a plain-language explanation. The prior report correctly described this
as a proxy risk, not a measured reader result.

Target evidence:

- `site/build.mjs:337-362` defines a plain-language public bridge for each
  family. The current F1/F2 bridges are, respectively, “Look beyond the
  obvious path, but treat what you find as something to inspect—not a shortcut
  to truth” and “Ask what each source can and cannot tell us about this exact
  claim; keep support, relevance, origin, and permission separate.” F3–F6
  receive equivalent plain bridges.
- `site/build.mjs:442-454` renders those public bridges before the technical
  `Specification` and `Technical mechanism` paragraphs inside the closed
  `Implementation detail` disclosure. The visible family questions and
  boundaries remain present.
- The current generated map route and committed standalone export show the
  plain bridges in the visible card text; the former `task-scoped information
  aperture`, `claim-scoped authority`, and `typed relationships` terms no
  longer lead the visible family purpose/how-it-works paragraphs. F1/F2
  specification and mechanism details retain the technical terms, and later
  route content may use them where the subject is technical. `site/check.mjs:95-108`
  asserts all six plain bridges and rejects empty glossary fields.
- `npm run check` and `python3 qa/site/audit_site.py` pass the map/no-script
  checks. The no-script route retains the family names, questions, boundaries,
  and relationship summary.

Recorded-render discrepancy:

- The committed `qa/visual/screenshots/map-desktop-1440x1000.jpg` visibly
  contains the prior F1/F2 lead copy (“Widen a task-scoped information
  aperture...” and “Keep source role, claim-scoped authority...”), not the
  target's plain bridges.
- The target commit did not modify the screenshot directory. Thus the current
  source/export correction is real, but the retained visual capture is stale
  and cannot be used as exact-target evidence that the corrected lead copy was
  rendered.

Disposition: **implementation corrected; exact-target visual evidence and
reader evidence remain open**. This review does not infer that a general reader
will understand the map, only that the target places the plain bridge before
technical disclosure in the inspected source/export.

Bounded correction/evidence action: regenerate the map desktop capture from
`2a54b24`, inspect the first F1/F2 cards at the intended responsive widths, and
update the visual QA record. A separately authorized cold-reader/mentor review
must determine whether the broad idea can be restated; do not treat this proxy
audit as that result.

### `SITE-PDF-007` — PDF companion was untagged

Prior condition: `pdfinfo` reported `Tagged: no`, and the ReportLab builder did
not create tagged document structure. The earlier finding recommended either a
tagged PDF or an explicit visual-only scope with the semantic HTML identified
as the accessible route.

Target evidence:

- `pdfinfo site/exports/pattern-map-v16-owner-review.pdf` still reports six
  letter-sized pages, no JavaScript/forms, and **`Tagged: no`**.
- The target PDF's first-page render now visibly includes: “Accessibility
  route: this PDF is an untagged visual review companion. Use the standalone
  HTML for semantic headings, landmarks, links, and assistive-technology
  navigation.” This text is generated at
  `site/scripts/generate_review_pdf.py:390-397`.
- The PDF's page-six render explicitly says that the untagged PDF was
  text-checked, rendered, and visually inspected, and that semantic and
  assistive-technology navigation belongs to standalone HTML. The generator
  records that scope at `site/scripts/generate_review_pdf.py:567-595`.
- `site/README.md:21-26` likewise calls the PDF an “untagged visual review
  companion, not the accessibility route” and directs readers to standalone
  HTML.
- All six committed render PNGs were inspected. Re-rendering the committed
  PDF with the bundled Poppler `pdftoppm` at 144 dpi produced byte-identical
  images to `qa/visual/pdf-renders/pattern-map-v16-owner-review-final-1.png`
  through `-6.png` (six of six hashes matched). The pages show no visible
  clipping, overlap, or unreadable glyph in this visual inspection.

Disposition: **mitigated/documented, not converted into a tagged PDF**. The
target implements the prior report's bounded scope correction, so the PDF is
not silently presented as an assistive-technology artifact. If the owner
intends the PDF itself to be an accessible reader-facing deliverable, the
underlying `Tagged: no` condition remains open and requires either tagged-PDF
generation plus structure verification or an explicit owner decision that the
semantic standalone HTML is the accessible route.

Bounded correction/evidence action: preserve the disclosure and visual QA
record. Do not claim PDF screen-reader support from the six visual renders.

## Static checks run on the target tree

The following read-only checks passed using the current target source and the
local generated route tree:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK

cd site && npm run check
PASS routes: 9
PASS exact first-screen framing, non-result boundary, and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS external Markdown links preserve URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragments
PASS standalone heading hierarchy and unique IDs
PASS responsive/no-script navigation and active-route semantics
PASS normal-text and dual-focus contrast thresholds
PASS standalone export exists

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names: all 9 routes
PASS no-script essential meaning is present in static HTML
PASS Apply vocabulary and route/stop/learning vocabulary
PASS reduced-motion, forced-colors, 200%-friendly reflow, and print hooks
PASS no-script simulation
PASS synthetic Echo-removal simulation
PASS historical diagram label/current-topology distinction and hash
PASS standalone HTML is self-contained with one h1, unique IDs, and named route sections
PASS external Markdown links preserve URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragment integrity
NOTE structural QA is not reader comprehension or effectiveness evidence
```

Additional independent read-only checks:

- `site/src/site.css` and the transient `site/dist/assets/site.css` have the
  same SHA-256; the same is true for `site/src/site.js` and its transient
  copied asset. This confirms that the local route checks used the target
  source assets; `site/dist/` is ignored build output, not a new committed
  artifact.
- The committed standalone export has one `h1`, 282 unique IDs, 62
  same-document fragments with zero missing targets, no unresolved
  `#source-*` fragment, nine named route sections, and no missing ARIA/label
  ID references in the inspected attributes.
- `git show --check` reports no whitespace error for the target's site source,
  checker, standalone export, or PDF builder changes.
- The six committed PDF renders were compared with a fresh Poppler render of
  the exact committed PDF; all six hashes matched.

## Manual owner residuals

These are deliberately not represented as resolved by this report.

### `OWNER-RESIDUAL-008` — physical keyboard traversal (A13)

Static source evidence supplies a skip link, a focusable `main#main`, named
links/buttons/summaries, `aria-expanded` state, `Escape` focus return, and a
static order. The committed QA record says synthetic Tab events did not advance
reliably (`qa/site/SITE_QA_REPORT.md:102-106`). A physical keyboard traversal
still needs to cover Home, Read, Explore, Apply, a secondary route, the More
open/close path, focus return, family controls, Show all, details/summary
controls, and local source links at desktop and narrow widths.

### `OWNER-RESIDUAL-009` — supported screen-reader review (A13)

The route audit checks landmarks, headings, names, `alt`, and static meaning;
it does not establish VoiceOver, NVDA, or another supported screen-reader
traversal. The owner should verify the first-screen reading order, three door
promises, map focus status and family controls, details/summary announcements,
mobile disclosure, historical image alt/caption, no-script behavior, and the
standalone export. No screen-reader certification is implied here.

### `OWNER-RESIDUAL-010` — browser print preview (A13, A06)

The static `@media print` rules are present at `site/src/site.css:487-497`,
the PDF renders are visually clear, and no-script checks pass. The committed
QA record states that browser print-media emulation was blocked
(`qa/site/SITE_QA_REPORT.md:98-100,114-119`). The owner should inspect print
previews for Home, Read, Explore, Apply, Examples, Sources, Research, and
History, including retained thesis/family/example/boundary/source text,
useful URLs, page breaks, expanded details, and unclipped tables/diagram.

### `OWNER-RESIDUAL-011` — cold-reader comprehension and technical density

The plain-language bridge is now present in the static map and standalone
export, but neither that fact nor the stale screenshot establishes that a real
thoughtful general reader can restate the idea. The 60–90-second and 10–15-
minute language remains an editorial estimate. A separately authorized
cold-reader/mentor review is needed for A01, A04, and the comprehension aspect
of A06. No reader result is claimed.

### `OWNER-RESIDUAL-012` — external source-link re-verification

The DOI/anchor syntax and local route integrity pass, but no external source
was opened in this lane. Before any authorized publication, reverify external
destinations, labels, and the inherited “not newly reverified” status. This
review intentionally did not browse.

### `OWNER-RESIDUAL-013` — exact-target visual capture freshness

`qa/visual/screenshots/home-mobile-390x844.jpg` and
`qa/visual/screenshots/map-desktop-1440x1000.jpg` visibly retain pre-revision
states even though the target source/export has the mobile and plain-copy
corrections. Regenerate and inspect those captures from
`2a54b24ec01707bb2a73032ab3f662cd995669ae` before treating A13 responsive and
map-composition evidence as complete. This residual is about evidence
freshness, not a claim that the corrected source fails.

### `OWNER-RESIDUAL-014` — PDF accessibility scope decision

The target now discloses that the PDF is untagged and directs assistive-
technology readers to standalone HTML, but `pdfinfo` still reports
`Tagged: no`. If the PDF is retained only as a visual owner-review companion,
the scope is explicit. If it is expected to serve as an accessible reading
artifact, the owner must authorize a tagged-PDF implementation and a structure
check. The visual renders do not settle that decision.

## Acceptance-gate snapshot

This is a proxy verification snapshot, not final owner acceptance.

| Gate | Verification at target commit | Remaining boundary |
| --- | --- | --- |
| A01 | Structural opening and plain map bridges are present; no prohibited first-screen result language found by `site/check.mjs`. | A 90-second real-reader description was not run; no comprehension result. |
| A02 | Static route/standalone/PDF evidence keeps the human problem and three doors before protocol, research, and Echo. | Fresh target mobile capture is needed because the retained mobile image is stale. |
| A03 | Static map/export checks confirm all six family names/questions in order. | No participant or reader inference. |
| A04 | Human-facing copy remains separate from implementation detail; the map bridge is less technical in target source. | Mentor/cold-reader adjudication remains open. |
| A05 | The recorded 60–90-second and 10–15-minute language is retained as editorial framing. | Timing is an estimate, not an observed reading result. |
| A06 | No-script/static route checks, closed-details copy, standalone fragments, and PDF scope labeling pass. | Browser print preview and exact-target visual refresh remain open. |
| A10 | Echo is late, separate, explicitly unrun/no-results, and directly anchored in routed and standalone outputs. | External source destinations were not reverified. |
| A13 | Static semantics, contrast, route integrity, standalone structure, reduced motion, forced colors, no-script, and PDF visual rendering pass. | Fresh mobile/map captures, physical keyboard, supported screen reader, browser print preview, and PDF scope decision remain. |
| A16 | Locked owner-intent checksum passes; target commit does not change `docs/OWNER_INTENT_V16.md`. | This report is advisory and does not authorize a thesis change. |
| A17 | No locked owner-intent edit is present in the target commit or this report. | Owner disposition is still required for residuals/corrections. |

## Final verification statement

At exact commit `2a54b24ec01707bb2a73032ab3f662cd995669ae`, the source and
committed standalone export resolve all of the prior implementation defects in
mobile-link CSS/semantics, ordinary-mode contrast tokens/focus treatment,
standalone heading/ID structure, standalone fragment integrity, Echo anchoring,
and map lead-copy ordering. The PDF's underlying untagged state remains, but it
is now explicitly scoped as a visual review companion with standalone HTML
identified as the semantic route.

The remaining open items are evidence freshness and owner/manual work, not
inferred reader outcomes: the committed mobile/map screenshots are stale
relative to the target source; physical keyboard traversal, supported
screen-reader review, and browser print preview are not complete; external
source destinations were not browsed; PDF tagging remains an owner scope
decision; and no reader comprehension or screen-reader certification is
claimed.
