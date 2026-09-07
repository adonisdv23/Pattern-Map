# v15.2 post-integration site accessibility / interaction red team

**Review posture:** read-only post-integration audit of the uncommitted site.

**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`

**Review date:** 2026-08-19

**Scope:** the canonical runtime routes (`/`, `/explore`, `/lab`, `/sources`),
`HomeEssay`, `ReferenceRoutes`, `DeepReceipt`, `ReadingNav`, `Term`,
`MicroVisual`, `globals.css`, rendered-html tests, and the v15.2 manuscript.
The review covered the three reading stops, native Popover behavior as far as
the available local tools permitted, navigation and skip links, focus return,
server/no-JavaScript meaning, semantic associations, responsive/print rules,
microvisual semantics, the deep receipt, and the preserved v13 image boundary.

No canonical implementation file was edited. No external site, provider,
browser session, deployment, publication, or live experiment was used.

## Executive release call

**Current call: HOLD FOR AN ACCESSIBILITY / BROWSER CONVERGENCE PASS.**

The integration is structurally healthy: all four routes server-render, the
offline build and existing seven rendered-HTML tests pass, same-page fragments
and Popover target IDs resolve, the three CSS-native figures have ordinary text
captions, and the v13 raster remains byte-for-byte unchanged. I found no P0
accessibility or semantic failure in the source review itself.

The artifact is not yet ready for external release because two release-critical
questions are not closed:

1. The reading-stop time promises are not evidenced by the current text budgets.
   The first stop is within the agreed 350-word ceiling, but the cumulative
   five-minute and 12–15-minute routes are materially shorter than the agreed
   reading contract.
2. The native Popover path delegates Escape/light-dismiss focus restoration,
   screen-reader announcement, cross-browser support, and collision behavior to
   the browser, while the available environment had no browser instance with
   which to verify those behaviors. The source checks prove markup shape, not
   interaction.

There is also one confirmed keyboard defect: every skip link targets a section
that is not focusable, so a keyboard user can be scrolled to the reading stop
while focus remains on the skip link. That should be fixed before release.

The separate methods/evidence review may have additional protocol P0s; the
“no P0” statement below is limited to this site architecture/accessibility
lane.

## Evidence and checks

### Checks run

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| `npm run lint` from `site/` | **PASS** | ESLint completed with exit 0. |
| `npm test` from `site/` | **PASS** | `vinext build` completed; all 7 rendered-HTML tests passed. |
| `npx tsc --noEmit` from `site/` | **FAIL, unrelated workspace typing** | Fails at `db/index.ts:1` (`cloudflare:workers`) and `worker/index.ts:6–7` (`Fetcher`, `D1Database`). No `site/app` error was emitted. This is still a red check for the repository and should not be described as a clean typecheck. |
| Local production server + SSR fetch | **PASS** | `npm run start -- --port 8773`; `/` 68,462 bytes, `/explore` 164,059, `/lab` 43,137, `/sources` 62,423. All returned HTML successfully. |
| Static IDs / same-page fragments / Popover ARIA references | **PASS** | A local Node parser found no duplicate IDs, no missing same-page fragment targets, and every rendered `aria-labelledby` / `aria-describedby` on a term panel resolved. |
| Native Popover keyboard/touch/AT/print run | **NOT RUN** | The in-app/local browser harness returned **“No browser is available”** for both a local-URL connection and the default browser. No screenshot, accessibility tree, viewport measurement, print emulation, or screen-reader claim below is therefore presented as observed pixels. |
| `axe-core` / HTML validator | **NOT RUN** | `axe-core` is present but there is no DOM/browser runtime in this environment; no external package was installed. |

### Rendered stop-budget measurement

I fetched the built SSR HTML and counted normalized visible text inside each
`HomeEssay` stop section, including headings, figure captions, labels, and the
stop-end copy, but excluding the masthead, rail, footer, and route-card chrome.
This is a reproducible text proxy, not a substitute for five human timed reads.

| Stop anchor | Section text proxy | Cumulative proxy from first stop | At 220–260 wpm |
| --- | ---: | ---: | ---: |
| `#stop-60-90` | 331 words | 331 | 1:16–1:30 |
| `#stop-5` | 621 words | 952 | 3:40–4:20 |
| `#stop-12-15` | 1,151 words | 2,103 | 8:05–9:33 |

