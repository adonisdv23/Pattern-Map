# Research claim convergence QA — 2026-08-30

Status: **PASS FOR THE SCOPED RESEARCH-CLAIM LANE**

Review base: `0beee9add00593e77eb5aafa41fdc447c833e83c`

This is a structural claim-boundary and source-status record. It is not a
systematic review, novelty clearance, protocol, preregistration, study, or
effectiveness result. No provider, model, corpus, dataset, participant, sample,
paper, or run was selected, acquired, or authorized.

## 1. Scope

The review covered only:

- `manuscript/SOURCES_AND_RESEARCH_ROUTE.md`;
- `docs/CLAIMS_AND_SOURCE_LEDGER_V16.md`;
- `research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md`;
- `research/future-studies/DL_NARROW_WEDGE_DECISION_MEMO_V0_1.md`; and
- `qa/research/**`.

It did not modify the owner-intent checkpoint, essay, short version, framework,
site, Echo preserved or curated artifacts, archive, handoff, or assets.

## 2. Claim ceiling verified

The component areas have substantial established and active prior work. The
maximum current contribution is an **authored, proportional, human-governed
design/governance synthesis and testable agenda**. It is not a novel mechanism,
exhaustive taxonomy, validated method, effectiveness result, universal
architecture, or proof that the combined practices improve decisions.

The phrase **before generation** is now consistently bounded as a logical
responsibility boundary within iterative agent loops. It applies whenever an
iteration selects what may influence the next generation; it does not claim
that all discrimination happens once before the first model call or token.

## 3. Source-neighbor dispositions

The dated source verification is in
`qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md`. The route is
targeted, not systematic or exhaustive.

| Neighbor group | Disposition | Consequence for the v16 claim |
|---|---|---|
| Anthropic context engineering and ACE evolving playbooks | **Accepted as adjacent work** | Context selection, compaction, memory, progressive disclosure, and evolving context/playbooks are active prior work; v16 cannot claim to originate them. |
| GroupQA | **Accepted with revision** | In its tested setting, paraphrased recurrence can be more persuasive than distinct support. It supports separating recurrence from independent support, not a universal persuasion law. |
| NIST agent-evaluation probes | **Accepted with revision** | An ongoing official project shows active work on rubric grounding and audit trails. It is not a final standard or validation of v16. |
| LEDGER and Graph of Trace | **Accepted as direct overlap** | Claim-to-evidence graphs and execution-trace views make a new receipt/trace mechanism an indefensible center for Candidate A. |
| FACTS&EVIDENCE and appropriate-reliance HCI | **Accepted with revision** | Existing evidence views and mixed, task-bounded reliance interventions narrow Candidate A to a provisional fixed-answer interface question. |
| Over-Searching, BCAS, and S2G-RAG | **Accepted as constraints** | More retrieval can harm abstention or cost, and search depth is a resource allocation choice; adaptive stopping needs harm and budget guardrails. |
| DREAM, BrowseComp-Plus, and ReportLogic | **Accepted with revision** | Deep-research evaluation already separates research dimensions, retrieval from end-to-end effects, and report logic; v16 may propose component isolation, not an empty-field claim. |
| Candidate A as a new receipt, ledger, trace, or attribution mechanism | **Rejected** | The existing applied receipt may be rendered as a stimulus, but trace production or receipt novelty is not the research question. |
| Candidate B as the automatically preferred first study | **Deferred** | Expectedness, key/trace separation, cue leakage, and real-domain adjudication remain unresolved. |

## 4. Candidate containment

Candidate A is a **provisional appropriate-reliance interface** question. It is
fixed-answer only: candidate conditions receive the same answer, available
evidence, and evidence-access boundary. Eligible outcomes concern appropriate
acceptance, rejection, or correction, including false acceptance, unnecessary
correction, and reviewer burden. Generated-answer or decision accuracy is not
an eligible outcome. The compact six-family view is a composite interface
unless an authorized later design isolates its elements.

Candidate B remains a provisional orthogonal observation-boundary question. It
does not establish a settled missingness taxonomy. No sequencing recommendation
between A and B is made.

The unowned matched-budget protocol still contains the earlier `M-A`
influence-receipt shorthand. This review did not edit it. If Candidate A ever
advances, that protocol requires an explicitly authorized revision before it
can govern the narrower fixed-answer interface question.

## 5. Focused verification

All scoped checks passed on 2026-08-30:

- `python3 qa/research/validate_research_boundaries.py` — **PASS**, including
  project separation, claim ceiling, source route, Candidate A/B containment,
  and no-results/authorization boundaries;
- `python3 -m unittest discover -s qa/research -p 'test_*.py' -v` — **PASS**,
  7 tests;
- `python3 -m py_compile qa/research/validate_research_boundaries.py
  qa/research/test_research_claim_convergence.py` — **PASS**;
- direct `curl -L` status check of 15 current primary/official routes — **13
  resolved with HTTP 200**; both CHI DOI routes resolved to ACM and returned
  HTTP 403, retained as **PARTIAL / RECHECK AT PUBLICATION** rather than treated
  as a content or status failure;
- local Markdown target check across the seven owned research Markdown
  artifacts — **PASS**, 13 local targets existed;
- `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — **PASS**;
- `git diff --check` — **PASS**; and
- owned-path-only diff inspection — **PASS**.

## 6. Unresolved uncertainty

- The targeted route is not a systematic search, exhaustive bibliography, or
  novelty opinion. A publication-authorized artifact would require a fresh
  search and venue/status recheck.
- Candidate A's distinct contribution, construct validity, cue effects, and
  acceptable reviewer burden are unresolved. Appropriate-reliance effects are
  task-dependent, and no participant work is authorized.
- Candidate B's expectedness rule, frozen key, trace-derived state, open-world
  validity, and domain adjudication remain unresolved.
- A direct resolver check for the two CHI 2025 DOI routes can be partial even
  when official institutional and indexing records identify the papers. Their
  status must be rechecked before any later-authorized publication.
- No first paper, provider, model, corpus, dataset, participant population,
  sample, precision target, pilot, model call, or run has been selected.

## 7. Result boundary

Passing these checks would establish only that the owned artifacts express the
agreed source-status and claim boundaries consistently. It would not establish
novelty, validity, usability, effectiveness, transfer, or empirical support.
