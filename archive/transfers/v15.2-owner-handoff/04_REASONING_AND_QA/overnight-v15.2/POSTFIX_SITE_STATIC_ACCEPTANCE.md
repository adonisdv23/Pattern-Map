# v15.2 post-fix static site / accessibility acceptance

**Review posture:** read-only acceptance review after the v15.2 site fixes.

**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`

**Review date:** 2026-08-19

**Decision: PASS WITH MANUAL QA RESIDUALS**

The post-fix source and standalone artifacts satisfy the requested static
acceptance contract. The three public reading labels are now consistently
`60–90 seconds`, `about four minutes`, and `about nine minutes`; each route's
server-rendered current item is correct; every skip destination is a keyboard
focus target; Explore skips to the first, named deep receipt; term definitions
are server-rendered and have a native-Popover path plus a static unsupported-UA
fallback; the stale home renderer is gone; standalone HTML inlines its CSS,
focus-return script, and raster assets; and the no-results boundary is present
on every route. `npm test` (build plus seven rendered-HTML tests) and
`npm run lint` both pass.

This is not a browser/AT or pixel release sign-off. No browser instance was
available in this environment, so native Popover behavior, screen-reader
announcement, actual focus return, collision placement, forced-colors pixels,
responsive layout, and printed PDF output remain unverified. The remaining
manual checks are listed below and are release-gate residuals, not claims of
observed browser failure.

## Evidence reviewed

The review read the complete post-integration site red-team and owner-reader
red-team reports, the current `HomeEssay`, `ReferenceRoutes`, `ReadingNav`,
`Term`, `DeepReceipt`, `globals.css`, rendered-HTML tests, standalone route
manifest, and a representative complete standalone route (`index.html`). The
source line references below point to the current worktree, not the earlier
pre-fix reports.

### Checks run

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| `npm test` from `site/` | **PASS** | Post-correction `vinext build` completed and all 7 rendered-HTML tests passed. The tests cover route rendering, fragments/IDs/current state, term source shape, Lab no-result/gate/result-ladder boundaries, starter-preview removal, and CSS/metadata assertions (`site/tests/rendered-html.test.mjs:19–224`). |
| `npm run lint` from `site/` | **PASS** | ESLint exited 0 with no diagnostics. |
| Route/current/skip static scan | **PASS** | The built SSR output reports `Start` on `/`, `Explore · receipt` on `/explore`, `Lab · no results` on `/lab`, and `Sources` on `/sources`; skip links and their `tabindex="-1"` targets resolve on all four routes. The equivalent offline assertions are `site/tests/rendered-html.test.mjs:139–161`. |
| Standalone dependency scan | **PASS** | `index.html`, `explore.html`, `lab.html`, and `sources.html` each have inline `<style>`, no `<link>` stylesheet, no external `<script src>`, and no local `src` asset. Raster images are `data:` URIs (2 in `index.html`, 1 in `explore.html`); route links are relative HTML navigation. `sources.html` has 19 intentional external source links, but no external runtime or asset dependency. |
| Stale-home scan | **PASS** | `rg` found no `isHome`, `#takeaway`, `#essay`, `origin-receipt`, or old home export in `site/app/ReferenceRoutes.tsx`; canonical home dispatch is `site/app/page.tsx:9–15`. |
| Browser / accessibility tree / AT / viewport / print | **NOT RUN** | The available browser harness had no browser. No screenshot, accessibility-tree, VoiceOver/NVDA, viewport, forced-colors, zoom, or PDF claim below is presented as observed. |

`tools/predeploy_smoke_check.py` is not present in this worktree, so that
repository-level check was not applicable here; no deployment or live external
check was attempted.

## Static acceptance matrix

### 1. Reading stops and time labels — PASS statically; timed cold-reader QA remains

The visible labels converge across the home route, in-page rail, manuscript
contract, and standalone export:

- Home route cards say `60–90 seconds`, `About 4 minutes`, and `About 9 minutes`
  (`site/app/HomeEssay.tsx:51–70`). The corresponding stop markers and end
  boxes say `60–90 sec` / `60–90 seconds`, `About 4 min` / `about four minutes`,
  and `About 9 min` / `roughly nine-minute full argument`
  (`HomeEssay.tsx:75–103,106–184,186–321`).