The 331-word first stop satisfies the Round 2 `R2-60` ceiling of 350 words and
is plausibly 60–90 seconds at the stated reading assumption. The current
five-minute marker is not supported by the cumulative text proxy unless a
reader spends substantial additional time inspecting the visual and receipt.
The current full route is roughly 600–1,200 words below the Round 2 target of
approximately 2,700–3,300 visible words. The manuscript itself declares the
same route contract in `source/THOUGHT_PIECE_V15_2.md:4–8,59–61,151–154`, so
this is a site/manuscript timing contract issue, not merely a CSS issue.

## P0 findings — release blockers

### None found in this lane

No current source-level P0 was found for this site/accessibility review. The
home masthead, first stop, Lab, and deep receipt consistently disclose that the
example is fictional or supplied, no model has been selected, no study has run,
and no empirical result or publication is being claimed
(`site/app/HomeEssay.tsx:43–50,83,174,252`; `site/app/DeepReceipt.tsx:9–19,80–87`;
`site/app/ReferenceRoutes.tsx:574–584`). The v13 image is labelled historical
and “not the v15.2 system map” (`site/app/HomeEssay.tsx:267–286`), and its
verified local SHA-256 remains
`8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.

This “none” result must not be read as a release approval: the P1 items below
are sufficient to keep the public release gate closed until they are repaired
or explicitly tested and accepted.

## P1 findings — fix or close with evidence before public release

### P1-01 — Skip links do not move keyboard focus to their targets

**Exact anchors:**

- `site/app/HomeEssay.tsx:31–32` links to `#stop-60-90`.
- `site/app/HomeEssay.tsx:75–80`, `104–109`, and `183–188` define the three
  targets as ordinary `<section>` elements with no `tabIndex` or programmatic
  focus behavior.
- `site/app/ReferenceRoutes.tsx:63–66` links Explore to `#map`, Lab to `#lab`,
  and Sources to `#sources`; the corresponding sections at
  `ReferenceRoutes.tsx:313`, `574`, and `670` are likewise not focusable.

**Attack:** Activating a skip link can scroll the viewport, but the active
keyboard focus remains on the skip link because the destination is not a
focusable element. The next Tab therefore proceeds through the DOM from the
rail/skip-link position rather than from the first heading of the promised
reading route. This is particularly harmful on the mobile sticky rail and to
screen-reader users who rely on the skip-link announcement as a transfer into
the main content.

The destination sections are semantically labelled (`aria-labelledby`), but
that does not itself create a focus target. The same issue affects route
navigation links when they are expected to hand a keyboard user to a section,
although skip links are the release-critical case.

**Minimum fix:** Give each skip destination a stable `tabIndex={-1}` and a
visible/appropriate focus treatment, or put the ID and `tabIndex={-1}` on the
destination heading. Preserve the fragment behavior when JavaScript is absent;
do not require a click handler. If the target is the section, use a small
focus style that does not turn every reading section into a persistent widget.
Keep `scroll-margin`/`scroll-padding` aligned with the sticky rail.

**Acceptance test:** With JavaScript disabled and with keyboard-only input,
focus the skip link, activate it, and verify all of the following at `/` and on
each subroute: focus is on the first heading/target within the chosen route;
the target is not hidden under the sticky rail; the next Tab enters the route
in reading order; Shift+Tab returns predictably; and the URL fragment remains
correct. Repeat at 390px and 820px widths. Add a rendered-HTML assertion that
each skip target has `tabindex="-1"` (or that its heading does).

### P1-02 — The three time markers are not yet truthful as a complete route contract

**Exact anchors:**

- `site/app/HomeEssay.tsx:75–102` marks the first route and says
  “Stop here after 60–90 seconds.”
- `site/app/HomeEssay.tsx:104–181` marks the second route and says “Stop here
  after about five minutes.”
- `site/app/HomeEssay.tsx:183–316` marks the third route and says “Stop here
  after the 12–15-minute full argument.”
- Route-card labels are at `HomeEssay.tsx:52–70`; the reading-nav labels are at
  `site/app/ReadingNav.tsx:5–18`.
- The source contract is at `source/THOUGHT_PIECE_V15_2.md:4–8,59–61,151–154`.
- The agreed acceptance budgets are recorded at
  `reports/overnight/v15_2/ROUND2_EDITORIAL_SELECTION_MATRIX.md:63–77` and
  `reports/overnight/v15_2/ROUND2_SITE_ARCHITECTURE_ACCESSIBILITY_AUDIT.md:142–147`.

