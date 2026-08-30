# v15.2 post-integration owner-reader / editorial / visual red team

**Review posture:** skeptical owner proxy; non-technical but systems-minded; low tolerance for AI-sounding prose; wants a durable thought piece that can improve real tools and still stand on its own.

**Reviewed:** the integrated v15.2 manuscript, the current home essay and deeper routes, the Signal Foundry bounded case, the v13 historical image treatment, the CSS-native microvisuals, the reading navigation, and the preceding overnight decision/audit records.

**Working tree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`

**Files inspected:**

- `source/THOUGHT_PIECE_V15_2.md`
- `site/app/HomeEssay.tsx`
- `site/app/ReferenceRoutes.tsx`
- `site/app/ReadingNav.tsx`
- `site/app/MicroVisual.tsx`
- `site/app/Term.tsx`
- `site/app/globals.css`
- `reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md`
- `reports/overnight/v15_2/ROUND2_OWNER_READER_REDTEAM.md`
- `reports/overnight/v15_2/ROUND2_SITE_ARCHITECTURE_ACCESSIBILITY_AUDIT.md`

## Executive verdict

This is now a serious, coherent owner-review candidate. The integration made the central idea easier to understand: a summary can inflate apparent plurality before generation, and a small receipt can preserve the distinction between observations, information paths, claim support, permission, and a person’s next action. The manuscript is much less like an AI-generated “framework overview” than the earlier versions because it begins with a concrete failure, states what the record does *not* prove, names prior art, gives a use/skip boundary, and commits to accepting a negative experiment.

The strongest sentence is still the reversal in the first stop:

> The summary has not merely shortened the evidence. It has changed its structure.

The strongest operational habit is the closing one: count observations, inspect distinct paths, test the exact claim, leave unresolved relations unresolved, and record what a person will do next. That is memorable even if the reader forgets the name “discrimination layer.”

The current result is not yet a research paper or a validated general framework. It is a promising design thought piece / research proposal with a bounded worked example and a credible path to falsification. That is an appropriate and honest position. It should not be presented as more than that.

**Release recommendation: CONDITIONAL — do not publish or externally circulate yet.** The argument and design direction should be frozen conceptually, not redesigned. Before release, make one small convergence pass for case visibility, research-language accessibility, tablet/mobile layout, and real browser/print QA. I found no P0 false-claim or status-disclosure failure in the current source, but I did find several P1 issues that are likely to affect a cold reader’s trust or comprehension.

## Evidence and confidence

The current source-level test suite passes its seven checks, including build, server rendering, route identifiers, native popover source checks, responsive/print rules, typography/focus checks, and removal of the old starter preview. That is meaningful evidence of structural consistency.

It is not a substitute for looking at the current integrated pages in a browser. The in-app browser was unavailable during this review, and the existing screenshots in the worktree predate the final v15.2 HomeEssay integration or show earlier v14/v15.1 states. I therefore treat the visual findings below as source/CSS risks to verify, not as claims that the current rendered pixels definitely fail. A fresh screenshot pass is a release gate.

## Cold read, stop by stop

The paraphrases below are what I believe an unaided owner would carry away after each route, before opening the deeper records.

| Stop | Unaided cold-read paraphrase | What works | Jargon / AI-slop / trust flag | Verdict |
| --- | --- | --- | --- | --- |
| **Title / first choice** | “This is about preventing an AI summary from treating repeated material as independent confirmation. I can start with a one-minute failure, use a five-minute receipt, read the longer argument, or inspect records.” | The dek makes the purpose concrete. The explicit technical definition of “discrimination” prevents the most obvious misreading. The time-labelled routes give the reader agency. | “The Discrimination Layer” remains a high-risk title because many readers will first hear social discrimination. The definition handles it, but the title still asks the reader to do work. “Optional deeper records” and “technical status” sound slightly like product navigation rather than an essay. | **Strong but needs a title-comprehension check.** Keep the historical name for continuity; do not rename casually. Make the route language plainer. |
| **60–90 seconds** | “Nine reports look like nine sources, but all trace to one announcement. There are nine observations, one known path, and zero paths counted as support for the broad claim. That is a hold, not a rejection; check one separately authored benchmark or failure report.” | This is the best part of the piece. The scene is specific, the numbers are visible, and the distinction between false reports and inflated corroboration is explicit. The CSS-native origin-count visual reinforces the sentence instead of decorating it. | “Origin relation” and “support path” are understandable in context but not ordinary language on first encounter. “One path is known” can be read as “one path exists” unless the reader notices the boundary. The phrase “the summary changed the structure of the evidence” is excellent but should be followed by one explicit sentence connecting the failure to an AI-generated answer. | **Release-quality argument with one small clarity improvement.** |
| **About five minutes** | “Before answering, ask where the material came from, whether it supports this exact claim, and whether it may be used / what a person should do. Keep shared, test-stipulated separate, and unresolved relations distinct. A correction must change the downstream count or route without deleting history.” | The three relation states arrive before technical codes. The compact five-field receipt is contestable rather than authoritative. The correction invariant gives the framework a testable operational standard. The repeated boundary that a receipt is not truth is necessary and effective. | “Provenance,” “disposition,” “permission,” and “relation state” are real terms but cluster quickly. “A human next step is not a fact” is memorable, though it may momentarily sound more philosophical than operational. The passage repeats “does not” several times; the caution is justified, but a reader could experience it as defensive disclaimer density. | **Very strong. This is the center of gravity.** |
| **12–15 minutes** | “This is a lightweight governance discipline, not a grand ranking algorithm: an immediate evidence loop, a slower outcome loop, a clear when-to-use/when-to-skip rule, objections, a narrow experiment, and a historical link back to v13. Prior work removes the easy novelty claim, so the remaining claim is deliberately small.” | The essay earns significance by naming how it could lose: old work under a new label, gatekeeping, rigor theater, decorative human review, and cost. The proposed comparison is narrow and the negative-result commitment is unusually honest. V13 continuity is handled as historical origin, not as proof of the new system. | This is where the prose becomes most research-plan-like. “Boundary-preserving synthesis,” “benchmark-stipulated origin-relation cue,” “conservative asserted-count risk,” “semantic review,” “count/claim/evidence coherence,” “rights-gated track,” and “primary denominator” are accurate but can sound like generated methodology language if the reader is not already invested. The essay needs one plain-language gloss for the comparison before these terms accumulate. | **Conceptually ready; editorially needs a light plain-language pass.** |
| **Explore / records and cases** | “The map decomposes the idea into families and responsibilities, then shows how it might appear in real workflows. Alpha Solver is illustrative. Signal Foundry provides a synthetic receipt: two matching claims share a supplied relation, a contradiction remains open, an expected artifact is missing, and the next step is HOLD / DEFER.” | The boundary between translation and validation is clear. Signal Foundry now contains exactly the useful distinctions: staged versus applied, transcript versus Visual Evidence, permission, human next step, and the proposed (not implemented) `CONTEXT_DISPOSITION` event. This is the best bridge from thought piece to tool-building. | The most important Signal Foundry decision is hidden inside a collapsed `<details>` block. A reader who does not expand it may never see **HOLD / DEFER**, the permission boundary, or the five-field receipt. “Two products make the responsibilities concrete” gives Alpha Solver equal visual weight even though Signal Foundry is the more operationally specific worked case. | **Good deeper route; make the case’s decision visible without requiring expansion.** |
| **Lab** | “There is a real test plan, but no model has been chosen and no study has run. F0/F1/F2 differ by what cue is supplied; 300 is provisional; invalid answers count; shortcut and parity checks remain open; real syndication is deferred and rights-gated.” | This route prevents the reader from mistaking local fixture machinery for an empirical result. It records safety and retirement conditions and explicitly allows a negative result to shrink or retire the claim. | “F0/F1/F2,” “operating characteristics,” “safety interval,” “semantic audit,” and “invalid-output differences” are appropriate for a methods page but too compressed for the main essay. The page is honest; it should not be made more impressive. | **Publishable as a clearly labelled protocol page after a readability pass.** |
| **Sources** | “The project knows what is established, what is a dataset, what is a standard, and what is still a preprint or an unresolved source. The literature narrows the novelty claim and the glossary makes the working distinctions inspectable.” | The source/status boundary supports the paper’s credibility. The selected-precedents wording no longer claims a complete literature review or one blanket authority class. | A source ledger can look like citation theater if the reader cannot tell which source changes which design choice. The page should keep the status taxonomy, but an owner-facing “why this source matters” sentence for the most important precedents would help. | **Useful and honest; maintain as evidence support, not as a second essay.** |

### What the reader should remember in one week

The likely durable memory is not “discrimination layer.” It is:

> Nine mentions are not necessarily nine supporting paths. Count the declared unit, inspect the relation, test the exact claim, keep unknown unknown, and write down the human next step.

That is the correct memory target. The framework name can remain a retrieval label, not the thing the reader must memorize. If a reader remembers only “check provenance,” the piece has underperformed, because provenance alone does not establish correctness, claim support, or permission. The current sentence that separates all four is therefore worth preserving, even if it is repeated once too often.

## Does it stand beyond a personal thought piece?

**Yes, conditionally.** It now has the ingredients of a significant design thought piece:

- a recognizable failure mode in AI-assisted evidence synthesis;
- a concrete, falsifiable unit of analysis rather than a claim that “better reasoning” is desirable;
- explicit separation of observation, relation, support, permission, and disposition;
- a correction rule that can change a downstream route;
- a stated cost boundary and explicit skip conditions;
- selected prior art that removes the broad novelty claim;
- a bounded Signal Foundry case that translates the idea into real workflow distinctions;
- a research bridge with controls, shortcut concerns, invalid-answer treatment, and a negative-result commitment;
- continuity with v13 without treating the old map as validation.

It is **not yet** a validated scientific framework, a general theory of AI reasoning, evidence that provenance discovery works, evidence that humans make better decisions with receipts, or a production architecture. The manuscript says this repeatedly and correctly. The risk is not overclaiming in the current text; the risk is that polished visual structure and the words “framework,” “research track,” and “Lab” make a casual reader infer validation that the status badges disclaim.

The strongest way to make it stand alone is not to add more concepts. It is to make the first concrete failure explicitly relevant to AI generation in one sentence, then let the small receipt and Signal Foundry case prove that the idea changes a route. The paper should remain a design proposition until the experiment or a real operator study earns a stronger claim.

## Editorial and AI-slop findings

### Voice that feels authored

These elements feel specific and worth keeping:

- “The summary changed the structure of the evidence.”
- “The reports have not become false.”
- “Unknown is where a polished summary is most tempted to put a guess.”
- “A review control must change something downstream.”
- “Perfect lineage for a false claim is still perfect lineage for a false claim.”
- “A named component earns nothing merely by being named.”
- “A negative result shrinks or retires the mechanism claim.”
- “The center moved; the caution survived.”

They contain tension, boundaries, and consequences. They do not sound like generic product copy.

### Phrases to simplify or quarantine to deeper routes

These are not wrong, but they are the places where an owner may hear “AI slop” or feel that the paper is simulating a methods vocabulary:

- “boundary-preserving synthesis”;
- “benchmark-stipulated origin-relation cue”;
- “conservative asserted-count risk”;
- “exact sample and safety intervals”;
- “matched resources”;
- “shortcut controls”;
- “semantic review”;
- “count/claim/evidence coherence”;
- “rights-gated track”;
- “primary denominator”;
- “protocol gates”;
- “cited retrieval workflow.”

Recommended treatment: keep the precise terms in Lab/Sources where they earn their place, but give the first occurrence in the 12–15 minute essay a plain-language gloss. For example: “Does the supplied relation note change whether the model counts repeated material as support, beyond simply being told the rule in words?” Then introduce the experimental label. Do not add more acronyms.

### Repetition and disclaimer density

The status language is necessary because the artifact has a polished research surface. However, “no model selected / no study run / no result / not published” appears in the header, route stops, research bridge, deeper pages, and footer. The repetition is currently acceptable for an owner-review artifact, but before publication it should be tiered:

- one prominent status in the home masthead;
- a compact route-specific status in Lab and Sources;
- one final footer status;
- fewer full-sentence disclaimers inside the essay where the same boundary has already been established.

This is a tone correction, not a request to weaken the claims. The page should sound careful because the reasoning is careful, not because it keeps announcing that it is careful.

### Title decision

Do not rename “The Discrimination Layer” solely to avoid discomfort; it is the historical and conceptual through-line. Do run a five-person comprehension check before release with the title shown alone for ten seconds. Ask: “What do you think this piece is about?” If most readers infer social discrimination, retain the title but make the subtitle or title lockup even more concrete. The current definition is necessary and likely sufficient for readers who continue, but the first glance must not send the wrong audience away.

## Visual and interaction red team

### What the current direction gets right

- The warm paper / ink / teal / violet / coral system gives the work an editorial identity rather than a generic SaaS dashboard look.
- The home page uses three small CSS-native explanatory visuals rather than a new decorative AI hero or a second conceptual map. That is the correct decision: the visual should show a count, a trace, or a test condition, not pretend to be evidence.
- The v13 raster is labelled as historical, preserved unchanged, and explicitly not the v15.2 system map. This answers the earlier concern about removing the origin diagram without letting the old topology silently become the new one.
- The compact receipt is visually structured as a record another person can contest; it is not styled as a score or a verdict.
- Native popovers have server-rendered explanatory content, an explicit close control, no-JavaScript-readable fallback, and print expansion rules. The source-level accessibility checks passed.
- The route stops and visible “stop here” boxes support skimming without making the reader scroll through the entire paper.

### P1 visual risks to verify before release

1. **Tablet route-card density.** The four masthead cards use four columns by default (`site/app/globals.css:115–116`) and do not collapse until the 780px media query (`site/app/globals.css:681–695`). At widths around 780–900px, the page may show four narrow cards with heavy wrapping and uneven heights. Verify at 720px, 820px, and 900px. If cramped, collapse to two columns earlier or make the optional deeper route a secondary link rather than a fourth equal card.

2. **Current integrated screenshots are missing.** The available image packet is from an earlier implementation and cannot certify the current v15.2 HomeEssay, the current route-card text, the current popovers, or the current Signal Foundry case. Capture fresh desktop 1440px, tablet 820px, and mobile 390px screenshots after the last integration, plus a print/PDF render.

3. **Popover runtime behavior.** Static tests protect the source pattern, but not every browser’s popover placement, trigger collision, focus return, screen-reader announcement, or print expansion. Manually open every term on desktop and mobile, tab into and out of it, close with the explicit control and Escape, and print the page with a popover open.

4. **Signal Foundry decision visibility.** The most important operational result is inside a collapsed `<details>` at `site/app/ReferenceRoutes.tsx:552–563`. The visible case card says “one synthetic receipt changes one route,” but a skim reader may never see `HOLD / DEFER`. Put a one-line status such as `RELATED · 2 observations / 1 known supporting-origin path · HOLD / DEFER` in the visible card, leaving the five-field receipt and invariants expandable.

### P2 visual/editorial risks

- The mobile reading rail contains thirteen destinations in a horizontally scrolling strip. The fade indicates overflow, but it does not tell a first-time reader that more destinations exist. Verify that the most important `Cases`, `Lab`, and `Sources` links are discoverable and keyboard-scrollable; consider a small “scroll for more” cue or a shorter primary set.
- The CSS hides the origin trace at mobile widths and retains the nodes/counts. That may be the right crop, but verify that a 390px reader still understands the relation without relying on the caption.
- “Explore holds records and cases; Lab and Sources hold technical status” is grammatically serviceable but reads like internal navigation. Prefer “Explore contains the records and cases; Lab contains the no-results protocol; Sources contains status and history.”
- The current `ReferenceRoutes.tsx` still contains an older `isHome` rendering branch while `page.tsx` sends the home route to `HomeEssay`. It is not a current-user-facing defect, but it is a drift trap: future edits can silently update one home implementation and not the other. Remove/quarantine the dead branch or add an explicit parity test before the next version.
- Alpha Solver and Signal Foundry currently receive equal card weight. That is defensible as a cross-case comparison, but Signal Foundry is the only case with a precise receipt, relation state, transcript/Visual Evidence boundary, and human next step. Its operational status should be visually primary or the heading should explain why both cases are needed.
- The v13 image is intentionally tall and dense. Keep it as a historical reference, but make the caption and adjacent plain-language description carry the meaning at small sizes. The image should never be required to understand v15.2.

## Correction priorities

### P0 — release blockers

**None identified in the current source review.** The current manuscript and home page disclose that this is fictional/conceptual, that no model or study has been selected/run, and that no empirical result or publication claim is being made. The narrow research proposal is explicitly bounded. No unsupported production-validation claim appears in the integrated Signal Foundry card.

That conclusion is conditional on the fresh browser/print pass: a rendered status omission or a broken route would become a P0 communication failure even though the source contains the text.

### P1 — fix before external release

1. **Expose the Signal Foundry route decision in the collapsed-card summary.** Show the relationship and `HOLD / DEFER` without requiring `<details>` expansion; retain the full five-field receipt inside.
2. **Run a current visual/interaction QA pass.** Verify 390px, 720px, 820px, 900px, and 1440px; desktop and mobile term popovers; keyboard flow; reduced motion; and print/PDF. Record screenshots from the integrated v15.2 build, not the old packet.
3. **Resolve tablet route-card density.** Collapse the four reading choices earlier or rebalance the optional deeper route if the current render is cramped.
4. **Add one plain-language bridge in the full essay’s research section.** Explain the question as “does a supplied note stop the model from counting repeated material as independent support, beyond being told the rule in words?” before introducing cue/condition terminology.
5. **Add one explicit AI consequence to the first stop.** For example: “Unless that relation survives into the prompt or evidence record, a model can inherit the inflated plurality when it writes the answer.” This ties the concrete scene to the title without adding a new concept.

### P2 — improve before or during the next revision

1. Run the title-comprehension check and decide whether the subtitle/lockup needs a little more concrete language; do not change the historical name based on intuition alone.
2. Replace the route-card internal wording (“technical status”) with plain navigation labels.
3. Add a small mobile navigation affordance or shorten the primary rail.
4. Remove/quarantine the unused legacy home branch in `ReferenceRoutes.tsx`, or test that the two home renderers cannot drift.
5. Give the key sources a one-line “why it matters here” annotation while preserving source-status distinctions.
6. Reduce repeated full disclaimers once the final status hierarchy is established; keep every substantive boundary, but vary the presentation.
7. Add a reader test that asks a non-technical person to restate the five fields and the difference between “unknown” and “separate.”

## Recommended execution sequence

1. **Freeze the conceptual contract.** Keep the current central claim, three relation states, five-field receipt, correction invariant, use/skip boundary, negative-result commitment, and v13 historical treatment. Do not add a new family, score, model, or generated hero/map.
2. **Make the smallest editorial patch.** Add the AI consequence sentence, plain-language research bridge, and visible Signal Foundry status. Clarify the deeper-route card wording.
3. **Perform current visual QA.** Render the integrated site at the five widths, inspect the reading rail, route cards, microvisuals, v13 image, case cards, popovers, and print output. Fix only observed layout/interaction defects.
4. **Perform the owner cold read.** Read title-only, first stop, five-minute stop, full essay, then Signal Foundry case. Stop at each route and write the one-sentence paraphrase without looking back. If the paraphrase loses the distinction between observation, path, support, or permission, revise the relevant sentence—not the entire architecture.
5. **Run a small external comprehension check.** One non-technical reader and one evidence/workflow-oriented reader should answer: what changed, what does the receipt prove, what does it not prove, and what happens next? Treat confusion as editorial evidence.
6. **Lock the release boundary.** Release as a thought piece / design proposal with a clearly labelled research track. Do not call it validated, empirical, production-ready, or a general theory. Keep the experiment and any real-syndication arm separate until rights, annotation, and study gates are explicit.
7. **Only then expand research.** The next research work should test the small claim, not broaden the map. If the supplied cue does not change the frozen model’s counting behavior beyond the rule-only baseline, accept the negative result and retire or narrow the mechanism claim.

## Final release call

**Current state:** owner-review candidate; conceptually integrated; source tests passing; visual runtime evidence incomplete.

**Recommended call:** `HOLD FOR ONE CONVERGENCE PASS`, then release the thought piece if the P1 checks pass. The work does not need another overnight expansion, another generated diagram, or a broader framework layer right now. It needs the integrated artifact looked at by a human, the most important case decision surfaced, and the research language made just plain enough that the reader never mistakes a planned test for a result.

The design has reached the point where restraint is part of quality. Preserve the v13 image as history, keep the three microvisuals because they explain actual relationships, and let the receipt—not a more spectacular map—carry the novel operational promise.
