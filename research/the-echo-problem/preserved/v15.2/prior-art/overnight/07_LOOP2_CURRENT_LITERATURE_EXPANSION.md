# Loop 2: Current-literature expansion and terminology stress test

Prepared 2026-08-18 for the Pattern Recognition / Discrimination Layer project.

This report re-reads the current package, especially [`PAPER_PROSPECTUS_V0.md`](../../PAPER_PROSPECTUS_V0.md), [`ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`](../../ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md), [`PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md`](../../PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md), [`THOUGHT_PIECE_V14.md`](../../../source/THOUGHT_PIECE_V14.md), and the Loop 1 theory and empirical red-team reports. It expands the search through 2024–2026 primary or authoritative sources, with emphasis on the exact origin-accounting intervention and its oracle-cue framing.

The labels used below are deliberate:

- **[S] Sourced evidence** means a bibliographic fact, method, result, or limitation stated in the linked paper, standard, or official research record.
- **[I] Inference** means a conclusion drawn by comparing those sources with the project package.
- **[H] Hypothesis** means a possible contribution or empirical expectation that remains untested.

This is a targeted novelty audit, not a systematic review, patentability opinion, or claim that an exhaustive search found no other work.

## Answer-first verdict

### The broad “discrimination layer” claim does not survive the 2026 literature

**[I]** The project cannot credibly present a new general layer for “evidence before generation,” source-aware selection, provenance, claim/evidence reasoning, adaptive acquisition, or evidence-grounded action. The surrounding literature has become substantially more integrated since the first prospectus:

- **HydraRAG** combines graph topology, text evidence, source reliability, and cross-source corroboration in a training-free agentic RAG system.
- **CONFACT** evaluates conflicting evidence and source credibility in RAG fact-checking.
- **ProvenanceGuard** treats claim support and exact source ownership as separate axes in multi-tool agent traces.
- **GenProve** and **TROVE** type fine-grained provenance relations such as quotation, compression, and inference.
- **CLUE** uses claim–evidence and inter-evidence conflict/agreement relations to explain uncertainty.
- **Xia’s matched-condition evidence-utilization protocol**, **Can Small Language Models Use What They Retrieve?**, and **When Iterative RAG Beats Ideal Evidence** use matched no-context/gold-oracle/contextual conditions to isolate whether and how models use supplied evidence.
- **Context Is Not Control** is an unreviewed but unusually close working manuscript: it tests whether explicit source-status/admissibility records change behavior in controlled synthetic tasks and explicitly warns that this is a boundary-conditioned cue-use test, not proof of intrinsic inference.
- Earlier constraining work already covered Pendo, ProVe, PaperTrail, source-reliability RAG, adaptive search, memory, human evidence interfaces, and provenance standards; see Loop 1 for the full audit.

**[S]** These are not merely component-level ancestors. They occupy the same integrated responsibility surface: structured evidence, relation or provenance metadata, source comparison, uncertainty/abstention, dynamic acquisition, or action gating. The project therefore has no defensible basis for saying that no prior framework covers the responsibility.

### The narrow origin-accounting study remains viable, but only as a cue-use benchmark

The strongest surviving first-paper claim is:

> **On newly authored fictional evidence bundles with a stipulated provenance graph, and for a frozen model under matched evidence and token budgets, adding an explicit typed origin-relation cue (`dependent`, `independent-as-stipulated`, or `unknown`) to the same origin-counting rule may reduce false-corroboration errors relative to the rule-only condition, without exceeding a preregistered loss in valid-origin recall.**

For the current protocol, make the candidate recall guard explicit in the paper: the proposed primary analysis uses a **5-percentage-point non-inferiority margin** for valid-origin recall. If that margin changes, it must be changed before efficacy results are inspected.

This is a **representation/use diagnostic**. It is not a provenance-inference result, an independence result, a truth result, a consensus result, a human-decision result, a routing result, or a validation of the full “layer.” The protocol’s own F2-versus-F1 contrast is the right unit of novelty: the same evidence, same rule, same output contract, and same resources, with the typed relation field as the focal change.

**[I]** Even this narrow claim is not a clean-sheet mechanism. Current source-boundary, source-ownership, origin-bound-memory, conflict-modeling, and oracle-context work make the *design pattern* familiar. What can still be distinct is the combination of:

1. a preregistered **false-corroboration** endpoint rather than generic answer accuracy;
2. a matched **rule-only control** that separates relation metadata from the instruction to count origins;
3. an explicit `unknown` state that is not silently treated as independent;
4. a provenance-controlled, origin-family-split bundle generator; and
5. a valid-origin recall safety endpoint plus declared stop/retire rules.

That is a candidate benchmark/measurement contribution, not a new “layer.” It survives only if the study is honest about its oracle status and if the effect survives leakage, label noise, model, order, style, and domain controls.

### The exact narrowest paper language

**Recommended title:**

> **Origin-Relation Cue Use in Evidence Bundles: A Controlled False-Corroboration Benchmark**

Acceptable alternatives:

- **Using Stipulated Provenance Relations to Audit Origin Counting in Language Models**
- **A Matched Oracle-Cue Test for Origin Accounting in Evidence Bundles**
- **Do Typed Origin Relations Change Evidence Counting? A Synthetic Cue-Use Study**

Avoid putting “discrimination layer,” “evidence before generation,” “independent corroboration,” “trust,” or “decision quality” in the title of this first paper. Those terms describe a larger program or import claims that the study cannot identify.

## Search protocol and cutoff

### Scope and source hierarchy

**Search cutoff:** 2026-08-18, inclusive. The search prioritized work published or publicly released from 2024 through the cutoff, while retaining older direct precedents already identified in Loop 1.

**Primary/authoritative routes used:**

- ACL Anthology and official ACL conference records for ACL, Findings, EACL, NAACL, EMNLP, and related papers;
- official IJCAI proceedings and DOI records;
- official CHI/ACM DOI records where available;
- NeurIPS official proceedings for the existing A-Mem precedent;
- arXiv records and author/replication repositories for 2026 work not yet assigned a peer-reviewed venue, explicitly labeled as preprints or working manuscripts;
- official standards or publisher pages for inherited provenance/decision-support precedents.

**Queries included combinations of:**

- `origin dependence`, `common origin`, `source independence`, `false corroboration`, `corroboration`, `sybil corroboration`;
- `typed provenance`, `source relation`, `source ownership`, `claim evidence relation`, `fine-grained provenance`;
- `oracle evidence`, `gold context`, `oracle retrieval`, `evidence utilization`, `retrieval utilization`;
- `conflicting evidence`, `source credibility`, `cross-source verification`, `source-aware fact checking`;
- `source boundary`, `source admissibility`, `memory poisoning`, `origin-bound authority`;
- `null result`, `closed-book outperforms oracle`, `retrieval hurts`, `simple baseline`, `no behavioral change`.

### Inclusion and exclusion

Included works had to be a primary research paper, official proceedings record, standard, or direct research artifact materially relevant to at least one of the following: supplied provenance/origin relations; source-aware evidence selection; claim-level attribution; oracle-context or matched evidence-use evaluation; conflict/corroboration; or negative/null results that bound the intervention.

Blogs, vendor announcements, social-media posts, and search snippets were not used as evidence for claims. An obscure working manuscript was retained only when it was directly close to the proposed intervention; its non-peer-reviewed status is stated. Search hits that merely use “discrimination” in a GAN/classifier sense were treated as terminology evidence, not conceptual precedent.

### Search limitation

**[I]** The statement “no paper has tested exactly F2 versus F1 on false corroboration with stipulated origin graphs” is a bounded search inference, not an absence finding. Current preprints may be incomplete, indexed under different terms, or posted after this cutoff. The manuscript must say “we did not locate a peer-reviewed study that isolates this exact contrast in the searched sources,” not “we are the first.”

## Closest-work comparison matrix

The matrix distinguishes direct technical overlap from the residual difference that could matter for the proposed study.