**Attack:** The first stop is good and remains within the 350-word cap. The
second and third markers are real DOM boundaries, but their actual cumulative
text is approximately 952 and 2,103 words respectively. Under the project’s
220–260 wpm assumption, the reader reaches the second marker in about 3:40–4:20
and the full marker in about 8:05–9:33 before accounting for visual inspection.
The full public route is therefore materially below the agreed 2,700–3,300
word target. A polished stop box does not make a route five or fifteen minutes
long; a reader must be able to reach the promised content and consequence at
that stop.

This is also a manuscript/site agreement risk. The manuscript’s front matter
and stop copy make the same promises, while the current site uses a shorter,
more compressed rendering. The argument is not too long; it is under-filled
for the selected time labels.

**Minimum fix:** Make one contract authoritative and update both artifacts in
the same patch. There are two coherent options:

1. Keep the current text and relabel based on a timed reader check (the first
   stop can remain 60–90 seconds; the cumulative second stop is closer to
   “about four minutes”; the full route is closer to “about nine minutes” plus
   figure inspection); or
2. Keep the 5-minute and 12–15-minute labels and add substantive, non-caveat
   material that earns that time. To meet the existing full-route target, add
   roughly 600–1,200 words across the loops, use boundary, objections, and
   research bridge, with the same additions in the manuscript and site. Do not
   pad with repeated status disclaimers, method acronyms, or a second receipt.

The smallest safe release patch is option 1 unless owner-proxy timing tests
show that the figures and table genuinely account for the gap. Do not silently
change only the route-card labels: update the visible stop markers, nav labels,
manuscript front matter, and acceptance tests together.

**Acceptance test:** Run five cold-reader timed passes with the title and route
cards, then stop at each visible box. For `R2-60`, no more than 350 visible
prose words precede the first stop and 4/5 readers explain “09 / 01 / 00 /
HOLD” without treating it as rejection. For the second stop, 4/5 readers name
the three questions, correction invariant, human next step, and no-results
boundary. For the full stop, 4/5 readers can state the two loops, use boundary,
objections, and narrow research bridge. The measured times, not the label alone,
must justify 60–90 seconds, about five minutes, and 12–15 minutes—or the labels
must be changed.

### P1-03 — Popover focus return and screen-reader announcement are delegated to the UA, not closed by the component

**Exact anchors:**

- `site/app/Term.tsx:19–28` owns one trigger ref and restores focus only through
  `requestAnimationFrame` in `restoreTriggerFocus`.
- The restoration callback is wired only to the explicit close button at
  `Term.tsx:52–59`.
- The trigger and panel are emitted at `Term.tsx:31–49` with
  `popoverTarget`, `popoverTargetAction`, `popover="auto"`, `role="region"`,
  `aria-labelledby`, and `aria-describedby`.

**What is good:** The current component no longer has the old dialog mismatch:
it has no `role="dialog"`, no `aria-modal`, no inert background, and the
backdrop is transparent (`globals.css:525`). The panel is present in server
HTML, all target/label/description IDs resolve, and the explicit close control
returns focus to its initiating trigger. Native `auto` popovers should provide
light dismissal and a one-auto-popover policy in supporting engines.

**Attack / browser risk:** Escape and outside/light dismissal have no component
handler. If a user tabs from the trigger into the panel and presses Escape, or
clicks outside while focus is in the panel, the source does not explicitly
restore focus to the initiating trigger or confirm which trigger owns the
closed panel. The implementation therefore depends on each browser’s Popover
focus-restoration and accessibility-tree behavior. The same is true of whether
the native invoker’s implicit expanded/controls relationship is announced by
the target screen reader. Static tests cannot establish either behavior, and
the local browser harness was unavailable.

This is not a recommendation to turn the term into a modal dialog. The current
nonmodal contract is the right information architecture: the explanation is
optional and the reading page must remain available. The release risk is that
the nonmodal implementation is not yet verified across the browser/AT matrix,
not that it lacks a focus trap.

**Minimum fix:** Keep the nonmodal native Popover path only if the supported
browser matrix demonstrates all required behavior. Add a narrowly scoped
enhancement (for example a `toggle`/`beforetoggle` handler on the active panel)
that restores focus only when the panel is being hidden and the active element
was inside that panel; do not attach one competing document Escape listener per
term. If the owner requires broad no-JavaScript support, use a native
`<details>/<summary>` fallback or a feature-detected fallback rather than
assuming Popover exists everywhere. Preserve the current `role="region"`,
label, and description association; do not reintroduce `role="dialog"` without
the full modal contract.

**Acceptance test:** On every route containing terms, with keyboard only:

- Tab to a term trigger; Enter and Space open it without moving focus into a
  modal trap. The trigger’s accessible name contains the visible term.
- The region is exposed with the visible term heading and the definition,
  example, and boundary as its description. Verify this with an accessibility
  tree and VoiceOver + Safari, NVDA + Chrome/Firefox, and one Chromium-based
  screen reader path.
- Tab into the panel, press Escape, and verify that exactly the initiating
  trigger is focused. Click the explicit close button and verify the same.
- Open term A, then term B. Verify A closes exactly once, B is fully usable,
  there is no focus jump to a different trigger, and a second Escape does not
  close unrelated content.
- Click outside from both the trigger and panel; verify light dismissal is
  deterministic and nonmodal background interaction is not accidentally
  inert.
- Repeat with JavaScript disabled. The definition/example/boundary must remain
  available in a browser without requiring hydration. Repeat in a browser that
  lacks Popover support or establish that such browsers are outside the
  support baseline; otherwise supply the `<details>` fallback.

### P1-04 — The fixed-corner term panel is viewport-safe but not trigger-safe

**Exact anchors:**

- `site/app/globals.css:505–524` positions every term panel `fixed` at the
  lower-right with a maximum width of 390px.
- `site/app/globals.css:755–763` changes the mobile panel to a nearly full-width
  fixed bottom sheet.
- The triggers are inline text buttons at `site/app/Term.tsx:31–41`.

**Attack:** The rule prevents ordinary off-viewport overflow, but every term
  explanation opens in the same viewport corner regardless of where the term
  appears. On a desktop paragraph, the explanation can be far from the phrase
  that invoked it and can cover unrelated route-end controls. On a narrow
  screen, the bottom sheet can cover the sentence or stop box that gives the
  term its context. There is no anchor relation, collision choice above/below
  the trigger, or “this explanation is for the phrase you just activated” cue
  beyond the panel heading.

This is an interaction/context risk rather than a simple `scrollWidth` bug: the
panel’s right/bottom insets are sensible, but the reading position is not
preserved. The current source cannot claim collision-safe behavior until a
browser pass checks long terms, triggers at the top/middle/bottom, and multiple
viewports.

**Minimum fix:** Prefer CSS anchor positioning with a supported fallback, or a
small measured fixed placement that clamps to safe-area insets and chooses the
side with available space. Keep a readable maximum height and internal scroll,
and ensure the trigger remains in view or the panel’s visible heading repeats
the term. Do not solve this by adding a second permanent glossary card or by
making the optional explanation a modal.

**Acceptance test:** At 1440, 1024, 820, 390, and 320 CSS pixels, open terms
near the left edge, center, right edge, first viewport, middle of a long stop,
and immediately before a stop-end box. The panel must remain fully within the
safe viewport, must not force document horizontal scrolling, must expose all
content through internal scrolling, and must not cover the only copy of the
sentence it explains. At 200% text zoom, repeat the test and verify the close
target remains reachable.

### P1-05 — The no-JavaScript promise is good for modern Popover UAs but incomplete as a browser fallback

**Exact anchors:**

- `site/app/Term.tsx:14–17` claims server HTML and no-hydration operation.
- The rendered SSR HTML does contain both the trigger and full panel content at
  `/`, `/lab`, and `/sources`; this part passes static inspection.
- `site/app/globals.css:801–813` attempts a print/static expansion with
  `[popover].term-popover { display: block !important; }`.

**Attack:** In a modern browser implementing the native Popover API, the panel
  is a real server-rendered native disclosure and no application JavaScript is
  needed to toggle it. In a browser that does not implement `popover` and
  `popovertarget`, however, the user receives a button with a hidden
  `[popover]` panel and no fallback behavior. The server HTML is present, but
  presence in source is not the same as readable no-JavaScript behavior when
  the user agent applies the Popover hidden rule.

The current acceptance language should therefore say either “no JavaScript in
supported native-Popover browsers” or provide a true baseline fallback. This
is especially important for screen-reader/browser combinations with different
Popover API support dates.

**Minimum fix:** Use `<details>/<summary>` as the progressive-disclosure
  baseline, optionally enhance the open panel with native Popover positioning,
  or add a tested feature-detected fallback that leaves the definition in normal
  flow. Keep the surrounding manuscript independently understandable as it is
  now. If the support baseline deliberately excludes non-Popover UAs, document
  that in the release checklist and test the selected Safari/Firefox/Chromium
  versions rather than calling the path universally no-JS safe.

