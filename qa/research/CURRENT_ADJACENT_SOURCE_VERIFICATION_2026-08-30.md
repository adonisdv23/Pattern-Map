# Current adjacent-source verification — 2026-08-30

Status: **READ-ONLY WAYFINDING QA / TARGETED, NOT SYSTEMATIC OR EXHAUSTIVE /
NO STUDY, MODEL, PROVIDER, DATASET, PARTICIPANT, OR RESULT**

Scope: active links added to
`manuscript/SOURCES_AND_RESEARCH_ROUTE.md`, plus the retained foundational
entry points. Check date: **2026-08-30, America/New_York**.

## Method and evidence ceiling

Each current 2024–2026 item was opened at an author, publisher, conference,
ACL Anthology, arXiv, or official engineering landing page. Title, date or
venue, abstract/summary, and publication status were inspected as read-only
public metadata. This was link and claim-boundary verification, not a
systematic search, risk-of-bias assessment, replication, or full-paper
methodological review.

`Conference paper` means the public publisher/conference record identifies the
work as published in the named proceedings. `Preprint` means the route must not
present peer review. `Official engineering report` is first-party practice
evidence, not independent scientific validation.

No subscription was purchased, provider called, corpus acquired, model run,
participant contacted, or external state changed.

## Current route checks

