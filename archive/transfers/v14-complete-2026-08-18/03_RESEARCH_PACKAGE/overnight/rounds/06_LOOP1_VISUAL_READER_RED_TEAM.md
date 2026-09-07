# Loop 1 visual-reader and metaphor red team

**Prepared:** 2026-08-18  
**Lane:** Pattern Recognition / Discrimination Layer  
**Status:** Independent read-only red team for the current local owner-review site. No core files were edited.  
**Scope:** Conceptual fidelity, topology, accessibility, crop resilience, cognitive load, responsive/print behavior, asset provenance, and whether the editorial images clarify or compete with the deterministic map.

## Bottom line

**[Design judgment from direct inspection]** The current integration is polished and coherent in palette, but the hero image is a high-risk semantic failure as currently used. Its colored lanes run left-to-right from heterogeneous evidence fragments through a central aperture/gate into a quieter right-hand context field. That topology reads as a mandatory filtering pipeline, even though the caption says “not a process diagram” and the prose says the flow is not a conveyor belt. The lone return line at the bottom does not counteract the dominant one-way reading.

The worked-example image is materially stronger: a visible source artifact branches to a countable set of report-like fragments, with two separately rooted artifacts at the side. Its adjacent live copy correctly carries the exact claim. It still needs a crop/count audit at mobile and print sizes because its provenance lines are the meaning-bearing detail.

The v13 historical anchor is correctly labeled as historical and linked to the full-resolution file. Its main risk is not incorrect labeling in the source; it is visual authority. The large portrait contains a central “Peripheral Signal Mining” hub and a conspicuous seven-step strip, so a quick reader can import the old topology as the current v14 system before reading the caption. At narrow widths it also becomes a tall interruption in the five-minute path.

The most important operational fact is that the existing visual QA packet predates the current image integration. The QA report explicitly says its twelve PNG inputs are not captures of the revised site. The current source passes structural tests, but the integrated hero, historical anchor, and worked-example image still need a fresh 1440, 720, 390, and print inspection. The correction list below treats that as an acceptance gate, not a cosmetic follow-up.

## Inspection record

### Materials inspected

- README.md, reports/V14_VISUAL_ASSET_EXPERIMENT_PLAN.md, reports/VISUAL_READER_QA_REPORT.md, and reviews/luna/FINAL_READER_AUDIT_SUMMARY.md.
- assets/imagegen/IMAGE_SELECTION_LEDGER.md, which records the production-derivative hashes and the editorial candidate decisions.
- Current site source: site/app/page.tsx, site/app/globals.css, site/app/content.ts, and site/tests/rendered-html.test.mjs.
- Integrated production-referenced assets:
  - site/public/images/context-before-answer.jpg, 1672 × 941, approximately 511 KB.
  - site/public/images/v13-six-families-origin-map.png, 1024 × 1536, approximately 1.9 MB.
  - site/public/images/nine-mentions-one-origin.jpg, 1536 × 1024, approximately 525 KB.
- Existing clean candidate renders:
  - H1 evidence-aperture, H2 braided-origins, H3 cartography-of-attention.
  - E1 nine-windows-one-origin, E2 echo-sheets-watermark, E3 provenance-constellation.
- Existing ChatGPT preview captures. These are portrait screenshots with black application chrome and prompt/edit controls, not production assets.
- Existing static desktop/mobile captures under reviews/claude_desktop/packet/. These are useful for the pre-image layout and map/typography, but the QA report says they are pre-disposition inputs rather than captures of the revised live site.

### Verification checks run

- npm run lint: passed with three non-fatal @next/next/no-img-element warnings at the three newly referenced image elements (hero, historical map, worked example).
- npm test: passed all four tests; the build completed and the server-rendered HTML/navigation assertions passed. The build emitted the existing vinext route-classification note.
- Image dimensions, file sizes, direct references, and SHA-256 values were inspected locally. The integrated hero and worked image are production derivatives rather than byte-identical candidate PNGs; the asset-selection ledger identifies them as H1 and E2 respectively and records their production hashes, placements, and final alt text. The ledger is useful provenance, but it is an editorial selection record rather than reader evidence and does not remove the need for the comprehension test below.

These checks establish source/build integrity, not reader comprehension or visual validity.

## Evidence posture

