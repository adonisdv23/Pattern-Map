# Quality assurance

QA evidence is grouped by editorial fidelity, applied usefulness, research
boundaries, site behavior, and visual integrity. Machine checks and advisory
reviews must state exactly what they establish and what remains manual.

Run the complete clone-contained verification sequence from the repository
root with:

```sh
qa/run_owner_review_checks.sh
```

When the exact owner-local v15.2 ZIP is available, add its separately verified
container check with `--source-zip PATH`. Omitting that option does not weaken
the complete extracted-accession check; it only preserves the documented
boundary that the 41,436,496-byte distribution container is outside Git.

## Completed artifact-gate rechecks

- A07/A08: exact post-site and final-regression reviews pass for framework
  completeness, observable artifact behavior, and rendered-route fidelity at
  `8aa5f94` and `2a54b24`.
- A09: every rendered Signal Foundry mention and link was inspected at
  `2a54b24`; the case remains fixture-only, read-only, and not validation.
- These are artifact gates. They do not establish live-agent compliance,
  product behavior, reader comprehension, or framework effectiveness.

## Current implementation and rendered evidence

- `qa/site/RENDERED_VERIFICATION_ROUND_2_2026-08-20.md` is the current report.
  It records the round-two evidence-integrity audit — including two named
  checkpoints that resolved to nothing — the rendered defects that source
  review could not see, and the measured sweep that replaced the round-one
  assertions.
- `qa/interaction/evidence/` holds that measurement: 240 records across ten
  routes and twelve viewports, summarised in `RENDERED_SWEEP_SUMMARY.md`, which
  is regenerated from the evidence by `qa/interaction/summarize_sweep.py` and
  verifiable with its `--check` flag.
- `qa/interaction/layout-probe.js`, `enhancement-probe.js`, and
  `layout-sweep-driver.js` are the instruments. They are local QA tools, never
  part of a committed build, and each states in its own report what it does not
  establish.
- `qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20.md` is the round-one response.
  Read it alongside the round-two report, which corrects three of its claims. It records the ten-route Guided experience,
  planning-only Apply semantics, line-free relationship Map, terminology
  helpers, 390/821/1024/default live-browser observations, and executable
  regression contracts.
- `qa/site/SITE_POLISH_QA.md`,
  `qa/visual/VISUAL_EXPERIENCE_REVISION_REPORT.md`, and the routed-site PNG
  matrix are preserved evidence for the earlier `a319794` design checkpoint.
  They are superseded for current Map and Apply semantics and are labeled as
  such; they must not be represented as current screenshots.
- `qa/visual/README.md` is the evidence index. It identifies the regenerated
  current PDF renders and distinguishes current source/live-browser evidence
  from historical routed-site captures.
- `qa/site/SITE_QA_REPORT.md` records the earlier nine-route build, semantic/static
  checks, no-script and Echo-removal simulations, link integrity, and explicit
  manual residuals.
- `qa/visual/VISUAL_QA_REPORT.md` records responsive browser captures,
  code-native visual behavior, the historical-map label, and PDF inspection.
- `qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md` records the
  current-head live route, More/Escape focus, Map state/live-region, visible-
  focus, and disclosure checks, together with the exact browser-permission and
  synthetic-keyboard limits that keep manual A13 gates open.
- This evidence establishes implementation structure and rendering only. It
  does not establish comprehension, persuasion, effectiveness, live-agent
  compliance, or a research result.
- Physical keyboard traversal, a supported screen-reader pass, real 200%
  browser/OS zoom, and a human print-preview pass remain open because the
  available automation surface could not establish those behaviors reliably.
