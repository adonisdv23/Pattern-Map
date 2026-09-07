# Prior-art delta v1

Status: targeted prior-art correction for the v15 discrimination-layer program. This document is a research aid, not a publication claim, empirical result, or legal opinion. v15.1 consolidation adds the structured-source-correlation precedent in S20; it does not reopen the literature search.

Access date: 2026-08-18 (America/New_York). Publication and venue labels below are the status visible in the linked primary record on that date.

## Bottom line

The targeted review narrows the novelty boundary substantially. Source copying, truth discovery, correlated-source fusion, double-counting control, citation-network amplification, near-duplicate detection, set-level retrieval, conflict-aware RAG, source-dependence auditing, and evidence-fusion mechanisms all have direct precedents. The project should not claim a new generic “discrimination layer,” a new deduplication primitive, or a general method for discovering truth or independent support.

The defensible research nucleus is smaller:

- **Retain as a design hypothesis:** a typed, visible policy can keep derivation, origin-family relation, claim stance, task relevance, authority, support, uncertainty, and action disposition separate before generation.
- **Accept as the narrow empirical estimand:** on stipulated synthetic graphs, compare a rule-only condition with a supplied typed origin-relation cue and measure false-corroboration accounting for one frozen model and one task. A positive effect would be an observable condition effect, not provenance discovery, real-world source independence, or factual correctness.
- **Modify the vocabulary:** “origin relation,” “common-origin family,” “copy/reproduction relation,” and “UNKNOWN” are safer than unqualified “independence.” Source disagreement, evidence conflict, and document diversity are not interchangeable with origin relation.
- **Defer:** learned origin inference, claims about human reliance or decision quality, deployment readiness, domain-general transfer, and any assertion about the truth of an open-world claim.
- **Reject:** novelty claims based on putting familiar retrieval, provenance, conflict, deduplication, memory, or decision primitives in one pre-generation pipeline.

Two attribution corrections matter immediately. Naphade’s Table 4 gives the 76.5% versus 67.6% paraphrase/distinct flip rates to **DeepSeek-R1-8B**, not Llama-3.1-70B-Instruct; Llama-3.1-70B-Instruct is 69.8% versus 62.9%. Newswire’s listed third author is **Luca D’Amico-Wong**, not “Li.”

## Search scope and accounting rules

### Scope

Searches ran on 2026-08-18 against publisher, society, venue, repository, and author-maintained primary records. The query set included:

- `Dong Berti-Équille Srivastava copying truth discovery source dependence`;
- `Dong Berti-Équille Srivastava dynamic copying detection truth discovery`;
- `Senn double counting meta-analysis`;
- `Greenberg citation distortions unfounded authority citation network`;
- `Naphade RAG paraphrased evidence GroupQA`;
- `NEWS-COPY noise robust de-duplication` and `Newswire historical news database`;
- `Li Padman Krishnan source dependence multi-source RAG`;
- `RAMDocs conflicting evidence RAG` and `EvidentialRAG information conflict`;
- `retrieval deduplication redundancy diversity set selection RAG`;
- `Zhang Ives Roth provenance natural language claims common origin paraphrases`;
- `Pochampally data fusion correlations common extraction rules`;
- `independent dependent evidence double counting` and `Cochrane multiple reports same study`.

Primary records were preferred for both bibliographic status and technical findings: PVLDB, BMJ/BMC/PubMed, Cochrane, ACM, ACL Anthology, NeurIPS, ICLR, COLM/OpenReview where directly available, and arXiv records/PDFs for working manuscripts. Search-result snippets, reviews, and advisory notes were used only to locate a primary record. No model, provider, paid API, deployment, production job, or external contact was used.

### Evidence labels

Each source card below separates:

- **Sourced fact:** what the primary record says, including the exact bounded finding used here.
- **Project inference:** the design or novelty implication drawn by this project; it is not attributed to the source.
- **Claim blocked:** wording the source does not permit.
- **Residual contribution:** what remains useful after the boundary correction.
- **Disposition:** `Accept`, `Modify`, `Defer`, or `Reject` for the project’s current claim posture.

The following dimensions remain distinct:

| Dimension | Meaning in this delta | What it must not be treated as |
| --- | --- | --- |
| Derivation | How an artifact or claim was transformed from another artifact | Common origin, support, or truth |
| Origin-family relation | A stipulated or evidenced relation such as `SAME`, `DISTINCT`, `COPY`, or `UNKNOWN` | A discovered fact about the world |
| Claim stance | Support, refute, qualify, conflict, or no stance toward a claim | Source independence |
| Evidence interaction | Agreement, contradiction, complementarity, redundancy, or uncertainty in retrieved material | Shared authorship or copying |
| Authority | Domain-, role-, time-, and claim-scoped source standing | Claim correctness |
| Support | Whether an artifact or span bears on a claim under a stated task | Reliability or independence |
| Recurrence | Number or pattern of reports, citations, or observations | Number of independent origins |
| Action disposition | Answer, compare, acquire, clarify, hold, defer, or refuse | Epistemic truth status |

## Publication and status ledger

