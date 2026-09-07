# Loop 3 — skeptical reader/editor/design review of the integrated site

**Status:** expert simulation for local owner handoff · 2026-08-18
**Scope:** current rendered local HTML, source, CSS, tests, asset boundaries, and available prior captures
**Target artifact:** `research/overnight/rounds/12_LOOP3_READER_DESIGN_REVIEW.md`

## Executive verdict

The integrated source now has the right conceptual spine:

1. the working proposition appears before the first exact example;
2. the route receipt carries the nine-observation/one-origin distinction in live semantic HTML;
3. the H1 image is no longer the masthead explanation and is visibly labelled an optional material metaphor;
4. the E2 worked image is adjacent to exact live text, a consistent nine-count, and a non-evidence caption;
5. the v13 PNG is labelled as a historical reference, linked at full resolution, and accompanied by a text summary;
6. the first-paper panel now matches the narrow stipulated-origin-relation cue-use boundary.

The receipt **passes an image-independent expert inspection**: the server-rendered HTML exposes `09` observations, `01` known common-origin cluster, `00` independently supporting origins established for the claim, `02` separate comparison roots, `UNKNOWN`, the typed relation key, and a human hold without requiring a raster. This is a source/DOM finding, not a human comprehension result.

The remaining handoff risk is verification, not a missing concept. The current 390, 720, and 1440 screenshots in the repository show the pre-receipt page; the current A4 PDF likewise does not contain the new receipt. The existing visual QA report therefore cannot be used as proof that the integrated receipt, demoted H1, new page length, or print pagination works. No connected in-app browser was available for this pass, so I could not take current viewport screenshots or perform a full interactive Tab traversal. Fresh captures and a short manual reader/focus pass are a P0 gate before any handoff beyond local source review.

### Final visual-selection disposition

| Element | Disposition for current local review | Handoff condition |
| --- | --- | --- |
| Semantic route receipt | **Retain; canonical explanatory surface** | Keep deterministic HTML/text. Make the disposition wording less independence-like and capture/print-test the large block. |
| E2 worked-example image | **Retain** | Keep only with its adjacent exact caption/alt/text and a fresh 390/720/A4 crop check. It is the strongest current editorial image. |
| v13 historical anchor | **Retain, bounded archival role** | Keep the pre-image historical label, full-resolution link, and text alternative; do not let its portrait/strip become the current map. |
| H1 context-before-answer | **Conditional retention, demoted further in release logic** | It may remain as an optional small editorial transition during owner review. If the handoff occurs before a current image/no-image reader pass, omit H1 by default. Remove it if any reader or current capture shows pipeline/gatekeeper interpretation. Do not substitute H2/H3. |

## Audit boundary and evidence status

The labels below prevent an expert simulation from being mistaken for a user study:

- **[S] Direct inspection:** current source, current server-rendered HTML, current CSS, tests, local assets, or an existing report/capture.
- **[I] Inference:** a reasoned conclusion from those observations.
- **[H] Hypothesis:** a claim that a reader/capture test could falsify.
- **[DJ] Design judgment:** a recommended edit or disposition.

### What was actually checked

**[S]** The local owner-review server at `http://127.0.0.1:8773/` returned HTTP 200 and server-rendered the current receipt, demoted H1, E2, v13 anchor, and updated research panel. A read-only HTML audit found:

- one page-level `h1`;
- ten `h2`, thirty-two `h3`, and five receipt `h4` headings;
- nine receipt table records (`O01`–`O09`);
- three non-empty-`alt` image elements;
- twelve `details` elements (eleven component records plus the v13 text summary);
- two intentionally focusable horizontal-scroll regions (receipt ledger and existing state table);
- no duplicate IDs;
- no missing `aria-labelledby` or `aria-describedby` targets in the served HTML;
- no empty image alt attributes;
- no current-page occurrences of the stale “five positive articles” wording.

