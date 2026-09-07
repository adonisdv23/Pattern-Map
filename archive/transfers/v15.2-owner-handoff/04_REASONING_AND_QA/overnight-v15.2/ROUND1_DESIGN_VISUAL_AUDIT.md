# Round 1 design / accessibility / explanatory-visual audit

## Pattern Map v15.1 → v15.2

**Lane:** design system, interaction accessibility, explanatory visuals, and
image provenance  
**Status:** provisional lane audit and prototype handoff  
**Date:** 2026-08-19  
**Scope:** read-only review of the v15.1 source/site/glossary and supplied
screenshots; new files are limited to this report and
`experiments/v15_2_concept_visuals/`  
**Verification boundary:** no browser QA, screen-reader run, deployment,
publication, push, commit, package-lock change, external image generation, or
live study/provider call was performed.

## Executive verdict

The v15.1 visual voice is already distinctive and credible: warm paper, ink,
serif reading type, compact mono labels, thin rules, and restrained teal / coral
/ violet accents make the reader feel like an edited field note rather than a
dashboard. The text-led opening and the live receipt are the right foundation.
The smallest useful v15.2 visual pass is therefore three deterministic CSS
microvisuals in the existing technical explanations, with a fourth reserved for
the Lab. A larger illustration gallery would dilute the argument and increase
the risk that a decorative topology is mistaken for a system claim.

**Recommendation:** keep the existing receipt and its text equivalence; adapt
prototypes 01–03 into the highest-value term explanations; keep prototype 04
behind the Lab route only. Do not add a new hero image, framework-map bitmap,
or generated visual to the term popovers.

The current `Term` component is a sound small disclosure affordance, but it is
not yet a complete accessible dialog/popover pattern. Its strongest properties
are plain-language definition + example + boundary, keyboard-triggerable
buttons, Escape/Close return to the trigger, a mobile fixed panel, and reduced-
motion CSS. Its material gaps are focus not moving into the inserted dialog,
no `aria-describedby` relationship for the definition, no collision strategy on
desktop, a no-JavaScript path that leaves a technical button inert, and no
clear decision whether the panel is a non-modal disclosure or a modal dialog.
These should be repaired or explicitly constrained before integration.

## Truth and genre boundary

The v15.2 charter says the framework and study remain proposed, the receipt is
fictional, `UNKNOWN` stays unresolved, `N=300` is a provisional design input,
and null / negative / harmful / unstable results remain reportable. Every
visual below repeats those boundaries in text. None of the prototypes is a
result, a provenance discovery, a claim-support score, or a live runtime.

The visual job is comprehension, not proof:

- show the unit being counted;
- isolate the one intentional difference in the planned conditions;
- keep provenance, claim support, and human disposition separate; and
- make a planned sample and unfavorable result commitment concrete without
  implying that a test ran.

## Evidence inspected

### Charter and editorial direction

- `reports/overnight/v15_2/PROGRAM_CHARTER.md`: reader outcome, visual
  acceptance criteria, semantic HTML/CSS preference, popup contract, image
  roles, and no-results boundary.
- `reports/overnight/v15_2/ROUND1_EDITORIAL_OWNER_PROXY_AUDIT.md`: the strongest
  current receipt delta, the three-question simplification, the term-risk
  table, and the warning against taxonomy fatigue / AI-slop cadence.
- `source/READER_OUTCOME_AND_READING_PATH_V15_1.md`: plain-language-first rule,
  interaction contract, and the distinction between a visual that deepens
  comprehension and one that rescues opaque prose.
- `source/THOUGHT_PIECE_V15.md`: fictional nine-report receipt, relation states,
  provenance / claim-support boundary, F0/F1/F2, `N=300`, and locked
  negative-result commitment.

### Site and glossary implementation

- `site/app/page.tsx`: masthead, route cards, receipt, count snapshot,
  `UNKNOWN` rule, relation key, human disposition, Lab condition table, sample
  size, negative-result commitment, source glossary, and existing image
  captions.
- `site/app/content.ts`: compact glossary plus technical glossary. The current
  technical entries already define F0/F1/F2, T1, `N=300`, provenance audit,
  system runtime, human disposition, locked negative-result commitment, and
  relation codes.
