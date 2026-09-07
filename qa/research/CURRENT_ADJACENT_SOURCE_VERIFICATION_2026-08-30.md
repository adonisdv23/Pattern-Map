# Current adjacent-source verification — 2026-08-30

Status: **READ-ONLY WAYFINDING QA / TARGETED, NOT SYSTEMATIC OR EXHAUSTIVE /
NO STUDY, MODEL, PROVIDER, DATASET, PARTICIPANT, OR RESULT**

Scope: current 2025–2026 links in
`manuscript/SOURCES_AND_RESEARCH_ROUTE.md`, plus retained foundational entry
points. Check date: **2026-08-30, America/New_York**.

## Method and evidence ceiling

Each current item was opened at an author, standards-body, publisher,
conference, ACL Anthology, arXiv, or official engineering landing page. Title,
date or venue, abstract/summary, and publication status were inspected as
read-only public metadata. This was link and claim-boundary verification, not a
systematic search, full-paper methodological review, risk-of-bias assessment,
replication, or novelty clearance.

`Conference paper` means the conference or proceedings record identifies the
work as published. `Preprint` means the route must not imply peer review.
`Official project` and `official engineering report` mean first-party public
records, not standards or independent scientific validation unless the record
itself says otherwise.

No subscription was purchased, provider called, corpus acquired, model run,
participant contacted, or external state changed.

## Current route checks

