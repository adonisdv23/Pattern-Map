# Pattern Map v16 site-polish plan

Status: **implementation plan recorded before the material visual revision**

This plan is an owner-review artifact for the local site lane. It is not
reader-comprehension evidence, effectiveness evidence, research evidence, or a
deployment plan.

## Baseline captured at the exact starting head

- Branch: `codex/pattern-map-v16-site-polish`
- Starting head: `4b5fc809e84a1d6c32c7565808821332421fa42e`
- Fresh baseline captures: `qa/visual/baseline-4b5/`
- Current strengths to preserve: warm paper palette, confident serif/mono/sans
  hierarchy, semantic landmarks, exact frozen first-screen copy, three principal
  doors, ordinary-language family bridges, progressive disclosures, historical
  labeling, and late/separate Echo handling.
- Baseline gaps to address: the home repeats a near-identical card grammar, the
  first mobile viewport has no principal-door affordance, the Map's current
  relationship view appears after the six family cards, Apply begins as a
  static four-card index, and route orientation has no persistent chapter rail.
- The pre-existing `qa/visual/screenshots/home-mobile-390x844.png` showed a
  solid dark lower region. A fresh 390x844 capture from this exact starting
  build paints the paper background through the viewport with `scrollWidth`
  equal to 390 and no clipped/overflowing boundary. The dark region is
  recorded as a stale capture artifact; it will not be overwritten as if it
  were a site rendering defect. The final mobile capture must still be made
  from the final committed build and visually inspected.

## Information architecture and visual system

1. Keep the first screen human-problem-first, with the exact frozen headline
   and standfirst. Make the three doors distinct teaching modes: a reading
   ribbon, a six-family map preview, and a route/receipt preview. On narrow
   screens, tune type and spacing so a clear principal-door affordance reaches
   the first viewport without a fixed-height hero.
2. Add a persistent wide-screen orientation rail with the current route marked
   by `aria-current`, principal doors, and a next-route cue. Collapse it into a
   normal-flow `<details>` index on narrow screens; it must never become a
   horizontal keyboard or touch trap and must not cover anchors.
3. Make Explore's first teaching object a current-v16 relationship map. Use
   semantic HTML nodes, code-native connectors where useful, a visible text
   equivalent, exact F1–F6 order/questions, keyboard-operable family focus, an
   `aria-live` status, a visibly looped F6 learning path, and an explicit
   baseline feeding absence + memory. Keep recurrence subordinate to F2/F5.
4. Give Read an editorial index, progress treatment, section rhythm, and a
   short pull quote while preserving the cumulative 60–90-second entry, the
   complete canonical essay, and the optional mentor handoff as a distinct
   disclosure.
5. Make Apply a bounded decision surface: ordinary/lightweight/moderate/
   advanced are choices with consequence, uncertainty, reversibility, budget,
   and permission cues. A local reversible interaction will produce a visible
   route receipt plus separate route/stop/learning/human-disposition states;
   static HTML will retain the complete vocabulary when JavaScript is absent.
6. Replace repeated example cards with three full-width teaching narratives:
   peripheral candidate → weighing → challenge; velocity/expected absence →
   explicit baseline; and nine reports → one common origin with independence
   `UNKNOWN`. Signal Foundry remains `ILLUSTRATION ONLY / READ-ONLY / NOT
   VALIDATION`; Echo remains late, separate, unrun, and no-results.
7. Keep Boundaries, Sources, Research, and History in the same publication
   system. Preserve the v13 image bytes and exact label
   `Historical v13 origin — not the current v16 topology.`

## Verification loop

- Build and static-check the focused implementation first.
- Run an initial browser pass on Home, Map, Read, Apply, and mobile; inspect
  screenshots and state transitions, then revise based on actual evidence.
- Capture final views at 1440x900, 1280x720, 1024x768, 768x1024, 390x844, and
  360x800. Inspect the exact final images, including the prior black-region
  location, rather than cropping or hiding it.
- Exercise pointer and supported keyboard paths for rail/menu Escape, family
  focus, disclosures, route receipt, stop/hold/human disposition, and reduced
  motion. Record the in-app browser's physical-keyboard boundary explicitly.
- Run no-script, standalone-fragment, semantic-name/heading, forced-colors,
  200% reflow, print-oriented, local-link, Echo-removal, historical-label,
  and PDF render checks.
- State plainly in QA that these are implementation and artifact checks, not
  reader comprehension, persuasion, effectiveness, screen-reader
  certification, or empirical evidence.

## Deliberate non-copying boundary

The v14/v15.2 references are used for editorial rhythm, persistent orientation,
chapter numbering, visual teaching objects, and layered reading. Their
provenance-first opening, thesis wording, provider/research posture, decorative
bitmap language, and Echo-centered framing are not being restored. The v16
content interface remains the authority.
