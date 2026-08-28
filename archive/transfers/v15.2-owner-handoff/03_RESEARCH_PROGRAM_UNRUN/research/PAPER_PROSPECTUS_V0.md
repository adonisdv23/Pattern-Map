# Paper prospectus v0.4: research program and first study

**Status:** loop-3-revised research prospectus; no study has been run  
**Prepared:** 2026-08-18  
**Evidence boundary:** this document turns the v14 thought piece, three first-pass Luna Max research memos, and adversarial novelty/feasibility review into a falsifiable program. It is not a manuscript submission, preregistration, novelty opinion, ethics approval, or empirical result.

## Answer first

The most credible first paper is not an evaluation of a universal “discrimination layer,” a full router, or human correction. It is a single offline behavioral study asking whether a supplied origin-relation-metadata condition produces less false corroboration than an explicit origin-counting-rule condition on the same frozen model, without suppressing recall of stipulated supporting origins. The observable contribution is a condition effect, not evidence about the model’s internal reasoning.

The wider program may later evaluate a **candidate compact, profiled evidence-selection and action policy** under dependence, contradiction, missingness, or costly acquisition. “Compact” is aspirational until ablations establish which fields are necessary; “minimal” is not yet supported. The first study should be allowed to lose. A null, harmful, shortcut-driven, or unstable result narrows or retires the origin-cue mechanism without pretending to falsify every other part of the conceptual map.

## Provisional title set

Preferred first-study title:

> **Oracle Origin-Relation Metadata in One Frozen Model: A Controlled False-Corroboration Benchmark**

Program-level titles to test with readers only after the first mechanism result:

1. **Evidence Before Generation: A Typed Evidence-Selection and Action Policy**
2. **From Retrieval to Disposition: Provenance-Aware Context Judgment Under Cost**
3. **The Evidence-Selection and Judgment Layer: A Research Agenda for Inspectable Context Policy**

Keep **Pattern Recognition / The Discrimination Layer** as the historical thought-piece title until a terminology study is complete. Do not make it the scientific title by default. “Discrimination” collides with social/legal discrimination and established classifier/discriminator meanings; preserving the mechanism does not require preserving the label.

## Narrow contribution claim

The immediate paper may propose and evaluate:

> On fictional evidence bundles with stipulated provenance graphs, whether an explicit `dependent` / `independent_as_stipulated` / `unknown` origin-relation field changes a frozen model’s origin-count output relative to the same evidence and origin-counting rule without that field.

This is a **representation and cue-use claim**. F2 is an oracle origin-relation metadata condition, not an evaluation of automated provenance discovery, real-world independence, truth, retrieval, human correction, or the full framework.

The later program may evaluate a domain-profiled action-policy contract that preserves source/artifact provenance and unknown dependence; separates claim support, scoped authority, relevance, and action consequence; and routes acquisition, clarification, provisional use, abstention, or escalation under declared budgets before generation or action. That remains an **integration, operationalization, and evaluation claim**, not a claim to have invented:

- information foraging or relevance feedback;
- value of information, metareasoning, or active acquisition;
- provenance, claim/evidence graphs, scientific argumentation, or common-origin analysis;
- retrieval-augmented generation, reranking, long-context use, or citation generation;
- mixed initiative, cognitive forcing, human review, calibration, organizational memory, or learning.

