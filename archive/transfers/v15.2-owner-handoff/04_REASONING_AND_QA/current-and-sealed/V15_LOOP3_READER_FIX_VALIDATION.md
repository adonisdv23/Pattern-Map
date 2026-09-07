# V15 Loop 3 Reader-Fix Validation

**Validation target:** repaired v15 local reader at commit `976d2c0` (`fix:
close v15 reader accessibility gaps`)

**Validation worktree:**
`/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-loop3-fix-review`

**Validation branch:** `codex/discrimination-layer-v15-loop3-fix-review`

**Prepared:** 2026-08-18

**Prior review:** `reports/V15_LOOP3_READER_DESIGN_ACCESSIBILITY_REVIEW.md`,
which reviewed the frozen reader at `6423a43` and identified no P0 findings,
three P1 findings, and four P2 findings.

**Scope constraint:** this validation does not edit the repaired site, source,
tests, manuscript, or canonical artifacts. The only intended worktree change is
this report.

## Verdict

**PASS — the named P1 and P2 repairs are closed by source, rendered-HTML,
CSS/contrast, and automated-test evidence.**

This is a static/DOM repair-closure verdict. The requested live viewport and
screenshot matrix at 1440×1000, 390×844, and 320×800 is **UNVERIFIED**, because
the documented in-app browser runtime had no available browser surface. That is
recorded as a tooling limitation, not treated as a content failure. No claim is
made here that the page was visually inspected at those viewports, that an A4
print raster was opened, or that a keyboard traversal was observed live.

## Evidence discipline

The labels below keep different kinds of evidence separate:

- **Automated/static:** rendered HTML from the local server, source and CSS
  inspection, deterministic arithmetic, HTTP responses, and test/lint output.
- **Visual judgment:** a property requiring a person to see a rendered page at a
  viewport, zoom, print preview, or assistive setting. Those properties remain
  **UNVERIFIED** when the browser was unavailable.
- **Tooling limitation:** a requested operation that could not be executed. It
  is not evidence that the implementation passes or fails that operation.

The acceptance contract remains the blueprint at
`reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md:200-205` and
`:273-285`: collapsed Explore summaries expose evidence status; the body uses a
legible serif; focus remains visible against every panel; tables do not clip in
print; mobile/reflow/image-blocked/reduced-motion behavior remains bounded; and
the reader keeps its no-results/T1 boundaries.

## Finding-by-finding closure

| Prior finding | Required repair | Evidence in `976d2c0` | Closure |
| --- | --- | --- | --- |
| P1-EXPLORE-01 | Put a visible evidence-status label in each collapsed Explore summary and test all 11. | `site/app/page.tsx:331-339` renders `Evidence status · …` inside every component summary. The rendered response has 11 `.component-summary-status` spans. `site/tests/rendered-html.test.mjs:63-68` asserts all 11 and expected labels. | **PASS (static/DOM)** |
| P1-ACC-01 | Replace the single blue ring with a checked treatment that remains visible on light and dark/accent surfaces. | `site/app/globals.css:26-30` uses a white inner outline plus an ink outer ring. Deterministic contrast arithmetic gives at least one ring ≥3:1 on paper, ink, teal, violet, coral, ochre, and blue. The regression test is at `site/tests/rendered-html.test.mjs:120-123`. | **PASS (static contrast); live focus visibility UNVERIFIED** |
| P1-PRINT-01 | Reset Lab and state-table overflow/minimum width for A4 print and wrap cells. | `site/app/globals.css:572-597` sets A4 margins, makes `.condition-table-wrap`/`.state-table` overflow visible, resets table `min-width`, sets `width:100%`/`table-layout:fixed`, and permits wrapping. The repaired test checks the print selectors at `site/tests/rendered-html.test.mjs:122-123`. | **PASS (static CSS geometry); A4 raster/pagination UNVERIFIED** |
| P2-META-01 | Remove or correct the hard-coded `localhost:3000` social-preview metadata. | `site/app/layout.tsx:4-9` retains local title/description/robots but contains no `openGraph` or `twitter` block. The rendered response contains zero `og:`/`twitter:` metadata. Source/rendered assertions are at `site/tests/rendered-html.test.mjs:60-61` and `:125-126`. | **PASS (static/DOM)** |
| P2-TYPE-01 | Align long-form body typography with the blueprint's serif editorial direction. | `site/app/globals.css:23` sets the body to `17px/1.58 var(--serif)`; compact interface/meta rules continue to use `var(--mono)`/small labels. The source regression is at `site/tests/rendered-html.test.mjs:120`. | **PASS (static source); line-length/reflow visual judgment UNVERIFIED** |
| P2-EDITORIAL-01 | Make the worked example earn its scroll after the preview and full receipt instead of repeating the full origin accounting. | `site/app/page.tsx:438-463` now titles the section “What changes after the receipt?”, states that the corrected record is an input rather than a verdict, shows before/after decision implications, and gives three bounded actions. The old “Nine positive articles. One launch announcement” worked-example title is absent from the rendered response. Preview (`:73-76`) and receipt (`:110-184`) remain distinct modes. | **PASS (static source/DOM); overall visual pacing UNVERIFIED** |
| P2-PRINT-02 | Make substantive images print-safe/eager and retain adjacent text equivalents. | The v13 map image at `site/app/page.tsx:217-225` and worked-example image at `:441-449` have no `loading="lazy"` attribute. The rendered response contains exactly two images and zero lazy attributes; the test asserts the source at `site/tests/rendered-html.test.mjs:124`. | **PASS (static source/DOM and asset HTTP); actual print image load UNVERIFIED** |

