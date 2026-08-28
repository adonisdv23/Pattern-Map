# Loop 1 empirical feasibility red team

Status: design review only; no live or paid study, recruitment, deployment, publication, or external data collection was performed.

Scope: this memo attacks `research/PAPER_PROSPECTUS_V0.md` and the earlier design in `research/overnight/02_EMPIRICAL_RESEARCH_DESIGN_LUNA_MAX.md`. It does not edit either source. The repository’s thought piece remains a conceptual framework with no empirical validation; Alpha Solver and Signal Foundry remain implementation contexts, not evidence.

## Executive verdict

The integrated prospectus is not executable as a first paper. It asks one program to validate constructs, provenance, claim support, routing, stopping, human correction, memory, terminology, fairness, and longitudinal outcomes while comparing seven AI conditions and nine ablations. That is a family of studies with different units of analysis and different ground truths, not one coherent experiment.

The smallest credible first study is a **single-mechanism offline benchmark**:

> When an AI model receives the same evidence text, do compact, relation-typed provenance cues with an explicit `unknown` origin state reduce false corroboration compared with citation-only context, after separating the effect of an origin-counting instruction from the effect of the metadata itself?

This study tests **origin accounting as a representation/use mechanism**, not the full discrimination layer, not automated origin discovery, not human decision quality, not acquisition/stopping, and not memory. It can be run offline with a new fictional corpus and one frozen local model. Its primary result is a paired reduction (or non-reduction) in false corroboration, with valid independent-origin recall as a safety endpoint.

Feasibility verdict:

- **Full prospectus as first paper:** `NOT FEASIBLE` without splitting into several papers and gates.
- **Earlier 7-class/7-condition/9-ablation program:** `OVER-SCOPED` for a first executable study; it has too many estimands and creates matched-resource ambiguities.
- **Reduced origin-accounting benchmark:** `FEASIBLE` as a bounded computational study, provided the authors accept a synthetic provenance truth boundary and do not claim improved decisions or human correction.
- **Human or field validation in Loop 1:** `DEFER`. It adds an independent burden/automation-bias study and cannot repair an unvalidated benchmark.

## 1. Red-team findings at a glance

| Finding | Severity | Why it invalidates or weakens the current program | Required correction |
| --- | --- | --- | --- |
| The C0 construct task mixes source-level, edge-level, task-level, and policy-level objects. | Critical | Agreement may reflect reading the rubric, not discriminant validity among latent constructs. | Remove C0 from the first study; test one typed relation with one unit. If a construct paper follows, build a separate multi-method validity design. |
| Synthetic provenance is treated as if it establishes real-world independence. | Critical | A generator can establish origin labels by fiat, but cannot establish epistemic independence or truth in the world. | Call the target `origin dependence` or `origin accounting`; do not call it consensus, truth, or independent corroboration beyond the stipulated graph. |
| Gold provenance cues make the task an information-display test, not end-to-end provenance inference. | Critical | If the intervention receives the correct relation labels, gains may come from an oracle cue. | State the estimand explicitly. Defer origin detection to a later study with noisy/unknown labels. |
| A5 changes prompts, metadata, packet structure, context, and routing at once. | Critical | Any difference is a bundle of information, instruction, verbosity, and algorithm effects. | Use the same evidence bundle and output schema; compare flat context, rule-only context, and typed metadata. No retrieval or routing in the first study. |
| “Matched resources” is not defined when typed metadata costs tokens. | High | Equal documents, equal tokens, and equal information cannot all hold automatically. | Pad metadata slots to equal length; report a practical same-content condition and token/latency overhead separately. |
| The prospectus has multiple primary endpoints and implied composites. | Critical | A favorable result can be selected from claim accuracy, false corroboration, calibration, utility, correction, time, and burden. | One primary contrast and one safety endpoint; all other measures are secondary/descriptive. |
| Five seeds are treated as if they increase item-level power. | High | Seeds repeat the same item and are not independent replications of the task population. | Cluster seeds within item; power on paired bundles, not seed count. |
| 400–600 items in each of five classes plus 240 people is an enormous data/annotation burden. | Critical | It is infeasible before codebook, split, and endpoint stability are known. | Build 300 paired bundles for one mechanism; defer human sample planning. |
| Multiple ablations and class interactions are under-powered and invite garden-of-forking paths. | High | Nine ablations × classes × models × endpoints overwhelms any preregistered family. | One primary contrast; at most two secondary contrasts and one predeclared stress test. |
| Human study is not a simple follow-on. | High | It introduces interface learning, order, expertise, workload, automation bias, accessibility, and ethical review confounds. | Do not recruit for Loop 1. Treat human correction as a separate paper after the benchmark has a stable error pattern. |
| Current stop rules mix data-quality, safety, efficacy, and naming decisions. | High | A failed parser, null effect, and terminology problem require different decisions; mixing them enables post hoc continuation. | Separate hard safety/data quarantine from efficacy equivalence and scope-narrowing gates. |
| The first paper still tries to validate “the layer.” | Critical | A null on origin counting would not falsify routing, claim support, or human correction; a positive origin result would not validate them. | Title and claim the paper around origin accounting only. |