| Field | Source and public status | Read-only check | Boundary carried into v16 |
| --- | --- | --- | --- |
| Context engineering | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic official engineering report, 2025 | **OPENED**; title/date and sections on finite context, just-in-time retrieval, progressive disclosure, memory, compaction, and subagents inspected | Context curation and agent decomposition are established adjacent practice; first-party guidance is not proof of universal effectiveness |
| Long-horizon continuity | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), Anthropic official engineering report, 2025 | **OPENED**; persistent artifact/handoff claims and explicit future-work limits inspected | Handoff artifacts and incremental continuity are not novel to Pattern Map and do not validate F4/F6 |
| Discovery/selection/organization | [ResearchArena](https://aclanthology.org/2025.findings-emnlp.303/), Findings of EMNLP 2025 | **OPENED**; ACL metadata and abstract inspected | Upstream discovery, selection, and organization are explicit research constructs; a keyword baseline may be credible |
| Perspective coverage | [Evaluating the Impact of Source Diversity for RAG in Historical Research](https://aclanthology.org/2026.lrec-1.53/), LREC 2026 | **OPENED**; ACL metadata, bounded multilingual historical setting, and perspective-shift claim inspected | Source choice may alter represented perspective in that setting; no universal diversity benefit or six-family validation follows |
| Source reliability | [Retrieval-Augmented Generation with Estimation of Source Reliability](https://aclanthology.org/2025.emnlp-main.1738/), EMNLP 2025 | **OPENED**; ACL metadata and cross-source reliability mechanism inspected | Reliability scoring/retrieval is active work; v16 must not claim an empty field or turn its multidimensional source record into a validated score |
| Dependence/redundancy/diversity | [How retriever redundancy and diversity impact RAG effectiveness](https://arxiv.org/abs/2608.13956), August 2026 preprint | **OPENED**; preprint status, synthetic FictionalQA setting, and duplicate/paraphrase/diversity comparison inspected | Directly defeats an uncontested novelty claim; preprint results remain bounded to the reported controlled setting |
| Real-web adaptive research | [DeepResearcher](https://aclanthology.org/2025.emnlp-main.22/), EMNLP 2025 | **OPENED**; ACL metadata and planning/cross-validation/reflection claims inspected | Planning, redirection, and reflection are active mechanisms; they are not invented by v16 |
| Sufficiency/gap-controlled retrieval | [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/), ACL 2026 | **OPENED**; ACL metadata and explicit sufficiency/gap controller inspected | Adaptive retrieval and stopping/gap representation are occupied technical areas; typed missingness requires a narrower construct claim |
| Agent memory | [MemoryAgentBench](https://arxiv.org/abs/2507.05257), 2025 preprint | **OPENED**; preprint status and four stated competencies inspected | Retrieval, learning, long-range understanding, and selective forgetting require separate tests; no v16 memory result follows |
| Retrieved-document attribution | [Source Attribution in Retrieval-Augmented Generation](https://arxiv.org/abs/2507.04480), 2025 preprint | **OPENED**; preprint status, document-level attribution, cost, and redundancy/complementarity scope inspected | An influence receipt must distinguish workflow selection from model-internal or counterfactual attribution |
| Attribution cue risk | [Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.findings-acl.1087/), Findings of ACL 2025 | **OPENED**; ACL metadata and counterfactual authorship-metadata design inspected | Source metadata can be a treatment cue; attribution cannot be treated as truth or a neutral record |
| Versioned human correction | [DeepFact](https://aclanthology.org/2026.acl-long.1586/), ACL 2026 | **OPENED**; ACL metadata and Audit-then-Score/versioned-correction design inspected | Auditable revision and human correction are active work; accepted disposition remains revisable evidence, not truth |
| Fine-grained deep-research evaluation | [ResearchRubrics](https://iclr.cc/virtual/2026/poster/10010639), ICLR 2026 | **OPENED**; official conference page, authors, abstract, rubric scope, and implicit-context finding inspected | Implicit criteria and retrieved-information reasoning are measurable but difficult; Pattern Map needs credible baselines and cannot infer an effect |
| Citation/report evaluation | [DeepResearch Bench](https://arxiv.org/abs/2506.11763), 2025 preprint | **OPENED**; preprint status and separation of report quality, effective citations, and citation accuracy inspected | Citation counts and accuracy are separate from decision usefulness and source independence |
| Agent-component reproducibility | [OAgents](https://aclanthology.org/2025.findings-emnlp.720/), Findings of EMNLP 2025 | **OPENED**; ACL metadata, run-variance warning, and redundant-component finding inspected | Mechanism isolation, repeated runs, and apples-to-apples budgets must precede an omnibus playbook claim |

## Retained foundational-link checks

| Source | 2026-08-30 status |
| --- | --- |
| [Information Foraging](https://doi.org/10.1037/0033-295X.106.4.643) | DOI resolver fetch was blocked by public robots policy in this tool. Bibliographic identity was independently returned by public search metadata. **PARTIAL / RECHECK AT PUBLICATION.** |
| [Principles of Metareasoning](https://doi.org/10.1016/0004-3702(91)90015-C) | The persistent DOI route was retained. Its equivalent ScienceDirect PII landing page opened through public search metadata; title, authors, journal/date, DOI, and bounded-rationality abstract matched. **VERIFIED PUBLISHER LANDING; DOI REDIRECT RECHECK AT PUBLICATION.** |
| [PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation opened; title, status, provenance scope, influence, derivation, revision, and role terms inspected. **VERIFIED OFFICIAL.** |
| [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) | Current official handbook landing page opened. **VERIFIED OFFICIAL LANDING; chapter-level claims require publication-time recheck.** |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | NeurIPS proceedings landing page opened. **VERIFIED PUBLISHER LANDING.** |
| [Principles of Mixed-Initiative User Interfaces](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) | Microsoft Research publication page opened. **VERIFIED AUTHOR-INSTITUTION LANDING.** |
| [Guidelines for Human–AI Interaction](https://doi.org/10.1145/3290605.3300233) | Direct DOI open did not return content in this tool; public search returned the ACM proceedings metadata and abstract. **PARTIAL / RECHECK AT PUBLICATION.** |

Blocked automated resolution is not evidence that a source is false or absent.
It is also not a reason to call the link publication-ready.

## Claims deliberately not resolved by this check

- No systematic-search completeness or exhaustiveness claim.
- No novelty clearance for the six-family arrangement, influence receipt,
  typed missingness, or matched-budget study.
- No determination that one narrow wedge is a publishable contribution.
- No evidence that Pattern Map improves decision quality, supported novelty,
  diversity, correction burden, or any other outcome.
- No generalization from one source-diversity, memory, attribution, retrieval,
  or agent-evaluation setting to all domains or systems.
- No provider/model/corpus/participant selection and no empirical result.

## Publication-time gate

Immediately before any later-authorized publication, re-open every external
link, verify title/version/publication status, replace moved links only with a
primary or official destination, and record the new date. The two partial DOI
checks above require direct resolution from the publication environment. A
successful 2026-08-30 landing-page check is not permanent link assurance.
