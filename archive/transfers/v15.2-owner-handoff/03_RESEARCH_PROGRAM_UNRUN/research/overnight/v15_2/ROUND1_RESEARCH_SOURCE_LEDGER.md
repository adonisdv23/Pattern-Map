# Round 1 research source ledger — Pattern Map v15.2

**Lane:** independent research/methods red team
**Prepared:** 2026-08-19
**Verification date for web records:** 2026-08-19
**Status:** primary-source ledger for bounded prior-art and methods claims
**Truth boundary:** no source below is evidence that the Pattern Map study ran
or that the proposed framework works.

## Reading and status rules

This ledger uses the following status vocabulary:

- **Published peer-reviewed paper/standard:** proceedings, journal, or standards
  record inspected at the publisher, society, or standards body.
- **Preprint:** public research record without a verified peer-reviewed venue in
  this pass. It can motivate a comparator or threat; it cannot establish field
  consensus or priority.
- **Working artifact:** author-provided manuscript or repository without a
  peer-reviewed status. It is supplemental only.
- **Local project artifact:** a repository file inspected as evidence of what
  this package says or implements. It is not external validation.

“Exact supported claim” means the narrow proposition directly supported by the
record. “Blocked claim” names the stronger statement that the record does not
support and that should not appear in Pattern Map prose. “Residual implication”
states what remains open for the project, without turning analogy into proof.

## A. Local package evidence and status boundary

| ID | Local record and status | Exact supported claim | Blocked claim | Residual implication |
| --- | --- | --- | --- | --- |
| L01 | `reports/overnight/v15_2/PROGRAM_CHARTER.md` — local integration contract | The overnight candidate must improve editorial, explanatory, design, and research hardening while preserving the no-study/no-result boundary. | The charter does not authorize a model run, preregistration, publication, or deployment. | Research recommendations must be framed as gates and future work, not execution. |
| L02 | `README.md:1-149` — local project readme | v15.1 is a conceptual synthesis, interactive reader, framework, and reproducible but unrun research program; no push or publication occurred. | The local package is not a validated research result or published study. | Handoff language can be confident about package status only, not efficacy. |
| L03 | `source/FRAMEWORK_COMPONENT_MAP.md:9-60` — local conceptual map | C01–C11 form a proposed responsibility decomposition with typed distinctions and explicit failure modes. | The map is not a minimal, complete, universal, novel, or validated architecture. | Use the map as a design contract and source of hypotheses; do not call it evidence. |
| L04 | `source/THOUGHT_PIECE_V15.md:24-127` — local authored argument | Repeated reports may preserve many observations while sharing one known origin under a stated relation rule. | A count of reports establishes independent support, truth, or real-world source independence. | Keep the “nine reports, one origin” example as the public anchor. |
| L05 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:14-77` — local frozen pre-run protocol | F2 is F1’s explicit rule plus stipulated relation values; primary set is 300 fictional bundles and safety set is fixed multiple-origin rows; no model/result exists. | F2 discovers provenance, proves independence, improves decisions, or validates the full layer. | The first paper can test only a narrow supplied-field condition effect. |
| L06 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:300-373` — local endpoint contract | `FC_cons` risk-codes invalid outputs and asserted counts ≥2 on `none/single/unknown`; VOR requires valid count ≥2 plus ≥2 selected support origins. | `FC_cons` is a pure semantic false-corroboration measure; VOR is exact origin-counting accuracy. | Scientific prose must call these a conservative risk endpoint and threshold safety guardrail. |
| L07 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:379-445` — local analysis/power contract | Paired McNemar/binomial plus bootstrap and a fixed-M one-sided guardrail are intended; N=300/M=75 are planning inputs. | The current scaffold demonstrates adequate power or coverage. | Freeze and validate the final interval method before preregistration. |
| L08 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:447-575` — local controls/release contract | Codebook, metadata-only, field-only, noise, split, invalid, negative-result, T1, and release-boundary controls are specified. | Listing a control is the same as passing it; T1 is a primary transfer result. | Treat unresolved controls as P0 gates and keep T1 descriptive/rights-gated. |
| L09 | `reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:12-112` — local QA receipt | Prior implementation defects were repaired and 15 focused tests/full synthetic generation smoke paths pass under offline conditions. | The repair pass authorizes a pilot or demonstrates model behavior. | Preserve the “implementation pass, not run authorization” wording. |
| L10 | `tests/test_origin_accounting.py:1-485` — local regression suite | Local generator/parser/scorer/manifest/power scaffolding invariants are exercised offline. | Unit tests show semantic model use, provenance discovery, or external generality. | Add fixtures for invalidity decomposition and count/stance/evidence incoherence before lock. |

