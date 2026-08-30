# Optional sources and research route

This route is deliberately subordinate to the manuscript. A reader should be
able to understand the idea without opening a framework, protocol, source
ledger, or historical archive.

In this project, **before generation** names a logical responsibility boundary,
not a one-time chronological stage. In an iterative agent loop, the boundary
applies whenever a search result, memory item, comparison, or prior draft is
considered for the next generation. It does not claim that all discrimination
precedes the first model call or ends after the first token is produced.

## Authority and historical continuity

- [Locked v16 owner intent](../docs/OWNER_INTENT_V16.md) — current proposition,
  audience, six-family scope, human-judgment boundary, and action limits.
- [Thesis and audience contract](../docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md) —
  plain-language reading stops, technical definition, and evidence boundary.
- [V16 claims and source ledger](../docs/CLAIMS_AND_SOURCE_LEDGER_V16.md) —
  controlled public claims, their strongest current basis, and the empirical
  or product claim each must not be upgraded into.
- [V13 recovery and intent memo](../archive/transfers/v14-complete-2026-08-18/10_FULL_REPOSITORY_SNAPSHOT/reports/V13_RECOVERY_AND_INTENT_MEMO.md) —
  historical reader problem, six-family continuity, and the warning that
  historical material is not proof.
- [V14 thought piece](../archive/transfers/v14-complete-2026-08-18/10_FULL_REPOSITORY_SNAPSHOT/source/THOUGHT_PIECE_V14.md) —
  source-aware terminology, implementation alternatives, counterarguments,
  and prior-art restraint.

The recovered v13 diagram is an immutable historical anchor. It is not the
current system map and is not used here as evidence that the framework works.

## Targeted prior-art route

This is a targeted wayfinding route, not a systematic or exhaustive literature
review. It was refreshed on **2026-08-30**. The current 2025–2026 public landing
pages were opened and inspected; older foundational links were rechecked as
read-only public access allowed, with blocked resolver status recorded in
research QA. Publication status varies: conference papers, official
engineering reports, and explicitly labeled preprints appear together because
they constrain different design questions. Every link, version, and status must
be checked again immediately before any later-authorized publication.