- The reading rail uses the same three labels
  (`site/app/ReadingNav.tsx:5–18`). The historical IDs `stop-5` and
  `stop-12-15` are retained as route-stable identifiers, while the visible
  labels are the revised four/nine-minute contract
  (`HomeEssay.tsx:106–113,186–193`).
- The source contract agrees: first impression, essential argument, and full
  essay are `60–90 seconds`, `about four minutes`, and `about nine minutes`
  (`source/THOUGHT_PIECE_V15_2.md:4–8`), with the four-minute and nine-minute
  stop prose at lines `154–157` and `305–307`.
- The rendered-HTML test asserts all three stop anchors, focusability, and
  labels (`site/tests/rendered-html.test.mjs:19–39`).

An offline text proxy over the standalone home route is directionally
consistent with those revised labels: approximately 374 words in the first
stop including its figure/caption/end box, 649 in the second stop, and 1,209
in the full stop, or roughly 1.4–1.7, 3.9–4.6, and 8.6–10.1 minutes at
220–260 words per minute when counted cumulatively. The first stop's prose
alone is about 321 words; the figure and short receipt explanation are the
intended inspection time. This is a text proxy, not a timed human read.

**Residual:** five cold-reader timing passes are still required before calling
the labels empirically honest. If the measured behavior diverges materially,
update the manuscript, home copy, rail, and standalone export together. No
static P0 or confirmed implementation P1 remains for the labels.

### 2. Initial `aria-current` per route — PASS

`ReadingNav` now accepts a server-supplied `initialActive` value and initializes
state from it (`site/app/ReadingNav.tsx:21–23`). The home passes `start`
(`site/app/HomeEssay.tsx:34–39`); Explore, Lab, and Sources pass
`deep-receipt`, `lab`, and `sources` respectively
(`site/app/ReferenceRoutes.tsx:39–55`). The effect still refines section state
after hydration and hash changes (`ReadingNav.tsx:24–54`), but it no longer
creates a subroute-wide `Start` flash or a wrong no-JavaScript current marker.

The route scan observed exactly these initial current labels:

| Route | Initial current link | Skip link / target |
| --- | --- | --- |
| `/` | `Start` | `Skip to the first reading stop` → `#stop-60-90` |
| `/explore` | `Explore · receipt` | `Skip to the detailed receipt` → `#deep-receipt` |
| `/lab` | `Lab · no results` | `Skip to the research question` → `#lab` |
| `/sources` | `Sources` | `Skip to the sources` → `#sources` |

The offline assertions for this exact contract are also in
`site/tests/rendered-html.test.mjs:139–161`.

### 3. Skip targets and Explore target — PASS statically; focus/scroll QA remains

The home skip link targets the first stop (`site/app/HomeEssay.tsx:31–32`),
and all three home stop sections have `tabIndex={-1}`
(`HomeEssay.tsx:75–81,106–112,186–192`). The focus style is explicit for
these programmatic targets (`site/app/globals.css:26–35`).

Subroutes now point to their actual first named sections, with Explore pointing
to the first deep receipt rather than bypassing it
(`site/app/ReferenceRoutes.tsx:44–48,67–70`). The deep receipt, Lab, and
Sources targets are focusable sections (`site/app/DeepReceipt.tsx:4–7` and
`site/app/ReferenceRoutes.tsx:331–332,446–447`). The rendered test checks that
the resolved skip target has `tabindex="-1"`
(`rendered-html.test.mjs:151–157`).

### 4. Native Popover semantics and unsupported fallback — PASS statically;
manual browser/AT gate remains

The term component now has the expected nonmodal native shape:

- A button trigger with a stable target, toggle action, and accessible label
  (`site/app/Term.tsx:60–72`).
- A server-rendered `popover="auto"` region with stable label and description
  references (`Term.tsx:73–82`), plus definition, example, and explicit
  “What it does not mean” boundary text (`Term.tsx:83–100`). The old dialog,
  modal, and client-only conditional path are absent.
- Explicit close returns focus to the initiating trigger
  (`Term.tsx:83–94`). Native Escape/light-dismiss closure is covered by scoped
  `beforetoggle`/`toggle` listeners that remember whether focus was inside the
  closing panel and restore only that trigger (`Term.tsx:34–58`). This avoids a
  competing document-wide Escape listener and preserves nonmodal background
  interaction.
