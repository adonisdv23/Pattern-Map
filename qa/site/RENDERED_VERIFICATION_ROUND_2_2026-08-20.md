# Round-two rendered verification and evidence-integrity audit

Status: **CORRECTIONS APPLIED — RENDERED MEASUREMENT COMPLETE — NAMED MANUAL AND OWNER GATES STILL OPEN**

Date: 2026-08-20

Reviewed predecessor: `cc5547d` (the exact state the independent ChatGPT Pro
round-one review inspected).

Corrected checkpoint: see the checkpoint register in
[`handoff/BRANCH_AND_PR_STATE.md`](../../handoff/BRANCH_AND_PR_STATE.md).

## What this pass was for

The round-one correction responded to the independent review by changing source
and then asserting the result. This pass did the opposite: it treated every
claim in that response as a hypothesis and went looking for the rendered
evidence. Two things followed from that. Several claims turned out to be true
and are now measured rather than asserted. Several turned out to be false, and
those are the substance of this report.

The distinction matters more here than in most projects. The publication argues
that a plan is not an event, that a recommendation is not a decision, and that
repetition is not corroboration. A QA record that asserts a responsive result
from a CSS reading is making exactly the error the work is about.

## Findings

### F-1 · The owner-review package was anchored to two commits that never existed

**Severity: blocks handoff.** The round-one package named
`5eb860e8d6918813622a7725eb0d854f6bef6ca2` as the "corrected implementation
checkpoint" and `bfaa62e7c186b2838e7b57c1490a1428338e862c` as the "corrected
owner-review evidence checkpoint," and described the branch carrying them as
pushed.

Neither object resolves:

```text
git cat-file -t 5eb860e8d6918813622a7725eb0d854f6bef6ca2
  fatal: git cat-file: could not get object info
git cat-file -t bfaa62e7c186b2838e7b57c1490a1428338e862c
  fatal: git cat-file: could not get object info
git rev-parse HEAD                                    → cc5547d…
git rev-parse origin/codex/pattern-map-v16-foundation → cc5547d…
```

The reflog contains no trace of either commit. The implementation work those
hashes described was real, and it was sitting uncommitted in the working tree;
what did not exist was the act of committing it. Fifteen files had already
inherited the invented hashes, including the manifest, the verification script's
`CONTENT_CHECKPOINT` constant, the acceptance matrix, the roadmap, the decision
log, and the QA report's own filename.

**Correction.** Every checkpoint hash now lives in one register in
`handoff/BRANCH_AND_PR_STATE.md`; every other document points at that register.
`verify_owner_review_package.py` reads the value from the register instead of
carrying its own copy, so an unstamped checkpoint reads `PENDING` rather than
resolving to something plausible. Every hash in the branch table was verified
with `git cat-file -t`. Recorded as **D-025**.

### F-2 · A deleted map node was styling the entire Map page

**Severity: visible regression, introduced by the round-one correction.** The
correction removed the absolutely positioned map nodes but kept their rules.
One orphan still matched:

```css
.map-route { border: 2px solid var(--navy); background: #e7f1f0; }
```

`map-route` was the class of a small removed node. It is also the class on the
whole Map route `<section>`. Measured in the browser, that section is
824 × 8702 px, and it was carrying a navy border and a pale blue-green panel
around the entire page — against a publication whose owner intent specifies a
warm paper ground.

Source review could not catch this: both rules read as correct in isolation.
The round-one QA report states the corrected site was visually inspected in a
live browser; this styling covers the full height of the route it names.

**Correction.** The orphaned rule is removed, along with the rest of the
superseded geometry. `qa/site/css-selector-use.spec.mjs` now fails when any
class selector cannot reach any generated page, and fails specifically when a
route-section class is given a node-level border or background.

### F-3 · 51 unreachable class selectors survived the correction

**Severity: latent.** Beyond `.map-route`, the stylesheet carried about 10 KB of
rules for markup that no longer exists — the old receipt card, an earlier
topology, removed microvisuals — and, in the `max-width: 1100px` block, the
coordinate system whose breakpoint collision was the original P0:

```css
.map-family-grid { grid-template-columns: repeat(3, …); top: 10rem; }
.map-canvas { min-height: 62rem; }
.map-record-row { top: 35rem; … }
```