**[S]** `npm test` passed: production build plus all four server-rendered HTML tests. `npm run lint` passed with no reported errors. These tests establish build/HTML invariants only; they do not establish viewport geometry, print pagination, screen-reader announcement quality, or reader comprehension.

**[S]** The existing `reports/VISUAL_READER_QA_REPORT.md` records prior 390 × 844, 720 × 900, and 1440 × 900 checks, but the available packet images prove that those captures predate the current receipt and content correction. For example, `reviews/claude_desktop/packet/site-desktop-1440x900-five-minute.png` shows the older question/definition layout without the route receipt, and `site-desktop-1440x900-example.png` still says “Five positive articles paraphrase the same vendor announcement.” The current source now says nine. The report’s claims about current responsive geometry must therefore be downgraded to prior-layout evidence until replaced by current captures.

**[S]** `exports/THOUGHT_PIECE_V14.pdf` was created before the current receipt integration. Its metadata predates the receipt and its source/build companion is not a current rendering of `site/app/page.tsx`. It cannot serve as A4 evidence for this handoff.

**[S]** The in-app browser skill was read and the browser runtime reported no available browser surfaces. This is why the current-pass visual and interactive claims below are explicitly conditional rather than presented as screenshot or human-study findings.

## 1. Conceptual comprehension audit

### Route receipt: strong semantic success, residual “decision gate” risk

**[S]** The current receipt is in `#five-minute`, immediately after the dark concrete preview and before the question grid. It has a visible heading, a fictional/no-live-data line, a boundary sentence that says it is not a required workflow, a four-field decision frame, a claim state, a four-cell count snapshot, a nine-row captioned table, a relation key, two comparison roots, and a human-disposition box.

**[S]** The receipt has no arrows, no left-to-right lanes, no central aperture, and no clean right-hand output field. Its primary relation is repeated in text: `Origin A · DEPENDENT`. The count distinction is explicit rather than inferred from line topology. This is the correct conceptual correction to the previous hero risk.

**[I]** An expert reader can now answer “What does 09 count?” and “What does 01 count?” without looking at an image. The receipt also makes the crucial non-equivalence visible: `01` is the common-origin cluster count, while `00` is independent supporting origins established for the current claim. B1/C1 are kept outside the nine-row table and explicitly not assessed for claim support.

**[H]** A less attentive reader may still infer that `HOLD · SEEK INDEPENDENT TEST`, the coral left border, and the word `INSUFFICIENT` are an automatic negative state. The receipt says “No automatic action is taken” and “No automatic admission, rejection, or truth verdict,” but the strong action box is visually more decisive than the surrounding explanatory copy. This is the remaining gatekeeper-adjacent risk.

**[P0 design edit]** Before handoff, change the action wording to a relation-neutral, human-owned form:

```text
HUMAN DISPOSITION
HOLD BROAD VALIDATION CLAIM · VERIFY ANOTHER ORIGIN RELATION
The reviewer may inspect a separately authored benchmark and record a reasoned change.
No automatic admission, rejection, or truth verdict.
```

If the shorter heading is required, use `HOLD · VERIFY ANOTHER ORIGIN RELATION` rather than `HOLD · SEEK INDEPENDENT TEST`. “Independent” should remain qualified as `independent-as-stipulated` in the benchmark context; it should not appear as an unqualified fact in the illustrative receipt. Keep the `00` count and relation key unchanged.

**[P1 design edit]** Reduce the coral bar’s decision-like salience or pair it with a neutral pattern/text treatment. It may remain a visual anchor, but it must not be the only cue that distinguishes the human disposition. The current copy already provides the semantic safeguard; the edit is to prevent the border from reading as a rejection channel.

### Count consistency: current source passes; stale artifacts do not

