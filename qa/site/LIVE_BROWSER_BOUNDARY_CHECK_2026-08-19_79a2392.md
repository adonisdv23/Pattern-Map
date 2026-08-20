# Pattern Map v16 live-browser boundary check

Status: **PASS FOR LIVE POINTER/FOCUS LOGIC; MANUAL A13 GATES REMAIN OPEN**

Review date: 2026-08-19

Repository head at review:
`79a239209f00a6efdff5bcb57bc087aae0ace66d`

Canonical site/content checkpoint:
`2a54b24ec01707bb2a73032ab3f662cd995669ae`

The commits after the canonical checkpoint contain QA, handoff, and draft-PR
metadata; they do not change `site/**`, the manuscript, framework, cases, or
research source. Immediately after the browser session, `npm run build` and
`npm run check` rebuilt the nine routes and standalone export and passed every
site assertion.

## Evidence boundary

This check used the in-app browser against the loopback-only local site at
`http://127.0.0.1:4173/`. It exercised ordinary navigation, pointer activation,
focus handoff, Escape behavior, Map state changes, live-region text, disclosure
state, and computed visible-focus styles. It did not deploy, publish, transmit
project data, call a provider or model, run a study, or contact a participant.

The browser surface did not advance end-to-end Tab traversal or native default
activation reliably. A request to use the browser's supported developer
capability for exact responsive viewport, print-media, and accessibility-tree
inspection was declined by the browser security layer. That decision was not
bypassed and no alternate browser-control surface was used.

Accordingly, this report is live implementation evidence, not a physical
keyboard result, supported screen-reader result, browser print-preview result,
reader-comprehension result, or accessibility certification.

## Live route results

At the available 1280×720 viewport, all nine routes were opened sequentially:

1. Home
2. Read
3. Map
4. Apply
5. Examples
6. Boundaries
7. Sources
8. Research
9. History

For every route:

- `innerWidth` and document `scrollWidth` were both 1280;
- exactly one `main` and one `h1` were present;
- the three principal links were Read the idea / Explore the map / Apply it;
- the skip link targeted `#main`;
- the route title and h1 matched the intended route;
- every non-Home route exposed the correct `aria-current="page"` link; and
- the browser console contained no error-level entries after the route pass.

Home intentionally has no principal-route `aria-current` item because Home is
represented by the Pattern Map wordmark rather than a fourth principal door.

## More-menu focus and Escape behavior

Pointer activation of `More +` produced all of the intended observable state:

- `aria-expanded` changed from `false` to `true`;
- the secondary navigation changed from `display: none` to `display: block`;
- focus moved to the first secondary route, `Examples`; and
- the route remained otherwise unchanged.

Pressing Escape while `Examples` held focus then produced:

- `aria-expanded="false"`;
- the secondary navigation returned to `display: none`; and
- focus returned to the `More +` button.

This verifies the implemented focus handoff and Escape-return path. It does not
substitute for starting at the browser chrome and traversing the full document
with a physical keyboard.

## Map interaction and visible focus

Before interaction, the Map showed six visible family cards, fourteen
disclosures, and the live status:

> All six families are visible. Focus controls add emphasis; they never hide
> essential meaning.

Activating the first family focus control produced:

- F1 `aria-pressed="true"` and F2–F6 `aria-pressed="false"`;
- all six family cards remained visible;
- the live status changed to `F1 is focused. The other families remain visible
  for comparison.`;
- focus remained on the activated family button; and
- the computed focus treatment was a 3px dark outline plus a 6px light outer
  ring.

Activating Show all reset every family button to `aria-pressed="false"`, kept
all six cards visible, restored the all-families live message, and left focus
on Show all.

Pointer activation of the first `Implementation detail` summary opened the
disclosure and exposed its specification, technical mechanism, and
implementation-level content. Focus remained on the summary with the same
dual focus treatment. A second pointer activation closed it.

## Keyboard and browser-capability boundary

The following attempts did not produce a reliable native-keyboard result in
this automation surface:

- Tab from the document body did not advance focus;
- Tab after an interactable element had focus did not advance to the next
  element; and
- Enter sent through the available synthetic key paths did not consistently
  invoke the native default action for button/summary controls.

Because pointer activation and scripted state changes work while default
keyboard traversal does not, the evidence supports the existing conclusion
that the automation surface is the limitation; it does not prove that a
physical browser keyboard path passes or fails.

The browser security layer declined the raw developer capability requested for
responsive viewport emulation, print-media capture, and browser accessibility-
tree inspection. The declined action did not alter the page: the viewport
remained 1280×720, More remained closed, and the page stayed on the loopback
site. No workaround was attempted.

## Acceptance effect

- A02/A06 receive additional live-browser support at the desktop viewport.
- A13 receives stronger evidence for focus styling, state visibility, pointer
  interaction, More-menu handoff, Escape return, Map live-region updates, and
  route integrity.
- A13 remains **PARTIAL — OWNER CONFIRMATION REQUIRED** for physical Tab/
  keyboard traversal, a supported screen reader, and browser print preview.
- A01/A04/A05 remain owner/mentor or observed-reader judgments; this browser
  check makes no comprehension, voice, or reading-time claim.

No canonical source correction was indicated by this bounded live-browser
pass.