No P0 finding was present in the prior review, and no new P0 issue was found by
this validation.

## Specific repair checks

### Visible evidence status in collapsed summaries

The repaired summary structure is visible in source at
`site/app/page.tsx:331-340`: component ID, name, one-sentence summary, and the
text label `Evidence status · {componentMaturity[component.id].label}` all sit
inside the native `<summary>`. The label is not color-only; its CSS token at
`site/app/globals.css:283` has text, border, and the existing status class.

Static rendered counts from `/tmp/v15_fix_home.html`:

| Check | Result |
| --- | ---: |
| `<h1>` | 1 |
| component `<details>` | 11 |
| collapsed summary status spans | 11 |
| total `<details>` | 13 |
| images | 2 |
| lazy image attributes | 0 |

The current rendered test also checks the expected “Prior art + synthesis” and
“Design + empirical hypothesis” labels. This validates presence in server HTML;
it does not claim a live assistive-technology announcement or a visual
inspection of each closed disclosure.

### Two-tone focus contrast on light and dark contexts

The global focus rule at `site/app/globals.css:26-30` is:

```css
outline: 3px solid #fff;
outline-offset: 3px;
box-shadow: 0 0 0 7px var(--ink);
```

Using the declared palette (`site/app/globals.css:4-15`), the calculated
foreground/background ratios are:

| Adjacent surface | White inner ring | Ink outer ring | At least one ring ≥3:1 |
| --- | ---: | ---: | --- |
| Paper `#f3efe5` | 1.15:1 | 14.65:1 | Yes |
| Ink `#1f1d19` | 16.83:1 | 1.00:1 | Yes |
| Teal `#1b6265` | 7.04:1 | 2.39:1 | Yes |
| Violet `#5c467d` | 7.99:1 | 2.11:1 | Yes |
| Coral `#9c4233` | 6.48:1 | 2.60:1 | Yes |
| Ochre `#76500f` | 7.18:1 | 2.34:1 | Yes |
| Blue `#35628c` | 6.41:1 | 2.63:1 | Yes |

The conclusion is specifically about the two-ring treatment as a whole. The
white ring is intentionally weak on paper, and the ink ring is intentionally
weak on dark/accent surfaces; the complementary ring supplies the contrast.
This is deterministic palette arithmetic, not a claim that a browser screenshot
was inspected. The repaired source regression only checks that both layers are
present (`site/tests/rendered-html.test.mjs:120-121`).

### A4 print-safe Lab and state tables

The declared page is A4 with 14mm side margins
(`site/app/globals.css:572-574`). Its printable width is:

`210mm − 14mm − 14mm = 182mm = 687.9 CSS px at 96 px/in`.

The repaired print rules at `site/app/globals.css:595-597` apply to both
`.condition-table-wrap` and `.state-table`: overflow is visible, `min-width` is
zero, width is 100%, layout is fixed, font size is 7pt, and cell contents may
wrap anywhere. This removes the prior 720px minimum-width conflict. The source
test checks the overflow and `min-width:0`/fixed-layout selectors. A print
preview, PDF, cell-by-cell pagination check, and replacement-glyph check were
not possible without the browser surface and are therefore unverified.

### No localhost OG/Twitter metadata