| Surface | Current state | Audit judgment |
| --- | --- | --- |
| Quick preview | “Nine positive articles can still trace to one launch announcement.” | **Consistent.** |
| Receipt | `09` observations, `01` common-origin cluster, `00` independently supporting origins established, `02` comparison roots | **Consistent and explicit.** |
| Worked-example heading/caption | Nine observations share one known origin; two roots shown for comparison | **Consistent.** |
| Worked-example Step 2/3/result | Nine articles/mentions; one known origin; no nine-fold confirmation | **Current source now consistent.** |
| First-paper panel | 80 development, 40 feasibility-only pilot, 300 primary, 60 stress; F2 metadata vs F1 rule | **Aligned with protocol v0.2, with pilot/effect boundary stated.** |
| Existing screenshot packet and prior PDF | Old five-article wording and no receipt | **Stale; must not be shipped as current QA evidence.** |

**[P0 design/process edit]** Replace or relabel the stale screenshot packet/report before handoff. At minimum, add a prominent `PRE-RECEIPT ARCHIVE · NOT CURRENT SITE` marker to the old packet and generate current captures with the same filenames or a new manifest. Otherwise a later reviewer can reasonably compare the current source against visibly contradictory screenshots and conclude that the count is still broken.

### H1 after demotion

**[S]** The H1 is no longer in the masthead. It follows the receipt, is constrained to `width: min(100%, 820px)`, is lazy-loaded, and is captioned “Optional material metaphor.” Its alt explicitly says that paths/colors do not encode required route, family, status, correctness, or result.

**[I]** The demotion materially improves the page’s reading order: the exact proposition and exact nine/one relation are available before the image. A reader can understand the receipt with images disabled. This is the correct role change from “hero explanation” to “optional editorial atmosphere.”

**[S]** The pixels have not changed. The current H1 still contains the same one-way lanes, aperture, and calmer output field that Loop 1 identified as a pipeline/gatekeeper metaphor. Moving it down and reducing its width lowers its anchoring power; it does not falsify the topology risk.

**[DJ] Final H1 decision:** retain only conditionally during local owner review, and treat **no H1 as the default handoff choice until a current image/no-image reader pass exists**. If the owner requires an image in the local review version, the current demoted placement is the least risky available placement. If any of the following occurs, remove it rather than adding another disclaimer:

- one or more readers describe it as the system route, a funnel, an automatic filter, or a central approval gate;
- the H1 condition reduces critical receipt/map accuracy relative to no-H1;
- the fresh 390 or print crop makes the aperture/output relationship more prominent than the caption/boundary;
- the image delays or visually buries the question grid and definition contract;
- the current visual test cannot be run before handoff.

H2 remains an unsafe substitution because its channels still read as process streams. H3 remains unsafe because lens/check/question glyphs can imply search-as-truth or status. No new image is indicated.

## 2. Image-independent and alternative-text audit

### Route receipt without images

**[S]** The server-rendered receipt does not depend on any `img`, SVG, canvas, or CSS background. The count snapshot, all nine row IDs, relation labels, comparison roots, unknown rule, disposition, and “not a reported dataset” footer are text/HTML. The receipt therefore passes the requested no-image structural criterion.

**[I]** This is the strongest current part of the integration. If a reader sees only the heading, table, and action copy, the intended distinction remains inspectable. The table may require horizontal scrolling on narrow screens, but that is an interaction/layout cost, not an image-dependency failure.

### H1 alternative

**[S]** The H1 has intrinsic dimensions, a non-empty alt, and a visible caption. Its alt includes both the material subject and a negative semantic boundary: paths/colors do not encode a required route, family, status, correctness, or result. This is acceptable for an optional metaphor.

**[P1 design edit]** Add “illustrative only” or “not a process diagram” to the alt itself if the image remains in the final local version. The visible caption already says “Optional material metaphor”; an alt-only reader should not have to infer that from the figure’s surrounding placement. A concise candidate is:

> Illustrative field of evidence fragments and bounded context frames; no required route, status, correctness, or result is encoded.

Do not describe the aperture as “admitting,” “withholding,” or “passing” material in alt text.