- `site/app/Term.tsx:15–18, 40–74`: current intent and behavior. It uses a
  button trigger, conditional `role="dialog"`, an explicit close button,
  Escape-to-close with focus return, and optional sample-size / flow visuals.
- `site/app/globals.css:26–30, 483–528, 607–625`: focus treatment, Term
  placement, mobile fixed-panel rule, reduced-motion rule, and print rules.
- `reports/VISUAL_READER_QA_REPORT.md`, `reports/V15_VISUAL_AND_ACCESSIBILITY_QA.md`,
  and `reports/V15_LOOP3_READER_DESIGN_ACCESSIBILITY_REVIEW.md`: existing
  static/responsive QA claims and disclosed manual-release limitations.

### Screenshots and image assets

Inspected visually:

- `reports/qa/site-final-20260818/responsive-desktop-1440x900-emulated.png`
- `reports/qa/site-final-20260818/responsive-tablet-720x900-emulated.png`
- `reports/qa/site-final-20260818/responsive-mobile-390x844-emulated.png`
- `reports/qa/site-final-20260818/site-receipt-current-desktop.png`
- `reports/qa/site-final-20260818/responsive-mobile-receipt-390x844-emulated.png`
- `reports/qa/site-final-20260818/responsive-mobile-ledger-390x844-emulated.png`
- `reviews/claude_desktop/packet/site-desktop-1440x900-component-c06.png`
- `reviews/claude_desktop/packet/site-mobile-390x844-component-c06.png`
- `site/public/images/nine-mentions-one-origin.jpg`
- `site/public/images/v13-six-families-origin-map.png`
- `site/public/og.png`
- `archive/v13/pattern-recognition-diagram-v12.png`

The supplied QA screenshots visibly carry `V14`, “PERSONAL SYSTEMS MEMO · V14
· PROVISIONAL,” and the older numbered navigation (`01 OVERVIEW`, `02
FAMILIES`, `03 MECHANISMS`, etc.). They therefore conflict with the current
v15.1 source, whose masthead and routes are `v15.1`, Essay / Receipt / Explore /
Lab / Sources, and whose receipt is present in the source. The existing review
material also labels the Claude packet as historical pre-receipt input. Treat
these PNGs as historical visual evidence, not current v15.1 release proof,
until they are regenerated from the exact approved source. This is an image
provenance / QA-bookkeeping issue; it is not evidence that the current
server-rendered source has the old structure.

## Current design audit

### Editorial hierarchy and visual voice

**Keep.** The masthead has a strong editorial order: status → title → plain
definition → concrete failure → proposition → reading route. The receipt then
turns the idea into a visible decision rather than a decorative diagram. Warm
paper and black ink support long reading; mono labels make status and record
IDs feel inspectable; teal is a useful through-line for explanation, while
coral and violet are reserved for risk / uncertainty / research boundaries.

**Change.** The opening still puts “The Discrimination Layer” in the largest
visual treatment before the reader has seen the ordinary-language problem. The
subtitle and explicit technical definition mitigate this, but the title test
remains open. A v15.2 visual pass should never repeat the technical noun inside
every popover heading. Use “where it came from,” “three versions of one task,”
and “what happens when the relation is unresolved” as visible headings; keep
the stable term in the label or glossary metadata.

**Change.** The main route already contains enough visual density in the
receipt: frame, claim block, count snapshot, nine-row table, relation key,
contrast roots, disposition, and footer. A new visual should replace a short
explanation or sit inside a popover—not be added as another full-width card
after the same point. The existing worked-example raster should remain an
illustration of the post-receipt application, not a second receipt.

### Typography, density, and mobile behavior

**Keep.** The source and current CSS use a legible Georgia-style serif for long
prose and headings, with Arial / mono roles for interface metadata. This is
more authored and less product-dashboard-like than a fully sans stack. The
compact labels work when paired with a sentence-sized explanation.

**Change.** The screenshots that can be inspected are stale v14 captures, so
they cannot establish current v15.1 line lengths, first-fold density, or
popover placement. The source CSS is responsive and the existing QA reports
describe contained table scrolling, but the Term-specific desktop collision
case is not covered. A trigger near the viewport edge can center a 360px panel
past the viewport because the desktop panel is absolutely positioned at
`left: 50%` with no collision correction. The mobile fixed panel is safer, but
its 70vh max height can cover the reading context; the panel needs an obvious
heading, close control, and readable scroll affordance.