**Acceptance test:** Fetch the SSR HTML with scripts removed and verify every
  term’s definition, example, and boundary remains ordinary text. Run a
  JavaScript-disabled test in a current supported UA and a deliberately
  unsupported/fallback UA. In both cases, the explanation must be discoverable
  without a generated client-only node and must not be the only place where a
  claim boundary is stated.

## P2 findings — fix before durable merge or explicitly defer

### P2-01 — Server-rendered `aria-current` is wrong on every subroute without hydration

**Exact anchors:**

- `site/app/ReadingNav.tsx:21–23` initializes `active` to `"start"`.
- `site/app/ReadingNav.tsx:24–54` computes the route and active section only in
  `useEffect`.
- `site/app/ReadingNav.tsx:56–62` emits `aria-current="location"` from that
  state.

**Evidence:** The SSR HTML for `/`, `/explore`, `/lab`, and `/sources` marks the
  `/` “Start” link as current before hydration. With JavaScript disabled it
  remains wrong on all three subroutes. With JavaScript enabled it eventually
  corrects after the effect/IntersectionObserver runs, but this creates a
  server/client semantic flash and leaves a no-JS reader with an inaccurate
  current-location announcement.

**Minimum fix:** Pass the route mode/current path into `ReadingNav`, or render
  the route-level current state in the server page wrapper and let the client
  enhancement manage only section-level active state. For a no-JS page, omit a
  misleading current marker rather than marking Start current. Add a hash/path
  test for the initial SSR state; keep `aria-current="location"` for the
  in-page section use if it remains useful.

### P2-02 — Several `aria-label`s sit on generic `div`s and are not reliable accessible names

**Exact anchors:**

- `site/app/HomeEssay.tsx:51` (`Choose a reading path`) and
  `HomeEssay.tsx:115` (`Three plain relation states`) are labels on generic
  `<div>` elements.
- `site/app/MicroVisual.tsx:9` labels the generic observations `<div>`.
- Equivalent generic-container labels occur in
  `site/app/ReferenceRoutes.tsx:90,488,609`.

**Attack:** A generic `div` has no landmark/widget/group role for which an
`aria-label` is announced, so the label may be ignored by the accessibility
tree. The visible child headings and text make these omissions nonfatal, but
the source currently implies a semantic grouping that is not consistently
real. The origin visual is especially easy to misread: the nine visible O01–O09
tokens are available, but `aria-label="Nine report observations"` is not a
reliable replacement for a labelled list/group.

**Minimum fix:** Remove labels that add no semantic value, or use a real
`section`/`aside` with a visible heading and `aria-labelledby`; use
`role="group"` only for an actual labelled group. Keep all microvisual meaning
in visible text and the `<figcaption>`, as `MicroVisual.tsx:28–31,44–47,59–62`
already does.

**Acceptance test:** Inspect the accessibility tree for every labelled
container. Each announced group must have a name, and no label may be the sole
carrier of a count, state, or boundary. Run forced-colors/grayscale review to
confirm the text still carries all states.

### P2-03 — Explore’s skip link bypasses the first, named deep receipt

**Exact anchors:** `site/app/ReferenceRoutes.tsx:63–66` says “Skip to the map”
for Explore, while `site/app/ReferenceRoutes.tsx:311–313` renders
`<DeepReceipt />` (whose target is `site/app/DeepReceipt.tsx:6`) before
`#map`.

**Attack:** The deep receipt is the first and most concrete Explore record, and
the reading navigation explicitly exposes `#deep-receipt` at
`ReadingNav.tsx:10`. The skip link silently jumps past it. That may be an
intentional shortcut for a map-first page, but it is not aligned with the
route’s actual source order or its most useful semantic record. It also makes
the generic “skip to map” promise differ from the route-card promise to inspect
the receipt.

**Minimum fix:** Either target `#deep-receipt` and label the link “Skip to the
detailed receipt,” or make the receipt explicitly optional before the map and
say so in the subpage masthead. Whichever choice is made, apply P1-01’s focusable
target fix and keep `ReadingNav` order consistent.

### P2-04 — A second home renderer remains live source code and can break the v15.2 contract

**Exact anchors:**

- `site/app/page.tsx:1–15` correctly sends the canonical home mode to
  `HomeEssay`.
- `site/app/ReferenceRoutes.tsx:56–123` still contains an old `isHome` branch
  with `#takeaway`, `#essay`, the old route cards, and a separate home body.