### E2 alternative

**[S]** E2’s alt explicitly names one coral source artifact, nine report fragments, two separately rooted fragments, and the fact that common origin does not make the reports false. The caption states that nine observations share one known origin, two artifacts have separate roots, repetition is neither erased nor treated as proof, colors encode no status, and the image is not a dataset/audit/result.

**[I]** E2 is semantically sufficient without visual inspection because the live worked-example text repeats the count, relation, claim split, and bounded action. It is the only retained generated asset that materially complements the nearby exact example rather than duplicating the system map.

**[P1 design edit]** Preserve the current E2 alt/caption, but change any future copy that calls B1/C1 “independent” without `separately rooted` or `independent-as-stipulated`. The image cannot establish that distinction by texture alone.

### v13 alternative

**[S]** The v13 image is wrapped in a full-resolution link, preceded by `Historical reference · v13 · not the v14 system map`, and followed by a caption saying its seven-step strip is historical. The `details` text summary states the six families, central hub, historical seven-step workflow, and v14 shift.

**[H]** The v13 image’s alt and collapsed text summary are enough for a high-level boundary, but not a complete textual inventory of the seven historical step labels. A reader who needs to inspect the archival artifact without opening the PNG may still lack exact step content. This is not a v14 topology error; it is a historical accessibility completeness gap.

**[P1 design edit]** Add a complete, concise seven-step transcription to the visible/expandable text summary, or explicitly state that the PNG is a decorative historical reference and link to a textual archival record. Do not expand the portrait by default on mobile simply to make its internal lettering readable; text is the more resilient alternative.

## 3. Responsive audit by target surface

Because no current screenshot was available, the following combines direct CSS geometry with the stale-capture limitation. “Pass” below means the source has a plausible containment rule; it does not mean a fresh render has been visually verified.

### 390 × 844 mobile

**[S] Source geometry:** at `max-width: 780px`, the outer site width becomes `calc(100% - 30px)`; the route frame, count grid, lower receipt columns, route cards, question grid, and example grids collapse to one column. The route table remains `min-width: 740px` inside `.route-receipt-table-scroll { overflow-x: auto; }`. The H1 image is full available width, approximately 16:9, with a caption below. The v13 figure is capped at 360px and the example image stacks above its caption.

**[I] Likely success:** the document should not horizontally overflow merely because the receipt or existing state table is wide; both are explicitly scroll-contained. The nine/one count is visible before the table and does not require scrolling. The H1 is no longer in the initial masthead viewport.

**[H] Main mobile risks:**

- the receipt is now a long vertical block before the question grid, so a reader may scan the large `09 / 01 / 00 / 02` values and skip the relation key or human boundary;
- the 740px ledger requires horizontal scroll to see all four columns, so the critical “not independent support” text may be off-screen after the reader sees `Origin A · DEPENDENT`;
- the four count cards become a long stack and can make `00` look like an absence/error rather than “not established for this claim”;
- the current H1 still occupies roughly 200px plus caption after a very long receipt and may feel like a second explanation rather than optional atmosphere;
- the v13 portrait remains a tall interruption when the continuity section is reached.

**[P0 capture check]:** at 390 × 844, verify that (a) the receipt’s four count labels are visible without a sideways gesture, (b) the scroll hint is visible before the table, (c) no page-level horizontal scrollbar appears, (d) H1 is not the first image encountered, and (e) the E2/v13 captions remain attached to their images.

**[P1 edit if the check fails]:** add a compact mobile relation summary immediately before the scroll table, such as `O01–O09 · Origin A · DEPENDENT · 0 independent supporting origins established`, while keeping the full semantic table for audit. This is a redundant text aid, not a replacement for table semantics.

### 720 × 900 intermediate

**[S] Source geometry:** at widths below 900px the rail becomes sticky and horizontal; below 780px the site enters the one-column layout. At 720px the one-column receipt rules apply. The route table remains contained in its own scroll region; the main page should remain within viewport width.