**Keep.** The prototypes use one column at narrow widths, short blocks, and
text equivalents. They do not shrink labels into unreadable code or require
horizontal page scrolling. If the live receipt retains a wide table, keep the
existing explicit contained-scroll region and mobile summary rather than
turning the table into a CSS-only visual.

### AI-slop and visual-language risk

The current visual language is most convincing when it shows a concrete object
and a consequence: `09 / 01 / 00`, `UNKNOWN stays unknown`, and `HOLD · VERIFY
ANOTHER ORIGIN RELATION`. It becomes less convincing when many equally weighted
cards, connector arrows, or repeated “not a result” labels stand in for a new
decision.

**Delete / defer:** generic pipeline arrows, funnels, apertures, gates,
checkmarks, “truth” icons, decorative constellations, and a new framework map.
The retained image ledger already rejected H1 because its one-way aperture can
imply a gatekeeper the framework does not claim. The historical v13 map has a
different topology and must not be redrawn as current CSS.

**Keep:** small CSS relationships with a sentence before and after them. The
four prototypes intentionally use report tiles, condition cards, a trace,
state cards, a bounded sample grid, and predeclared outcome rails. Each has one
named conceptual job and an explicit boundary.

## `Term` / glossary accessibility audit

### What is working

1. The trigger is a real `<button>` with `aria-expanded` and `aria-controls`
   (`site/app/Term.tsx:40–47`), so it is keyboard reachable and not a hover-only
   affordance.
2. The panel contains a visible heading, definition, example, and
   “What it does not mean” boundary (`site/app/Term.tsx:52–61`), matching the
   charter's progressive-disclosure contract.
3. Escape and the explicit close button return focus to the trigger
   (`site/app/Term.tsx:26–36, 55–56`). The global two-tone focus treatment is
   designed to remain visible across light and dark panels
   (`site/app/globals.css:26–30`), and the existing QA report records the
   earlier low-contrast ring as repaired.
4. The panel changes to a viewport-fixed, scrollable bottom sheet at narrow
   widths (`site/app/globals.css:607–625`), which is a better touch target than
   trying to keep a tiny anchored panel inside a 390px text column.
5. The sample-size and evidence-to-human-action visuals are opt-in, and the
   surrounding glossary cards repeat their definitions as live text. This is
   the right direction: a visual can deepen a sentence but cannot be the only
   way to recover it.
6. Reduced motion is already addressed globally (`prefers-reduced-motion` in
   `site/app/globals.css`): smooth scrolling is disabled and transitions are
   suppressed. The prototypes add no motion at all.

### Material changes before integration

1. **Clarify the interaction role.** The inserted element is `role="dialog"`
   (`site/app/Term.tsx:52`) but is not modal: focus stays on the trigger, the
   page is not inert, and there is no focus trap. Either implement a genuine
   dialog pattern (move focus to the panel heading or close button, provide
   `aria-modal`, contain focus, and restore focus) or use a non-modal disclosure
   / popover role whose interaction contract allows focus to remain in the
   reading flow. Do not leave a dialog role with an ambiguous expectation.
2. **Associate the content.** Add an `aria-describedby` relationship to the
   definition/example/boundary region, or use a single description element.
   `aria-labelledby` names the dialog, but the current panel does not promise
   that its substantive text is announced as the explanation opens.
3. **Make the trigger self-describing.** Add `aria-haspopup="dialog"` if the
   dialog pattern is retained, and keep the visible label plain. “Explain X”
   is useful; ensure the accessible name does not become duplicated by a
   nested heading or visual-only label.
4. **Plan for no JavaScript.** The comment says prose remains readable without
   JavaScript, but a `Term` trigger rendered as a button is inert when JS is
   unavailable (`site/app/Term.tsx:38–51`). The technical glossary cards do
   repeat definitions, which saves the route, but inline first-use terms in the
   receipt should have a visible sentence that does not require activation.
   If a term is essential, use a native `<details>` fallback or a static
   adjacent definition.
