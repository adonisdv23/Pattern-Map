# Research-boundary QA

Status: integrity and containment checks only; not a study or effectiveness
evaluation.

Run from the repository root:

    python3 qa/research/validate_research_boundaries.py

The validator checks current project separation, the exact EP unfavorable-
result taxonomy, the broader agenda's required flagship outcomes, explicit
unrun/no-results language, and future-protocol authorization boundaries. It
does not call a model, provider, participant, dataset, registry, publication,
or deployment channel.

For Markdown link QA, `research/the-echo-problem/preserved/v15.2/**` is an
immutable, byte-verified historical subset rather than an active-document
surface. Do not rewrite its historical relative links. Exclude that subtree
from the active-document link pass and check the current recovery routes in
`research/the-echo-problem/PRESERVED_V15_2_INDEX.md`; the index explains the
five unique historical targets that otherwise appear unresolved in the
focused subset.
