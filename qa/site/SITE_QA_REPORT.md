# Pattern Map v16 site QA report

> **Historical implementation notice.** This report covers the earlier
> nine-route site. The current ten-route, planning-only Apply and line-free Map
> implementation is recorded in
> `qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20.md` and
> `qa/site/RENDERED_VERIFICATION_ROUND_2_2026-08-20.md`.

Status: local owner-review candidate

This report records implementation and artifact QA only. It is not reader-comprehension, persuasion, behavioral-effectiveness, model-quality, empirical, participant, or research evidence.

## Scope and base

- Branch: `codex/pattern-map-v16-site`
- Required base: `7a2ed72bf9bdb924bdf96236fa22ef8056979ebb`
- Verified branch HEAD before editing: exact required base.
- Implementation clone: `/Users/gpt/Pattern-Map` (writable isolated fallback); the managed worktree remained untouched.
- Exclusive writes stayed within `site/**`, `assets/diagrams/**`, and `qa/site/**` / `qa/visual/**`.
- No hosting API, deployment, production URL, publication, GitHub Release, merge, study/provider/model/participant run, dataset acquisition, preregistration, outreach, or spend was used.

## Focused checks

All of the following pass on the final generated site:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK

python3 qa/editorial/validate_content_interface.py
PASS immutable owner-intent checkpoint and content-interface JSON
PASS exact three-door, secondary-route, and source manifests
PASS locked six-family identity, questions, boundaries, and invariants
PASS human-problem first screen, examples, and late Echo placement
PASS claim, no-script, visual, output, and external-action obligations

cd site && npm run build
Built 9 routes to site/dist
Built standalone export to site/exports/standalone/pattern-map-v16.html

cd site && npm run check
PASS routes: 9
PASS exact first-screen framing, non-result boundary, and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS external Markdown links preserve parenthesized URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragment integrity
PASS standalone heading hierarchy and unique IDs
PASS responsive/no-script navigation and active-route semantics
PASS normal-text and dual-focus contrast thresholds
PASS standalone export exists

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names for all 9 routes
PASS no-script essential meaning is present in static HTML
PASS Apply vocabulary and route/stop/learning vocabulary
PASS reduced-motion, forced-colors, 200%-friendly reflow, and print hooks
PASS no-script simulation
PASS synthetic Echo-removal simulation
PASS historical diagram label/current-topology distinction and hash
PASS standalone HTML is self-contained with one h1, unique IDs, and named route sections
NOTE structural QA is not reader comprehension or effectiveness evidence
```

The site package has a dependency-free, deterministic `site/package-lock.json`. Transient `site/dist/` output remains ignored; the committed direct-open export is under `site/exports/standalone/` as requested.

Primary integration review found that the first site commit allowed emphasis
parsing to rewrite `_blank` inside generated anchor markup and truncated a DOI
containing parentheses. The renderer now protects completed inline tokens,
supports balanced parentheses in link destinations, and has regression checks
across the Sources route and standalone export. No malformed anchor from the
pre-integration candidate was pushed to the canonical remote branch.

The final builder/operator advisory then exposed two further blind spots:
single-underscore emphasis mutated visible machine-like state identifiers, and
unmapped local source links produced silent home fallbacks or dead standalone
fragments. The renderer now supports asterisk emphasis only, fails the build on
an unmapped local Markdown link, maps every current source reference to an
intentional route, and checks exact representative state/status tokens plus all
standalone fragments. Canonical framework and case wording was not changed to
accommodate either renderer defect.

## Content and route contract

The generated site includes:

- Exact frozen headline and standfirst on the first screen, followed in order by `Read the idea`, `Explore the map`, and `Apply it`.
- Secondary routes: `Examples`, `Boundaries`, `Sources`, `Research`, and `History`.
- Read route: cumulative 60-90-second entry, complete canonical essay, and distinct optional mentor cover note.
- Explore route: exact F1-F6 order, names, questions, accessible focus controls, current relationship view, glossary explanations, and static meaning when controls are closed or JavaScript is removed.
- Apply route: ordinary, lightweight, moderate, and advanced choices; operator path; agent Quickstart and deeper guide; templates; observable route, stop, and learning states.
- Examples route: specialist/peripheral candidate, velocity or expected absence with a baseline, and common-origin recurrence with independence `UNKNOWN`.
- Signal Foundry is labeled `ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION`.
- Echo is labeled and placed as `SEPARATE PROJECT - UNRUN - NO RESULTS`, subordinate and late; synthetic removal leaves all three principal routes coherent.
- History route preserves the recovered v13 image byte-for-byte under `assets/diagrams/` and labels it `Historical v13 origin — not the current v16 topology.` The current map is explicitly the code-native relationship view.

## Semantic and static accessibility audit

The static audit checks every route for `lang="en"`, one `main` landmark, a skip link, a labeled principal nav, one level-one heading with no heading jumps, accessible names for links/buttons/summaries, and `alt` on images. The skip target is `main#main` with `tabindex="-1"` so the target is programmatically focusable. The standalone export is additionally checked for one level-one heading, unique prefixed IDs, named route sections, complete fragment targets, and no heading-level jumps.

