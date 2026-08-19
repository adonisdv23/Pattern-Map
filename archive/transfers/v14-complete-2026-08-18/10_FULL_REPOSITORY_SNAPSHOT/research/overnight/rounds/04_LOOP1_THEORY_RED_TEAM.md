# Round 1 theory red-team: adversarial novelty and terminology audit

Prepared 2026-08-18 for the Pattern Recognition / Discrimination Layer project.

## Scope and judgment standard

This memo red-teams the current **Paper prospectus v0**, **THOUGHT_PIECE_V14**, the targeted **prior-art map**, and the preceding theory memo. It is a bounded audit, not a systematic review or a patentability opinion. I searched and checked additional primary/authoritative sources where the current prospectus makes its narrowest claim: argument-based decision support, provenance verification, source-aware RAG, adaptive/agentic search, deep-research systems, human-facing claim/evidence provenance, memory, authorization/privacy, and RAG attack surfaces.

Labels:

- **[S] Sourced:** a claim directly supported by a linked paper, standard, or official research record.
- **[I] Inference:** a red-team conclusion drawn from the sources and project documents.
- **[H] Hypothesis:** a remaining contribution candidate that must be tested rather than asserted.

The prospectus is substantially more disciplined than the v14 thought piece: it explicitly says the intended paper is a minimal typed context-judgment policy, allows the policy to lose, names strong baselines and ablations, and renounces invention claims for most component families. The main remaining problem is not an explicit false claim so much as **semantic inflation**: a new label and a wide conjunction of familiar responsibilities can sound like a novel mechanism even after the manuscript says that each ingredient has prior art.

## Adversarial verdict

The narrow contribution survives only in the following constrained form:

> **A profiled, auditable action-policy contract that preserves typed evidence and source-dependence states and chooses among further acquisition, clarification, provisional use, abstention, escalation, or answer under an explicit resource/authorization envelope; evaluated against strong retrieve-and-read, source-aware RAG, provenance-only, claim-only, and human-review baselines on provenance-controlled tasks.**

Even this is a **composition, operationalization, and evaluation claim**, not a new mechanism family. The literature now contains close integrated systems that combine search, reasoning, graph memory, source/reliability weighting, evidence selection, claim–evidence interfaces, provenance verification, dynamic stopping, human intervention, and memory. The prospectus must not imply that no existing framework reaches the same responsibility merely because no one system uses the project’s exact field names.

Four findings should change the project’s posture:

1. **“Minimal” is currently indefensible.** The prospectus proposes a minimal typed policy but still carries most of C01–C11: brief/authorization, provenance, common-origin/dependence, claim/evidence graphs, multidimensional assessments, routing, packet receipts, human disposition, memory, and feedback. Until ablations demonstrate which fields are necessary and which are redundant, call it a **candidate compact policy** or **profiled policy**, not minimal.
2. **The closest prior art is broader than the current matrix.** Introne & Iandoli’s Pendo is an argument-based decision-support system that computes with evidence and reports improved decision performance; ProVe verifies claims against documented provenance; PaperTrail maps generated claims to source evidence and omissions and tests the human interface; Agentic Reasoning, Search-o1, and DeepResearcher integrate adaptive web search with structured context/memory; RA-RAG estimates source reliability; DOS RAG shows that simple source-faithful retrieval can beat elaborate pipelines under matched budgets. These sources collectively narrow the room for an “integrated policy” novelty claim.
3. **The distinct opportunity is a testable interface contract, not a box.** The project can still be distinct if it formalizes the typed state/action semantics, makes unknown dependence and authorization non-default states, and demonstrates an outcome benefit at matched resources. A graph, receipt, packet, memory ledger, or human owner is not independently novel.
4. **Terminology is not cosmetic.** “Discrimination layer” collides with protected-class discrimination, classifier/discriminator terminology, and minibatch discrimination. “Evidence-grounded decision,” “authority,” “independence,” “support,” “route receipt,” and even “context judgment” also carry field-specific meanings. The scientific title should use a functional name until a terminology study shows that the historical label is understood correctly.

## The narrow claim under hostile reading

The prospectus says the eventual paper may propose and evaluate:

> “A domain-profiled control contract that preserves source/artifact provenance and unknown dependence; separates claim support, scoped authority, relevance, and action consequence; and routes acquisition, clarification, provisional use, abstention, or escalation under declared budgets before generation or action.”

That sentence is promising but contains at least ten possible novelty claims. A hostile reviewer will parse it as follows:

| Phrase in the narrow claim | Hostile reading | Prior-art pressure | Safe disposition |
|---|---|---|---|
| **domain-profiled** | A schema whose semantics can be specialized to a task/domain rather than claiming universal truth. | Evidence ontologies, domain decision-support systems, clinical provenance, and multi-criteria decision analysis already profile semantics by domain. | Keep, but state the first domain profile and which fields are domain-specific. Do not present “domain-profiled” as a novel principle. |
| **control contract** | A runtime- and data-model contract that determines what enters a decision context and why. | PROV/data-lineage standards, event/audit logs, argument-based decision systems, mixed-initiative systems, and policy/access-control systems already use contracts, records, and control boundaries. | Potentially useful vocabulary; define pre/post conditions, invariants, actor authority, and failure semantics. A name alone is not a contribution. |
| **preserves source/artifact provenance** | Source identity, artifact/version identity, transformations, actors, timestamps, and lineage persist through retrieval, packaging, generation, and memory. | W3C PROV-O, nanopublications, ECO, data-lineage systems, ProVe, provenance verification, and evidence-synthesis audit trails. | Explicitly profile PROV-O or explain incompatibility. The contribution can be a tested preservation guarantee through the policy pipeline, not provenance itself. |
| **unknown dependence** | A source relationship can remain unresolved instead of being treated as independent or duplicate. | Claim-provenance work and evidence synthesis already show source grouping, common origin, and unresolved provenance; correlated-source fusion makes a graded dependence state necessary. | Keep as a typed state and evaluate its routing effect. Do not claim that the state concept is new. |
| **separates claim support** | Atomic claim-to-span support/contradiction/insufficiency is separate from source identity and relevance. | FEVER, SciFact, FActScore, SEE, Micropublications, ProVe, PaperTrail, GopherCite, ALCE, and general automated fact-checking pipelines. | Keep only as a typed composition and evaluation target; add an explicit comparison to claim-only and citation-only baselines. |
| **separates scoped authority** | A source is authoritative only for a bounded proposition class, role, or time period. | Source credibility/epistemic-vigilance work; source-reliability RAG; evidence-type ontologies; argument-based decision support; recent authority-bias work shows metadata can distort model reliance. | Define scope, bearer, time, jurisdiction, and evidence relation. Do not let “authority” become a hidden prior or a trust score. |
| **separates relevance** | Relevance to the current decision is not support, truth, or source quality. | Relevance feedback, information foraging, claim verification, provenance verification, and standard retrieval pipelines. | Keep as a semantic distinction, not a novelty claim. Test whether explicit separation changes action selection. |
| **separates action consequence** | The value/urgency of acquiring or inspecting a source is decision-specific and may differ from truth/support. | Value of information, metareasoning, influence diagrams, resource rationality, Pendo, adaptive search, and agentic search-control work. | Formalize the action utility/cost; avoid borrowing “VOI” for a qualitative score. |
| **routes acquisition/clarification/provisional/abstention/escalation** | The system decides whether to search, ask, hold, answer, or escalate before generating. | Information foraging and VOI; mixed initiative; Self-RAG, WebGPT, GopherCite, Search-o1, Search Wisely, DeepResearcher, and other agentic RAG systems. | The action vocabulary is a candidate policy surface. It is distinct only if the policy uses typed provenance/dependence/authorization states and improves matched-budget outcomes. |
| **under declared budgets** | The policy accounts for tokens, latency, money, disclosure, and human attention. | Information value, metareasoning, resource rationality, systematic-review search/stopping, DOS RAG budget comparisons, agentic search studies. | Keep as a constraint and evaluation factor. Report all resource types; no novelty inference from a budget field. |
| **before generation or action** | Evidence judgment is an explicit pre-generation stage. | RAG, WebGPT, Self-RAG, GopherCite, ALCE, Search-o1, Agentic Reasoning, DeepResearcher, and most evidence-grounded QA pipelines. | The timing is established. The contribution must be the typed policy and measurable downstream effect. |

[I1] The sentence is defensible only if “control contract” means a precisely specified **action policy plus typed state invariants**. If it means “a diagram that connects all the desirable pieces,” the claim is already covered by neighboring decision-support and agentic-research systems.

## Closest integrated frameworks that the prospectus must confront

### 1. Pendo: argument-based decision support with evidence weighting and outcomes