**[I] Likely success:** 720px is a useful pressure test because it exposes the stacked receipt and H1 without the extreme narrowness of 390px. The current heading/receipt ordering is conceptually stronger than the stale packet: proposition, route cards, problem, receipt, then optional H1.

**[H] Main intermediate risks:**

- the sticky rail consumes vertical space and can hide the top of an anchored section if `scroll-padding-top: 64px` is insufficient for font enlargement;
- the route receipt may dominate the first several screens, making the subsequent question grid and distinction contract feel like a second pass rather than part of the five-minute overview;
- table horizontal scrolling plus a long page may cause the reader to miss the separate-root note below the table;
- the H1’s width rule is safe geometrically but its image/receipt repetition may be cognitively redundant.

**[P0 capture check]:** capture 720 × 900 with the top of the receipt, ledger, and H1 transition visible across successive scroll positions. Confirm the `HOLD`/`INSUFFICIENT` state is not mistaken for an automatic route gate and that the first-image order is still receipt before H1.

### 1440 × 900 desktop

**[S] Source geometry:** the page shell leaves 118px for the rail; content is capped at 1180px. The section body is approximately 950px after the 180px marker and 50px gap. The receipt table’s 740px minimum therefore fits without scrolling at desktop, and the demoted H1 caps at 820px and centers.

**[I] Likely success:** the receipt should read as a single framed artifact with a clear top-to-bottom hierarchy. The 2 × 2 decision frame and four-cell count grid are plausible at this width; the H1 is visibly subordinate to the receipt because it is narrower and later.

**[H] Main desktop risks:**

- the receipt’s full border, four large count numerals, table, and coral disposition box may read as a product dashboard or authoritative audit record despite the fictional/no-verdict labels;
- the repeated `DEPENDENT` rows may be visually monotonous and make the reader’s eye skip the relation key;
- the v13 portrait is still visually dense and colorful relative to the text, even with a historical boundary;
- the retained H1 can still be interpreted as an explanatory system visual if its aperture is noticed before the reader reaches the map.

**[P0 capture check]:** on the actual current page, ask an independent reviewer where the proposition, route receipt, system map, and worked example begin. If the reviewer calls the receipt a “pipeline” or the H1 the “system map,” use the no-H1 disposition and revise receipt emphasis.

## 4. Keyboard, focus, and semantic behavior

### Direct positives

**[S]** Global CSS gives links, buttons, summaries, and `[tabindex="0"]` elements a 3px blue `:focus-visible` outline. The skip link is keyboard-reachable. The two horizontal-scroll regions have labels/descriptions and are intentionally focusable. Component records use native `details/summary`; the existing `CollapseControl` test checks that closing a record returns focus to its summary. The v13 image is a normal link with a descriptive accessible label.

**[S]** The current served HTML has no duplicate IDs and all tested ARIA ID references resolve. The route table has a caption, column headers, row headers, and nine row records. The receipt does not use `aria-live`, `role="status"`, custom drag behavior, or hidden image-only data.

### Missing direct evidence

**[S]** No full Tab traversal, screen-reader announcement trace, mobile keyboard traversal, or print-media emulation was performed in this Loop 3 pass because the in-app browser was unavailable. The existing QA report also explicitly discloses that it did not complete a synthetic Tab traversal and that its visual packet predates the current receipt.

**[P0 handoff check]:** perform a short manual sequence on the current rendered page:

1. Tab from the browser/page start through the skip link, rail links, route cards, receipt scroll region, v13 link/summary, component summaries, close controls, worked-example links, research/source links.
2. Confirm focus is never invisible, trapped, or lost behind the sticky rail.
3. On the receipt scroll region, verify the focus announcement includes a useful region name and the visible scroll hint is nearby.
4. Open/close one component and the v13 summary with keyboard only; verify focus return/retention.
5. With images blocked, read the page in DOM order and confirm the three image alternatives do not replace live claims.

