# Empirical Research Design for the Pattern Recognition / Discrimination Layer

Status: overnight research design; protocol proposal only; no experiment, recruitment, live retrieval, paid provider call, deployment, or publication was performed.

Repository context: the local repository has no repository-specific `AGENTS.md`. Its README, thesis contract, thought piece, prior-art map, claims register, and research-paper readiness path were reviewed. The repository explicitly says that the current work is a provisional thought piece and research agenda, that it contains no empirical validation, and that Alpha Solver and Signal Foundry are bounded implementation contexts rather than evidence. This memo preserves that boundary.

## 1. Purpose and claim boundary

The broad thesis is that an AI system may benefit from an explicit responsibility for deciding what context to acquire, identify, preserve, compare, enrich, admit, withhold, and update before generation, with inspectability, cost bounds, source awareness, and human correction. That sentence is a design proposition, not an observed result.

The first paper should test a smaller claim:

> For evidence-sensitive tasks in which reports can be dependent, contradictory, incomplete, or costly to inspect, a minimal typed context-judgment policy—preserving provenance and unknown dependence, separating claim support from source authority and relevance, and routing acquisition/abstention under a declared budget—can improve evidence-grounded task decisions or correction per unit resource relative to strong, simpler retrieval-and-citation workflows.

This formulation makes five commitments that can be falsified:

1. **Task scope:** the claim is initially about named evidence-sensitive task classes, not all AI use.
2. **Intervention:** the minimum tested intervention is typed context judgment, not the entire eleven-component conceptual map.
3. **Comparator:** “better” means better than strong matched baselines, not better than no system.
4. **Outcome:** the primary outcomes concern evidence-grounded correctness, appropriate abstention/routing, correction, utility, and cost—not fluency, citation count, or self-reported trust.
5. **Boundary:** any benefit must survive matched time, retrieval access, context/token limits, model budget, and review opportunity.

The design is intentionally staged. Construct validity and data quality precede efficacy claims; a controlled human study precedes any field pilot; independent replication precedes a general claim.

## 2. Evidence posture

The paper should mark every assertion as one of the following.

| Label | Meaning in this memo | Examples |
| --- | --- | --- |
| **Sourced evidence** | A bounded statement directly supported by a primary paper, standard, dataset paper, or official institutional source. | FEVER supplies claim labels and evidence sentences; PROV-O supplies a provenance vocabulary; long-context use can vary with position. |
| **Inference** | A reasoned implication from sourced evidence and the project’s distinctions. It is plausible but not itself measured here. | If copied reports are counted as independent, a model may overestimate corroboration. |
| **Speculative hypothesis** | A preregisterable prediction about the proposed intervention. | Origin-aware grouping will reduce false corroboration without unacceptable loss of independent evidence. |
| **Illustration** | A synthetic or bounded example used to make a construct concrete. | A migration-tool pilot packet with a vendor benchmark and rollback reports. |
| **Implementation context** | A product or repository artifact that may inspire a test but does not validate the framework. | Alpha Solver and Signal Foundry. |

The existing thought piece’s distinctions—recurrence is not independence, provenance is not correctness, authority is not support, relevance is not truth, and attention priority is not a factual conclusion—are conceptual synthesis until the studies below demonstrate that raters and systems can apply them reliably and that keeping them separate has measurable value.

## 3. Research questions and hypotheses

### Primary research questions

**RQ1 — Construct boundary.** Can independent raters reliably distinguish source authority, claim support, provenance/derivation, independence, recurrence, relevance, attention priority, enrichment value, action priority, disposition, and outcome without collapsing them into a single “trust” judgment?

**RQ2 — Evidence quality.** On dependent-evidence, contradiction, missingness, and multi-hop tasks, does typed context judgment improve the accuracy and completeness of evidence linked to a decision or generated answer?

**RQ3 — Human correction.** Does exposing typed evidence paths, unknowns, exclusions, and stopping reasons help people detect and correct system errors, or does the added structure create overload and automation bias?

**RQ4 — Resource-bounded routing.** Does explicit acquisition/stopping policy improve useful evidence or decision utility per unit time, token, compute, and reviewer attention, while retaining safety-critical recall?

**RQ5 — Scope and moderation.** Are effects concentrated in tasks with common-origin dependence, contradiction, temporal change, or high cost of error, and absent or negative in simple low-stakes controls?

**RQ6 — Revision and memory.** Under time-sliced evidence, does preserving origin through summarization and update reduce stale or provenance-laundered decisions without suppressing legitimate new evidence?

**RQ7 — Terminology and governance.** Does “discrimination layer” communicate the intended technical meaning to representative readers after definition, and do the interface and policy create unequal source coverage, privacy exposure, or unsafe reliance?

### Preregistered hypotheses

These are speculative predictions, not results.

| ID | Hypothesis | Primary test | What would count against it |
| --- | --- | --- | --- |
| H1 | Typed labels for support, authority, relevance, and independence are discriminantly valid: raters perform above a prespecified agreement floor and classify intentionally crossed cases correctly. | Construct-sorting study with hold-out cases. | Agreement is near chance, dimensions are inseparable, or a simpler two-label scheme performs equally well. |
| H2 | On dependent-evidence tasks, origin-aware grouping lowers false-corroboration rate at matched evidence budget. | Paired benchmark comparison; false corroboration is the primary endpoint for this class. | No reduction, or valid independent evidence is suppressed more often than copied evidence is discounted. |
| H3 | Claim/evidence support labels plus evidence spans improve supported-claim rate and contradiction/insufficiency detection over document relevance alone. | FEVER/SciFact/AVeriTeC-style tasks with provenance-controlled variants. | Gains disappear against a strong reranker or arise only from extra context/tokens. |
| H4 | A bounded router improves utility-adjusted evidence yield per cost and increases appropriate `acquire`, `answer`, `hold`, `clarify`, or `refuse` decisions. | Interactive synthetic acquisition environment with fixed menu and costs. | Fixed-budget retrieval matches or beats it; the router over-searches, stops too early, or harms high-severity recall. |
| H5 | A typed, progressive-disclosure evidence packet reduces time to correct seeded errors relative to ordinary citations without increasing inappropriate refusal. | Randomized human review study. | Correction is no better, review time is materially higher, or reviewers accept incorrect outputs more often. |
| H6 | Origin-bound memory reduces stale-memory and provenance-laundering errors over a temporal sequence. | Synthetic longitudinal benchmark with controlled updates and rollback. | No reduction, or the policy misses valid updates and increases stale decisions. |
| H7 | Effects are moderated by evidence dependence/contradiction and task stakes: benefits are larger on high-dependence tasks and near zero on low-dependence negative controls. | Hierarchical interaction model. | Benefits are uniform only because the intervention adds generic retrieval or formatting, or it harms simple tasks. |
| H8 | The name “discrimination layer” is not retained if a substantial fraction of representative readers infer social classification or unfair treatment after the technical definition. | Blinded comprehension and terminology comparison. | Persistent material misunderstanding or harm signal; the mechanism may remain while the name changes. |

### Minimum meaningful effects to set before the definitive study

The following are design candidates, not discovered thresholds. The preregistration must choose one primary endpoint per task class and set the minimum practically important difference before seeing definitive results. A reasonable starting set is:

- at least **+5 percentage points** in evidence-grounded task success or supported-claim rate;
- at least **−10 percentage points** in false-corroboration or unsupported high-consequence claim rate;
- at least **+0.15 standard deviations** in blinded decision utility, or a prespecified non-inferiority margin if safety and utility are the concern;
- at least **−15%** time to localize and correct a seeded error at no more than **+10%** total task time;
- no more than **+2 percentage points** loss in valid independent-evidence recall and no more than **+5 percentage points** inappropriate refusal;
- no subgroup disparity increase larger than a preregistered absolute **5 percentage points** without a documented mitigation and sensitivity analysis.

These values must be stress-tested using pilot variance, item difficulty, participant/task clustering, and multiple-comparison correction. They are not a license to declare small statistically significant changes useful.

## 4. Named task classes and test cards

Each task instance should carry a task-class code, evidence-dependence level, stakes level, temporal status, source-language/region slice where licensed, and a complete gold provenance graph or an explicit `unknown` state. The task itself—not the system’s output—defines the gold labels.

| Code | Named task class | Task instance | Gold object and primary endpoint | Why it tests the thesis |
| --- | --- | --- | --- | --- |
| **C0** | Construct discrimination and terminology | Raters classify short evidence packets and explain which labels apply: authority, support, relevance, independence, recurrence, attention, action, or disposition. Separate readers compare “discrimination layer” with “context judgment layer.” | Multi-label/ordinal construct labels, pairwise similarity, hold-out transfer, and restatement accuracy. | Tests whether the proposed distinctions are usable before claiming system value. |
| **C1** | Atomic claim verification with evidence | Given a claim and a bounded corpus, return `supports`, `refutes`, `insufficient`, or `contested`, with exact evidence spans and confidence. | Verdict accuracy/macro-F1, evidence precision/recall/F1, supported-claim rate, calibration. | Tests claim support without equating document relevance or source reputation with truth. |
| **C2** | Dependent-evidence/common-origin discrimination | Given reports that include originals, syndications, paraphrases, summaries, and unknown-origin items, identify the claim relation and count independent pathways. | Origin relation accuracy, false-corroboration rate, independent-evidence recall, `unknown` retention. | Directly tests “recurrence is not independence.” |
| **C3** | Multi-hop synthesis under contradiction and missingness | Answer a bounded question requiring multiple pieces of evidence, including one contradiction, one stale version, one irrelevant but authoritative document, and a missing expected perspective. | Decision/answer correctness, contradiction detection, gap classification, evidence-path completeness, abstention quality. | Tests graph relationships, gaps, and context selection rather than retrieval alone. |
| **C4** | Cost-bounded acquisition and stopping | In a simulator, choose among search, compare, enrich, ask, answer, hold, or refuse. Each action has declared time/token/compute cost and can reveal evidence with known probabilities. | Expected decision utility net of cost, evidence gain per cost, stopping regret, high-severity miss rate, budget compliance. | Tests whether explicit route/stopping policy is useful rather than merely verbose. |
| **C5** | Temporal memory, update, and rollback | Process a sequence of dated evidence, summaries, revisions, and outcomes. Later evidence may supersede or contradict earlier material. | Stale-memory error, origin-preserving recall, harmful update rate, calibration drift, rollback success. | Tests whether feedback revises policy without rewriting old evidence or laundering authority. |
| **C6** | Human evidence audit and decision support | Participants inspect model outputs under ordinary citation, typed packet, or ablated interface conditions, then accept, correct, defer, or escalate. | Blinded decision quality, seeded-error correction, appropriate reliance, time, workload, provenance localization. | Tests human correction and whether a “human in the loop” is substantive. |
| **C7** | Low-dependence/low-stakes negative controls | Simple supplied-input calculation, direct extraction, or creative rewrite with no disputed external evidence. | Accuracy, latency, unnecessary review, refusal/clarification rate, cost. | Prevents rewarding complexity or refusal when the framework is unnecessary. |

### Task construction rules

1. Keep **decision stakes synthetic or low consequence** until an ethics-approved study demonstrates safe operation. No participant should make a real medical, employment, financial, legal, production, or customer decision through the experimental system.
2. Use both **known-answer tasks** and **open-world-like packets**. The former permit precise scoring; the latter test unknown, insufficient, and contested states without pretending that an inaccessible source proves absence.
3. Place copied and independent evidence in matched lexical and topical distributions. Otherwise a source-identity cue, not the discrimination policy, can solve C2.
4. Include **counterbalanced error types**: unsupported completion, wrong source authority, false corroboration, stale evidence, missing expected perspective, overconfident uncertainty, and unnecessary refusal.
5. Include **negative cases** where additional search is not valuable and where the obscure/peripheral item is noise. “Peripheral” must never receive an epistemic bonus by construction.

## 5. Constructs and operational definitions

The intervention should expose typed records, not one master trust score. Scores may be used for a declared local action, but the underlying fields remain inspectable.

