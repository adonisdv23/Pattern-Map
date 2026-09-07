# V15.1 integration ledger

Status: `COMPLETE · LOCAL OWNER REVIEW · NO EMPIRICAL RESULTS`

Base: sealed v15 owner-review checkpoint `82f87b1`

Integration branch: `codex/discrimination-layer-v15-1`

Integrator: Codex Sol, with parallel independent lanes for prior art, methods,
and editorial/site work.

## Owner-approved direction

- Release name: v15.1, a convergence and hardening release.
- Preserve v15 as the canonical base; no conceptual reset.
- Make unfamiliar terms understandable through plain-language prose first and
  optional interactive definitions second.
- Preserve and expand the compact glossary.
- Add small explanatory visuals only where they materially improve
  understanding.
- Establish explicit 60–90 second, five-minute, conceptual, and research paths.
- Keep the study unrun and the results surface empty.
- Consider `adonisdv23/Pattern-Map` as the future canonical repository, with no
  remote mutation until separately authorized.

## Lane dispositions

| Lane | Integrated commits | Accepted | Modified during orchestration | Deferred or rejected |
| --- | --- | --- | --- | --- |
| Reader contract and repository orientation | `6d0b236`, `a350b3f` | North-star takeaway, time budgets, plain-language-first rule, GitHub checkpoint contract | Repository structure made explicitly archival-first and no-write | Automatic unrelated-history merge; immediate push |
| Prior art | `b753650` | Pochampally et al. correlation-aware data-integration precedent; narrower correlation-versus-copy boundary | Integrated as an added boundary, not a new study arm | Systematic-review language; broad novelty recovery |
| Editorial and routed site | `0318527`, `ac345a1`, `ffbee18`, `1a4973f` | Four routes, short reading paths, expanded glossary, accessible term explanations, sample-size visual, historical v13 boundary | Replaced opaque first-fold labels; stabilized disclosure identifiers; corrected inherited text transforms; repaired hydration | Glossary-as-rescue for unclear prose; decorative visuals for every term |
| Methods | `19eb36f`, `bea928f`, `ecdd7af` | Descriptive absolute count error and selected support-origin set precision/recall/exact match | Removed general evidence-ID diagnostics after construct review; limited origin-set checks to selected support evidence; defined empty and unknown cases | Any change to FC_cons, VOR, F0/F1/F2, denominators, or confirmatory interpretation |
| PDF and handoff | final convergence commit | Updated 20-page companion, owner packet, package map, QA receipt, and deterministic package builder | Retained the v15 manuscript filename as a compatibility path while identifying content as v15.1 | Treating the PDF as canonical accessible content |

## Important methods correction

The first diagnostic proposal treated all selected evidence IDs as though they
should be supporting citations. That was wrong: a report can be legitimately
used for assessment because it is neutral or refuting. Penalizing that report
would measure stance selection, not origin accounting.

The integrated diagnostics therefore inspect only selected reports whose
benchmark stance is `supports` when measuring support-origin recovery. Unknown
or contested support-only ground truth is unscored. Empty-set behavior is
explicit:

- precision is undefined when no support origin is selected;
- recall is zero when the reference set is nonempty and selection is empty;
- recall is undefined when both sets are empty; and
- exact set match remains meaningful.

The primary false-corroboration outcome and valid-origin safety outcome remain
unchanged.

## Plain-language acceptance

The following labels no longer appear as unexplained first-fold requirements:

| Technical term | Integrated first explanation |
| --- | --- |
| F0/F1/F2 | Three versions of the same evidence task: ordinary, rule-only, and rule-plus-supplied-origin-labels |
| T1 | A separate optional real-world check that cannot validate the main experiment |
| N=300 | 300 planned primary fictional test cases; a sample size, not a score or result |
| Provenance audit | An inspection of where material came from and how it changed |
| System runtime | Actual running software, rather than an illustration or protocol |
| Human disposition | A person’s recorded next step, such as hold, verify, accept, or reject |
| Negative-result commitment | A promise to preserve and report failure, no effect, harm, instability, or shortcuts as honestly as success |

Each high-friction term also has an interactive definition, example, and “what
it does not mean” boundary. The visible sentence remains understandable if the
interaction is never opened.

## Non-negotiable integration checks

- [x] The visible page is understandable without opening glossary interactions.
- [x] F0/F1/F2, T1, N=300, provenance audit, system runtime, disposition, and
  the negative-result commitment receive plain-language explanations.
- [x] The essential argument is a genuine route and approximately five minutes.
- [x] Explore, Lab, Sources, and the full glossary are directly reachable.
- [x] Research labels state that no model is selected, no study has run, and no
  result exists.
- [x] Secondary diagnostic additions do not change the primary estimand or
  safety gate.
- [x] Prior-art changes do not turn a targeted search into a systematic-review
  claim.
- [x] The v13 historical image and current worked-example image keep their
  bounded roles.
- [x] No deployment, GitHub push, dataset acquisition, or model/provider call
  occurred.

## Three QA loops

| Loop | Scope | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Evidence and methods | Pass after construct and empty-set corrections | 15 Python tests; parser fixtures; compilation; prior-art disposition |
| 2 | Editorial and information architecture | Pass after terminology, route, and first-fold revisions | Four production routes; seven rendered-HTML tests; lint/build pass |
| 3 | Adversarial reader, accessibility, packaging, and handoff | Pass after term typography and hydration repairs | Desktop/mobile browser checks; Escape/focus return; unique IDs; 20-page PDF inspection; deterministic package verification |

Full commands, limitations, and artifact hashes are recorded in
`reports/V15_1_FINAL_VALIDATION.md` and the embedded package manifest.

## Preserved boundaries

- The site and manuscript are conceptual surfaces; the Lab is an unrun
  protocol surface.
- The PDF is an untagged visual companion; semantic HTML and Markdown are
  canonical.
- The v13 diagram is a historical anchor, not the current topology.
- Generated images are illustrations, not evidence.
- The public GitHub repository was inspected read-only. No push, release,
  setting change, or deployment was performed.
- No external execution is authorized by this integration.