- Anchor positioning is used when supported, with block/inline flip
  fallbacks (`site/app/globals.css:548–557`). The fixed safe-area placement and
  bounded internal scroll remain the baseline (`globals.css:519–545,792–801`).
- In a UA that does not support `:popover-open`, the panel is deliberately
  normal-flow, visible, unbounded, and its close control is hidden
  (`globals.css:559–570`). This is the no-JavaScript/unsupported-UA fallback:
  definitions are available as ordinary text even when the trigger cannot
  toggle a native popover.
- The standalone exporter carries the same focus-return behavior in its inline
  script (`output/v15_2/standalone/index.html:893–906`), so the exported file
  does not depend on the application runtime for this enhancement.

Static term counts in the standalone artifacts are consistent with the source:
`index.html` has 2 popovers/definitions/examples/boundaries, `lab.html` has 6,
and `sources.html` has 8; `explore.html` has no term component. The rendered
HTML test checks the target/ARIA shape and the expanded definition text
(`rendered-html.test.mjs:171–194`).

**Manual residual:** the source proves markup and event wiring, not the UA
behavior. Test native Popover support, Escape/light dismiss, focus return,
second-trigger behavior, accessible-tree announcement, and the fallback in
the selected Chromium/Safari/Firefox matrix. Treat this as a P1 release gate
until the browser/AT checklist below is recorded. A partial UA that recognizes
`:popover-open` but does not implement the declarative invoker also needs an
explicit support-baseline decision; the static `@supports` branch alone cannot
prove every partial implementation.

### 5. Expanded definitions and print/static expansion — PASS statically;
PDF QA remains

All term panels and their complete definition/example/boundary are present in
server HTML (`site/app/Term.tsx:73–100`; the offline rendered test checks this
at `rendered-html.test.mjs:189–194`). The print stylesheet forces closed native
popover content into normal flow, removes the close control, expands closed
`details` records, and exposes table overflow
(`site/app/globals.css:823–891`, especially `828`, `842–861`, and `875–879`).

The static behavior is therefore correct in intent: supported native-Popover
UAs disclose on demand, unsupported UAs receive ordinary-flow definitions,
and print receives the definitions even when panels/details start closed.

**Manual residual:** render all four routes to A4 PDF with terms closed and
open. Confirm each definition appears once, in source order, with no hidden
close control, clipped table, rail, route-card chrome, or awkward page break.

### 6. Dead home renderer — PASS

`site/app/page.tsx:9–15` dispatches the home mode only to `HomeEssay` and routes
the other modes to `PatternRecognitionPage` from `ReferenceRoutes`. The current
`ReferenceRoutes.tsx` exports only `PageMode = "explore" | "lab" | "sources"`
and the corresponding component (`ReferenceRoutes.tsx:37–44,489–496`); the
former `isHome` branch/default export and old `#essay`/`#takeaway` targets are
absent. This removes the stale v15.1 renderer that could drift from the v15.2
route contract.

### 7. Standalone self-containment — PASS statically

The manifest declares four v15.2 files and their byte sizes
(`output/v15_2/standalone/STANDALONE_ROUTES.json:1–24`) with status
`LOCAL_OWNER_REVIEW_NO_RESULTS`. The representative `index.html` begins with
the route/status marker (`index.html:1`), inlines the entire stylesheet and
metadata before the body (`index.html:1–892`), includes the complete route
body and no asset `src` outside `data:` URIs (`index.html:892`), and ends with
the inline Popover focus-return script (`index.html:893–907`). The other three
files have the same inline style/script shape and contain no local `src` or
stylesheet dependencies; their first-line route/status comments are visible at
`explore.html:1`, `lab.html:1`, and `sources.html:1`.

Cross-route links are relative HTML navigation (`index.html`, `explore.html`,
`lab.html`, `sources.html`), not runtime imports. `sources.html` retains
external scholarly hyperlinks as content links; no external stylesheet,
script, image, font, or application endpoint is required to render the file.

### 8. No-results boundary — PASS