No-script simulation strips script blocks from the home, map, and apply HTML and retains the first-screen problem, six-family content, and implementation choices. A `noscript` rule exposes the secondary routes when the disclosure script is unavailable. The standalone export embeds CSS and JavaScript and references only the repository-local historical image path; it does not require a deployed server.

At narrow widths the header wraps onto two rows and keeps all three principal links visible; `More` discloses only the five secondary routes. The active route carries `aria-current="page"` and a non-color-only visual treatment. Normal-text tokens used for muted and family labels pass a computed 4.5:1 contrast threshold against the paper surface. The dual focus indicator supplies a dark ring for light surfaces and a light outer ring for dark surfaces; both checked pairs exceed 3:1.

The stylesheet contains explicit reduced-motion, forced-colors, 200% reflow, and print rules. The print rules remove site chrome and preserve route content. A separate browser print-media capture was attempted but the browser security policy declined the CDP permission; that blocked capture is recorded as a residual, not represented as a pass.

## Keyboard and focus evidence

The final browser DOM exposes this initial focus order: skip link, wordmark, the three principal links, the `More +` button, secondary route links, and the three principal door cards. The skip target has `tabindex="-1"`. Activating `More +` sets `aria-expanded="true"`, opens the secondary navigation, and moves focus to `Examples`.

The in-app Browser automation surface did not advance focus reliably after synthetic `Tab` keypresses, even when the focused element was established through the supported DOM interaction path. Therefore this is a partial keyboard QA result: static order, focus target, accessible names, and menu focus handoff pass; end-to-end physical Tab traversal remains unverified in this automation surface. No claim of reader effectiveness is made.

## Echo-removal and historical checks

- Echo-removal simulation: passes for Read / Explore / Apply vocabulary and application state vocabulary after removing Echo and origin-accounting text.
- Historical asset SHA-256: `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.
- Standalone HTML contains the local historical image path `../../../assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png` and no external stylesheet or script dependency.

## Residuals

The post-revision advisory reports correctly found that the PNG captures
committed at their exact target still predated the narrow-navigation and Map
copy corrections. The primary integration pass rebuilt the local site and
replaced those two evidence files. At 390×844, `innerWidth` and `scrollWidth`
were both 390 and Read / Explore / Apply / More were all visibly rendered. At
1440×1000, the refreshed Map showed the plain-language F1/F2 bridges, one route
`h1`, complete glossary content, and no horizontal overflow. These captures
support render freshness only; they are not comprehension or accessibility
results.

A later live-browser boundary check at repository head `79a2392` reopened all
nine routes at 1280×720, found one main/one h1 and no horizontal overflow or
browser-console errors, and re-exercised the More focus handoff/Escape return,
Map focus/reset live status, dual focus ring, and disclosure pointer behavior.
The same run again could not make synthetic Tab or native keyboard-default
activation advance reliably. The browser security layer declined the
developer capability needed for responsive emulation, print-media capture,
and browser accessibility-tree inspection, and that decision was not
bypassed. See
`qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md`.

1. Browser-level physical Tab traversal could not be completed because synthetic Tab events did not advance focus in the in-app automation surface. The site still has a semantic tab order and explicit focus styling; manual owner review should confirm the physical keyboard path.
2. The browser security policy declined the CDP permission needed to emulate print media. Static print hooks and no-script checks pass; a manual print-preview check remains open.
3. The existing targeted source links are presented as source pointers, not as newly reverified evidence. No external source read was performed for this lane.
4. QA evidence here is structural and visual implementation evidence only. It is not reader comprehension, effectiveness, model, study, participant, or research evidence.