| Work and verified record | What the source actually supplies [S] | Overlap with the proposed origin-cue protocol | Difference and disposition [I] |
|---|---|---|---|
| **Xingyu Tan, Xiaoyang Wang, Qing Liu, Xiwei Xu, Xin Yuan, Liming Zhu & Wenjie Zhang, “HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning,” EMNLP 2025.** DOI [10.18653/v1/2025.emnlp-main.730](https://doi.org/10.18653/v1/2025.emnlp-main.730); [ACL record](https://aclanthology.org/2025.emnlp-main.730/) | HydraRAG combines graph topology, document semantics, source reliability, agent-driven exploration, and a tri-factor cross-source verification step involving source trustworthiness, cross-source corroboration, and entity-path alignment. It reports experiments on seven benchmark datasets. | It is the closest current integrated RAG precedent for treating source relations and cross-source agreement as more than relevance. “Corroboration” is already an explicit computational operation. | It learns/executes retrieval and reasoning over real benchmark evidence; it does not isolate a supplied `dependent`/`independent`/`unknown` relation cue against a rule-only control. **Must cite and use as a strong integrated baseline.** Do not claim source-aware corroboration is new. |
| **Ziyu Ge, Yuhao Wu, Daniel Wai Kit Chin, Roy Ka-Wei Lee & Rui Cao, “Resolving Conflicting Evidence in Automated Fact-Checking: A Study on Retrieval-Augmented LLMs,” IJCAI 2025.** DOI [10.24963/IJCAI.2025/1073](https://doi.org/10.24963/IJCAI.2025/1073); [official proceedings](https://www.ijcai.org/proceedings/2025/1073) | Introduces CONFACT, pairs claims with conflicting information from sources of varying credibility, and studies credibility information in retrieval and generation. The paper reports vulnerabilities when conflicts are present and notes that automatically estimated credibility can add noise relative to expert-verified labels. | It directly tests the need to distinguish evidence relationships rather than aggregate all retrieved text. It is a current comparator for conflict, source credibility, and authority/relevance separation. | Credibility and media background are not origin dependence. It does not treat a repeated report as a copied origin or maintain `unknown`. **Must cite; add a credibility-weighting/conflict baseline and do not equate origin relation with source trust.** |
| **Ander Alvarez, Santhiya Rajan, Samuel Mugel & Román Orús, “ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents,” arXiv 2026.** [arXiv:2606.18037](https://arxiv.org/abs/2606.18037); arXiv-issued DOI [10.48550/arXiv.2606.18037](https://doi.org/10.48550/arXiv.2606.18037); no peer-reviewed DOI located by cutoff | Decomposes answers into atomic claims, routes claims to source-specific evidence, retains stable tool/source IDs, checks support and stated attribution, and returns per-claim and answer-level block/allow decisions. On a harder multi-source benchmark, source-plus-relation accuracy is reported as much lower than binary blocking. | It makes the same conceptual move from pooled support to claim-level relation/source ownership. Its low exact-source performance shows why a false-corroboration endpoint is sensible. | It is a post-generation verifier over MCP traces, not a pre-generation origin-counting cue test. Its source labels are captured trace metadata, not a stipulated source-family graph. **Must-read current preprint; cite with status caveat.** |
| **Yedidel Louck, “Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees,” arXiv 2026.** [arXiv:2606.24322](https://arxiv.org/abs/2606.24322); arXiv-issued DOI [10.48550/arXiv.2606.24322](https://doi.org/10.48550/arXiv.2606.24322); no peer-reviewed DOI located by cutoff | Formalizes memory items with content, origin, scope, write time, and action class; studies laundering through summarization, trusted-tool echo, and manufactured corroboration; assumes an authenticated origin-labeling boundary and gates consequential action on independent trusted principals or fresh authorization. | This is a direct conceptual challenge to “origin accounting prevents manufactured corroboration.” It already uses origin-bound labels, non-malleable propagation, append-only verdict logs, and a distinction between repeated copies and independent trusted principals. | It is a security model with an origin oracle and action authorization, not a non-adversarial claim-support benchmark. Its independence is authenticated-channel independence, not the protocol’s fictional `independent-as-stipulated` relation. **Must-read; if retained, the paper must distinguish origin counting for informational support from origin-bound authorization for consequential action.** |
| **Haizhou Xia, “Diagnosing Evidence Utilization in Long-Context and Retrieval-Augmented Language Models under Matched Evidence Conditions,” arXiv 2026.** [arXiv:2606.06758](https://arxiv.org/abs/2606.06758); arXiv-issued DOI [10.48550/arXiv.2606.06758](https://doi.org/10.48550/arXiv.2606.06758); the abstract introduces a four-condition diagnostic protocol; no peer-reviewed DOI located by cutoff | Uses matched no-evidence, full-context, retrieved-evidence, and oracle-evidence conditions under fixed examples, prompts, score fields, retrieval controls, and validity checks. It explicitly says the protocol measures observable condition-level behavior, not internal causal attention. | This is the closest methodological precedent for the proposed “oracle-cue use” framing and for separating absence of evidence, availability of evidence, and use of evidence. | Its oracle condition supplies relevant passages, not source-origin relations, and its endpoint is evidence utilization rather than false corroboration. **Must cite as a design precedent and explain why F2 is a narrower oracle relation-metadata condition.** |
| **Ikhtiyor Nematov, Tarik Kalai, Elizaveta Kuzmenko, Gabriele Fugagnoli, Dimitris Sacharidis, Katja Hose & Tomer Sagi, “Source Attribution in Retrieval-Augmented Generation,” arXiv 2025.** [arXiv:2507.04480](https://arxiv.org/abs/2507.04480); arXiv-issued DOI [10.48550/arXiv.2507.04480](https://doi.org/10.48550/arXiv.2507.04480); preprint status at cutoff | Uses Shapley-style attribution to estimate the influence of retrieved documents and explicitly studies redundancy, complementarity, and synergy among sources. | It is the closest current source-influence/redundancy comparator and shows that source contributions need not be additive. | Influence attribution is not a supplied origin-family graph and does not isolate the F2/F1 relation-field contrast. **Must cite as a close preprint comparator; do not claim source attribution or redundancy analysis is new.** |
| **Sanchit Pandey, “Can Small Language Models Use What They Retrieve? An Empirical Study of Retrieval Utilization Across Model Scale,” arXiv 2026.** [arXiv:2603.11513](https://arxiv.org/abs/2603.11513); arXiv-issued DOI [10.48550/arXiv.2603.11513](https://doi.org/10.48550/arXiv.2603.11513); no peer-reviewed venue/DOI located by cutoff | Compares no retrieval, BM25, dense, and oracle retrieval with a parametric-known/unknown split. It reports that small models often fail even when an answer-bearing passage is supplied and that adding context can destroy answers previously known. | It is a direct negative control for the assumption that a correct metadata cue or answer-bearing context will be used. It demonstrates why a relation cue cannot be interpreted as a cognitive capability without matched cue-use testing. | It studies scale and answer extraction, not provenance or corroboration. **Cite as a current preprint and use its logic: report cue-use failure, retrieval harm, and model-specificity rather than only mean accuracy.** |
| **Mahdi Astaraki, Mohammad Arshi Saloot, Ali Shiraee Kasmaee, Hamidreza Mahyar & Soheila Samiee, “When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering,” arXiv 2026.** [arXiv:2601.19827](https://arxiv.org/abs/2601.19827); arXiv-issued DOI [10.48550/arXiv.2601.19827](https://doi.org/10.48550/arXiv.2601.19827); no peer-reviewed DOI located by cutoff | Compares no context, static gold context, and iterative RAG with stepwise retrieval, hypothesis refinement, and evidence-aware stopping. It reports iterative RAG beating the static gold-context condition in its chemistry multi-hop setup and explicitly cautions that gold context is not necessarily an operational upper bound. | It stresses that supplying all “ideal” evidence is not enough and that timing/order/route can matter. This bounds any claim that F2 tests a complete evidence policy. | It studies active acquisition and reasoning synchronization, not source dependence. **Cite as a negative/ceiling warning; do not call the proposed oracle cue an upper bound on a real system.** |
| **R.J. Sabouhi, “Context Is Not Control: Source-Boundary Failures in Controlled Text-Mediated Evidence Use,” working manuscript v0.6, May 2026.** [PDF](https://symbolicsuite.com/context-is-not-control.pdf); [replication repository](https://github.com/rjsabouhi/context-is-not-control); no DOI/peer-reviewed venue located by cutoff | Tests synthetic memory, policy, and documentation rows where text is present but current/admissible source status differs. It compares raw rendering, sanitization, and explicit source-boundary records, and explicitly interprets the latter as boundary-conditioned answering rather than intrinsic source-boundary inference. | This is the closest conceptual analog to supplying a typed relation field while holding text constant. It also anticipates the project’s own warnings about oracle cues, lexical leakage, synthetic truth, output format, and model/prompt sensitivity. | It concerns admissibility/currentness/role, not common origin or corroboration. It is a working manuscript, not peer-reviewed evidence. **Must-read for novelty and methods; cite only with the status and limitations visible.** |
| **Qinggang Zhang, Zhishang Xiang, Yilin Xiao, Le Wang, Junhui Li, Xinrun Wang & Jinsong Su, “FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation,” ACL 2025.** DOI [10.18653/v1/2025.acl-long.1062](https://doi.org/10.18653/v1/2025.acl-long.1062); [ACL record](https://aclanthology.org/2025.acl-long.1062/) | Models discrepancies between retrieved context and parametric knowledge at the fact level and adds a self-thinking process before generation. | It establishes fact-level conflict modeling and warns that forcing context adherence can suppress useful internal knowledge. | It does not type source origin or separate dependent copies from independent paths. **Must cite for the safety endpoint: a cue that lowers false corroboration but suppresses valid convergence is not a success.** |
| **Jingyi Sun, Greta Warren, Irina Shklovski & Isabelle Augenstein, “Explaining Sources of Uncertainty in Automated Fact-Checking,” ACL 2026.** DOI [10.18653/v1/2026.acl-long.2110](https://doi.org/10.18653/v1/2026.acl-long.2110); [ACL record](https://aclanthology.org/2026.acl-long.2110/) | CLUE identifies span-level claim–evidence and inter-evidence conflict/agreement relations and generates uncertainty explanations grounded in those interactions. | It is a current peer-reviewed precedent for explicit typed relations between evidence pieces and uncertainty, and for evaluating explanations against evidence conflicts rather than only final verdicts. | Relations are model-discovered span interactions and the output is an explanation, not a supplied provenance graph or origin count. **Must cite; do not claim typed agreement/conflict relations are new.** |
| **Jingxuan Wei, Xingyue Wang, Yanghaoyu Liao, Jie Dong, Yuchen Liu, Caijun Jia, Bihui Yu & Junnan Zhu, “GenProve: Learning to Generate Text with Fine-Grained Provenance,” ACL 2026.** DOI [10.18653/v1/2026.acl-long.228](https://doi.org/10.18653/v1/2026.acl-long.228); [ACL record](https://aclanthology.org/2026.acl-long.228/) | Defines generation-time fine-grained provenance with sentence-level provenance triples and distinguishes Quotation, Compression, and Inference in the ReFInE dataset. It reports a gap between surface quotation and inference provenance. | It directly establishes typed provenance relations and a benchmark that scores relation correctness separately from answer quality. | It types how generated claims use source sentences, not whether reports share an upstream origin. **Must cite; use it to distinguish relation typing from origin accounting.** |
| **Junnan Zhu, Min Xiao, Yining Wang, Feifei Zhai, Yu Zhou & Chengqing Zong, “TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification,” ACL 2025.** DOI [10.18653/v1/2025.acl-long.577](https://doi.org/10.18653/v1/2025.acl-long.577); [ACL record](https://aclanthology.org/2025.acl-long.577/) | Traces target sentences to source sentences and annotates relationships such as quotation, compression, and inference over multi-document/long-document settings. | It is a benchmark precedent for source tracing plus relationship classification, including the principle that source location alone is insufficient. | It does not label source families or common-origin dependence. **Must cite and add a relation-type control if the project later claims general typed provenance.** |
| **Rui Xing, Timothy Baldwin & Jey Han Lau, “Evaluating Evidence Attribution in Generated Fact Checking Explanations,” NAACL 2025.** DOI [10.18653/v1/2025.naacl-long.282](https://doi.org/10.18653/v1/2025.naacl-long.282); [ACL record](https://aclanthology.org/2025.naacl-long.282/) | Introduces citation masking and recovery for attribution quality, reports that strong LLMs still make attribution errors, and finds human-curated evidence important for better explanations. | It supports claim-level attribution and masking/recovery as evaluation primitives. | It concerns generated explanations and curated evidence, not source-family dependence. **Must cite for the output/evaluation distinction and for not treating citation presence as attribution correctness.** |
| **Nandan Thakur, Luiz Bonifacio, Crystina Zhang, Odunayo Ogundepo, Ehsan Kamalloo, David Alfonso-Hermelo, Xiaoguang Li, Qun Liu, Boxing Chen, Mehdi Rezagholizadeh & Jimmy Lin, “Knowing When You Don’t Know”: A Multilingual Relevance Assessment Dataset for Robust Retrieval-Augmented Generation, Findings EMNLP 2024.** DOI [10.18653/v1/2024.findings-emnlp.730](https://doi.org/10.18653/v1/2024.findings-emnlp.730); [ACL record](https://aclanthology.org/2024.findings-emnlp.730/) | NoMIRACL separates non-relevant and relevant retrieved-passage cases and measures hallucination and error rates. The record reports very high hallucination on non-relevant passages for some models and high error on relevant passages for others, showing a trade-off. | It is a direct negative control for unknown/insufficient evidence and for the assumption that an evidence packet is safely used once present. | It labels relevance, not origin dependence. **Must cite in the negative-literature section and include non-relevant/insufficient controls.** |
| **David Rau, Hervé Déjean, Nadezhda Chirkova, Thibault Formal, Shuai Wang, Stéphane Clinchant & Vassilina Nikoulina, “BERGEN: A Benchmarking Library for Retrieval-Augmented Generation,” Findings EMNLP 2024.** DOI [10.18653/v1/2024.findings-emnlp.449](https://doi.org/10.18653/v1/2024.findings-emnlp.449); [ACL record](https://aclanthology.org/2024.findings-emnlp.449/) | Reports a reproducible RAG benchmark and notes that closed-book can outperform oracle retrieval on ELI5 and WoW, making those datasets unsuitable for some RAG claims; it also finds stronger retrieval helps on NQ. | It is a peer-reviewed null/benchmark-suitability precedent: oracle evidence can fail to help, and dataset annotations can be partial or misaligned. | It does not test source origin. **Must cite; include a low-dependence negative control and do not treat oracle evidence as a universal ceiling or guarantee.** |
| **Alex Laitenberger, Christopher D. Manning & Nelson F. Liu, “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models,” EMNLP 2025.** DOI [10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656); [ACL record](https://aclanthology.org/2025.emnlp-main.1656/) | Under scaled token budgets, simple Document’s Original Structure RAG matches or beats more elaborate multi-stage pipelines on the tested long-context QA tasks. | It is the strongest current complexity-tax warning and a direct argument for F1/F2 matched resource accounting. | It is not origin-aware. **Must cite and include a simple source-faithful baseline before any claim that typed structure is worth its overhead.** |
| **Aochong Oliver Li & Tanya Goyal, “Memorization vs. Reasoning: Updating LLMs with New Knowledge,” Findings ACL 2025.** DOI [10.18653/v1/2025.findings-acl.1326](https://doi.org/10.18653/v1/2025.findings-acl.1326); [ACL record](https://aclanthology.org/2025.findings-acl.1326/) | KUP separates direct memorization from indirect reasoning over complex updates. The paper reports very low indirect-probing accuracy for continued-pretraining methods and uses oracle RAG as an upper-bound comparator. | It establishes that a model may have or receive the relevant information yet fail to use it in an indirect task. | It concerns temporal update conflicts, not source dependence. **Must cite as a reason to separate cue presence from cue use and to report failures, not only gains.** |
| **Anna Martin-Boyle, Cara A. C. Leckey, Martha C. Brown & Harmanpreet Kaur, “PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A,” CHI 2026.** DOI [10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101) | Decomposes documents and generated answers into claims/evidence, surfaces support and omissions, and studies a researcher-facing interface. The reported study found changes in trust without a corresponding behavioral correction benefit under cognitive burden. | It directly bounds any future packet/receipt/human-correction claim. | It is a human interface, not an origin graph. **Must cite if the thought piece retains progressive packets, human disposition, or correction.** |
| **Introne & Iandoli, “Improving Decision-making Performance through Argumentation: An Argument-based Decision Support System to Compute with Evidence,” Decision Support Systems 64 (2014).** DOI [10.1016/j.dss.2014.04.005](https://doi.org/10.1016/j.dss.2014.04.005) | Pendo represents questions, claims, pro/con evidence and theory, computes relative weights, creates reusable artifacts, and evaluates decision support with an outcome task. | It remains a direct integrated decision-support precedent against a broad “evidence-to-action” novelty claim. | It is not an LLM or origin-cue study. **Must cite for any eventual action-policy or decision-outcome paper; use as the non-LLM comparator.** |
| **Amaral, Rodrigues & Simperl, “ProVe: A Pipeline for Automated Provenance Verification of Knowledge Graphs Against Textual Sources,” Semantic Web (2024).** DOI [10.3233/SW-233467](https://doi.org/10.3233/SW-233467) | ProVe uses documented triple provenance, evidence extraction/selection, support/refute/neutral stance, and aggregation; it explicitly separates provenance support from truthfulness. | It is a direct precedent for claim–evidence–provenance verification and for refusing to equate source support with truth. | It does not decide whether multiple reports share an origin or whether to acquire more evidence. **Must cite and position the origin cue as an additional relation-policy test, not a new provenance concept.** |

## What the current literature says about the oracle-cue framing

### “Oracle” must be scoped to the supplied relation, not the world

The protocol currently calls F2 a typed-cue condition. That is directionally correct but not precise enough for a skeptical reviewer. There are at least four different oracle constructs:

1. **Oracle retrieval:** the retrieved passage is guaranteed to contain the answer or gold evidence.
2. **Oracle context:** all annotated evidence is supplied at once.
3. **Oracle provenance:** the system is handed source/artifact/derivation relations that a deployed system would have to discover or verify.
4. **Oracle semantics:** the benchmark stipulates that a relation such as `independent-as-stipulated` has the intended meaning within the synthetic graph.

The proposed F2 is primarily (3) and (4). It is not oracle retrieval, because F0–F2 can contain the same reports. It is not real-world independence, because the generator cannot establish causal or epistemic independence. It is not an oracle truth label, because claim polarity and graph membership are only true by construction.

**Recommended methods sentence:**

> “F2 is an oracle **origin-relation metadata condition**: the model receives the benchmark’s stipulated relation field. We measure whether it uses that field under a fixed counting rule; we do not measure relation discovery, real-world source independence, or truth.”

Use **oracle relation cue** or **stipulated origin-relation cue** in the methods. Use **cue-use diagnostic** or **representation-use test** in the abstract. Do not call the result “provenance reasoning,” “independent corroboration,” or “epistemic discrimination.”

### F2 versus F1 is the only causal contrast that identifies the proposed value

The current protocol’s F0/F1/F2 structure is sound in principle:

| Condition | Evidence and output | Instruction | Identified comparison |
|---|---|---|---|
| **F0: citation-only** | Opaque source/artifact IDs and dates; no origin rule or relation | Ordinary bounded evidence assessment | Baseline performance with evidence but no origin control |
| **F1: rule-only** | Same evidence, same IDs, same output contract | “Count distinct origin pathways; do not treat repeated reports as independent; preserve unknown.” | Effect of an explicit cognitive/policy rule |
| **F2: typed cue** | Same evidence and rule, plus fixed-width relation field containing `dependent`, `independent-as-stipulated`, or `unknown` | Same as F1 | **Value of the supplied typed relation beyond the rule** |

**[I]** F2–F1 is not a test of whether provenance metadata is useful in general. It is a test of whether this particular model, prompt, relation vocabulary, and packet format use the supplied relation to alter origin counting. F1–F0 tests whether the rule matters at all. If F1 and F2 tie while both beat F0, the result belongs to instruction/policy design, not relation metadata. If F2 beats F1 only when labels are perfectly clean, the result is an oracle upper bound.

### Required oracle-cue controls

The current protocol should add or make explicit the following controls before data generation:

1. **Fixed-width metadata:** relation slots, IDs, dates, report counts, and evidence text occupy comparable token budgets in F1 and F2.
2. **Opaque randomized IDs:** never use semantic origin names, sequential cluster IDs, or count-revealing field order.
3. **Relation vocabulary stress:** use at least two semantically equivalent prompt renderings and one codebook/label-permutation stress condition. The primary condition may retain human-readable labels, but the stress set should detect whether formatting rather than semantics drives the effect.
4. **Overlap crossing:** include low-overlap dependent paraphrases and high-overlap independent-as-stipulated reports; otherwise a surface classifier can solve the task without the cue.
5. **Position crossing:** randomize relation-field position and report order; avoid “the last row is the answer” shortcuts.
6. **Unknown preservation:** test agreement with withheld relation and ensure the correct response is `unknown`/insufficient, not random independence.
7. **Relation noise:** include declared 5%, 10%, and possibly 20% relation flips as secondary stress conditions. If F2 fails sharply under small noise, call it an oracle upper bound rather than a deployable policy.
8. **Negative evidence:** conflict bundles must include dependent copies on one side and independent support/refutation on the other; otherwise false corroboration is underdefined.
9. **Model/seed lock:** one frozen local model and predeclared seeds for the primary analysis; seeds are nested repetitions, not additional independent bundles.
10. **No hidden retrieval:** no live web, external tools, model self-search, or prompt repair in the primary experiment.

## Closest integrated precedents and the residual contribution

### Three increasingly narrow interpretations of the project

| Interpretation | Current literature status | Surviving disposition |
|---|---|---|
| **A. A universal “discrimination layer” before generation** | [S] Integrated agentic RAG, source-aware RAG, claim/evidence systems, provenance verification, argument-based decision support, and human interfaces already cover most responsibilities. | **Retire as a paper contribution.** Keep only as historical thought-piece language if a separate comprehension study justifies it. |
| **B. A compact typed context/action contract combining provenance, dependence, unknowns, cost, and routing** | [I] A composition may be operationally useful, but no current source establishes that this exact conjunction is the minimum or improves outcomes. Search-control and source-aware systems already cover neighboring policy surfaces. | **Defer.** Require a stable narrow effect, feature ablations, strong baselines, and a second study. Call it “candidate profiled policy,” not minimal. |
| **C. A supplied typed origin-relation cue changes false-corroboration behavior beyond an explicit rule** | [S] No located peer-reviewed work isolates this exact F2–F1 contrast and endpoint; [S] multiple current works make the oracle design and typed relation pattern familiar. | **Viable as a bounded benchmark/measurement paper**, subject to strict truth boundary, leakage controls, and null/retire criteria. |

### What is actually distinctive if the study succeeds

**[H]** The strongest novelty statement would be:

> “We introduce a provenance-controlled synthetic benchmark and a matched F0/F1/F2 protocol that measures whether a frozen language model uses stipulated origin-relation metadata to avoid false corroboration, while separately measuring loss of valid independent-as-stipulated support and robustness to relation noise.”

This is distinct in **estimand and benchmark design**, not because `dependent`, `independent`, `unknown`, provenance, or corroboration are new terms. It is also conditional on the benchmark being released with:

- machine-readable source/artifact/transformation/time manifests;
- proposition and origin-family splits;
- immutable prompts, model hashes, seeds, and parser versions;
- human semantic audit of claim polarity and transformations;
- a leakage report and surface-only classifier;
- a predeclared primary endpoint and confidence interval;
- invalid-output and metadata-overhead accounting;
- negative outputs and failure bundles, not only winning examples.

### What remains explicitly out of scope

The first paper must not claim:

- that a model can infer real source independence;
- that multiple stipulated origins are epistemically independent in the world;
- that origin count establishes truth or consensus;
- that provenance metadata improves retrieval quality;
- that F2 routes acquisition, stopping, clarification, escalation, or human review;
- that a correct origin count improves a human decision;
- that an oracle cue generalizes to deployed RAG, agent memory, or open-web research;
- that a positive result validates the full C0–C11 architecture;
- that the historical “discrimination layer” is a new mechanism.

## Missing negative and null-result literature to add to the project package

The current package already cites DOS RAG, PaperTrail, and several failure/attack papers. The following additional results should be explicitly integrated because they prevent a positive cue-use result from being inflated into a universal evidence-layer result.

| Null, negative, or boundary result [S] | Why it matters for this project [I] | Concrete protocol response |
|---|---|---|
| **BERGEN:** closed-book outperformed oracle retrieval on ELI5 and WoW in the reported diagnostic analysis, while NQ showed a more conventional oracle benefit. | Oracle context is not guaranteed to help; benchmark/task answerability and annotation quality can reverse the sign. | Add low-dependence and answerable-from-memory controls. Do not describe F2 as an upper bound or assume any cue should help everywhere. |
| **NoMIRACL:** models can hallucinate on non-relevant passages and miss relevant passages; the direction differs by model family. | Evidence availability and evidence use are separable, and abstention can trade against valid recall. | Use false-corroboration as the primary endpoint and valid-origin recall as a safety endpoint. Report both directions by model/structure. |
| **DOS RAG:** simple retrieve-then-read can match or beat elaborate multi-stage RAG under scaled token budgets. | Added structure can be a complexity tax; a graph or receipt can look principled while adding no outcome value. | Match tokens, metadata width, latency, and parser cost; include a simple source-faithful baseline. |
| **KUP / Memorization vs. Reasoning:** even when updated material is available, models can perform very poorly on indirect reasoning; oracle RAG is only a comparator. | A model can read relation text and still fail the intended operation. | Include cue-use failures, invalid outputs, and relation-noise stress; do not infer internal reasoning from output compliance. |
| **PaperTrail:** claim/evidence provenance altered trust more readily than behavior under cognitive burden. | Transparency, confidence, and perceived grounding are not correction or decision quality. | Defer human claims; if a later human study occurs, measure correction, inspection, omission detection, reliance, and burden. |
| **Pandey 2026 preprint:** sub-7B models often fail with oracle retrieval and can be harmed by added context. | A cue may be ignored or distract; effects may be model-scale-specific. | Report model identity and scale as part of the estimand; no cross-model generalization from one frozen model. |
| **Astaraki et al. 2026 preprint:** iterative retrieval can outperform static gold context, and static oracle evidence is not necessarily an operational ceiling. | All-at-once evidence and metadata do not test active acquisition or route quality. | Keep routing out of the origin paper and state that F2 is not an upper bound on a full system. |
| **CONFACT:** manually curated credibility labels can outperform automated credibility estimates in conflict resolution; credibility metadata can add noise. | A typed cue can encode incorrect or institutionally biased authority. | Keep authority out of the primary origin estimand; add cue-noise and metadata-swap stress only as secondary work. |
| **FaithfulRAG:** forcing context adherence can suppress useful parametric information. | A false-corroboration reduction could be purchased by rejecting valid convergence or relevant evidence. | Retain the non-inferiority valid-origin recall margin and report per-structure loss. |
| **Source-boundary working manuscript:** explicit boundary records change behavior in synthetic tasks, but the authors explicitly label the result boundary-conditioned and flag lexical, prompt, and format confounds. | The exact pattern “metadata changes behavior” is already being independently explored and its confounds are known. | Add neutral-label/position/paraphrase tests and phrase the effect as cue-conditioned use. |
| **Li et al., “LLMs Trust Humans More, That’s a Problem!” (ACL 2025):** user-provided text can be favored over conflicting database evidence; the paper measures authority bias across six LLMs and proposes ABDD/CDEQ. DOI [10.18653/v1/2025.acl-long.1400](https://doi.org/10.18653/v1/2025.acl-long.1400); [ACL record](https://aclanthology.org/2025.acl-long.1400/). | Source-role or authority metadata can change behavior even when content support is held constant; an origin cue must not be interpreted as a neutral truth signal. | Keep “authority” out of the primary origin estimand; add metadata-swap/role-neutral controls if source labels are shown. |
| **Abolghasemi et al., “Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models” (Findings ACL 2025):** counterfactual authorship metadata changed attribution quality by 3–18% and exposed human-authorship bias. DOI [10.18653/v1/2025.findings-acl.1087](https://doi.org/10.18653/v1/2025.findings-acl.1087); [ACL record](https://aclanthology.org/2025.findings-acl.1087/). | Metadata can alter attribution without changing evidence; F2 gains may be label/role salience rather than origin accounting. | Randomize opaque IDs and relation labels, cross metadata position, and report whether the cue changes the claim-state endpoint rather than only a stated count. |

### Negative literature that is still missing from the project’s argument

**[I]** The package needs a dedicated subsection on **cue value being zero or negative**. Existing prose says the policy may lose, but the current argument still reads as if typed origin metadata is the likely positive intervention. Add the following prior null possibilities to the prospectus and protocol:

- F2 = F1: the explicit rule is sufficient; relation metadata adds no value.
- F2 < F1 on valid-origin recall: the cue induces over-discounting or conservative abstention.
- F2 wins only in formatting-easy conditions: the effect is leakage.
- F2 wins only with perfect relations: the result is an oracle upper bound.
- F2 changes stated counts but not claim state: the cue is used cosmetically, not decision-relevantly.
- F2 reduces false corroboration but increases omission of independent support: the policy is not safe as a blanket rule.
- F2’s token/latency/metadata cost exceeds its false-corroboration benefit on low-dependence controls: the policy has a negative break-even region.

There is no located peer-reviewed null result on exactly the project’s typed origin cue. That is a gap worth testing, not evidence that a positive result is likely.

## Terminology stress test

### “Discrimination layer” should not lead the scientific paper

**[I]** A bounded exact-phrase search did not reveal a stable cross-disciplinary use matching the project’s intended meaning. It did reveal multiple established senses: social/legal discrimination, ML discriminator/classifier layers, GAN “minibatch discrimination,” and network/traffic discrimination. This is a terminology collision finding, not proof that no one understands the phrase.

The disclaimer in the thought piece (“technical differentiation, not social classification”) does not remove the title-level problem. A reviewer who sees “discrimination layer” may reasonably expect fairness, classification, or representation-learning work and may treat the redefinition as rhetorical branding.

**Disposition:**

- Use a functional scientific title: **Origin-Relation Cue Use**, **Provenance-Aware Origin Accounting**, or **Evidence Selection and Action Policy**.
- Keep “Pattern Recognition / The Discrimination Layer” only as historical site/thought-piece lineage until a separate human comprehension/terminology study passes.
- Do not use “discrimination” as a construct label in the origin benchmark.

### Recommended terminology replacements

| Risky term | Why it is risky | Recommended term in the first paper |
|---|---|---|
| **discrimination layer** | Social/legal harm, classifier/GAN, network filtering, and separability meanings collide. | **origin-relation cue**, **evidence-selection policy**, or **provenance-aware action policy** |
| **independence** | Implies statistical or causal independence that synthetic text cannot establish. | **independent-as-stipulated origin paths** |
| **consensus / corroboration** | Suggests real-world epistemic convergence; a copied bundle can look like consensus. | **origin-path count**; **false-corroboration event** for the operational error |
| **provenance reasoning** | F2 supplies provenance; the model is not asked to discover it. | **provenance-cue use** or **origin-relation cue use** |
| **oracle cue** | “Oracle” can be misunderstood as truth or retrieval gold. | **stipulated origin-relation metadata condition** in the methods; shorthand **oracle relation cue** after definition |
| **supported claim** | May mean textual entailment, evidentiary weight, or truth. | `claim_state = supported/refuted/insufficient/contested` with explicit relation and scope |
| **evidence-grounded** | Used for retrieved, cited, entailed, source-linked, and true. | **claim-supported under the benchmark manifest** or **source-attributed** |
| **authority** | Can mean legal jurisdiction, expertise, reputation, authorship, or permission. | Keep out of origin paper; later use **scoped source authority** with bearer, proposition, time, and jurisdiction |
| **route receipt** | Nonstandard and can imply enforcement/accountability without it. | **selection-and-action audit record** or **routing audit record** |
| **unknown origin** | Could be read as “probably independent.” | **unresolved origin relation; not counted as independent** |
| **minimal policy** | Feature minimality has not been demonstrated; C0–C11 is broad. | **candidate compact policy** or **profiled policy** |
| **human correction** | A cue or interface can change trust without correction. | **seeded-error correction under measured burden**, only in a separate study |

### The project should distinguish four relation vocabularies

The current package risks collapsing relations that belong to different levels:

1. **Derivation relation:** copied, paraphrased, summarized, translated, quoted, inferred.
2. **Origin-family relation:** same upstream origin, distinct origin, unknown origin.
3. **Claim stance relation:** supports, refutes, qualifies, neutral, insufficient.
4. **Action relation:** admissible, provisional, hold, escalate, authorized, unauthorized.

**[I]** GenProve and TROVE already show why derivation relation is not the same as source-family relation. ProVe and ProvenanceGuard show why claim support is not the same as source ownership. Louck’s memory-security model shows why origin/authority is not the same as content support. The first study should contain only the second relation family plus claim stance as an output; it should not imply that one `relation` field solves all four levels.

## Must-cite sources for an eventual paper

The following list is the minimum current set, grouped by why a reviewer would expect it. Full author/title/venue/DOI/URL details are supplied so the eventual bibliography can be checked rather than inferred from shorthand.

### Direct origin, source relation, and conflict precedents

1. **Tan, Xingyu; Wang, Xiaoyang; Liu, Qing; Xu, Xiwei; Yuan, Xin; Zhu, Liming; Zhang, Wenjie.** “HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning.” *Proceedings of EMNLP 2025*, pp. 14431–14459. DOI: [10.18653/v1/2025.emnlp-main.730](https://doi.org/10.18653/v1/2025.emnlp-main.730). Official record: [ACL Anthology](https://aclanthology.org/2025.emnlp-main.730/).

2. **Ge, Ziyu; Wu, Yuhao; Chin, Daniel Wai Kit; Lee, Roy Ka-Wei; Cao, Rui.** “Resolving Conflicting Evidence in Automated Fact-Checking: A Study on Retrieval-Augmented LLMs.” *Proceedings of IJCAI 2025*, pp. 9656–9664. DOI: [10.24963/IJCAI.2025/1073](https://doi.org/10.24963/IJCAI.2025/1073). Official record: [IJCAI proceedings](https://www.ijcai.org/proceedings/2025/1073).

3. **Alvarez, Ander; Rajan, Santhiya; Mugel, Samuel; Orús, Román.** “ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents.” *arXiv preprint*, 2026. URL: [arXiv:2606.18037](https://arxiv.org/abs/2606.18037); arXiv-issued DOI: [10.48550/arXiv.2606.18037](https://doi.org/10.48550/arXiv.2606.18037). No peer-reviewed DOI was located by the cutoff; label as preprint.

4. **Louck, Yedidel.** “Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees.” *arXiv preprint*, 2026. URL: [arXiv:2606.24322](https://arxiv.org/abs/2606.24322); arXiv-issued DOI: [10.48550/arXiv.2606.24322](https://doi.org/10.48550/arXiv.2606.24322). No peer-reviewed DOI was located by the cutoff; label as preprint. This is essential if the paper uses “manufactured corroboration,” “origin-bound,” or action-gating language.

5. **Zhang, Qinggang; Xiang, Zhishang; Xiao, Yilin; Wang, Le; Li, Junhui; Wang, Xinrun; Su, Jinsong.** “FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation.” *Proceedings of ACL 2025*, pp. 21863–21882. DOI: [10.18653/v1/2025.acl-long.1062](https://doi.org/10.18653/v1/2025.acl-long.1062). Official record: [ACL Anthology](https://aclanthology.org/2025.acl-long.1062/).

6. **Sun, Jingyi; Warren, Greta; Shklovski, Irina; Augenstein, Isabelle.** “Explaining Sources of Uncertainty in Automated Fact-Checking.” *Proceedings of ACL 2026*, pp. 45510–45534. DOI: [10.18653/v1/2026.acl-long.2110](https://doi.org/10.18653/v1/2026.acl-long.2110). Official record: [ACL Anthology](https://aclanthology.org/2026.acl-long.2110/).

### Oracle-context, evidence-use, and negative-result precedents

7. **Xia, Haizhou.** “Diagnosing Evidence Utilization in Long-Context and Retrieval-Augmented Language Models under Matched Evidence Conditions.” *arXiv preprint*, 2026. URL: [arXiv:2606.06758](https://arxiv.org/abs/2606.06758); arXiv-issued DOI: [10.48550/arXiv.2606.06758](https://doi.org/10.48550/arXiv.2606.06758). The abstract introduces a four-condition diagnostic protocol; no peer-reviewed DOI was located by the cutoff. Treat as a preprint, but it is methodologically close enough that omitting it would make the oracle framing look uninformed.

8. **Pandey, Sanchit.** “Can Small Language Models Use What They Retrieve? An Empirical Study of Retrieval Utilization Across Model Scale.” *arXiv preprint*, 2026. URL: [arXiv:2603.11513](https://arxiv.org/abs/2603.11513); arXiv-issued DOI: [10.48550/arXiv.2603.11513](https://doi.org/10.48550/arXiv.2603.11513). No peer-reviewed DOI was located by the cutoff. Use as current negative/scale evidence, not as a settled universal result.

9. **Astaraki, Mahdi; Saloot, Mohammad Arshi; Kasmaee, Ali Shiraee; Mahyar, Hamidreza; Samiee, Soheila.** “When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering.” *arXiv preprint*, 2026. URL: [arXiv:2601.19827](https://arxiv.org/abs/2601.19827); arXiv-issued DOI: [10.48550/arXiv.2601.19827](https://doi.org/10.48550/arXiv.2601.19827). No peer-reviewed DOI was located by the cutoff. Cite with preprint status.

- **Additional close working artifact:** **Sabouhi, R.J.** “Context Is Not Control: Source-Boundary Failures in Controlled Text-Mediated Evidence Use.” Working manuscript v0.6, May 2026. [PDF](https://symbolicsuite.com/context-is-not-control.pdf); [replication repository](https://github.com/rjsabouhi/context-is-not-control). No DOI or peer-reviewed venue was located by the cutoff. It is not evidence of a settled result, but its explicit boundary-conditioned cue-use framing and confound audits make it essential to disclose in the novelty/methods discussion.

10. **Thakur, Nandan; Bonifacio, Luiz; Zhang, Crystina; Ogundepo, Odunayo; Kamalloo, Ehsan; Alfonso-Hermelo, David; Li, Xiaoguang; Liu, Qun; Chen, Boxing; Rezagholizadeh, Mehdi; Lin, Jimmy.** “Knowing When You Don’t Know”: A Multilingual Relevance Assessment Dataset for Robust Retrieval-Augmented Generation.” *Findings of EMNLP 2024*, pp. 12508–12526. DOI: [10.18653/v1/2024.findings-emnlp.730](https://doi.org/10.18653/v1/2024.findings-emnlp.730). Official record: [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.730/).

11. **Rau, David; Déjean, Hervé; Chirkova, Nadezhda; Formal, Thibault; Wang, Shuai; Clinchant, Stéphane; Nikoulina, Vassilina.** “BERGEN: A Benchmarking Library for Retrieval-Augmented Generation.” *Findings of EMNLP 2024*, pp. 7640–7663. DOI: [10.18653/v1/2024.findings-emnlp.449](https://doi.org/10.18653/v1/2024.findings-emnlp.449). Official record: [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.449/).

12. **Laitenberger, Alex; Manning, Christopher D.; Liu, Nelson F.** “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models.” *Proceedings of EMNLP 2025*, pp. 32559–32569. DOI: [10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656). Official record: [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1656/).

13. **Li, Aochong Oliver; Goyal, Tanya.** “Memorization vs. Reasoning: Updating LLMs with New Knowledge.” *Findings of ACL 2025*, pp. 25853–25874. DOI: [10.18653/v1/2025.findings-acl.1326](https://doi.org/10.18653/v1/2025.findings-acl.1326). Official record: [ACL Anthology](https://aclanthology.org/2025.findings-acl.1326/).

14. **Martin-Boyle, Anna; Leckey, Cara A. C.; Brown, Martha C.; Kaur, Harmanpreet.** “PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A.” *CHI 2026*. DOI: [10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101). Official DOI record: [ACM DOI](https://doi.org/10.1145/3772318.3791101).

### Fine-grained provenance and attribution

15. **Wei, Jingxuan; Wang, Xingyue; Liao, Yanghaoyu; Dong, Jie; Liu, Yuchen; Jia, Caijun; Yu, Bihui; Zhu, Junnan.** “GenProve: Learning to Generate Text with Fine-Grained Provenance.” *Proceedings of ACL 2026*, pp. 5027–5048. DOI: [10.18653/v1/2026.acl-long.228](https://doi.org/10.18653/v1/2026.acl-long.228). Official record: [ACL Anthology](https://aclanthology.org/2026.acl-long.228/).

16. **Zhu, Junnan; Xiao, Min; Wang, Yining; Zhai, Feifei; Zhou, Yu; Zong, Chengqing.** “TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification.” *Proceedings of ACL 2025*, pp. 11755–11771. DOI: [10.18653/v1/2025.acl-long.577](https://doi.org/10.18653/v1/2025.acl-long.577). Official record: [ACL Anthology](https://aclanthology.org/2025.acl-long.577/).

17. **Xing, Rui; Baldwin, Timothy; Lau, Jey Han.** “Evaluating Evidence Attribution in Generated Fact Checking Explanations.” *Proceedings of NAACL 2025*, pp. 5475–5496. DOI: [10.18653/v1/2025.naacl-long.282](https://doi.org/10.18653/v1/2025.naacl-long.282). Official record: [ACL Anthology](https://aclanthology.org/2025.naacl-long.282/).

18. **Schreieder, Tobias; Schopf, Tim; Färber, Michael.** “Attribution, Citation, and Quotation: A Survey of Evidence-based Text Generation with Large Language Models.” *Proceedings of ACL 2026*, pp. 30956–31000. DOI: [10.18653/v1/2026.acl-long.1430](https://doi.org/10.18653/v1/2026.acl-long.1430). Official record: [ACL Anthology](https://aclanthology.org/2026.acl-long.1430/). This is a survey rather than primary experimental evidence, but it is authoritative current terminology/field-map evidence and reports fragmentation across 134 papers and 300 metrics.

- **Li, Yuxuan; Guo, Xinwei; Gao, Jiashi; Chen, Guanhua; Zhao, Xiangyu; Zhang, Jiaxin; Liu, Quanying; Wu, Haiyan; Yao, Xin; Wei, Xuetao.** “LLMs Trust Humans More, That’s a Problem! Unveiling and Mitigating the Authority Bias in Retrieval-Augmented Generation.” *Proceedings of ACL 2025*, pp. 28844–28858. DOI: [10.18653/v1/2025.acl-long.1400](https://doi.org/10.18653/v1/2025.acl-long.1400). Official record: [ACL Anthology](https://aclanthology.org/2025.acl-long.1400/). Primary authority-bias experiment; cite when discussing source-role metadata, authority, or human correction.

- **Abolghasemi, Amin; Azzopardi, Leif; Hashemi, Seyyed Hadi; de Rijke, Maarten; Verberne, Suzan.** “Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models.” *Findings of ACL 2025*, pp. 21105–21124. DOI: [10.18653/v1/2025.findings-acl.1087](https://doi.org/10.18653/v1/2025.findings-acl.1087). Official record: [ACL Anthology](https://aclanthology.org/2025.findings-acl.1087/). Primary counterfactual metadata/attribution experiment; cite as a cue-leakage and trust/attribution boundary.

### Established integrated baselines retained from Loop 1

19. **Introne, Joshua E.; Iandoli, Luca.** “Improving Decision-making Performance through Argumentation: An Argument-based Decision Support System to Compute with Evidence.” *Decision Support Systems* 64 (2014). DOI: [10.1016/j.dss.2014.04.005](https://doi.org/10.1016/j.dss.2014.04.005).

20. **Amaral, Gabriel; Rodrigues, Odinaldo; Simperl, Elena.** “ProVe: A Pipeline for Automated Provenance Verification of Knowledge Graphs Against Textual Sources.” *Semantic Web* (2024). DOI: [10.3233/SW-233467](https://doi.org/10.3233/SW-233467).

21. **Wu, Junde; Zhu, Jiayuan; Liu, Yuyuan; Xu, Min; Jin, Yueming.** “Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools.” *Proceedings of ACL 2025*. DOI: [10.18653/v1/2025.acl-long.1383](https://doi.org/10.18653/v1/2025.acl-long.1383).

22. **Li, Xiaoxi; Dong, Guanting; Jin, Jiajie; Zhang, Yuyao; Zhou, Yujia; Zhu, Yutao; Zhang, Peitian; Dou, Zhicheng.** “Search-o1: Agentic Search-Enhanced Large Reasoning Models.” *Proceedings of EMNLP 2025*. DOI: [10.18653/v1/2025.emnlp-main.276](https://doi.org/10.18653/v1/2025.emnlp-main.276).

23. **Zheng, Yuxiang; Fu, Dayuan; Hu, Xiangkun; Cai, Xiaojie; Ye, Lyumanshan; Lu, Pengrui; Liu, Pengfei.** “DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments.” *Proceedings of EMNLP 2025*. DOI: [10.18653/v1/2025.emnlp-main.22](https://doi.org/10.18653/v1/2025.emnlp-main.22).

24. **Wu, Peilin; Zhang, Mian; Zhang, Xinlu; Du, Xinya; Chen, Zhiyu.** “Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty.” *Proceedings of EMNLP 2025*. DOI: [10.18653/v1/2025.emnlp-main.998](https://doi.org/10.18653/v1/2025.emnlp-main.998).

25. **Hwang, Jeongyeon; Park, Junyoung; Park, Hyejin; Kim, Dongwoo; Park, Sangdon; Ok, Jungseul.** “Retrieval-Augmented Generation with Estimation of Source Reliability.” *Proceedings of EMNLP 2025*. DOI: [10.18653/v1/2025.emnlp-main.1738](https://doi.org/10.18653/v1/2025.emnlp-main.1738).

26. **Xu, Wujiang; Liang, Zujie; Mei, Kai; Gao, Hang; Tan, Juntao; Zhang, Yongfeng.** “A-Mem: Agentic Memory for LLM Agents.” *NeurIPS 2025*. DOI: [10.52202/085713-0593](https://doi.org/10.52202/085713-0593).

## Claim-level language changes for the manuscript and site

The following table is intended to be used as an editing checklist in the next core revision. It does not authorize edits to the core files in this lane.

| Avoid or qualify | Replace with | Why |
|---|---|---|
| “We introduce a discrimination layer that makes judgment visible before generation.” | “We test a stipulated origin-relation cue for origin counting before generation.” | The first sentence claims a broad architecture; the second names the identified intervention. |
| “The system recognizes independent corroboration.” | “The frozen model is given benchmark-stipulated origin relations and is evaluated on whether it counts origin pathways as instructed.” | F2 supplies the relation; the model does not discover or verify it. |
| “Independent sources provide consensus.” | “Multiple independent-as-stipulated origin paths are present in the synthetic manifest.” | Synthetic graphs cannot establish real-world epistemic independence or consensus. |
| “Typed provenance improves evidence-grounded decisions.” | “In the tested synthetic bundles, F2 reduces the prespecified false-corroboration event relative to F1, if the effect and recall margin pass.” | The current design has no human decision, routing, or field outcome. |
| “The oracle cue tests provenance reasoning.” | “The oracle relation-metadata condition tests provenance-cue use.” | “Reasoning” would imply inference of a hidden relation. |
| “Evidence presence is enough for grounding.” | “Evidence availability and evidence utilization are separate conditions.” | BERGEN, NoMIRACL, KUP, and current oracle-utilization studies show the distinction. |
| “Unknown provenance is treated conservatively.” | “Unknown origin relation is preserved and is not counted as an independent supporting path.” | “Conservative” is vague and may hide an asymmetric cost choice. |
| “Support means the claim is true.” | “Support is a benchmark-scoped claim–evidence relation; truth is outside the synthetic study’s truth boundary.” | ProVe and provenance literature explicitly separate support from truth. |
| “Our policy is minimal.” | “Our candidate compact/profiled policy will be evaluated for feature necessity.” | Minimality requires ablations and a defined feature cost. |
| “A route receipt guarantees accountability.” | “A selection-and-action audit record supports replay and inspection if its fields and authorization boundaries are enforced.” | A log can record an unauthorized or wrong decision after the fact. |
| “The result generalizes to RAG/agents.” | “A public transfer challenge will be descriptive; failure to transfer precludes a real-world origin-accounting claim.” | Oracle synthetic success is an upper-bound-like cue-use result only. |
| “Trust and transparency improve safety.” | “Trust, inspection, correction, reliance, and safety are separate endpoints.” | PaperTrail and attribution/authority-bias work make this distinction empirically necessary. |
| “The layer handles action consequence.” | “Action consequence is out of scope in the origin paper; it is a later policy study variable.” | The first protocol does not measure acquisition cost, authorization, or action outcomes. |
| “The field has no integrated framework for this responsibility.” | “The searched literature contains multiple integrated systems covering adjacent or overlapping responsibilities; this study isolates a narrower cue-use contrast.” | This is the defensible state of knowledge after the 2026 expansion. |

### Suggested abstract language

> “We evaluate whether a language model uses explicit, benchmark-stipulated origin relations when counting supporting evidence. In a matched synthetic benchmark, the model receives the same reports and origin-counting rule in all conditions; the focal intervention adds a typed relation field distinguishing dependent, independent-as-stipulated, and unknown origin. The primary endpoint is false corroboration, with valid-origin recall as a safety endpoint. The study does not infer provenance, establish real-world independence, or evaluate retrieval, human decisions, routing, or deployment.”

### Suggested limitations language

> “A positive F2–F1 contrast would support only a cue-conditioned origin-accounting effect for the tested model, prompt, label vocabulary, and stipulated graph generator. It would not establish that the model can discover provenance, that the reports are epistemically independent outside the benchmark, that the counted evidence is true, or that a broader evidence-selection policy improves decisions. If the effect disappears under relation noise, paraphrase/position controls, a strong rule-only baseline, or a second model, we will treat it as an oracle upper bound or model-specific artifact.”

## Explicit stop, narrow, and retire criteria

The project should preregister these criteria before generating the definitive benchmark. They are designed to make a null result publishable and to prevent scope expansion after a positive but fragile result.

### Stop before the main run

Stop data collection and repair the protocol if any of the following occurs:

1. A surface-only classifier predicts origin structure above the preregistered leakage threshold from report text, IDs, order, length, or metadata alone.
2. A semantic audit cannot establish claim polarity, transformation type, source/artifact membership, and intended relation for at least the required manifest-integrity threshold.
3. F1 and F2 differ in token budget, metadata width, output contract, model call count, or parser behavior in a way that cannot be matched or modeled.
4. The primary model can access live retrieval, hidden tool calls, previous benchmark outputs, or non-frozen prompt repairs.
5. Relation labels reveal cluster count or origin structure by naming, numbering, field position, or systematic formatting.
6. The benchmark’s “independent” condition depends on real-world claims, people, allegations, private data, or unverifiable external source history.
7. The planned primary endpoint, safety margin, or invalid-output rules are changed after inspecting efficacy results.

### Retire the typed-cue efficacy claim

Retire the positive typed-cue claim, and report a null or negative result, if:

1. **F2 does not beat F1:** the preregistered confidence interval does not support the minimum false-corroboration reduction.
2. **F2 loses valid-origin recall:** F2 is more than the preregistered non-inferiority margin below F1 on multiple-origin convergence bundles.
3. **F1 = F2 but both beat F0:** the improvement is attributable to the explicit rule, not relation metadata. Retire “typed provenance cue” novelty and report an instruction effect.
4. **Effect is formatting-only:** F2 wins only in the primary label/position format and disappears under position, paraphrase, codebook, or token-matched stress tests.
5. **Effect is oracle-only:** F2 wins with perfect relations but collapses under declared relation noise. Report an oracle upper bound; do not recommend a deployed cue or policy.
6. **Effect is not decision-relevant:** the model changes `origin_count_supporting` but not claim state, false-corroboration event, valid-origin recall, or another preregistered endpoint.
7. **Effect is model/seed-specific:** the result reverses across the predeclared model/seed/structure checks. Narrow to a model-specific finding or stop.
8. **Effect is not robust to low-dependence negatives:** the cue adds errors or material cost where origin dependence is absent, and no declared break-even region exists.
9. **Effect is dominated by a strong baseline:** a simple rule-only, source-faithful, or reliability-aware baseline matches or exceeds F2 at lower matched cost.
10. **Synthetic/public transfer fails:** a descriptive public transfer challenge cannot preserve documented provenance semantics. Make no real-world origin-accounting claim.

### Retire the “discrimination layer” label

Retire the label from scientific titles, abstracts, keywords, and search metadata regardless of benchmark outcome if:

- a terminology comprehension pilot shows readers infer fairness/classification/network meanings;
- the origin study is positive but cannot demonstrate a broader policy effect;
- the literature search finds a direct framework using the same responsibility under a clearer established name;
- the label increases reviewer misclassification or decreases willingness to inspect the evidence protocol.

The thought piece can preserve the phrase as historical lineage, but the research paper should use a functional title even if the benchmark succeeds.

### Stop expansion into the full policy

Do not proceed from a positive F2–F1 result directly to human correction, routing, memory, or field deployment. A next study must be selected only after the origin result is stable and must have its own endpoint:

- **Noisy provenance inference:** measure relation discovery against verified source/artifact lineage; this is a new study, not a continuation of F2.
- **Human comprehension/correction:** compare cue/packet interfaces with PaperTrail-like claim/evidence displays, measuring seeded correction, inspection, burden, and automation bias.
- **Profiled action policy:** compare acquisition/hold/abstain/escalate routing against Search Wisely, RA-RAG, DOS RAG, and Pendo-like baselines under explicit budgets.
- **Origin-bound memory/security:** compare append-only lineage and action authorization against memory-poisoning and manufactured-corroboration threats, with authenticated origins and a separate threat model.

If no one next study can state a single primary estimand and a falsifiable stop condition, retire the universal framework paper and publish the benchmark or null finding instead.

## Compact must-change / optional / reject table

| Priority | Change | Reason |
|---|---|---|
| **Must change** | Re-title the first paper around **origin-relation cue use** or **provenance-aware origin accounting**. | The broad “discrimination layer” label collides with several established fields and overstates the study. |
| **Must change** | State F2 as oracle relation metadata and F2–F1 as the only headline contrast. | Current oracle-context literature makes this distinction central; the model is not inferring provenance. |
| **Must change** | Add HydraRAG, CONFACT, ProvenanceGuard, Louck’s origin-bound memory preprint, Xia’s four-condition protocol, Pandey’s oracle-utilization preprint, Astaraki’s gold-context diagnostic, and Sabouhi’s source-boundary manuscript to the prior-art discussion. | These are the nearest 2025–26 technical precedents and must be confronted directly. |
| **Must change** | Add NoMIRACL, BERGEN, DOS RAG, KUP, PaperTrail, and the current oracle-utilization negatives to the null-result section. | A positive cue result is otherwise vulnerable to ceiling, utilization, and complexity objections. |
| **Must change** | Cite ACL 2025 authority-bias and attribution-bias studies when discussing source-role labels, authority, trust, or human correction. | Metadata can alter model attribution and reliance without changing evidentiary content; this is a direct cue-leakage threat. |
| **Must change** | Use `origin dependence` / `origin relation`; reserve `independent-as-stipulated` for the synthetic manifest. | Unqualified independence and consensus exceed the truth boundary. |
| **Must change** | Pre-register false-corroboration reduction, valid-origin recall non-inferiority, relation noise, leakage audits, and invalid-output handling. | Prevents a fragile formatting or instruction effect from becoming a provenance claim. |
| **Must change** | Match fixed-width metadata, report text, output contract, model calls, and resource cost across F1/F2. | DOS RAG and oracle-context work show that complexity and token differences can dominate. |
| **Must change** | Explicitly report F1 = F2 as an instruction-rule result, not a typed-cue result. | This is a primary negative/null interpretation, not a failed study. |
| **Optional** | Add neutral relation labels and codebook/position/paraphrase stress sets. | Useful to quantify label and wrapper dependence after the primary test is locked. |
| **Optional** | Add a public transfer challenge with unknown origin preserved and no relabeling of URL/source diversity as independence. | Provides a bounded external validity check without corrupting the synthetic estimand. |
| **Optional** | Release generator, manifests, relation schema, parser, hashes, replay checker, leakage report, and negative outputs. | A benchmark artifact may be publishable even if the effect is null. |
| **Optional** | Run a separate human terminology/comprehension pilot. | Only this can justify retaining “discrimination layer” as a public scientific label. |
| **Reject** | Claim a novel universal pre-generation layer or mechanism. | Current integrated systems cover the broad responsibility surface. |
| **Reject** | Call stipulated multiple origins “real independent corroboration,” “consensus,” or “truth.” | Synthetic provenance establishes graph membership by construction only. |
| **Reject** | Treat relation cue success as provenance discovery, evidence quality, source authority, retrieval quality, or human decision improvement. | None of these are identified by F2–F1. |
| **Reject** | Use trust, confidence, citation count, fluency, or packet presence as primary safety evidence. | Current human and attribution literature shows these can diverge from behavior and correctness. |
| **Reject** | Expand to routing, memory, human correction, or deployment solely because F2 succeeds. | Each requires a separate estimand, baseline, threat model, and stop criterion. |

## Bottom line for the parent project

**[I]** The 2024–2026 literature closes most of the conceptual novelty gap that remained in the first prospectus. The searched systems, benchmarks, and clearly labeled current research artifacts use source reliability, cross-source corroboration, fact-level conflict, fine-grained provenance, source admissibility, oracle evidence, dynamic retrieval, stopping, and memory/action gates; some of the closest 2026 items remain preprints or working manuscripts.

**[I]** The project should stop trying to defend the phrase “discrimination layer” as a novel architecture. The defensible research contribution is a much smaller, falsifiable measurement claim: whether a frozen model uses a supplied typed origin-relation cue to avoid false corroboration beyond an explicit origin-counting rule, under stipulated synthetic provenance and matched resources.

**[H]** If that effect is stable and survives the specified negative controls, the artifact may justify a benchmark paper and a later profiled-policy study. If it is null, rule-only, formatting-only, oracle-only, or recall-harming, that is still a useful result—but the correct conclusion is to retire the typed-cue novelty claim and publish the boundary/complexity finding. In either case, the broad “layer” thesis should remain a historical framing or research agenda, not the empirical paper’s headline.