5. **Prevent viewport collisions.** The desktop panel is centered from the
   inline trigger (`site/app/globals.css:496–502`) with no left/right boundary
   calculation. Add collision-safe placement or constrain the panel inside a
   wrapper with `max-inline-size` and edge-aware alignment. Test first-use
   terms near both sides of the receipt and at 200% reflow.
6. **Keep print complete.** Closed client panels are absent from print, so the
   surrounding sentence/glossary must carry the definition. Do not make the
   visual the only copy of `N=300`, `UNKNOWN`, or negative-result meaning. The
   prototypes' print rules preserve text and remove connector decoration.
7. **Avoid repeated triggers.** The page currently exposes some terms at the
   first receipt and repeats related definitions in the technical glossary. Use
   a popover at the highest-value first occurrence, then a normal glossary
   entry. Reopening the same concept at every route adds interaction cost and
   weakens hierarchy.
8. **Audit color as a supplement.** Teal, violet, coral, ochre, and blue are
   useful accents, but state names and labels must remain explicit. The current
   site generally does this; any integrated prototype must preserve the same
property in grayscale, forced colors, and images-disabled mode.

## Image and screenshot provenance disposition

| Asset | Classification | Decision | Reason / boundary |
| --- | --- | --- | --- |
| `archive/v13/pattern-recognition-diagram-v12.png` and byte-identical site copy | Historical anchor | **Keep unchanged** | Historical context only; not current topology or evidence. Preserve supplied hash and caption/transcript. |
| `site/public/images/nine-mentions-one-origin.jpg` (E2 derivative) | Explanatory figure | **Keep, adapt caption if needed** | Generated through the recorded OpenAI image-generation route; exact model not exposed. It makes shared-origin imagery visible but cannot carry counts, status, or claim support by itself. |
| `site/public/og.png` (S1 derivative) | Share-preview atmosphere | **Keep out of reading path** | Accurate share art, not a diagram or evidence. Do not reuse as a popover visual. |
| `assets/imagegen/archive/context-before-answer.jpg` (H1) | Rejected / archived concept | **Delete from integration shortlist; retain as audit evidence** | Aperture and one-way flow imply a mandatory gatekeeper / pipeline. The image ledger explicitly archives it. |
| `reports/qa/site-final-20260818/*.png` | QA screenshot evidence | **Do not ship as site imagery** | Supplied images visibly say V14 / old navigation and conflict with current v15.1 source. Regenerate before using as release proof. |
| `reviews/claude_desktop/packet/*.png` | Historical review packet | **Keep as historical review evidence** | The QA report identifies this packet as pre-receipt / historical. It is useful for regression context, not current visual sign-off. |
| `experiments/v15_2_concept_visuals/*.html` | CSS/semantic prototypes | **Use for integration shortlist** | No external assets, no model-authored SVG, no bitmap provenance issue, and live text carries every relationship. |

No bitmap generation was essential for this lane. The concepts are categorical
relationships, counts, and predeclared states; CSS/semantic HTML is more
auditable, printable, resizable, and screen-reader-compatible than another
illustrated topology.

## Prototype disposition and ranked integration shortlist

### 1. `01-origin-vs-report-count.html` — keep, adapt first

**Conceptual job:** answer “are nine observations nine origins?” in one glance.
Nine labelled report records sit in an ordered list, a single `Origin A` node
names the known shared path, and B1/C1 are explicitly marked comparison roots
whose support is unassessed. The count strip repeats `09 / 01 / 00` in live
text.

**Why it earns space:** it makes the most important unit distinction visible
without implying that the reports are false or that a provenance trace proves
the claim. It is materially clearer than the current sample-size dot visual for
the central reader outcome.

**Integration:** use at the first `origin relation` / “where material came
from” explanation or as a compact receipt companion. On the home route, keep
the full receipt text and use only a compressed version if space is limited.

**Change before integration:** reduce the nine tiles to a 3×3 cluster at
desktop and a 2×5/one-column fallback only if the actual popover width cannot
hold the labels; keep `O01–O09` in accessible text. Verify the connector does
not look causal or directional. Keep “claim support unassessed” adjacent to
`00`.

### 2. `02-f0-f1-f2.html` — keep, adapt in Lab

**Conceptual job:** answer “what changed between F0, F1, and F2?” without
making the reader memorize codes.