The repaired layout metadata at `site/app/layout.tsx:4-9` contains title,
description, application name, and noindex/ nofollow robots only. It has no
`metadataBase`, `openGraph`, or `twitter` block. The rendered response from the
local server had zero `property="og:` and zero `name="twitter:` tags. This
removes the previous hard-coded `http://localhost:3000/og.png` output rather
than replacing it with another unverified host.

### Serif editorial body alignment

`site/app/globals.css:23` now uses the declared Georgia/Times serif stack for
the body. Interface and metadata continue to use the compact mono rules, for
example `:94-98` and `:130`, so this repair does not relabel all interface text
as prose. The source test at `site/tests/rendered-html.test.mjs:120` passes.
Actual line length, rasterized font fallback, and 200% zoom readability remain
visual questions, not static facts.

### Reduced repetition in the worked example

The revised block at `site/app/page.tsx:435-463` no longer restates the full
nine-observation accounting sequence. It keeps the preview and typed receipt as
the explanatory modes, then uses the worked example for the difference after
correction:

1. The receipt is an input to a decision, not a verdict (`:440`).
2. The visual is explicitly illustrative and points to the post-correction
   application (`:441-449`).
3. The before/after contrast identifies what stays on hold and what becomes
   actionable (`:451-454`).
4. Three bounded actions and the `ORIGIN-EX-01` implication are explicit
   (`:455-463`).

The rendered response contains the new heading and all three action labels, and
does not contain the prior worked-example opening. This is source/DOM evidence;
the subjective amount of repetition over the full scroll remains unverified
without a live visual read.

### Eager local images

The two substantive images are local paths and have dimensions, `decoding="async"`
where applicable, alt text, and nearby captions. The repaired source contains no
`loading="lazy"` attribute (`site/app/page.tsx:217-225` and `:441-449`;
`site/tests/rendered-html.test.mjs:124`). During the local-server check,
`/images/nine-mentions-one-origin.jpg` returned HTTP 200 as `image/jpeg` and
`/images/v13-six-families-origin-map.png` returned HTTP 200 as `image/png`.
That establishes local asset availability, not a print-engine load guarantee.

### Desktop first-fold compression

The repair diff reduces the desktop masthead and route preamble spacing:

| Rule | Prior frozen value | Repaired value | Source |
| --- | --- | --- | --- |
| Masthead padding | `72px 0 76px` | `48px 0 60px` | `site/app/globals.css:91` |
| Metadata bottom margin | `28px` | `20px` | `site/app/globals.css:92` |
| H1 bottom margin / max size | `28px` / `7.15rem` | `20px` / `6.55rem` | `site/app/globals.css:100` |
| Hero opening top margin / max size | `42px` / `2.05rem` | `28px` / `1.8rem` | `site/app/globals.css:104` |
| Thesis margin/padding | `46px 0 32px` / `24px` | `32px 0 22px` / `18px` | `site/app/globals.css:110` |
| Route top margin / card minimum/padding | `34px` / `150px` / `22px` | `24px` / `132px` / `18px` | `site/app/globals.css:115-118` |

The route order and first-fold labels remain explicit in
`site/app/page.tsx:65-94`: owner-review/no-results status, title, thesis,
opening boundary, and distinct Essay/Explore/Lab cards. Responsive rules remain
present at `site/app/globals.css:497-520`, including a single-column route grid
on narrow screens. This is source-level compression evidence. No browser DOM
geometry or screenshot was available, so actual fold position at 1440×1000 is
unverified.

## Browser viewport QA

The documented in-app browser path was attempted against the local reader at
`http://127.0.0.1:8773/` after starting the assigned dev server. The browser
control runtime reported **“No browser is available”** for the URL, and the
required discovery call `agent.browsers.list()` returned `[]`. Per the browser
skill's fallback boundary, no raw CDP, Playwright, Selenium, or separate browser
automation path was used.

| Requested condition | Result | What is and is not established |
| --- | --- | --- |
| 1440×1000 desktop | **UNVERIFIED — tooling unavailable** | Source confirms compressed masthead and route order; no live fold, focus, contrast, or layout observation. |
| 390×844 mobile | **UNVERIFIED — tooling unavailable** | Responsive CSS and one-column route rule are present; no live reflow or page-overflow observation. |
| 320×800 narrow mobile | **UNVERIFIED — tooling unavailable** | Responsive CSS and labeled table scrollers are present; no live 320px overflow/focus observation. |
| Keyboard/focus traversal | **UNVERIFIED live; static partial** | Existing source/test coverage includes skip link, unique targets, native details, and close-focus return; no full tab sweep. |
| 200% zoom/reflow | **UNVERIFIED — tooling unavailable** | No browser geometry or clipped-rail observation. |
| `prefers-reduced-motion: reduce` | **PASS static; live unverified** | `site/app/globals.css:567-569` disables smooth scrolling and reduces transitions/animations; no essential animation is present in source. |
| Images blocked | **PASS static; live unverified** | Both images have alt/caption text; the receipt explicitly says no image is required for its interpretation at `site/app/page.tsx:183`. |
| A4 print/PDF | **PASS static CSS; raster/pagination unverified** | Controls/overflow rules and table reset are present; no print preview or PDF was captured. |

