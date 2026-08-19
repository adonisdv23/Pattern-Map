# Pattern Map v16 site QA report

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
PASS exact first-screen headline/standfirst and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS external Markdown links preserve parenthesized URLs and safe anchor attributes
PASS standalone export exists

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names for all 9 routes
PASS no-script essential meaning is present in static HTML
PASS Apply vocabulary and route/stop/learning vocabulary
PASS reduced-motion, forced-colors, 200%-friendly reflow, and print hooks
PASS no-script simulation
PASS synthetic Echo-removal simulation
PASS historical diagram label/current-topology distinction and hash
PASS standalone HTML is self-contained for direct local opening
NOTE structural QA is not reader comprehension or effectiveness evidence
```

The site package has a dependency-free, deterministic `site/package-lock.json`. Transient `site/dist/` output remains ignored; the committed direct-open export is under `site/exports/standalone/` as requested.

Primary integration review found that the first site commit allowed emphasis
parsing to rewrite `_blank` inside generated anchor markup and truncated a DOI
containing parentheses. The renderer now protects completed inline tokens,
supports balanced parentheses in link destinations, and has regression checks
across the Sources route and standalone export. No malformed anchor from the
pre-integration candidate was pushed to the canonical remote branch.

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

The static audit checks every route for `lang="en"`, one `main` landmark, a skip link, a labeled principal nav, one level-one heading with no heading jumps, accessible names for links/buttons/summaries, and `alt` on images. The skip target is `main#main` with `tabindex="-1"` so the target is programmatically focusable.

No-script simulation strips script blocks from the home, map, and apply HTML and retains the first-screen problem, six-family content, and implementation choices. The standalone export embeds CSS and JavaScript and references only the repository-local historical image path; it does not require a deployed server.

The stylesheet contains explicit reduced-motion, forced-colors, 200% reflow, and print rules. The print rules remove site chrome and preserve route content. A separate browser print-media capture was attempted but the browser security policy declined the CDP permission; that blocked capture is recorded as a residual, not represented as a pass.

## Keyboard and focus evidence

The final browser DOM exposes this initial focus order: skip link, wordmark, the three principal links, the `More +` button, secondary route links, and the three principal door cards. The skip target has `tabindex="-1"`. Activating `More +` sets `aria-expanded="true"`, opens the secondary navigation, and moves focus to `Examples`.

The in-app Browser automation surface did not advance focus reliably after synthetic `Tab` keypresses, even when the focused element was established through the supported DOM interaction path. Therefore this is a partial keyboard QA result: static order, focus target, accessible names, and menu focus handoff pass; end-to-end physical Tab traversal remains unverified in this automation surface. No claim of reader effectiveness is made.

## Echo-removal and historical checks

- Echo-removal simulation: passes for Read / Explore / Apply vocabulary and application state vocabulary after removing Echo and origin-accounting text.
- Historical asset SHA-256: `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.
- Standalone HTML contains the local historical image path `../../../assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png` and no external stylesheet or script dependency.

## Residuals

1. Browser-level physical Tab traversal could not be completed because synthetic Tab events did not advance focus in the in-app automation surface. The site still has a semantic tab order and explicit focus styling; manual owner review should confirm the physical keyboard path.
2. The browser security policy declined the CDP permission needed to emulate print media. Static print hooks and no-script checks pass; a manual print-preview check remains open.
3. The existing targeted source links are presented as source pointers, not as newly reverified evidence. No external source read was performed for this lane.
4. QA evidence here is structural and visual implementation evidence only. It is not reader comprehension, effectiveness, model, study, participant, or research evidence.