**Why it earns space:** the cards repeat “same evidence” and highlight only
the intentional difference. F2 is not visually rewarded as a winner; its
purpose is framed as a question against F1. The boundary explicitly blocks the
product-version / performance-grade misread.

**Integration:** replace or sit above the current Lab condition table inside
the F0/F1/F2 explanation. It belongs on `/lab`, not the first five-minute
essay route.

**Change before integration:** preserve the target site's exact parity wording
and ensure that the code labels remain secondary to the plain names. Do not
add effect sizes, “better” arrows, or success coloring before any run.

### 3. `03-provenance-unknown-hold.html` — keep, adapt at receipt

**Conceptual job:** answer “does provenance prove the claim, and what do we do
when relation is unresolved?”

**Why it earns space:** it separates the trace (Origin A → O01–O09 → bounded
packet), relation state (`DEPENDENT` / `INDEPENDENT-AS-STIPULATED` / `UNKNOWN`),
claim state (`INSUFFICIENT`), and human action (`HOLD`). This directly addresses
the owner-proxy finding that `00` can otherwise look like evidence discard.

**Integration:** use in the provenance-audit / recorded-decision explanation
or as a shortened receipt visual. It should not duplicate the entire nine-row
ledger.

**Change before integration:** make the line from origin to reports visually
non-causal (a trace / derivation label, not a confidence arrow). Retain the
plain statement that a source can be perfectly traced and still fail to
support the claim.

### 4. `04-sample-size-negative-result.html` — keep only in Lab

**Conceptual job:** answer “is `N=300` a result, and what if the test
disappoints?”

**Why it may earn space:** the four groups of 75 make the planned denominator
concrete, while the four interpretation rails keep null, rule-only, harmful,
and shortcut / unstable outcomes visible.

**Why it is last:** it is the densest visual and it combines two concepts that
can compete for attention. A sentence may be better in the first Lab fold; the
visual is useful only after the reader has accepted that the study is unrun.

**Integration:** technical glossary / Lab only. If the final popover is too
small, keep the result rails and remove the dots, or use a plain “300 planned
bundles” sentence plus a compact four-item list.

**Change before integration:** keep “four planned structures · 75 each” only
if the protocol still uses those four equal groups. Do not let decorative dots
look like observed participants, model calls, or favorable outcomes.

## Explicit keep / change / delete ledger

| Decision | Material | Action | Acceptance condition |
| --- | --- | --- | --- |
| **Keep** | Nine-report / one-origin receipt, `09 / 01 / 00`, `UNKNOWN`, `HOLD` | Protect as the primary explanatory object | A cold reader can state why repeated reports remain useful but do not become independent support. |
| **Keep** | Text-led opening, serif / mono hierarchy, warm paper / ink system | Preserve visual voice | No added visual delays the concrete failure or changes the genre into a dashboard. |
| **Keep** | E2 worked-example raster with alt/caption boundary | Retain as one explanatory figure after the receipt | It remains labelled illustration-only and is never required to recover the counts or status. |
| **Keep** | Historical v13 map unchanged | Retain as historical anchor + live transcript | It is never presented as the v15.2 topology or empirical evidence. |
| **Change** | `Term` interaction semantics | Decide non-modal disclosure versus true dialog; add description association and collision-safe placement | Keyboard, screen-reader, mobile, print, and no-JS checks pass on exact approved source. |
| **Change** | First-use technical term phrasing | Put plain definition before short code; show one visual only where it changes comprehension | A reader can answer the sentence without opening the popup. |
| **Change** | Screenshot QA bookkeeping | Regenerate screenshots from v15.1/v15.2 source before release claims | No image labelled current visibly says V14 or carries an older route map. |
| **Delete / defer** | H1 aperture / gatekeeper hero concept | Keep only in design-process archive | No one-way filtering or truth-gate semantics are introduced. |
| **Delete / defer** | New framework-map bitmap / generic pipeline visual | Do not integrate | Deterministic map and text already exist; no decorative topology competes with them. |
| **Delete / defer** | Sample-size visual in the first-minute route | Reserve for Lab or sentence-only fallback | First fold remains problem / thesis / status / receipt focused. |

## Acceptance tests for v15.2 integration

These are proposed acceptance tests for the parent integrator. They are not
claimed as run by this lane.

