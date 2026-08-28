# Visual reader QA report

Recorded: 2026-08-18

Status: `READY_FOR_LOCAL_OWNER_REVIEW_WITH_DISCLOSED_MANUAL_RELEASE_CHECKS`

Tested surface: `http://127.0.0.1:8773/`

Canonical accessible surface: semantic HTML reader

Visual/print companion: `exports/THOUGHT_PIECE_V14.pdf`

## Build and structural validation

| Check | Result |
| --- | --- |
| `npm run lint` | Pass; zero reported lint errors. |
| `npm test` | Pass; production build plus four Node tests. |
| Server-rendered complete reading experience | Pass. |
| Same-page navigation and unique identifiers | Pass; ten numbered destinations including `04 Connections`. |
| Receipt semantics | Pass; claim heading, 09/01/00/02 counts, exactly nine O01–O09 rows, relation key, `UNKNOWN`, and human disposition are server rendered. |
| Historical anchor | Pass; v13 image and seven-step live-text transcription are present and labeled historical. |
| Image roles | Pass; E2 and v13 are present, H1 is absent from the rendered HTML and public site tree, and the 1200×630 social-card metadata is rendered. |
| Disposable starter UI | Absent. |
| Canonical framework JSON | Parses successfully. |
| Local HTTP | `200` at `127.0.0.1:8773`. |
| Public hosting | None; the reader remains local-only. |

The SSR test confirms one `h1`, a skip link, six named map families, eleven
native component `details` records, the map text equivalent, semantic two-loop
relationship content, the worked example, twelve limitations, bounded cases,
research, sources, complete same-page link targets, and unique IDs. The page
remains meaningful before client hydration.

## Fresh responsive inspection

The in-app browser loaded a temporary local-only QA harness containing
same-origin iframes with exact CSS viewports. The harness was removed after the
captures; it is not part of the site.

| Viewport | Inner/client width | Document scroll width | Page overflow | Key observed behavior |
| --- | ---: | ---: | --- | --- |
| 1440 × 900 | 1440 | 1440 | None | Two-column route cards, full rail, large title, and text-led opening remain contained. |
| 720 × 900 | 720 | 720 | None | Route cards stack, the receipt mobile summary is enabled, and type remains readable without page-level sideways scrolling. |
| 390 × 844 | 390 | 390 | None | Title, proposition, route cards, receipt frame/counts, and all section content reflow to one column. |

At 390px, the receipt’s table region has a 322px client width and a 740px
scroll width, exactly as intended: the region—not the document—scrolls
horizontally. Before that table, the live summary says:

> O01–O09 · Origin A · DEPENDENT · zero supporting origins counted under the
> stated relation rule

The four count blocks remain visible without a sideways gesture: 09
observations, 01 known common-origin cluster, 00 supporting origins under the
stated relation rule, and 02 separate comparison roots. Fresh screenshots are
stored under `reports/qa/site-final-20260818/`:

- `responsive-desktop-1440x900-emulated.png`
- `responsive-tablet-720x900-emulated.png`
- `responsive-mobile-390x844-emulated.png`
- `responsive-mobile-receipt-390x844-emulated.png`
- `responsive-mobile-ledger-390x844-emulated.png`

The source screenshots include the dark QA-harness surround and a scale label;
the page inside each frame uses the exact stated CSS viewport. The earlier
twelve PNGs under `reviews/claude_desktop/packet/` are preserved as historical,
pre-receipt review inputs and are not represented as current captures.

## Accessibility and input behavior

- Semantic landmarks, one top-level heading, ordered heading levels, lists,
  tables, links, a skip link, and native `details`/`summary` controls are used.
- The family map has a prose equivalent. The two-loop figure exposes its labels
  and explanation semantically. Decorative connectors are hidden from assistive
  technology.
- The origin receipt is complete live text. No image is required to understand
  its counts, relation types, uncertainty rule, or disposition.
- The E2 and v13 images have non-empty alt text, captions, intrinsic dimensions,
  and adjacent live-text boundaries. The v13 seven-step strip is transcribed.
