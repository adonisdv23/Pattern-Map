# Research-paper readiness path

Status: `READINESS_PLAN_ONLY`

Recorded: 2026-08-18

## Bottom line

The current project is not a research paper, has not been peer reviewed, and contains no experimental result. It is best understood as a provisional practitioner thought piece plus a conceptual framework and research agenda. Turning it into scholarship requires selecting one contribution form, narrowing the claims to that form, completing a defensible prior-art review, and collecting evidence that could prove the framework wrong.

The six forms below are alternatives, not sections to combine into one maximal paper. After the 2026 literature expansion, the strongest near-term sequence is:

1. retain the broad framework as historical thought-piece and research-program framing, not a novelty claim;
2. implement and audit the narrow [origin-relation cue protocol](ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md) and its [operationalization specification](overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md);
3. run the 40-bundle feasibility pilot without interpreting efficacy;
4. if every gate passes, preregister and run the paired 300-bundle F2-versus-F1 false-corroboration study;
5. publish a bounded positive, null, harmful, or shortcut-contaminated result honestly; and
6. only then choose one separate next study—noisy provenance inference, terminology/comprehension, a correction interface, or a profiled action policy.

## Readiness shared by every scholarly form

Before submission of the first cue-use study as research, the work needs:

- a single primary research question and explicit unit of analysis;
- a reproducible prior-art search protocol, inclusion criteria, screening log, and synthesis—not only the current targeted map;
- a contribution statement limited to the matched origin-relation cue estimand and explicit comparison with current cross-source, conflict, provenance, and evidence-utilization work;
- operational definitions for derivation relation, origin-family relation, claim stance, all-assigned false-corroboration risk, recall of stipulated supporting origins, and unresolved origin;
- exact F1/F2 prompt/resource parity, a rule-only control, negative controls, relation-noise stress, and leakage probes;
- task, dataset, participant, and outcome choices made before observing results;
- an analysis plan, uncertainty reporting, negative-result policy, and falsifiers;
- ethics, privacy, authorization, retention, and sensitive-source review proportionate to the data and participants;
- artifact, code, prompt/model/tool version, and provenance documentation sufficient for replication;
- limitations that separate conceptual coherence, implementation feasibility, usability, and outcome effectiveness.

The exact historical diagram is now preserved and hash-verified. The standalone HTML remains a prerequisite for any claim that depends on byte-identical HTML, while the owner-designated live source and recovery memo support bounded claims about v13 content, visual structure, continuity, and intent.

## Candidate form 1: conceptual systems-framework paper

**Central research question**

What typed responsibilities and relationships are necessary to make pre-generation context judgment inspectable without collapsing authority, support, independence, relevance, cost, and action into one score?

**Plausible contribution**

A domain-bounded taxonomy, reference architecture, explicit distinction contract, and propositions connecting evidence identity, common origin, claim support, routing, human disposition, and outcome updates.

**Prior-art burden**

Highest across disciplines. A protocol-led scoping or systematic review must show where existing models already connect these responsibilities, where they use different names, and what precise gap remains. The present field map is orientation, not an exhaustive review.

**Required empirical evidence**

At minimum: expert review of construct coverage and discriminant validity; inter-rater testing of operational definitions on representative cases; counterexamples showing when the architecture should not apply. A purely conceptual paper would still need disciplined source synthesis and evaluation of the theory against rival frameworks.

**Possible hypotheses or propositions**

- P1: Authority, support, independence, relevance, and action priority are empirically distinguishable judgments.
- P2: Keeping those judgments typed exposes correctable errors that a single score hides.
- P3: Origin-bound derivations reduce false corroboration after summarization or reuse.

**Evaluation method**

Protocol-led literature synthesis; expert interviews; iterative construct sorting; Delphi-style refinement only if justified; inter-rater agreement with disagreement analysis; analytic comparison against rival architectures; adversarial boundary cases.

**Potential datasets**

Curated case packets sampled across scientific evidence, policy, product research, and technical evaluation; synthetic provenance graphs with known common origins; public claim-evidence corpora used only for the constructs they actually contain. The dataset must not be built solely from Alpha Solver or Signal Foundry.

**Human-participant needs**

Domain experts, information-science or HCI researchers, and intended knowledge-worker users. Expert status, conflicts, compensation, recruitment, and stopping rules must be specified before recruitment.

**Ethics and privacy**