### Semantic issue to repair

**[S]** The claim block inside the receipt is a `div` whose first text is a styled `p.card-label` (`Claim under review`), while the other receipt blocks use `h4` headings. A screen-reader heading navigation user will find `Count snapshot`, `Observation ledger`, `Origin relation key`, `Separate roots shown for contrast`, and `HOLD…`, but not the claim block as a peer heading.

**[P1 exact edit]:** make the claim block a section with a visible `h4 id="origin-receipt-claim-title"` and `aria-labelledby`, or give the existing label a heading element at the same level. Keep the visual style if desired. This is a small semantic consistency fix, not a change to the claim.

### Focus/scroll judgment

**[DJ]** Keeping the receipt table’s overflow region focusable is justified because the table is intentionally wider than 390px. Do not remove `tabIndex={0}` merely to shorten the Tab sequence. If a fresh manual pass finds the region too noisy, provide a visible link to the ledger rather than silently allowing a keyboard user to miss columns.

## 5. Print/A4 audit

### Direct source positives

**[S]** Print CSS sets A4, hides interactive-only navigation, makes the receipt table overflow visible, removes its 740px minimum, repeats the table header with `display: table-header-group`, reduces table text to 7pt, and preserves the image’s intrinsic aspect ratio with `object-fit: contain`. The v13 text summary is forced open in print. The route receipt’s header/frame/claim/count/disposition blocks are marked `break-inside: avoid`.

### Residual print risks

**[H]** The current A4 output may still be awkward even if it is technically unclipped:

- the nine-row table may split across pages while the relation key and separate-root note move to the next page;
- `.route-receipt-lower` is not included in the print `break-inside: avoid` set, so its two explanatory columns can split or strand the B1/C1 note;
- `.continuity-note` retains its desktop three-column grid in print. With a 150px marker, 280px v13 figure, two 28px gaps, and a narrow remaining text column, the historical prose can become cramped beside a tall portrait;
- the receipt’s large count values and full table add substantial pages before the system map; the old 25-page companion cannot predict the new length;
- H1 remains printable even though it is optional. Without a current print decision, the A4 artifact may carry both the large receipt and a large metaphor image, increasing visual load.

**[P0 print check]:** render a fresh A4/PDF from the current site and inspect page boundaries. Confirm the receipt title, fictional/no-verdict boundary, count snapshot, table header, relation key, B1/C1 note, and human disposition remain legible and associated. Confirm the v13 historical label and text summary precede/follow the portrait on the same page or provide an unambiguous page break.

**[P1 exact CSS edits if needed]:**

```css
@media print {
  .route-receipt-lower,
  .route-receipt-key,
  .route-receipt-disposition,
  .continuity-note {
    break-inside: avoid;
  }

  .continuity-note {
    display: block;
  }

  .origin-map-figure {
    width: min(100%, 72mm);
    margin-top: 6mm;
  }
}
```

The exact widths should be tuned against the fresh PDF; the purpose is to prevent the v13 portrait from squeezing the continuity prose into an unreadable third column and to keep the receipt’s relation explanation together.

## 6. Research-panel and first-paper boundary audit

**[S]** The current panel reads “Can a model use stipulated origin-relation metadata without overcounting copied evidence?” It states 80 development bundles, 40 feasibility-only pilot bundles, 300 primary bundles, 60 stress bundles, exact F1/F2 token parity, one frozen model, and a five-point candidate valid-origin-recall loss. It explicitly says the test is cue use, not provenance discovery or the full layer.

**[I]** This is materially tighter than the prior generic “typed context judgment” wording and is aligned with protocol v0.2. It keeps the receipt’s `DEPENDENT`, `INDEPENDENT-AS-STIPULATED`, and `UNKNOWN` vocabulary inside an oracle/stipulated boundary.