| Field | Source and public status | Read-only check | Boundary carried into v16 |
| --- | --- | --- | --- |
| Context engineering | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic official engineering report, published 2025-09-29 | **OPENED**; title, date, finite-context framing, iterative curation, retrieval, progressive disclosure, compaction, memory, and subagent sections inspected | First-party practice evidence establishes direct adjacency, not independent validation or universal efficacy |
| Evolving playbooks | [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://iclr.cc/virtual/2026/poster/10008343), ICLR 2026 conference paper/poster | **OPENED**; official conference title, authors, venue, and generation/reflection/curation playbook description inspected | Iterative context adaptation and evolving playbooks are not Pattern Map inventions; the reported benchmark results do not transfer to v16 |
| Recurrence versus support | [Rational Synthesizers or Heuristic Followers?](https://aclanthology.org/2026.findings-acl.2003/), peer-reviewed Findings of ACL 2026 paper, DOI `10.18653/v1/2026.findings-acl.2003`; [earlier arXiv record](https://arxiv.org/abs/2601.06189) retained for version history | **OPENED**; official ACL venue metadata, GroupQA scope, and reported paraphrase-versus-independent-support result inspected | Directly sharpens the recurrence boundary in the tested setting; does not establish origin, source independence, or universal model behavior |
| Expected absence | [Absence Bench: Language Models Can’t See What’s Missing](https://proceedings.neurips.cc/paper_files/paper/2025/hash/36b31e1bb8ecd4f4081686448e9eff2d-Abstract-Datasets_and_Benchmarks_Track.html), peer-reviewed NeurIPS 2025 Datasets and Benchmarks Track paper, DOI `10.52202/085713-1277` | **OPENED**; official proceedings metadata, original-plus-edited context design, three-domain scope, and reported omission-detection result inspected | An explicit baseline is not sufficient by itself; the bounded result does not establish open-world absence, Candidate B's orthogonal construct, or a Pattern Map effect |
| Agent grounding probes | [Building Evaluation Probes into Agentic AI](https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai), ongoing official NIST project, started April 2026 | **OPENED**; project status, rubric-based grounding probes, audit-trail objective, faithfulness/completeness/sufficiency dimensions, and invitation-for-input status inspected | NIST is developing an approach; this page is not a standard, validated universal method, or Pattern Map result |
| Claim/evidence trace graphs | [LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents](https://arxiv.org/abs/2608.18398), August 2026 arXiv preprint | **OPENED**; title, date, preprint status, trace/evidence/workflow nodes, typed edges, and example-based scope inspected | A new trace, graph, evidence anchor, or claim-support path is not a defensible Candidate A novelty center |
| Execution-trace visualization | [Graph of Trace: Visualizing Execution Traces of Scientific Agents](https://aclanthology.org/2026.acl-demo.29/), ACL 2026 system-demonstration paper | **OPENED**; ACL venue record, execution-event graph, visualization, and bounded expert-evaluation abstract inspected | Human review of structured agent traces is active peer-reviewed work; its reported setting does not validate Pattern Map receipts |
| Fine-grained evidence interface | [FACTS&EVIDENCE](https://aclanthology.org/2025.naacl-demo.35/), NAACL 2025 system-demonstration paper | **OPENED**; ACL venue record and user-driven claim breakdown, explanation, multi-source evidence, and selective-use aims inspected | Claim/evidence views are established interface objects; the paper does not establish Candidate A's proposed reliance outcome |
| Appropriate reliance — sources/inconsistencies | [Fostering Appropriate Reliance on Large Language Models](https://doi.org/10.1145/3706598.3714020), CHI 2025 conference paper | DOI resolution returned an automated-access block; title, DOI, venue, controlled-study abstract, and bounded findings were cross-checked on the Princeton institutional publication record | Sources and inconsistencies can change reliance in the reported setting; this is not a general interface prescription. **PARTIAL / RECHECK AT PUBLICATION.** |
| Appropriate reliance — intervention trade-offs | [To Rely or Not to Rely?](https://doi.org/10.1145/3706598.3714097), CHI 2025 conference paper | DOI resolution returned an automated-access block; title, DOI, venue, abstract, and intervention scope were cross-checked on the arXiv and University of Toronto author/lab records | Reducing over-reliance need not improve joint appropriate reliance; Candidate A must count both error directions. **PARTIAL / RECHECK AT PUBLICATION.** |
| Over-searching | [Over-Searching in Search-Augmented Large Language Models](https://aclanthology.org/2026.eacl-long.361/), EACL 2026 long paper | **OPENED**; ACL venue record, answerable/unanswerable split, abstention, noise, multi-turn, and cost claims inspected | More search can add cost or harm under tested conditions; acquisition and stopping need explicit guardrails rather than a monotone-benefit assumption |
| Budget-constrained search | [Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search](https://aclanthology.org/2026.lrec-1.808/), LREC 2026 paper | **OPENED**; ACL/ELRA venue record, fixed tool/completion budgets, search-depth and retrieval-strategy comparisons inspected | Search, token, and operating budgets belong in the estimand; the reported tasks and models do not choose a v16 design |
| Sufficiency and structured gaps | [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/), ACL 2026 long paper | **OPENED**; ACL venue metadata and sufficiency/gap controller abstract inspected | Candidate B overlaps active gap/sufficiency work and needs a narrower construct; no typed-missingness novelty follows |
| Outcome-driven memory operations | [Memory-R1](https://aclanthology.org/2026.acl-long.583/), peer-reviewed ACL 2026 long paper, DOI `10.18653/v1/2026.acl-long.583` | **OPENED**; official ACL venue metadata, `ADD`/`UPDATE`/`DELETE`/`NOOP` operations, training scope, and reported benchmark setting inspected | Learned memory operations are active prior work; the reported results do not establish correctness, authorization, safety, human governance, or Pattern Map effectiveness |
| Workflow provenance | [PROV-AGENT](https://impact.ornl.gov/en/publications/prov-agent-unified-provenance-for-tracking-ai-agent-interactions-/), peer-reviewed IEEE e-Science 2025 proceedings paper, DOI `10.1109/eScience65000.2025.00093` | **OPENED**; official ORNL publication metadata, venue, pages, DOI, W3C PROV/MCP scope, and workflow-capture description inspected | Workflow provenance is occupied component prior art; a trace does not establish claim truth, permission, independence, or receipt novelty |
| Query-only memory injection | [Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42a97bbd9844d2bf68596730af80bcdf-Abstract-Conference.html), peer-reviewed NeurIPS 2025 main-conference paper, DOI `10.52202/085713-1554` | **OPENED**; official proceedings metadata, query-only threat model, later-query influence, and bounded attack description inspected | Versioning, provenance, and storage permission are not memory-security guarantees; retrieved memory must not become instruction or authority merely through reuse |
| Memory-based authorization bypass | [FragFuse](https://www.usenix.org/conference/usenixsecurity26/presentation/rao), peer-reviewed USENIX Security 2026 paper | **OPENED**; official proceedings metadata, cross-interaction fragmentation/fusion threat, tested access-control setting, and reported bounded attack results inspected | A scoped memory record does not establish safe composition or authorization; the paper exposes a threat boundary but does not validate a Pattern Map defense |
| Agentic deep-research evaluation | [DREAM: Deep Research Evaluation with Agentic Metrics](https://arxiv.org/abs/2602.18940), 2026 arXiv preprint | **OPENED**; title, preprint status, temporal/factual/reasoning evaluation dimensions, and tool-using evaluator proposal inspected | Agentic evaluation is a proposed active direction, not a standard or a Pattern Map validation result |
| Retrieval/agent disentanglement | [BrowseComp-Plus](https://aclanthology.org/2026.acl-long.1023/), ACL 2026 long paper | **OPENED**; ACL venue record, fixed human-verified corpus, fairness/reproducibility motivation, and retriever-versus-agent separation inspected | A future omnibus study must isolate retrieval contribution from end-to-end behavior; no benchmark or corpus is selected here |
| Report-level logic | [ReportLogic](https://aclanthology.org/2026.acl-long.384/), ACL 2026 long paper | **OPENED**; ACL venue record, macro/expositional/structural logic, human annotation, and judge-cue robustness abstract inspected | Report support and judge robustness are separate dimensions; fluency, verbosity, or one score cannot stand in for decision quality |

## Retained foundational-link checks

| Source | 2026-08-30 status |
| --- | --- |
| [Information Foraging](https://doi.org/10.1037/0033-295X.106.4.643) | DOI resolver fetch was blocked by public robots policy in the available tool. Bibliographic identity was returned by public search metadata. **PARTIAL / RECHECK AT PUBLICATION.** |
| [Principles of Metareasoning](https://doi.org/10.1016/0004-3702(91)90015-C) | The persistent DOI route was retained. Equivalent publisher metadata matched title, authors, journal/date, and DOI. **VERIFIED PUBLISHER METADATA; DOI REDIRECT RECHECK AT PUBLICATION.** |
| [PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation opened; title, status, provenance scope, influence, derivation, revision, and role terms inspected. **VERIFIED OFFICIAL.** |
| [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) | Current official handbook landing page opened. **VERIFIED OFFICIAL LANDING; chapter-level claims require publication-time recheck.** |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | NeurIPS proceedings landing page opened. **VERIFIED PUBLISHER LANDING.** |
| [Principles of Mixed-Initiative User Interfaces](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) | Microsoft Research publication page opened. **VERIFIED AUTHOR-INSTITUTION LANDING.** |
| [Guidelines for Human–AI Interaction](https://doi.org/10.1145/3290605.3300233) | Direct DOI open did not return content in the available tool; public search returned ACM proceedings metadata and abstract. **PARTIAL / RECHECK AT PUBLICATION.** |

Blocked automated resolution is not evidence that a source is false or absent.
It is also not a reason to call the link publication-ready.

## Claims deliberately not resolved by this check

- No systematic-search completeness or exhaustiveness claim.
- No novelty clearance for the six-family arrangement, an appropriate-reliance
  interface, Candidate B's orthogonal record, or the matched-budget study.
- No determination that either narrow question is a publishable contribution.
- No evidence that Pattern Map improves decision quality, support, diversity,
  correction burden, reliance, or any other outcome.
- No generalization from one recurrence, omission-detection, memory-attack,
  interface, retrieval, trace, stopping, or deep-research evaluation setting
  to all domains or systems.
- No provider, model, paper, corpus, participant, sample-size, or run selection.

## Publication-time gate

Immediately before any later-authorized publication, re-open every external
link, verify title/version/publication status, replace moved links only with a
primary or official destination, and record the new date. The DOI resolver
checks marked partial above require direct resolution from the publication
environment. A successful 2026-08-30 landing-page check is not permanent link
assurance.
