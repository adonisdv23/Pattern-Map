# V15 visual, responsive, print, and accessibility QA

- **Artifact under review:** local v15 owner-review package
- **Canonical reading surface:** `site/` semantic HTML
- **Visual/print companion:** `exports/THOUGHT_PIECE_V15.pdf`
- **Review date:** 2026-08-18
- **Verdict:** **PASS for local owner review, with the explicit limitations below**

This report is a release-surface QA record. It is not a WCAG conformance
claim, an assistive-technology user study, a publication approval, or evidence
that the proposed framework is empirically effective.

## 1. Material changes covered by this pass

The reader-design review identified three P1 and four P2 defects. The repaired
reader now:

- exposes an evidence-status badge in every one of the eleven collapsed
  component summaries;
- replaces the low-contrast blue-only focus ring with a two-tone white/ink
  treatment that remains visible on light and dark surfaces;
- removes the `720px` print minimum from the Lab condition table and applies a
  fixed, wrapping A4 table layout to both the Lab and state comparisons;
- removes localhost-derived Open Graph and Twitter metadata from the local-only
  review build;
- restores the editorial serif reading face while retaining mono and sans
  interface roles;
- turns the worked example into a post-receipt decision application instead of
  repeating the nine-report accounting explanation;
- loads both local evidence illustrations eagerly so print and first traversal
  do not depend on lazy-image timing; and
- compresses the desktop opening enough to place all three route choices inside
  a 1000-pixel-high first fold.

The PDF prior-art table also received a visual-QA correction. A row describing
the 2024 human evidence-dependence study had been mislabeled as Schelpe. The
final PDF names `Strittmatter et al. · 2024` for that study and places Schelpe
with the byte-exact-deduplication comparators.

## 2. Semantic and static reader checks

Commands:

```text
cd site
npm run lint
npm test
git diff --check
```

Result:

- ESLint: pass.
- Production Vinext build: pass.
- Rendered-HTML regression suite: **5/5 pass**.
- Whitespace/error-marker check: pass.

The rendered-HTML suite verifies, among other conditions:

- one document-level `h1`;
- complete, unique same-page fragment targets;
- eleven expandable component records and eleven visible summary-status spans;
- a keyboard-returning close control for every long component record;
- no results section or empirical-result language;
- the F0/F1/F2 lock, descriptive T1 boundary, and `No F3 exists` statement;
- the nine-row typed origin-accounting receipt and its preserved `UNKNOWN`
  boundary;
- no localhost Open Graph or Twitter metadata;
- no lazy-loaded local illustrations;
- serif body typography;
- the two-tone focus rule; and
- print-specific fixed/wrapping rules for the two wide comparison tables.

## 3. Browser layout checks

The built production reader was served locally and inspected through the
documented in-app browser path. Temporary viewport overrides were reset after
the checks.

### Desktop — 1440 × 1000

- `documentElement.clientWidth = 1440`
- `documentElement.scrollWidth = 1440`
- Page-level horizontal overflow: none.
- Reading body: `Georgia, "Times New Roman", serif`.
- Route-choice block: top `817.80px`, bottom `952.30px`.
- All three route cards end at `952.30px`, inside the 1000-pixel viewport.
- Component summary statuses: 11 present and rendered.
- Historical v13 image: complete, intrinsic size `1024 × 1536`.
- Worked-example image: complete, intrinsic size `1536 × 1024`.

### Narrow reader — 390 × 844

- `documentElement.clientWidth = 390`
- `documentElement.scrollWidth = 390`
- Page-level horizontal overflow: none.
- Component summary statuses: 11 present and rendered.
- Both local images: complete with nonzero intrinsic dimensions.
- Receipt table region: `322px` client width, `740px` scroll width,
  `overflow-x: auto`, `tabindex="0"`.
- State table region: `360px` client width, `680px` scroll width,
  `overflow-x: auto`, `tabindex="0"`.
- Lab table region: `360px` client width, `720px` scroll width,
  `overflow-x: auto`, `tabindex="0"`.

### Tablet — 768 × 1024

- `documentElement.clientWidth = 768`
- `documentElement.scrollWidth = 768`
- Page-level horizontal overflow: none.
- Sticky navigation is internally scrollable: `624px` client width, `918px`
  scroll width, `overflow-x: auto`.
- Component summary statuses: 11 present and rendered.
- Both local images: complete with nonzero intrinsic dimensions.
- All three wide-table regions remain contained; the receipt region uses a
  `700px` client box for its `740px` internal table and stays keyboard-focusable.

### Minimum supported check — 320 × 800

- `documentElement.clientWidth = 320`
- `documentElement.scrollWidth = 320`
- Page-level horizontal overflow: none.
- Component summary statuses: 11 present and rendered.
- Both document-link regions: `290px` client and scroll width; no spill.
- Receipt table region: `252px` client width, contained `740px` internal scroll
  width, `overflow-x: auto`, `tabindex="0"`.
- State and Lab regions remain contained and keyboard-focusable at `290px`
  client width.
- Both local images remain complete with nonzero intrinsic dimensions.

### 200% reflow proxy — 1280 × 720 physical viewport / 640 × 360 CSS viewport

The in-app browser did not apply its zoom keyboard shortcuts, so the reflow
check used the standard equivalent-CSS-viewport proxy: half the reference
viewport dimensions. This verifies responsive reflow and overflow behavior,
but it is not represented as an observed browser-zoom UI state.

- `documentElement.clientWidth = 640`
- `documentElement.scrollWidth = 640`
- `.page-shell` client and scroll widths are both `640px`.
- Page-level horizontal overflow: none.
- Navigation remains an internal horizontal scroll region: `496px` client
  width, `918px` scroll width.