Closest constraining precedents include [PROV-O](https://www.w3.org/TR/prov-o/), [claim provenance](https://aclanthology.org/2020.acl-main.406/), [ProVe](https://doi.org/10.3233/SW-233467), [HydraRAG](https://aclanthology.org/2025.emnlp-main.730/), [CONFACT](https://www.ijcai.org/proceedings/2025/1073), [FaithfulRAG](https://aclanthology.org/2025.acl-long.1062/), [CLUE](https://aclanthology.org/2026.acl-long.2110/), [Xia's matched evidence-utilization protocol](https://arxiv.org/abs/2606.06758), [Nematov et al.'s source-attribution analysis](https://doi.org/10.48550/arXiv.2507.04480), [BERGEN](https://aclanthology.org/2024.findings-emnlp.449/), [Pendo](https://doi.org/10.1016/j.dss.2014.04.005), and [PaperTrail](https://doi.org/10.1145/3772318.3791101). Multiple integrated systems now cover overlapping parts of the wider responsibility. The immediate scientific burden is only to show that the supplied relation field changes origin accounting beyond an explicit rule under exact F1/F2 token parity and a frozen model.

## Immediate first study

The study design now lives in [Oracle Origin-Relation Metadata in One Frozen Model](ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md); the [Loop 3 consolidated operationalization specification](overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md) fixes the JSON/JSONL schemas, generator grammar, prompts, parser, metrics, power simulation, QA, and release manifest. The plan uses 80 development bundles, 40 feasibility-only pilot bundles, 300 novel primary bundles balanced across one-origin repetition, multiple-origin convergence, unknown origin, and conflict, plus 60 locked stress bundles. It compares citation-only, rule-only, and stipulated-relation conditions while holding the evidence text, output contract, model, decoding, and input-token budget fixed.

The sole primary endpoint is the all-assigned, conservative-risk-coded paired false-corroboration contrast for typed cue versus rule only. Recall of stipulated supporting origins is the fixed-denominator safety/non-inferiority endpoint. Human correction, retrieval, routing, memory, terminology, authority, field outcomes, and decision utility are explicitly out of scope. A positive result earns a bounded condition-effect claim for the tested frozen model; it does not validate the layer.

## Proposed conceptual object

For the wider program, the proposed working unit is a versioned **evidence cue plus selection-and-action audit record**. This is a design choice to test, not a universal minimum; a document, claim, observation, or argument may be the better unit for another task.

| Field | Minimum record | Must not mean |
| --- | --- | --- |
| Decision brief | Question, scope, audience, stakes, allowed operations, time/token/money/review budget | That the brief or expected baseline is correct |
| Claim | Atomic proposition with scope and time window | A paragraph-level answer or truth |
| Evidence span | Exact passage, observation, measurement, or artifact location with context on demand | Citation presence or document relevance |
| Relation | Supports, contradicts, qualifies, contextualizes, omits, or derives from | A generic unlabeled edge |
| Provenance | Source, artifact, version, actor, time, transformation, possible common origin | Correctness or authorization |
| Dependence | Independent, dependent with type/scope, or unknown | Different URL, wording, publisher, or community |
| Typed assessments | Scoped authority, claim support, relevance, recurrence, attention priority, uncertainty type, action consequence | One universal trust or quality score |
| Why now | Gap, contradiction, origin conflict, temporal change, decision sensitivity, or owner request | Persuasive rationale text |
| Next action | Inspect, compare, acquire, ask, use provisionally, answer, hold, defer, refuse, or escalate | A factual conclusion or automatic command |
| Cost and stop receipt | Expected/realized latency, tokens, money, risk, review burden, stop reason | Exact value of information unless its assumptions are defensible |
| Human disposition | Accept, reject, request more work, defer, hold, override, or escalate; actor and authority | External truth or permanent preference |
| Outcome link | Predefined later observation, horizon, exposure, confounders, policy version | Retroactive rewriting of evidence or proof of causality |

Past packets, raw captures, and graph states remain immutable. Later evidence may append a correction, supersession, disputed edge, new disposition, or proposed policy update; it must not silently rewrite the historical input.

## Primary research questions

1. **Construct boundary:** Can representative raters distinguish authority, support, provenance, independence, recurrence, relevance, attention, enrichment value, action priority, disposition, and outcome on held-out cases?
2. **Common origin:** Does explicit origin/dependence handling reduce false corroboration without materially suppressing genuine independent convergence?
3. **Claim support:** Do atomic claim/evidence relations improve supported-claim and contradiction/insufficiency detection over document relevance and citation presence?
4. **Routing:** Under fixed budgets, does an explicit acquire/compare/ask/answer/hold/refuse policy improve net decision utility or stopping regret?
5. **Human correction:** Does a progressive evidence cue and route receipt help people locate and correct seeded errors, or does it create clutter, delay, and automation bias?
6. **Boundary moderation:** Are effects concentrated in dependent, contradictory, temporally changing, or consequential tasks and absent or negative in simple controls?
7. **Memory:** Does origin-bound, versioned memory reduce stale reuse and provenance laundering across time?
8. **Terminology:** Do representative readers infer the intended technical function from “discrimination layer,” or is another name materially clearer and safer?

## Main hypotheses and falsifiers

| Hypothesis | Primary measure | A result that narrows or falsifies it |
| --- | --- | --- |
| Typed constructs remain distinguishable on held-out packets. | Agreement by label, crossed-case accuracy, dimensional structure | Dimensions collapse, agreement stays near chance, or a simpler codebook performs equally well |
| Origin-aware grouping lowers false corroboration. | All-assigned false-corroboration risk and recall of stipulated supporting origins | No reduction, or lost stipulated supporting-origin recall outweighs the reduction |
| Typed claim/evidence paths improve evidence-grounded success. | Conjunctive action/verdict correctness plus acceptable evidence path | Gains disappear against a strong reranker or equal context/token budget |
| Bounded routing improves utility per cost. | Net utility, stopping regret, supported evidence per cost, high-severity misses | Fixed retrieval matches or wins; router over-searches, stops early, or misses critical evidence |
| Progressive packets improve human correction. | Seeded-error correction, time-to-localize, appropriate reliance, workload | More burden without correction gain, greater overreliance, or inappropriate refusal |
| Origin-bound memory reduces stale/provenance-laundered reuse. | Stale reuse, origin retention, rollback, harmful update rate | No benefit, or reduced exploration and valid updating |
| The historical label communicates its intended meaning. | Blinded restatement and connotation comparison | Material social-classification or ML-discriminator confusion after definition |

## Named task classes

Use the following classes as test cards, not as a claim that every paper must cover all of them:

- **C0 — Construct and terminology discrimination:** crossed short packets and blinded title/definition tests.
- **C1 — Atomic claim verification:** support/refute/insufficient/contested with exact spans and calibration.
- **C2 — Common-origin discrimination:** originals, syndication, paraphrase, shared datasets, independent observations, and unknown dependence.
- **C3 — Contradiction and missingness:** a bounded synthesis with stale material, a contradiction, an authoritative-but-irrelevant source, and an expected-but-unavailable perspective.
- **C4 — Cost-bounded acquisition:** a simulator with explicit search, inspect, compare, ask, answer, hold, refuse, and escalation costs.
- **C5 — Temporal memory and rollback:** dated evidence, correction, supersession, summary reuse, policy versions, and a rollback test.
- **C6 — Human evidence audit:** seeded system errors under citations, typed packet, progressive packet, and ablated conditions.
- **C7 — Low-dependence negative controls:** supplied-input extraction, bounded calculation, or creative rewriting where the added layer should have little or negative value.

## Data plan

### Public components

- [FEVER](https://aclanthology.org/N18-1074/) and [SciFact](https://aclanthology.org/2020.emnlp-main.609/) can test claim/evidence labeling in bounded corpora.
- [AVeriTeC](https://arxiv.org/abs/2305.13117) can contribute real-world claim-verification structure with careful licensing, temporal, reputational, and privacy review.
- [HoVer](https://aclanthology.org/2020.findings-emnlp.309/) can supply multi-hop evidence tasks.
- Natural Questions, BEIR, and licensed TREC collections can stress retrieval and answerability, but their relevance labels must not be relabeled as support or independence.

### Required synthetic component

A provenance-controlled generator is necessary because ordinary public corpora do not provide complete source-origin truth. The immediate study needs only source/artifact/origin/time nodes; originals, copies, paraphrases, independent-as-stipulated observations; contradiction; and an explicit unknown-origin condition. Authorization states, action costs, retrieval, memory, and outcomes belong to later experiments and must not enter the first estimand.

Generate F1/F2 condition pairs within each bundle; those pairs differ only in whether the fixed relation slots contain stipulated relation codes or no-cue placeholders. Treat the four origin structures as balanced strata, not as cross-structure counterfactual pairs: identical prose cannot coherently realize both support-only and conflict graphs. Split by proposition and origin family rather than random document so paraphrases and derived reports cannot leak across development, pilot, primary, or stress splits. Release generator code, seeds, truth manifests, and a dataset card only if publication is later authorized.

### Ethical collection boundary

Use public, license-cleared, synthetic, or explicitly consented material. Do not use private product records, credentials, cookies, personal contact data, medical/employment records, unredacted allegations, or real consequential decisions. Alpha Solver and Signal Foundry may inform schema design only; neither is validation data.

## Later-program conditions and ablations

The immediate F0–F2 study is specified in the dedicated protocol and must not expand into the table below. If later work tests the wider action policy, headline comparisons should use the same model version, retrieval index, tool access, token/context caps, run count, time budget, and review opportunity.

| ID | Condition | Question answered |
| --- | --- | --- |
| A0 | No external context, abstention allowed | Prior-knowledge/answerability control only |
| A1 | Ordinary retrieval plus citations | Does any retrieval solve the task? |
| A2 | Strong source-faithful retrieval/reranking RAG | Does the full proposal beat the strongest simple baseline? |
| A3 | Provenance-only | Is lineage sufficient? |
| A4 | Claim/evidence-only | Is atomic support sufficient without origin and routing? |
| A5 | Candidate profiled typed policy | Does the proposed intervention add net value? |
| A6 | Gold-provenance or gold-span oracle on synthetic data | Where is the ceiling, and which stage fails? |

Required A5 ablations remove, one at a time: origin grouping, typed fields, unknown dependence, adaptive stopping, visible exclusions, provenance, human override, origin-bound memory, and progressive disclosure. An ablation that receives less context or a weaker model is not a fair mechanism test.

The simple baseline is not a straw person. A 2025 controlled evaluation found a source-faithful retrieve-then-read baseline could match or outperform more elaborate tested pipelines under matched/scaled token budgets ([Laitenberger, Manning & Liu](https://aclanthology.org/2025.emnlp-main.1656/)). Added structure must therefore pay for itself.

## Later-program outcomes and analysis

### Primary outcome candidates

- evidence-grounded task success: correct action/verdict **and** acceptable evidence path;
- false corroboration with valid independent-evidence recall as a paired safety endpoint;
- utility net of unsupported-error harm, search cost, review cost, and latency;
- correction of seeded errors with time-to-localize and workload;
- appropriate abstention/routing rather than raw refusal count.

### Secondary outcomes

Evidence precision/recall, contradiction and omission detection, Brier score and risk–coverage, route compliance, provenance completeness, origin-cluster accuracy, token/time/money cost, clicks, evidence-span inspection, review burden, subgroup coverage, and rollback success.

Do not use citation count, fluency, global trust, or self-reported satisfaction as a substitute for the primary outcome.

### Planning posture—not discovered facts

Earlier global targets for raters, items across five task classes, seeds, and a 240-person interface study are retired as first-paper targets. They were not tied to one estimand or primary contrast. Each later study requires its own feasibility pilot, practically important effect, unit, clustering assumptions, multiplicity plan, and power simulation before definitive data access. Model seeds remain repeated measurements within items, not additional independent observations.

### Statistical posture

Preregister one primary outcome and unit per class. Use mixed-effects models for participant/item/origin-family structure where estimable, report absolute effects and 95% intervals, and treat seed variation as uncertainty rather than cherry-picking. Use equivalence or non-inferiority tests for null/narrowing claims; “not statistically significant” is not evidence of equivalence.

## Stage gates

1. **P0 — Claim and prior-art protocol.** Register databases, queries, dates, eligibility, screening, extraction, and comparison features. Output: screened corpus and scoped novelty statement.
2. **P1 — Origin-relation metadata benchmark.** Freeze the 80 development, 40 pilot, 300 primary, and 60 stress bundles; F0–F2 prompts; leakage checks; exact F1/F2 token parity; model; parser; power simulation; and one primary/safety endpoint pair. Output: a bounded oracle relation-metadata condition effect or negative result for one frozen model.
3. **P2 — Noisy provenance or construct study.** Choose one: test predicted/noisy origin relations, or separately test human construct/terminology comprehension. Do not combine them.
4. **P3 — Candidate action-policy comparison.** Only if P1/P2 justify it, compare strong source-faithful, source-reliability, claim-only, provenance-only, and profiled-policy conditions under matched resources.
5. **P4 — Controlled human correction study.** Only after a stable error worth correcting exists; one compact interface intervention and one human primary endpoint.
6. **P5 — Optional bounded longitudinal pilot.** Only after governance/ethics approval and predefined outcomes. Output: feasibility in one setting, not enterprise validation.
7. **P6 — Independent second-domain/adversarial replication.** Only then consider a narrow cross-domain claim.

A negative gate stops escalation. It does not invalidate the conceptual work; it determines the smaller defensible paper.

## Small-paper portfolio

If the end-to-end paper is premature, the research can decompose into publishable questions:

1. Search decision receipts: search, stop, hold, or ask under budget.
2. Provenance–action gap: citation-only versus actionable claim paths.
3. Typed reasoning cues versus generic explanations.
4. Common-origin control with an explicit unknown-dependence state.
5. A type-specific uncertainty grammar for support, identity, origin, scope/time, and consequence.
6. The complexity tax: full policy versus strong simple baseline.
7. Directed and serendipitous evidence discovery with unvisited branches preserved.
8. Role-aware evidence networks with authority, dissent, audience, disposition, and version.

The first portfolio item has now been narrowed to the origin-cue benchmark. The provenance–action gap remains the most plausible next paper only if that benchmark exposes a stable error and the added interface can be tested without changing the underlying evidence.

## Safety, privacy, fairness, and stop events

Predefine immediate quarantine for secret/private-data exposure, unauthorized retrieval or action, a real consequential recommendation, defamatory or discriminatory labeling, loss of auditable raw evidence, or prompt-injection/memory propagation into later tasks. Preserve the receipt, stop runs, remove affected artifacts from analysis, and require documented containment before resuming.

Fairness analysis should begin with source-ecology coverage, omission, burden, language, accessibility, and authority-prior bias. Do not infer protected attributes merely to populate a fairness table. Public availability is not blanket authorization to acquire, transform, retain, or redistribute.

## Manuscript architecture after the immediate P1 study

1. False corroboration and the bounded cue-use claim
2. Claim provenance, report/study identity, and closest origin-accounting prior art
3. Stipulated graph semantics and what synthetic origin cannot establish
4. Fictional bundle generator, leakage audit, and F0–F2 resource matching
5. One primary endpoint, one safety endpoint, and preregistered analysis
6. Results, including invalid runs, overhead, stress tests, and negative outcomes
7. Shortcut, model-instability, and public-transfer limitations
8. Claims permitted by the gate and the next experiment, if any

Until P1 has preregistered data and results, the honest genre remains conceptual framework plus research agenda—not an empirical research paper.

## Current local evidence package

- `research/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md`
- `research/overnight/02_EMPIRICAL_RESEARCH_DESIGN_LUNA_MAX.md`
- `research/overnight/03_NEW_INSIGHTS_AND_VISUAL_OPPORTUNITIES_LUNA_MAX.md`
- `research/overnight/rounds/04_LOOP1_THEORY_RED_TEAM.md`
- `research/overnight/rounds/05_LOOP1_EMPIRICAL_RED_TEAM.md`
- `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`
- `research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md`
- `research/RESEARCH_PAPER_READINESS_PATH.md`
- `research/CLAIMS_AND_EVIDENCE_REGISTER.md`
- `research/OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md`
- `source/THOUGHT_PIECE_V14.md`

These files are inputs to future protocol work. Their presence is not evidence that a study or peer review has occurred.