| ID | Source and official record | Status on 2026-08-18 | Use in this delta |
| --- | --- | --- | --- |
| S1 | Dong, Berti-Équille & Srivastava, [Integrating Conflicting Data: The Role of Source Dependence](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf) | PVLDB 2(1), VLDB 2009, pp. 550–561; published paper | Source dependence and truth-discovery boundary |
| S2 | Dong, Berti-Équille & Srivastava, [Truth Discovery and Copying Detection in a Dynamic World](https://www.vldb.org/pvldb/vol2/vldb09-335.pdf) | PVLDB 2(1), VLDB 2009, pp. 562–573; published paper | Time-varying copying and source quality |
| S3 | Senn, [Overstating the evidence – double counting in meta-analysis and related problems](https://doi.org/10.1186/1471-2288-9-10) | BMC Medical Research Methodology 9:10, 2009; published, refereed article | Effective-independence analogy and audit discipline |
| S4 | Greenberg, [How citation distortions create unfounded authority: analysis of a citation network](https://pubmed.ncbi.nlm.nih.gov/19622839/) | BMJ 2009; published article, DOI [10.1136/bmj.b2680](https://doi.org/10.1136/bmj.b2680) | Citation recurrence and authority boundary |
| S5 | Naphade, [Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering](https://arxiv.org/abs/2601.06189) | arXiv v1, submitted 2026-01-08; comments say ACL ARR submission; no acceptance shown in the checked record | Closest LLM redundancy/attribution comparator; unreviewed working manuscript |
| S6 | Silcock et al., [Noise-Robust De-Duplication at Scale](https://arxiv.org/abs/2210.04261) and [ICLR 2023 poster record](https://iclr.cc/virtual/2023/poster/11067) | ICLR 2023 poster; published conference contribution | Large-scale near-duplicate detection |
| S7 | Silcock, Arora, D’Amico-Wong & Dell, [Newswire: A Large-Scale Structured Database of a Century of Historical News](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets & Benchmarks Track; published conference paper | Reproduction clusters and outlet-count boundary |
| S8 | Li, Padman & Krishnan, [Same Question, Different Source, Different Answer: Auditing Source-Dependence in Medical Multi-Source RAG](https://arxiv.org/abs/2605.29084) | arXiv v1, submitted 2026-05-27; no venue acceptance shown in the checked record | Closest source-dependence RAG audit; unreviewed working manuscript |
| S9 | Wang, Prasad, Stengel-Eskin & Bansal, [Retrieval-Augmented Generation with Conflicting Evidence](https://arxiv.org/abs/2504.13079) | COLM 2025 conference paper, as stated in the paper and arXiv comments | Ambiguity, misinformation, and noise benchmark |
| S10 | Hossain, Shayoni & Mridha, [EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning](https://arxiv.org/abs/2607.10491) | arXiv v1, submitted 2026-07-11; no venue or acceptance shown in the checked record | Closest conflict/uncertainty fusion comparator; unreviewed working manuscript |
| S11 | Carbonell & Goldstein, [The use of MMR, diversity-based reranking for reordering documents and producing summaries](https://doi.org/10.1145/290941.291025) | SIGIR ’98 conference paper; published ACM record | Established diversity-aware reranking |
| S12 | Lee, Jo, Park & Lee, [Shifting from Ranking to Set Selection for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.861/) | ACL 2025 main conference, oral presentation; published ACL Anthology record | Set-wise coverage and redundancy reduction |
| S13 | Verma et al., [NEST: Nested Evidence Survival for Retrieval](https://aclanthology.org/2026.acl-industry.35/) | ACL 2026 Industry Track; published ACL Anthology record | Training-free recall/selection and redundancy removal |
| S14 | Cho & Lee, [RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](https://arxiv.org/abs/2604.19047) | arXiv v2; record says accepted to ACL 2026 Main Conference; ACL publication page not located during this pass | Redundancy-aware benchmark design; status qualified |
| S15 | Ross et al., [How retriever redundancy and diversity impact RAG effectiveness](https://arxiv.org/abs/2608.13956) | arXiv v1, submitted 2026-08-14; no venue or acceptance shown | Closest current controlled redundancy study; unreviewed working manuscript |
| S16 | Schelpe, [Byte-Exact Deduplication in Retrieval-Augmented Generation: A Three-Regime Empirical Analysis Across Public Benchmarks](https://arxiv.org/abs/2605.09611) | arXiv v1, submitted 2026-05-10; record calls it a preprint | Byte-exact deduplication adjacency; unreviewed working manuscript |
| S17 | Cochrane, [Handbook chapter 4: Searching for and selecting studies](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | Current official handbook chapter | Reports-versus-study unit discipline |
| S18 | Strittmatter, Pilditch & Lagnado, [Reasoning about (In)Dependent Evidence: A Mismatch between Perceiving and Incorporating Dependencies?](https://www.research-collection.ethz.ch/entities/publication/0659291b-e61d-4afe-9932-a4aeec8b9705) | ETH repository record: 2024 conference paper, published version available | Human evidence-dependence analogy |
| S19 | Zhang, Ives & Roth, [“Who said it, and Why?” Provenance for Natural Language Claims](https://aclanthology.org/2020.acl-main.406/) | ACL 2020, published ACL Anthology paper, pp. 4416–4426 | Closest direct natural-language claim-provenance comparator; inferred provenance is distinct from supplied benchmark relations |
| S20 | Pochampally, Das Sarma, Dong, Meliou & Srivastava, [Fusing Data with Correlations](https://doi.org/10.1145/2588555.2593674) ([primary PDF](https://people.cs.umass.edu/~ameli/projects/dataIntegration/papers/corrFusion-SIGMOD2014.pdf)) | SIGMOD 2014, pp. 433–444; published conference paper | Correlations broader than literal copying; limits of binary dependence labels |

## Detailed source cards

### S1 — Dong, Berti-Équille & Srivastava: static source dependence

**Sourced fact.** The PVLDB paper defines source dependence in a structured truth-discovery setting: sources can derive values directly or transitively from a common source, and copying can spread erroneous values. It presents a Bayesian dependence-inference model integrated with iterative truth discovery and reports experiments on synthetic and real data. The paper also cautions that equal values alone do not prove copying: a source may copy only part of an item or independently verify some values. Primary record: [PVLDB PDF](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf), DOI [10.14778/1687627.1687690](https://doi.org/10.14778/1687627.1687690).

**Exact finding used.** Shared values are not sufficient to infer a copy relation; dependence needs a model and can be partial. The paper’s setting assumes structured records and a truth-discovery objective, not open-world natural-language claims.

**Project inference.** A source graph needs relation type, direction, scope, and uncertainty. An `UNKNOWN` origin relation is a valid state; recurrence cannot silently become `DISTINCT`.

**Claim blocked.** The project cannot claim that text overlap, agreement, or repeated publication automatically proves common origin, independent support, or factual truth. It also cannot claim that a simple origin graph transfers unchanged from structured records to web or LLM evidence.

**Residual contribution.** The paper supplies a mature conceptual and algorithmic precedent for source-dependence modeling and shows why partial copying and independent verification need separate representation. It leaves open a narrow, controlled test of supplied origin metadata in a pre-generation interface.

**Disposition: Modify.** Retain common-origin accounting as a scoped design problem; remove any implication that the project introduces source-dependence reasoning as a general mechanism.

### S2 — Dong, Berti-Équille & Srivastava: dynamic copying detection

**Sourced fact.** The dynamic-world PVLDB paper models copying relationships that change over time. It describes why voting can fail when sources copy erroneous or stale values, uses a hidden Markov model to infer copying and change points, and combines time-varying source quality dimensions such as coverage, exactness, and freshness. Primary record: [PVLDB PDF](https://www.vldb.org/pvldb/vol2/vldb09-335.pdf), DOI [10.14778/1687627.1687691](https://doi.org/10.14778/1687627.1687691). The paper notes that copying links in its real example are not all directly observed.

**Exact finding used.** Origin/dependence is temporal and uncertain; a source’s value can change while its relation to other sources changes as well.

**Project inference.** Any project origin field should be time-scoped and auditable. “Same origin” at one capture time cannot be treated as a permanent source property.

**Claim blocked.** A static source-family label cannot support a universal claim about independence, reliability, or freshness. An inferred relationship in a case study is not a verified relation for every source or artifact.

**Residual contribution.** Dynamic copying detection provides the closest formal precedent for temporal origin updates and freshness-aware source treatment. The project can use it to define a later extension, while keeping the near-term study at stipulated, immutable relations.

**Disposition: Defer.** Preserve temporal relation updates as a later research question; do not include learned dynamic-copy inference in the narrow study.

### S3 — Senn: double counting in meta-analysis

**Sourced fact.** Senn’s published BMC article explains how counting the same study more than once, counting multiple aspects or arms without handling dependence, or combining overlapping reports can create spurious precision. It emphasizes transparent, checkable methods and illustrates the issue with published examples. Primary records: [BMC article](https://doi.org/10.1186/1471-2288-9-10), [University of Glasgow repository record](https://eprints.gla.ac.uk/6996/).

**Exact finding used.** The unit being counted must be identified before aggregating observations; repeated reports, arms, or analyses can inflate apparent evidence when correlation is ignored.

**Project inference.** The evidence ledger should preserve every observation while separately tracking artifact identity, underlying origin unit, claim, and aggregation unit. “More rows” must not automatically mean “more support.”

**Claim blocked.** The project cannot say that an append-only ledger, citation count, or report count establishes truth or independent corroboration. Nor can a meta-analysis analogy establish a universal correction factor for web evidence.

**Residual contribution.** Senn supplies the audit discipline: disclose the unit, overlap, uncertainty, and aggregation rule. This is a strong effective-independence analogy, not a new RAG algorithm.

**Disposition: Accept.** Retain the unit-accounting rule and transparency requirement, explicitly labeled as an analogy and not as a direct transfer of medical statistics.

### S4 — Greenberg: citation-network amplification

**Sourced fact.** Greenberg’s BMJ case study reconstructs a citation network around a specific Alzheimer’s/inclusion-body-myopathy claim: 242 papers, 675 citations, and 220,553 citation paths. The analysis reports bias against refuting or weakening papers, amplification through papers without new data, and conversion of a hypothesis into apparent fact through citation alone. The article is a domain-specific network analysis, not a universal prevalence estimate. Primary records: [PubMed](https://pubmed.ncbi.nlm.nih.gov/19622839/), [BMJ DOI](https://doi.org/10.1136/bmj.b2680), [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2714656/).

**Exact finding used.** Citation recurrence can amplify authority independently of new evidence; a citation network can reveal distortion patterns that a raw count hides.

**Project inference.** Recurrence, citation traffic, outlet count, and source diversity need separate fields. A claim-level audit should distinguish a new observation from a copied or citation-only transmission.

**Claim blocked.** “Many citations” cannot be used as a proxy for independent support, factual correctness, or authority. A single case study cannot justify a universal network-bias rate or a claim that every high-recurrence cluster is manipulative.

**Residual contribution.** Greenberg motivates claim-specific citation-network inspection and a provenance-aware recurrence audit. It does not supply a source-origin classifier for natural-language evidence.

**Disposition: Accept.** Retain as a bounded precedent for separating citation recurrence from evidential support; retain the case-study scope.

### S5 — Naphade: paraphrased and redundant group evidence in LLM RAG

**Sourced fact.** Naphade’s arXiv v1 manuscript, submitted 2026-01-08, is labeled with an ACL ARR submission comment and has no accepted venue shown in the checked record. The study uses GroupQA: 1,635 controversial binary questions and 15,058 retrieved documents, with Google Custom Search top-10 retrieval, GPT-4o-generated questions, automated stance labels, and manually checked labels for a sample. The evaluated models are DeepSeek-R1-8B, Gemini-2.5-FL, Llama-3.1-70B-Instruct, and Qwen3-32B. Primary records: [arXiv abstract/status](https://arxiv.org/abs/2601.06189) and [direct PDF](https://arxiv.org/pdf/2601.06189).

**Exact finding used.** Table 4 reports distinct-versus-paraphrased opposing-evidence flip rates as follows: DeepSeek-R1-8B **67.6% vs 76.5%**; Gemini-2.5-FL **63.7% vs 75.6%**; Llama-3.1-70B-Instruct **62.9% vs 69.8%**; Qwen3-32B **67.3% vs 73.7%**. The paper reports a redundancy-associated increase in belief revision in this setup. A separate Llama-3.1-70B leave-one-out attribution check matched the verbal attribution to the causally influential document on 26% of 200 questions.

**Attribution correction.** The 67.6% and 76.5% values belong to DeepSeek-R1-8B. Assigning those values to Llama-3.1-70B-Instruct is incorrect; Llama’s values are 62.9% and 69.8%. The main text says paraphrases were generated with GPT-4o, while an appendix passage names `gpt-4o-mini`; this discrepancy remains unresolved and is recorded below.

**Project inference.** Repetition and paraphrase can affect model belief revision, and verbal citation or attribution may not identify causal document influence. A valid origin-accounting evaluation needs controlled relation labels, duplicate/paraphrase conditions, and a causal or leave-one-out diagnostic.

**Claim blocked.** This unreviewed, model- and task-specific study does not show that all LLMs equate repetition with consensus, that retrieved documents are independent or copied, or that explanation text proves evidence use. “Distinct documents” in the experiment is not a verified distinct-origin label.

**Residual contribution.** Naphade is a close behavioral comparator for the narrow cue experiment and a warning against relying on count or explanation alone. It helps set attribution and redundancy baselines without becoming evidence for real-world source independence.

**Disposition: Modify.** Use the corrected per-model results and label the work an unreviewed ACL ARR working manuscript; treat its relation to origin accounting as an adjacent behavioral result, not a provenance result.

### S6 — NEWS-COPY: noise-robust large-scale deduplication

**Sourced fact.** Silcock, D’Amico-Wong, Yang & Dell present NEWS-COPY in an ICLR 2023 poster. The paper evaluates 27,210 documents, 122,876 positive duplicate pairs, and 973 newspapers from 1920–1977 historical news. It compares hashing, n-gram, locality-sensitive hashing, neural bi-encoder, and reranking approaches on noisy OCR, abridgement, and near-copy material. Primary records: [arXiv](https://arxiv.org/abs/2210.04261), [ICLR poster](https://iclr.cc/virtual/2023/poster/11067), [OpenReview](https://openreview.net/forum?id=bAz2DBS35i), [official code](https://github.com/dell-research-harvard/NEWS-COPY).

**Exact finding used.** The reported adjusted Rand index values are 93.7 for the reranker, 91.5 for the bi-encoder, 73.7 for LSH, and 75.0 for n-gram. The paper reports de-duplication of 10 million documents in 11 hours 45 minutes on one NVIDIA A6000 and finds near duplicates that hashing can miss.

**Project inference.** Reproduction detection needs robust semantic and OCR-noise handling, not only byte or exact lexical matching. A duplicate signal should remain a signal; origin assignment and human review are separate steps.

**Claim blocked.** The project cannot claim deduplication as a new mechanism, nor claim that high text similarity proves a definitive copy relation, shared claim origin, or falsity. NEWS-COPY does not establish source identity or factual correctness.

**Residual contribution.** NEWS-COPY supplies a published scale and evaluation precedent for duplicate clusters. The residual project question is whether a typed reproduction/origin field changes claim accounting or action policy beyond deduplication alone.

**Disposition: Accept.** Use it as direct prior art for near-duplicate detection and as a benchmark-design constraint.

### S7 — Newswire: historical reproduction clusters

**Sourced fact.** Silcock, Arora, Luca D’Amico-Wong & Dell’s Newswire is a NeurIPS 2024 Datasets & Benchmarks Track paper. It constructs a structured database from roughly 138 million front-page article texts and identifies 2.7 million unique public-domain U.S. newswire articles from 1878–1977. The paper reports about 32.1 million reproductions of 2.719 million unique wire articles and uses a neural bi-encoder to handle abridgement and noise. Primary records: [NeurIPS paper page](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html), [arXiv](https://arxiv.org/abs/2406.09490), [direct PDF](https://arxiv.org/pdf/2406.09490), and [official dataset record](https://huggingface.co/datasets/dell-research-harvard/newswire).

**Exact finding used.** In a historical newswire corpus, many outlet appearances can be clustered around a smaller set of reproduced wire articles. The corpus explicitly quantifies reproduction rather than assuming every outlet appearance is an independent source.

**Project inference.** Outlet count must not be treated as origin diversity. A source-family graph can use reproduction clusters as evidence while retaining uncertainty about the underlying claim and about unclustered material.

**Claim blocked.** The project cannot infer independent perspectives, source reliability, or claim truth from the number of outlets. Newswire’s historical coverage does not establish behavior for current web, video transcripts, or arbitrary domains.

**Residual contribution.** Newswire supplies a large, published corpus and a realistic test surface for copy-cluster accounting. It strengthens the case for origin-aware evidence treatment without providing a universal origin oracle.

**Disposition: Accept.** Use for corpus and benchmark design; keep the outlet-count boundary explicit.

### S8 — Li, Padman & Krishnan: source dependence in medical multi-source RAG

**Sourced fact.** This arXiv v1 manuscript was submitted 2026-05-27, with no venue acceptance shown in the checked record. It studies TransplantQA: 1,115 patient questions, 102 handbooks from 23 U.S. centers, and five organ types. The authors report 48,056 grounded answers and 5,730,465 pairwise comparisons, use hierarchical retrieval, and report human judge agreement of κ=0.842. A higher-capacity reference run showed handbook absence reducing answer availability by 13.6 percentage points while pairwise divergence stayed essentially unchanged. Primary records: [arXiv](https://arxiv.org/abs/2605.29084) and [direct PDF](https://arxiv.org/pdf/2605.29084).

**Exact finding used.** Retrieval quality changes the measured prevalence of cross-source disagreement: finding more relevant handbooks can expose disagreement that a weaker retrieval configuration misses. The paper’s five-label relationship taxonomy concerns answer/source relationships, not a copying or common-origin graph.

**Project inference.** A single answer or citation is insufficient to characterize multi-source evidence. Source scope, institutional policy, retrieval omission, and answer divergence need separate fields from origin relation.

**Claim blocked.** The work does not permit a claim that answer disagreement means source copying, that source scope differences are dependence, or that a single-gold evaluation establishes the best answer. Its results are a preprint-specific medical RAG finding, not a general origin-accounting result.

**Residual contribution.** Li et al. provide a close comparator for source-aware retrieval audits, source-set completeness, and disagreement measurement. They motivate a retrieval-control condition in later studies while leaving common-origin relation as a distinct variable.

**Disposition: Modify.** Use as an unreviewed source-dependence comparator; do not collapse its inter-source answer taxonomy into the project’s origin-family vocabulary.

### S9 — RAMDocs: conflicting evidence benchmark

**Sourced fact.** Wang, Prasad, Stengel-Eskin & Bansal present RAMDocs, a benchmark combining ambiguity, misinformation, and irrelevant noise in the same query context, plus MADAM-RAG multi-agent debate. The paper is labeled a COLM 2025 conference paper. It reports evaluation with Llama3.3-70B-Instruct, Qwen2.5-72B-Instruct, and GPT-4o-mini; the main text reports an 11.40-point improvement on AmbigDocs with Llama3.3-70B and a 13.10-point FaithEval improvement with Qwen2.5. Primary records: [arXiv](https://arxiv.org/abs/2504.13079), [direct PDF](https://arxiv.org/pdf/2504.13079), [COLM/OpenReview record](https://openreview.net/forum?id=z1MHB2m3V9), and [official code](https://github.com/HanNight/RAMDocs).

**Exact finding used.** A RAG system can fail when ambiguity, misinformation, noise, and support imbalance co-occur; conflict handling requires more than a binary “agree/disagree” switch.

**Project inference.** Evidence stance, ambiguity, noise, and origin-family relation should be separately typed. A conflict router alone is not equivalent to a source-origin or recurrence accounting layer.

**Claim blocked.** The project cannot claim that generic conflict-aware retrieval is unoccupied prior art, that debate recovers factual truth in arbitrary corpora, or that misinformation labels provide provenance.

**Residual contribution.** RAMDocs supplies a published benchmark condition for stress-testing conflict handling. The remaining project question is whether origin metadata changes accounting under controlled copy/reproduction graphs.

**Disposition: Accept.** Retain as direct conflict-handling prior art and as a benchmark condition, with no origin or truth inference.

### S10 — EvidentialRAG: conflict and uncertainty fusion

**Sourced fact.** EvidentialRAG is an arXiv v1 manuscript submitted 2026-07-11; the checked record shows no venue or acceptance. The method uses a Llama-3-8B-Instruct evaluator to extract/normalize claims and map them to Dirichlet evidence, Llama-3-70B-Instruct for generation, `bge-large-en-v1.5` retrieval, `bge-reranker-v2-m3`, top-k 5, conflict transfer λ=.6, and explicit direct/conflict-aware/abstention routes. In the paper’s CRAG ambiguous-subset table, three-seed averages report hallucination 34.8, conflict resolution 51.2, factuality F1 47.1, and abstention 39.2 for EvidentialRAG; standard CRAG is not a universal win, with Corrective slightly above it on the listed EM/F1. Primary records: [arXiv](https://arxiv.org/abs/2607.10491), [direct PDF](https://arxiv.org/pdf/2607.10491), DOI [10.48550/arXiv.2607.10491](https://doi.org/10.48550/arXiv.2607.10491).

**Exact finding used.** Evidence conflict and uncertainty can be represented before generation with explicit abstention and routing; the reported method treats retrieved chunks equally for source credibility and lists this as a limitation.

**Project inference.** Conflict fusion, uncertainty handling, and origin-family accounting are separate layers. A future matched-budget comparator may test incremental value against an already conflict-aware baseline; that is adjacent/future work, not a required arm in the locked F0/F1/F2 confirmatory family. Calibration remains outside that family absent an explicit probability target and proper scoring rule.

**Claim blocked.** The project cannot claim a vacant “conflict-aware evidence layer,” a general factuality gain, a source-credibility solution, or provenance support from EvidentialRAG. The evaluator/judge setup, 200-response audit, three seeds, and stated credibility limitation constrain transfer.

**Residual contribution.** EvidentialRAG is a close unreviewed comparator and useful baseline for conflict-preserving pre-generation routing. Its limitations sharpen the residual need for source identity, origin relation, and claim-scoped authority.

**Disposition: Modify.** Retain it as a close unreviewed adjacent/future comparator; keep conflict/uncertainty fusion distinct from origin dependence, with no locked-core arm added.

### S11 — Carbonell & Goldstein: MMR and diversity-aware reranking

**Sourced fact.** The SIGIR ’98 ACM record describes maximal marginal relevance (MMR), a diversity-based reranking approach for document reordering and summaries. Primary record: [ACM DOI](https://doi.org/10.1145/290941.291025).

**Exact finding used.** Retrieval selection can trade individual query relevance against redundancy or similarity within the selected set.

**Project inference.** Any proposed set-level retrieval policy needs to compare with established diversity-aware reranking, not only top-k relevance.

**Claim blocked.** A redundancy penalty or “diverse context” objective is not a new mechanism. Diversity also does not prove independent origin, support, or factual correctness.

**Residual contribution.** MMR is a simple, interpretable control for the narrow study and a reminder that source-set selection and origin accounting address different problems.

**Disposition: Accept.** Include MMR or an equivalent diversity control in later matched-budget comparisons.

### S12 — Lee et al.: SetR set-wise passage selection

**Sourced fact.** Lee, Jo, Park & Lee’s ACL 2025 paper proposes set-wise passage selection that identifies information requirements and selects a collectively covering set, with an explicit goal of reducing redundancy. The ACL Anthology record identifies it as an ACL 2025 main-conference paper. Primary record: [ACL Anthology](https://aclanthology.org/2025.acl-long.861/) and [PDF](https://aclanthology.org/2025.acl-long.861.pdf).

**Exact finding used.** Retrieval can be optimized at the set level for collective coverage rather than independent passage ranking; the paper reports gains on multi-hop RAG benchmarks.

**Project inference.** “Select a non-redundant evidence set before generation” has direct published precedent. The project’s residual question is relation-aware accounting, not set selection itself.

**Claim blocked.** The project cannot claim set-wise selection, redundancy reduction, or collective coverage as a new responsibility. SetR does not establish source origin, copy relation, or claim truth.

**Residual contribution.** SetR is a strong baseline for evidence-packet selection and a clean control against which an origin cue could be evaluated.

**Disposition: Accept.** Treat as direct adjacent prior art and baseline candidate.

### S13 — Verma et al.: NEST

**Sourced fact.** NEST is listed in the ACL 2026 Industry Track. It separates recall amplification from precision selection using nested retrieval scopes and a survival-consistent MRR selection step intended to remove redundancy. The ACL record reports gains up to +2.4 EM, +2.1 F1, and +6.8 retrieval recall points, with 12–18 ms additional latency, on WebQuestions, HotpotQA distractor, and a proprietary InternalQA benchmark. Primary record: [ACL Anthology](https://aclanthology.org/2026.acl-industry.35/) and [DOI](https://doi.org/10.18653/v1/2026.acl-industry.35).

**Exact finding used.** Redundancy pruning can be integrated with recall-preserving retrieval selection in a published RAG framework.

**Project inference.** A pre-generation layer that separates recall from selection is not by itself novel. It must show why an origin relation adds value beyond retrieval diversity and survival controls.

**Claim blocked.** The project cannot claim training-free redundancy removal, recall/precision separation, or MRR selection as an unoccupied design space. NEST’s benchmarks do not test source-family inference.

**Residual contribution.** NEST offers a recent published retrieval baseline and a way to control context-set construction when isolating origin metadata.

**Disposition: Accept.** Add to the adjacency/baseline register; preserve the no-origin-inference boundary.

### S14 — Cho & Lee: RARE

**Sourced fact.** RARE’s arXiv v2 record (submitted 2026-04-21, revised 2026-06-30) says it was accepted to ACL 2026 Main Conference. The record presents a redundancy-aware evaluation framework that decomposes documents into atomic facts, tracks overlap, and constructs RedQA for finance, legal, and patent corpora. It reports a strong-retriever PerfRecall@10 decline from 66.4% on 4-hop General-Wiki to 5.0–27.9% at 4-hop depth in the high-similarity settings. Primary record: [arXiv](https://arxiv.org/abs/2604.19047) and [direct PDF](https://arxiv.org/pdf/2604.19047). An ACL publication page was not located during this pass, so the status remains “accepted; publication page pending.”

**Exact finding used.** Standard QA benchmarks can misrepresent retrieval behavior when documents overlap heavily; fact-level redundancy tracking changes what retrieval quality means in such corpora.

**Project inference.** Document count and benchmark retrieval recall are not evidence diversity. Atomic fact overlap is a useful input to origin-accounting evaluation but is not itself provenance.

**Claim blocked.** The project cannot claim redundancy-aware evaluation or fact-level overlap tracking as new. RARE does not identify actual copying, common authorship, or factual truth.

**Residual contribution.** RARE gives a near-direct benchmark-design precedent for high-similarity corpora and an evaluation control for the narrow relation-cue study.

**Disposition: Accept.** Use as accepted ACL adjacency, while preserving the qualified publication-status wording until the venue page is available.

### S15 — Ross et al.: controlled redundancy and diversity in RAG

**Sourced fact.** Ross, Koopman, van der Vegt & Zuccon’s arXiv v1 was submitted 2026-08-14 in Information Retrieval; the record shows no venue or acceptance. The paper uses FictionalQA to suppress parametric prior answers and compares exact duplicates, LLM paraphrases of one document, and diverse documents from different genres while controlling whether the answer is present in exact or rephrased form. It reports no significant correctness improvement from duplicates or paraphrases and a 17–47% improvement from diverse documents in its setup. Primary records: [arXiv abstract/status](https://arxiv.org/abs/2608.13956) and [direct PDF](https://arxiv.org/pdf/2608.13956).

**Exact finding used.** Retrieved-set redundancy and diversity can have different effects; exact duplicate or paraphrase recurrence is not interchangeable with diverse evidence under this synthetic control.

**Project inference.** The project must not assume that repetition always persuades or always harms. A useful study needs matched evidence content, explicit origin/relation controls, and model/task-specific outcomes.

**Claim blocked.** This current unreviewed manuscript does not establish a universal RAG law, verified source independence for its “diverse” documents, or transfer to real-world claims. It also cannot settle the differing behavior observed in Naphade because the tasks, controls, models, and outputs differ.

**Residual contribution.** Ross et al. provide a close current comparator and a controlled design for separating repetition, paraphrase, and diversity. Their study can inform baseline conditions without being treated as settled evidence.

**Disposition: Modify.** Include as an unreviewed working manuscript and require a comparison of its controlled redundancy conditions when designing the project’s study.

### S16 — Schelpe: byte-exact deduplication in RAG

**Sourced fact.** Schelpe’s arXiv v1, submitted 2026-05-10, calls itself a preprint and studies byte-exact chunk deduplication across three regimes. The abstract reports context reductions of 0.16% on 22.2 million BeIR passages, 24.03% on constructed enterprise patterns, and 80.34% on multi-turn WildChat, plus a cross-vendor five-judge evaluation claiming no measurable quality regression after a human-in-the-loop audit. Primary record: [arXiv](https://arxiv.org/abs/2605.09611) and [direct PDF](https://arxiv.org/pdf/2605.09611).

**Exact finding used.** Byte-exact deduplication can materially reduce context in some high-redundancy regimes while preserving the paper’s measured quality metrics; the paper does not present byte deduplication as a new primitive.

**Project inference.** Any origin-aware pipeline needs exact dedup as a cheap control, but exact dedup does not address paraphrase, OCR noise, syndicated copy, or latent common origin.

**Claim blocked.** The project cannot claim byte deduplication or deterministic duplicate removal as a novel layer. The author-reported cross-vendor result is a preprint result, not independently re-run here and not evidence of semantic independence.

**Residual contribution.** Schelpe supplies a current adjacency point for cost/quality controls and a reminder to quantify exact duplicate removal before assigning complexity to semantic origin modeling.

**Disposition: Modify.** Include as an unreviewed comparator, with no reliance on its paid-provider measurements beyond the reported bounded finding.

### S17 — Cochrane: reports versus studies

**Sourced fact.** The current Cochrane Handbook chapter says a single study can have multiple reports, that multiple reports should be linked and collated so the study rather than the report is the unit of interest, and that secondary reports should not be discarded because they may contain additional design or outcome information. It lists practical identifiers such as trial ID, authors, location, interventions, participant numbers, and date. Primary record: [Cochrane Handbook chapter 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04), especially sections 4.2.3 and 4.6.2.

**Exact finding used.** Reports and studies are different units; preserving secondary reports while avoiding multiple counting is a documented evidence-synthesis rule.

**Project inference.** The ledger can preserve raw artifacts and still aggregate by a declared origin or study-like unit. Unknown linkage should remain visible and should not be counted as distinct by default.

**Claim blocked.** The project cannot claim that its ledger or relation labels invent the reports-versus-unit distinction. Cochrane’s medical review rule cannot be transferred as an automatic truth rule for video, web, or LLM evidence.

**Residual contribution.** Cochrane supplies a clear operational analogy for grouping, preserving, documenting uncertainty, and choosing an analysis unit.

**Disposition: Accept.** Use as a methodological guardrail and explicit analogy.

### S18 — Strittmatter, Pilditch & Lagnado: human dependence reasoning

**Sourced fact.** The ETH repository lists the 2024 work as a conference paper with a published open-access version. Its abstract states that independent corroborating evidence should provide stronger support than dependent evidence, that overlooking dependence can produce double-counting and overestimation, and that the authors test people’s sensitivity to dependence in fictitious scenarios, including differing source reliabilities. Primary record: [ETH Research Collection](https://www.research-collection.ethz.ch/entities/publication/0659291b-e61d-4afe-9932-a4aeec8b9705), with [published PDF](https://www.research-collection.ethz.ch/bitstreams/763c09a6-4bfc-49fb-af7f-8bd8f029cb82/download).

**Exact finding used.** Dependence is a recognized factor in evidential reasoning, and perception of dependence need not equal correct incorporation of dependence.

**Project inference.** An interface should expose relation uncertainty and test whether a supplied relation cue changes accounting; displaying a relation is not proof that users or models use it correctly.

**Claim blocked.** This human-behavior analogy does not establish a RAG effect, an origin detector, or a universal benefit of showing provenance. It cannot support a claim that readers will make better decisions merely because the graph is visible.

**Residual contribution.** The paper motivates a later human evaluation with calibration, correction, and decision outcomes kept separate. It reinforces the distinction between relation perception and relation incorporation.

**Disposition: Accept.** Retain as a bounded effective-independence analogy and as a reason to defer human-effect claims until measured.

### S19 — Zhang, Ives & Roth: natural-language claim provenance

**Sourced fact.** Zhang, Ives & Roth’s ACL 2020 paper defines a provenance graph for a natural-language claim, models provenance inference primarily as information extraction addressed with textual entailment, and evaluates the approach on two benchmark datasets. The ACL Anthology record identifies it as a published ACL 2020 paper, pages 4416–4426. Primary record: [ACL Anthology](https://aclanthology.org/2020.acl-main.406/) and [PDF](https://aclanthology.org/2020.acl-main.406.pdf).

**Exact finding used.** Natural-language claim provenance and report/paraphrase evolution have a direct published representation and inference precedent. The paper’s inferred provenance graph is not the project’s supplied benchmark relation field.

**Project inference.** The current residual question must be framed as supplied typed origin metadata versus a byte-identical explicit rule, not as provenance discovery or a new claim-provenance graph. Inferred relations, stipulated relations, derivation, and claim stance remain separate vocabularies.

**Claim blocked.** The project cannot imply that natural-language provenance graphs, common-origin reasoning over reports, or provenance inference are unoccupied. It cannot use a result under stipulated labels as evidence that the model inferred a real source path.

**Residual contribution.** S19 is the closest direct published comparator for the representation neighborhood. It sharpens the boundary around the narrow F2-minus-F1 observable-condition hypothesis without adding a new study arm.

**Disposition: Modify.** Add S19 to the manuscript, prospectus, reader source route, claim matrix, and loop-1 ledger receipt; preserve the supplied-relation/no-provenance-discovery boundary.

### S20 — Pochampally et al.: correlations beyond literal copying

**Sourced fact.** Pochampally, Das Sarma, Dong, Meliou, and Srivastava’s SIGMOD 2014 paper studies data fusion when source correlations are broader than literal copying. It identifies positive correlation caused by common extraction rules without copying, and negative correlation caused by complementary source domains or extractors that focus on different information. It formalizes correlation-aware fusion and evaluates the approach on real-world and synthetic data. Primary records: [ACM DOI](https://doi.org/10.1145/2588555.2593674) and the authors’ [primary PDF](https://people.cs.umass.edu/~ameli/projects/dataIntegration/papers/corrFusion-SIGMOD2014.pdf).

**Exact finding used.** A binary `dependent`/`independent` split is too coarse for source fusion: sources may be correlated for different reasons, and correlation may be positive or negative. Common extraction processes can create dependence without direct copying; complementary sources can be negatively correlated while both remain useful.

**Project inference.** The framework’s future relation vocabulary should be typed and scoped rather than treating every relation as a copy edge. Candidate extensions include common-process, complementary, and unresolved-dependence relations with direction, time, confidence, and relation provenance. The current `DPND`/`INDP`/`UNKN` states are an intentionally narrow accounting device for the stipulated synthetic diagnostic, not a complete dependence taxonomy.

**Claim blocked.** The project cannot present three synthetic relation states as a general source-dependence ontology, call `INDP` real-world independence, or transfer structured truth-fusion performance to natural-language claims or LLM behavior. It cannot infer common extraction rules from agreement alone.

**Residual contribution.** S20 closes the demonstrated consolidation gap from the overnight review and strengthens the reason to preserve typed relation uncertainty. It does not add a new confirmatory study arm; the narrow F2-versus-F1 test remains a supplied relation-cue diagnostic on a stipulated graph.

**Disposition: Accept with boundary.** Add S20 to the main ledger, bibliography, and manuscript prior-art paragraph. Preserve the current narrow three-state protocol while recording graded/typed dependence as a future extension rather than claiming it is solved.

## Retrieval deduplication and closest adjacent work

The retrieval boundary now has a layered baseline set:

1. **Exact/byte control:** byte-exact chunk removal (S16).
2. **Noisy and semantic reproduction detection:** NEWS-COPY and Newswire (S6–S7).
3. **Diversity and set construction:** MMR, SetR, and NEST (S11–S13).
4. **High-similarity evaluation:** RARE (S14).
5. **Controlled redundancy effects:** Ross et al. (S15).
6. **Conflict and uncertainty:** RAMDocs and EvidentialRAG (S9–S10).
7. **Natural-language claim provenance:** Zhang, Ives & Roth (S19); inferred provenance is not supplied origin metadata.
8. **Origin/source-dependence:** Dong et al. and Li et al. (S1–S2, S8).

These layers answer different questions. Deduplication asks whether retrieved artifacts overlap. Set selection asks which items jointly cover a query. Conflict handling asks how evidence stances or uncertainties interact. Source dependence asks whether observations share an origin or transmission path. The project must not use one layer as a substitute for another.

The two closest current contrasts are Naphade versus Ross. Naphade reports more belief revision under paraphrased opposing evidence in its GroupQA setup, while Ross reports no significant correctness gain from duplicate/paraphrased sets and a gain from diverse genres in FictionalQA. The results are not contradictory evidence about a single law: they use different question construction, retrieval, model families, labels, context controls, and outcomes. The correct project inference is to test matched conditions rather than pick one headline as universal.

## Effective-independence analogies

The following analogies are useful because they formalize or operationalize a repeated-observation problem:

- **Cochrane:** reports must be linked to underlying studies while preserving secondary reports.
- **Senn:** double-counting shared studies, arms, or analyses can create spurious precision.
- **Pochampally et al.:** source correlation can arise without copying and can be complementary or negative; a binary dependence label can erase useful structure.
- **Dong et al.:** copied values and dynamic source relations alter truth-discovery weights.
- **Greenberg:** citation traffic can amplify authority without adding data.
- **Strittmatter et al.:** dependent evidence can be perceived and incorporated differently by human reasoners.

The analogy stops at the unit/accounting principle. A video transcript, a news article, a citation, a model-generated paraphrase, and a randomized trial report are not the same object. None of these sources licenses an automatic independence detector for the project. The project should state “effective independence for this stipulated graph and task” only if it defines the unit, relation, uncertainty state, and aggregation rule.

## Closest working manuscripts and status discipline

Working manuscripts are useful for overlap detection and study design, but they are not treated as settled technical evidence. Their exact status is recorded here:

| Manuscript | Status visible in primary record | Narrow use | Boundary |
| --- | --- | --- | --- |
| Naphade, [arXiv:2601.06189](https://arxiv.org/abs/2601.06189) | arXiv v1; ACL ARR submission comment; no acceptance shown | Redundancy, paraphrase, and attribution comparator | Do not treat “distinct documents” as distinct origins; use corrected per-model Table 4 values |
| Li, Padman & Krishnan, [arXiv:2605.29084](https://arxiv.org/abs/2605.29084) | arXiv v1; no venue acceptance shown | Source-set completeness and cross-source divergence comparator | Inter-source answer relation is not common-origin relation |
| Hossain et al., [arXiv:2607.10491](https://arxiv.org/abs/2607.10491) | arXiv v1; no venue or acceptance shown | Conflict/uncertainty baseline | No source credibility/provenance; judge and benchmark limitations |
| Ross et al., [arXiv:2608.13956](https://arxiv.org/abs/2608.13956) | arXiv v1 submitted 2026-08-14; no venue or acceptance shown | Controlled duplicate/paraphrase/diversity comparator | Synthetic FictionalQA and unreviewed status limit transfer |
| Schelpe, [arXiv:2605.09611](https://arxiv.org/abs/2605.09611) | arXiv v1; record calls it a preprint | Byte-dedup cost/quality control | Exact overlap only; author-reported provider panel |
| Xia et al., [arXiv:2606.06758](https://arxiv.org/abs/2606.06758) | arXiv working preprint carried forward from the adjacent-fields map; publication status not re-established in this pass | Evidence-utilization/source-influence comparator | Do not cite as venue-reviewed in this delta |
| Nematov et al., [arXiv:2507.04480](https://arxiv.org/abs/2507.04480) | arXiv working preprint carried forward from the adjacent-fields map | Source attribution comparator | Attribution is not origin-family discovery |
| Louck, [arXiv:2606.24322](https://arxiv.org/abs/2606.24322) | arXiv working preprint carried forward from the adjacent-fields map | Provenance laundering threat model | Threat-model adjacency, not settled efficacy evidence |
| ProvenanceGuard, [arXiv:2606.18037](https://arxiv.org/abs/2606.18037) | arXiv working preprint carried forward from the adjacent-fields map | Provenance/memory security adjacency | Do not treat the threat model as a validated deployment result |

The accepted or published adjacent records in this delta (NEWS-COPY, Newswire, SetR, NEST, MMR, RAMDocs, and the named historical sources) are still bounded by their task and corpus. Acceptance status does not turn their constructs into a universal truth or origin solution.

## Corrected novelty boundary and dispositions

| Proposed wording or mechanism | Disposition | Corrected wording |
| --- | --- | --- |
| “A novel universal pre-generation discrimination layer” | Reject | A provisional synthesis and evaluation agenda that connects established mechanisms under explicit boundaries |
| “Source-aware RAG or conflict handling is new” | Reject | Source-aware, conflict-aware, and uncertainty-aware RAG are established adjacent mechanisms; compare against them |
| “Deduplication or redundancy-aware retrieval is new” | Reject | Exact, semantic, noisy, diversity-aware, and set-wise retrieval controls are established; origin relation remains separate |
| “More citations, outlets, or repeated reports mean more independent support” | Reject | Recurrence must be separated from origin relation and support; copied or overlapping reports require grouping/uncertainty |
| “Distinct retrieved documents are independent origins” | Modify | Treat distinctness as a task-defined document property unless an origin relation is separately supplied or inferred with uncertainty |
| “Conflict, disagreement, or paraphrase reveals copying” | Modify | Record evidence interaction and possible origin relation separately; do not infer copying from stance or similarity alone |
| “Supplied typed origin metadata improves accounting beyond a rule-only control” | Accept | Retain as the narrow observable-condition hypothesis on stipulated synthetic graphs |
| “A positive cue effect demonstrates provenance discovery or real-world independence” | Reject | A positive cue effect would be model/task/format-specific behavior under supplied labels |
| “The framework improves human decisions or reliance” | Defer | Require a separate human study with correction, calibration, workload, and decision outcomes |
| “Automated origin inference solves common-origin uncertainty” | Defer | Treat learned relation inference as a later, independently validated component |
| “An append-only ledger guarantees reliable evidence” | Reject | A ledger preserves observations and revisions; it does not establish correctness or authority |
| “The project is validated, enterprise-ready, or deployment-proven” | Reject | The current state is a thought-piece framework plus an unrun study protocol |

### Accept

- Keep typed relation vocabularies distinct.
- Keep `UNKNOWN` as an explicit origin state.
- Keep raw acquisition artifacts immutable while allowing interpretation/disposition revision.
- Retain NEWS-COPY, Newswire, MMR, SetR, NEST, RARE, RAMDocs, and conflict-aware methods as optional future controls or adjacency, not required arms in the locked F0/F1/F2 study.
- Retain source copying, double-counting, citation amplification, and evidence-dependence as bounded prior art and analogies.

### Modify

- Replace unqualified “independence” with a declared origin relation or “effective independence under a stipulated graph.”
- Separate source scope and answer divergence from copying/dependence.
- Report model-specific Naphade results with corrected attribution and unreviewed status.
- Treat exact deduplication, diversity/set-selection, and conflict-aware baselines as adjacent/future comparator candidates; do not add them to the locked F0/F1/F2 study without a separate decision.

### Defer

- Learned source-origin inference in open corpora.
- Time-varying copy detection beyond stipulated graph updates.
- Human reliance, trust, correction, and decision-quality effects.
- Deployment, governance, enterprise readiness, or cross-domain transfer claims.

### Reject

- Universal mechanism novelty.
- Count-based corroboration.
- Truth, authority, or independence inferred from provenance, citations, conflict resolution, or ledger presence.
- Any claim that an unreviewed working manuscript settles a general model behavior.

## Unresolved uncertainties and required follow-up

1. **Naphade generation attribution:** the main text names GPT-4o for paraphrase generation, while an appendix passage names `gpt-4o-mini`. Preserve the discrepancy until the authors’ exact released artifact or a later version resolves it.
2. **Naphade source relation:** the experiment’s “distinct” documents are not verified independent origins. No conclusion about real-world copying should be drawn from the table.
3. **Naphade model naming:** the shorthand “Gemini-2.5-FL” should be retained as printed until the paper clarifies the exact model endpoint/version.
4. **Dynamic dependence:** Dong et al. show that copying can change over time, while real examples can have unobserved links. The narrow project study should use immutable, supplied relations before attempting temporal inference.
5. **Semantic deduplication:** NEWS-COPY’s strong cluster metrics are corpus-specific. False merges and missed relations remain possible for paraphrase, translation, summarization, or shared templates.
6. **Newswire coverage:** the historical corpus is valuable but not a general model of current web, broadcast, or transcript ecosystems. Reproduction clusters do not label claim truth.
7. **Source-dependence taxonomy:** Li et al.’s five labels describe cross-source answer relationships, not derivation or common-origin edges. Mapping between them requires a separate schema decision.
8. **Conflict versus origin:** RAMDocs and EvidentialRAG evaluate ambiguity, misinformation, noise, conflict, and uncertainty. Those axes can coexist with origin relation but cannot substitute for it.
9. **Working-manuscript status:** Naphade, Li et al., EvidentialRAG, Ross et al., and Schelpe are used for overlap and design comparison only. RARE is marked accepted to ACL 2026 in arXiv but lacks a venue page in this pass; retain qualified wording.
10. **Retrieval-set effects:** Naphade and Ross use different datasets, retrieval controls, models, and outcomes. A matched project experiment must preregister which condition is varied and which outcome is estimand.
11. **Human transfer:** Senn, Cochrane, and Strittmatter et al. motivate accounting and dependence checks but do not predict model or user behavior in Signal Foundry.
12. **Relation-label reliability:** a future study must report label construction, graph generation, relation visibility, ambiguity, and leakage controls. A supplied label is an experimental treatment, not an observed external fact.
13. **Truth boundary:** no source reviewed here licenses a claim that the proposed layer identifies factual truth in open-world material. Keep support, authority, provenance, and origin separate.
14. **Structured-correlation boundary:** Pochampally et al. study structured data fusion and source correlations, not natural-language claim provenance or LLM cue use. Use the paper to narrow the relation vocabulary, not to claim direct empirical transfer.

## Near-term research guardrail

The current protocol can remain narrow if it uses a frozen, stipulated graph and makes the treatment explicit:

```text
same evidence packet
  ├─ F1: explicit rule-only origin accounting
  └─ F2: same rule + supplied typed origin relation
       ↓
  one frozen model, one task, fixed prompt/token/cost budget
       ↓
  false-corroboration accounting, relation-use diagnostic, descriptive confidence/abstention as separate endpoints
```

The treatment must not be described as a provenance detector. A null, negative, or direct-code effect is plausible. A positive effect would support only the bounded observable-condition hypothesis for the stipulated graph, model, task, label format, and prompt.

For the locked F0/F1/F2 confirmatory core, the required comparison is the relation-free rule-only condition with explicit `UNKNOWN` origin cases. Exact/byte deduplication, diversity-aware or set-wise retrieval controls such as MMR/SetR, and conflict-aware systems such as RAMDocs/EvidentialRAG are adjacent or future comparators, not required added arms. Calibration is excluded from the confirmatory family unless the study declares an explicit probability target and a proper scoring rule; descriptive confidence and abstention remain separate endpoints.

This guardrail preserves the useful contribution—testing whether a visible typed origin cue changes accounting—without inheriting claims that the reviewed prior art already blocks.

## Primary URL index

For audit convenience, the primary technical records used in this delta are collected here:

- [Dong et al. static source dependence](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf) and [dynamic copying](https://www.vldb.org/pvldb/vol2/vldb09-335.pdf);
- [Senn](https://doi.org/10.1186/1471-2288-9-10), [Greenberg PubMed](https://pubmed.ncbi.nlm.nih.gov/19622839/), and [Cochrane chapter 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04);
- [Naphade](https://arxiv.org/abs/2601.06189), [Li/Padman/Krishnan](https://arxiv.org/abs/2605.29084), [RAMDocs](https://arxiv.org/abs/2504.13079), and [EvidentialRAG](https://arxiv.org/abs/2607.10491);
- [NEWS-COPY](https://iclr.cc/virtual/2023/poster/11067) and [Newswire](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html);
- [Zhang, Ives & Roth, ACL 2020 natural-language claim provenance](https://aclanthology.org/2020.acl-main.406/);
- [Pochampally et al., SIGMOD 2014, Fusing Data with Correlations](https://doi.org/10.1145/2588555.2593674) and [primary PDF](https://people.cs.umass.edu/~ameli/projects/dataIntegration/papers/corrFusion-SIGMOD2014.pdf);
- [MMR](https://doi.org/10.1145/290941.291025), [SetR](https://aclanthology.org/2025.acl-long.861/), [NEST](https://aclanthology.org/2026.acl-industry.35/), and [RARE](https://arxiv.org/abs/2604.19047);
- [Ross et al.](https://arxiv.org/abs/2608.13956) and [Schelpe](https://arxiv.org/abs/2605.09611);
- [Strittmatter et al.](https://www.research-collection.ethz.ch/entities/publication/0659291b-e61d-4afe-9932-a4aeec8b9705).