**[P1 design edit]** The words “before locking three hundred primary and sixty stress bundles” are methodologically accurate in context but can read like a promise of a future completed study. Keep “proposed” or “design draft” visibly adjacent to the panel, and preserve the page’s “not empirically validated” labels. Do not add a result-like effect size to the panel.

**[P1 consistency check]:** ensure the route receipt uses the same relation vocabulary and boundary as the protocol’s four separate vocabularies: derivation, origin family, claim stance, and action. The current receipt mostly does this; the action heading’s unqualified “independent” is the remaining mismatch.

## 7. Prioritized edit list before handoff

### P0 — must be resolved before claiming current visual readiness

1. **Generate and inspect fresh current captures.** Use the actual integrated page at 1440 × 900, 720 × 900, 390 × 844, and A4/print. Replace or explicitly archive the old pre-receipt screenshot packet and PDF. Verify receipt, H1 order, E2 caption, v13 label, page overflow, caption adjacency, table scroll, and print pagination.
2. **Make the disposition language relation-neutral.** Replace `HOLD · SEEK INDEPENDENT TEST` with `HOLD · VERIFY ANOTHER ORIGIN RELATION` or equivalent, and retain the no-automatic-verdict text. Do not let the coral border or “independent” word recreate the gatekeeper metaphor.
3. **Run a short manual keyboard/image-blocked pass.** Confirm skip link, sticky rail, table scroll region, native disclosures, focus return, image alternatives, and no hidden claim in a raster. Record the result in the current QA report.
4. **Choose the H1 handoff state.** If the current visual/reader pass cannot be completed before handoff, remove H1 for the handoff artifact. If it is retained for local owner review, keep it demoted and mark it conditional; do not call it the hero.

### P1 — fix in the next coherent source pass

1. Promote the receipt claim block’s styled label to a real `h4`/labelled section for heading navigation.
2. Add a compact mobile text summary of `O01–O09 / Origin A / DEPENDENT / 00 independent supporting origins` if the 740px table causes readers to miss relation columns.
3. Add the complete v13 seven-step text transcription or a clearly linked archival transcript; do not make the portrait itself the accessible source.
4. Add print break rules for the lower relation block and collapse the continuity note to a block in print if the fresh A4 render confirms cramped columns.
5. Extend structural tests to assert all three image alts/captions, receipt `caption`/`scope`/ARIA references, exactly nine receipt rows, current nine-count wording, H1 demotion/order, and the presence of the explicit no-verdict boundary. Keep viewport/print checks separate from the Node HTML tests.
6. Keep the visual QA report and asset manifest synchronized with the current production derivatives and hashes. The old packet should remain available for audit but must be labelled historical/pre-receipt.

### P2 — only after current comprehension passes

1. Consider reducing repeated table copy while preserving all typed relation information; the current nine identical “repeats the launch announcement” cells may be visually monotonous at desktop.
2. Consider whether E2 can be made slightly smaller now that the receipt carries the exact relation; do not crop away its source or separate roots.
3. If H1 passes the reader test, keep it as a small editorial break only. Do not regenerate H2/H3 or add a second abstract topology image.

## 8. Final image/no-image reader judgment

**[S]** In the current served HTML, the route receipt is fully interpretable without images. The E2 and H1 images are optional after the receipt; v13’s high-level historical boundary is available in alt/caption/text summary, though its complete step transcription remains a P1 improvement.

**[I]** The page’s conceptual center has successfully moved from “look at an evidence-processing image” to “inspect a typed relation record, then optionally see editorial material.” This is a material improvement over the prior integrated hero placement.

**[H]** A reader may still over-credit the receipt as an authoritative audit because of its large frame, count numerals, table, and disposition box. The copy says fictional/no verdict, but the visual form resembles a product receipt. The fresh test should ask readers whether the receipt is a worked illustration, a live system record, a reported dataset, or an approval artifact.