**Evidence posture.** Findings about the documents are direct observations of their proposed scope. Methodological cautions below are recommendations grounded where possible in primary or authoritative methods sources; they are not empirical results about this project.

## 2. Construct separability attack

### 2.1 The current C0 is not a single measurement problem

The prospectus asks raters to distinguish:

- **source-level** properties: scoped authority;
- **artifact/graph** properties: provenance, derivation, recurrence, and origin dependence;
- **claim-edge** properties: support, contradiction, insufficiency;
- **task-level** properties: relevance and attention priority;
- **policy-level** properties: enrichment value, action priority, and disposition;
- **outcome-level** properties: later observed consequence and update.

These are not interchangeable indicators of one latent trait. They have different arguments, units, time indices, and ground truths. For example, “this source is authoritative for its release notes” is a source/claim-scope judgment; “this passage supports claim X” is an edge judgment; “inspect this item next” is a decision under cost; “the pilot succeeded” is a later outcome. A single packet-sorting score cannot establish that the dimensions are empirically distinct.

**Sourced methodological constraint.** Construct validation requires a network of expected relations, not only inter-rater agreement; the classic construct-validity treatment is [Cronbach & Meehl (1955)](https://doi.org/10.1037/h0040957), and convergent/discriminant validation explicitly compares multiple traits and methods in a multitrait–multimethod matrix ([Campbell & Fiske (1959)](https://doi.org/10.1037/h0046016)).

**Red-team inference.** The earlier C0 design can produce high agreement simply because all raters follow a clear codebook or because the cases contain obvious lexical cues. Agreement would not show that authority, support, relevance, and action priority are discriminant constructs, nor that all belong in a minimal layer.

### 2.2 What must be removed from the first study

Do not make the first study answer any of these:

- whether “authority” and “support” are psychometrically separable;
- whether “discrimination layer” is the best or safest name;
- whether humans can apply eleven fields reliably;
- whether a route receipt improves decisions;
- whether outcome feedback or memory updates are valid.

Those are distinct studies. In particular, a terminology result cannot be used as construct evidence, and a model’s ability to follow an origin table cannot establish human interpretability.

### 2.3 Narrowed construct

Use one construct with one unit:

> **Origin dependence:** a typed relation between two evidence artifacts indicating `dependent`, `independent-as-stipulated-by-the-benchmark`, or `unknown` under a declared provenance graph.

“Independent-as-stipulated” is deliberate. The first study tests whether the model uses a relation record to avoid counting repeated artifacts as multiple pathways. It does not claim that a synthetic graph proves epistemic independence, causal independence, source honesty, or truth.

The first study therefore evaluates an **origin-accounting cue**. A later construct study can test whether human experts interpret this cue consistently; a later origin-inference study can test whether a system can infer it from real provenance.

## 3. Benchmark leakage and provenance-ground-truth attack

### 3.1 Public datasets are unsuitable as the primary origin benchmark

FEVER, SciFact, HoVer, AVeriTeC, Natural Questions, and BEIR have useful, documented task labels, but their released labels do not provide complete source-origin truth for every report. FEVER’s claims and evidence are tied to a bounded Wikipedia setup ([Thorne et al.](https://doi.org/10.18653/v1/N18-1074)); SciFact has expert claim/evidence rationales in a scientific corpus ([Wadden et al.](https://doi.org/10.18653/v1/2020.emnlp-main.609)); AVeriTeC provides real-world claims and web evidence ([Schlichtkrull, Guo, & Vlachos](https://arxiv.org/abs/2305.13117)). None should be relabeled as “independent sources” merely because multiple documents appear.

**Recommendation.** Use no public corpus in the primary statistical test. Use public datasets only as a descriptive transfer challenge after the primary analysis is locked, with any origin labels manually documented as partial or `unknown`.

### 3.2 Synthetic truth is useful but narrow

A synthetic generator can guarantee that four reports share an origin or that three reports are generated from separate origin nodes. It cannot demonstrate that the reports would count as independent evidence in a real epistemic community. The data-generating process also risks teaching the model the generator’s style rather than the intended relation.

Therefore the primary paper must say:

- **What is true by construction:** source/artifact/derivation/time graph, assigned relation, claim polarity, and report-to-origin membership.
- **What is not established:** real-world truth, source authority, independent causal confirmation, prevalence, or usefulness to a human decision-maker.
- **What is being tested:** whether a model uses a relation-typed cue to count origin pathways and avoid false corroboration.

### 3.3 Specific leakage routes and controls

| Leakage/shortcut | How it can arise | Control in the reduced study |
| --- | --- | --- |
| Origin IDs leak the label | `origin_A`, `origin_B`, or sequential IDs reveal the number of clusters. | Random opaque IDs per item; randomize which reports share an ID; never use cluster order as a label. |
| Formatting leaks the condition | Typed bundles contain extra brackets, tables, or distinctive delimiters. | Fixed-width metadata slots in every condition; use a placeholder/padding block of equal length. A blinded format classifier must stay at chance. |
| Lexical copying solves dependence | Dependent reports are more similar than independent reports. | Match lexical overlap and length across relation strata; include independent reports with shared technical vocabulary and dependent paraphrases with low surface overlap. |
| Template/style solves the label | One author or template writes all dependent reports. | Cross style, author simulation, order, and report position across every relation type; hold out style combinations. |
| Model pretraining contamination | FEVER/Wikipedia/SciFact text may be memorized. | Primary corpus is newly authored fictional micro-reports; public text is secondary descriptive transfer only. |
| Generator artifacts | Punctuation, token count, entity names, or metadata order correlates with relation. | Train a non-semantic classifier on surface features; if it exceeds a preregistered ceiling, regenerate or quarantine the affected split. |
| Test-family leakage | Near-duplicate reports or a base proposition cross splits. | Split by underlying proposition and origin family, not document. Hash exact/near duplicates and compare all transformations before release. |
| Gold graph is mistaken for an inferred graph | Correct origin labels supplied to the model make the task an oracle test. | Label the estimand as cue-use/representation. Do not claim end-to-end provenance inference. Add a separate noisy-cue stress test only as secondary. |
| Public transfer labels are over-trusted | Annotators infer common origin from URLs or publishers. | Preserve `unknown` unless a source-to-source derivation is documented; report transfer descriptively, not as primary evidence. |

### 3.4 Minimal corpus design

Create **300 primary bundles** from novel, fictional, non-sensitive micro-reports. Each bundle contains a target claim and four to six reports. Use four balanced origin structures, 75 bundles each:

1. **One-origin repetition:** all supporting reports derive from one original; no independent supporting origin exists.
2. **Multiple-origin convergence:** supporting reports derive from three separately authored origin nodes; the relation is independent-as-stipulated.
3. **Unknown origin:** reports agree, but the graph intentionally withholds the relation; the correct state is not to count them as independent.
4. **Conflict:** one origin supports, one origin refutes, and one dependent copy repeats either side.

Use at least two fictional content domains (for example, technical evaluation and environmental observation) and cross each with report style and order. Do not use real people, real allegations, medical records, or sensitive current events. Have an independent content audit check that the reports express the intended claim polarity and that copies/paraphrases preserve or negate meaning as specified. The audit validates semantic construction; it does not upgrade synthetic origin to real-world independence.

Add **60 stress bundles** (descriptive, not primary) with report-order changes and known metadata corruption rates (for example, 10% relation-field flips). Do not use stress bundles to enlarge primary (N) after seeing results.

## 4. Matched-resource and comparator attack

### 4.1 Why the prospectus A5 comparison is confounded

A5 simultaneously changes:

- evidence representation;
- prompt instructions;
- source/artifact metadata;
- relation labels;
- packet structure and exclusions;
- acquisition/stopping behavior;
- human override;
- memory and route receipts.

If A5 wins, the result cannot identify which change mattered. If it loses, a missing implementation component could be blamed after the fact. The prospectus also says “matched tokens/context” while giving the proposed condition extra semantic metadata. Equal raw text, equal tokens, equal compute, equal retrieval access, and equal information cannot all be assumed; they must be specified as separate estimands.

The 2025 controlled RAG evaluation by Laitenberger, Manning, and Liu is a direct warning: a simple source-faithful retrieve-then-read baseline can match or outperform more elaborate pipelines under scaled token budgets ([ACL Anthology; DOI 10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656)). The first study must make the baseline strong and must not attribute a formatting or context-size gain to a layer.

### 4.2 Three-condition design

All conditions receive the identical evidence text, report order, claim, output schema, maximum output tokens, and a fixed compact metadata block. The primary model and decoding settings are identical. Metadata slots are padded so the input-token distribution is equal within a small prespecified tolerance.

| Condition | Information shown | Instruction | Estimand |
| --- | --- | --- | --- |
| **F0 — citation-only** | Opaque source/artifact IDs and dates; no origin relation. | Generic instruction to assess the claim and cite support. | Baseline performance. |
| **F1 — rule-only** | Same opaque metadata and evidence as F0. | Adds the explicit rule “count distinct origin pathways; do not treat repeated reports as independent; preserve unknown.” | Instruction/cognitive-rule effect without relation information. |
| **F2 — typed-cue** | Same evidence, output, instruction, and fixed-width metadata; origin relation field is populated with the true `dependent`, `independent-as-stipulated`, or `unknown` state. | Same rule as F1. | **Primary contrast F2 − F1:** value of relation-typed provenance cues beyond an explicit rule. |

F0 versus F1 is secondary: it estimates the instruction effect. F2 versus F0 is secondary: it estimates total cue-plus-rule effect. Do not add A0–A6, human conditions, retrieval variants, or nine ablations to the primary study.

### 4.3 What the design does and does not match

- **Matched:** source text, task labels, number of reports, report order, model/checkpoint, prompt except the predeclared relation field/rule contrast, output schema, output cap, metadata slot length, decoding, and run ledger.
- **Not claimed to be matched:** human interpretability, real-world acquisition cost, unknown-origin detection, source authority, and practical deployment burden.
- **Reported separately:** input/output tokens, latency, memory/compute, invalid-output rate, and any metadata construction cost.

The relation field is deliberately supplied in F2. This is an upper-bound representation test. It is not a fair test of a system that must discover provenance. A later experiment can replace the field with predicted/noisy relations; it must not be smuggled into this result.

## 5. Primary endpoint and analysis attack

### 5.1 Current problem

The prospectus lists evidence-grounded success, false corroboration, utility, calibration, correction, time, burden, source diversity, provenance completeness, subgroup coverage, and rollback as candidate “primary” outcomes across classes. A favorable paper could select whichever moved. A utility composite also hides normative weights and makes a synthetic task look consequential.

### 5.2 One primary endpoint

For each bundle and condition, parse a structured response containing:

- `origin_count_supporting`: number of distinct supporting origin pathways asserted;
- `claim_state`: `supported`, `refuted`, `insufficient`, or `contested`;
- `confidence`: a probability for the selected claim state;
- `evidence_ids`: reports used for the assertion.

Define a **false-corroboration event** (FC_i=1) if the model asserts at least two independent supporting pathways when the manifest contains zero or one supporting origin, or if it labels a claim supported on the basis of dependent copies while omitting the contradictory/insufficient state required by the bundle. The exact parser and condition-specific gold rule are frozen before runs.

The primary estimand is the paired difference:

`ΔFC = P(FC = 1 | F2) − P(FC = 1 | F1)`

Lower is better. The primary unit is a bundle, not a model seed or report. The primary contrast is F2 versus F1.

### 5.3 One safety endpoint

Define **valid-origin recall** as the proportion of bundles with at least two independent-as-stipulated supporting origins for which the model asserts at least two, while not counting dependent copies. The typed cue must not reduce this by more than a prespecified absolute margin (candidate: 5 percentage points). This prevents a system from winning by calling everything dependent or unknown.

### 5.4 Secondary endpoints

- origin-count absolute error;
- claim-state accuracy and macro-F1 across support/refute/insufficient/contested;
- confidence Brier score and risk-coverage, reported descriptively unless explicitly powered;
- evidence-ID precision/recall against the bundle manifest;
- invalid structured-output rate;
- input/output tokens, latency, and local compute;
- performance on the 60 stress bundles;
- relation-stratum and content-domain estimates as exploratory moderation.

Do not report “decision utility,” human correction, fairness of authority judgments, or field outcome benefit from this study. The synthetic bundle has no real consequence function, so a normative utility score would create false precision.

### 5.5 Statistical plan

Use paired item-level comparisons because every condition sees the same bundle. The primary result is an absolute risk difference with a paired bootstrap confidence interval over bundles and an exact/permutation test or mixed-effects logistic model with bundle as the unit. If multiple seeds are run, nest seed variation within bundle; do not count seed repeats as new bundles.

Use one primary contrast at two-sided α = .05. Treat F0–F1, F2–F0, stress bundles, domains, and model robustness as secondary. Apply Holm adjustment to the small predeclared family of secondary inferential contrasts ([Holm, 1979](https://doi.org/10.2307/4615733)); do not use post hoc endpoint selection. If a family of exploratory slices is reported, label it exploratory and control false discovery with a prespecified procedure such as Benjamini–Hochberg ([Benjamini & Hochberg, 1995](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)).

An efficacy claim requires both:

1. a lower F2 false-corroboration rate than F1 by at least the predeclared minimum important difference; and
2. valid-origin recall under the non-inferiority margin.

If the confidence interval is compatible with both a useful benefit and no benefit, report imprecision rather than “inconclusive success.”

## 6. Power and planning red team

### 6.1 What is wrong with current targets

The prospectus’s 60–80 construct raters, 400–600 items per five classes, five seeds, and 240 participants look precise but are not tied to one effect, one unit, or one primary contrast. A large item count cannot repair a weak or contaminated gold label. Five seeds do not turn one bundle into five independent pieces of evidence. A 240-person human study cannot be powered until the task time, error prevalence, learning/carryover, and item variance are known.

The earlier memo’s “+5 percentage points” and “−10 percentage points” thresholds were design candidates, not evidence. They were also too generic across different endpoints. Sample-size reasoning should begin with a practically important effect and its uncertainty; see [Lakens (2013)](https://doi.org/10.3389/fpsyg.2013.00863). A pilot should be treated as feasibility and instrument repair, not a reliable efficacy effect-size estimator ([Leon, Davis, & Kraemer, 2011](https://doi.org/10.1016/j.jpsychires.2010.10.008)).

### 6.2 Reduced target

Target **300 primary bundles**, balanced 75 per origin structure. Before locking the final (N), run an auditable paired-Bernoulli simulation using plausible baseline FC rates and discordance. A transparent planning scenario is:

- baseline F1 false-corroboration rate: 20–40%;
- F2 absolute reduction of practical interest: 8 percentage points;
- paired discordance: 10–30% of bundles;
- two-sided α = .05, target power at least 80% for the pooled primary contrast;
- 10% reserve only for predeclared data-quality invalidation, not for favorable stopping.

At 300 bundles, an 8-point paired effect may be detectable under moderate discordance; a 3–5-point effect will generally require substantially more bundles. The actual power curve, not this illustration, belongs in the preregistration. If the simulation cannot reach 80% power for the smallest claimed effect at an affordable (N), downgrade the study to an estimation/benchmark paper and remove superiority language.

Do not power confirmatory conclusions for each origin structure, domain, model, seed, or stress condition. Those are descriptive or exploratory. If the effect exists only in one structure, narrow the claim to that structure.

### 6.3 No human sample in Loop 1

There is no participant sample-size calculation in the reduced study because there is no human efficacy study. This is a feature, not a missing section. A later human study must be separately powered on a single correction endpoint after the benchmark shows a reproducible error worth correcting. Report a pilot using feasibility outcomes—task comprehension, completion, attrition, timing, accessibility, and interface failures—rather than treating a small convenience sample as evidence of improved human decisions. The CONSORT pilot/feasibility extension is [Eldridge et al. (2016)](https://doi.org/10.1186/s40814-016-0105-8).

## 7. Human-study burden and confound attack

The earlier proposal’s H0–H3 study is not a simple “add a packet and measure correction” experiment. It would confound:

- prior expertise and domain knowledge;
- interface familiarity and training;
- whether H2 exposes extra evidence rather than better organization;
- progressive disclosure versus information amount;
- report order and long-context position;
- seeded-error prevalence and salience;
- demand characteristics and belief that typed evidence is better;
- automation bias and inappropriate deference;
- accessibility, reading speed, and fatigue;
- carryover if the same participant sees matched origin variants;
- rater disagreement over the “correct” decision;
- time pressure versus careful review.

Human appropriate reliance is a distinct human-factors claim; it cannot be inferred from model false-corroboration. A human study also requires consent, compensation, data retention, accessibility, ethics review, and harm monitoring. The prospectus is correct to name these burdens, but it still treats P4 as a routine next stage. The red-team recommendation is to defer P4 until the first computational study has:

1. a stable, observable error mode;
2. a compact interface intervention rather than a full system;
3. a single human primary endpoint;
4. a trained but blinded adjudication rubric; and
5. a power simulation based on actual item difficulty.

No human participant should make a real consequential decision through the system. A future human study should use synthetic/public packets and require participants to accept, correct, or defer a frozen model output, with no downstream action.

## 8. Stop-rule and gate attack

### 8.1 Separate hard stops from scientific conclusions

The current prospectus combines critical harm events, construct failure, baseline ties, terminology confusion, and non-significance in one family of “stop or narrow” criteria. Use four separate gates:

1. **Safety/data quarantine (hard stop):** private/secret data, unauthorized retrieval, harmful real-person labeling, missing raw evidence, or condition leakage. Freeze the affected run and do not interpret it as efficacy evidence.
2. **Feasibility gate:** parser failure, unable-to-reproduce runs, unacceptable invalid-output rate, metadata format detectable above the predeclared ceiling, or unresolved split leakage. Repair or stop; do not silently change the test.
3. **Primary efficacy gate:** one predeclared F2-versus-F1 contrast and one valid-origin-recall margin. Report benefit, harm, or imprecision.
4. **Scope gate:** decide whether the result supports only origin-cue use under stipulated graphs, a stronger claim, or no useful claim. This is a scientific interpretation, not a reason to rerun until positive.

### 8.2 Fixed stopping

Run the preregistered 300 primary bundles once. Do not peek and stop for a positive effect. Allowed early termination is only for hard safety/data quarantine or a technical failure that invalidates the run. If a technical failure occurs, the preregistration must define whether the affected bundles are rerun, excluded, or replaced before looking at outcomes. If sequential sampling is scientifically necessary later, use a prespecified sequential procedure; do not call an unregistered peek a pilot.

### 8.3 Candidate feasibility thresholds

These are recommendations to preregister, not observed values:

- condition-format classifier accuracy no higher than a prespecified small margin above chance;
- at least 98% parsable outputs, with invalid outputs scored as failures rather than repaired;
- at least 99% provenance manifest integrity and zero unrecorded condition changes;
- no unresolved exact/near-duplicate cross-split leakage;
- no unreviewed private or sensitive text in the corpus;
- run replay produces the documented deterministic or seed-bounded output;
- no more than 10% of primary bundles invalidated for data-quality reasons; otherwise report a benchmark failure, not a positive result.

## 9. Smaller executable first-study protocol

### Study title

**Origin Accounting Under Typed Provenance Cues: A Controlled Offline Benchmark**

### Claim under test

For a frozen local model and newly authored fictional evidence bundles with stipulated provenance, typed origin cues with an explicit unknown state reduce false corroboration relative to an explicit origin-counting rule without those cues, at matched evidence text and padded metadata length.

### Out of scope

The study does not test or claim:

- full discrimination-layer effectiveness;
- human decision quality or correction;
- automated common-origin discovery;
- source authority, truth, prevalence, or real-world consensus;
- retrieval quality, acquisition value, stopping, memory, outcome learning, or deployment;
- fairness of real-world authority or source-selection policies;
- terminology comprehension;
- enterprise readiness or safety in consequential use.

### Materials

- 300 primary fictional bundles, 75 per origin structure;
- 60 predeclared stress bundles with report-order perturbations and relation-field noise, analyzed descriptively;
- four to six reports per bundle, one target claim, and a complete manifest;
- two content domains and multiple writing styles crossed with structure;
- no real person, private record, current allegation, or paid/live source;
- a source-artifact-origin-time graph generated before model runs;
- human semantic audit of claim polarity, paraphrase equivalence, contradiction, and formatting; origin labels remain stipulated graph facts.

### Systems

- one frozen, locally runnable open-weight instruction model selected before the test split is opened;
- deterministic decoding for the primary run, or a predeclared small seed set if deterministic decoding is unavailable;
- optional second model only as a robustness analysis, not a second powered claim;
- no live web, provider API, paid call, tool acquisition, or prompt tuning after the test lock.

### Conditions

F0, F1, and F2 as defined in Section 4.2. Use the same bundle order across conditions for each paired item; use a separate predeclared permutation set for stress testing. All outputs use the same strict schema and cap. Invalid outputs are failures; no manual retries.

### Primary analysis

1. Lock generator, manifests, split hashes, prompts, model hash, decoder, parser, and analysis script.
2. Run F0–F2 on every primary bundle.
3. Parse `FC`, valid-origin recall, claim state, confidence, evidence IDs, tokens, latency, and invalid output.
4. Test F2 versus F1 on the pooled paired bundle unit.
5. Report absolute difference, paired confidence interval, effect by origin structure/domain as exploratory, and all failed/invalid runs.
6. Apply the predeclared equivalence/non-inferiority criterion for valid-origin recall.
7. Run stress bundles only after the primary output is frozen; label them secondary.

### Falsifiers for the reduced study

| Result | Falsification/narrowing decision |
| --- | --- |
| F2 does not reduce FC by the minimum important effect versus F1. | No evidence that typed origin cues add value beyond the rule in this setting; do not claim an origin-accounting benefit. |
| F2 reduces FC but valid-origin recall falls beyond the non-inferiority margin. | The cue encourages blanket discounting; reject the intervention as currently specified. |
| F1 equals F2 and both beat F0. | The explicit rule, not provenance metadata, explains the effect; narrow to instruction/policy and do not claim typed evidence value. |
| F2 beats F1 only on formatting-easy cases or a single relation/domain. | Narrow to that condition; investigate shortcut leakage before any efficacy claim. |
| A surface-only classifier predicts F0/F1/F2 or relation strata above the preregistered ceiling. | Quarantine/regenerate the corpus; no result is interpretable until leakage is repaired. |
| F2 works only with gold metadata and fails with 10% relation noise. | Claim only a perfect-cue upper bound; defer end-to-end/noisy provenance claims. |
| Effects vary materially by model or seed. | Report model-specific/instability result; no general AI claim. Seeds remain uncertainty, not extra (N). |
| Public transfer challenge fails while synthetic primary succeeds. | Narrow entirely to stipulated synthetic origin accounting; do not claim transfer to public evidence. |
| The metadata token/latency overhead is substantial despite padding. | Report a cost trade-off; no “more efficient” claim. A useful accuracy effect may still support a bounded representation result only if cost is transparent. |
| More than 10% of primary bundles are invalidated or output parsing is unreliable. | Feasibility failure; stop before interpreting efficacy. |

## 10. Preregistration and reproducibility checklist

Register before opening the primary test split or running the model:

- exact claim, primary contrast, unit, and minimum important effect;
- generator code, random seeds, origin graph schema, relation strata, writing-style assignment, and split rule;
- data-quality and surface-classifier tests with fixed thresholds;
- exact model/checkpoint hash, tokenizer, prompt, metadata slot format, decoding, output cap, and parser;
- F0/F1/F2 condition definitions and token-padding rule;
- fixed (N=300), allowed data-quality invalidation, and no efficacy peeking;
- `FC` and valid-origin-recall algorithms, including contradiction/unknown treatment;
- paired bootstrap/permutation or mixed-model specification;
- one primary contrast, secondary contrast family, Holm correction, and exploratory labeling;
- missing/invalid run policy, replay test, stress-set lock, and reporting of all failures;
- no claim of real-world independence or decision utility from stipulated synthetic graphs.

Release, if later authorized, the generator, manifests, prompt templates, model/config hashes, parser, analysis code, surface-leakage report, semantic-audit protocol, run ledger, and a data card. If text cannot be redistributed, release hashes and a reproducible generator rather than silently releasing a substitute corpus.

## 11. Why the first paper is smaller but still useful

The reduced study does not validate the visual framework. It answers one mechanism question that the broad thesis depends on: can a system avoid treating repeated artifacts as multiple evidence pathways when a provenance relation is made explicit? It also cleanly exposes the first decision boundary:

- If the model cannot use typed origin cues when they are supplied, adding a full graph/router/interface is unlikely to help without first solving basic cue use.
- If the model uses them but gains are only due to the explicit rule, the contribution is a policy instruction, not a typed provenance layer.
- If the cue reduces false corroboration but suppresses genuine origin diversity, the framework needs calibrated unknowns and appeal rather than automatic discounting.
- If the effect survives the controls, the next study can justify testing noisy origin inference or a human audit interface; it has not yet earned a human-decision or field claim.

This is a useful negative or positive result precisely because it does not let success in one mechanism stand in for the whole architecture.

## 12. Final feasibility judgment

**Proceed only with the reduced computational benchmark.** The current prospectus should be treated as a roadmap, not a first-paper protocol. The earlier memo’s broad C0–C7/A0–A6/P0–P6 design is valuable as a research portfolio but fails the feasibility red team on construct heterogeneity, comparator equivalence, endpoint multiplicity, power interpretation, and human-study burden.

The reduced first study is executable if and only if it is presented as:

> a controlled test of relation-typed provenance cues for origin accounting on stipulated synthetic graphs under a frozen offline model.

It is not executable as “validation of the discrimination layer,” and it cannot support claims about better decisions, human correction, acquisition value, memory, enterprise use, or real-world consensus. A positive result should unlock a separately preregistered noisy-provenance or human-audit study; a null, unstable, or harmful result should narrow or retire the origin-accounting component for this task class.

## Methods sources

These sources ground methodological constraints or reporting recommendations; none validates the proposed intervention.

- Cronbach, L. J., & Meehl, P. E. (1955). “Construct Validity in Psychological Tests.” [Psychological Bulletin; DOI 10.1037/h0040957](https://doi.org/10.1037/h0040957).
- Campbell, D. T., & Fiske, D. W. (1959). “Convergent and Discriminant Validation by the Multitrait-Multimethod Matrix.” [Psychological Bulletin; DOI 10.1037/h0046016](https://doi.org/10.1037/h0046016).
- Thorne, J., et al. (2018). “FEVER: a Large-scale Dataset for Fact Extraction and VERification.” [ACL Anthology; DOI 10.18653/v1/N18-1074](https://doi.org/10.18653/v1/N18-1074).
- Wadden, D., et al. (2020). “Fact or Fiction: Verifying Scientific Claims.” [ACL Anthology; DOI 10.18653/v1/2020.emnlp-main.609](https://doi.org/10.18653/v1/2020.emnlp-main.609).
- Schlichtkrull, M., Guo, Z., & Vlachos, A. (2023). “AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web.” [arXiv:2305.13117](https://arxiv.org/abs/2305.13117).
- Laitenberger, A., Manning, C. D., & Liu, N. F. (2025). “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models.” [ACL Anthology; DOI 10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656).
- Lakens, D. (2013). “Calculating and Reporting Effect Sizes to Facilitate Cumulative Science.” [Frontiers in Psychology; DOI 10.3389/fpsyg.2013.00863](https://doi.org/10.3389/fpsyg.2013.00863).
- Leon, A. C., Davis, L. L., & Kraemer, H. C. (2011). “The Role and Interpretation of Pilot Studies in Clinical Research.” [Journal of Psychiatric Research; DOI 10.1016/j.jpsychires.2010.10.008](https://doi.org/10.1016/j.jpsychires.2010.10.008).
- Eldridge, S. M., et al. (2016). “CONSORT 2010 Statement: Extension to Randomised Pilot and Feasibility Trials.” [Pilot and Feasibility Studies; DOI 10.1186/s40814-016-0105-8](https://doi.org/10.1186/s40814-016-0105-8).
- Holm, S. (1979). “A Simple Sequentially Rejective Multiple Test Procedure.” [Scandinavian Journal of Statistics; DOI 10.2307/4615733](https://doi.org/10.2307/4615733).
- Benjamini, Y., & Hochberg, Y. (1995). “Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing.” [Journal of the Royal Statistical Society Series B; DOI 10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x).
