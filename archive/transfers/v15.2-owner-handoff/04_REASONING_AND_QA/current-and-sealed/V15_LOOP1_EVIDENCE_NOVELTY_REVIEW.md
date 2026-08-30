# V15 loop 1 evidence and novelty red-team review

## Review identity and disposition

- **Target worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-loop1`
- **Review branch:** `codex/discrimination-layer-v15-loop1-review`
- **Reviewed base:** `6423a43` (`Record v15 reader integration gate`)
- **Review date and status cutoff:** 2026-08-18
- **Review type:** independent evidence, citation, publication-status, and novelty-boundary review
- **External effects:** none. No model, provider, paid service, deployment, publication, contact, or dataset download was used.
- **Disposition:** `FAIL_PENDING_REQUIRED_FIXES`
- **Finding count:** P0: 0; P1: 1; P2: 5

This report is the only intended change in this lane. It does not edit the frozen manuscript, reader, research memos, matrix, or decision ledger. The disposition is not a statement that the study has run; the target package repeatedly says that it has not.

## Scope and exact checks

I inspected the required v15 surfaces line-by-line:

- `source/THOUGHT_PIECE_V15.md`
- `site/app/page.tsx`
- `site/app/content.ts`
- `research/PRIOR_ART_DELTA_V1.md`
- `research/PAPER_PROSPECTUS_V1.md`
- `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`
- `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md`
- `reports/V15_DECISION_LEDGER.md`

For reconciliation, I also checked `research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md`, the status-bearing source cards in the delta, the current source array in `site/app/content.ts`, and the offline origin-accounting implementation references used by the protocol. The exact checks were:

1. Compared every prior-art and residual-novelty statement in the manuscript and reader against the delta, adjacent-fields map, prospectus, claim/source/artifact matrix, and ledger.
2. Searched all reviewed surfaces for the terms `independence`, `INDP`, `origin relation`, `unknown`, `calibration`, `MMR`, `SetR`, `NEST`, `RARE`, `Schelpe`, `Zhang`, `Naphade`, `Ross`, `Li`, and `EvidentialRAG`.
3. Checked whether each material source separates a primary-record fact from the project inference, the claim it blocks, and the residual use. The source ledger below records that audit.
4. Checked publication status and exact URLs in primary or official records as of the review cutoff. A working manuscript, an acceptance claim without a venue page, and a published venue record are kept distinct.
5. Compared the F0/F1/F2 conditions, `FC_cons`, VOR, fixed denominators, `UNKN`, calibration exclusion, descriptive T1 boundary, comparator disposition, and no-results status across the manuscript, protocol, prospectus, site Lab, matrix, and ledger.
6. Checked for result language, generic mechanism novelty, provenance-inference, real-world independence, human-effect, transfer, or deployment leakage in the reader and manuscript.
7. Ran repository-level read-only status/hash checks and will run `git diff --check` plus a standard-library Markdown URL/syntax check after adding this report. The site dependency directory is absent in this isolated worktree, so the Next/ESLint build cannot be rerun here without installing packages; no installation was attempted.

## Primary-source verification ledger

The entries below deliberately distinguish the record from the project interpretation. “Blocks” states what the record prevents the project from claiming. “Residual” states the narrow use that remains available.

| Source and primary/official record | Sourced fact and exact finding used | Project inference and blocked claim | Residual use |
| --- | --- | --- | --- |
| Dong, Berti-Équille & Srivastava, [Integrating Conflicting Data: The Role of Source Dependence](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf) | PVLDB 2(1), VLDB 2009 published paper. It models source dependence in truth discovery, including partial/transitive copying and the warning that matching values alone do not establish copying. | Source dependence and copying-aware truth discovery are established. The project cannot present a generic copy detector, dependence model, or truth-discovery mechanism as unoccupied. | A bounded source-dependence precedent and a reason to keep recurrence, derivation, and support separate. |
| Dong, Berti-Équille & Srivastava, [Truth Discovery and Copying Detection in a Dynamic World](https://www.vldb.org/pvldb/vol2/vldb09-335.pdf) | PVLDB 2(1), VLDB 2009 published paper. It treats copying and source quality as time-varying rather than fixed. | Time-varying copying/source-quality handling is also established; the project cannot imply that mutable origin relations are a new general mechanism. | A boundary for later temporal relation work; it does not supply the current synthetic cue contrast. |
| Senn, [Overstating the evidence](https://doi.org/10.1186/1471-2288-9-10) | BMC Medical Research Methodology 9:10 (2009), published refereed article. Shared studies, arms, or analyses can be double-counted and create spurious precision when the analysis unit is wrong. | Repeated reports or rows cannot be treated as independent evidence merely because they are separately displayed. The project cannot claim the general double-counting principle as its own mechanism. | An effective-independence/accounting analogy for declaring the unit and preserving dependence. |
| Greenberg, [How citation distortions create unfounded authority](https://pubmed.ncbi.nlm.nih.gov/19622839/) | BMJ 2009 published article. Its citation-network analysis documents distortion and amplification of an unsupported claim into apparent authority. | Citation recurrence is not new support. The project cannot claim citation-network amplification or a generic anti-amplification mechanism as new. | A bounded precedent for separating recurrence, authority, and claim support. |
| Silcock et al., [NEWS-COPY](https://arxiv.org/abs/2210.04261) and [ICLR 2023 poster record](https://iclr.cc/virtual/2023/poster/11067) | Published ICLR 2023 duplicate-detection contribution. Its duplicate relation is tied to the same original article despite abridgement/OCR variation. | A duplicate detector and noisy/semantic reproduction control are established. A nonduplicate result does not establish a separate origin, and NEWS-COPY cannot provide the current typed support relation. | A bounded same-original/dependent fixture candidate for descriptive T1, subject to rights and annotation gates. |
| Silcock, Arora, D’Amico-Wong & Dell, [Newswire](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets & Benchmarks Track published paper. It supplies historical news reproduction clusters; the third author is Luca D’Amico-Wong. | Cluster recurrence is not a count of distinct origins, and the record does not supply claim stance, support-origin sets, or real-world separate-root labels. The project cannot use cluster size as an origin result. | Aggregate recurrence context or bounded descriptive T1 material, with rights/version/field gates. |
| Zhang, Ives & Roth, [“Who said it, and Why?” Provenance for Natural Language Claims](https://aclanthology.org/2020.acl-main.406/) | ACL 2020 published paper. It defines provenance graphs for natural-language claims, models provenance inference as information extraction/textual entailment, and evaluates the approach on two benchmark datasets. | Natural-language claim provenance and report/paraphrase origin reasoning have a direct published precedent. The project cannot imply that a provenance/common-origin graph over claims is an unoccupied design space, nor that the current study discovers provenance. | A close comparator for inferred claim provenance. The residual study must be distinguished as a supplied, benchmark-stipulated relation field tested against a byte-identical rule-only condition, not an inference system. |
| Carbonell & Goldstein, [MMR](https://doi.org/10.1145/290941.291025) | SIGIR 1998 published ACM record. Maximal marginal relevance is a diversity-based document reranking method. | Diversity-aware reranking is established; the project cannot claim a new redundancy penalty or set-diversity primitive. | An adjacent/future matched-budget comparator, not a required arm in the locked F0/F1/F2 core. |
| Lee et al., [SetR](https://aclanthology.org/2025.acl-long.861/) | ACL 2025 main-conference published paper. It selects a collectively covering retrieval set and explicitly addresses redundancy. | Set-wise coverage and redundancy reduction are established; the project cannot claim set construction as new or treat it as source-origin certification. | An adjacent/future set-selection comparator, not a required added arm in the locked core. |
| Verma et al., [NEST](https://aclanthology.org/2026.acl-industry.35/) | ACL 2026 Industry Track published record. It combines nested retrieval scopes with survival-consistent MRR selection intended to remove redundancy while preserving recall. | Training-free redundancy removal and recall/selection separation are established adjacent mechanisms; the project cannot claim them as a new layer or as origin-family inference. | An adjacent/future retrieval control. |
| Cho & Lee, [RARE](https://arxiv.org/abs/2604.19047) | arXiv v2 record, submitted 2026-04-21 and revised 2026-06-30, says accepted to ACL 2026 Main Conference; no ACL venue page was located in this pass. It evaluates redundancy in high-similarity corpora with fact-level overlap. | Redundancy-aware evaluation and fact-overlap tracking are not new, and the acceptance record must not be presented as a venue publication page. RARE does not establish copying, common authorship, or factual correctness. | An accepted-but-status-qualified adjacent benchmark-design comparator. |
| Schelpe, [Byte-Exact Deduplication in RAG](https://arxiv.org/abs/2605.09611) | arXiv v1 preprint record submitted 2026-05-10; the record calls it a preprint. It studies byte-exact deduplication across RAG regimes. | Exact deduplication is an existing control; the project cannot treat it as a new mechanism or as an origin relation. | An unreviewed byte-exact adjacent comparator, not a required F0/F1/F2 arm. |
| Wang et al., [RAMDocs](https://arxiv.org/abs/2504.13079) | COLM 2025 conference paper. It benchmarks RAG with conflicting evidence, ambiguity, misinformation, and noise. | Conflict handling and evidence interaction are established; conflict is not derivation/common-origin relation. The project cannot claim a vacant conflict-aware RAG layer or factuality result. | An adjacent/future conflict comparator, not a required added arm in the locked core. |
| Li, Padman & Krishnan, [Same Question, Different Source, Different Answer](https://arxiv.org/abs/2605.29084) | arXiv v1 submitted 2026-05-27; the checked record shows no venue acceptance. It audits answer variation across institutional source sets and uses a source-dependence taxonomy for cross-source answers. | Cross-source answer variation is not a derivation or common-origin relation. The project cannot repurpose the taxonomy as origin-family labels or claim source-dependent RAG auditing as new. | An unreviewed source-set/comparative behavior comparator. |
| Hossain, Shayoni & Mridha, [EvidentialRAG](https://arxiv.org/abs/2607.10491) | arXiv v1 submitted 2026-07-11; the checked record shows no venue or acceptance. It uses evidential fusion, conflict-aware routes, and abstention for multi-source RAG. | Conflict/uncertainty fusion is not provenance or derivation. The project cannot claim a new conflict-aware uncertainty layer or infer source origin from its outputs. | An unreviewed conflict/uncertainty comparator, adjacent/future only. |
| Naphade, [Rational Synthesizers or Heuristic Followers?](https://arxiv.org/abs/2601.06189) | arXiv v1 submitted 2026-01-08; the record comment says ACL ARR submission and shows no acceptance. Table 4 reports distinct/paraphrased opposing-evidence rates of 67.6%/76.5% for DeepSeek-R1-8B, 63.7%/75.6% for Gemini-2.5-FL, 62.9%/69.8% for Llama-3.1-70B-Instruct, and 67.3%/73.7% for Qwen3-32B. | Paraphrase/redundant-group behavior is a close unreviewed behavioral precedent, but its “distinct documents” are not verified separate origins. The project cannot attribute 67.6%/76.5% to Llama, treat document distinctness as origin independence, or claim a universal paraphrase law. | An unreviewed model-behavior comparator; the corrected DeepSeek/Llama attribution must remain visible. |
| Ross et al., [How retriever redundancy and diversity impact RAG effectiveness](https://arxiv.org/abs/2608.13956) | arXiv v1 submitted 2026-08-14; the checked record shows no venue or acceptance. On FictionalQA it compares exact duplicates, paraphrases of one document, and diverse genre documents; duplicate/paraphrase sets show no significant correctness gain in the reported setup, while diverse sets improve correctness by 17–47%. | Its controlled redundancy result does not establish a universal RAG law or verified origin independence. The project cannot treat the manuscript as settled evidence or as the same estimand as F2 minus F1. | The closest current unreviewed redundancy comparator and design reference for future matched conditions. |
| Laitenberger, Manning & Liu, [Stronger Baselines for RAG](https://aclanthology.org/2025.emnlp-main.1656/) | EMNLP 2025 published ACL record. It compares multi-stage systems with DOS RAG, a simple retrieve-then-read method preserving original passage order, under scaled token budgets; it recommends strong simple baselines and matched budgets. | Added complexity needs a matched resource comparison; the source does not make the locked F0/F1/F2 study require a new arm. The phrase “source-faithful simple baseline” is a fair project gloss of the paper’s source-fidelity finding, but should be marked as inference. | A published baseline-discipline precedent and adjacent/future comparator. |

## Findings

### P0 — none

No P0 finding was identified. The package does not report a model outcome, participant outcome, transfer result, deployment result, or broad mechanism result. The absence of such claims is supported consistently by `source/THOUGHT_PIECE_V15.md:5-9`, `site/app/page.tsx:67-69`, `site/app/page.tsx:523-533`, `research/PAPER_PROSPECTUS_V1.md:1-10`, `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-13`, `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md:15-25`, and `reports/V15_DECISION_LEDGER.md:14-35`.

### P1-01 — omitted closest direct natural-language provenance comparator

- **Locations:** `research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md:24-28`, especially line 26; `research/PRIOR_ART_DELTA_V1.md:63-84`; `source/THOUGHT_PIECE_V15.md:299-341`; `research/PAPER_PROSPECTUS_V1.md:52-78`; `site/app/content.ts:278-293`.
- **Exact repository evidence:** the adjacent-fields map labels Zhang, Ives & Roth (ACL 2020) “the closest direct precedent for common-origin reasoning over reports and paraphrases.” A search for `Zhang|Ives|Roth` returns no match in the integrated delta, thought piece, prospectus, or site source array. The delta’s status ledger instead starts with S1–S18 and does not carry this map entry.
- **Primary verification:** the [ACL Anthology record](https://aclanthology.org/2020.acl-main.406/) identifies a published ACL 2020 paper whose stated contribution is a formal natural-language claim-provenance graph with provenance inference and benchmark evaluation. This is not a claim that Zhang et al. test the current F2 condition; it is a direct precedent for the representation and task neighborhood.
- **Why material:** the residual v15 question is framed around an origin-relation field and reports/paraphrases. Leaving the map’s closest direct natural-language provenance record out of every reader-facing novelty boundary makes the residual look farther from prior work than the project’s own map supports. It also weakens the required distinction between inferred provenance and a supplied benchmark relation.
- **What it blocks:** the project cannot imply that natural-language claim provenance, report/paraphrase origin graphs, or common-origin reasoning are unoccupied. It also cannot imply that the current F2-minus-F1 study evaluates provenance inference.
- **Required fix:** add a status-bearing source card to `research/PRIOR_ART_DELTA_V1.md` with sourced fact, project inference, blocked claim, and residual contribution; cite it in the manuscript and prospectus; add it to the reader or link the full delta from the source section. Reconcile `V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md` and `V15_DECISION_LEDGER.md` if the residual wording changes. Keep the residual narrow: supplied relation metadata versus the explicit rule, not inferred provenance.
- **Disposition:** `MODIFY` before a clean package pass.

### P2-01 — nearest retrieval comparators are not visible on the final reader/manuscript source surface

- **Locations:** `research/PRIOR_ART_DELTA_V1.md:77-82`, `research/PRIOR_ART_DELTA_V1.md:342-354`, `source/THOUGHT_PIECE_V15.md:314-322`, `site/app/page.tsx:614-624`, and `site/app/content.ts:278-293`.
- **Exact repository evidence:** the delta carries MMR, SetR, NEST, RARE, and Schelpe with primary URLs and status. The manuscript names MMR and SetR but does not link MMR and does not surface NEST, RARE, or Schelpe in the prior-art paragraph. The reader’s “Selected primary and official references” array includes SetR and Ross but omits MMR, NEST, RARE, and Schelpe.
- **Why material:** the reader’s source paragraph states that duplicate detection and retrieval diversity have direct precedents, but the most relevant direct comparator records are discoverable only by opening the research memo. “Selected” limits the claim, so this is not a broad novelty failure; it is an auditability and nearest-comparator visibility defect.
- **Required fix:** either add the omitted records with exact status labels and their adjacent/future disposition, or make the selected list explicitly non-exhaustive and link the delta immediately beside it. Do not turn them into required added arms of the locked F0/F1/F2 study.
- **Disposition:** `MODIFY`.

### P2-02 — top-level reader terminology can be read as real-world independence

- **Locations:** `site/app/page.tsx:6-18`, especially lines 10-11; `site/app/page.tsx:191`; `site/app/content.ts:264`; `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:160-164`.
- **Exact repository evidence:** the reader’s distinction contract labels two rows “Recurrence / Independence” and “Independence / Different URLs, wording, or unknown origin,” and the definition note says “Authority, support, independence, relevance, authorization, and action priority remain different judgments.” The glossary instead defines “Origin relation” and explicitly says it is not real-world causal or epistemic independence; the protocol says the origin vocabulary must not absorb real-world independence.
- **Why material:** the receipt and Lab later use `INDEPENDENT-AS-STIPULATED`, and the limitations explicitly deny real-world independence, so the boundary is present. The unqualified central label nevertheless makes the public thesis sound broader than the locked construct, especially before the reader reaches the glossary or Lab.
- **Required fix:** change the central labels to “Origin relation / stipulated distinctness” or add “as stipulated” at the point of use, then align the definition note and challenge text. Preserve the explicit denial of real-world independence and the `UNKN` behavior.
- **Disposition:** `MODIFY`.

### P2-03 — manuscript prior-art status wording does not identify which working records are unreviewed

- **Locations:** `source/THOUGHT_PIECE_V15.md:324-335`; cross-check `research/PRIOR_ART_DELTA_V1.md:370-386`, `research/PAPER_PROSPECTUS_V1.md:68-78`, and `site/app/content.ts:286-292`.
- **Exact repository evidence:** the manuscript says the “last four” current comparisons have status/task boundaries that must remain explicit, then says only that “several are unreviewed working manuscripts.” It does not identify the status of Li/Padman/Krishnan, EvidentialRAG, Naphade, or Ross inline. The delta has exact dates and status labels; the reader labels some records but is not the manuscript.
- **Why material:** a reader of the manuscript cannot tell which records are published, venue-published, accepted with no venue page, or arXiv-only from the paragraph itself. This can make a working comparison look like settled venue evidence.
- **Required fix:** add a compact status parenthesis/table or link the status ledger immediately after the RAG paragraph. State the exact arXiv submission date and “no venue/acceptance shown” for Li, EvidentialRAG, Naphade, and Ross; keep RARE’s acceptance claim qualified until an ACL page is available.
- **Disposition:** `MODIFY`.

### P2-04 — stale project/case ownership wording remains in the integrated prior-art memo

- **Locations:** `research/PRIOR_ART_DELTA_V1.md:108` and `research/PRIOR_ART_DELTA_V1.md:368`.
- **Exact repository evidence:** line 108 says, “Any Signal Foundry origin field should be time-scoped and auditable.” Line 368 says, “None of these sources licenses an automatic independence detector for Signal Foundry.”
- **Why material:** Signal Foundry is a bounded case study, not the owner label for the whole research program. These sentences can make a case-study product name appear to own the research construct or imply a product-specific detector claim.
- **Required fix:** replace the case name with “the project” or “the project’s origin field,” preserving the bounded-case wording elsewhere. Recompute the memo hash and record the disposition in the ledger when the canonical file is amended.
- **Disposition:** `MODIFY`.

### P2-05 — one reader source entry presents a project inference as if it were the primary finding

- **Locations:** `site/app/content.ts:292`; related boundary `reports/V15_DECISION_LEDGER.md:118` and `research/PRIOR_ART_DELTA_V1.md:466`.
- **Exact repository evidence:** the Laitenberger entry says the published paper is a “reason to require added structure to beat a source-faithful simple baseline under matched resources.” The ACL record’s abstract instead describes DOS RAG as a simple retrieve-then-read method preserving original passage order, reports its benchmark comparison, and recommends a strong simple baseline with matched token budgets.
- **Why material:** the source supports the matched-baseline discipline and source-fidelity observation, but “require added structure” is the project’s implication, not a reported requirement from the paper. The current F0/F1/F2 lock deliberately keeps MMR/SetR/conflict systems adjacent or future rather than required arms.
- **Required fix:** split the entry into a sourced description (“published simple retrieve-then-read and matched-budget baseline precedent”) and a project inference (“therefore added structure needs a matched comparison”). Keep the inference explicitly adjacent/future and do not add a confirmatory arm without a separate decision.
- **Disposition:** `MODIFY`.

## Checks that passed and issues I tried to falsify

The following attempted falsifications did not produce a finding in this loop:

- **Generic mechanism novelty:** the manuscript, reader, delta, matrix, and ledger all reject a new generic copying, deduplication, conflict, source-dependence, or pre-generation mechanism claim. The primary records above support that narrowing.
- **Naphade attribution:** the corrected Table 4 assignment is present in `research/PAPER_PROSPECTUS_V1.md:73-78` and the delta; DeepSeek-R1-8B carries 67.6%/76.5%, while Llama-3.1-70B-Instruct carries 62.9%/69.8%.
- **Naphade status and construct:** the reviewed artifacts label it an ACL ARR-submission arXiv manuscript with no acceptance shown and do not treat “distinct documents” as verified separate origins.
- **Ross status and scope:** the reviewed artifacts identify 2026-08-14 submission, no venue/acceptance shown, FictionalQA, duplicate/paraphrase/diverse conditions, and the task-specific boundary. It remains a closest recent unreviewed comparator rather than settled evidence.
- **Li and EvidentialRAG:** the artifacts distinguish cross-source answer variation and conflict/uncertainty fusion from derivation/common-origin relations, and retain their arXiv-only statuses.
- **Newswire authorship and role:** the delta uses Luca D’Amico-Wong and treats Newswire clusters as recurrence context rather than origin labels.
- **F0/F1/F2 causal core:** the protocol and prospectus preserve the same-evidence, byte-identical rule-only comparison, explicit `UNKN`, fixed `A`/`M`, conservative invalid coding, and F2-minus-F1 contrast. No required added MMR, SetR, exact-dedup, or conflict-system arm was found.
- **Calibration boundary:** calibration is explicitly excluded from the confirmatory family unless a probability target and proper scoring rule are specified; descriptive confidence and abstention remain separate in `research/PRIOR_ART_DELTA_V1.md:466`, `research/PAPER_PROSPECTUS_V1.md:187-209`, and `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:349-382`.
- **T1 leakage:** NEWS-COPY and Newswire remain descriptive and outside `A`, `M`, intervals, tests, VOR, and effect estimates in the manuscript, reader, prospectus, protocol, matrix, and ledger.
- **Result leakage:** no checked surface presents a model result, effect estimate, participant result, field result, or deployment outcome as observed evidence.

## Required-fix order

1. Reconcile the omitted Zhang et al. provenance comparator and rerun the novelty wording check (P1-01).
2. Correct the reader’s origin-relation terminology and add/route the omitted nearest comparator records (P2-01 and P2-02).
3. Make manuscript status labels explicit and correct the two stale project-name references (P2-03 and P2-04).
4. Split the Laitenberger source fact from the project inference and verify that the adjacent/future comparator boundary remains unchanged (P2-05).
5. Rerun the same line-level and primary-source checks, then update the final-package hashes/ledger dispositions before treating the review gate as clear.

## Defensible residual claim after correction

The defensible residual is a protocol hypothesis, not an observed result:

> If an authorized run selects one frozen model, then on newly authored fictional evidence bundles whose origin relations are supplied by a benchmark graph, a typed relation cue may change that model’s all-assigned conservative false-corroboration behavior beyond an otherwise byte-identical rule-only condition; the fixed multiple-origin safety set protects recall.

This is a model-, task-, format-, prompt-, and stipulated-graph-specific question. It does not assert provenance inference, real-world independence, factual correctness, human or field benefit, transfer, deployment value, or broad mechanism novelty. The protocol must still pass its explicit pre-run gates, including tokenizer parity, leakage controls, semantic audit, fixed manifests, and the declared interval/coverage checks.

## Final PASS/FAIL disposition

**FAIL_PENDING_REQUIRED_FIXES.** There is no P0, and most high-risk status and empirical-boundary checks pass. The omitted ACL provenance comparator is a P1 novelty-reconciliation defect because the repository’s own map identifies it as the closest direct precedent for the exact origin/provenance neighborhood. The five P2 findings are required documentation and terminology corrections. After the named fixes, hash/ledger reconciliation, and a fresh line-level review, this lane can be reconsidered for `PASS` without expanding the locked F0/F1/F2 causal core.