Those declarations were inert only because a later block reset `position` to
`static`. The mechanism that let two breakpoints disagree about where a row sits
was still in the file, one `position: absolute` away from returning.

**Correction.** The dead rules are removed. Removal was verified as behaviourally
empty by capturing every computed value of 22 layout-relevant properties for
every element on the two most complex routes, swapping the stylesheet, and
diffing: **0 differences across 776 elements on `/map/` and 1,826 elements on
`/apply/`.** `map-layout-contract.spec.mjs` now asserts the absence of the
mechanism — no `position: absolute` and no fixed coordinates on any map
element — rather than the absence of one bad rule.

### F-4 · The 44 × 44 touch-target claim was not true of the orientation rail

**Severity: accessibility, claimed complete.** Disposition PRO-R1-10 recorded
"discrete controls have 44px minimum." Measured, the ten desktop orientation
rail links were **159 × 25.76 px**. The rail is hidden below 821 px, so the
mobile checks never saw it, and the widths where it does show include tablet
sizes where touch is plausible.

**Correction.** `.orientation-link` now carries `min-height: 2.75rem`. Because
ten links at 44 px exceed a short viewport, the rail also gained
`max-height: calc(100vh - 2rem)` and `overflow-y: auto`, which additionally
fixes a latent problem: at its previous 640 px height it already overflowed
windows shorter than about 700 px with no way to reach the lower entries.
Measured across all twelve viewports and ten routes: **0 discrete controls
below the target.**

### F-5 · The Apply route's own controls had no designed focus indicator

**Severity: accessibility.** The focus rule covered `button`, `a`, and
`summary`. The Apply route's four fieldsets are radio inputs — the primary
interactive controls of the route the P0 was about — and fell back to the
browser default ring, not the project's 3 px indicator with its 6 px halo. The
existing dual-focus contrast check passes because it measures the custom
indicator, which these controls never received.

**Correction.** The rule now includes `input`, `select`, and `textarea`, with a
tighter offset for radios and checkboxes so the halo sits beside the control
rather than over its label, and the forced-colors override was extended to
match.

### F-6 · Visual evidence files claimed a format their bytes contradicted

**Severity: evidence integrity.** The round-one review raised this as P2; it was
not addressed. 49 files under `qa/visual/` were named `.png` while their bytes
began `FF D8 FF` — JPEG.

**Correction.** All 49 renamed with `git mv`, preserving bytes and history, and
every reference updated. `qa/visual/verify_image_formats.py` now fails when any
current evidence file's extension disagrees with its magic bytes, and runs
inside `qa/run_owner_review_checks.sh`. Forty further mismatches exist under
`archive/` and `research/**/preserved/`; renaming those would violate the
accession rules, so the checker reports them as a preserved condition and says
so out loud rather than silently excluding them.

### F-7 · The touch-target fix was pushing open the reading line

**Severity: typography, introduced by the round-one correction.** The optional
term helper is a small pill that appears inside running prose. Round one gave it
`min-width: 2.75rem; min-height: 2.75rem` to meet the 44-pixel target. Measured,
that turned a 23-pixel line box into a 44-pixel one every time a term appeared —
a relationship-band heading measured 67 px for what should be two 23-pixel
lines.

The independent review had asked for exactly the opposite: increase hit areas
"without enlarging inline text links indiscriminately."

**Correction.** The painted control is small again (53 × 20 px) and the target
is expanded by an absolutely positioned `::after` overlay of 44 px, which costs
the reading line nothing. The same heading now measures 47 px. Because the
target is no longer the painted box, `layout-probe.js` was taught to measure the
union of the painted box and any such overlay, and to record which of the two it
used — so the number in the evidence still describes what a finger can land on.

### F-8 · Family context did not survive a route crossing

**Severity: accepted round-one item, deferred as optional.** The independent
review asked that opening a family from one route land the reader in that
family's state on the next, and that examples offer a way back. Family links
carried a fragment only, so a reader arriving from Home landed on an unfocused
Map.

**Correction.** Family links now carry `?family=F3` alongside the fragment. On
load the Map restores that focus without moving the caret; a fragment the reader
just followed outranks a query carried in from the previous route; focus changes
sync the URL through `replaceState` so a focused view is shareable. Each example
states which families it teaches and links back to each of them, in static
markup that does not depend on scripting. Scripting adds only an arrival note.

