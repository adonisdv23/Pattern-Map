# Optional sources and research route

This route is deliberately subordinate to the manuscript. A reader should be
able to understand the idea without opening a framework, protocol, source
ledger, or historical archive.

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

- **Context engineering and agent harnesses.** Anthropic's official
  [context-engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  already treats context as a finite resource to be curated through
  just-in-time retrieval, progressive disclosure, compaction, memory, and
  subagents. Its [long-running-agent harness report](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  uses persistent artifacts and incremental handoffs. Pattern Map therefore
  cannot claim to invent context curation, memory, or agent decomposition.
- **Discovery, selection, organization, and perspective coverage.** The
  peer-reviewed [ResearchArena](https://aclanthology.org/2025.findings-emnlp.303/)
  separates research into discovery, selection, and organization, while a
  2026 [source-diversity study](https://aclanthology.org/2026.lrec-1.53/)
  shows that source choice can change represented perspectives in one bounded
  historical-RAG setting. Neither establishes a universal diversity benefit or
  validates the six-family map.
- **Source reliability, dependence, and redundancy.** Peer-reviewed
  [Reliability-Aware RAG](https://aclanthology.org/2025.emnlp-main.1738/)
  estimates source reliability and uses it in retrieval. A separate August
  2026 [redundancy/diversity preprint](https://arxiv.org/abs/2608.13956)
  compares duplicate, paraphrased, and diverse evidence in a controlled
  synthetic setting. These works make an empty-field claim untenable. They
  also leave Pattern Map's separation of role, support, origin, relevance,
  track record, and permission as a design boundary rather than a validated
  scoring mechanism.
- **Adaptive acquisition, sufficiency, and stopping.** Peer-reviewed
  [DeepResearcher](https://aclanthology.org/2025.emnlp-main.22/) studies
  planning, cross-validation, reflection, and redirection in real-web research.
  [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) explicitly predicts
  evidence sufficiency and structured gaps during iterative retrieval. The
  proposal to acquire adaptively and stop on sufficiency or cost is therefore
  adjacent to active technical work, not a new mechanism established by v16.
- **Memory, revision, and long-horizon continuity.** The 2025
  [MemoryAgentBench preprint](https://arxiv.org/abs/2507.05257) evaluates
  retrieval, test-time learning, long-range understanding, and selective
  forgetting in incremental interactions. This reinforces the need to test
  versioning, correction, and forgetting separately; it does not show that the
  v16 memory contract works.
- **Attribution, provenance, and correctability.** A 2025
  [document-attribution preprint](https://arxiv.org/abs/2507.04480) examines
  which retrieved documents influence a RAG answer and the cost of estimating
  that influence. Peer-reviewed work on
  [attribution bias](https://aclanthology.org/2025.findings-acl.1087/) shows
  that source metadata can itself change attribution. The 2026
  [DeepFact](https://aclanthology.org/2026.acl-long.1586/) benchmark uses
  versioned, auditable evidence-backed corrections. Together they warn against
  treating a citation, influence estimate, metadata cue, or accepted human
  disposition as truth.
- **Deep-research evaluation and reproducibility.** The peer-reviewed
  [ResearchRubrics](https://iclr.cc/virtual/2026/poster/10010639) evaluates
  long-form research against fine-grained explicit and implicit criteria. The
  [DeepResearch Bench preprint](https://arxiv.org/abs/2506.11763) separates
  report assessment from effective-citation count and citation accuracy.
  Peer-reviewed [OAgents](https://aclanthology.org/2025.findings-emnlp.720/)
  reports nontrivial run variance and redundant-seeming agent components under
  its tested setting. These sources support stronger baselines, matched
  resources, mechanism isolation, and reproducibility checks; they do not
  supply a result for Pattern Map.

The component areas have substantial established and active prior work; the
proposal is to hold them together as one proportional, human-governed
responsibility before generation. That is
an authored design and governance synthesis with a testable agenda—not a novel
mechanism, exhaustive taxonomy, technical layer, or demonstrated improvement.

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
