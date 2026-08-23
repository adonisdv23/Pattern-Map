# Visual QA evidence index

Status: **owner-review evidence; not reader, accessibility, or research results**

## Current correction evidence

Use these paths for the current v16 review:

- `pdf-renders-final-v16-polish/` — six rendered pages from the secondary PDF
  companion; and
- `../site/PRO_ROUND_2_CORRECTION_QA_2026-08-22_c889260.md` — exact-checkpoint
  source, contract, and live-browser evidence for the current ten-route site.

The corrected implementation checkpoint is
`c88926034cd75773dcc42d3842983c879dda5b58`.

## Superseded routed-site captures

`screenshots-final-v16-polish/`, its `interaction-states/` folder, and
`VISUAL_EXPERIENCE_REVISION_REPORT.md` are exact evidence for the earlier
`a319794f5cf2d395c34e5af4935c9299f12dfd5c` checkpoint. They remain useful
design history, but they are not current screenshots: the Map now uses
line-free relationship bands, Apply produces planning recommendations without
fabricating actual event states, and the site now has a Guided route and term
helpers.

No replacement routed-site screenshot binaries are claimed for `c889260`.
Current visual evidence consists of the regenerated PDF renders plus the live
viewport observations and executable layout/interaction contracts in the
current correction report.

## Stale pre-polish evidence warning

`screenshots/home-mobile-390x844.jpg` contains a large black lower region and
is **not a current-site capture**. It is retained as dated QA history because
it triggered the P0 visual review. Fresh exact-base and polished captures show
that the region was an incomplete/stale capture artifact rather than a current
CSS, overflow, document-height, or paint defect.

Do not use the stale image to judge the current owner-review site. The polished
folder contains a fully painted replacement for its own historical checkpoint;
the current correction report contains the later 390-pixel live-browser
observation.

## Evidence boundary

Screenshots demonstrate rendered layout and visible states at named
viewports. They do not establish comprehension, persuasion, effectiveness,
physical-keyboard success, screen-reader support, or browser print behavior.
Those manual gates remain separate.