The home masthead states `No model selected · no study run · no empirical
result · not published` (`site/app/HomeEssay.tsx:43–50`); the home stop and
closing copy retain fictional/no-result boundaries (`HomeEssay.tsx:84,
177,324–325`). Subpages repeat the no-results status in the masthead
(`site/app/ReferenceRoutes.tsx:59–64`), while Lab explicitly says no model,
no run, and no result (`ReferenceRoutes.tsx:331–347`). The Lab's corrected
protocol language now keeps the fixed `M=75` safety membership/hash and
`-0.05` lower-bound margin explicit, with validity/output filtering prohibited
and interval/coverage/paired-invalid receipts still open
(`ReferenceRoutes.tsx:378–405`). Its result ladder separately preserves
direct-code/field-only shortcuts, surface or semantic-audit failure, unstable
results, noise fragility/non-transferability, and stopped/quarantined runs
(`ReferenceRoutes.tsx:415–430`). The rendered test asserts these new Lab
boundaries (`site/tests/rendered-html.test.mjs:98–127`), and the regenerated
standalone Lab contains them (`output/v15_2/standalone/lab.html:892`).
Explore’s receipt is fictional and not a result (`site/app/DeepReceipt.tsx:6–19,80–87`),
and the case card calls Signal Foundry an offline contract fixture, not
validation (`ReferenceRoutes.tsx:303–319`). The standalone manifest and route
comments retain `LOCAL_OWNER_REVIEW_NO_RESULTS` (`STANDALONE_ROUTES.json:1–4`;
`index.html:1`, `explore.html:1`, `lab.html:1`, `sources.html:1`).

## Remaining P0 / P1 / P2

### P0 — none found statically

No source-level P0 was found in this acceptance lane. Every route discloses
conceptual/local/no-result status, the historical v13 raster remains captioned
as historical and not the v15.2 system map (`site/app/HomeEssay.tsx:272–305`),
and the standalone files are self-contained for rendering. This does not waive
the manual release gates below.

### P1 — manual release gates, no confirmed static implementation failure

1. **Native Popover and AT matrix:** verify actual Escape/light-dismiss focus
   restoration to the initiating trigger, accessible name/description,
   second-trigger behavior, nonmodal background interaction, and unsupported or
   partial-UA fallback (`Term.tsx:34–58`, `globals.css:548–570`).
2. **Responsive collision/scroll and skip-target interaction:** verify the
   anchor/fixed placement at all requested widths, 200% zoom, sticky-rail
   offsets, and keyboard traversal after skip activation. Static CSS covers the
   mechanisms (`globals.css:696–717,719–801`), but no browser measured them.
3. **Timed route contract:** run cold-reader passes to confirm the revised
   four/nine-minute labels and first-stop 60–90-second experience. The source
   and text proxy align, but timing is not proven by static HTML
   (`HomeEssay.tsx:51–70,98–101,177–181,315–318`).

### P2 — manual quality checks

1. Render print/PDF for all four routes, including closed/open terms and closed
   `details` (`globals.css:823–891`).
2. Inspect forced-colors and grayscale/reduced-motion behavior, confirming that
   microvisual states, relation states, no-result status, and boundaries remain
   text-readable (`globals.css:808–821`).
3. Capture current 320/390/720/820/900/1440px renders and verify tablet route
   cards, mobile rail discoverability, table overflow, v13 image caption, and
   the three approved microvisuals. These are source-supported but not
   pixel-verified.
4. Normalize or explicitly justify `aria-label` on generic containers. The
   labels on the relation-state grid, origin-observation row, Explore decision
   contrast, and Lab metrics are not guaranteed accessible names without a
   grouping role or labelled section (`site/app/HomeEssay.tsx:118`,
   `site/app/MicroVisual.tsx:9`, `site/app/ReferenceRoutes.tsx:244,367`). The
   visible headings/text carry the meaning today, so this is not a P0/P1
   blocker, but it remains a durable semantics cleanup.

## Precise manual browser / AT checklist

Record browser, version, OS, viewport, zoom, input method, and result for each
item. Repeat with JavaScript disabled where stated. Do not treat source regexes
or SSR presence as a substitute for the observations.

### Keyboard and route semantics

- [ ] At `/`, `/explore`, `/lab`, and `/sources`, load with JavaScript
      disabled. Confirm the initial `aria-current="location"` is respectively
      Start, Explore · receipt, Lab · no results, and Sources.
- [ ] At 390px and 820px, Tab to the skip link, activate it, and confirm focus
      lands on the named `tabindex="-1"` section; the sticky rail does not cover
      the heading; the next Tab enters the section in reading order; Shift+Tab
      returns predictably; and the URL fragment is preserved.