### Semantic and content tests

1. Each integrated visual has a real heading, a `figure`/`figcaption` or
   labelled section, and a prose sentence that states the relationship before
   the CSS arrangement.
2. Removing color, borders, arrows, dots, and generated images leaves enough
   text to recover the count, state, and action. No critical relationship is
   hidden in `aria-label` on an element that suppresses its visible children.
3. The origin visual keeps `09 observations`, `01 known common-origin cluster`,
   and `00 supporting origins counted` distinct; it does not imply that `00`
   means “the origin does not exist.”
4. The F0/F1/F2 visual states one planned task, one frozen model boundary, and
   the primary F2-versus-F1 question; it never displays an outcome arrow.
5. The provenance visual keeps relation, claim support, and disposition as
   separate records; `UNKNOWN` never becomes `DEPENDENT` or
   `INDEPENDENT-AS-STIPULATED` by visual proximity.
6. The sample visual says `N=300` is planned fictional bundles, no study has
   run, and the negative-result commitment is predeclared rather than a
   prediction.

### Popover keyboard and screen-reader tests

1. From the reading flow, Tab reaches each trigger in source order; Enter and
   Space open it; the trigger exposes expanded state and an explanation role.
2. The final chosen role is internally consistent: if `dialog`, focus moves to
   a labelled heading or close control, `aria-modal` / focus containment are
   intentional, Escape closes, and focus returns; if non-modal disclosure,
   focus remains in a documented reading flow and the panel is not announced as
   a modal dialog.
3. The screen reader announces the term label, definition, example, and
   boundary once, without requiring hover or color. The close control has a
   useful name and is reachable.
4. A no-JavaScript or blocked-hydration rendering still exposes the plain
   definition in surrounding text or a native disclosure. The visual is an
   enhancement, not the only semantic path.
5. A second trigger does not leave two ambiguous dialogs open, and a panel
   cannot be clipped by the viewport edge or an ancestor overflow region.

### Responsive, motion, contrast, and print tests

1. Check 320px, 390px, 720px, and 1440px CSS widths plus 200% reflow. The page
   has no horizontal scroll; only deliberately labelled data regions scroll.
2. At narrow widths, the panel remains inside the viewport, has a readable
   close target, and does not hide the only copy of the sentence being
   explained. Long definitions scroll inside the panel without trapping the
   page.
3. Under `prefers-reduced-motion: reduce`, no essential movement, smooth
   scroll, or auto-expanding transition remains. There is no hover-only
   meaning.
4. Verify body, labels, trigger affordances, panel text, state text, and focus
   indicators against every accent panel in normal and forced-color modes.
   Color is never the only status channel.
5. In browser print preview, closed popovers do not remove substantive
   definitions; figures, counts, state words, and status text fit the page;
   connectors and decorative dots may disappear without changing meaning.

### Cold-reader comprehension tests

Use five readers with no glossary or project context.

- After the first visual, ask: “How many report observations? How many known
  common-origin clusters? Does the visual say the reports are false?” Pass if
  at least four of five answer `09`, `01`, and “no.”
- After F0/F1/F2, ask: “What is the one primary comparison?” Pass if at least
  four of five say “F2 versus F1, supplied relation labels versus the explicit
  rule,” without describing F2 as a product version or a result.
- After provenance / UNKNOWN / HOLD, ask: “What does the trace prove, what
  remains unknown, and what happens next?” Pass if at least four of five say
  lineage does not prove claim support, UNKNOWN stays unresolved, and a human
  holds / verifies.
- After the Lab visual, ask: “What does `N=300` mean, and what if the cue
  harms performance?” Pass if at least four of five say planned fictional
  bundles, no result, and reject / report harm rather than spin it as success.

## Handoff to parent integrator

The files in `experiments/v15_2_concept_visuals/` are the complete lane-owned
prototype package. The parent integrator should record each accepted,
modified, deferred, or rejected recommendation in the canonical v15.2 ledger;
no prototype should be wired into production by implication. The best next
decision is whether the origin visual should live in the receipt itself or in
the first “origin relation” explanation. The second-best decision is whether
the Lab has enough room for the combined sample / negative-result visual or
should retain only a sentence and the four outcome labels.