## Rendered evidence

Ten routes × twelve viewports × two probes = **240 measured records, 0
failures**: [`qa/interaction/evidence/`](../interaction/evidence/), summarised
in [`RENDERED_SWEEP_SUMMARY.md`](../interaction/evidence/RENDERED_SWEEP_SUMMARY.md),
which is generated from the evidence file rather than written by hand.

Viewports: 1440×900, 1280×720, 1101×900, 1100×900, 1024×768, 900×900, 821×844,
820×844, 768×1024, 600×900, 390×844, 320×800. The 1101/1100 pair is the exact
boundary the independent review identified. Measured, the six-column row becomes
a two-row three-column grid across that boundary, with no stacking fault and no
overlap at either width.

Instruments, all readable and re-runnable:

| Instrument | What it measures |
| --- | --- |
| `qa/interaction/layout-probe.js` | Bounding boxes, pairwise overlap, page overflow, map band stacking, touch-target sizes, term-help state |
| `qa/interaction/enhancement-probe.js` | Focus order and indicators, term-help keyboard contract, no-script rendering, print cascade, colour-independent family identity |
| `qa/interaction/layout-sweep-driver.js` | Walks a route queue at a fixed viewport so one sweep is internally consistent |
| `qa/interaction/summarize_sweep.py` | Regenerates the summary from the evidence, with `--check` |

### Apply, exercised rather than described

Driven live at 1440×900
([`apply-planning-states-2026-08-20.json`](../interaction/evidence/apply-planning-states-2026-08-20.json)):

| Input | Recommended action | Observed state after |
| --- | --- | --- |
| reversible · low · quick · **restricted** | `CLARIFY` | unchanged |
| consequential · high · substantial · **human-gate** | `HOLD` | unchanged |
| consequential · high · substantial · supplied | `COMPARE` | unchanged |
| click "Simulate human HOLD" | `SIMULATED_HOLD`, labelled | unchanged |
| click "Reset simulation" | `NOT_SIMULATED` | unchanged |

"Unchanged" means all five observed fields stayed `NOT_RUN`, `NOT_TRIGGERED`,
`NOT_OBSERVED`, `NOT_AVAILABLE`, `NOT_RECORDED`. Permission dominates
regardless of consequence, uncertainty, or budget. The page carries exactly one
live region, a 66-character `role="status"` sentence — not the whole card.

## Method boundaries, stated as boundaries

Two probe results were false positives before they were true ones, and saying so
is part of the record:

- Chromium returns a stale bounding box for content inside a closed
  `<details>`, so the first probe reported a collapsed disclosure as visible
  overflow. Fixed with `checkVisibility()` plus a closed-ancestor walk.
- A wide table inside `overflow-x: auto` is correct responsive behaviour, not
  page overflow. The probe now ignores any element with a scrolling or clipping
  ancestor.

Both were found by investigating a flagged result instead of accepting it. A
third boundary is built into the probe rather than left to prose: focus is moved
programmatically, which does not engage `:focus-visible` in Chromium, so where
the pseudo-class does not fire the check asks whether a `:focus-visible` rule in
the page's own stylesheets actually selects that element. The report says which
of the two paths produced each result.

The print result is the stylesheet's own `@media print` rules applied in screen
context. It is not a print preview and the record labels it that way.

## Still open

Unchanged from round one, and not narrowed by this pass:

- physical keyboard traversal on real hardware;
- a supported screen-reader pass;
- the browser's own zoom control at 200% — reflow is measured at 640 and 320 CSS
  pixels, the widths that 200% and 400% zoom produce from a 1280 px viewport,
  which is the WCAG reflow condition but not the zoom control itself;
- browser print preview and a printed page;
- physical Windows forced-colors rendering;
- touch hardware;
- owner and mentor judgment of voice, comprehension, pacing, and taste.

Nothing in this pass is reader-comprehension evidence or effectiveness evidence.
Rendered measurement shows that the interface behaves as described. It cannot
show that the description is worth reading.

No merge, deployment, publication, Release, empirical or model study,
participant activity, provider selection or call, spend, dataset acquisition,
preregistration, or outreach occurred.
