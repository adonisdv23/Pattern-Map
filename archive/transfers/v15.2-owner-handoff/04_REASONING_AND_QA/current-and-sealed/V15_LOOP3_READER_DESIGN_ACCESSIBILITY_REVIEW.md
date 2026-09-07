# V15 Loop 3 Reader, Design, and Accessibility Review

**Review target:** frozen v15 local reader at commit `6423a43`

**Review worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-loop3`

**Prepared:** 2026-08-18

**Scope:** `site/app/**`, `site/tests/**`, `source/THOUGHT_PIECE_V15.md`,
`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md`, and the visible
no-results/T1/receipt boundaries.

## Executive verdict

**FAIL — the reader is not ready for a closed loop-3 sign-off.**

The server-rendered reader builds, passes its four existing tests, passes ESLint,
serves the page and local image/CSS assets, preserves the no-results/T1/receipt
truth conditions, and has a strong static semantic baseline. No P0 finding was
identified.

Three P1 defects remain in the frozen implementation:

1. Explore record summaries omit their evidence status. The status appears only
   after expansion even though the blueprint requires it before expansion.
2. The one global keyboard focus ring uses `--blue` against every surface. On
   the dark quick-example panel, the ring is only 2.63:1 against the panel
   background, below the 3:1 focus-indicator target and the blueprint's
   requirement that focus remain visible against every panel.
3. The Lab F0/F1/F2 table has a 720px minimum width that is not reset by print
   CSS. With the declared A4 page and 14mm side margins, the printable content
   width is approximately 688px; the table can therefore overflow or clip in
   print, contrary to the print contract.

The required live visual matrix could not be executed because the browser
control runtime reported no available browser surface (`agent.browsers.list()`
returned `[]`). This is recorded as a review-gate failure, not silently treated
as a visual pass. Desktop, tablet, mobile, 200% zoom, keyboard traversal,
blocked-image, reduced-motion, and print rendering still require an actual
browser run after the three P1 fixes.

## Evidence discipline and conditions

The report distinguishes:

- **Automated/static evidence:** command output, rendered HTML, source lines,
  CSS rules, deterministic contrast arithmetic, and existing tests.
- **Visual judgment:** a judgment that requires seeing the rendered page under a
  viewport or assistive condition. These are marked **UNVERIFIED** where the
  browser was unavailable.
- **Review limitation:** an inability to execute the requested condition, not a
  claim that the site passes it.

The intended acceptance contract is in
`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:273-285`. It requires
keyboard/source-order access, one semantic heading structure, no mobile page
scroll, a focusable labeled table scroller, 200% reflow, image-blocked
equivalence, reduced motion, contrast, and print-safe tables/controls.

### Conditions attempted

| Condition | Requested check | Evidence and result |
| --- | --- | --- |
| Build/server | Build and run the local reader | `npm test` built successfully; `npm run dev -- --hostname 127.0.0.1 --port 8773` started the assigned reader at `http://127.0.0.1:8774/` because 8773 was already occupied. `GET /` returned 200. **PASS**. |
| Server-rendered semantics | H1, headings, IDs, same-page targets, disclosures, receipt, Lab status | Four existing tests passed. Static render had one `<h1>`, 10 `<h2>`, 38 `<h3>`, 6 `<h4>`, 13 `<details>`, and 3 focusable `role="region"` scrollers. **PASS (static).** |
| Desktop | Visual pacing, first fold, typography, contrast, focus, Essay/Explore/Lab separation | No browser surface was available. **UNVERIFIED.** |
| Tablet | 768px-ish layout, sticky navigation, table treatment, loop diagram, no clipped rail | No browser surface was available. **UNVERIFIED.** |
| Mobile | 390×844 and 320–390 CSS px, concise first fold, no page-level horizontal scroll, nav reachability | No browser surface was available. CSS has responsive branches and labeled scrollers, but rendered overflow and focus auto-scroll were not observed. **UNVERIFIED.** |
| 200% zoom/reflow | 1280×720 viewport at 200%, readable content, wrapped navigation, no fixed-rail clipping | No browser surface was available. Source media rules are plausible but not a visual proof. **UNVERIFIED.** |
| Keyboard/focus | Skip link, source-order traversal, details, close-and-return focus, focus visibility | Existing source test proves the close handler returns focus to `summary`; same-page tests prove targets. The full tab sweep and dark-panel focus visibility were not executable. **PARTIAL; P1-ACC-01 remains.** |
| Reduced motion | Immediate scrolling and no essential transition/animation under `prefers-reduced-motion` | `site/app/globals.css:564-567` disables smooth scrolling and reduces transition/animation duration. No essential animation is present in source. **PASS (static); live confirmation unavailable.** |
| Images blocked | Alt text and nearby text preserve the worked example, v13 map, counts, and status | The rendered page has two `<img>` elements and two `alt` attributes. Both figures have captions; the v13 figure has an expandable text transcription. **PASS (static); blocked-image rendering unavailable.** |
| Print | Controls disappear, details expand, tables fit, backgrounds are not required | Print CSS hides navigation/controls and expands closed details. The Lab table width defect is **P1-PRINT-01**; pagination and actual raster loading are **UNVERIFIED**. |
| Contrast | Body text and controls meet the stated contrast contract | Static arithmetic passes common text pairs, but the global focus ring fails on the dark quick-example panel. **FAIL; P1-ACC-01.** |
| Narrative pacing | Avoid repeated cards/slogans; preserve first-fold clarity; keep Essay/Explore/Lab distinct | Source review shows clear route separation but repeats the same nine-report/origin explanation across preview, receipt, and worked example. **P2-EDITORIAL-01.** Visual pacing is otherwise **UNVERIFIED**. |
| Receipt truth | Fictional, no verdict, zero counted supporting origins, unknown preserved | Source/rendered text and existing tests preserve `ORIGIN-EX-01`, fictional/no-live-data status, `INSUFFICIENT`, 09/01/00/02 counts, `UNKNOWN stays unknown`, and human `HOLD`. **PASS (static).** |
| No-results/T1 boundaries | No result surface, no F3, T1 outside A/M and statistical conclusions | Source/rendered text and existing tests preserve “No model selected · no study run · no results,” “No F3 exists,” and T1 exclusion from `A`, `M`, intervals, tests, VOR, and effect estimates. **PASS (static).** |

## P0 findings

**None identified.** The main document server-renders, has one H1, exposes the
core argument without client hydration, and does not show a fabricated result
surface.

## P1 findings

### P1-EXPLORE-01 — Evidence status is hidden inside each record instead of exposed in its summary

**Evidence type:** source inspection against the canonical information
architecture; no visual claim was made.

The blueprint requires each of the eleven native `<details>` summaries to
expose the component ID, name, one-sentence purpose, **and evidence status**
before expansion (`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:200-205`).
The frozen implementation's summary at `site/app/page.tsx:333-336` exposes only
the ID, name, summary sentence, and an aria-hidden “Inspect” affordance. The
evidence label is rendered only inside the expanded body at
`site/app/page.tsx:346-348`, via `componentMaturity[component.id]`.

**Impact:** a reader scanning Explore cannot distinguish “Prior art +
synthesis,” “Prior art + design hypothesis,” or “Unresolved” without opening
all eleven records. That delays the epistemic-status boundary precisely where
the blueprint asks for a quick, inspectable map, and it makes collapsed records
look more equally established than they are.

**Required fix:** add a visible, text-labelled status token to every summary
(not color alone), derived from `componentMaturity`, while retaining the full
evidence-boundary explanation inside the body. Add a rendered test that checks
all 11 summaries contain the expected status label and that the status remains
present when details are closed.

### P1-ACC-01 — Focus indicator is insufficiently contrasting on a focusable dark panel

**Evidence type:** static calculation plus source inspection; no visual claim
was made.

**Exact locations and text:**

- `site/app/globals.css:26-30` applies one rule to every focusable link,
  button, summary, and `tabindex="0"` element:
  `outline: 3px solid var(--blue)`, where `--blue` is `#35628c` at
  `site/app/globals.css:15`.
- `site/app/page.tsx:103-108` places the focusable link **“Inspect the typed
  receipt ↓”** inside `.quick-example`.
- `site/app/globals.css:152-156` gives `.quick-example` the dark `--ink`
  background (`#1f1d19`).

**Automated evidence:** relative luminance arithmetic gives the blue outline
against the ink panel a contrast ratio of **2.63:1**, below the 3:1 target for
a visible non-text focus indicator. The same blue ring is also low against
the accent backgrounds used by `.example-contrast` and `.result-commitment`
(`site/app/globals.css:347-350` and `434-438`) should those panels gain a
focusable child later. The blueprint explicitly requires the focus indicator to
remain visible against every panel (`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:283`).

**Impact:** a keyboard user can reach the receipt link but may not reliably see
where focus is while it is on the dark quick-example panel. This is a direct
failure of the stated accessibility contract, even though the link itself and
the skip link are present.

**Required fix:** use a two-tone focus treatment whose outer/inner ring each
has a checked contrast strategy across paper, ink, teal, coral, violet, ochre,
and blue surfaces—for example a light inner ring plus a dark outer ring, with
the exact colors verified against every focusable panel. Add a focused-state
regression check for the dark quick-example link and at least one light-panel
control at desktop and mobile widths.

### P1-PRINT-01 — Lab condition table can exceed the declared A4 printable width

**Evidence type:** static CSS geometry; actual print rendering unavailable.

**Exact locations:**

- `site/app/page.tsx:541-552` renders the focusable Lab comparison region with
  the F0/F1/F2 table.
- `site/app/globals.css:414-418` sets `.condition-table-wrap` to horizontal
  overflow and `.condition-table-wrap table { min-width: 720px; }`.
- `site/app/globals.css:569-591` declares A4 print with 14mm left/right
  margins but resets only `.route-receipt table` at line 589; it does not
  reset `.condition-table-wrap table`.

**Automated evidence:** A4 content width with the declared 14mm side margins
is `210mm - 28mm = 182mm`, approximately `688px` at 96 CSS px/in. The Lab
table minimum is `720px`, approximately `190.5mm`, leaving it about `8.5mm`
wider than the printable content box. The print contract requires that tables
do not clip (`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:284`).

**Impact:** the most important Lab comparison—the exact F0/F1/F2 condition
lock—can produce horizontal overflow or clipped columns in an A4 print/PDF
render. The screen scroller is intentionally useful on narrow screens, but
print must expose the whole table without requiring an interactive scrollbar.

**Required fix:** in `@media print`, set `.condition-table-wrap { overflow:
visible; }` and `.condition-table-wrap table { min-width: 0; width: 100%;
table-layout: fixed; }`, then render an A4 print receipt and inspect every cell
for wrapping/clipping. Re-check the generic `.state-table` table as well even
though its 680px minimum is closer to the available width.

## P2 findings

### P2-META-01 — Local social-preview metadata resolves to the wrong host

**Evidence type:** rendered HTML plus source/test evidence.

`site/app/layout.tsx:9-20` supplies a relative Open Graph image path
`/og.png`. The local server rendered it as
`<meta property="og:image" content="http://localhost:3000/og.png">`; the
same hard-coded expectation is codified in
`site/tests/rendered-html.test.mjs:60`. The reader was actually served at
`http://127.0.0.1:8774/` in this review. Because the document is marked
`noindex, nofollow` (`site/app/layout.tsx:8`) and is explicitly local-only, this
is not a publication blocker, but it makes copied owner-review metadata point
to an unrelated/unavailable port.

**Required fix:** either set an explicit local `metadataBase` matching the
owner-review server, make the test assert a relative URL, or keep social
metadata disabled for the local-only build. Confirm that no absolute localhost
URL can survive a future share/deployment configuration.

### P2-TYPE-01 — Body typography does not follow the editorial blueprint

**Evidence type:** source comparison; visual judgment unavailable.

The blueprint calls for a “highly legible serif” body and compact sans-serif
interface/meta type (`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:253-256`).
The site sets the entire body to `font: 17px/1.58 var(--sans)` at
`site/app/globals.css:23`; only headings, selected leads, pull quotes, and
some cards switch to `var(--serif)`. This may be a deliberate readable choice,
but it is a clear implementation/design-system deviation for a long-form
reader.

**Required fix:** decide and document whether v15 intentionally changes the
body type system. If not, set long-form prose to the approved serif and retain
sans for navigation/meta/table labels; then visually re-check line length,
small-screen wrapping, and 200% zoom.

### P2-EDITORIAL-01 — The opening boundary is repeated across three reading modes

**Evidence type:** exact source text; pacing judgment is partly visual and is
therefore not fully verified.

The same explanation appears in all of these locations:

- `site/app/page.tsx:103-108`: “Preserve nine observations. Do not silently
  turn them into nine origins” plus “A known common origin does not make a
  report false.”
- `site/app/page.tsx:110-184`: the full `ORIGIN-EX-01` receipt repeats the
  nine-observation/one-origin accounting, unknown rule, and disposition.
- `site/app/page.tsx:430-461`: the worked example again opens with “Nine
  positive articles. One launch announcement,” repeats the same-origin rule in
  steps 2–3, and restates the packet conclusion.

This is not a truth-boundary error—the repetition is accurate—but it creates a
long scroll before the reader reaches objections and Lab, contrary to the
blueprint's preference for paragraphs over repeated cards/slogans
(`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:113-114`) and its
instruction to state limitations once before the concise audit list
(`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:122-123`).

**Required fix:** keep the quick preview and the full receipt as distinct
reading modes, but shorten the later worked example to application/difference:
link back to the receipt rather than re-explaining every count and relation.
Preserve one new decision implication in the worked example so it earns its
place.

### P2-PRINT-02 — Lazy-loaded substantive images need a print receipt

**Evidence type:** source inspection; print rendering unavailable.

The historical map image is `loading="lazy"` at
`site/app/page.tsx:218-224`, and the worked-example image is also lazy at
`site/app/page.tsx:437-444`. Print CSS preserves these figures
(`site/app/globals.css:586-597`) but does not guarantee that a browser will
load a lazy image that has not entered the viewport before print. Both images
have useful alt text and adjacent text, so this is not an image-blocked
semantic failure; it is a print completeness risk.

**Required fix:** run an actual A4 print test from the top and from a deep Lab
anchor. If either raster is absent or replaced by a blank box, make the print
path eager/print-safe or explicitly document that the adjacent text equivalent
is the canonical print content.

## What passes statically

### Reader and route separation

The top-level frame communicates the three intended modes in source order:

- `site/app/page.tsx:78-94` provides text links to Essay, Explore, and Lab.
- `site/app/ReadingNav.tsx:6-20` provides same-page navigation for Start,
  Essay, Receipt, Explore map/records/loops, Illustration, Objections, Cases,
  Lab, and Sources.
- `site/app/page.tsx:97`, `277`, `312`, `364`, `430`, `466`, `497`, `523`,
  and `614` define the major section anchors (the source has unique IDs and
  the existing test verifies every same-page target).
- The Lab starts with a high-contrast status threshold at
  `site/app/page.tsx:526-530` and repeats “No model selected · no study run ·
  no results.”

This matches the blueprint's Essay/Explore/Lab architecture
(`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:163-175`).

### Semantic and keyboard baseline

- `site/app/page.tsx:53-54` supplies a skip link to `#essay`.
- `site/app/layout.tsx:37` sets `lang="en"`.
- There is exactly one H1 in the rendered response. The heading sequence is
  H1 → H2 → H3/H4 without a static level skip.
- The receipt table uses a caption; all three tables use column/row scopes. The
  three horizontal data regions are labeled and focusable
  (`site/app/page.tsx:146-157`, `404-416`, and `541-552`). The state and Lab
  tables rely on their labeled regions and prose scroll hints rather than a
  native `<caption>`; add captions if screen-reader traversal shows context
  loss.
- `site/app/CollapseControl.tsx:6-14` closes the native `<details>` and sends
  focus back to its summary. The existing test verifies both behaviors.
- All 11 responsibility records are native `<details>` elements; their
  summaries expose the component ID, name, and one-sentence summary before
  expansion (`site/app/page.tsx:319-355`).

### Images and blocked-image equivalence

The static render contains exactly two images and exactly two alt attributes:

- `site/app/page.tsx:218-224` identifies the v13 map as historical and names
  its six-family/step content. The adjacent caption and expandable transcript
  preserve the historical/non-current-topology boundary.
- `site/app/page.tsx:437-445` labels the nine-mentions image as illustrative,
  not factual; its alt text says the common origin does not make the reports
  false, and its caption supplies the counts/status boundary.

The receipt itself states at `site/app/page.tsx:183` that no image is required
to interpret its counts, relation types, or disposition.

### Reduced motion and contrast arithmetic

`site/app/globals.css:564-567` switches smooth scrolling off and suppresses
transition/animation duration under `prefers-reduced-motion: reduce`. No
essential animation or auto-motion is present in the source.

The following foreground/background pairs exceed 4.5:1 in the static palette:

| Pair | Ratio |
| --- | ---: |
| ink on paper | 14.65:1 |
| muted on paper | 5.69:1 |
| teal on paper | 6.13:1 |
| sage on paper | 5.16:1 |
| violet on paper | 6.96:1 |
| coral on paper | 5.64:1 |
| ochre on paper | 6.25:1 |
| blue on paper | 5.58:1 |
| white on ink | 16.83:1 |
| white on teal | 7.04:1 |
| white on violet | 7.99:1 |

These pass values do not clear the focus-ring finding, because focus is a
non-text visual indicator with its own visibility requirement against its
adjacent surface.

## Receipt and epistemic-status audit

### Receipt truth conditions

The site preserves the manuscript's fictional receipt rather than presenting
it as a result:

- `site/app/page.tsx:110-115` labels `ORIGIN-EX-01` “fictional bundle,” “no
  live data,” and “no verdict.”
- `site/app/page.tsx:125-139` records the broad-validation claim as
  `INSUFFICIENT`, with 09 observations, 01 common-origin cluster, 00 counted
  supporting origins, and 02 contrast roots whose support is unassessed.
- `site/app/page.tsx:142-166` preserves all nine observations and keeps
  `UNKNOWN` separate from dependent/independent totals.
- `site/app/page.tsx:176-183` records a human HOLD disposition and explicitly
  denies automatic admission, rejection, or a truth verdict.

The existing rendered test checks these exact phrases and values at
`site/tests/rendered-html.test.mjs:41-52`.

### No-results and T1 boundaries

The Lab preserves the current scientific boundary:

- `site/app/page.tsx:526-533` says “Protocol + offline harness,” “No model
  selected · no study run · no results,” and calls the surface an
  implementation receipt rather than a finding.
- `site/app/page.tsx:541-549` exposes F0/F1/F2 and says the only primary
  contrast is F2 minus F1.
- `site/app/page.tsx:579-584` labels T1 “descriptive transfer only,” says
  “No F3 exists,” keeps T1 outside `A`, `M`, confidence intervals, McNemar
  rows, VOR, and effect estimates, and requires rights/annotation gates.
- `source/THOUGHT_PIECE_V15.md:501-518` makes the same T1 boundary in the
  canonical manuscript.

No `id="results"` surface, mock chart, effect-size placeholder, or result
number was found; the existing test asserts the absence of a results anchor.

## Required fix and re-review checklist

Before calling loop 3 PASS:

1. Expose the evidence status in every collapsed Explore summary and add a
   rendered regression assertion for all 11 records.
2. Fix the focus indicator with a checked dual-ring or equivalent treatment;
   verify the quick-example link and every other focusable surface at desktop,
   tablet, mobile, and 200% zoom.
3. Reset the Lab condition table's print minimum width and overflow; render an
   A4 receipt and inspect the F0/F1/F2 table plus the state table for clipping.
4. Re-run the browser matrix at 1440×900, 1024×768, 768×1024, 390×844, and
   320×800 (or equivalent desktop/tablet/mobile conditions), including a full
   keyboard traversal from skip link through all disclosures and return links.
5. Re-run at 200% zoom in a 1280×720 window and confirm no page-level
   horizontal scroll, clipped fixed rail, hidden focused link, or inaccessible
   table content.
6. Run with `prefers-reduced-motion: reduce`; block images; and print from the
   top and from a deep Lab anchor. Record screenshots or equivalent receipts.
7. Decide whether the body sans-serif is intentional. If not, restore the
   blueprint's serif long-form body and re-check line length and reflow.
8. Shorten the worked-example repetition or explicitly document why its second
   telling earns the additional scroll cost.
9. Resolve the `localhost:3000` social-preview metadata before any owner-review
   artifact is shared outside the local server.

## Checks run

From `site/` in the assigned worktree:

- `npm ci` — completed successfully from the lockfile; npm reported 20
  dependency audit findings (1 low, 4 moderate, 15 high). No dependency files
  were intentionally changed by this review.
- `npm test` — passed: build completed and all 4 rendered HTML tests passed.
- `npm run lint` — passed with no output/errors.
- `GET http://127.0.0.1:8774/` — HTTP 200, `text/html`.
- Local asset requests for `/app/globals.css`,
  `/images/nine-mentions-one-origin.jpg`,
  `/images/v13-six-families-origin-map.png`, and `/og.png` — HTTP 200.
- Static heading/image/details/region counts and same-page target checks —
  consistent with the existing tests.
- Palette contrast arithmetic — recorded above; focus contrast exposed
  P1-ACC-01.
- Browser-control bootstrap and discovery — setup succeeded but
  `agent.browsers.list()` returned `[]`; no browser automation or visual
  screenshot was performed.

No site source, test, manuscript, or canonical artifact was edited in this
review; the only intended change is this report.