- `ReferenceRoutes.tsx:722–724` still exports a default `Home` that calls that
  old branch.

**Attack:** The currently routed home is correct, but a future import or route
  refactor can accidentally select the stale branch. Its `ReadingNav` now
  advertises `#stop-60-90`, `#stop-5`, and `#stop-12-15`, while that branch has
  none of those targets. That is a latent broken-navigation and manuscript/site
  agreement failure, not merely dead code.

**Minimum fix:** Remove the old home branch and default export from
`ReferenceRoutes`, or make it an explicitly named non-runtime historical fixture
outside the app tree. Keep one canonical home renderer and add a route test that
imports the actual app page rather than only checking source strings.

### P2-05 — Term panel title is named by a `<strong>`, not a heading, and touch sizing is unverified

**Exact anchors:** `site/app/Term.tsx:42–49` uses a `<span role="region">`, and
`Term.tsx:50–52` names it with `<strong id="…-heading">`. The trigger styling is
at `site/app/globals.css:491–504`.

**Attack:** The ARIA `aria-labelledby` association is structurally valid and
the static ID check passes, but the title is not a heading for screen-reader
heading navigation. The inline trigger has a minimum height but only small
horizontal padding; at 320/390px and high text zoom, it may be a difficult touch
target even though it is technically a button. This is not the old 1px-padding
implementation, but the WCAG inline-target exception should be an explicit,
tested design decision.

**Minimum fix:** Use an actual heading element inside the labelled region (or
document why a short named region is sufficient), preserve the visible term in
the button’s accessible name, and test the inline target before increasing its
padding enough to disrupt prose. Do not add a heading level merely for styling;
use the smallest semantic heading appropriate to the route.

**Acceptance test:** Heading navigation reaches a term explanation only when it
is intentionally open; the panel’s accessible name/description remains correct;
the trigger and close control are comfortably operable at 320/390px and 200%
zoom; and no line of prose becomes an accidental row of large cards.

### P2-06 — The print rule is present but has not been rendered; closed Popovers could still regress in a UA-specific print path

**Exact anchors:** `site/app/globals.css:775–818`, especially
`801–813`, expands closed term panels and hides `.term-close` at `780`.

**What passes statically:** The rule is the right intent: term definitions are
server-rendered, panel display is forced in print, the close button is hidden,
table overflow becomes visible, and details/component bodies are expanded.

**Risk:** No print engine was available. Native Popover UA rules, top-layer
serialization, page breaks, and `display: block !important` behavior vary. The
term trigger’s dotted underline/button styling also remains in print, and a
long definition could split awkwardly after the trigger. The v13 image and deep
receipt tables need a real PDF check for page breaks and legibility.

**Minimum fix / acceptance:** Render `/`, `/explore`, `/lab`, and `/sources` to
PDF at the declared A4 page size with all terms closed and one term open before
printing. Definitions/examples/boundaries must appear exactly once, in source
order, with no close controls, rail, route cards, shadows, clipped table, or
horizontal-scroll instruction that is the only way to read a table. If the
browser does not print closed Popovers despite the CSS rule, switch the print
surface to a normal-flow disclosure copy rather than relying on top-layer
serialization.

### P2-07 — Existing tests assert source patterns, not the interaction contract

**Exact anchors:**

- `site/tests/rendered-html.test.mjs:125–137` checks IDs and strings but not
  focusable skip destinations, current-path `aria-current`, or route budgets.
- `rendered-html.test.mjs:146–165` calls the term test “native nonmodal, no-JS”
  while checking only source regexes and a few SSR strings.
- `rendered-html.test.mjs:173–190` checks CSS text, including print rules, but
  does not render a viewport or print document.

**Minimum fix:** Keep these fast offline tests, but add a separate browser test
layer (or an explicitly documented manual matrix) for focus, Popover open/close,
light dismiss, second-trigger behavior, viewport collision, print, and screen
reader semantics. Add offline assertions for the three word budgets, stop-end
order, skip-target focusability, and route-specific initial current state. Do
not make regex checks the release evidence for behavior they cannot observe.

## Specific surfaces that passed the static red team

These are conditions to preserve while fixing the P1/P2 findings:

- `Term` uses a nonmodal role (`region`), has stable heading/description IDs,
  includes definition/example/boundary text in server HTML, and has an explicit
  close control that returns focus (`site/app/Term.tsx:31–68`). The old
  dialog/`aria-modal` mismatch is not present in this integration.
- The static parser found no duplicate IDs on any route; same-page `#` links
  resolve; rendered Popover target IDs and term ARIA references resolve.