## B. Primary prior-art and methods ledger

| ID | Primary record and status (verified 2026-08-19) | Exact supported claim | Blocked claim | Residual implication for Pattern Map |
| --- | --- | --- | --- | --- |
| S01 | W3C, **PROV-O: The PROV Ontology** (W3C Recommendation, 2013). [Official standard](https://www.w3.org/TR/prov-o/) | PROV-O provides a formal vocabulary for entities, activities, agents, derivations, specialization, attribution, and temporal/lineage relations. | PROV-O does not certify truth, source independence, relevance, authorization, or decision quality. | A “provenance spine” is an integration/use proposal, not a new provenance vocabulary. State which fields are PROV-compatible and which are project-specific. |
| S02 | Zhang, Ives & Roth, **“Who said it, and Why?” Provenance for Natural Language Claims** (ACL 2020, published peer-reviewed proceedings). [ACL Anthology](https://aclanthology.org/2020.acl-main.406/) | Defines a provenance graph for a natural-language claim, models provenance inference using information extraction/textual entailment, and evaluates it on two benchmark datasets for claim verification. | It does not test the supplied F2 relation field, the F1 rule-only control, the current FC/VOR endpoints, or action routing. | Directly blocks generic claims that claim provenance graphs or origin tracing are new; leaves a narrow cue-use contrast and a supplied-versus-inferred boundary. |
| S03 | Pochampally et al., **Fusing Data with Correlations** (SIGMOD 2014, published peer-reviewed proceedings). [ACM DOI](https://doi.org/10.1145/2588555.2593674) · [Author PDF](https://people.cs.umass.edu/~ameli/projects/dataIntegration/papers/corrFusion-SIGMOD2014.pdf) | Source correlation can be broader than copying: shared extraction rules can produce positive correlation and complementary source/extractor coverage can produce negative correlation; naive voting can fail. | It does not evaluate LLMs, natural-language origin cues, or the F2/F1 endpoint, and it does not show that its model transfers directly to the project corpus. | A binary dependent/distinct vocabulary is too coarse for a future general tool. Keep v1 codes narrow and plan typed relation, direction, scope, time, uncertainty, and relation provenance later. |
| S04 | Dong, Berti-Équille & Srivastava, **Integrating Conflicting Data: The Role of Source Dependence** (PVLDB/VLDB 2009, published). [PVLDB PDF](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf) | Source dependence and copying can distort truth discovery; dependence can be partial and shared values alone do not establish copying. | It does not establish that repeated reports in a natural-language bundle share an origin, or that a fixed `DPND` field solves the inference problem. | Preserve unresolved origin and relation uncertainty; do not treat lexical agreement as a discovered graph. |
| S05 | Dong, Berti-Équille & Srivastava, **Truth Discovery and Copying Detection in a Dynamic World** (PVLDB/VLDB 2009, published). [PVLDB PDF](https://www.vldb.org/pvldb/vol2/vldb09-335.pdf) | Copying and source quality can change over time; dynamic models use time-varying relationships and quality. | It does not validate static, immutable origin labels for open-world evidence or LLM behavior. | A future origin system needs time-scoped relations and update provenance; the first synthetic diagnostic must remain static by design. |
| S06 | Senn, **Overstating the evidence – double counting in meta-analysis and related problems** (BMC Medical Research Methodology 2009, published). [BMC DOI](https://doi.org/10.1186/1471-2288-9-10) | Counting the same study/report/arm more than once can overstate apparent evidence; unit and dependence handling must be transparent. | A meta-analysis analogy does not provide a universal web evidence correction or prove that the project’s relation rule is correct. | Supports the thought-piece discipline of preserving observations while separating aggregation units; label the transfer as analogy. |
| S07 | Greenberg, **How citation distortions create unfounded authority: analysis of a citation network** (BMJ 2009, published). [PubMed](https://pubmed.ncbi.nlm.nih.gov/19622839/) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2714656/) | A case-specific citation network can amplify an unsupported claim through repeated citations without new data and can omit/underweight refutation. | One network case does not establish that every high-recurrence cluster is copied, coordinated, false, or independent of new evidence. | Supports separating recurrence/citation traffic from support and origin; do not infer intent or truth from recurrence alone. |
| S08 | Silcock et al., **Noise-Robust De-Duplication at Scale** (ICLR 2023 poster, published conference contribution). [ICLR record](https://iclr.cc/virtual/2023/poster/11067) · [arXiv record](https://arxiv.org/abs/2210.04261) | Near-duplicate detection can handle OCR noise, abridgement, and scale using multiple matching methods. | Deduplication is not origin certification, truth finding, or evidence-quality assessment. | Blocks any claim that robust duplicate detection is a new mechanism; use it as an adjacency and future input to relation assignment. |
| S09 | Silcock et al., **Newswire: A Large-Scale Structured Database of a Century of Historical News** (NeurIPS 2024 Datasets & Benchmarks Track, published). [NeurIPS record](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html) | Historical news can be organized into large reproduction clusters around inferred wire originals. | Cluster size is not origin count, and a reproduction database does not provide the project’s target claim stance/support sets or real-world independence. | T1 may borrow documented same-original labels only with rights/version/annotation receipts; never map all distinct rows to `INDP`. |
| S10 | Carbonell & Goldstein, **The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries** (SIGIR 1998, published). [ACM DOI](https://doi.org/10.1145/290941.291025) | Diversity-aware reranking can reduce redundancy while preserving relevance in a retrieval set. | Diversity is not origin inference, provenance, claim support, or truth. | The broad “avoid redundant context” idea is established; the project’s remaining question must be relation-cue behavior, not generic diversity. |
| S11 | Lee, Jo, Park & Lee, **Shifting from Ranking to Set Selection for Retrieval Augmented Generation** (ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.acl-long.861/) | Retrieval-set selection can optimize joint coverage/redundancy rather than independent document ranking. | It does not provide stipulated origin-family metadata or test F2/F1. | Any “set-wise evidence selection” novelty language is blocked; compare against simple set/redundancy baselines in a future architecture study. |
| S12 | Ge et al., **Resolving Conflicting Evidence in Automated Fact-Checking: A Study on Retrieval-Augmented LLMs** (IJCAI 2025, published peer-reviewed proceedings). [IJCAI record](https://www.ijcai.org/proceedings/2025/1073) | CONFACT evaluates RAG under conflicting information from sources with differing credibility and reports vulnerabilities plus gains from credibility-aware handling. | Credibility is not origin dependence; source background does not establish copying or distinct origin. | Keep authority/credibility and origin relation as separate dimensions; conflict handling is established adjacent prior art. |
| S13 | Zhang et al., **FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation** (ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.acl-long.1062/) | Fact-level conflict between retrieved context and parametric knowledge can be modeled before generation; context adherence can have trade-offs. | It does not test a supplied origin-family relation field or prove that suppressing false corroboration improves truth or utility. | Supports retaining a safety/recall guardrail: a cue that reduces one risk while suppressing valid support is not a success. |
| S14 | Hagström et al., **A Reality Check on Context Utilisation for Retrieval-Augmented Generation** (ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.acl-long.968/) | Synthetic datasets can exaggerate context characteristics and yield inflated utilization findings relative to real retrieved context; source-related properties matter. | It does not evaluate origin accounting or prove that every synthetic diagnostic is invalid. | The project may use synthetic bundles for a bounded diagnostic, but must not generalize to real evidence without a separately authorized transfer/annotation study. |
| S15 | Laitenberger, Manning & Liu, **Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models** (EMNLP 2025, published). [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1656/) | Under scaled token budgets, a simple source-faithful retrieve-then-read baseline can match or outperform more complex multi-stage RAG systems. | It does not assess origin-relation metadata, false corroboration, or the project’s model. | Complexity tax is a direct design constraint: any extra relation/router layer must show a decision change per token/time/reviewer cost. |
| S16 | Abolghasemi et al., **Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models** (Findings ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.findings-acl.1087/) | Counterfactual authorship metadata changes attribution quality and reveals bias toward explicit human authorship in evaluated LLM/RAG settings; the reported abstract effect is 3–18% in that study. | It does not establish origin dependence, false corroboration, or semantic relation understanding; its task and models differ. | Metadata salience is a competing explanation. Codebook permutation, neutral labels, position controls, and report-masking diagnostics are required. |
| S17 | Li et al., **LLMs Trust Humans More, That’s a Problem! Unveiling and Mitigating the Authority Bias in Retrieval-Augmented Generation** (ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.acl-long.1400/) | Across six LLMs and varied tasks, the paper reports a user-versus-database authority bias and tests credibility-aware conflict mitigation. | Authority bias is not origin-family dependence, and its result cannot validate the F2/F1 cue. | Keep authority, source role, origin relation, and support as distinct fields; use authority metadata as a negative/control comparator. |
| S18 | Nematov et al., **Source Attribution in Retrieval-Augmented Generation** (arXiv 2025, preprint). [arXiv](https://arxiv.org/abs/2507.04480) | Applies Shapley-style and approximate attribution to retrieved documents and studies redundancy, complementarity, and synergy in document influence. | It does not supply `DPND`/`INDP`/`UNKN`, isolate F2 versus F1, or establish that source influence equals origin independence. | Directly blocks generic source-attribution novelty. The residual is a stipulated relation cue and its narrowly defined output-risk diagnostic. |
| S19 | Xia, **A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models** (arXiv 2026, preprint). [arXiv](https://arxiv.org/abs/2606.06758) | Uses matched no-evidence/full-context/retrieved/oracle-evidence conditions and reports observable utilization behavior across five local open-weight models; explicitly avoids treating outputs as internal causal attention. | It does not test origin relations, false corroboration, or the Pattern Map framework, and its preprint status is not peer-reviewed evidence. | The project’s oracle-cue framing is methodologically adjacent, not first. Borrow the behavioral-language boundary and matched-condition discipline. |
| S20 | TROVE, **A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification** (ACL 2025, published). [ACL Anthology](https://aclanthology.org/2025.acl-long.577/) | Provides source-sentence tracing and typed relationship classification for fine-grained text provenance. | Source-sentence provenance relations are not upstream report-origin families, and the paper does not test F2/F1. | Distinguish derivation/provenance relation types from the first study’s origin-family cue. |
| S21 | Wei et al., **GenProve: Learning to Generate Text with Fine-Grained Provenance** (ACL 2026, published). [ACL Anthology](https://aclanthology.org/2026.acl-long.228/) | Defines and evaluates fine-grained provenance relations such as quotation, compression, and inference in generated text. | Generation-time provenance relation typing does not establish source origin, truth, or a pre-generation action policy. | Further supports keeping derivation and origin vocabularies separate; do not call all relation typing “origin accounting.” |
| S22 | RFC 8785, **JSON Canonicalization Scheme** (IETF RFC, 2020). [RFC Editor](https://www.rfc-editor.org/rfc/rfc8785.html) | Specifies canonical JSON serialization rules and conformance expectations. | A canonical byte representation does not prove semantic validity, provenance, or replicability of a model run. | The local `deterministic-json-v1` helper must remain labeled non-RFC-conformant until independently tested before release. |

## C. Status-specific interpretation ledger

### Published evidence that should be used confidently, but narrowly

The strongest stable comparators for the package are PROV-O (S01), natural-
language claim provenance (S02), source dependence/correlation (S03–S05),
conflicting-evidence RAG (S12–S13), synthetic-context caution (S14),
complexity-matched baselines (S15), metadata/authority bias (S16–S17), and
fine-grained provenance relations (S20–S21). Each supports a bounded adjacent
claim. None is evidence for the Pattern Map effect.

### Preprints that should remain visible but status-labeled

Nematov (S18) and Xia (S19) are important current methodological comparators.
They should be cited as preprints, not as settled consensus or priority claims.
Their value is in bounding the residual and improving controls, not in proving
that the project is late or invalid.

### Claims not supported by this ledger

This pass found no source that supports any of the following stronger claims:

- the Pattern Map framework is a novel universal architecture;
- a model has discovered provenance or real-world independence in this package;
- origin-relation metadata improves truth, human decisions, safety, or utility;
- a model internally reasoned over relation fields;
- `N=300` is adequately powered without a frozen operating-characteristic
  receipt;
- the local surrogate tokenizer is equivalent to a selected model tokenizer;
- a synthetic effect transfers to public news, production tools, or deployment;
- the project is the first to study evidence/cue use in any broad sense.

## D. Search limitation and update rule

This is a targeted primary-source audit, not a systematic review, patent search,
or exhaustive absence finding. The correct novelty language is:

> In the primary records checked through 2026-08-19, we did not locate a
> peer-reviewed study that isolates this exact F2-versus-F1 contrast on the
> project’s conservative asserted-count-risk endpoint with stipulated origin
> graphs. That is a bounded search statement, not proof of priority or absence.

Before any paper submission, rerun the search with the exact model/task/date
cutoff, inspect new records, and update every status field. A newly found close
study should narrow the residual claim rather than be hidden in a supplement.

## E. Source-to-decision map

| Decision | Sources that constrain it | Required project wording |
| --- | --- | --- |
| Broad architecture novelty | S01–S05, S10–S13, S18, S20–S21 | “Boundary-preserving synthesis/design hypothesis,” not new universal layer. |
| Origin relation semantics | S03–S05, S18, S20–S21 | “Stipulated relation cue” with explicit type/status/scope; not real independence. |
| Matched condition design | S14–S19 | “Observable condition effect”; include oracle, synthetic, one-model, and metadata-bias limits. |
| Simplicity/cost | S10–S11, S15 | Compare to simple baselines and report token/latency/reviewer cost. |
| Public thought-piece example | S06–S09, local L04 | Preserve reports while separating observations, origins, support, and action. |
| Transfer/T1 | S07–S09, local L08 | Descriptive, rights/version/annotation gated; never primary evidence. |
| Reproducibility release | S22, local L07–L09 | Local receipts are implementation scaffolding; release-grade canonicalization and schemas remain open. |

## F. Parent integration note

The parent integrator should use this ledger to update the v15.2 convergence
record without editing the canonical source from this lane:

1. Retain the current narrow F2/F1 question and explicit no-result boundary.
2. Replace “new discrimination layer” and “model used metadata” with the
   bounded condition-effect language above.
3. Add invalidity decomposition and count/stance/evidence coherence to the P0
   method gates.
4. Keep `N=300`, `|M|=75`, T1, tokenizer parity, and shortcut controls visibly
   provisional until their receipts exist.
5. Cite S01–S21 with status labels and never use this ledger as evidence that
   the study ran.
