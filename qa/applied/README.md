# Applied-framework QA

Status: focused structural and procedure QA, not effectiveness evidence.

Run from the repository root:

    python3 qa/applied/validate_framework.py

The check validates:

- JSON parsing and the local six-family schema contract;
- exactly six family IDs and names;
- Markdown/JSON family alignment;
- required builder and agent artifacts;
- cross-file boundary language;
- bounded-case disclaimers and Signal Foundry containment;
- the fixture-scoped Signal Foundry cost/stop/resume envelope;
- canonical route, stop, and learning vocabulary across entry-point artifacts;
- Quickstart outcome close-out and preflight group-status observability;
- bounded v13 process/workflow/model-path continuity without hierarchy;
- receipt fixtures through the documented preflight and stop rules.

These checks do not show that the framework improves decisions, that any case
works in production, or that any research result exists. They show only that
the first-wave artifacts are structurally present and preserve selected
guardrails.