- The first route keeps technical F/T/N shorthand out of the text before its
  stop-end marker (`HomeEssay.tsx:96–100`), and the compact receipt is followed
  by the plain “hold, not rejection” explanation.
- Exactly three microvisual variants are used: origin count
  (`MicroVisual.tsx:8–32`), trace/hold (`:38–49`), and conditions (`:53–63`).
  Each is a `<figure>` with visible text and a `<figcaption>`; no result or
  effect is encoded only in color. The decorative origin connectors are
  `aria-hidden` (`MicroVisual.tsx:14–15`).
- The deep receipt preserves a captioned table, scoped row/column headers,
  a labelled keyboard-focusable overflow region, plain state before codes, and
  the B1/C1 contrast boundary (`DeepReceipt.tsx:40–77`).
- Responsive CSS collapses route/receipt/visual grids at 780px, hides the
  decorative origin trace on narrow screens, gives term panels safe-area insets,
  and keeps tables inside explicit overflow regions (`globals.css:681–763`).
  These are source-level positives; the required pixel pass remains open.
- The print stylesheet deliberately expands terms/details and converts table
  wrappers to visible flow (`globals.css:775–843`). It needs rendering evidence,
  not redesign by assumption.
- The local v13 image is used only as a historical figure with an explicit
  “not the v15.2 system map” boundary. Preserve that caption and the text
  summary when adjusting responsive layout.

## Browser-risk matrix

| Surface | Chromium-family risk | Safari/Firefox/AT risk | Gate |
| --- | --- | --- | --- |
| Native `popover` / `popovertarget` | Likely supported in a current engine, but no local browser run confirmed target attributes, top-layer placement, or implicit expanded state. | Support/version and accessibility-tree behavior can differ; unsupported UAs need a real fallback. | **P1**: test selected versions or ship `<details>` fallback. |
| Escape/light-dismiss focus | Explicit button path is deterministic; native dismissal is not handled in component code. | Focus restoration and screen-reader announcement must be checked with VoiceOver/NVDA/Firefox/Chrome combinations. | **P1**. |
| Fixed panel placement | Insets avoid obvious viewport overflow; trigger/panel relation and overlap remain unverified. | Safe-area, dynamic viewport, zoom, and top-layer differences can change bottom-sheet geometry. | **P1**. |
| Print | CSS intent is present. | Popover top-layer serialization and page breaks are engine-specific. | **P2**, but no external release without a PDF pass. |
| Sticky mobile rail / skip links | Fragment scroll likely works; target focus does not by source. | AT may announce the rail/skip link instead of the reading heading after activation. | **P1** for skip focus. |
| `IntersectionObserver` nav state | Hydration should eventually update the active section. | No-JS and pre-hydration subroutes mark Start current; observer support/scroll timing needs fallback. | **P2**. |

## Smallest coherent file-level patch sequence

This is an implementation recommendation for the parent integrator; no step was
performed in this audit lane.

1. **Repair focus targets first.** Update `HomeEssay.tsx` and the subpage shell
   in `ReferenceRoutes.tsx` so skip destinations/headings are focusable with
   `tabIndex={-1}` and their mobile scroll offsets are correct. Add the offline
   assertion before changing visual styling.
2. **Freeze one route contract.** Measure the current route with owner-proxy
   readers, then update `source/THOUGHT_PIECE_V15_2.md`, `HomeEssay.tsx`, and
   `ReadingNav.tsx` together. Either keep the current prose and make the labels
   approximately four/nine minutes where warranted, or add earned argument
   content to meet the selected five/12–15-minute contract. Do not pad the
   first stop or duplicate the detailed receipt.
3. **Close the native term contract.** In `Term.tsx`/`globals.css`, retain the
   nonmodal semantics and stable ARIA IDs; add a scoped hide/focus-return
   enhancement or adopt details-first markup. Define the supported browser
   baseline and fallback. Make placement collision-safe, then run the keyboard,
   touch, AT, second-trigger, and no-JS matrix.
4. **Make the nav server-honest.** Pass the route mode or server current item to
   `ReadingNav.tsx`, remove the incorrect pre-hydration `Start` marker on
   subroutes, and decide whether Explore skips to `#deep-receipt` or explicitly
   skips an optional receipt. Add fragment/current-state tests.
5. **Remove the duplicate home implementation.** Delete or quarantine the old
   `isHome` branch/default from `ReferenceRoutes.tsx`; keep `page.tsx`/`HomeEssay`
   as the only canonical home route. This is the smallest way to stop future
   v15.1/v15.2 ID and manuscript drift.