| Construct | Operational definition and observable record | Gold/measurement rule | Explicit non-meaning |
| --- | --- | --- | --- |
| Decision brief | Versioned question, intended decision, audience, allowed operations, expected baseline, stakes, and budgets attached to every run. | Binary protocol-compliance checks plus blinded reviewer rating of task fit. | Not a claim that the question or baseline is correct. |
| Operational authorization | Whether an action (retrieve, transform, disclose, retain, or act) is permitted in the task packet. | Gold policy in the task manifest; any violation is an error even if the answer is factually correct. | Not source authority or truth. |
| Source authority | Claim- and domain-scoped standing to answer a specified kind of question, coded `not assessed`, `low`, `scoped`, or `high`, with rationale. | Independent adjudicators apply a rubric that names the scope; use weighted agreement and audit disagreements. | Not universal trust, correctness, independence, or permission to act. |
| Claim support | Relation of a specific atomic claim to an evidence span: `supports`, `refutes`, `insufficient`, `contradictory`, or `unresolved`. | Gold labels and spans from expert/adjudicator panel; partial credit only for a predeclared span overlap/entailment rule. | Not document relevance, citation presence, or model confidence. |
| Provenance | Directed source/artifact/derivation/agent/time graph for each evidence item and transformation. | Synthetic graphs have exact truth; public packets use documented provenance and `unknown` where not established. Report node/edge precision, recall, and completeness. | Not correctness, authority, independence, or authorization. |
| Independence | Whether two observations have distinct relevant information pathways, coded `independent`, `dependent`, or `unknown`. | Gold relation in synthetic graph; human-adjudicated relation in public packets. Unknown is not independent. | Not mere different URLs, publishers, wording, or communities. |
| Recurrence | Number of observed artifacts/claims after artifact identity and origin grouping, with a timestamped count. | Compare raw repetition with origin-adjusted repetition. | Not corroboration or truth. |
| Relevance | Task-specific usefulness of an item for the declared question/decision and constraints. | Blind raters score 0–3 against a rubric before seeing system condition; report ordinal agreement. | Not authority, truth, popularity, or owner endorsement. |
| Attention priority | Rank/urgency for inspection given task consequences and uncertainty. | Compare rank correlation and top-k recall of adjudicated “must inspect” items. | Not truth probability or action approval. |
| Enrichment value | Predicted expected improvement in the primary outcome from an allowed next action minus its declared cost/risk. | Record prediction before action; compare to realized gain with calibration/regret. | Not evidence acceptance or action authority. |
| Action priority | Ordered route among `acquire`, `compare`, `enrich`, `ask`, `answer`, `hold`, `refuse`, and `escalate`. | Gold action is derived from a prespecified utility matrix and adjudicated safety constraints; report appropriate-action rate and regret. | Not a factual conclusion. |
| Owner disposition | Explicit human `accept`, `reject`, `defer`, `hold`, `override`, or `request-more-work` event with reason. | Agreement with blinded rubric is secondary; disagreement itself is preserved as data. | Not proof, objective truth, or permanent preference. |
| Context quality | The selected packet’s useful-evidence recall, irrelevant-context rate, material-exclusion error, and provenance completeness under a fixed context budget. | Score against gold useful/irrelevant/material categories. | More text, more sources, or more citations is not automatically better. |
| Evidence-grounded success | A task is successful only when the action/verdict is correct **and** the required evidence path/uncertainty state is acceptable. | Predeclared conjunctive rubric; no credit for a lucky unsupported answer. | Not fluency or user satisfaction. |
| Calibration | Agreement between stated probability and observed correctness. | Brier score, reliability curve, expected calibration error with a predeclared binning rule, and selective risk-coverage. Brier’s original scoring rule is [Brier (1950)](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VFOAAN%3E2.0.CO;2); neural calibration evaluation is [Guo et al. (2017)](https://proceedings.mlr.press/v70/guo17a.html). | Not authority, permission, or utility. |
| Decision utility | Net value of the selected action under the task’s declared consequences: `U = benefit(correct action) − harm(unsupported/high-severity error) − search cost − review cost − latency cost`. | Weights and severity tiers are fixed before the run; publish unweighted components and sensitivity to plausible weights. | Not a universal welfare function or proof of causal real-world benefit. |
| Auditability | Ability of an independent reviewer to reconstruct what was observed, selected, excluded, transformed, and why. | Provenance-path completeness plus blinded localization time and reconstruction accuracy. | More metadata is not automatically more understandable. |
| Human appropriate reliance | Accept correct output, correct incorrect output, defer when evidence is insufficient, and avoid unnecessary override/refusal. | Four-cell confusion matrix against gold system correctness and safety rubric. | Self-reported trust or liking. |
| Workload | Time, clicks, review minutes, NASA-TLX or a shorter validated workload instrument if a human study justifies it, and number of artifacts inspected. | Measure per task and per correctly resolved task; retain raw and normalized values. | “Easy” self-report alone. |
| Fairness/coverage | Error, burden, source-coverage, and exclusion metrics by predeclared topic, region, language, source type, and other relevant slices. | Report absolute and relative disparities with uncertainty; avoid inferring protected status of individuals. | A single aggregate score proving fairness. |
| Privacy/harm | Unauthorized acquisition, PII exposure, sensitive-content exposure, reputational risk, harmful recommendation, and unsafe over- or under-refusal. | Event log plus independent harm review; any critical event triggers quarantine/stop. | Absence of observed harm is not proof of safety. |

## 6. Candidate public data and an ethically collectable corpus

Public datasets are useful for narrow constructs, not as evidence that they contain the full layer. In particular, FEVER, SciFact, and AVeriTeC supply claim/evidence labels but do not by themselves provide complete common-origin ground truth. The study must not infer independence from their source count.

| Resource | Use | Direct primary/authoritative source | Fit and limitation |
| --- | --- | --- | --- |
| **FEVER** | C1 claim verdicts and evidence sentences; train/development only, with a locked evaluation split. | Thorne et al. (2018), [ACL Anthology / DOI 10.18653/v1/N18-1074](https://aclanthology.org/N18-1074/) | Large, public, and explicitly evidence-linked. Claims were generated from Wikipedia; it is a bounded benchmark, not open-world truth or common-origin evidence. |
| **SciFact** | C1 scientific claim/evidence/rationale and domain-shift tests. | Wadden et al. (2020), [ACL Anthology / DOI 10.18653/v1/2020.emnlp-main.609](https://aclanthology.org/2020.emnlp-main.609/) | Expert-written scientific claims and rationales. Abstract-level evidence and a narrow scientific corpus do not establish general authority or real-time updating. |
| **AVeriTeC** | C1/C3 web-claim verification, multi-step evidence, temporal leakage tests where the released snapshot permits. | Schlichtkrull, Guo, & Vlachos (2023), [arXiv:2305.13117](https://arxiv.org/abs/2305.13117); shared-task specification [DOI 10.18653/v1/2024.fever-1.1](https://doi.org/10.18653/v1/2024.fever-1.1) | Real-world claims checked by fact-checking organizations and evidence from the web. Content may be sensitive or reputationally harmful; use only licensed/released material, redact personal data, and do not treat fact-checker labels as universal truth. |
| **HoVer** | C3 multi-hop retrieval and verification. | Jiang et al. (2020), [ACL Findings / DOI 10.18653/v1/2020.findings-emnlp.309](https://aclanthology.org/2020.findings-emnlp.309/) | Tests multi-hop evidence chains. Wikipedia provenance remains bounded and does not supply independent-source truth. |
| **Natural Questions** | C1/C3 retrieval and answerability/null-answer controls. | Kwiatkowski et al. (2019), [TACL / DOI 10.1162/tacl_a_00276](https://doi.org/10.1162/tacl_a_00276); official [Google release](https://ai.google.com/research/NaturalQuestions/download) | Real anonymized aggregated queries and Wikipedia pages with annotated answers. It is not a claim-support or source-dependence benchmark; use for retrieval/answerability only. |
| **BEIR** | Retrieval baseline stress test across heterogeneous domains; not a full layer benchmark. | Thakur et al. (2021), [NeurIPS Datasets and Benchmarks paper](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/65b9eea6e1cc6bb9f0cd2a47751a186f-Abstract-round2.html) | Useful for zero-shot retrieval comparison. Relevance judgments do not equal claim support, provenance, or decision utility. |
| **TREC collections** | Optional authoritative retrieval test collections and reproducible search baselines. | [NIST TREC overview and tracks](https://trec.nist.gov/) | Use only collections whose license and task fit are documented. TREC relevance is not truth or authorization. |
| **Synthetic provenance benchmark** | C2–C5 causal tests with exact origin, derivation, contradiction, staleness, and cost truth. | New benchmark; release generator, seeds, manifests, and a dataset card. | Necessary because public corpora do not provide complete dependence labels. Synthetic cases must be audited for realism and paired with public cases. |

### Synthetic benchmark specification

Construct a graph generator whose hidden truth contains:

- source, artifact, version, timestamp, and transformation nodes;
- claims and evidence spans;
- original reports, verbatim copies, paraphrases, summaries, translations, and coordinated variants;
- independent observations that share vocabulary but not origin;
- contradiction, partial support, stale versions, and expected-but-missing evidence;
- action costs, deadlines, permission states, and severity tiers.

Generate matched sets in which only the origin relationship changes. For example, a claim can have four agreeing reports in one condition (one original plus three copies) and four independently authored reports in another; lexical overlap, document count, topic, length, and authority labels are balanced. Include an `unknown-origin` condition in which the correct action is to preserve uncertainty rather than force either independent or dependent.

Split by **origin family**, not just random document, to prevent near-duplicate leakage. Use temporal splits for C5. Keep a locked adversarial set generated after the codebook is frozen. Publish the generator and truth manifest even if source text cannot be redistributed.

### Ethically collectable real-world task packets

If a public packet is added, use a documented archival snapshot and license-cleared text, with no live scraping during the experiment. Candidate domains are:

1. **Public scientific evidence packets:** claims and abstracts from SciFact-like sources, with non-sensitive topics preferred.
2. **Public technical evaluation packets:** open software documentation, release notes, issue reports, and benchmarks; the decision is whether to run a **synthetic sandbox pilot**, never whether to deploy or purchase.
3. **Public policy/history packets:** dated official and independent documents where the task is to reconstruct what was stated and what remains uncertain, not to label a person or community.
4. **Synthetic longitudinal packets:** the preferred initial C5 setting, because update truth, permissions, outcomes, and harms can be fully controlled.

Do not use private enterprise records, YouTube cookies, provider tokens, personal contact data, medical records, employment records, or unredacted allegations. Alpha Solver and Signal Foundry may inform packet schemas only; neither supplies validation data.

## 7. AI conditions, baselines, and ablations

The headline comparison should be a fair resource-matched comparison, not a comparison with an intentionally weak model. Lock model weights or versioned local checkpoints, prompts, retrieval indexes, tokenizer, context limits, tool permissions, and random seeds. Prefer offline/open-weight configurations for the initial study. Do not run paid or live providers as part of this overnight design.

| ID | Condition | What it receives | Purpose |
| --- | --- | --- | --- |
| **A0** | No external context / answerability control | Question or claim only; explicit abstention allowed. | Negative control and prior-knowledge ceiling; never the main baseline for claims about retrieval. |
| **A1** | Ordinary retrieval plus citations | Query, fixed top-k lexical/dense retrieval, snippets, and citation rendering. | Strong simple workflow analogue. Records source count but not typed provenance or action policy. |
| **A2** | Strong retrieval/reranking RAG | Same access and budget as A1; current best reproducible local reranker within the locked protocol. | Tests whether generic retrieval/reranking explains any gain. Cite RAG precedent, e.g. [Lewis et al. (2020)](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html). |
| **A3** | Provenance-only | A1/A2 plus source/artifact/derivation receipts, but no separate support/authority/relevance/independence policy. | Tests whether lineage alone is sufficient. |
| **A4** | Claim-only | Atomic claims, evidence spans, and support/contradiction states, but no common-origin graph or cost-bounded router. | Tests claim decomposition without the full distinction contract. |
| **A5** | Minimal typed discrimination policy | A decision brief, provenance spine, claim/evidence graph, scoped authority/support/relevance/independence fields, explicit unknowns, common-origin grouping, bounded router, packet exclusions, and auditable stop receipt. | Proposed intervention. It should be the smallest implementation that can test H2–H5; it need not implement every conceptual component. |
| **A6** | Oracle diagnostic (not a headline comparator) | A5 with gold provenance/origin labels or gold evidence spans, only on synthetic data. | Estimates achievable ceiling and detects whether model errors arise in retrieval, grouping, or decision policy. Never report as a fair real-world system. |

### Required ablations of A5

- **A5−origin:** remove common-origin grouping while preserving token and context budget.
- **A5−typed:** collapse authority, support, relevance, and independence into one score.
- **A5−unknown:** force binary independent/dependent and remove unknown state.
- **A5−stopping:** fixed top-k or fixed context with no acquisition decision/stop receipt.
- **A5−exclusion:** hide material exclusions, failed captures, or unresolved gaps from the packet.
- **A5−provenance:** preserve labels in the packet but remove source/derivation reconstruction.
- **A5−override:** no human correction/route override (AI-only condition).
- **A5−memory:** summarize and reuse without origin-bound pointers.
- **A5−progressive:** show the whole graph at once rather than progressive disclosure (human study only).

Every ablation must be matched on model, retrieval calls, output-token ceiling, context-token ceiling, and total wall-clock budget. If A5 gets more text or a larger context, the study is measuring more context, not discrimination.

## 8. Human conditions and participant design

### Human interface conditions

The primary human study should be between participants to reduce learning and cross-condition contamination.

| ID | Condition | Interface |
| --- | --- | --- |
| **H0** | Ordinary research | Fixed packet or offline search-like browser, notes, and ordinary citations; no typed labels. |
| **H1** | Citation packet | Curated evidence cards with claim citations and source metadata, but no explicit common-origin/unknown/action fields. |
| **H2** | Typed progressive packet | Evidence cards plus provenance graph, support/contradiction spans, origin/unknown labels, exclusions, budget/stop receipt, and accept/override/defer/escalate controls. Progressive disclosure keeps the first view compact. |
| **H3** | Opaque-score control | A single “confidence/reliability” indicator with the same approximate information volume as H2 but without dimension labels. This tests whether any gain is simply confidence signaling. |

Do not tell participants that H2 is expected to be superior. Outcome adjudicators and data analysts should be blinded to condition labels where feasible. Measure whether participants can explain which evidence path led to their action; explanation quality is secondary, not a substitute for correctness.

### Participant strata

Recruit separate strata for:

- information or research professionals who routinely evaluate sources;
- technical knowledge workers who make bounded evidence-sensitive decisions;
- general adult users for terminology/comprehension only, if ethics review permits.

Record prior AI use, domain familiarity, information-literacy training, accessibility needs, and language proficiency as covariates—not as grounds to exclude people from the target population. Do not recruit people to make actual consequential decisions. Compensation, consent, withdrawal, and power dynamics must be specified in the ethics application and preregistration.

## 9. Study protocols

### Phase 0 — Scope and prior-art lock

Before data collection, run a protocol-led scoping review across information retrieval, evidence synthesis, provenance, claim verification, source credibility, sensemaking, mixed initiative, value of information, RAG/context engineering, memory, calibration, decision support, and human-AI reliance. Search both names and mechanisms, document inclusion/exclusion, deduplicate, and code whether each work already connects the proposed responsibilities. Report the search and screening flow using [PRISMA 2020](https://doi.org/10.1136/bmj.n71), without presenting PRISMA as evidence that the framework is novel.

**Gate:** if a simpler existing framework already covers the same responsibility with equal or better construct clarity, the paper should become a comparative synthesis or be stopped; do not relabel existing work as novelty.

### Phase 1 — Construct and terminology study (C0)

**Materials.** Build 120–180 short packets: crossed cases where authority and support diverge, repeated-but-dependent reports, relevant-but-low-authority items, high-attention/low-truth-risk items, unknown origin, missing expected evidence, and clear low-stakes controls. Include 20–30 terminology vignettes comparing the current name with serious alternatives.

**Procedure.**

1. Round 1: independent raters apply the draft codebook and give a short rationale.
2. Disagreement review: a separate adjudication panel labels disagreements without seeing the original rater identity or proposed intervention.
3. Codebook revision: revise definitions only in a documented pilot, then freeze them.
4. Round 2: fresh raters or hold-out items apply the frozen codebook.
5. Terminology test: ask readers to restate the thesis, identify what the layer does not mean, and select likely governance risks after reading the definition.

**Primary outcomes.** Agreement and hold-out transfer for the core dimensions; restatement accuracy and material misinterpretation rate for the name. Analyze dimensions separately; an aggregate agreement score can hide one failed construct.

**Gate.** Retain a construct only if it has an operational rubric, useful agreement on hold-out cases, and a demonstrated downstream decision or correction role. Otherwise merge, narrow, or remove it.

### Phase 2 — Provenance-rich benchmark (C1–C5)

Combine license-cleared public tasks with the synthetic graph generator. Annotate a subset of public packets for origin relation, temporal status, authority scope, support, contradiction, and gaps. Use at least two independent annotators per item and a third adjudicator for disagreement. Make origin-family and temporal hold-outs mandatory.

Run deterministic validators before model evaluation:

- every derived item points to an origin or carries `unknown`;
- no gold answer appears in metadata, filenames, prompts, or retrieval ranking features;
- copies/paraphrases are not split across train and test by document only;
- action costs sum to the declared budget;
- unauthorized actions have an explicit gold violation state;
- stale versions have a known supersession relation;
- all public text has a license/retention record and redaction log.

**Gate:** freeze a versioned dataset card, manifests, annotation guide, split hash, contamination report, and harm review before the definitive AI comparison.

### Phase 3 — Offline AI comparison (A0–A6)

For each task instance, run all eligible systems on the same corpus snapshot, random seed set, model budget, context budget, retrieval cap, and wall-clock cap. Save raw retrieval results, prompts, model outputs, route decisions, provenance receipts, cost/latency telemetry, and errors. Use at least five independent seeds for stochastic systems; deterministic systems still receive repeated runs if hardware or parallelism can introduce variation.

The primary analysis is task-level, not a cherry-picked best prompt. A5 is compared with A2 and A3/A4 for mechanism attribution. A6 is diagnostic only. Report per-class and pooled results with item and seed uncertainty.

### Phase 4 — Human correction and decision-support experiment (H0–H3)

Randomize participants to conditions. Give a tutorial using practice items that do not overlap with test origins. Each participant receives 16–24 test tasks balanced across C1–C4 and C7, with seeded errors and correct outputs mixed. The system’s output is frozen before participant review.

Participants must make one of `accept`, `correct`, `defer`, `hold`, `ask`, or `escalate`, cite the evidence path they relied on, and state confidence. A separate blinded panel scores the decision and evidence path. Record time from first packet view, inspect/expand events, overrides, and reasons. Use progressive disclosure only in H2; do not give H2 extra raw evidence.

**Primary endpoint.** Blinded evidence-grounded decision success and seeded-error correction rate. **Safety endpoints.** inappropriate acceptance of unsupported high-severity output and inappropriate refusal/defer on supported low-risk output. **Process endpoints.** correction localization time, review minutes, workload, and provenance reconstruction.

### Phase 5 — Optional bounded longitudinal pilot (C5)

Only proceed if Phases 1–4 show construct reliability, a meaningful benefit against strong baselines, no critical harm signal, and an approved governance plan. Use reversible, non-production tasks with synthetic or public evidence. Predefine outcomes before the decision and preserve the historical packet/policy version. Compare predicted versus observed outcomes and propose updates; never silently rewrite past evidence or use one owner’s disposition as universal truth.

The pilot is not required for a first paper. If performed, it must be separately approved and reported as a transfer/feasibility study, not proof of enterprise readiness.

### Phase 6 — Adversarial and cross-domain replication

After a positive primary study, test a second domain and adversarial packets: coordinated copying, source impersonation, provenance laundering through summaries, prompt injection in retrieved text, memory poisoning, selective silence, stale updates, and high-cost rare evidence. Independent investigators should build at least part of the replication corpus. A positive result only on synthetic copy graphs is not sufficient for a general thesis.

## 10. Metrics and scoring plan

### AI and artifact metrics

| Outcome family | Measures | Interpretation guardrail |
| --- | --- | --- |
| Verdict/answer | Accuracy, macro-F1, balanced accuracy where labels are imbalanced, exact/partial answer score. | Report per class; do not hide `insufficient` and `contested` under binary accuracy. |
| Evidence quality | Evidence-span precision/recall/F1, supported-claim rate, evidence sufficiency, contradiction detection, citation entailment, material-exclusion error. | A citation counts only if it supports the atomic claim under the rubric. |
| Dependence | Origin relation precision/recall/F1, false-corroboration rate, independent-evidence recall, unknown-retention rate. | Penalize both over-discounting and false independence. |
| Selection | Useful-evidence recall at fixed context budget, irrelevant-context rate, gap recall, harmful inclusion and harmful omission. | More context is not a success criterion. |
| Routing | Appropriate action rate, utility regret, acquire/stop/hold/refuse precision, high-severity miss rate, unauthorized-action rate. | The utility matrix and severity weights are preregistered. |
| Calibration | Brier score, reliability diagram, expected calibration error, selective risk-coverage, abstention utility. | Report calibration separately from accuracy and source authority. |
| Auditability | Provenance node/edge completeness, reconstruction accuracy, time to locate support or exclusion, reproducible replay rate. | Receipts must help a reviewer, not merely exist. |
| Efficiency | Wall-clock latency, model tokens, retrieval calls, context tokens, CPU/GPU time, reviewer minutes, monetary cost if any, budget overrun. | Compare quality per resource and raw resource use. |
| Robustness | Performance under copy/paraphrase, stale version, contradiction, unknown-origin, source-impersonation, prompt injection, and context-position perturbations. | Avoid testing only cases that encode the proposed heuristic. |

### Human metrics

- **Blinded decision quality:** proportion of decisions meeting the conjunctive evidence-grounded rubric.
- **Seeded-error correction:** incorrect system outputs corrected to the gold action/claim state.
- **Appropriate reliance:** accept correct outputs, correct incorrect outputs, defer on insufficient evidence, and avoid unnecessary override.
- **Over- and under-discrimination:** inappropriate refusal/deferral on supported evidence versus unsupported completion/acceptance.
- **Correction localization:** elapsed time and number of interactions to identify the wrong relation, source, span, or route.
- **Evidence-path fidelity:** whether the participant’s cited path actually supports the decision.
- **Workload and burden:** review minutes, interactions, inspect depth, and validated workload score; report completion and dropout.
- **Comprehension:** ability to restate the difference between authority, support, independence, relevance, and action priority.

### Decision utility

Use an explicit utility table per task class. For an item (i), a preregistered score can be:

`U_i = B_i − H_i − C_search,i − C_review,i − C_latency,i`

where (B_i) is the benefit of the correct bounded action, (H_i) is the severity-weighted harm of an unsupported or unsafe action, and the three costs are measured telemetry. Publish each component, not only the composite. Run sensitivity analyses across plausible harm weights and report whether the sign of the condition effect changes. If utility weights cannot be defended, report evidence quality and cost without a utility claim.

## 11. Sample size and power considerations

Exact sample sizes should be finalized from pilot variance and item difficulty by simulation, not selected after results. Use [Faul et al. (2009)](https://doi.org/10.3758/BRM.41.4.1149) or an auditable simulation script for planning, and report the assumed effect, intraclass correlations, attrition, seed variance, and multiplicity. A pilot estimates feasibility and variance; it should not be used as a disguised efficacy test. Reporting should follow current randomized-trial guidance such as [CONSORT 2025](https://doi.org/10.1001/jama.2025.4347), with the design-specific extension documented.

### Phase 1 construct/reliability target

- **Raters:** target 60–80 raters across expert and intended-user strata for the definitive construct study; a 15–20-rater pilot is for codebook repair only.
- **Items:** 150–200 packets, with at least 30% crossed/adversarial cases and 20% low-stakes controls. Each item receives at least two independent labels; 25–30% is double-coded across all raters for overlap, and all disagreements go to adjudication.
- **Planning criterion:** simulation should show 80% power to distinguish the preregistered agreement floor from chance/near-chance for each core construct while retaining uncertainty intervals. Do not infer construct validity from a single omnibus alpha.

### Phase 3 AI benchmark target

- **Items:** initial target 400–600 locked items per major class (C1–C5), with at least 100 independent adversarial/unknown-origin items per C2/C3 class and 100 low-dependence controls. If annotation capacity is lower, reduce claims and publish a benchmark pilot rather than underpowered superiority claims.
- **Runs:** all systems on every item; at least five seeds for stochastic systems; report item-clustered and seed variability.
- **Power:** simulate paired/hierarchical outcomes under the minimum meaningful effects above, with family-wise correction across the primary endpoints. The design should target 80–90% power for the smallest claimed effect, not for an optimistic effect inferred from the pilot.
- **Split discipline:** no origin family crosses train/development/test; no prompt/model tuning on the locked test set.

### Phase 4 human study target

- **Participants:** target 240 participants (80 per H0/H1/H2) for the primary study, with H3 added only if it is central to the claim; a smaller 60–90-person pilot estimates task time, dropout, item difficulty, and interface burden.
- **Tasks:** 16–24 tasks per participant, balanced over C1–C4 and C7, with no participant seeing matched origin variants in more than one condition.
- **Planning criterion:** simulation of a mixed-effects model should provide 80% power for a between-condition standardized effect around 0.30–0.35 on the primary decision-quality endpoint and for the preregistered safety non-inferiority margin, after participant and item random effects and attrition. If the design cannot support subgroup claims, do not make them; treat subgroup estimates as exploratory.
- **Attrition and exclusions:** add a preregistered 10–15% attrition allowance; do not remove slow, low-confidence, or disagreeing participants unless exclusions were specified before unblinding.

### Phase 5 pilot and replication

Do not power a field pilot to prove general effectiveness from a single organization. Use it to estimate adoption, retention, workarounds, missing outcomes, privacy burden, and transfer parameters. A second-domain replication should be powered to the same minimum effect or explicitly reported as an uncertainty/feasibility replication.

## 12. Preregistration and statistical analysis

Register the protocol on a time-stamped public registry such as [OSF Registrations](https://help.osf.io/article/158-register-your-project) before final test-set access, model evaluation, or participant recruitment. If the study becomes a randomized human experiment, include objectives, allocation, outcomes, sample-size rationale, harms, and deviations in a CONSORT-compatible plan; if it is a pilot, use the [CONSORT pilot/feasibility extension](https://doi.org/10.1186/1745-6215-17-1-1). For a human protocol, use a SPIRIT-compatible checklist ([Chan et al., 2013](https://doi.org/10.1136/bmj.e7586)).

The preregistration must contain:

1. one primary question and unit of analysis per task class;
2. exact task lists, source snapshot, split hashes, licenses, provenance generator seed, and contamination checks;
3. frozen model/checkpoint, tokenizer, prompt, retrieval index, reranker, context/token caps, tool permissions, and seed policy;
4. all comparator and ablation conditions, including negative controls and oracle diagnostics;
5. primary and secondary endpoints, formulas, severity/utility weights, calibration bins, and minimum meaningful effects;
6. randomization, counterbalancing, allocation concealment where possible, blinding, practice items, and participant exclusion rules;
7. missing-data and timeout handling, run-failure handling, and a policy for unavailable evidence;
8. model formula, random-effects structure, contrast coding, multiplicity correction, robustness checks, and equivalence/non-inferiority criteria;
9. subgroup/fairness slices and harm-monitoring thresholds;
10. a negative-result and early-stop policy;
11. versioned deviations log and a distinction between confirmatory and exploratory analyses.

### Analysis model

For binary task success, use a mixed-effects logistic model with condition, task class, dependence, stakes, and preregistered interactions as fixed effects, and participant/item/origin-family random intercepts where estimable. For continuous time, utility, or workload, use an appropriate transformed or robust mixed model and report medians/quantiles when distributions are skewed. Do not use a maximal random-effects structure that fails to converge without documenting the prespecified fallback. The rationale for separating item and participant variation follows the repeated-measures concern discussed by [Barr et al. (2013)](https://doi.org/10.1016/j.jml.2012.11.001).

Report absolute effects, standardized effects where useful, 95% confidence intervals, uncertainty from seeds and items, and adjusted p-values only as secondary summaries. For a null claim, use an equivalence or non-inferiority test against a preregistered margin; “not significant” is not evidence of no meaningful effect.

Use intention-to-treat for human assignment and all valid system runs for the primary analysis. A per-protocol analysis can exclude protocol violations only as secondary and must show the excluded records. Missing or failed retrieval is an observed system state, not negative evidence about the claim; record it separately.

## 13. Inter-rater reliability and adjudication

Use reliability as evidence about a construct’s operational usability, not as proof of truth.

- For nominal labels with two raters, report Cohen’s kappa ([Cohen, 1960](https://doi.org/10.1177/001316446002000104)) alongside raw agreement and prevalence tables.
- For more than two raters or multi-label annotations, report a prespecified multi-rater statistic (e.g., Fleiss’ kappa or Krippendorff’s alpha) plus per-label agreement and disagreement matrices. Do not choose the statistic after seeing prevalence.
- For ordinal authority/relevance/action ratings, use weighted agreement and an intraclass correlation only when the scale and random-effects interpretation justify it.
- Use confidence intervals by bootstrap over items and, where needed, raters. Report how many items were adjudicated and the exact adjudication rule.
- Keep `unknown`, `insufficient`, and `contested` as valid labels. Do not force a majority label when the evidence is genuinely unresolved.
- The adjudicator must see the packet and codebook, not the system condition or hypothesis. If adjudication changes a gold label, preserve the pre-adjudication label and reason.
- Use a hold-out set for the final codebook. Do not repeatedly tune the codebook against the definitive test set.

Useful agreement is a gate, not a cosmetic statistic. If core dimensions cannot be distinguished beyond a prespecified floor on hold-out cases, remove or merge them before testing the full intervention.

## 14. Data-quality, provenance, and reproducibility checks

### Dataset checks

- Verify licenses, source dates, archive hashes, redactions, and permitted redistribution.
- Hash every source/artifact/version and maintain a manifest of transformations.
- Validate that every derived item has a parent edge or an explicit unknown state; use the [W3C PROV-O recommendation](https://www.w3.org/TR/prov-o/) as a vocabulary reference, not as a correctness guarantee.
- Test split leakage by exact match, near-duplicate similarity, citation/URL overlap, origin-family overlap, and temporal contamination.
- Audit synthetic generators for shortcuts: source IDs, punctuation, length, or filenames must not reveal origin or label.
- Sample at least 10% of benchmark items for independent manual audit and 100% of adversarial items.

### System checks

- Run a no-op/replay test to verify that immutable raw evidence is not rewritten by summarization or memory updates.
- Verify that unauthorized actions are blocked and recorded, not silently retried.
- Verify that failed captures are recorded as failures, not interpreted as source absence.
- Verify that `unknown` dependence survives every transformation and packet export.
- Replay the same seed/configuration and compare outputs, routes, costs, and receipts.
- Perturb context order and duplicate one source to test whether the system counts repeated text as evidence.
- Check that an excluded document’s content does not appear in the generated answer through hidden memory or prompt carryover.
- Maintain a run ledger with model, prompt, retrieval index, hardware, timestamp, seed, token counts, tool calls, and failures.

### Human-study checks

- Include comprehension checks and practice items, but do not use them to remove participants after seeing condition effects unless preregistered.
- Use attention checks that are task-relevant and do not reward blind acceptance of the system.
- Record screen-reader/keyboard/accessibility barriers and offer an equivalent accessible interface.
- Inspect timing distributions for idle tabs and technical outages; preserve rather than silently trim records.
- Separate participant identifiers from content and consent data; maintain a deletion/retention schedule.

## 15. Fairness, privacy, security, and harm review

Risk review should use the [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) and, for human participants, the principles of the [Belmont Report](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html). These are governance references, not evidence that the framework is safe.

### Fairness and representation

- Define the population and source ecology before sampling. Include, where the task genuinely calls for it, regional, linguistic, topical, source-type, and institutional slices; do not add protected-class labels merely to create a fairness table.
- Evaluate equalized error patterns only when a meaningful gold standard and group definition exist. Otherwise report coverage, omission, source-diversity, burden, and error slices with uncertainty.
- Do not infer a person’s protected attribute from text. If public claims contain protected-class or vulnerable-group content, redact or use only aggregated non-identifying labels.
- Audit authority priors for institutional and geographic exclusion. An “official” source may be authoritative for a narrow official statement and not for lived experience or comparative impact.
- Treat a large aggregate improvement as insufficient if it increases false rejection, undercoverage, or review burden for a slice. Predefine a mitigation or stop threshold.
- Report language and accessibility limits. A benchmark that is English-only or screen-reader-hostile cannot support a universal claim.

### Privacy and authorization

- Use public, license-cleared, synthetic, or explicitly consented data only. Public does not mean unrestricted for every use; check license, terms, and ethical expectations.
- Do not collect or expose personal contact data, credentials, cookies, tokens, private prompts, internal documents, health information, employment records, or unredacted allegations.
- Store content separately from provenance pointers where possible; minimize raw retention; document retention, deletion, redaction, and controlled-access rules.
- Treat technical accessibility as distinct from authorization. An experiment that can fetch a page must still check whether acquisition, transformation, retention, and disclosure are permitted.
- If any human data beyond minimal study logs is proposed, obtain the appropriate institutional ethics determination before recruitment. Do not treat a registry entry as ethics approval.

### Security and harm threat model

Test and monitor coordinated copying, source impersonation, provenance laundering, prompt injection in retrieved evidence, memory poisoning, selective silence, stale supersession, and overconfident unsupported completion. Do not publish a benchmark that materially amplifies harmful claims or exposes attack strings without a release review.

**Immediate stop/quarantine events:** exposure of private or secret data; unauthorized live retrieval or action; a system output that recommends a real consequential action; discriminatory or defamatory labeling of a person/group; loss of raw evidence/provenance needed to audit; or an injection/memory exploit that propagates into subsequent tasks. Preserve the audit receipt, stop further runs, remove the affected artifact from the analysis set, notify the responsible ethics/security owner, and do not resume until the root cause and containment are documented.

## 16. Failure, stop, and narrowing criteria

These are proposed decision rules to preregister, not findings.

| Observed result | Required interpretation/action |
| --- | --- |
| Core constructs fail the hold-out agreement floor or readers cannot restate the distinction. | Stop efficacy claims; revise/merge constructs. If “discrimination layer” remains materially misunderstood after definition, rename to a less ambiguous term while preserving or separately testing the mechanism. |
| A5 is not better than A2 under matched resources on the primary endpoint, and the equivalence interval excludes the meaningful effect. | Do not claim added value of the full layer for that task class. Examine whether A3/A4 or a simpler checklist is sufficient. |
| A5 improves evidence metrics but not blinded decision utility or correction. | Narrow the claim to evidence organization/auditability; do not claim better decisions. |
| A5’s gains disappear when A2 receives equal tokens/context and strong reranking. | Attribute the gain to retrieval/context budget or implementation quality, not a distinct discrimination layer. |
| A5−origin matches A5 on dependence tasks. | Drop common-origin analysis as a claimed necessary mechanism, or narrow it to specific dependence patterns. |
| Origin-aware grouping reduces false corroboration but suppresses valid independent evidence more than it helps. | Retire or redesign common-origin discounting; require calibrated uncertainty and human appeal rather than automatic discounting. |
| A5 increases appropriate abstention but also materially increases inappropriate refusal or reviewer burden. | Treat over-discrimination as a failure; narrow to high-stakes/high-dependence tasks or redesign the router. |
| Human users show more automation bias, slower correction, or lower evidence-path fidelity under H2. | Do not claim human benefit. Consider a machine-audit or expert-only use case, progressive disclosure, or abandonment. |
| Feedback/memory improves aggregate calibration but worsens subgroup coverage, diversity, or stale-memory safety. | Block policy update; retain historical versions; narrow or retire outcome-learning claims. |
| Results occur only on synthetic graphs or one dataset. | Report a benchmark/mechanism result only; no open-world or general-domain claim. Require independent public/second-domain replication. |
| A simpler prior framework covers the same responsibilities with clearer constructs and equal outcomes. | Recast as a comparative synthesis or subsume the framework; do not defend novelty by renaming components. |
| Any critical privacy, authorization, security, or harmful reliance event occurs. | Stop and quarantine as above; no efficacy interpretation from affected runs. |

### Aggregate success rule for a narrow paper

A first empirical paper may claim a bounded benefit only if, on at least two non-identical task classes (one with known dependence and one with contradiction/missingness):

1. the frozen codebook reaches the reliability floor;
2. A5 beats A2 on the preregistered primary endpoint by at least the minimum meaningful effect under matched resources;
3. no safety endpoint crosses its non-inferiority margin;
4. the result persists across origin-family hold-out and seed uncertainty;
5. at least one human or blinded audit measure shows improved correction/auditability, if a human claim is made; and
6. no critical harm, privacy, authorization, or subgroup failure remains unexplained.

Failure to meet this rule does not make the work worthless. It determines the narrower paper: construct paper, benchmark paper, provenance mechanism paper, auditability study, or negative result.

## 17. Phased roadmap and evidence gates

| Phase | Work | Exit evidence | Permitted claim after exit |
| --- | --- | --- | --- |
| P0 | Claim and prior-art protocol; exact source/terminology reconciliation. | Search protocol, screened corpus, claim map, updated novelty boundary. | “This is a bounded synthesis/research question.” |
| P1 | C0 construct/terminology study. | Frozen definitions, reliability, disagreement analysis, reader restatement, rename decision. | “These constructs are/are not operationally distinguishable in this sample.” |
| P2 | Provenance-rich C1–C5 benchmark. | Dataset card, graph truth, licenses, leakage audit, annotation agreement, adversarial hold-out. | “This benchmark measures the named task and includes known dependence conditions.” |
| P3 | A0–A6 offline comparison and ablations. | Reproducible run ledger, matched-resource analysis, uncertainty, error taxonomy, no critical harm. | “The tested policy did/did not improve the named computational tasks under these conditions.” |
| P4 | H0–H3 controlled human correction study. | Registered allocation, blinded adjudication, decision/correction/workload results, accessibility and harm review. | “The tested interface did/did not change human correction/reliance on these tasks.” |
| P5 | Optional bounded longitudinal pilot. | Governance approval, outcome definitions, versioned feedback, drift/privacy/workaround audit. | “Feasibility/transfer evidence in one bounded setting”; not enterprise readiness. |
| P6 | Independent second-domain/adversarial replication. | Replication protocol, cross-domain results, residual risks, negative findings. | Only now consider a carefully scoped cross-domain claim. |

The phases are gates, not a promise to execute all of them. A negative P1 or P3 should stop escalation. The shortest credible paper may be a construct/benchmark paper; a decision-support claim requires P4; a field or enterprise claim requires P5–P6 and separate authorization.

## 18. What the eventual paper may and may not say

| Evidence available | Defensible wording | Prohibited wording |
| --- | --- | --- |
| Thought piece plus literature | “We propose an integrative framework and an evaluation agenda.” | “The layer works,” “novel architecture,” or “validated.” |
| P1 only | “Raters distinguished these operational definitions under these conditions.” | “The distinctions improve decisions.” |
| P2 only | “We release a provenance-controlled benchmark for dependence/claim/routing tasks.” | “Real-world sources are independent,” “open-world truth is solved.” |
| P3 | “The tested policy improved/failed on named tasks under matched offline resources.” | “AI systems generally benefit,” “enterprise-ready.” |
| P4 | “The tested interface changed human correction/reliance in this population and task set.” | “Human oversight is solved,” “safer in deployment.” |
| P5 | “A bounded pilot measured feasibility and these prospective outcomes.” | “The product or framework is validated,” “causal business value.” |
| P6 | “The effect replicated/failed across these predeclared domains and threats.” | “Universal discrimination layer,” “complete solution.” |

## 19. Primary and authoritative sources

The following are the sources used to ground methodological or task-design choices. They are not evidence that the proposed layer works.

### Evidence, retrieval, provenance, and context

- Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). “FEVER: a Large-scale Dataset for Fact Extraction and VERification.” [ACL Anthology; DOI 10.18653/v1/N18-1074](https://doi.org/10.18653/v1/N18-1074).
- Wadden, D., et al. (2020). “Fact or Fiction: Verifying Scientific Claims.” [ACL Anthology; DOI 10.18653/v1/2020.emnlp-main.609](https://doi.org/10.18653/v1/2020.emnlp-main.609).
- Schlichtkrull, M., Guo, Z., & Vlachos, A. (2023). “AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web.” [arXiv:2305.13117](https://arxiv.org/abs/2305.13117).
- Jiang, Y., et al. (2020). “HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification.” [ACL Findings; DOI 10.18653/v1/2020.findings-emnlp.309](https://doi.org/10.18653/v1/2020.findings-emnlp.309).
- Kwiatkowski, T., et al. (2019). “Natural Questions: A Benchmark for Question Answering Research.” [TACL; DOI 10.1162/tacl_a_00276](https://doi.org/10.1162/tacl_a_00276).
- Thakur, N., et al. (2021). “BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models.” [NeurIPS Datasets and Benchmarks](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/65b9eea6e1cc6bb9f0cd2a47751a186f-Abstract-round2.html).
- Lewis, P., et al. (2020). “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.” [NeurIPS 2020](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
- Liu, N. F., et al. (2024). “Lost in the Middle: How Language Models Use Long Contexts.” [TACL; DOI 10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638).
- Lebo, T., Sahoo, S., & McGuinness, D. (eds.) (2013). “PROV-O: The PROV Ontology.” [W3C Recommendation](https://www.w3.org/TR/prov-o/).
- Cochrane. “Cochrane Handbook for Systematic Reviews of Interventions,” current handbook, especially Chapter 4 on study/report identity and synthesis. [Official handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04).

### Resource-bounded choice and human-AI interaction

- Howard, R. A. (1966). “Information Value Theory.” [IEEE; DOI 10.1109/TSSC.1966.300074](https://doi.org/10.1109/TSSC.1966.300074).
- Pirolli, P., & Card, S. K. (1999). “Information Foraging.” [Psychological Review; DOI 10.1037/0033-295X.106.4.643](https://doi.org/10.1037/0033-295X.106.4.643).
- Russell, S., & Wefald, E. (1991). “Principles of Metareasoning.” [Artificial Intelligence; DOI 10.1016/0004-3702(91)90015-C](https://doi.org/10.1016/0004-3702(91)90015-C).
- Horvitz, E. (1999). “Principles of Mixed-Initiative User Interfaces.” [Microsoft Research](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/).
- Amershi, S., et al. (2019). “Guidelines for Human-AI Interaction.” [CHI; DOI 10.1145/3290605.3300233](https://doi.org/10.1145/3290605.3300233).

### Calibration, agreement, and statistical design

- Brier, G. W. (1950). “Verification of Forecasts Expressed in Terms of Probability.” [Monthly Weather Review; DOI 10.1175/1520-0493(1950)078%3C0001:VFOAAN%3E2.0.CO;2](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VFOAAN%3E2.0.CO;2).
- Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). “On Calibration of Modern Neural Networks.” [PMLR](https://proceedings.mlr.press/v70/guo17a.html).
- Cohen, J. (1960). “A Coefficient of Agreement for Nominal Scales.” [Educational and Psychological Measurement; DOI 10.1177/001316446002000104](https://doi.org/10.1177/001316446002000104).
- Artstein, R., & Poesio, M. (2008). “Inter-Coder Agreement for Computational Linguistics.” [Computational Linguistics; DOI 10.1007/s10579-007-9076-4](https://doi.org/10.1007/s10579-007-9076-4).
- Faul, F., Erdfelder, E., Buchner, A., & Lang, A.-G. (2009). “Statistical Power Analyses Using G*Power 3.1.” [Behavior Research Methods; DOI 10.3758/BRM.41.4.1149](https://doi.org/10.3758/BRM.41.4.1149).
- Barr, D. J., Levy, R., Scheepers, C., & Tily, H. J. (2013). “Random Effects Structure for Confirmatory Hypothesis Testing: Keep It Maximal.” [Journal of Memory and Language; DOI 10.1016/j.jml.2012.11.001](https://doi.org/10.1016/j.jml.2012.11.001).
- Schulz, K. F., Altman, D. G., & Moher, D. (2010). “CONSORT 2010 Statement.” [BMJ; DOI 10.1136/bmj.c869](https://doi.org/10.1136/bmj.c869). For the current update, see [CONSORT 2025; DOI 10.1001/jama.2025.4347](https://doi.org/10.1001/jama.2025.4347).
- Chan, A.-W., et al. (2013). “SPIRIT 2013 Statement: Defining Standard Protocol Items for Clinical Trials.” [BMJ; DOI 10.1136/bmj.e7586](https://doi.org/10.1136/bmj.e7586).

### Governance and ethics

- Tabassi, E. (2023). “Artificial Intelligence Risk Management Framework (AI RMF 1.0).” [NIST AI 100-1; DOI 10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). “The Belmont Report.” [U.S. HHS official text](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html).
- Page, M. J., et al. (2021). “The PRISMA 2020 Statement.” [BMJ; DOI 10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71).

## Closing design judgment

The strongest credible empirical program is not a grand end-to-end demonstration. It is a sequence that can lose: first show that the distinctions are operationally separable; then build a provenance-controlled benchmark; then compare a minimal typed policy with strong simple retrieval, citation, claim, and provenance baselines under matched resources; then test whether people correct errors better; and only then consider bounded outcomes and replication. If the extra distinctions do not improve evidence-grounded decisions or correction enough to justify their cost—or if they create over-refusal, unequal coverage, privacy exposure, or governance harm—the appropriate result is to narrow, rename, subsume, or retire the thesis for that task class.
