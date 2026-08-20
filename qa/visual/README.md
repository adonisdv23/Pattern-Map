# Visual QA evidence index

Status: **owner-review evidence; not reader, accessibility, or research results**

## Current polished-site evidence

Use these paths for the current v16 visual review:

- `screenshots-final-v16-polish/` — final routed-site viewport matrix from the
  polished build;
- `screenshots-final-v16-polish/interaction-states/` — visible F1 focus,
  advanced/HOLD receipt, and corrected standalone-orientation states;
- `pdf-renders-final-v16-polish/` — six rendered pages from the secondary PDF
  companion; and
- `VISUAL_EXPERIENCE_REVISION_REPORT.md` — route-by-route interpretation and
  evidence boundaries.

The exact implementation/evidence checkpoint for the final state captures is
`a319794f5cf2d395c34e5af4935c9299f12dfd5c`.

## Stale pre-polish evidence warning

`screenshots/home-mobile-390x844.png` contains a large black lower region and
is **not a current-site capture**. It is retained as dated QA history because
it triggered the P0 visual review. Fresh exact-base and polished captures show
that the region was an incomplete/stale capture artifact rather than a current
CSS, overflow, document-height, or paint defect.

Do not use the stale image to judge the current owner-review site. Use
`screenshots-final-v16-polish/home-390x844.png`, which is fully painted and was
inspected alongside the 360x800 capture.

## Evidence boundary

Screenshots demonstrate rendered layout and visible states at named
viewports. They do not establish comprehension, persuasion, effectiveness,
physical-keyboard success, screen-reader support, or browser print behavior.
Those manual gates remain separate.