- Both document-link regions remain contained at `610px`.
- All eleven evidence-status labels remain rendered.
- Receipt, state, and Lab tables remain labelled, keyboard-focusable internal
  scroll regions rather than causing page-level overflow.

The narrow layouts intentionally keep wide data tables as labelled internal
scroll regions instead of shrinking their screen typography below a readable
size. The A4 print layout uses a separate fixed/wrapping rule.

### Screenshot limitation

The normal in-app-browser screenshot operation was attempted for the desktop
and 320-pixel first folds. Both attempts timed out while running
`Page.captureScreenshot`. DOM, intrinsic-image, computed-style, geometry, and
overflow inspection remained available and produced the measurements above.
No raw CDP call or separate browser-automation fallback was used. Therefore the
owner packet records the verified first-fold geometry and the screenshot-tool
limitation rather than claiming that responsive screenshots were captured.

## 4. Focus visibility and contrast

The former focus color, `#35628c` against `#1f1d19`, measured only `2.626:1`.
The repaired rule uses a white inner outline and an ink outer ring:

```css
outline: 3px solid #fff;
outline-offset: 3px;
box-shadow: 0 0 0 7px var(--ink);
```

Calculated sRGB contrast ratios:

| Pair | Ratio |
|---|---:|
| White `#ffffff` / ink `#1f1d19` | `16.826:1` |
| Ink `#1f1d19` / paper `#f3efe5` | `14.654:1` |
| Ink `#1f1d19` / light paper `#fbf9f3` | `15.982:1` |

The inner outline remains visible on the dark panels; the outer ring remains
visible on the paper surfaces. This is a focused repair check, not a complete
color-contrast audit of every foreground/background pair.

## 5. PDF generation and structural checks

Final command:

```text
/Users/gpt/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  tools/render_v15_reader_pdf.py
```

Final PDF properties:

| Property | Result |
|---|---|
| SHA-256 | `0542cdd14311fd07f7d9fa5e02c05584e83ed31d4d2cb07f305c5e3751254dca` |
| Pages | 20 |
| Page size | A4, `595.276 × 841.89 pt` on every page |
| PDF version | 1.4 |
| Encryption | none |
| Forms | none |
| JavaScript | none |
| Open action | none |
| Embedded reading faces | Georgia, Georgia Bold, Georgia Italic, Arial, Arial Bold |
| Outline entries | 19 |
| Tagged PDF | **No** |

ReportLab retains an unused Base-14 Helvetica resource in the page resources;
all selected reading faces above are embedded. The PDF is deliberately and
visibly labeled as an **untagged visual/print companion**. The semantic HTML and
Markdown remain canonical for accessible reading.

Text extraction confirmed exactly one copy of this footer on every page:

```text
UNTAGGED VISUAL/PRINT COMPANION · HTML IS CANONICAL · NO EMPIRICAL RESULTS
```

It also confirmed that the corrected prior-art table contains both
`Strittmatter et al. · 2024` and `Schelpe`, and no longer contains the erroneous
`Schelpe et al. · 2024` string.

## 6. Page-by-page raster inspection

The final PDF—not the earlier pre-correction render—was rasterized with Poppler
at 120 dpi:

```text
pdftoppm -png -r 120 exports/THOUGHT_PIECE_V15.pdf <temporary-prefix>
```

All 20 pages were inspected in five four-page contact sheets. Dense or
high-consequence pages were additionally inspected at full rendered size,
including the receipt, distinction table, component cards, corrected prior-art
table, F0/F1/F2 condition table, corpus/endpoints, analysis gates, T1/negative
result page, limitations, and owner-decision page.

Page-by-page result:

| Pages | Content | Result |
|---|---|---|
| 1–2 | Cover and two-track reading contract | Pass |
| 3–4 | Counting error and typed receipt | Pass |
| 5–6 | Distinction contract and historical v13 anchor | Pass |
| 7–10 | Six families, two loops, and C01–C11 cards | Pass |
| 11 | Worked decision application and labelled illustration | Pass |
| 12–13 | Corrected verified-prior-art table and closest comparators | Pass |
| 14 | Adversarial reading and retirement conditions | Pass |
| 15–17 | F0/F1/F2 lock, fixed denominators, and stop gates | Pass |
| 18 | Descriptive T1 and locked unfavorable interpretations | Pass |
| 19 | Sixteen limitations and absent-results boundary | Pass |
| 20 | Owner questions, canonical surfaces, and final status | Pass |

No clipped text, overlaps, broken tables, black squares, missing illustrations,
unreadable glyphs, incorrect page sizes, missing page numbers, or footer
omissions were observed in the final raster set.

## 7. Residual limitations

1. The PDF is untagged and is not the canonical accessible reading surface.
2. The reader has not undergone a formal WCAG 2.2 conformance audit, automated
   axe scan, screen-reader matrix, or disabled-user study.
3. Browser screenshots could not be captured because the supported screenshot
   operation timed out; responsive DOM and geometry checks passed.
4. The browser did not expose a working zoom shortcut; 200% reflow was checked
   with the equivalent half-size CSS viewport proxy, not a claimed live zoom
   observation.
5. Print CSS was checked statically and the separate A4 PDF was rendered and
   inspected. The browser’s own print-preview UI was not available through the
   supported local-browser controls.
6. These checks establish release-surface coherence and rendering quality only.
   They do not establish model behavior, framework effectiveness, transfer, or
   any empirical result.

## 8. Gate decision

**PASS.** The semantic HTML remains the canonical two-track reader; the final
20-page PDF is a polished, explicitly untagged visual/print companion; the
reader repairs close the identified P1/P2 presentation defects; and the
remaining limitations are disclosed rather than converted into unsupported
accessibility or empirical claims.
