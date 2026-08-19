# Pattern Map v16 visual QA report

Status: local owner-review candidate

Visual QA covers composition, responsive behavior, focus-state rendering, no horizontal overflow, historical/current labeling, and the PDF companion. It is not reader-comprehension, persuasion, behavioral-effectiveness, model-quality, empirical, participant, or research evidence.

## Browser captures

Screenshots are retained under `qa/visual/screenshots/`:

- `home-desktop-1440x1000.png` - desktop first screen after hero tightening; the three principal doors are visible in the initial composition.
- `home-tablet-1024x768.png` - tablet first screen; no horizontal overflow and doors remain present.
- `home-mobile-390x844.png` - mobile reflow; doors stack and the header uses the compact More control.
- `map-desktop-1440x1000.png` - current relationship view and F1/F2 opening composition.
- `apply-tablet-1024x768.png` - four implementation choices and the Apply route opening composition.
- `history-desktop-1440x1000.png` - historical route with the exact v13/current-topology label.
- `history-full.png` - full-page historical-route capture from the earlier 1024px inspection pass.
- `home-print-media.png` is not present: the supported local CDP print-media permission was declined by the browser security policy, so no blocked artifact is being represented as evidence.

## Viewport results

| Viewport | Route | Result |
| --- | --- | --- |
| 1440 x 1000 | Home | Exact headline and standfirst; all three doors visible; no overflow. The measured door group ended at approximately y=934 within the 1000px viewport. |
| 1024 x 768 | Home | Doors visible; `scrollWidth=1024`; no horizontal clipping. |
| 390 x 844 | Home | `scrollWidth=390`; hero text width approximately 370px; doors stacked; no horizontal clipping. |
| 1440 x 1000 | Explore | F1-F6 cards visible in document order; six focus controls present; focus changes emphasis without hiding other cards. |
| 1024 x 768 | Apply | Four implementation cards, 12 operator steps, Quickstart open, and seven template links present; `scrollWidth=1024`. |
| 1440 x 1000 | History | Historical/current distinction visible before the preserved diagram; image has a descriptive alt and the exact historical label. |

## Interaction and focus-state inspection

On Explore, the initial status reads: `All six families are visible. Focus controls add emphasis; they never hide essential meaning.` Activating the F1 focus control changes it to: `F1 is focused. The other families remain visible for comparison.` The button exposes `aria-pressed="true"` in that state.

On the global menu, activating `More +` sets `aria-expanded="true"`, opens the secondary links, and moves focus to `Examples`. The static focus order is skip link, wordmark, principal routes, More, secondary routes, and principal door cards. The in-app automation surface did not advance focus reliably on synthetic Tab events; this remains an explicit residual in `qa/site/SITE_QA_REPORT.md`.

## PDF companion inspection

Final PDF: `site/exports/pattern-map-v16-owner-review.pdf`.

- `pdfinfo`: six letter-sized pages, unencrypted, no JavaScript, no form fields.
- Reopened with `pypdf`: 9,147 extracted characters; exact opening headline, F1/F6, Signal Foundry illustration label, Echo no-results label, historical/current label, and explicit QA limitation all present.
- Rendered with bundled Poppler at 144 dpi to `qa/visual/pdf-renders/pattern-map-v16-owner-review-final-1.png` through `-6.png`.
- All six final pages were visually inspected. The first page establishes the opening copy and three doors; pages 2-4 cover the reading path, six-family table, and bounded examples; page 5 carries the proportionate application table and clean 01-12 operator path; page 6 carries historical lineage, QA status, local handoff, and the no-deployment boundary.
- A first render exposed literal operator-step markup. That was corrected, regenerated, re-rendered, and checked for both `<font` and `&nbsp;` residuals; both residual checks are false in the final extracted text.

## Visual system and bitmap policy

The site uses semantic HTML, CSS, typography, borders, cards, and code-native relationship treatments. `qa/visual/VISUAL_NEEDS.md` finds no justified generated bitmap need, so no image-generation call or generated candidate was made. The only committed image is the preserved historical v13 asset copied from the immutable archive with its recorded SHA-256.

## Residuals

1. Browser print-media emulation was blocked by the browser security policy; static print rules are present and the owner should do one manual print-preview pass.
2. Physical keyboard Tab traversal remains a manual-owner check because the in-app automation surface did not advance synthetic Tab focus reliably.
3. Visual QA demonstrates implementation rendering and does not establish reader comprehension, effectiveness, persuasion, model quality, or research outcomes.