- **[Sourced evidence]** Visual metaphors carry an implied ontology. In a controlled study, compatible and incompatible verbal metaphors changed how users derived information from graph forms. [Ziemkiewicz and Kosara, “The Shaping of Information by Visual Metaphors,” IEEE TVCG, DOI](https://doi.org/10.1109/TVCG.2008.171).
- **[Sourced evidence]** Narrative visualizations frame interpretation through selection, omission, representation, annotation, and interaction; a caption does not erase the framing effect of the visible structure. [Hullman and Diakopoulos, “Visualization Rhetoric,” DOI](https://doi.org/10.1109/TVCG.2011.255).
- **[Sourced evidence]** Uncertainty encodings should be matched to uncertainty types rather than treated as one universal visual quantity. [MacEachren et al., “Visual Semiotics & Uncertainty Visualization,” DOI](https://doi.org/10.1109/TVCG.2012.279). A survey of 86 uncertainty-visualization studies also argues for measuring more than performance and satisfaction. [Hullman et al., “In Pursuit of Error,” DOI](https://doi.org/10.1109/TVCG.2018.2864889).
- **[Sourced evidence]** Graph readability is task- and size-dependent: node-link views help some path tasks while matrix or table forms can help at larger sizes. [Ghoniem, Fekete, and Castagliola, DOI](https://doi.org/10.1057/palgrave.ivs.9500092).
- **[Sourced evidence]** Claim-retrieval interface work combines context, provenance, user control, and serendipity rather than assuming one search route. [Dück, Holter, and Chan, “Finding Needles in Document Haystacks,” DOI](https://doi.org/10.1145/3706598.3713715).
- **[Sourced evidence]** PaperTrail’s CHI 2026 claim/evidence interface found a trust–behavior gap and clutter/usability costs when granular provenance was added. [Martin-Boyle et al., DOI](https://doi.org/10.1145/3772318.3791101).
- **[Direct inspection]** The current hero has arrows, lanes, a central gate, and a left-to-right output field; the worked image has a source fan-out and two side roots; the v13 image has a hub and an explicit seven-step strip.
- **[Design judgment]** The hero’s topology is more likely to override its disclaimer than the disclaimer is to correct the topology. The worked image and v13 anchor need adjacent text because their meaning-bearing relations become difficult to inspect when reduced.
- **[Testable hypothesis]** A reader who sees the current hero before the thesis will be more likely to describe an automatic filter or fixed pipeline than a reader who sees the thesis with no hero or with a non-directional editorial image.

## Asset-by-asset red team

### A. Integrated hero: context-before-answer.jpg

**What works**

- **[Direct inspection]** The ivory, navy, teal, coral, violet, ochre, sage, and blue palette fits the site and echoes the six-family system without using literal labels.
- **[Direct inspection]** Heterogeneous fragments, origin points, a translucent inspection structure, and a bounded right-side field make “context before answer” immediately legible at a glance.
- **[Direct inspection]** It avoids robots, chat windows, faces, brand marks, and claims of empirical proof. The caption explicitly says it is an editorial illustration and not a process diagram.
- **[Design judgment]** The wide 16:9 aspect ratio and generous margins are good for a masthead and survive a straightforward desktop/mobile width reduction better than a dense portrait asset.

**Conceptual failure**

- **[Direct inspection]** Five or more colored routes visibly begin on the left, enter the same layered chamber, and continue through a hard-edged gate toward the right. Most endpoints are arrows or clean field elements. This is a classic input → filter → output grammar.
- **[Design judgment]** The central aperture looks like a single authority that decides what is admitted. The thesis instead separates authority, support, independence, relevance, authorization, action priority, and human disposition, and permits different orders, holds, questions, and refusals.
- **[Design judgment]** The bottom blue return line is too thin and too peripheral to rebalance the dominant flow. A reader can interpret it as a technical retry path, not a consequential human correction or an alternate evidence branch.
- **[Direct inspection]** The right-hand field is visually calmer and cleaner than the left. That makes the output look more resolved or more trustworthy even though the thesis does not claim that selection produces truth.
- **[Direct inspection]** Several paper fragments contain pseudo-text, charts, and marks that resemble source evidence. Because there is no text equivalent for those marks, a reader may infer specificity or empirical grounding that is not there.
- **[Design judgment]** Reusing the same six-family accent colors in the hero can make decorative colored lanes look like exact family assignments. The current caption does not say that color is decorative and does not map to the live family cards.

**Red-team verdict:** **Do not treat the integrated hero as semantically safe merely because it is labeled illustrative.** It is a strong editorial object but a weak representation of non-linear evidence discovery. Keep only after the reader test, and prefer either a non-directional field/aperture image or an explicit revision that removes the one-way lane grammar. Selecting no hero is a valid result under the asset plan.

### B. Historical anchor: v13-six-families-origin-map.png

**What works**

- **[Direct inspection]** The file is the recovered 1024 × 1536 diagram and is linked as a full-resolution image. The source caption says “Historical origin map · v13,” states that the original diagram is hash verified, and explicitly warns that its seven-step strip is historical rather than the v14 topology.
- **[Design judgment]** It gives the continuity note a concrete historical artifact rather than an unsupported verbal claim. This is valuable if the reader needs to understand why v14 moves from finding peripheral signals to deciding what may influence generation.
- **[Direct inspection]** The image has enough internal labels for a sighted reader who opens the full-resolution link to inspect the old system.

**Reader and layout risks**

- **[Direct inspection]** The central hub, surrounding families, and “HOW IT WORKS (7 STEPS)” strip are visually more explicit and diagrammatic than the current v14 relationship map. A fast reader may treat this older visual as the canonical map and skim the v14 map as a restatement.
- **[Design judgment]** The label in the figcaption arrives after a large, high-authority image. A pre-image eyebrow such as “HISTORICAL REFERENCE · NOT THE V14 SYSTEM MAP” would establish the boundary before the reader interprets the topology.
- **[Direct inspection]** At desktop the portrait is placed in a third grid column beside the continuity text. At narrower widths it becomes a standalone column with a default width of up to 360 pixels and a natural height of roughly 540 pixels. That is a large interruption in the five-minute path before the distinction contract.
- **[Design judgment]** A sighted reader may remember “central signal mining plus seven steps” more strongly than the prose distinction between the historical and current systems. A screen-reader user receives a long family/step description in alt text but not a complete textual transcription of the map.
- **[Print risk]** The print stylesheet does not give the historical figure a dedicated width/height or a compact archival treatment, while the continuity grid retains its multi-column structure. A print renderer may make the map small beside a narrow text column or split the caption from the image.

**Red-team verdict:** Keep the historical anchor, but contain its authority and footprint. Treat it as a referenced artifact with a short textual summary and a full-resolution link, not as an inline second system map.

### C. Integrated worked-example image: nine-mentions-one-origin.jpg

**What works**

- **[Direct inspection]** A coral source artifact at left fans to nine visually distinct report-like cards. Two side artifacts have separate roots. The repeated observations are preserved rather than deleted.
- **[Direct inspection]** The image has a 3:2 landscape shape and no readable text or real brands, which is appropriate for a conceptual example.
- **[Design judgment]** It complements the adjacent six-step live sequence better than the hero complements the system map. It provides an intuitive origin-cluster cue while the HTML carries exact claims, wording, and limitations.
- **[Direct inspection]** The current caption makes the crucial boundary explicit: the nine observations are not treated as nine independent confirmations, and the side artifacts are illustrative separate origins.

**Reader and crop risks**

- **[Direct inspection]** The provenance lines are fine and numerous. At 360-pixel mobile width they will be visible as texture rather than inspectable relations. The image can communicate “many cards point to a source” but not the exact distinction among report, intermediate repost, and independent origin.
- **[Design judgment]** The fan-out can still imply that a known common origin makes all nine reports false or irrelevant. The live text correctly says they remain observations; the image alone does not.
- **[Print risk]** The print rule applies object-fit: cover and a max-height of 72 mm. If the grid row height or print width forces cropping, the source artifact or one of the two separate roots can disappear while the caption still claims it exists.
- **[Accessibility risk]** The alt text is unusually good in that it names the source, nine fragments, and two separate roots. It should also say that the image is illustrative and does not establish factual provenance; otherwise a screen-reader user may hear a definitive finding rather than an example.

**Red-team verdict:** This is the strongest current image for retention, provided the origin count, two independent roots, and illustrative status survive all crops and the alt/text equivalent remains adjacent.

### D. Candidate and preview set

The clean candidates were inspected at native size. The preview files are portrait screenshots of a generation/editing interface with black chrome and should not be treated as production artwork, thumbnails, or provenance evidence.

| Asset | Provisional desk score / 28 | Strength | Red-team concern | Current decision |
| --- | ---: | --- | --- | --- |
| Integrated H1 / context-before-answer | 20 | Strong material, wide crop, clear “inspection” motif | Gate and arrows create the exact filter/pipeline grammar the essay rejects | Reject as-is; test only after a non-directional revision or omit |
| H2 / braided-origins | 21 | Crossings, side paths, and double-headed comparisons are richer than H1 | Streams still enter one cylindrical chamber and resolve into a right-hand output; it remains a conveyor with decoration | Do not substitute as-is |
| H3 / cartography-of-attention | 21 | Shows a boundary, peripheral clusters, an unknown gap, and changing attention | Large magnifying glass implies spotlight/search-as-truth; check/question glyphs imply status; radial center can make salience look like authority; mobile crop loses the boundary | Possible section transition only after a reader test; not a safe hero by default |
| Integrated worked example | 25 | Countable cards, common source, separate roots, strong editorial fit | Fine topology becomes texture at mobile/print; side roots may crop; common-origin fan can imply falsity | Best current retention candidate with explicit text and crop QA |
| E1 / nine-windows-one-origin | 25 | Nine countable cards, direct origin fan, two side artifacts | Direct fan oversimplifies transformations; exact count and side-root positions need a crop test | Strong alternative if its count and caption are verified |
| E2 / echo-sheets-watermark | 25 | Material transformation and repeated-source idea are intuitive | “Watermark” can imply authenticity/security; line groups remain directional; central source may disappear in narrow crops | Optional alternative; do not use the watermark as a credibility encoding |
| E3 / provenance-constellation | 23 | Intermediate origin nodes and an explicit unresolved gap are useful | More like a graph specification than an editorial entry; top-level report count is hard to verify at a glance; hierarchy can imply the coral artifact is truth | Use only if the deterministic relation legend is nearby; otherwise redundant |

Scores are an **independent [Design judgment]** applying the existing asset-plan rubric, not a user-study result. They intentionally challenge the production ledger’s more favorable H1 score (27/28) because this pass evaluates topology as a reader might infer it, not only prompt compliance and craft. The ledger’s E2 selection and provenance record are sound, but neither score is visual comprehension evidence. The plan’s “at most one hero and one worked-example image” rule is sound; the historical archive figure should remain a separately labeled third role.

## Topology, accessibility, and cognitive-load audit

### What the deterministic map gets right

**[Direct inspection]** The current six-family HTML map is a sparse 2 × 3 card grid with a prose text equivalent and a human-correction note. It does not draw connecting arrows between every card, which makes it less pipeline-like than the hero. The two-loop figure uses explicit verbs and return text, and the worked-example sequence is live ordered HTML. This is the right division of labor: exact labels and relations in HTML, atmosphere in an image.

**[Prior-review evidence]** The final Luna audit already flagged that the six-family arrows in the earlier visual system implied more linearity than the prose intended. The current hero repeats that same risk more strongly than the sparse HTML map. The visual correction should therefore start at the hero rather than adding another explanatory caption to the map.

### Accessibility

- **Alt-text topology:** The current hero alt says that fragments and source trails are “passing through” an aperture into a bounded field. That wording encodes sequence and reversibility that a screen-reader user cannot verify from the image. Replace it with a concise metaphor statement that explicitly says no exact route, status, or approval is encoded.
- **Historical map:** The v13 alt lists many family names and the learning loop, but does not supply the complete seven-step text or a short text transcription. Add a nearby text summary or a linked archival transcript. A sighted reader can zoom the full PNG; an alt-only reader should not need the image to know that it is historical and not the v14 topology.
- **Worked example:** The current alt names one source, nine fragments, and two separate roots. Preserve that information and add “illustrative; not a reported dataset or provenance finding.”
- **Caption parity:** The figure captions are visible, but the current source does not explicitly connect a caption ID to the image via aria-describedby. Native figure semantics usually expose the relationship, but an explicit association would make the non-evidence boundary more robust across assistive technologies.
- **Color semantics:** The site correctly uses text labels and does not rely on color alone in the HTML map. The images reuse the family palette without a legend. State in the caption or adjacent text that image colors are decorative and do not encode family, support, independence, or confidence.
- **Keyboard and fallback:** A failed image still needs to leave its caption and adjacent live text readable. The current dimensions prevent layout shift, but the source/build tests do not check asset failure, alt length, or crop meaning.

### Cognitive load and visual competition

- The hero is inserted between the title definition and the thesis callout. In the current source it is therefore the first large explanatory object a reader encounters, before the proposition has been stated. The image’s process-like geometry can anchor the interpretation before the disclaimer is read.
- The hero’s six accent colors, the v13 map’s family colors, the HTML family cards, the loop colors, and the worked image’s colored fragments create a repeated visual system. Repetition creates continuity, but it also invites false mapping: a coral lane in the hero may be read as the coral family or as a special status.
- The three production images are not redundant in role on paper—entry metaphor, historical continuity, and worked example—but the hero currently duplicates the deterministic map and loop figure. This makes the editorial image compete with the exact system rather than create emotional entry.
- The v13 portrait adds a second detailed map before the current system map. Even with a caption, it increases memory load and risks making the reader reconcile two topologies before understanding either.

## Responsive and print risk register

| Surface | Current source behavior | Likely failure | Testable correction |
| --- | --- | --- | --- |
| 1440 px desktop | Hero is full content width; continuity note uses three columns; worked image uses a 2.1:0.9 grid | Hero pushes the proposition and route cards below the first screen; v13 portrait dominates a narrow third column; worked image may make the caption too narrow | Capture the actual revised page. Ask where the thesis is first stated and whether the image is mistaken for the system map |
| 720 px reflow | At 900 px the rail becomes sticky; at 780 px most grids collapse; v13 figure is capped at 360 px | A 720-pixel reader gets a tall historical figure and a wide hero before reaching the map; no fresh revised capture verifies this | Test 720 × 900 at 100% and 200% equivalent; preserve the five-minute route and figure captions |
| 390 px mobile | Hero is full width at roughly 360 × 203; v13 figure can be 360 × 540; worked image is full width at roughly 360 × 240 | Fine routes become texture; the portrait can overwhelm the continuity text; horizontal provenance distinctions disappear | Ask readers to identify source, nine reports, two independent roots, and unknowns from the mobile crop and adjacent copy |
| Print | Hero is capped at 82 mm with object-fit: cover; worked image is capped at 72 mm with object-fit: cover; continuity grid is not separately collapsed for print | Meaning-bearing edges or origins can be silently cropped; v13 may be small beside a narrow continuity column; current PDF evidence predates integration | Render a fresh PDF after image integration. Require caption adjacency and an explicit “illustrative” label on the same page |
| Low bandwidth / image failure | Three img elements have dimensions; hero is high-priority, archive/worked are lazy; lint reports three no-img-element warnings | A 1.9 MB archival PNG and two raster images can delay the first decision; a failed hero may leave a large blank region or alter reading order | Add responsive derivatives or a controlled static-image route; test the text-only path and avoid replacing live semantics with an image component |

The lint warnings are not a conceptual failure and do not require a framework-specific image component by themselves. The relevant red-team issue is whether responsive/print optimization changes the visible topology. Any optimization must preserve the full image or declare a focal crop.

## Prioritized, testable correction list

### P0 — resolve before owner approval

#### P0.1 Stop the hero from asserting a one-way filter

**Correction:** Do not ship the current H1 as the visual explanation of the layer without a reader test. Preferred options, in order:

1. Use no hero image and let the title, thesis callout, and deterministic map establish the argument.
2. Keep an editorial hero only if its visible geometry is non-directional: evidence field, bounded frame, competing paths, and human-correctable ambiguity without arrowheads or a single central gate.
3. If the current asset must remain, move it after the proposition and label it as a material metaphor rather than an inspection route; do not expect the caption alone to undo the topology.

**Acceptance test:** In the protocol below, fewer than 1 in 8 formative readers should call the hero a pipeline, funnel, gatekeeper, or automatic approval route, and at least 6 of 8 should state that the image does not encode exact system topology. If the no-image condition performs better, select no hero.

#### P0.2 Make the non-evidence boundary available to image-only and alt-only readers

**Correction:** Revise hero alt/caption language so it does not say that material is “passing through” a reversible aperture. Say that it is an illustrative field for considering evidence before generation and that no route, status, or correctness is encoded. Add a short live text equivalent immediately adjacent to the figure. Apply the same explicit illustrative boundary to the worked image.

**Acceptance test:** With images hidden and only heading, caption, alt-equivalent, and live copy available, readers can answer the eight critical comprehension items below with no critical topology error.

#### P0.3 Re-run visual QA on the actual integrated site

**Correction:** Produce fresh local captures after the current image refs are present at 1440 × 900, 720 × 900, 390 × 844, and print/A4. The existing static packet is not evidence for this integration; the QA report says it predates the revised site.

**Acceptance test:** No image crop separates caption from figure, removes a meaning-bearing source/origin/unknown, hides the “historical” label, or pushes the proposition out of the intended first-screen path without an intentional reading decision.

### P1 — correct in the next visual pass

#### P1.1 Contain the historical anchor’s authority

**Correction:** Put a visible pre-image label such as “HISTORICAL REFERENCE · V13 · NOT THE V14 SYSTEM MAP” before the PNG. Keep the full-resolution link and caption. Consider a contained archival thumbnail or a collapsible “open historical map” treatment so the seven-step strip does not become a second default system map. Never use a crop as if it were the whole historical diagram; use contain and preserve the full link.

**Acceptance test:** Readers identify v13 as historical, can state one difference from v14, and do not name the v13 hub/steps as the current topology.

#### P1.2 Preserve the worked-example semantics at narrow and print sizes

**Correction:** Keep the current image only if a text sentence adjacent to it states: nine observations, one known common origin in the illustration, two separately rooted illustrative artifacts, and no conclusion that repetition is false. Avoid object-fit: cover when it removes any of those anchors; if a crop is necessary, use a declared focal crop and a second text/table representation.

**Acceptance test:** At 390 pixels and in print, readers can identify the common-origin group and the two separate roots from the image-plus-caption; if they cannot, the image becomes decorative and the live text must carry the relation explicitly.

#### P1.3 Remove decorative color ambiguity

**Correction:** Add a short caption sentence that colors in the editorial images are material/illustrative and do not map to the six family statuses, support, authority, independence, or confidence. Keep all exact status and relation encoding in HTML/SVG/text.

**Acceptance test:** Readers shown the hero and family map can name the six families without assigning a hero lane to a family or treating a color as a truth/status code.

#### P1.4 Reduce visual duplication in the five-minute path

**Correction:** Retain at most one hero, one worked-example image, and the explicitly historical anchor, as the asset plan permits. If the hero remains process-like, remove it rather than adding another explanatory map. Do not load candidate previews or alternate candidates in production.

**Acceptance test:** In a 60-second first-impression comparison, readers can state the proposition before describing the image. A high rate of image-first explanations indicates that the hero competes with the thesis.

#### P1.5 Record asset provenance before any later publication decision

**Correction:** Preserve the asset-plan record for each retained image: role, prompt ID, generator route, generation date, selection score, intended placement, exact production hash, source-candidate hash, and final alt text. The current ledger identifies the hero as an H1 derivative and the worked image as an E2 derivative; keep those links explicit because the production files do not byte-match the candidate PNGs.

**Acceptance test:** An independent reviewer can map every production image to its candidate/source, explain why it was selected, and recover the exact file without relying on visual memory.

### P2 — harden after the concept passes

#### P2.1 Make responsive and print crops intentional

**Correction:** Provide responsive derivatives or srcset/sizes where the site runtime supports them. Set an explicit focal point for any print crop. Prefer full-frame containment for topology-bearing images. Re-render the PDF after integration; do not rely on the older PDF inspection.

**Acceptance test:** The hero retains both evidence field and bounded context; the worked image retains source plus both side roots; the archive remains identifiable as a complete historical artifact in print.

#### P2.2 Add a text transcription or structured summary for the historical map

**Correction:** Keep the current concise alt, but add a linked text summary of the v13 family names and seven-step strip. This prevents the PNG’s internal typography from being the only way to inspect the historical artifact.

**Acceptance test:** A reader using only text can understand what v13 asked, what the v14 shift is, and why the older diagram is not the current system map.

#### P2.3 Optimize asset weight without changing meaning

**Correction:** Generate no new art in this loop. If optimization is later authorized, create responsive/compressed derivatives from the retained files, keep the archival PNG linked as the canonical historical source, and record hashes. The current lint warnings can be addressed only if the replacement preserves semantic img behavior, dimensions, alt, captions, and local/offline operation.

**Acceptance test:** Text and proposition render without waiting for a hero image; images do not cause a visible layout shift; image failure still leaves the reading path complete.

#### P2.4 Avoid status glyphs and salience encodings in candidates

**Correction:** Do not select H3 or E3 because a question mark, checkmark, node size, brightness, centrality, or radial placement appears to communicate uncertainty or authority. Those meanings require exact legends and deterministic encoding.

**Acceptance test:** Readers do not interpret a brighter/larger/central node as more true, authoritative, or approved unless the deterministic text explicitly defines that relation.

## Independent-reader comprehension protocol

This is a short formative protocol, not a powered study. Its purpose is to detect a topology or authority misunderstanding before a later owner-review pass. It should be run after fresh captures are available and before any public publication decision.

### Participants and conditions

- Recruit 6–8 independent readers who did not write the site or the overnight memos. Include at least one person who regularly reads technical essays and, if possible, one screen-reader or low-vision reader.
- Use a within-reader, counterbalanced comparison of:
  1. current integrated hero plus live caption;
  2. no hero image, with the same title/thesis/map text;
  3. text/alt-equivalent condition, with the image hidden but caption and adjacent prose preserved.
- Show the v13 anchor and worked-example image in separate blocks. Do not explain the intended answer before the reader responds.
- Test the same content at 1440 × 900, 720 × 900, 390 × 844, and one print/A4 rendering. For a short protocol, assign each reader two viewports and counterbalance the rest; do not claim full responsive coverage from one viewport.

### Task sequence

#### Task A — first-impression hero interpretation

Show only the masthead through the hero and caption for 45 seconds. Ask the reader to answer aloud:

1. What is this image trying to help you understand?
2. Does it show a fixed sequence, a possible relationship, or something else?
3. Does the central structure determine truth, decide admission, or merely suggest inspection?
4. Where could a person hold, redirect, challenge, or stop the route?
5. What would the image not allow you to conclude?

Code each response for pipeline/funnel, single gatekeeper, clean output equals better evidence, human correction, bounded metaphor, exact system specification, and uncertain/other.

#### Task B — proposition and map comprehension

Let the reader continue through the five-minute path. Ask:

6. State the working proposition in your own words.
7. Are the six family cards a mandatory order, a list of responsibilities, or a complete implementation?
8. What can change a current route, and what can change only future routing?

Expected answers are: the layer makes pre-generation context judgment inspectable; the map is a responsibility/relationship decomposition rather than a required sequence or proven implementation; current human correction/evidence can revise a route, while only an approved policy update changes future routing.

#### Task C — historical-anchor boundary

Show the continuity section with the v13 PNG. Ask:

9. Is the visible map the current v14 system map, a historical reference, or an unresolved source?
10. Name one thing the older visual emphasizes and one thing v14 changes.
11. If you ignored the caption, what would you think the seven-step strip was?

The critical error is treating v13’s “Peripheral Signal Mining” hub or seven-step strip as the current v14 topology. A reader may find the old artifact useful while still recognizing that boundary.

#### Task D — worked-example relation

Show the worked image plus its caption, then ask:

12. How many report-like observations are in the illustrative group?
13. What does the common source imply, and what does it not imply?
14. What role do the two side artifacts play?
15. Is this a reported dataset, a provenance audit, or an illustrative example?

Expected answers are nine observations, one known common origin in the illustration, no automatic conclusion that the reports are false or irrelevant, two separately rooted illustrative artifacts, and no empirical/provenance result. If a crop prevents the reader from seeing the side roots, the adjacent text must carry that fact.

#### Task E — text-only and accessibility equivalence

Hide all three production images or provide only their alt/text equivalents. Ask the reader to repeat questions 6, 9, and 12–15. A visual is complementary only if its removal does not remove a claim the HTML and prose are supposed to carry.

For a screen-reader or keyboard spot check, verify:

- the image, caption, and full-resolution historical link are reached in a sensible order;
- the reader hears “illustrative/not evidence” before inferring a process or result;
- the v13 historical boundary and worked-example count are available without opening a raster;
- no pseudo-text in an image is required to understand the argument.

#### Task F — crop and print resilience

At each assigned viewport, ask the reader to point to or describe:

- the evidence field and the bounded context field in the hero;
- the common-origin source and the two independent roots in the worked image;
- the historical label and the full-resolution link for v13.

Record whether a crop changes the answer. A crop that merely removes decorative texture is acceptable; a crop that removes a source, root, unresolved gap, return path, or historical boundary is not.

### Scoring and stop rules

Score eight critical propositions as correct/incorrect:

1. The hero is an editorial metaphor, not a process specification.
2. The proposed layer concerns judgment before generation.
3. The six-family map does not require one linear order.
4. Human correction can affect a current route.
5. Outcome learning does not silently rewrite historical evidence.
6. The v13 image is historical, not the current v14 map.
7. Nine mentions remain observations and are not automatically nine independent confirmations.
8. The worked image’s side artifacts are illustrative separate roots, not a measured result.

Use these **formative gates**, not statistical claims:

- At least 6 of 8 readers should answer at least 7 of 8 propositions correctly in the image condition.
- No more than 1 of 8 readers should make a critical topology error on any single item: hero-as-pipeline, v13-as-current-map, or repeated-mentions-equals-proof.
- The image condition should not reduce critical-item accuracy by more than 10 percentage points versus the no-image condition. If it does, remove or redesign the image.
- At least 6 of 8 readers should describe one human correction/hold/clarify possibility without prompting.
- The alt/text-only condition should preserve all eight propositions. If it does not, fix the live copy rather than adding more image detail.

Also record confidence (1–5), response time, perceived effort (1–5), and the reader’s first spontaneous metaphor. A high confidence score paired with a wrong pipeline interpretation is more concerning than an admitted uncertainty.

### Qualitative error codes

- T1 Fixed pipeline or funnel.
- T2 Central gatekeeper decides truth or approval.
- T3 Clean right-hand field means verified or safe.
- T4 V13 diagram read as current system map.
- T5 Nine mentions treated as independent proof.
- T6 Common-origin reports treated as false or discarded.
- T7 Image color/node size interpreted as status or authority.
- T8 Image-only detail required; alt/text equivalent insufficient.
- T9 Crop removes source, root, unknown, return, or historical boundary.
- T10 Image interpreted as a reported dataset or real case.

The debrief should ask what visual cue caused each error. This distinguishes a caption problem from a topology problem; the latter cannot be repaired by adding a sentence below the image.

## Recommended decision after the protocol

1. **If H1 fails topology comprehension:** remove it from the masthead. The strongest conceptual page may have no hero image; the deterministic map and thesis are already sufficient.
2. **If H1 passes but increases cognitive load:** move it after the proposition and treat it as a section transition, not a mechanism explanation.
3. **If the worked image passes count/origin/crop tests:** retain it with explicit illustrative wording and a text relation summary.
4. **If the v13 anchor causes current-map confusion:** keep the archival link but collapse or visually contain the PNG; add a pre-image historical boundary and text summary.
5. **If image and no-image conditions are equivalent:** prefer the lower-weight, lower-ambiguity composition and preserve the image candidates only in the audit folder.
6. **If the image makes a reader feel the idea but no reader can state the topology:** treat that as emotional entry, not comprehension, and do not let it stand in for the system map.

## Source and judgment ledger

| Item | Type | Use in this red team |
| --- | --- | --- |
| Ziemkiewicz and Kosara 2008, [DOI](https://doi.org/10.1109/TVCG.2008.171) | Primary controlled visual-metaphor study | Supports treating funnel/gate/spotlight geometry as a cognitive claim, not decoration |
| Hullman and Diakopoulos 2011, [DOI](https://doi.org/10.1109/TVCG.2011.255) | Primary/authoritative visualization-rhetoric account | Supports testing selection, omission, annotation, and visible structure |
| MacEachren et al. 2012, [DOI](https://doi.org/10.1109/TVCG.2012.279) | Primary uncertainty/semiotics studies | Supports type-specific uncertainty encodings and avoiding universal confidence color |
| Hullman et al. 2018, [DOI](https://doi.org/10.1109/TVCG.2018.2864889) | Survey of uncertainty-visualization evaluations | Supports measuring interpretation, route, attention, workload, and correction in addition to accuracy |
| Ghoniem et al. 2005, [DOI](https://doi.org/10.1057/palgrave.ivs.9500092) | Primary graph-readability experiment | Supports sparse graphs and a text/table alternative when relation detail grows |
| Dück et al. 2025, [DOI](https://doi.org/10.1145/3706598.3713715) | Primary CHI interface study | Supports preserving context, provenance, user control, and serendipity in discovery |
| Martin-Boyle et al. 2026, [DOI](https://doi.org/10.1145/3772318.3791101) | Primary CHI claim/evidence interface study | Supports the trust–behavior and clutter caution around adding provenance detail |
| Existing reports/V14_VISUAL_ASSET_EXPERIMENT_PLAN.md | Local project constraint | Defines H/E roles, seven-dimension rubric, no-image option, crop tests, and required asset provenance |
| Existing v14 source and site | Project source | Defines the non-linear, human-correctable, evidence-versus-learning boundary |
| Image-by-image observations above | Direct inspection | Establishes visual risks; not empirical reader evidence |
| Protocol and thresholds above | Design hypothesis | Proposed formative test; not a validation result |

## Handoff summary

The current site is structurally healthy, but the integrated visuals have not yet earned conceptual trust. The hero needs a topology test before it is allowed to introduce the thesis. The worked example is promising and complementary, subject to count/origin/crop checks. The v13 anchor should remain, but as a clearly bounded archival artifact rather than a second current map. The next safe action is a fresh, counterbalanced reader pass with image/no-image/alt-only conditions and the exact responsive/print surfaces named above. No new image generation is needed for this loop.