- [ ] Repeat the preceding check with JavaScript enabled at 320, 390, 720,
      820, 900, and 1440px. Test Explore's `Skip to the detailed receipt`
      specifically: focus must land on `#deep-receipt`, before `#map`.
- [ ] Follow every home route card and rail stop. Confirm each visible label
      matches the selected contract and that the stop box is the boundary the
      reader reaches, not merely a heading at the start of a longer section.
- [ ] At narrow widths, keyboard-scroll the horizontal reading rail and verify
      `Cases`, `Lab · no results`, and `Sources` are discoverable and reachable.

### Native Popover and fallback

- [ ] In a current supported Chromium, Safari, and Firefox build, tab to every
      term trigger on `/`, `/lab`, and `/sources`. Enter and Space must open the
      nonmodal explanation without an inert background or modal focus trap.
- [ ] Verify the trigger accessible name contains the visible term; the opened
      region is named by that term and described by its definition, example, and
      “What it does not mean” boundary in the accessibility tree.
- [ ] With focus in the panel, press Escape and confirm focus returns to the
      exact initiating trigger. Click the explicit close button and confirm the
      same. Click outside from both the trigger and panel and verify deterministic
      light dismissal without making unrelated content inert.
- [ ] Open term A, then term B. Confirm A closes once, B remains usable, focus
      does not jump to the wrong trigger, and a second Escape does not close
      unrelated content.
- [ ] Repeat at triggers near the top, middle, and bottom of long content. At
      1440, 1024, 900, 820, 720, 390, and 320px, and at 200% text zoom, confirm
      the panel stays inside the safe viewport, flips/clamps when needed, has
      internal scrolling for long text, does not cause document horizontal
      scrolling, and does not cover the only sentence/context it explains.
- [ ] With JavaScript disabled in a supported native-Popover UA, verify the
      server-rendered explanation remains discoverable and usable. In a
      deliberately unsupported or partial-Popover UA, verify the definition,
      example, and boundary are ordinary visible text and the no-op trigger does
      not hide the only explanation.
- [ ] Use VoiceOver + Safari, NVDA + Chrome, NVDA + Firefox (or an equivalent
      Chromium AT path), and one mobile screen reader. Record whether region
      announcement, heading navigation, close naming, and focus return match the
      static contract.

### No-results, visuals, responsive, and print

- [ ] On every route, confirm the visible status says no model/no study/no
      empirical result/not published as applicable; ensure fictional examples,
      Signal Foundry's `HOLD / DEFER`, and the v13 historical boundary cannot be
      mistaken for findings or authorization.
- [ ] At 320/390/720/820/900/1440px, inspect route-card density, sticky rail,
      receipt/table overflow regions, microvisual text equivalents, and the
      historical-image caption. Confirm no body `scrollWidth` overflow except
      deliberately focusable table wrappers.
- [ ] In forced-colors mode and grayscale, confirm every relation/status state
      remains understandable from text and labels, not color or shape alone.
- [ ] With reduced motion enabled, confirm smooth scrolling/transitions do not
      become disorienting and focus remains visible.
- [ ] Print `/`, `/explore`, `/lab`, and `/sources` to A4 with terms/details
      initially closed and with a term open. Definitions must appear exactly
      once, controls/rail/route cards must be absent, tables must be readable,
      and page breaks must not clip the receipt, v13 boundary, or no-results
      status.

### Timed owner-reader checks

- [ ] Run at least five cold-reader passes with no explanation beyond the title
      and route cards. At the 60–90-second stop, readers should recover
      `09 / 01 / 00 / HOLD` and understand that HOLD is not rejection.
- [ ] At the about-four-minute stop, at least 4/5 readers should name the three
      questions, correction rule, permission boundary, and human next step.
- [ ] At the about-nine-minute stop, at least 4/5 readers should state the two
      loops, use/skip boundary, objections, narrow research question, and
      no-results status. Record actual times; change labels if they do not match
      the observed route.

## Final gate

Static acceptance is **PASS**. Overall release status is **PASS WITH MANUAL QA
RESIDUALS** because the only unclosed items are browser/AT/pixel/PDF and
cold-reader observations that cannot be established from source, SSR, or
standalone HTML. No implementation edit was made during this review.