6. **Normalize semantic labels and test surfaces.** Replace generic-container
   `aria-label`s with real labelled regions or visible text; use a heading in
   the term panel if heading navigation is part of the contract. Extend
   `rendered-html.test.mjs` for budgets/skip targets/ARIA, and add the browser
   and PDF checks as a release artifact rather than pretending regex tests cover
   them.
7. **Run the final evidence pass.** Re-run lint/build/tests, fix or document the
   unrelated Cloudflare typing check, capture current 320/390/720/820/900/1440
   screenshots and A4 PDFs, and record keyboard/AT results. Keep the v13 hash
   and all no-result boundaries unchanged.

## Acceptance checklist for the release gate

Release may move from **HOLD** to **CONDITIONAL ACCEPT** only when all of these
are evidenced:

- [ ] Skip links move focus to the named route target with JavaScript enabled
      and disabled at desktop, tablet, and mobile widths.
- [ ] The three visible stop labels match timed cold-reader behavior and the
      manuscript front matter; the first remains within 350 words, the second
      satisfies the chosen five-minute contract, and the full route satisfies
      the chosen 12–15-minute contract or is honestly relabelled.
- [ ] Popover open, explicit close, Escape, light dismiss, and second-trigger
      behavior preserve the initiating focus and do not create a modal/inert
      mismatch. Screen-reader names and descriptions are verified, not inferred
      from source regexes.
- [ ] A current supported browser and a documented fallback/unsupported path
      both preserve term definitions without requiring hydration.
- [ ] Terms stay within safe viewport bounds and preserve reading context at
      320/390/820/1440 CSS pixels and 200% text zoom; body `scrollWidth` does
      not exceed the viewport except in deliberately focusable table wrappers.
- [ ] All three microvisuals retain visible text equivalents, state/boundary
      language, and no result-implying arrow/color semantics. There are no new
      decorative visuals beyond the three approved placements.
- [ ] Print/PDF shows every term definition once, expands details, keeps tables
      readable, hides controls/rail/shadows, and preserves the historical image
      boundary.
- [ ] SSR/static checks still show unique IDs, resolvable same-page fragments,
      resolved ARIA references, no accidental v15.1 home route, and unchanged
      no-model/no-study/no-result/no-publication status.

## Final matrix

| Finding / surface | Decision | Rationale |
| --- | --- | --- |
| P0 site/accessibility source failures | **ACCEPT** | None found in this lane; status and historical-image boundaries are explicit and the built routes render. |
| Skip-link focus | **REVISE** | Confirmed keyboard defect; fix before public release. |
| Three reading-stop markers | **REVISE** | Real anchors exist, but the second/full time budgets are not currently supported by the text contract. |
| Native nonmodal Popover semantics | **CONDITIONAL ACCEPT** | Current role/ARIA/no-modal shape is directionally correct; retain only after cross-browser/AT focus and announcement evidence, with a fallback decision. |
| Popover placement/collision | **REVISE** | Fixed-corner placement is viewport-safe but context-detached and unverified at zoom/mobile edges. |
| No-JS/server term meaning | **CONDITIONAL ACCEPT** | SSR content exists and modern native Popover can operate without hydration; unsupported-UA behavior is not a safe universal fallback yet. |
| Microvisual count/semantics | **ACCEPT** | Exactly three approved CSS-native figures, each with visible text/caption and no result claim. |
| Deep receipt/table | **ACCEPT** | Explicit relation codes, plain states, scoped headers, focusable overflow, and contrast-root boundary survive static review; verify print/responsive pixels. |
| Responsive CSS | **CONDITIONAL ACCEPT** | Source rules cover grids, safe areas, and table overflow; no browser viewport evidence exists. |
| Print CSS | **CONDITIONAL ACCEPT** | Intent is correct; PDF rendering is still a release check. |
| Reading nav SSR state | **REVISE** | Subroutes incorrectly mark Start current without hydration. |
| Duplicate home source | **DEFER only with owner sign-off; otherwise REVISE** | Runtime currently uses `HomeEssay`, but the stale branch can reintroduce broken v15.2 targets. |
| Existing offline tests | **REVISE** | Keep them, but add behavior-level/browser/PDF evidence and budget/skip assertions. |

**Final gate:** **HOLD — revise P1-01 through P1-05 or close each with the
specified browser/timed evidence, then re-run the full checklist.**

