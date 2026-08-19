# Quality assurance

QA evidence is grouped by editorial fidelity, applied usefulness, research
boundaries, site behavior, and visual integrity. Machine checks and advisory
reviews must state exactly what they establish and what remains manual.

## Scheduled gate checks

- A07/A08: inspect framework completeness and agent executability after the
  applied advisory review, then recheck the rendered routes after site
  integration.
- A09: inspect every Signal Foundry mention and link after site integration;
  no surface may turn the bounded illustration into implementation or
  validation evidence.
- Record the integrated commit, evidence, residual limitation, and controlled
  disposition. A manuscript-only or scaffold-only snapshot cannot close these
  gates.

## Current rendered evidence

- `qa/site/SITE_QA_REPORT.md` records the nine-route build, semantic/static
  checks, no-script and Echo-removal simulations, link integrity, and explicit
  manual residuals.
- `qa/visual/VISUAL_QA_REPORT.md` records responsive browser captures,
  code-native visual behavior, the historical-map label, and PDF inspection.
- This evidence establishes implementation structure and rendering only. It
  does not establish comprehension, persuasion, effectiveness, live-agent
  compliance, or a research result.
- Physical keyboard traversal and a human print-preview pass remain open
  because the available automation surface could not provide reliable Tab or
  print-media emulation evidence.