The archived [prior-art and adjacent-fields map](../archive/transfers/v14-complete-2026-08-18/03_RESEARCH_PACKAGE/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md)
and accompanying [reference list](../archive/transfers/v14-complete-2026-08-18/03_RESEARCH_PACKAGE/REFERENCES.md)
remain the historical route through earlier foundations. They include
[Information Foraging](https://doi.org/10.1037/0033-295X.106.4.643),
[Principles of Metareasoning](https://doi.org/10.1016/0004-3702(91)90015-C),
the W3C [PROV-O Recommendation](https://www.w3.org/TR/prov-o/), the
[Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current),
the original [retrieval-augmented generation paper](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),
and primary work on [mixed-initiative interfaces](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/)
and [human–AI interaction guidelines](https://doi.org/10.1145/3290605.3300233).

### Current adjacent fields, 2025–2026

- **Context selection, adaptation, and evolving playbooks.** Anthropic's 2025
  official [context-engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  treats context as finite and iteratively curated through retrieval,
  compaction, memory, and progressive disclosure. The peer-reviewed ICLR 2026
  paper [Agentic Context Engineering (ACE)](https://iclr.cc/virtual/2026/poster/10008343)
  goes further by treating context as an evolving playbook updated through
  generation, reflection, and curation. These sources rule out a claim that
  Pattern Map invented context curation, iterative context adaptation, or
  playbook evolution. Anthropic's report is first-party practice guidance, not
  independent validation of this project.
- **Recurrence versus support.** The 2026
  [GroupQA preprint](https://arxiv.org/abs/2601.06189) reports, in its tested
  RAG setting, that paraphrasing an argument can be more persuasive than adding
  distinct independent support. That result directly motivates separating
  recurrence, origin relation, and claim support, but it does not establish the
  provenance or independence of any source in a Pattern Map example.
- **Audit trails and execution traces.** NIST's ongoing official
  [agent-evaluation-probes project](https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai)
  is developing rubric-based grounding checks and machine-readable audit
  trails; it is an early project, not a published standard. The August 2026
  [LEDGER preprint](https://arxiv.org/abs/2608.18398) builds claim-to-evidence
  trace graphs, while the peer-reviewed ACL 2026 system demonstration
  [Graph of Trace](https://aclanthology.org/2026.acl-demo.29/) visualizes
  agent execution traces for human review. A new trace, graph, audit trail, or
  receipt is therefore not the defensible research contribution here.
- **Evidence views and appropriate reliance.** The peer-reviewed NAACL 2025
  system demonstration [FACTS&EVIDENCE](https://aclanthology.org/2025.naacl-demo.35/)
  already presents claim-level verification, explanations, and multiple
  evidence sources to users. Two CHI 2025 conference papers—
  [Fostering Appropriate Reliance on Large Language Models](https://doi.org/10.1145/3706598.3714020)
  and [To Rely or Not to Rely?](https://doi.org/10.1145/3706598.3714097)—show
  that interface cues can change over- and under-reliance in nonuniform ways
  in their bounded tasks. This narrows Candidate A to a provisional
  fixed-answer appropriate-reliance interface question; it supplies no reason
  to assume that a claim/evidence view improves judgment.
- **Stopping and resource cost.** The peer-reviewed EACL 2026 paper
  [Over-Searching](https://aclanthology.org/2026.eacl-long.361/) reports
  unnecessary search, added cost, and worse abstention under some tested
  conditions. The peer-reviewed LREC 2026
  [budget-constrained agentic-search study](https://aclanthology.org/2026.lrec-1.808/)
  varies search depth, retrieval strategy, and completion budget under fixed
  constraints. [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) adds an
  explicit sufficiency-and-gap controller. These works make stopping and
  budget accounting required comparators and costs, not Pattern Map inventions.
- **Deep-research evaluation.** The 2026 [DREAM preprint](https://arxiv.org/abs/2602.18940)
  proposes tool-using evaluation for temporal, factual, and reasoning checks.
  The peer-reviewed ACL 2026 papers
  [BrowseComp-Plus](https://aclanthology.org/2026.acl-long.1023/) and
  [ReportLogic](https://aclanthology.org/2026.acl-long.384/) respectively
  separate retriever contribution from end-to-end agent performance and test
  report-level support relations plus judge sensitivity to superficial cues.
  Together they require dimension-specific outcomes, frozen evaluation
  boundaries, and cue-robust checks; no benchmark label is a Pattern Map
  effectiveness result.

The component areas have substantial established and active prior work. The
bounded contribution is an **authored, proportional, human-governed
design/governance synthesis and testable agenda**. It is not a novel mechanism,
exhaustive taxonomy, validated method, effectiveness result, universal
architecture, or claim that one technical layer must sit at a single moment in
an agent loop.

## Echo route

The Echo Problem / ECHO-01 is a separate v15.2-derived origin-accounting track.
Its curated [EP v0.1 project](../research/the-echo-problem/README.md) and
[status/no-results record](../research/the-echo-problem/STATUS_AND_BOUNDARIES.md)
now preserve the protocol, fixtures, and unfavorable-result classes. The
project remains unrun and has no results. The v16 manuscript uses only the
fictional common-origin example; it does not import a result, a selected model,
or a claim of discovered provenance.

## Future research route

A future, separately authorized research agenda could compare an ordinary
retrieval-and-generation route with a structured upstream-choice route under
matched tasks, evidence budgets, model configurations, and human-review costs.
Useful questions include supported-claim handling, evidence diversity,
missing-perspective detection, correction effort, and decision usefulness.
The design would need to preserve null, harmful, shortcut-driven, fragile,
non-transfer, and stop outcomes. A protocol or fixture would remain a plan,
not a result.