Research ethics review as required; informed consent; minimal collection; no confidential product data by default; removal or controlled treatment of personal/sensitive source material; protection against reputational harm from authority labels.

**Reproducibility**

Publish the review protocol, search strings, screening decisions where licensing permits, codebook, construct definitions, coded examples, disagreement log, analysis scripts, and versioned framework.

**Falsifiers**

Experts cannot distinguish the core constructs above chance or useful agreement; a simpler existing architecture covers the same responsibility without material loss; the proposed relations contradict repeated real cases; added typing does not expose or prevent distinct errors.

**Limitations**

A framework can be internally coherent yet unusable or ineffective. Cross-domain breadth may conceal domain-specific evidence standards. Expert consensus is not outcome validation.

**Possible venues or audiences**

Information-science and cross-disciplinary design audiences. The official scopes of [JASIST](https://www.asist.org/publications/jasist/) and [Design Science](https://www.cambridge.org/core/journals/design-science) make them plausible readerships only if the work provides original, rigorous, field-relevant knowledge. This is not a venue endorsement or a claim of present readiness.

**What cannot yet be claimed**

That the architecture is novel as a whole, minimal, complete, general, reliably applicable, or beneficial.

## Candidate form 2: design-science paper

**Central research question**

How can a traceable artifact instantiate pre-generation context judgment, and what design knowledge emerges from building and evaluating it in a bounded setting?

**Plausible contribution**

A problem-grounded artifact, explicit design requirements and principles, implementation, demonstration, evaluation, and a reasoned account of which design knowledge transfers beyond the setting.

**Prior-art burden**

Design-science method plus technical precedents for evidence graphs, provenance, retrieval, routing, review interfaces, and memory. Existing tools with similar functions must be compared, not merely cited.

**Required empirical evidence**

Problem evidence from intended users; iterative artifact evaluations; technical correctness and traceability tests; usability or work-practice evaluation; comparison to a simpler baseline; negative and boundary cases.

**Possible hypotheses**

- H1: The artifact lets reviewers localize and correct a misjudgment faster than a conventional cited answer.
- H2: Origin-aware grouping reduces duplicated-evidence influence under matched time and retrieval budgets.
- H3: Explicit stopping receipts improve perceived and observed auditability without unacceptable task-time cost.

**Evaluation method**

Design cycles with requirements traceability; formative walkthroughs; technical tests; controlled task comparison; ablation of provenance, separate dimensions, common-origin analysis, and human override; summative mixed-method evaluation.

**Potential datasets**

A synthetic benchmark with seeded provenance and known claims; a license-cleared public document collection; bounded organizational cases only under explicit authorization. Product repositories can supply design examples, not outcome evidence by default.

**Human-participant needs**

Problem owners and representative analysts for requirements and evaluation; independent reviewers for outcome scoring where feasible.

**Ethics and privacy**

Separate research consent from employment or product use; prevent sensitive source contents from entering prompts or released artifacts; document role-based access and deletion/retention; assess interface-induced authority and automation bias.

**Reproducibility**

Release requirements, design rationale, architecture, schemas, runnable artifact or faithful mock, test corpus or generation procedure, baseline configuration, study materials, analysis, and complete model/prompt/tool versions.

**Falsifiers**

The artifact does not meet its own traceability invariants; users cannot understand or correct it; a simpler interface performs equivalently at lower cost; the claimed design principles do not transfer even to a second bounded setting.

**Limitations**

Artifact success can be implementation-specific; demonstration is not theory validation; iterative design with the same users can overfit local work practices.

**Possible venues or audiences**

Design-science scholars and design-oriented information-systems audiences. [Design Science](https://www.cambridge.org/core/journals/design-science) explicitly publishes research on the creation and embedding of artifacts and systems; any specific conference cycle or track must be rechecked when the work is ready.

**What cannot yet be claimed**

That a local visual map is a research artifact, that implementation feasibility proves conceptual correctness, or that product examples demonstrate transferable design knowledge.

## Candidate form 3: HCI or sensemaking-system paper

**Central research question**

How do people understand, inspect, and correct an AI system's pre-generation judgments, and which representation best supports calibrated reliance under information overload?

**Plausible contribution**

Interaction techniques and empirical knowledge about exposing evidence paths, common origin, uncertainty, exclusions, stopping decisions, and human override without overwhelming users.

**Prior-art burden**

Sensemaking, information foraging, human information interaction, visual analytics, mixed initiative, explainable AI, trust/reliance, automation bias, provenance interfaces, and human-AI guidelines.

**Required empirical evidence**

Representative-user studies with task and comprehension measures; comparison to conventional search, bookmarking, or cited-answer interfaces; qualitative analysis of correction strategies; accessibility evaluation; learning and fatigue effects.

**Possible hypotheses**

- H1: A typed evidence path improves correct identification of unsupported or dependent claims.
- H2: Showing material exclusions and unknowns improves calibrated reliance more than generic confidence displays.
- H3: Progressive disclosure preserves correction quality while reducing perceived overload relative to a fully expanded graph.

**Evaluation method**

Formative interviews and contextual inquiry; participatory or co-design where appropriate; controlled within- or between-participant studies; think-aloud or retrospective explanation; longitudinal follow-up for learning effects; qualitative coding and preregistered quantitative analysis.

**Potential datasets**

Decision vignettes with seeded errors and ground truth; provenance-rich news or research packets; task-specific corpora whose sensitivity and licenses permit participant exposure.

**Human-participant needs**

Representative knowledge workers plus a separate expert group for outcome adjudication. Include varied levels of AI, domain, and information-literacy experience; plan for accessibility rather than treating it as post hoc QA.

**Ethics and privacy**

Informed consent; protection from workplace evaluation or coercion; careful handling of interaction logs, screen recordings, and potentially sensitive queries; deception only if justified and reviewed; post-study explanation of seeded errors.

**Reproducibility**

Release interface versions, stimuli, task scripts, measures, codebook, preregistration, anonymized data or defensible synthetic substitute, analysis scripts, and known deviations.

**Falsifiers**

Users misunderstand the distinctions; the interface increases overreliance; correction quality is no better than baseline; cognitive load or task time offsets the benefit; accessibility barriers exclude intended users.

**Limitations**

Short laboratory tasks may not reproduce real stakes, organizational politics, tacit expertise, or evolving source landscapes. Self-reported trust is not decision quality.

**Possible venues or audiences**

Human-computer interaction and human information interaction audiences. Official descriptions position [ACM IUI](https://iui.acm.org/2026/call-for-papers/) at the AI–HCI intersection and call for evidence appropriate to claims; [ACM CHI](https://chi2026.acm.org/contributions-to-chi/) accepts several contribution forms but requires an original HCI contribution and appropriate validation; [ACM CHIIR](https://sigir.org/conferences/sponsored-conferences/) focuses on user-centered information interaction and retrieval. Fit and current calls must be rechecked at submission time.

**What cannot yet be claimed**

Usability, reduced overload, calibrated reliance, accessibility, faster correction, or improved human judgment.

## Candidate form 4: AI context/evidence architecture paper

**Central research question**

Does a provenance- and common-origin-aware context policy improve supported generation and appropriate abstention under matched retrieval and compute budgets?

**Plausible contribution**

A formal task definition, typed context/evidence representation, routing algorithm, benchmark with known derivations, and evaluation showing where origin-aware and multidimensional selection helps or fails.

**Prior-art burden**

Information retrieval, reranking, RAG, source-aware retrieval, claim verification, attribution, long-context use, value of information, active learning, agent memory, calibration, and adversarial retrieval or memory security. A generic “source-aware RAG” novelty claim is already untenable.

**Required empirical evidence**

Multiple model families or defensible scope restriction; ordinary RAG and strong reranker baselines; matched context, latency, and spend; ablations; repeated runs; uncertainty; contamination checks; adversarial common-origin and source-quality conditions.

**Possible hypotheses**

- H1: Origin-aware selection reduces false support from syndicated or copied sources.
- H2: Claim-level support plus separate authority improves supported-claim rate relative to document relevance alone.
- H3: A value-bounded router improves supported-claim yield per unit cost without reducing appropriate abstention.
- H4: Origin-bound memory reduces provenance laundering across summarization and reuse.

**Evaluation method**

Offline benchmark evaluation; controlled corpus perturbations; ablation; calibration analysis; cost and latency accounting; adversarial red-team cases; blinded human adjudication for outputs without reliable automatic labels.

**Potential datasets**

FEVER or SciFact for bounded claim/evidence behavior; a new provenance-rich corpus with explicit report-to-origin links; synthetic copied/coordinated variants; time-sliced collections for update and staleness. Reuse requires license and construct-fit review.

**Human-participant needs**

Expert annotators for claim decomposition, entailment, common origin, and action appropriateness; independent adjudication and measured agreement. End-user studies are optional only if the contribution stays computational.

**Ethics and privacy**

Respect dataset licenses and subject privacy; avoid amplifying harmful or defamatory content; document provider data use; prevent private prompts or outputs from entering released benchmarks; threat-model provenance manipulation.

**Reproducibility**

Release task definition, splits, provenance graph or generator, baselines, prompts, model and API snapshots, retrieval indexes, seeds, run counts, cost accounting, evaluation code, annotation guide, and error analysis. Report what cannot be reproduced when proprietary models are used.

**Falsifiers**

No benefit over strong retrieval/reranking baselines; gains vanish under matched tokens or spend; performance depends on leaked ground truth; common-origin detection suppresses genuine evidence; added provenance reduces neither errors nor correction effort.

**Limitations**

Benchmarks simplify open-world identity and authority; automated metrics can reward plausible unsupported output; provider and index drift impede exact replication; one domain cannot establish generality.

**Possible venues or audiences**

Information-retrieval, NLP, knowledge-management, and trustworthy-AI systems audiences. [ACM SIGIR](https://sigir.org/conferences/sponsored-conferences/) is a plausible audience only for a strong retrieval contribution; relevant NLP venues would require a clearly computational or evaluation contribution rather than a renamed systems essay.

**What cannot yet be claimed**

Improved factuality, provenance integrity, cost efficiency, generality, robustness, or protection from coordinated or memory-based attacks.

## Candidate form 5: empirical decision-support evaluation

**Central research question**

Under what conditions does the framework improve decision quality, correction, and evidence efficiency compared with ordinary research workflows?

**Plausible contribution**

Causal or carefully bounded comparative evidence about decision outcomes, mechanisms, costs, and heterogeneous effects by task, expertise, and stakes.

**Prior-art burden**

Decision support and decision quality, cognitive bias, automation bias, evidence-based management, information overload, organizational sensemaking, expertise, and the relevant application domain.

**Required empirical evidence**

Validated task and outcome measures; adequate sample and power justification; randomized or credible quasi-experimental comparison; matched resources; process measures; delayed or real outcomes where feasible; analysis of harms and subgroups.

**Possible hypotheses**

- H1: The framework improves blinded decision-quality ratings under equal research time.
- H2: It reduces unsupported high-consequence claims and time to correction.
- H3: Its benefits are greatest when sources are dependent or evidence is incomplete, and smallest for low-stakes familiar tasks.
- H4: Without progressive disclosure, its review overhead can outweigh its benefit.

**Evaluation method**

Preregistered controlled study followed, only if warranted, by a longitudinal field pilot. Compare ordinary search/bookmarking, strong cited RAG, and the candidate profiled evidence-selection responsibility. Use blinded outcome adjudication, mixed-effects or otherwise justified models, equivalence/non-inferiority tests where appropriate, and transparent missing-data analysis.

**Potential datasets**

Validated decision vignettes; historical decisions with time-bounded information and later outcomes; simulated but realistic evidence environments; prospective organizational tasks only with explicit permission and safeguards.

**Human-participant needs**

Representative decision makers or analysts, not convenience participants alone. Independent outcome raters; domain experts for consequential tasks; sufficient recruitment to estimate heterogeneity and avoid exaggerated pilot effects.

**Ethics and privacy**

Formal review as required; no consequential real-world decision delegated to an experimental system; protect employer, client, and source confidentiality; manage conflicts and participant power dynamics; monitor disparate errors and unsafe reliance.

**Reproducibility**

Preregistration, power rationale, tasks, randomization, conditions, stopping rule, measures, outcome rubric, analysis code, anonymized data or controlled-access plan, deviations, and full system versions.

**Falsifiers**

No decision-quality gain under matched resources; higher correction time, overload, or overreliance; gains exist only on contrived dependence cases; harms or disparate errors outweigh aggregate benefit; effects fail to replicate.

**Limitations**

Decision quality is domain- and time-dependent; observed outcomes may be noisy or delayed; organizational use adds incentives and constraints absent from experiments; causal attribution is hard in field deployments.

**Possible venues or audiences**

Decision-support, information-systems, HCI, and information-science audiences. Venue choice should follow the dominant contribution and method, not the project label; no specific venue should be selected before the study design and target population are fixed.

**What cannot yet be claimed**

Improved decisions, efficiency, safety, correction, overload reduction, return on investment, or field effectiveness.

## Candidate form 6: practitioner thought piece without academic positioning

**Central question**

What distinctions should practitioners preserve when deciding what context an AI system should acquire and allow to influence an answer?

**Plausible contribution**

A clear, source-aware vocabulary; visual framework; bounded examples; failure patterns; design questions; and practical review prompts that help teams reason about pre-generation context.

**Prior-art burden**

Accurate attribution to the established fields that supply the mechanisms; no suggestion that established concepts are new; transparent separation of owner premise, synthesis, case illustration, and hypothesis.

**Required empirical evidence**

No empirical study is required if the piece makes no effectiveness claim. Reader comprehension and expert fact-checking are still advisable before sharing, and every factual statement needs a source.

**Possible propositions to pose, not confirm**

- Treat context selection as an inspectable decision rather than an invisible prelude to generation.
- Keep authority, support, independence, relevance, and action separate.
- Preserve origin through enrichment and memory.
- Do not claim learning without an outcome and update rule.

**Evaluation method**

Source audit; adversarial editorial review; representative-reader restatement; terminology testing; accessibility, link, mobile, print, and PDF QA. Report feedback as editorial evidence, not scientific validation.

**Potential source material**

The cited primary literature, exact recovered v13 archive, bounded product artifacts, synthetic worked examples, and openly labeled design hypotheses.

**Human-participant needs**

No human-subject research. Informal reader feedback must not be presented as a study. Obtain permission before attributing or publishing a reader's feedback.

**Ethics and privacy**

No confidential examples; no sensitive-source disclosure; no protected-class use of the term “discrimination” without an explicit technical definition and exclusion; no product or person authority ratings that create unsupported reputational claims.

**Reproducibility**

Maintain the source register, bibliography, claim dispositions, exact product revisions, archived historical files, local site source, and export receipt. A thought piece can be auditable even when it is not experimental.

**Falsifiers or editorial rejection conditions**

Representative readers cannot restate the central idea; the terminology consistently communicates the wrong thesis; the piece implies novelty or validation it does not have; examples cannot be traced; the visual map collapses distinctions the prose claims to preserve.

**Limitations**

It can clarify a design problem but cannot establish scientific novelty, construct validity, usability, effectiveness, enterprise readiness, or generality.

**Possible venues or audiences**

AI product teams, research operations, knowledge-management practitioners, evidence-sensitive analysts, and informed general readers. A translational outlet such as ASIS&T's [Information Matters](https://www.asist.org/publications/) could be an audience only after editorial and attribution review. The current authorized destination is local owner review, not publication.

**What cannot yet be claimed**

Peer review; original scientific discovery; validated architecture; demonstrated product benefit; formal research contribution; safe deployment at scale.

## Proposed research program

The stages are cumulative gates, not a commitment to perform every study.

### Stage 0. Historical and claim reconciliation

- Preserve, hash, render, and inspect the exact v13 diagram; retain standalone-HTML recovery as an open source-completeness item.
- Trace each historical claim and term to its exact location.
- Reconcile the provisional component map without erasing differences.
- Convert every material v14 sentence into a claim-register row or explicitly non-claiming prose.

**Exit evidence:** immutable source manifest, v13 recovery memo, terminology receipt, clean claim lineage.

### Stage 1. Current-literature and claim-boundary lock

- Preserve the 2026 targeted-search protocol, inclusion rules, verified records, and negative/rival results.
- Treat HydraRAG, CONFACT, ProVe, ProvenanceGuard, CLUE, matched evidence-utilization work, BERGEN, DOS RAG, and PaperTrail as constraining precedents rather than peripheral citations.
- Keep the claim as F2-versus-F1 cue use; do not claim that the searched literature proves absolute novelty or exhaustive absence.
- If a systematic/scoping review is later needed for a broader paper, preregister it as a separate research artifact.

**Exit evidence:** current comparison matrix, verified bibliography, exact permitted-claim paragraph, and explicit stop/retire rules.

### Stage 2. Benchmark implementation and offline QA

- Implement the deterministic fictional generator, schemas, public/restricted manifests, prompt builder, strict parser, metric evaluator, power simulation, and replay tooling.
- Build 80 development bundles and 40 pilot bundles, blocking proposition and origin families across all splits.
- Require exact token parity, deterministic regeneration, semantic audit, surface-shortcut probes, relation-noise stress, and privacy/governance checks.
- Do not run or open the primary split during development.

**Exit evidence:** every pilot acceptance gate passes, with no efficacy interpretation.

### Stage 3. Preregistered origin-relation cue study

- Freeze 300 primary bundles, 60 stress bundles, model/tokenizer hashes, F0/F1/F2 prompts, parser, invalid-output policy, five-point candidate recall margin, power plan, and analysis code.
- Run the paired F2-versus-F1 false-corroboration comparison once under the preregistered stopping rule.
- Report fixed-set recall of stipulated supporting origins as the safety/non-inferiority endpoint and every invalid, null, harmful, formatting-only, or noise-fragile result.

**Exit evidence:** a bounded cue-use or negative result plus complete run, QA, and deviation records.

### Stage 4. Choose exactly one next study

- If the origin result is stable, select one: noisy relation inference; reader terminology/comprehension; a correction interface; a profiled acquire/hold/escalate policy; or origin-bound memory/security.
- Give that study its own unit, primary endpoint, baselines, burden, privacy model, accessibility plan, and stop criterion.
- Do not inherit efficacy from the oracle-cue benchmark.

**Exit evidence:** a separate protocol whose estimand is not rescued by adding every framework component.

### Stage 5. Controlled evaluation of the selected next study

- Fix primary outcomes, exclusion criteria, sample/power rationale, randomization, stopping, and analysis before results.
- Match time, tokens, retrieval access, and spend.
- Use ablations to test separate dimensions, common origin, provenance, stopping, and override.
- Report effect sizes, uncertainty, failures, costs, and negative results.

**Exit evidence:** preregistration, complete run ledger, results with uncertainty, independent outcome adjudication, replication package.

### Stage 6. Longitudinal field pilot

- Proceed only if controlled evidence supports value and safeguards.
- Use bounded, reversible, non-production or low-consequence workflows first.
- Measure correction, drift, learning, workarounds, organizational incentives, privacy, and real cost over time.
- Keep human authority explicit; do not let pilot participation authorize production decisions.

**Exit evidence:** field protocol, governance approval, longitudinal audit, harms and dropouts, evidence about transfer beyond laboratory tasks.

### Stage 7. Adversarial and cross-domain replication

- Test coordinated copying, source impersonation, provenance laundering, prompt injection, memory poisoning, selective silence, and delayed source changes.
- Replicate in a domain with different evidence standards and different investigators.

**Exit evidence:** threat-specific metrics, mitigations and residual risk, independent replication or a documented failure to transfer.

## Measurement framework

No single metric should stand in for the thesis.

| Construct | Candidate measures | Guardrail |
| --- | --- | --- |
| Claim quality | supported-claim rate; contradiction and insufficiency detection; evidence-span precision/recall | Fluency and citation count are not support. |
| Independence | common-origin precision/recall; false-corroboration rate; unknown-dependence retention | Do not reward calling uncertain reports independent. |
| Context selection | useful-evidence recall; irrelevant-context rate; material-exclusion error | More included context is not automatically better. |
| Routing | appropriate acquire/answer/hold/refuse rate; regret under defined utility; escalation precision | Utilities and harms must be explicit. |
| Stopping and cost | evidence gain per dollar/minute/token; latency; reviewer minutes; budget overrun | A cheap wrong answer is not efficient. |
| Auditability | provenance completeness; correction localization time; reproducibility of the evidence path | More fields are not automatically more usable. |
| Human judgment | decision accuracy or blinded quality rubric; calibrated reliance; correction success; workload | Self-reported trust is not quality. |
| Updating | calibration change; stale-memory retrieval; harmful update rate; rollback success | Outcome association is not causal proof. |
| Equity and safety | error and burden by relevant group; sensitive-data exposure; unauthorized action rate | Aggregate gains cannot hide concentrated harm. |

## Decision gates

- **Remain a thought piece** if the main value is conceptual clarity and representative readers can understand it, but no distinct research gap or evaluable artifact is yet established.
- **Become a systems framework** if v13 reconciliation, scoping review, and construct work produce a stable minimum architecture and bounded design principles.
- **Begin formal paper development** only after a primary research form, method, baseline, data path, ethics path, and falsifiers are selected.
- **Stop or substantially reframe** if a simpler prior framework subsumes the contribution, core constructs cannot be distinguished, the overhead lacks plausible benefit, or the terminology persistently causes material misunderstanding.

Venue names in this document identify possible audiences from current official scope pages. They are not submission recommendations, rankings, deadlines, or predictions of acceptance; fit must be reverified when a mature study exists.
