# Research-boundary QA

Status: integrity and containment checks only; not a study or effectiveness
evaluation.

Run from the repository root:

    python3 qa/research/validate_research_boundaries.py

The validator checks current project separation, the exact EP unfavorable-
result taxonomy, explicit unrun/no-results language, future-protocol
authorization boundaries, generic-diligence and mechanism-isolation sequencing,
the two resource estimands, decision-accuracy/accepted-error priority, the
narrow-wedge memo's no-selection contract, the dated targeted source route,
publication-time recheck language, and high-signal novelty/effectiveness/result
inflation phrases. It performs structural claim-boundary QA only. It does not
open the web, call a model, provider, participant, dataset, registry,
publication, or deployment channel.

The read-only public-source check behind the current route is recorded in
[CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md](CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md).
That report records opened primary/official landing pages, preprint versus
conference/official status, partial resolver checks, unresolved claims, and the
mandatory publication-time recheck. It is targeted wayfinding QA, not a
systematic review or research result.

The active EP v1.1 design checkpoint has its own provider-free deterministic
checks:

```sh
python3 -m unittest discover -s research/the-echo-problem/v1_1/harness -p 'test_*.py' -v
```

See [ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md](ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md)
for dispositions, exact real-tokenizer scope, and the boundary between local
implementation checks and unrun research.

For Markdown link QA, `research/the-echo-problem/preserved/v15.2/**` is an
immutable, byte-verified historical subset rather than an active-document
surface. Do not rewrite its historical relative links. Exclude that subtree
from the active-document link pass and check the current recovery routes in
`research/the-echo-problem/PRESERVED_V15_2_INDEX.md`; the index explains the
five unique historical targets that otherwise appear unresolved in the
focused subset.