- Color is never the only information channel: family names, numbers, IDs,
  relation labels, state words, and return text remain explicit.
- The 3px focus styling is retained. A current component disclosure was opened,
  its bottom close control was used, and focus returned to the parent `summary`.
- The receipt table region was clicked/focused and confirmed as a `DIV` with
  `tabindex="0"`; its visible scroll hint explains the narrow-screen behavior.
- `prefers-reduced-motion: reduce` disables smooth scrolling and reduces
  transition/animation duration.

### Keyboard and assistive-technology limitation

The connected in-app-browser wrapper did not yield a trustworthy complete
synthetic Tab traversal from the browser chrome into the first page control.
That limitation does not erase the successful focus-return exercise, the native
control semantics, the focusable receipt region, or the rendered-HTML tests,
but it prevents claiming a complete automated keyboard audit. A manual
Tab/Shift+Tab/Enter/Space pass and a real screen-reader pass remain mandatory
before any public release.

## Zoom, image independence, and print

- The exact 720px layout is the effective CSS-width pressure of 200% zoom on a
  1440px canvas and has no page overflow. The 390px test is narrower still.
  Direct browser zoom emulation was unavailable, so an actual 200% manual zoom
  spot-check remains a release gate.
- Server-rendered text contains the complete proposition, receipt, map text,
  component records, worked example, limitations, cases, research, and sources.
  Image load state is therefore not the only route to any substantive claim.
- Print CSS removes interactive-only navigation, opens component content,
  preserves receipt groupings where possible, uses `object-fit: contain`, and
  avoids treating the historical v13 image as the current map. Direct
  in-app-browser print-media emulation was unavailable; browser print preview
  remains a manual release check.

## Social-card inspection

The final social card was generated once through the current OpenAI image-
generation route, inspected at full size, and converted to 1200×630. The title
and subtitle are accurate; nine paper fragments relate to a shared source while
two comparison roots remain separate. It contains no additional labels, model
branding, fake status, workflow arrows, funnel, gate, or truth-verdict UI. Its
role is share-preview art only.

- File: `site/public/og.png`
- SHA-256: `26d87ad92d12edabebb829daabf7ca60681ac720ff15705c86bb677a99bf3b24`
- Exact generator model: not exposed; no legacy DALL-E version inferred.

## PDF inspection

Canonical file: `exports/THOUGHT_PIECE_V14.pdf`

SHA-256: `c96b5f062fec5dd9a09b7a592dc88c915839a872bb172f1a621bdbb53d0612f7`

| Property | Result |
| --- | --- |
| Pages | 29 |
| Page size | A4, consistent |
| File size | 3,252,782 bytes |
| Encryption | None |
| Embedded JavaScript | None |
| Empty/textless pages | None; all 29 extract text |
| Required current content | Receipt, O01–O09, v13 transcript/image, nine-article example, E2, limitations, frozen-model research design, sources, glossary, and closing question present |
| Stale “Five positive” wording | Absent |
| Outline entries | 13 |
| Replacement characters | None |
| Embedded body font | Yes (`ArialMT` subset); standard PDF base fonts remain for display roles |
| Visible clipping or overlap | None found across full render |
| Tagging | Not tagged |

The PDF was rasterized into 29 PNG pages under
`reports/qa/current-pdf-final-20260818/`. All four contact sheets were inspected,
then pages 2, 3, 4, 20, 25, 28, and 29 were inspected at full size. Those pages
cover the receipt, relation key/disposition, v13 historical map and transcript,
E2 example, first-paper direction, glossary, and closing statement. No clipping,
overlap, inaccessible crop, or stale count was found. The PDF is explicitly a
visual/print companion; because it is untagged, the semantic HTML is the
canonical accessible reading surface.

## Release boundary

This QA supports local owner review. It does not authorize publication or
establish empirical validity, a user-study result, formal accessibility
conformance, a tagged-PDF claim, owner approval, or a production-ready system.
Before publication, perform the remaining manual keyboard, screen-reader,
actual 200% zoom, and browser print-preview checks on the exact approved commit.