**Decision:** keep the semantic receipt; retain E2; retain v13 as historical; hold H1 only conditionally and default to no H1 for any handoff that precedes current visual/reader verification. No image currently earns the right to define the v14 topology. The deterministic HTML is the comprehension surface; the images are subordinate editorial roles.

## 9. Evidence and judgment ledger

| Finding | Type | Why it matters |
| --- | --- | --- |
| Current server responds 200 and contains receipt/H1/E2/v13/research panel. | **[S]** | Confirms the integrated source is actually served locally. |
| Receipt contains nine row IDs, caption, scoped headers, relation key, counts, unknown note, and human disposition. | **[S]** | Supports image-independent semantic comprehension at the DOM level. |
| Current page no longer contains the stale five-article wording. | **[S]** | Count inconsistency is fixed in source; old screenshot/PDF evidence remains stale. |
| Receipt is less pipeline-like than the H1. | **[I]** | It uses grouped fields and repeated relation text rather than directional topology. |
| `HOLD · SEEK INDEPENDENT TEST` can sound like a gatekeeper action. | **[H] + [DJ]** | Strong action wording and coral border may override the no-verdict copy; revise/test. |
| H1 demotion lowers but does not eliminate semantic topology risk. | **[I]** | Pixels are unchanged; only placement/width/caption changed. |
| E2 is the strongest current editorial image. | **[DJ]** | Its count/origin relation is adjacent to exact live text and its alt/caption preserve the boundary. |
| v13 should remain historical, not removed. | **[DJ]** | It preserves the exact recovered anchor, but needs a fuller text alternative. |
| Current responsive/print behavior is safe. | **Not yet claimed** | CSS is plausible; current screenshots/PDF do not cover the new receipt. |
| The receipt improves reader accuracy. | **Not claimed** | No human reader study was run. |

## References used for the audit

- Local current source: `site/app/page.tsx`, `site/app/globals.css`, `site/tests/rendered-html.test.mjs`.
- Local visual constraints: `reports/V14_VISUAL_ASSET_EXPERIMENT_PLAN.md`, `assets/imagegen/IMAGE_SELECTION_LEDGER.md`.
- Local prior review: `research/overnight/rounds/06_LOOP1_VISUAL_READER_RED_TEAM.md` and `research/overnight/rounds/09_LOOP2_OPPORTUNITY_AND_INTERFACE_SPEC.md`.
- Local current study boundary: `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` version 0.2.
- Local historical-source boundary: `archive/v13/LIVE_SITE_REFERENCE_MANIFEST.json`.
- Local QA limitation: `reports/VISUAL_READER_QA_REPORT.md`.
- W3C [WCAG 2.2 SC 1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html), [SC 1.4.1: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), [HTML tables](https://html.spec.whatwg.org/multipage/tables.html), and [ARIA disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/). These support the semantic/alternative-text recommendations; they do not establish reader comprehension of this page.
- Ziemkiewicz & Kosara, “The Shaping of Information by Visual Metaphors,” DOI [10.1109/TVCG.2008.171](https://doi.org/10.1109/TVCG.2008.171), and Hullman & Diakopoulos, “Visualization Rhetoric: Framing Effects in Narrative Visualization,” DOI [10.1109/TVCG.2011.255](https://doi.org/10.1109/TVCG.2011.255). These support treating aperture/funnel/gate framing as testable interpretation rather than neutral decoration.

## Handoff summary

The current integration is conceptually much stronger than the prior hero-first layout. The route receipt succeeds as a deterministic, image-independent distinction between nine observations and one known origin; E2 remains the right illustrative example; v13 remains a bounded archival anchor; and H1 is appropriately demoted but not yet earned as a retained handoff asset.

Before handoff, replace the stale captures/PDF with current 1440/720/390/A4 renders, run the short manual keyboard/image-blocked pass, and neutralize the “seek independent test” wording. If those checks cannot happen, ship the deterministic receipt, E2 with its text boundary, and v13 with its archival label, but omit H1. No core files, images, publication, or deployment were changed by this review.