The lack of screenshots is therefore a documented environment limitation. It is
not silently converted into a visual PASS or a content FAIL because server
rendering, source checks, and DOM metrics were available.

## Static and local checks run

All commands below ran in the validation worktree. The repair source remained
unchanged.

| Check | Result |
| --- | --- |
| `npm ci` from `site/` | **PASS**; lockfile install completed. npm reported 20 audit findings (1 low, 4 moderate, 15 high); dependency files were not changed. |
| `npm run lint` from `site/` | **PASS**; no ESLint errors. |
| `npm test` from `site/` | **PASS**; build completed and all 5 rendered HTML tests passed. |
| `git diff --check` | **PASS**; no whitespace errors. |
| `git diff HEAD^ HEAD --check` | **PASS**; repaired commit has no whitespace errors. |
| Repository Markdown/link checker discovery | **NOT AVAILABLE**; `rg --files | rg '(markdown|link|check|lint)'` found no repository Markdown/link checker to run. |
| Static semantic/DOM check against server response | **PASS**; one H1, 11 component disclosures, 11 summary status labels, unique IDs, and all 39 same-page fragments resolved. |
| Static image/metadata check | **PASS**; 2 images, 0 lazy attributes, 0 OG metadata, 0 Twitter metadata. |
| Static print selector and A4-width check | **PASS**; both Lab/state selectors reset overflow/min-width; 687.9 CSS px calculated content width. |
| Palette contrast arithmetic | **PASS for two-ring strategy**; every listed paper/ink/accent surface has at least one ring ≥3:1. |
| Local server `GET /` | **PASS**; HTTP 200, `text/html`, 861,188 bytes in the validation run. |
| Local `/app/globals.css` | **PASS**; HTTP 200, `text/javascript`. |
| Local `/images/nine-mentions-one-origin.jpg` | **PASS**; HTTP 200, `image/jpeg`. |
| Local `/images/v13-six-families-origin-map.png` | **PASS**; HTTP 200, `image/png`. |
| Local `/og.png` | **PASS** as an asset request; HTTP 200, `image/png`. Its existence does not imply social metadata is emitted; rendered OG/Twitter tags were zero. |
| Browser bootstrap/discovery | **LIMITATION**; URL lookup said no browser available and `agent.browsers.list()` returned `[]`; no screenshot or fallback automation was used. |

## Receipt, no-results, and T1 boundary recheck

The repair validation did not broaden any scientific or safety denominator. The
reader still states:

- `site/app/page.tsx:65-76`: local owner review, “No study run · no empirical
  results · not published,” and conceptual synthesis rather than a result;
- `site/app/page.tsx:110-184`: fictional `ORIGIN-EX-01`, no live data, typed
  relation ledger, `UNKNOWN` preserved, zero supporting origins counted, and a
  human HOLD rather than an automatic verdict;
- `site/app/page.tsx:524-540`: Lab is a protocol/offline harness with no model,
  no study run, no results, and F0/F1/F2 as the only current experimental
  conditions;
- `site/app/page.tsx:580-585`: T1 is descriptive transfer only, “No F3 exists,”
  and remains outside `A`, `M`, confidence intervals, McNemar rows, VOR, and
  effect estimates.

The existing rendered tests continue to assert these boundaries at
`site/tests/rendered-html.test.mjs:19-79`. This validation does not add data,
change an endpoint, or imply any result.

## Residual limitations and handoff

The repair closure is complete for the named P1/P2 issues under static/DOM
evidence. A future browser-enabled pass is still needed for visual confirmation
of first-fold position, typography and line length, focus placement at each
viewport, 200% zoom, no page-level horizontal scroll, image-blocked rendering,
reduced-motion runtime behavior, and A4 pagination/raster loading. Those are
follow-up verification items, not unresolved source findings in this report.

Only `reports/V15_LOOP3_READER_FIX_VALIDATION.md` is intended to be committed
from this validation worktree; no site/source implementation was edited.