[S] Introne & Iandoli, “Improving Decision-Making Performance Through Argumentation: An Argument-Based Decision Support System to Compute with Evidence,” *Decision Support Systems* 64 (2014), DOI [10.1016/j.dss.2014.04.005](https://doi.org/10.1016/j.dss.2014.04.005), describes Pendo. Pendo distinguishes evidence from theory, represents questions/claims/pro/con structure, computes relative weights of competing claims under different evidence sets, and creates reusable knowledge artifacts. The reported study tested housing-market forecasting with an objective outcome and found improved mean performance for assisted participants, while also finding that unaided performance did not predict assisted performance.

[I2] Pendo is not the same system: it does not supply the project’s full provenance/dependence/authorization/memory contract. But it directly undermines any claim that the project is the first to connect evidence representation, claim comparison, computational weighting, decision support, reusable artifacts, and outcome evaluation. It also exposes a hidden design choice in the prospectus: if the typed dimensions are ultimately aggregated into an action/verdict, that aggregation is an argument/decision engine and must be compared with Pendo-like belief aggregation—not treated as a neutral routing step.

**Disposition:** must cite; use Pendo as a closest decision-outcome comparator and as a warning that the “typed policy” could replace rather than augment human reasoning.

### 2. ProVe: provenance verification already has evidence selection and support semantics

[S] Amaral, Rodrigues & Simperl, “ProVe: A Pipeline for Automated Provenance Verification of Knowledge Graphs Against Textual Sources,” *Semantic Web* (2024), DOI [10.3233/SW-233467](https://doi.org/10.3233/SW-233467), takes a knowledge-graph triple and its documented provenance, extracts passages, ranks/ selects evidence, classifies support/refute/neutral stance, and aggregates a support result. The paper explicitly distinguishes provenance support from truthfulness and describes evidence selection as a standard fact-checking subtask.

[I3] This is especially constraining for the prospectus’s “evidence cue” and “route receipt” unit. The cue-plus-source-support object is already an evaluated pipeline; what remains for the project is the **cross-source action policy** and its effect on a consequential decision, not the evidence cue itself. ProVe also offers a useful term—**verifiability**—that may be clearer than “evidence-grounded” when the claim is only that a source supports a recorded assertion.

**Disposition:** must cite; add as a direct comparator for claim/span/provenance verification and define the additional policy layer.

### 3. PaperTrail: claim–evidence provenance plus an actual human study

[S] Martin-Boyle et al., “PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A,” CHI 2026, DOI [10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101), decomposes source documents and generated answers into claims/evidence, maps support and omitted information, and evaluated the interface with 26 researchers. The authors report lower trust under PaperTrail but no corresponding behavioral change: users continued relying on LLM-generated scholarly edits because the task was cognitively burdensome.

[I4] PaperTrail is a near-direct challenge to the prospectus’s bounded packet, claim-evidence path, progressive disclosure, and human correction hypotheses. It shows that more granular provenance can change self-report without changing behavior. A future project study must therefore measure correction, inspection, omission detection, and reliance—not packet presence, trust, or perceived transparency.

**Disposition:** must cite; make it a human-interface baseline and explicitly state why the project’s route receipt differs from a claim-evidence provenance interface.

### 4. Agentic Reasoning: web search, tool selection, graph memory, and dynamic context

[S] Wu et al., “Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools,” ACL 2025, DOI [10.18653/v1/2025.acl-long.1383](https://doi.org/10.18653/v1/2025.acl-long.1383), dynamically invokes web search, code execution, and a Mind-Map agent; the Mind-Map stores reasoning context in a structured knowledge graph and tracks logical relationships. The authors report ablations on tool selection and memory.

[I5] This framework already has the skeleton of C02/C04/C07/C10: decide when to call a tool, retrieve external material, build a graph of context, and continue reasoning. It lacks the project’s explicit source-dependence, authority/support separation, authorization envelope, owner disposition, and immutable evidence semantics. Those gaps are useful boundaries, but “web search + structured graph memory + adaptive tool choice” cannot be claimed as the project’s integrated novelty.

**Disposition:** must cite for the current AI-systems frontier; use as a baseline even if the project is not a neural agent paper.

### 5. Search-o1 and DeepResearcher: dynamic search and evidence refinement are already active

[S] Li et al., “Search-o1: Agentic Search-Enhanced Large Reasoning Models,” EMNLP 2025, DOI [10.18653/v1/2025.emnlp-main.276](https://doi.org/10.18653/v1/2025.emnlp-main.276), invokes search when uncertain and uses a separate Reason-in-Documents module to analyze retrieved documents before injecting them into the reasoning chain. [S] Zheng et al., “DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments,” EMNLP 2025, DOI [10.18653/v1/2025.emnlp-main.22](https://doi.org/10.18653/v1/2025.emnlp-main.22), trains agents to navigate the open web, with reported planning, cross-validation, self-reflection, research redirection, and honesty when no definitive answer is found. Its implementation includes a browsing loop that decides whether to continue reading or stop and retains a short-term memory for each query.

[I6] These systems are not provenance-governed in the project’s sense, and their learned policies do not expose an owner/authorization/typed-assessment contract. Nevertheless, they already implement the claimed pre-generation behaviors: uncertainty-triggered acquisition, document analysis before injection, cross-validation, stop decisions, and provisional non-answer. The project must compare against them conceptually and, where feasible, by replaying their traces or adopting their action baselines.

**Disposition:** must cite both for any statement about pre-generation routing, dynamic acquisition, or “deep research.”

### 6. Search Wisely: over-search/under-search are now measured policy errors

[S] Wu et al., “Search Wisely: Mitigating Sub-optimal Agentic Searches by Reducing Uncertainty,” EMNLP 2025, DOI [10.18653/v1/2025.emnlp-main.998](https://doi.org/10.18653/v1/2025.emnlp-main.998), formally defines over-search and under-search, measures them across QA datasets and agentic RAG systems, and trains a confidence-threshold policy that reduced these behaviors and improved benchmark scores.

[I7] This materially narrows the prospectus’s route/stopping contribution. The project can still add source-dependence and consequence-sensitive routing, but it cannot present “search/stop/hold under cost” as an unoccupied problem. The crucial comparison is not whether the project routes; it is whether typed provenance/dependence/authorization improves search-decision quality beyond uncertainty/confidence-based policies at equal resource cost.

**Disposition:** must cite; add as the primary current search-policy baseline.

### 7. RA-RAG: source reliability is already used for selection and aggregation

[S] Hwang et al., “Retrieval-Augmented Generation with Estimation of Source Reliability,” EMNLP 2025, DOI [10.18653/v1/2025.emnlp-main.1738](https://doi.org/10.18653/v1/2025.emnlp-main.1738), estimates source reliability by cross-checking multiple sources, selects reliable and relevant documents, and aggregates source-specific responses using weighted majority voting.

[I8] RA-RAG is not the project’s full vector of authority/support/relevance/dependence/action consequence. It is, however, a direct counterexample to a novelty claim that conventional RAG only ranks relevance while the proposed policy considers source quality. The project’s possible distinction is to reject RA-RAG’s implicit collapse of source reliability into a weight by preserving typed, scoped, uncertain relations and handling dependence rather than treating cross-source agreement as reliability. That distinction must be implemented and tested; it cannot be claimed from a schema.

**Disposition:** must cite; make RA-RAG a one-score/reliability-aggregation comparator and include correlated-copy adversaries.

### 8. DOS RAG: simple source-faithful retrieval can beat added architecture

[S] Laitenberger, Manning & Liu, “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models,” EMNLP 2025, DOI [10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656), reports that a simple Document’s Original Structure RAG baseline consistently matched or outperformed more elaborate multi-stage systems on tested long-context QA benchmarks. The authors recommend matched-token-budget comparisons before adding pipeline complexity.

[I9] This is a direct adversarial test for the prospectus’s “minimal typed policy” and route-receipt overhead. If a simple source-faithful retrieve-then-read system matches the proposed system on the target task, the project must claim a narrower governance/inspection benefit—or accept a negative mechanism result. The baseline must be included before any architecture claim is credible.

**Disposition:** must cite; require DOS RAG or a functionally equivalent strong baseline in A2.

### 9. A-Mem: adaptive linked memory and memory evolution are not new

[S] Xu et al., “A-Mem: Agentic Memory for LLM Agents,” NeurIPS 2025, DOI [10.52202/085713-0593](https://doi.org/10.52202/085713-0593), dynamically indexes and links memories, updates contextual representations as new memories arrive, and reports experiments against memory baselines.

[I10] C10’s linked memory, evolution, and context-sensitive reuse are already active agent-memory mechanisms. The project can distinguish itself only by making memory **origin-bound, authorization-aware, version-preserving, and outcome-governed**, then testing stale/error propagation and rollback. “Versioned memory” alone is a standard audit design, not a new contribution.

**Disposition:** must cite; narrow C10 to provenance-preserving memory safety and evaluate it.

### 10. S-RAG and memory/privacy work: authorization is an adversarial security problem

[S] Zeng et al., “S-RAG: A Novel Audit Framework for Detecting Unauthorized Use of Personal Data in RAG Systems,” ACL 2025, DOI [10.18653/v1/2025.acl-long.512](https://doi.org/10.18653/v1/2025.acl-long.512), audits whether personal text was used by black-box RAG systems. [S] Wang et al., “Unveiling Privacy Risks in LLM Agent Memory,” ACL 2025, DOI [10.18653/v1/2025.acl-long.1227](https://doi.org/10.18653/v1/2025.acl-long.1227), demonstrates a memory-extraction attack against private user-agent interactions.

[I11] The prospectus’s authorization envelope and immutable ledger are not sufficient security claims. Authorization needs an enforcement point, data-use purpose, retention/erasure policy, disclosure boundary, and attack evaluation. A receipt that records unauthorized acquisition after the fact is an audit artifact, not authorization control.

**Disposition:** must cite for C01/C03/C10; add a threat model and distinguish *policy declaration*, *enforcement*, and *post hoc audit*.

### 11. RAG Paradox and attribution bias: visibility can create new attack/bias channels

[S] Choi et al., “The RAG Paradox,” Findings of EMNLP 2025, DOI [10.18653/v1/2025.findings-emnlp.1291](https://doi.org/10.18653/v1/2025.findings-emnlp.1291), shows how revealing retrieved documents and sources can let attackers craft poisoned documents that are more likely to be retrieved and trusted. [S] Abolghasemi et al., “Evaluation of Attribution Bias in Generator-Aware RAG,” Findings of ACL 2025, DOI [10.18653/v1/2025.findings-acl.1087](https://doi.org/10.18653/v1/2025.findings-acl.1087), finds that authorship metadata can change attribution quality and induce a human-authorship bias. [S] Li et al., “LLMs Trust Humans More, That’s a Problem!” ACL 2025, DOI [10.18653/v1/2025.acl-long.1400](https://doi.org/10.18653/v1/2025.acl-long.1400), identifies an authority-bias phenomenon and uses atomic conflict detection and credibility assessment as mitigation.

[I12] The project currently treats visible provenance, scoped authority, source identity, and owner review as safeguards. These sources make them **dual-use controls**: visibility can support correction but also enable poisoning; authority metadata can guide inspection but also launder institutional bias; citations can increase confidence without improving behavior. The evaluation must include source poisoning, authority metadata counterfactuals, and an attack where the route receipt itself becomes a targeting signal.

**Disposition:** must cite for the transparency, authority, and provenance-risk sections; reject any unqualified claim that inspectability increases trustworthiness.

## Hidden reinvention audit

The project’s careful caveats do not prevent a reviewer from seeing the following as established constructs under new names.

| Project term/feature | Existing construct(s) it may be renaming | Red-team concern | Distinctive test if retained |
|---|---|---|---|
| **Evidence cue** | Evidence span, sentence selection, rationale, quote support, nanopublication assertion | ProVe, FEVER, GopherCite, ALCE, PaperTrail already select or expose claim-level evidence. | Show that adding a cue to a **route receipt** improves an action or correction outcome over the same span/citation without the receipt. |
| **Route receipt** | Audit log, provenance record, selection manifest, search trajectory, event-sourcing record, Cochrane inclusion/exclusion log | New noun for an old record; “receipt” can imply accountability without enforcement. | Define immutable fields and an invariant that permits independent replay; test replay/correction/authorization detection, not receipt readability alone. |
| **Evidence spine** | Data lineage, PROV graph, artifact registry, provenance chain | Standards already describe the underlying entities/activities/agents/derivations. | Demonstrate preservation through normalization, packet compression, model invocation, and memory reuse; profile PROV-O. |
| **Unknown dependence** | Missing/unresolved provenance, correlated-source uncertainty, study/report grouping, unknown provenance state | The state is sensible but not original; treating unknown as independent is a known error. | A controlled copied/syndicated/independent/unknown benchmark plus an action-policy ablation. |
| **Typed assessments** | Multi-criteria decision analysis, argument weights, source/claim credibility, evidence ontology, reliability vectors | “Separate fields” can be a schema restatement of MCDM or source-reliability weighting; fields may be correlated or not ratable. | Discriminant validity, crossed-case reliability, incremental action utility, and comparison to one-score and latent-trust models. |
| **Scoped authority** | Domain authority, source credibility, institutional role, authorship metadata | Authority is both a human and model bias channel; it can be a hidden prior. | Counterfactual metadata test; authority must be relation- and time-scoped and never substitute for claim support. |
| **Relevance vs support** | Relevance feedback vs entailment/stance; fact-checking pipeline stages | This is already a basic distinction in information retrieval and automated fact checking. | Test whether exposing the distinction changes selection under adversarial lexical overlap. |
| **Action consequence** | Utility, risk, decision priority, VOI, metareasoning, resource rationality | A consequence field without a utility model may be a vague urgency label. | Predeclare decision outcomes/harms and compare policy regret/net utility. |
| **Two loops** | Sensemaking/foraging loops; organizational learning; iterative search and cross-task memory | The distinction is useful, but not a mechanism claim. | Prove an audit invariant: within-task search cannot silently update cross-task policy; test rollback and temporal leakage. |
| **Bounded context packet** | Evidence set, cited answer, nanopublication, claim-evidence interface, selected context window | The packet contents are established piecemeal. | Compare packet variants on correction, omission, and exposure; include PaperTrail and DOS RAG baselines. |
| **Human disposition** | Mixed initiative, appropriate reliance, cognitive forcing, argument-based decision support | Human presence is not correction; Pendo and PaperTrail show tool-mediated performance/behavior effects can diverge. | Measure actual evidence inspection, error detection, override quality, burden, and subgroup differences. |
| **Versioned memory ledger** | Organizational memory, event sourcing, provenance, agent memory, append-only audit | Versioning/retention is a governance pattern; A-Mem shows adaptive linked memory. | Test stale reuse, provenance laundering, privacy leakage, rollback, and valid new-evidence discovery. |
| **Outcome link** | Calibration, decision-support outcome evaluation, organizational learning, Pendo reusable artifacts | An outcome record does not establish that an evidence path caused the outcome. | Predefine exposure, outcome, horizon, confounders, policy version, and no-update/rollback decision. |
| **Discrimination policy** | Retrieval policy, decision policy, evidence admission, source selection, selective prediction | The noun suggests a new layer while the behavior is a policy over evidence. | Rename to an action-policy or evidence-admission policy unless terminology study proves otherwise. |

[I13] The hidden-reinvention problem is not fatal. Many fields use integration contributions. It changes the paper’s burden: the paper must make its **composition boundary** and **invariants** the object of study, and show why existing composition patterns do not already meet the same requirements.

## Claim-by-claim dispositions for prospectus and site language

| Current or implied claim | Red-team status | Required disposition |
|---|---|---|
| “Retrieval helps find material, provenance traces it, claim verification tests propositions, but no single one answers the whole pre-generation question.” | **Too broad as written.** It is plausible for the named canonical systems but not established against current integrated agentic research and decision-support systems. | Replace with: “The reviewed systems optimize different subsets of this responsibility; we test whether a particular typed composition adds value.” Add the comparison matrix and search protocol. |
| “The smallest useful unit is an evidence cue plus route receipt.” | **Unsupported universal.** A document, claim, observation, argument, or decision may be the useful unit depending on task; existing systems already use evidence spans plus provenance. | Say “the smallest unit proposed for this study” and test it against document, claim-only, citation-only, and packet units. |
| “Minimal typed context-judgment policy.” | **Overclaim.** No minimality result; many dimensions remain. | Change to “candidate compact typed policy” until the ablation gate selects a subset. If no subset wins, publish a construct/benchmark paper. |
| “Domain-profiled control contract.” | **Plausible but underspecified.** Could be MCDM/argumentation/decision-support plus provenance. | Provide a formal contract: state types, legal transitions, authorization enforcement, route receipt schema, and replay invariants. State what is not covered. |
| “Unknown dependence is preserved.” | **Potentially distinct only at the end-to-end boundary.** Existing work models unresolved provenance; current agentic systems often do not expose it. | Make this the centerpiece of a narrow benchmark/policy paper, not one field in a universal stack. Use `unknown_origin/dependence` as a first-class outcome and test its cost. |
| “Typed claim/evidence paths improve evidence-grounded success.” | **Testable, not established.** ProVe, PaperTrail, and claim-verification systems show components; no project result yet. | Keep as a hypothesis. Define acceptable path independently of answer correctness and pre-register the conjunctive endpoint. |
| “A route chooses answer/hold/refuse/escalate.” | **Established policy family.** Search Wisely, Self-RAG, WebGPT, GopherCite, DeepResearcher, and mixed initiative already choose when/what to retrieve or abstain. | Claim a source-dependence/authorization-aware policy, not routing itself. Include learned and heuristic policy baselines. |
| “Visible exclusions and provenance improve correction.” | **Open and risky.** PaperTrail reduced trust but did not change reliance; RAG Paradox shows transparency can aid poisoning. | Keep as a bidirectional hypothesis with correction and attack endpoints. Do not use “auditability” as a proxy for safety. |
| “Outcome feedback should revise policy.” | **Established conceptual pattern; causal benefit unknown.** Organizational learning, calibration, Pendo, and agent memory already address update. | Define a safe update protocol and test it against no-update, naive-update, and provenance-governed-update conditions. |
| “The framework scales down or disappears for low-dependence tasks.” | **Good boundary claim, not evidence.** It is a design expectation. | Make C7 a negative-control class and report overhead/negative value. This is one of the strongest anti-bureaucracy tests. |
| “Discrimination layer” is a technical differentiation/selection responsibility. | **Terminologically hazardous.** Explanation may not neutralize the ordinary/legal/ML meanings. | Scientific title should use “evidence-selection and action policy” or similar until H8 passes. Keep historical label as a provenance note, not the main claim. |

## What could still be distinct, if anything?

The following are credible **candidate contributions**, ordered from strongest to weakest. None is established by the current materials.

### A. Unknown-dependence-aware action policy under matched budgets

[H1] Given a provenance-controlled corpus with independent, copied, syndicated, common-process, contradictory, stale, and unknown-origin reports, a policy that preserves dependence states and uses them to choose `compare/acquire/hold/answer` improves false-corroboration safety and decision utility over (a) relevance-only RAG, (b) source-reliability weighting, (c) document-count consensus, and (d) claim-only verification, at equal retrieval/review cost.

Why this may remain distinct: existing claim-provenance work identifies origin and support; RA-RAG weights reliability; agentic systems search and stop. The proposed experiment would test the **joint action consequence** of explicitly preserving unknown dependence rather than silently collapsing it.

What would falsify it: no gain over source-reliability or strong retrieve-and-read baselines; large loss of valid independent convergence; or metadata/graph construction cost that exceeds utility.

### B. A typed contract with measurable invariants, not a feature checklist

[H2] The project can contribute a machine- or human-executable contract with invariants such as:

- provenance edges cannot imply truth/support;
- unknown origin cannot be counted as independent;
- no unauthorized source/tool/action can enter a packet;
- a packet cannot omit the reason for an exclusion or stop;
- a human disposition cannot rewrite immutable observations;
- an outcome cannot update a policy without a versioned, scoped proposal;
- a claim cannot be marked supported without a claim-specific evidence path.

Why this may remain distinct: prior systems cover individual invariants, but the exact **cross-stage composition** may be a useful artifact if formally specified and replay-tested.

What would falsify it: the invariants are merely restatements of PROV/access-control/event-sourcing semantics; or an existing system satisfies them after ordinary configuration.

### C. A provenance–action evaluation metric/benchmark

[H3] Define an evidence-grounded decision path as a conjunction of (i) correct/appropriate action, (ii) claim-specific support or explicit insufficiency, (iii) dependence-aware source accounting, (iv) authorization compliance, and (v) replayable selection receipt. Evaluate this path under controlled adversarial source graphs and costs.

Why this may remain distinct: current benchmarks usually score retrieval/evidence/verdict/citation separately and do not make action/authorization/provenance jointly necessary. The contribution would be a benchmark/metric, not a new reasoning mechanism.

What would falsify it: reviewers cannot agree on path quality; the conjunction is too brittle to reflect useful performance; or it simply reproduces existing FEVER/ALCE/ProVe metrics under new names.

### D. Human correction through progressive evidence and route disclosure

[H4] A progressive interface that shows a compact claim/evidence/dependence cue first, then provenance/exclusions/uncertainty on demand, improves seeded-error localization and appropriate correction at lower burden than a full graph or citation-only interface.

Why this may remain distinct: PaperTrail shows a real claim-evidence provenance interface can change trust without behavior. The project could contribute an interaction result if it tests progressive disclosure, unknown dependence, exclusions, and route rationale.

What would falsify it: no correction improvement; greater automation bias; or PaperTrail-style cognitive burden.

### E. Origin-bound memory and rollback

[H5] Memory that retains source/artifact/claim origin and policy version across summarization/reuse reduces provenance laundering and stale reuse without suppressing valid exploration.

Why this may remain distinct: A-Mem and organizational-memory work address linked/evolving memory, while memory privacy/security work exposes risk. An origin-preservation and rollback benchmark could be useful.

What would falsify it: lineage-aware memory has no benefit, adds unacceptable burden, leaks more information, or suppresses discovery.

### Not distinct enough to lead a paper

[I14] The following should not be lead contributions: “evidence before generation,” “a bounded context packet,” “a provenance spine,” “claim/evidence graphs,” “source-aware selection,” “human disposition,” “versioned memory,” “route receipts,” or the visual six-family decomposition. They can be components, requirements, or explanatory devices, but each is already strongly prefigured by prior systems.

## Terminology and construct collision audit

### “Discrimination layer”

[I15] The exact intended phrase did not emerge as a stable cross-disciplinary term in the bounded search. That is not evidence of absence. The search did surface established collisions:

- **Legal/social:** discrimination commonly denotes unequal treatment or protected-class harm; a technical disclaimer may not overcome the title-level reading.
- **Machine learning:** discriminator/discriminative layer suggests a classifier or a GAN discriminator; “minibatch discrimination” is an established GAN term.
- **Network/systems:** application or traffic discrimination suggests protocol treatment or filtering.
- **Statistics/IR:** discrimination can mean separability or ranking ability, which is different from evidence admission and governance.

The collision is especially costly because the manuscript uses “pattern recognition,” “source authority,” “selection,” and “sensitive evidence” nearby. A reader may infer a fairness or classifier paper, then treat the later disclaimer as a redefinition.

**Disposition:** use a functional scientific title: **Evidence Before Generation: A Typed Evidence-Selection and Action Policy** or **From Retrieval to Disposition: Provenance-Aware Context Judgment Under Cost**. Retain “Pattern Recognition / The Discrimination Layer” only as historical lineage in the site/thought-piece metadata until the terminology study passes.

### “Context judgment”

This is safer than “discrimination” but still ambiguous with context-window selection, context engineering, prompt compression, and model attention. Define it as a policy over evidence/state/actions, not a judgment made by the generator. A title using “evidence-selection” is more searchable and less likely to be mistaken for generic context-window work.

### “Evidence-grounded decision”

Grounded can mean retrieved, cited, entailed, supported, provenance-linked, or causally justified. The prospectus uses all of these boundaries. Replace with one of:

- **claim-supported action** when claim-specific support is the endpoint;
- **provenance- and authorization-compliant action** when governance is the endpoint;
- **evidence-path-valid action** when the project explicitly defines a conjunctive path metric.

Do not write “grounded” without an operational definition.

### “Independence” and “dependence”

These terms invite statistical/causal interpretations. The project generally means **source-origin independence** or **provenance dependence**, not probabilistic independence. Use `origin relation: independent / dependent(type, scope) / unknown` and say that the label is epistemic/operational, not a causal claim.

### “Authority”

Authority can mean institutional role, legal jurisdiction, expertise, authorship, source reputation, or user preference. Use **scoped source authority** with a proposition class, jurisdiction, time, and bearer. Keep it separate from support, reliability, truth, and permission. Cite the 2025 authority-bias work as a reason to test metadata effects.

### “Support”

Support can mean textual entailment, evidentiary weight, causal support, practical usefulness, or rhetorical backing. Define `supports(claim, span, scope, relation_type, confidence)` and include `refutes`, `qualifies`, `insufficient`, and `unknown`. Avoid “supported” as a synonym for true.

### “Route receipt”

This is memorable but nonstandard. It can remain a project term only if the paper defines the receipt as an append-only **selection-and-action audit record** with a replay test. Otherwise use “routing audit record” or “selection manifest.” Avoid implying that a receipt proves authorization or correctness.

## Must-cite work added in this loop

These are not optional embellishments if the prospectus or eventual paper retains its current scope:

| Work | Why it is a must-cite | Direct source |
|---|---|---|
| Introne & Iandoli (2014), Pendo | Argument-based decision support computes evidence weights, supports competing claims, creates reusable artifacts, and reports decision outcomes. | [DOI 10.1016/j.dss.2014.04.005](https://doi.org/10.1016/j.dss.2014.04.005) |
| Amaral, Rodrigues & Simperl (2024), ProVe | Evidence selection and claim support verification against documented provenance; directly separates support from truth. | [DOI 10.3233/SW-233467](https://doi.org/10.3233/SW-233467) |
| Wu et al. (2025), Agentic Reasoning | Dynamic web search, tool selection, structured graph memory, and iterative reasoning. | [DOI 10.18653/v1/2025.acl-long.1383](https://doi.org/10.18653/v1/2025.acl-long.1383) |
| Li et al. (2025), Search-o1 | Uncertainty-triggered search and document refinement before injection into reasoning. | [DOI 10.18653/v1/2025.emnlp-main.276](https://doi.org/10.18653/v1/2025.emnlp-main.276) |
| Zheng et al. (2025), DeepResearcher | Open-web browsing, stopping/short-term memory, planning, cross-validation, redirection, and non-definitive-answer behavior. | [DOI 10.18653/v1/2025.emnlp-main.22](https://doi.org/10.18653/v1/2025.emnlp-main.22) |
| Wu et al. (2025), Search Wisely | Formal over-search/under-search errors and a learned search decision policy. | [DOI 10.18653/v1/2025.emnlp-main.998](https://doi.org/10.18653/v1/2025.emnlp-main.998) |
| Hwang et al. (2025), RA-RAG | Source reliability estimation and reliability/relevance-based retrieval/aggregation. | [DOI 10.18653/v1/2025.emnlp-main.1738](https://doi.org/10.18653/v1/2025.emnlp-main.1738) |
| Laitenberger, Manning & Liu (2025), DOS RAG | Strong simple source-faithful baseline; matched-budget complexity warning. | [DOI 10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656) |
| Xu et al. (2025), A-Mem | Dynamic linked memory and memory evolution. | [DOI 10.52202/085713-0593](https://doi.org/10.52202/085713-0593) |
| Zeng et al. (2025), S-RAG | Authorization/privacy audit for RAG data use; source-use provenance is a security issue. | [DOI 10.18653/v1/2025.acl-long.512](https://doi.org/10.18653/v1/2025.acl-long.512) |
| Martin-Boyle et al. (2026), PaperTrail | Claim–evidence provenance interface, omissions, and a human behavior study. | [DOI 10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101) |
| Choi et al. (2025), RAG Paradox | Source/citation transparency can expose systems to poisoning. | [DOI 10.18653/v1/2025.findings-emnlp.1291](https://doi.org/10.18653/v1/2025.findings-emnlp.1291) |
| Abolghasemi et al. (2025), Attribution Bias | Authorship metadata affects attribution and trust. | [DOI 10.18653/v1/2025.findings-acl.1087](https://doi.org/10.18653/v1/2025.findings-acl.1087) |
| Li et al. (2025), Authority Bias | Atomic conflict/credibility assessment and source-authority bias in RAG. | [DOI 10.18653/v1/2025.acl-long.1400](https://doi.org/10.18653/v1/2025.acl-long.1400) |
| Wang et al. (2025), Memory Privacy | Memory extraction attack; C10 needs privacy threat modeling. | [DOI 10.18653/v1/2025.acl-long.1227](https://doi.org/10.18653/v1/2025.acl-long.1227) |

The prior memo’s existing citations remain necessary: Pirolli & Card, Howard, Russell & Wefald, Kamar & Horvitz, Golovin & Krause, W3C PROV-O, SEE, Micropublications, Zhang et al. claim provenance, Pochampally et al. source correlations, FEVER/SciFact/FActScore, RAG/Self-RAG/WebGPT/GopherCite/ALCE, Parasuraman & Riley, Lee & See, Buçinca, Bansal, Walsh & Ungson, Crossan et al., Argote & Miron-Spektor, March, Sperber et al., Metzger, Cochrane, and PRISMA.

## Adversarial evaluation requirements

The current prospectus already specifies A0–A6 and many measures. The following additions are necessary to prevent a false positive for “integration benefit.”

### Baseline requirements

At minimum, A2/A5 comparisons should include:

1. DOS RAG or an equivalent simple source-faithful retrieve-then-read system under scaled/matched token budgets.
2. Self-RAG/Search-o1/agentic-search-like adaptive retrieval or a faithful trace-replay surrogate.
3. RA-RAG-like source reliability weighting with weighted aggregation.
4. ProVe-like claim/span support verification when a documented provenance source is available.
5. Pendo-like argument/evidence weighting or a transparent claim/pro-con aggregation baseline for decision tasks.
6. PaperTrail-like claim-evidence interface for human correction.
7. A deliberately non-graph receipt-only control to test whether metadata creates the appearance of rigor without benefit.

### Adversarial source families

- copied and paraphrased reports with known origin;
- independent reports that converge on the same claim;
- common-process reports that do not copy text;
- authoritative-but-irrelevant sources;
- low-authority but decisive evidence;
- user-provided false text conflicting with retrieved evidence (authority-bias test);
- source metadata swaps (human/organization/anonymous) with content held constant;
- poisoned sources that exploit visible retrieval/citation behavior;
- stale versions and superseding corrections;
- inaccessible or expected-but-missing perspectives;
- unauthorized/private artifacts and memory extraction attempts;
- low-dependence controls where the full policy should add little or negative value.

### Primary endpoints

Do not let citation coverage or model confidence carry the argument. Use a pre-registered endpoint that combines:

- correct or appropriate action/verdict;
- claim-specific support/contradiction/insufficiency;
- origin/dependence accounting;
- authorization compliance;
- cost and review burden;
- correction or abstention quality;
- replayability of the route receipt.

Report component metrics separately so a failure at provenance extraction cannot be hidden by a correct final answer.

### Complexity tax

[H6] The strongest general hypothesis may be **conditional value**, not universal improvement: the typed policy helps mainly when dependence, contradiction, missingness, temporal change, or consequence asymmetry is high, and its cost dominates on simple/low-dependence controls. Pre-register the interaction and report the policy’s break-even point. If no conditional interaction appears, retire the “decision-sensitive layer” framing and narrow to a specific mechanism or benchmark.

## Concrete manuscript and site dispositions

### Must change before a paper or scientific landing page

1. Replace “minimal” with “candidate compact” or “profiled” until the feature-minimality gate is passed.
2. Replace “no single one answers the whole pre-generation question” with a bounded statement tied to a protocol-led search and a feature matrix.
3. Add all must-cite works in the previous table, especially Pendo, ProVe, PaperTrail, Agentic Reasoning, Search-o1, DeepResearcher, Search Wisely, RA-RAG, DOS RAG, A-Mem, S-RAG, RAG Paradox, Authority Bias, Attribution Bias, and Memory Privacy.
4. Change the scientific title to a functional label: **Evidence Before Generation: A Typed Evidence-Selection and Action Policy** or **From Retrieval to Disposition: Provenance-Aware Context Judgment Under Cost**.
5. Define “evidence-grounded,” “support,” “authority,” “origin dependence,” “independence,” “route receipt,” “action consequence,” and “minimal” in a glossary and in the evaluation protocol.
6. State whether authorization is enforced, merely declared, or audited after the fact. Add a threat model for unauthorized retrieval, memory leakage, and source poisoning.
7. Add a Pendo-like decision-support comparator and a PaperTrail-like human-interface comparator.
8. Require the A2 DOS RAG baseline and matched-resource accounting in the headline experiment.
9. Make the title/abstract’s primary claim conditional: improve **under source dependence/contradiction/missingness/cost**, not improve “evidence-grounded decisions” generally.
10. Treat visible provenance/exclusions as dual-use: evaluate correction and poisoning, not only transparency/trust.

### Optional but high-value

1. Use “verifiability” for whether a source supports a recorded claim and reserve “truth” for a separately evaluated task.
2. Add a formal relation to PROV-O, ECO, Toulmin, and Pendo rather than presenting an independent vocabulary.
3. Release a provenance-controlled generator, origin-family splits, route-receipt schema, and replay checker as the first durable artifact.
4. Add a counterfactual source-metadata condition for authority and authorship bias.
5. Include a human comprehension/rename study before freezing the historical label.
6. Report a break-even complexity curve showing when graph/receipt/review cost is justified.
7. Add a “policy versus representation” table: which fields influence runtime decisions, which are only for audit, and which are only for human display.
8. Compare immutable event/ledger semantics to an ordinary append-only audit log; do not imply that versioning alone preserves epistemic status.

### Reject or defer

1. Reject “the discrimination layer is a novel mechanism” unless a new algorithm/theorem is actually supplied.
2. Reject “no prior framework combines these responsibilities” without a registered systematic review and feature-level evidence.
3. Reject “human disposition makes the system correctable/safe” without behavior and workload results.
4. Reject citation count, fluency, trust, or model confidence as primary evidence of success.
5. Defer universal cross-domain claims until a second-domain/adversarial replication succeeds.
6. Reject the idea that `route receipt`, `evidence cue`, or `evidence spine` is sufficient novelty by itself.
7. Reject a universal penalty for recurrence/common origin; preserve graded uncertainty and test valid convergence loss.
8. Reject silent policy updates from downstream outcomes; require scoped, reviewed, versioned proposals and rollback.

## Compact must-change / optional / reject table

| Priority | Change | Rationale |
|---|---|---|
| **Must change** | Rename the scientific title and avoid leading with “discrimination layer.” | Collision with social/legal discrimination, ML discriminators, and network discrimination; reader comprehension is not established. |
| **Must change** | Replace “minimal” with “candidate compact/profiled” until ablations establish minimality. | Current C01–C11 composition is not minimal or construct-validated. |
| **Must change** | Add Pendo, ProVe, PaperTrail, Agentic Reasoning, Search-o1, DeepResearcher, Search Wisely, RA-RAG, DOS RAG, A-Mem, S-RAG, RAG Paradox, Authority Bias, Attribution Bias, and Memory Privacy. | These are direct integrated or adversarial precedents that narrow the contribution. |
| **Must change** | Define and enforce the difference between policy declaration, authorization enforcement, and audit. | A receipt after unauthorized acquisition is not a control; S-RAG and memory-privacy work make this material. |
| **Must change** | Add DOS RAG, RA-RAG, adaptive search, Pendo-like weighting, and PaperTrail-like interface baselines. | Prevents architecture complexity from masquerading as mechanism value. |
| **Must change** | Make the contribution conditional on dependence/contradiction/missingness/cost and pre-register the interaction. | A universal benefit claim is not supported and likely false. |
| **Must change** | Use a defined path endpoint: action/verdict + support/insufficiency + dependence + authorization + cost/replay. | “Evidence-grounded” is underspecified and conflates several outcomes. |
| **Optional** | Use “verifiability” for source support, and map lineage to PROV-O/ECO/Toulmin/Pendo. | Improves semantic precision and interoperability. |
| **Optional** | Add source-metadata counterfactuals, visible-receipt poisoning, and memory extraction tests. | Converts current risk observations into publishable adversarial results. |
| **Optional** | Publish a provenance-controlled generator, route-receipt schema, and replay checker. | Could become a focused benchmark/tool paper if end-to-end effects are weak. |
| **Optional** | Add a complexity break-even curve and low-dependence negative controls. | Makes the framework’s “scale down or disappear” claim testable. |
| **Reject** | “Evidence before generation,” claim/evidence graphs, provenance, source-aware selection, human review, versioned memory, or route receipts as standalone novelty. | Each has strong direct precedent. |
| **Reject** | “No prior framework covers the whole responsibility” without systematic search. | The current review is targeted and current agentic systems are rapidly integrating overlapping pieces. |
| **Reject** | Trust, transparency, citations, fluency, or confidence as safety/decision-quality proxies. | PaperTrail, attribution-bias, authority-bias, and RAG Paradox results contradict that shortcut. |
| **Reject** | Universal recurrence discount or automatic policy learning from outcomes. | Can suppress valid convergence or institutionalize/propagate error. |

## Bottom line

[S] The project’s components are well-grounded in prior literature, and new 2025–2026 work makes the surrounding space more integrated than the current thought piece acknowledges. [I16] The distinctive claim should be reduced to a **provenance/dependence-aware action-policy contract with explicit invariants**, evaluated for conditional value under matched resource and review costs. [H] The most promising first paper is likely a focused benchmark/mechanism study on unknown source dependence and action routing, or a human-correction study on progressive claim/evidence/dependence receipts—not a universal “discrimination layer” architecture paper.

If the proposed policy cannot beat strong simple and specialized baselines on the dependence/contradiction/missingness cases it is designed for, the correct result is to narrow further, publish the negative/complexity finding, or retire the label. The project’s strongest intellectual asset is its willingness to name those failure conditions; the next revision should make them the center of the scientific claim rather than leaving them as caveats around a broad architecture.

