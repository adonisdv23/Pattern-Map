# Overnight research memo: new insights and visual opportunities

**Prepared:** 2026-08-18  
**Lane:** Pattern Recognition / Discrimination Layer  
**Status:** Read-only overnight research; this is a literature-grounded opportunity memo, not validation of the provisional thesis.  
**Scope:** The memo adds adjacent primary and authoritative literature to the current v14 materials, proposes small falsifiable studies and product applications, and gives v15 interface and visual guidance. It does not claim that any mechanism listed here is novel.

## How to read the evidence posture

The current thought piece already has substantial overlap with information foraging, sensemaking, provenance, value of information, source-aware retrieval, mixed initiative, claim verification, calibration, and organizational learning. The useful question for v15 is therefore not “what new name can be attached to the layer?” It is “which separations or controls are worth their cost, under which human and organizational conditions, and how can the reader inspect them without being shown a misleading pipeline?”

Labels used below:

- **[Sourced evidence]** A result, observation, standard, or argument from the linked literature. The source type and important limitation are stated where material.
- **[Inference]** A conclusion drawn across the literature and the current thesis. It is not a result of a new experiment.
- **[Design hypothesis]** A proposed product or visual intervention that should be tested.
- **[Research question]** A deliberately unresolved question or a falsifier for a proposed intervention.
- **[Illustration]** A conceptual visual example, not an evidence display or empirical result.

The links point to a publisher, official institutional record, open author copy, standards body, or direct DOI. The access date is the date of this overnight pass; publication status is noted where a result is a preprint or a conceptual paper.

## Executive synthesis

1. **Acquisition is a control problem, not only a retrieval problem.** In an EMNLP 2025 study of agentic search, both over-search (redundant steps) and under-search (missed necessary retrieval) were measurable failure modes; search-decision accuracy tracked the model’s uncertainty about whether to search. One model could have avoided searching in 27.7% of observed search steps. [Sourced evidence: Wu et al., “Search Wisely,” [ACL record](https://aclanthology.org/2025.emnlp-main.998/), [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.998).] The layer should expose a reason to search, a reason to stop, and an explicit hold/clarify state. [Inference]

2. **Discrimination complexity has to beat a strong simple baseline.** Under matched token budgets, an EMNLP 2025 comparison found a simple retrieve-then-read baseline that preserves original passage order and source fidelity could match or outperform more elaborate long-context RAG pipelines. [Sourced evidence: Laitenberger, Manning, and Liu, “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models,” [ACL record](https://aclanthology.org/2025.emnlp-main.1656/), [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1656).] A v15 story should show the simple comparator beside the proposed layer and make “added policy” pay rent in a controlled evaluation. [Design hypothesis]

3. **Agreement is not independence.** A 2025 source-reliability RAG method estimates reliability partly by cross-source checking and weighted voting. [Sourced evidence: Hwang et al., “Retrieval-Augmented Generation with Estimation of Source Reliability,” [ACL record](https://aclanthology.org/2025.emnlp-main.1738/), [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1738).] Evidence-synthesis practice separately warns that multiple reports may represent one underlying study and must not be counted as independent studies. [Sourced evidence: [Cochrane Handbook, current edition](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current).] [Inference] Recurrence should be shown with origin clusters and an “independence unknown” state, not collapsed into a stronger support score.

4. **A provenance display can improve inspectability while failing to change behavior.** PaperTrail (CHI 2026) decomposed answers and documents into claims and evidence, including supported, unsupported, and omitted claims. In a within-subject study with 26 researchers, granular provenance lowered trust relative to a citation baseline but did not change reliance/edit behavior; extra information also created clutter and usability costs under time pressure. [Sourced evidence: Martin-Boyle et al., “PaperTrail,” [open author PDF](https://anmartin94.github.io/files/chi26-828.pdf), [arXiv record](https://arxiv.org/abs/2602.21045), [DOI](https://doi.org/10.1145/3772318.3791101).] [Inference] “More provenance” is not a sufficient design goal. A useful evidence path must connect a claim to a concrete next action, and evaluation must measure correction and verification, not trust alone.

5. **Explanation is not verification.** A pre-registered CHI 2025 experiment with 308 participants found that explanations increased reliance on both correct and incorrect LLM outputs, whereas sources or inconsistencies in explanations reduced reliance on incorrect outputs. [Sourced evidence: Kim et al., “Fostering Appropriate Reliance,” [Microsoft Research record](https://www.microsoft.com/en-us/research/publication/fostering-appropriate-reliance-on-large-language-models-the-role-of-explanations-sources-and-inconsistencies/), [DOI](https://doi.org/10.1145/3706598.3714020).] Earlier mixed-method work likewise found that explanations did not increase complementary human-AI team performance and could increase acceptance regardless of correctness. [Sourced evidence: Bansal et al., “Does the Whole Exceed its Parts?,” [UW record](https://idl.uw.edu/papers/ai-explanations-team-performance), [DOI](https://doi.org/10.1145/3411764.3445717).] [Inference] The layer should optimize for a user’s ability to check, challenge, or defer—not for persuasive rationale text.

6. **The useful unit may be a typed reasoning cue, not a generic explanation or ranked source.** A CHI 2026 contextual inquiry and think-aloud study with six ICU teams and 25 expert physicians identified eight kinds of AI information with distinct decision roles, such as resolving contradictions, surfacing alternatives, and indicating plan preference; value depended on task variability, fit with goals, and complementarity with prior knowledge. [Sourced evidence: Sivaraman et al., “Intelligent Reasoning Cues,” [arXiv record](https://arxiv.org/abs/2602.00259), [DOI](https://doi.org/10.1145/3772318.3790953).] A CHI 2025 experiment similarly found that adaptively selecting which feature analyses to present improved appropriate reliance compared with presenting every analysis. [Sourced evidence: Li et al., “From Text to Trust,” [DOI](https://doi.org/10.1145/3706598.3713133).] [Design hypothesis] v15 can make cue role explicit: “contradiction,” “alternative,” “gap,” “common origin,” or “action consequence,” with “why now” and “what would change my decision?” fields.

7. **Uncertainty representations change strategy and trust, not necessarily accuracy.** Studies in target identification and map-based decisions found that visualized uncertainty altered search/selection strategies while leaving accuracy or confidence unchanged in some conditions. [Sourced evidence: Riveiro et al., [DOI](https://doi.org/10.1016/j.cag.2014.02.006); Korporaal, Ruginski, and Fabrikant, [DOI](https://doi.org/10.3389/fcomp.2020.00032).] A 2025 study found context, attitude toward AI, and the visual encoding itself affected decisions and trust, with no universal best method. [Sourced evidence: Reyes, Batmaz, and Kersten-Oertel, [DOI](https://doi.org/10.3389/fcomp.2025.1464348).] [Inference] Do not put a single confidence halo around a claim. State what is uncertain—support, identity, origin, scope, or consequence—and evaluate route, attention, workload, and correction as well as accuracy.

8. **Evidence discovery is both directed and serendipitous.** CHI 2025 work on “needles in document haystacks” identified multiple hypothesis-exploration pathways and combined sentence-level claim retrieval, contextualization, provenance tracking, user control, and serendipity; it reports expert interviews/use cases and a user study with 10 participants across political discourse and medical research. [Sourced evidence: Dück, Holter, and Chan, “Finding Needles in Document Haystacks,” [ETH record](https://www.research-collection.ethz.ch/entities/publication/781b1396-263b-40db-9282-03ded6e9f4bc), [CHI DOI](https://doi.org/10.1145/3706598.3713715).] [Inference] A path display should show branches considered, branches left unexplored, and the reason a claim became salient; a query-to-answer arrow hides the most important work.

9. **The eventual application is a network of roles, not only a person plus a model.** Sensemaking AI’s 2026 research/design agenda argues that much human-centered AI remains dyadic and static, while real decisions involve volatile environments, social networks, values, path dependence, and the need to preserve dissent and hand authority back to people. [Sourced evidence, conceptual/scoping rather than a causal experiment: Comes, “Sensemaking AI,” [EPJ Data Science article](https://link.springer.com/article/10.1140/epjds/s13688-026-00634-5), [DOI](https://doi.org/10.1140/epjds/s13688-026-00634-5).] [Inference] Product provenance should include role, owner, disposition, audience, and version; organizational use should not turn a provisional evidence route into an unappealable score.

10. **A visual metaphor is itself a reasoning intervention.** Experiments show that verbal/visual metaphors shape what information users derive from a display, and visualization-rhetoric work shows that selection, omission, annotation, and interaction frame interpretation. [Sourced evidence: Ziemkiewicz and Kosara, [DOI](https://doi.org/10.1109/TVCG.2008.171); Hullman and Diakopoulos, [DOI](https://doi.org/10.1109/TVCG.2011.255).] [Inference] A funnel, conveyor belt, ladder, or pyramid would contradict the thesis even if its labels say “iterative.” Use a forked trail, typed relation field, or layered archive only with an explicit legend and a text equivalent.

## What this adds to the current v14 map

The current map already separates the six families and includes a two-loop relation between evidence and learning. The following are deltas or sharper boundary conditions rather than claims of new mechanisms:

| Addition | Sourced signal | Implication for the thesis |
| --- | --- | --- |
| Search stopping and route receipts | Over- and under-search are distinct agentic-search errors; uncertainty tracks search decisions. [Wu 2025](https://doi.org/10.18653/v1/2025.emnlp-main.998) | Acquisition needs an observable stop/hold/clarify policy and a receipt for why a search occurred. |
| Complexity tax | Simple source-faithful RAG can beat elaborate pipelines under matched budgets. [Laitenberger et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1656) | “Discrimination layer” is a hypothesis about net decision value, not a license to add gates. |
| Independence as a first-class uncertainty | Reliability-by-agreement methods exist, but evidence synthesis distinguishes reports from independent studies. [Hwang et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1738); [Cochrane](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) | Show source origin clusters and unknown dependence; recurrence must not masquerade as corroboration. |
| Claim/evidence/omission path | PaperTrail gives granular provenance but finds a trust–behavior gap and clutter cost. [Martin-Boyle et al. 2026](https://doi.org/10.1145/3772318.3791101) | Provenance must be actionable and progressive, with omitted/unsupported states visible. |
| Cue role and adaptive disclosure | Reasoning-cue work distinguishes contradiction, alternatives, gaps, and other roles; adaptive analysis improved reliance. [Sivaraman et al. 2026](https://doi.org/10.1145/3772318.3790953); [Li et al. 2025](https://doi.org/10.1145/3706598.3713133) | Replace an undifferentiated “relevance/importance” display with typed cues plus “why now.” |
| Strategy-sensitive uncertainty | Visual uncertainty often changes strategy and attention without a simple accuracy gain. [Korporaal et al. 2020](https://doi.org/10.3389/fcomp.2020.00032); [Hullman et al. 2018](https://doi.org/10.1109/TVCG.2018.2864889) | Evaluate uncertainty displays for interpretation, route, workload, and correction, not just confidence. |
| Directed + serendipitous discovery | Claim retrieval studies deliberately combine user control and serendipity. [Dück et al. 2025](https://doi.org/10.1145/3706598.3713715) | A route should preserve unchosen branches and serendipitous finds, rather than imply a single optimal path. |
| Role/network context | Sensemaking AI emphasizes collective agency, values, dissent, and path dependence. [Comes 2026](https://doi.org/10.1140/epjds/s13688-026-00634-5) | The provenance object should name the decision role and authority boundary, not only the model and source. |

## Smaller, testable papers or experiments

These are deliberately narrower than the full thesis. Each is a proposal, not a result. A paper should pre-register the primary outcome and include the simplest credible baseline. “Improvement” should mean a decision or verification benefit that survives time, attention, and cost accounting.

### 1. Search decision receipts: when should the layer search, stop, hold, or ask?

- **Question:** Does an uncertainty-aware search controller reduce redundant retrieval while preserving necessary acquisition?
- **Design:** Use a fixed set of multi-hop and single-hop questions with controlled corpus coverage. Compare (a) ordinary retrieve-then-answer, (b) source-faithful retrieve-then-read, and (c) a controller that records search reason, expected gap, stop criterion, and hold/clarify option. Match token, latency, and retrieval budgets.
- **Measures:** Over-search steps, under-search misses, search-step uncertainty, supported-claim rate, unresolved-claim rate, abstention/clarification quality, latency, cost, and user correction time. Log the route receipt rather than only the final answer.
- **Falsifier/boundary:** If the controller does not improve supported claims or appropriate stopping per unit cost, or if it improves benchmark accuracy only by spending materially more resources, the added control is not justified.
- **Anchor:** [Wu et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.998) and [Laitenberger et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1656).

### 2. The provenance–action gap: citations versus claim paths

- **Question:** Which evidence-path representation helps people find and repair unsupported or omitted claims?
- **Design:** Randomize participants to citation-only, claim-to-evidence, or claim-to-evidence plus omission/contradiction plus a concrete next-action affordance. Use scholarly editing, policy comparison, or incident-summary tasks with planted supported, unsupported, and copied-source cases.
- **Measures:** Unsupported/omitted claim detection, correction rate, time-to-verification, edit distance, source switching, appropriate reliance, workload, and trust. Measure whether people actually inspect the path before acting.
- **Falsifier/boundary:** If granular provenance lowers trust but does not improve correction or verification, then the display is an audit aid at best, not a human-decision aid. If a dense path hurts correction under time pressure, default disclosure is too high.
- **Anchor:** [PaperTrail, CHI 2026](https://doi.org/10.1145/3772318.3791101) and [The HaLLMark Effect, CHI 2024](https://doi.org/10.1145/3613904.3641895).

### 3. Typed reasoning cues versus generic explanations

- **Question:** Do cue types such as contradiction, alternative, anomaly, gap, origin conflict, and action consequence improve appropriate reliance over a generic explanation or ranked source list?
- **Design:** Build a small cue taxonomy and compare a generic explanation, a relevance-ranked evidence list, and typed cue cards. Each card should expose “why now,” source/span, relation, uncertainty type, and suggested verification action. Use tasks where the model is sometimes correct and sometimes wrong in different ways.
- **Measures:** Correct acceptance, correct rejection, error detection, appropriate abstention, choice of next source, path diversity, verification time, and NASA-TLX or equivalent workload. Record which cue was actually used.
- **Falsifier/boundary:** If typed cues only reduce global trust, increase checking without improving decisions, or fail when task goals change, the taxonomy is decorative or too rigid.
- **Anchor:** [Sivaraman et al. 2026](https://doi.org/10.1145/3772318.3790953), [Li et al. 2025](https://doi.org/10.1145/3706598.3713133), and [Kim et al. 2025](https://doi.org/10.1145/3706598.3714020).

### 4. Common-origin control: recurrence, copying, and unknown dependence

- **Question:** Does explicit origin clustering reduce false corroboration without suppressing genuine independent consensus?
- **Design:** Construct a benchmark with independent reports, direct copies, paraphrased copies, shared press releases, common upstream datasets, and genuinely convergent observations. Compare count-based recurrence, URL-level deduplication, and origin-aware grouping. Include an “unknown dependence” condition rather than forcing a binary label.
- **Measures:** False corroboration, recall of true consensus, source-diversity calibration, origin-cluster accuracy, and user willingness to inspect a second source. Report error asymmetry: missed independence versus overcounted copies.
- **Falsifier/boundary:** If origin inference is too noisy to improve decisions, or if it systematically discounts legitimate common-source reporting, present it as an uncertain cue rather than an automatic weighting rule.
- **Anchor:** [Hwang et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1738) and the [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current), especially its treatment of multiple reports of one study.

### 5. An uncertainty grammar for support, identity, origin, scope, and consequence

- **Question:** Does type-specific uncertainty communication help people choose safer next actions better than one scalar confidence?
- **Design:** Factorially compare a scalar confidence badge, typed textual labels, and typed visual encodings for at least: evidence support uncertainty, source identity/authority uncertainty, common-origin uncertainty, temporal/scope uncertainty, and uncertainty about action consequences. Use time-pressured tasks with a mix of low- and high-stakes decisions.
- **Measures:** Interpretation of what is uncertain, calibration, appropriate reliance, verification route, willingness to defer, confidence, attention allocation, workload, and downstream error. Include a no-uncertainty-display baseline.
- **Falsifier/boundary:** If a display changes avoidance strategy but not decision quality, or if users interpret the visual type as a probability of truth, the encoding is misleading. A result should not be reduced to “more uncertainty is safer.”
- **Anchor:** [MacEachren et al. 2012](https://doi.org/10.1109/TVCG.2012.279), [Korporaal et al. 2020](https://doi.org/10.3389/fcomp.2020.00032), and [Reyes et al. 2025](https://doi.org/10.3389/fcomp.2025.1464348).

### 6. The complexity tax: full discrimination layer versus a strong simple baseline

- **Question:** Under equal resource and review budgets, does the complete set of separations outperform simple source-faithful retrieval plus citations?
- **Design:** Compare the full proposed policy with a minimal baseline and a staged ablation: provenance only; provenance plus claim support; support plus origin; all dimensions plus adaptive stopping. Use both model-only and human-assisted conditions.
- **Measures:** Supported-claim rate, appropriate reliance, correction time, decision quality, latency, token cost, interface complexity, and operator training time. Include failure cases where a simple answer is correct and cases requiring multi-source comparison.
- **Falsifier/boundary:** No net gain after accounting for cost, or gains limited to synthetic benchmark artifacts, should narrow the thesis to specific high-value tasks.
- **Anchor:** [Laitenberger et al. 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1656) and the existing v14 research requirement for strong simple baselines.

### 7. Branching evidence trails and serendipitous findings

- **Question:** Does preserving visible branches improve discovery and reduce premature closure without causing unmanageable search sprawl?
- **Design:** Compare a linear ranked result list, a branchable claim trail, and a branchable trail with explicit cost/stop controls. Give participants both target-finding tasks and open-ended hypothesis exploration. Make unvisited branches and serendipitous findings recordable.
- **Measures:** Target recall, novel-but-relevant finding rate, diversity of source/origin clusters, premature closure, search depth, time, workload, and ability to explain why the final claim was retained.
- **Falsifier/boundary:** If branches increase novelty but reduce decision quality, or users cannot tell explored from unexplored material, the trail needs stronger scope and route receipts.
- **Anchor:** [Dück et al. 2025](https://doi.org/10.1145/3706598.3713715) and [Xu et al. 2015](https://doi.org/10.1109/mcg.2015.50).

### 8. From one operator to a role-aware evidence network

- **Question:** Does recording role, authority, dissent, and disposition improve correction and organizational learning compared with a single-user evidence log?
- **Design:** Start with a controlled simulation or longitudinal field pilot in which a researcher, reviewer, steward, or decision owner receives the same evidence packet. Compare a single shared status with role-specific dispositions and visible dissent. Keep raw sources immutable while allowing interpretations to change.
- **Measures:** Independent error detection, escalation quality, time to correction, dissent preservation, source diversity, repeated mistakes, memory contamination, and perceived agency. Track whether the group becomes overconfident through agreement.
- **Falsifier/boundary:** If role labels create bureaucracy without improving corrections, or if visible dissent merely increases noise, use role context only in high-stakes or multi-owner tasks.
- **Anchor:** [Comes 2026](https://doi.org/10.1140/epjds/s13688-026-00634-5) is a conceptual/scoping agenda; [Woolley et al. 2010](https://doi.org/10.1126/science.1193147) is a group-performance precedent, not evidence for this product.

## Organizational and product applications

These are plausible application surfaces, not demonstrations that the framework works in them. Each has a different authority boundary and failure cost; the same visual or scoring rule should not be carried across them unchanged.

| Application | Useful evidence-path object | Product opportunity | Boundary that must remain explicit |
| --- | --- | --- | --- |
| Scholarly research and literature review | Claim, exact passage, study/report identity, method qualifier, related reports, disagreement, omission, and update date | A claim-evidence canvas that helps a researcher compare papers, preserve context, mark a result as provisional, and export a traceable review note | Citation count is not evidence strength; multiple papers may share one underlying study; no “verified” label without a defined corpus and task |
| Incident response and operations | Event observation, timestamp, system/run/version, operator action, competing explanation, current status, and disposition | A route receipt showing what was checked, which hypotheses remain open, who owns the next check, and what evidence would change the response | A plausible causal story is not a causal finding; raw logs and human interpretations need separate retention and access rules |
| Procurement and vendor evaluation | Requirement/claim, vendor artifact, independent test, contract scope, authorization, conflict, date, and missing evidence | A comparison packet that distinguishes “meets stated requirement,” “independently tested,” “authorized for this use,” and “still unknown” | A vendor’s recurrence in marketing material is not independent corroboration; a ranking should not silently become a purchasing decision |
| Governance, audit, and compliance | Control, evidence artifact, owner, time/version, transformation, exception, reviewer disposition, and appeal | An append-only audit trail with explicit evidence gaps and a human disposition queue | “No evidence found” is not “no risk”; a compliance score must not replace the underlying evidence and appeal path |
| Enterprise knowledge and agent memory | Fact/claim, origin, scope, freshness, derivation, supersession, access policy, and confidence type | Memory entries that preserve source identity and why a fact was retained, with safe forgetting/supersession and owner review | Summaries can launder origin; copied memories can manufacture recurrence; retention and privacy policy are part of the evidence path |
| Cross-functional decision rooms | Claim, role, perspective, private concern, public disposition, unresolved disagreement, and decision consequence | A shared evidence room that protects private review until a user chooses to expose it, then records dissent and decision ownership | Group agreement is not independent support; the system must not pressure minority reviewers into a false consensus |
| Customer support and policy operations | Customer statement, policy version, case precedent, exception, jurisdiction, and escalation rule | A bounded context packet with a “why this policy applies” path and a visible “ask a human” route | A helpful tone cannot cover jurisdiction or authorization gaps; the customer-facing answer should not expose internal secrets |

The most tractable first product experiment is likely a low-risk research or internal-operations prototype where claims, passages, source versions, and user dispositions can be logged without implying automated authority. High-stakes deployment would require a separate safety, access, and accountability review.

## Evidence-path interface: a minimum useful object

The literature points toward an interface unit smaller than a document and richer than a source rank. The following is a **[Design hypothesis]** for a minimum record. It is deliberately a schema proposal, not a standard.

1. **Claim or decision question:** Atomic proposition, scope, time window, and intended decision. Do not make a paragraph-level answer the only unit.
2. **Evidence span:** Exact passage, observation, measurement, or artifact location. Preserve the surrounding context on demand.
3. **Relationship:** Supports, contradicts, qualifies, contextualizes, omits, or is derived from the claim. A line without a typed relation is only a citation.
4. **Identity and origin:** Source/artifact identifier, owner/publisher, creation and access times, version, transformation history, and possible common-origin cluster. Use “unknown” when dependence is not known.
5. **Authority and authorization:** Domain, jurisdiction, role, and permission to use the material. Keep this separate from whether the passage supports the claim.
6. **Uncertainty type:** Support, identity, origin, scope/time, measurement, model inference, or action consequence. A scalar may be useful within one type but must not be presented as universal truth confidence.
7. **Reason this cue is shown:** Current gap, contradiction, unusual change, missing source, decision sensitivity, or user request. This is the proposed “why now” field.
8. **Next action and cost:** Inspect context, compare an independent source, acquire another patch, ask an owner, use provisionally, hold, defer, or refuse. Include expected latency/attention/cost where estimable.
9. **Human disposition:** Accepted, rejected, unresolved, superseded, or escalated; who made the disposition, in what role, and under what authority. Preserve a history rather than overwriting the raw artifact.
10. **Outcome link:** Later correction, decision consequence, or review result. Keep outcome feedback distinct from source truth and avoid updating a prior merely because an outcome was convenient.

### Progressive disclosure

PaperTrail’s trust–behavior gap and clutter result suggest three levels:

- **Route receipt:** One compact record of the current question, the chosen search/stop action, the main gap, cost, and current state.
- **Cue card:** One claim, one typed relation, one evidence span, origin/uncertainty labels, and one suggested next action.
- **Audit expansion:** Full derivation, source versions, transformation history, unchosen branches, reviewer dispositions, and outcome links.

[Inference] The default screen should not present the full graph. It should provide enough structure for the user to challenge the current route, then allow deliberate expansion. The hidden-state policy should be explicit: “not shown yet,” “not searched,” “not found,” “not authorized,” and “not applicable” are different states.

### A non-linear route grammar

The conceptual run is better represented as permitted moves than as a fixed sequence:

~~~text
[decision context]
      ↘ candidate patch A ──┐
      ↘ candidate patch B ───┼─> [claim / evidence / relation]
      ↘ owner question ─────┘          │
               ↖ [new gap / contradiction / origin issue]
                              ├─> inspect / compare / acquire
                              ├─> use provisionally
                              ├─> hold / clarify / defer
                              └─> refuse or escalate
                                      ↺
                           [human disposition + outcome]
                                      ↺ policy/history
~~~

[Illustration] The branches are a grammar, not a claim that every run visits every state. A real route receipt would number one observed path, retain unvisited alternatives, and distinguish “not chosen” from “not available.” This is the distinction the current six-family arrows should make clearer.

## Visual cognition and human-factors implications

### What the literature says to measure

Uncertainty-visualization research warns that a display can change strategy without improving accuracy. [Sourced evidence: Riveiro et al. 2014, [DOI](https://doi.org/10.1016/j.cag.2014.02.006); Korporaal et al. 2020, [DOI](https://doi.org/10.3389/fcomp.2020.00032).] A survey of 86 uncertainty-visualization user studies argues that evaluation has overemphasized performance and satisfaction and often assumes overly predictable statistical judgment. [Sourced evidence: Hullman et al., “In Pursuit of Error,” [DOI](https://doi.org/10.1109/TVCG.2018.2864889).]

For the v15 site, the visual comprehension questions are therefore:

- Can a reader tell that a relation map permits multiple orders and returns?
- Can a reader distinguish support, authority, independence, relevance, and action priority?
- Can a reader tell whether a branch was searched, unsearched, unavailable, or merely not shown?
- Can a reader identify which uncertainty type is being shown?
- Can a reader find the exact source span and the proposed next action?
- Does the display make a reviewer more likely to catch a wrong claim, or only more likely to say that the system is trustworthy?
- Does the visual increase premature closure, source avoidance, or workload?

These should be tested with interpretation, path/attention, correction, appropriate reliance, workload, and decision-quality measures—not only a comprehension quiz or a confidence rating.

### Deterministic HTML/SVG: roles that should remain exact

Use deterministic HTML, CSS, accessible tables, and SVG for anything that has a claim to exactness, state, topology, or auditability:

- The six-family relationship map, with typed edges and a legend stating that it is not a mandatory sequence.
- The evidence-path view: claim, evidence span, source identity, relation, origin cluster, uncertainty type, and next action.
- A one-run route receipt with exact states such as searched, not searched, held, clarified, or escalated.
- Comparison of the full layer with the simple source-faithful baseline and ablations.
- Status labels, counts, dates, source versions, and provenance transformations.
- Append-only history and human dispositions.
- Text equivalents, keyboard focus, reduced-motion behavior, print layout, and high-contrast variants.

Exact visual encodings should not rely on color alone. Shape, text, line style, and a short legend should carry the distinction. For example, a dotted relation can mean “origin uncertain” only if the nearby legend says so; it must not also mean “weak support.”

### Editorial raster or illustrative image: roles that can aid comprehension

Editorial images can materially help when the reader needs an intuitive entry into a conceptual change that an exact diagram would flatten. Keep them sparse, clearly labeled, and separate from the evidence display.

1. **The opening shift from answer to context.** A quiet desk, field notebook, or set of marked source cards can convey that the work is deciding what to inspect before drafting. The image should not contain legible factual text, logos, source counts, or a single glowing “truth.”
2. **A bounded route through ambiguity.** A trail with forks and returns can make exploration, stopping, and re-entry memorable. Show more than one plausible branch and an unvisited branch; do not show a single hero path or a treasure at the end.
3. **Human correction and responsibility.** A hand marking a source card or moving a claim into “hold” can communicate owner disposition and override. It should be explicitly illustrative, not a photograph of a real organization or an implied case study.
4. **Layered history without erasure.** Transparent sheets, archive cards, or strata can convey raw artifact, transformation, interpretation, and supersession. The image should not imply that higher layers are more authoritative.
5. **Competing frames.** Overlapping translucent fields or several partial windows can convey that different roles inspect different evidence and that the context packet is bounded. Keep the frame edges visible so the omission is part of the metaphor.
6. **A quiet transition image between sections.** A small, consistent editorial motif can separate “mechanism,” “human correction,” and “research agenda” without pretending to be a chart.

Every editorial image should carry a caption such as: “Illustrative metaphor; not a data display or empirical result.” Its alt text should say what conceptual relation it illustrates and what it does not establish. The adjacent prose must carry the exact claim.

### Things that should not be delegated to an editorial image

Do not use a raster image to show exact evidence topology, claim support, source counts, uncertainty values, a chronological audit trail, or the status of a particular claim. Do not use a cinematic scene as a substitute for a source, a citation, a benchmark result, or a user study. Do not depict a real institution, patient, incident, or vendor unless the relevant facts and permissions are actually in scope.

## Non-misleading visual metaphors

Visual semiotics research shows that a metaphor imports an ontology before the labels are read. [Sourced evidence: Ziemkiewicz and Kosara, “The Shaping of Information by Visual Metaphors,” [DOI](https://doi.org/10.1109/TVCG.2008.171).] Narrative-visualization research likewise treats selection, omission, representation, annotation, and interactivity as framing choices. [Sourced evidence: Hullman and Diakopoulos, [DOI](https://doi.org/10.1109/TVCG.2011.255).] The following guardrails are therefore part of the content, not cosmetic advice.

| Metaphor | What it can communicate | Guardrails | What it must not imply |
| --- | --- | --- | --- |
| Forked trail with returns | Directed discovery, alternate hypotheses, stopping and revisiting | Label one path as “recorded exploration”; show unvisited and unavailable branches; mark why a branch was chosen | A complete search, a single optimal path, or a final destination that is “truth” |
| Constellation or evidence field | Non-linear relationships among claims, sources, and observations | Use typed links such as supports, contradicts, derived-from, common-origin, or unknown; use text labels and a small graph | That salience, size, centrality, or brightness means authority or truth |
| Layered archive / transparent strata | Raw material, transformation, interpretation, supersession, and preserved history | Label each layer and keep raw artifact visibly separate from interpretation; show reversibility | That upper layers are more authoritative or that a summary replaces the source |
| Window, frame, or cross-section | Bounded context, role-specific view, and deliberate omission | Draw the frame and annotate “outside current packet”; link to expansion or ask/hold states | That the frame is the whole world or that excluded material was checked and rejected |
| Route card or instrument panel | Current decision state, budget, next action, and human owner | Put alternatives and stop/hold/clarify beside the current recommendation; show state and cost | That the route is a fact, an automatic command, or a universal score |
| Braided threads | Multiple evidence and learning loops that remain connected | Keep strands distinguishable and label crossing/merging relations | That all strands converge on one answer or that agreement means independence |

### Metaphors to avoid or use only with an explicit rebuttal

- Funnel, pipeline, conveyor belt, assembly line, or one-way river: implies fixed order and irreversible reduction.
- Ladder, staircase, pyramid, or elevation map: implies a single hierarchy where “higher” means more authoritative.
- Funnel into a glowing answer, spotlight, needle, or treasure: implies one obvious relevant item and hides unsearched alternatives.
- Balance scale: implies that support and contradiction are commensurable quantities even when they are typed, scoped, and action-dependent.
- Traffic-light red/green truth coding: encourages binary correctness and can confuse uncertainty, risk, and action priority.
- Blur, opacity, or tiny size for “low credibility”: makes a less salient item harder to inspect and can turn visual attention into an accidental authority score.
- Dense network hairball: can imply complexity while making actual relations unreadable. A controlled graph should remain small and typed; for larger graphs, offer a filterable table or matrix.

Graph readability is task-dependent. Controlled graph studies find that node-link views help some path-finding tasks while matrix or table forms can outperform them as graphs grow; no representation is universally best. [Sourced evidence: Ghoniem, Fekete, and Castagliola, [DOI](https://doi.org/10.1057/palgrave.ivs.9500092); [network-visualization cognitive-fit study](https://doi.org/10.1016/j.socnet.2018.01.005).] [Design hypothesis] Keep the v15 graph intentionally sparse and offer a table or relation list as the canonical inspection view.

## Specific v15 site opportunities

1. **Recast the six-family map as a relation map.** Keep the six families, but reduce the visual insistence of the current lane-like arrows. Use a central decision/context boundary with surrounding family cards, and label edges with permitted relations: “can invoke,” “records,” “updates,” “checks,” or “hands to.” Use arrowheads only for genuinely temporal or causal relations. Add the legend: “Relationship map; a run may visit a subset in different orders.”

2. **Make terminal states first-class.** Place “use provisionally,” “acquire,” “clarify,” “hold,” “defer,” “refuse,” and “escalate” as visible exits from the decision context. This prevents the reader from interpreting the map as an engine that must always end in generation.

3. **Split one observed route from the policy grammar.** In the “two loops / one preserved history” figure, show a numbered, thin route for one example and a separate, dashed relation for possible feedback. The caption should say “one illustrative run,” not “the pipeline.”

4. **Add a compact route-receipt card.** Show question, candidate patch, reason to acquire, reason to stop, cost, unresolved gap, owner, and disposition. This is a high-value deterministic component because it makes the thesis inspectable without adding another decorative system diagram.

5. **Add a typed evidence-path specimen.** Use one short claim with two evidence spans: one supports, one qualifies or contradicts, and a third shares an origin with the first. Show exact spans, version/date, origin status, uncertainty type, and next action. Use a text table alongside the SVG.

6. **Show the simple baseline.** Put “source-faithful retrieve-then-read + citations” next to the proposed layer with a neutral label, not a straw-man. The purpose is to make the research obligation visible: additional discrimination must produce measurable net benefit.

7. **Use an “uncertainty legend,” not an uncertainty aura.** The specimen should distinguish support, identity/authority, origin, scope/time, and action consequence. A single badge called “confidence” would contradict the separation thesis.

8. **Make missingness explicit.** Add states for “not searched,” “searched—no result,” “not available,” “not authorized,” “not shown yet,” and “not applicable.” This is a small UI decision with large epistemic consequences.

9. **Use one or two editorial images for the conceptual transition, not for the mechanism.** The strongest roles are the opening “context before answer” image and a human-correction/branching-trail transition. The exact map, evidence path, and route receipt should remain deterministic and accessible.

10. **Test whether the visual itself is understood.** A v15 reader audit should ask a participant to draw or describe the route, identify an unsearched branch, find a contradictory span, and explain the difference between support and authority. If a reader instead describes a pipeline, hierarchy, or confidence meter, the visual has failed regardless of how attractive it is.

## Suggested evaluation and reporting ledger

For each prototype or paper, report:

- **Task and stakes:** What decision is being made, by whom, under what time/attention/authorization boundary?
- **Baseline:** The simplest credible retrieval/citation workflow, with matched token, latency, and review budgets.
- **Evidence unit:** Source, artifact, passage, claim, event, or memory; do not change the unit mid-study.
- **Outcome:** Supported-claim rate, correct/incorrect reliance, appropriate abstention, correction, decision quality, or another pre-registered primary metric.
- **Cost:** Search steps, latency, tokens, money, reviewer time, clicks, and workload.
- **Path behavior:** Which branches were visited, which cues were inspected, whether a user sought an independent source, and where premature closure occurred.
- **Uncertainty interpretation:** Whether users understood the type and scope of uncertainty, not only whether they reported lower confidence.
- **Provenance behavior:** Whether users could locate exact evidence, detect common origin, and understand omissions or transformations.
- **Human agency:** Whether users could override, defer, ask, or appeal, and whether they understood who held decision authority.
- **Failure boundaries:** Task types, roles, source environments, or time pressures where the intervention fails.

This ledger operationalizes the current research horizon: construct boundary, provenance-rich benchmark, strong simple baselines, people and outcomes. It also prevents a visually compelling case study from being mistaken for a validation result.

## Source ledger

The following are the most relevant additions or refinements for this lane. The method notes are included so a later editor can preserve evidence/inference boundaries.

### Acquisition, source reliability, and simplicity

- **Wu, S. et al. (2025). “Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty.” EMNLP 2025.** Primary peer-reviewed NLP study. Reports over-search and under-search as separate failure modes and connects search-decision uncertainty to accuracy; proposes a training method. [ACL Anthology](https://aclanthology.org/2025.emnlp-main.998/) · [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.998).
- **Laitenberger, M., Manning, C. D., and Liu, N. F. (2025). “Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models.” EMNLP 2025.** Primary controlled benchmark under matched token budgets; its key value here is the complexity boundary, not a claim that one RAG method wins universally. [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1656/) · [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1656).
- **Hwang, J. et al. (2025). “Retrieval-Augmented Generation with Estimation of Source Reliability.” EMNLP 2025.** Primary method paper using cross-source consistency and weighted voting to estimate source reliability; agreement is not proof of independence. [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1738/) · [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1738).
- **Cochrane Collaboration. Cochrane Handbook for Systematic Reviews of Interventions, current edition.** Authoritative evidence-synthesis guidance; relevant precedent for grouping multiple reports of one underlying study and making eligibility/updates explicit. [Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current).

### Evidence-path interfaces, explanations, and reliance

- **Martin-Boyle, A. et al. (2026). “PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A.” CHI 2026.** Primary user study with 26 researchers; claim/evidence/omission decomposition, lower trust but no reliance/edit change versus citation baseline, and clutter/usability costs. [Open PDF](https://anmartin94.github.io/files/chi26-828.pdf) · [arXiv](https://arxiv.org/abs/2602.21045) · [DOI](https://doi.org/10.1145/3772318.3791101).
- **Hoque, M. N. et al. (2024). “The HaLLMark Effect: Supporting Provenance and Transparent Use of Large Language Models in Writing with Interactive Visualization.” CHI 2024.** Primary qualitative/user study with creative writers; shows provenance visualization can support control and ownership, not that it establishes correctness. [University of Iowa record](https://iro.uiowa.edu/esploro/outputs/conferenceProceeding/The-HaLLMark-Effect-Supporting-Provenance-and/9984787459302771) · [DOI](https://doi.org/10.1145/3613904.3641895).
- **Kim, Y. et al. (2025). “Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies.” CHI 2025.** Pre-registered experiment with 308 participants plus think-aloud; generic explanations increased reliance on right and wrong outputs, while sources/inconsistencies reduced wrong reliance. [Microsoft Research record](https://www.microsoft.com/en-us/research/publication/fostering-appropriate-reliance-on-large-language-models-the-role-of-explanations-sources-and-inconsistencies/) · [DOI](https://doi.org/10.1145/3706598.3714020).
- **Kim, J. et al. (2024). “‘I’m Not Sure, But…’: Examining the Impact of LLM Uncertainty Expression on User Reliance and Trust.” FAccT 2024.** Pre-registered medical-QA experiment with 404 participants; first-person uncertainty wording reduced overreliance on incorrect answers, while generic phrasing was weaker. [Microsoft Research record](https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/) · [DOI](https://doi.org/10.1145/3630106.3658941) · [Open PDF](https://facctconference.org/static/papers24/facct24-56.pdf).
- **Bansal, G. et al. (2021). “Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance.” CHI 2021.** Mixed-method studies across three datasets; explanations did not increase complementary team performance and increased acceptance of recommendations regardless of correctness. [UW record](https://idl.uw.edu/papers/ai-explanations-team-performance) · [DOI](https://doi.org/10.1145/3411764.3445717).
- **Fok, R. and Weld, D. (2024). “In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making.” AI Magazine.** Peer-reviewed synthesis arguing that explanations matter when they enable verification; useful conceptual guardrail, not a new experiment. [DOI](https://doi.org/10.1002/aaai.12182).
- **Spatharioti, S. E. et al. (2025). “Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance.” CHI 2025.** Primary online decision experiments; LLM search was faster but produced overreliance when wrong, and simple color highlighting improved error detection in one intervention. [Microsoft Research record](https://www.microsoft.com/en-us/research/publication/effects-of-llm-based-search-on-decision-making-speed-accuracy-and-overreliance/) · [DOI](https://doi.org/10.1145/3706598.3714082).
- **Bo, Y. et al. (2025). “To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models.” CHI 2025.** Randomized study with 400 participants across logical-reasoning and image-estimation tasks; interventions reduced overreliance but did not generally improve appropriate reliance, with some confidence increases on wrong choices. [arXiv record](https://arxiv.org/abs/2412.15584) · [DOI](https://doi.org/10.1145/3706598.3714097).
- **Li, Z. et al. (2025). “From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis.” CHI 2025.** Primary randomized experiment; presenting every feature analysis was not reliably helpful, while adaptive selection improved appropriate reliance/accuracy in the reported setting. [DOI](https://doi.org/10.1145/3706598.3713133).
- **Sivaraman, V. et al. (2026). “Intelligent Reasoning Cues: A Framework and Case Study of the Roles of AI Information in Complex Decisions.” CHI 2026.** Primary contextual inquiry and think-aloud work with ICU teams and expert physicians; proposes cue roles and adaptive decision support. [arXiv](https://arxiv.org/abs/2602.00259) · [DOI](https://doi.org/10.1145/3772318.3790953).

### Discovery, provenance, and organizational context

- **Dück, L. et al. (2025). “Finding Needles in Document Haystacks: Augmenting Serendipitous Claim Retrieval Workflows.” CHI 2025.** Primary interface research combining claim retrieval, context, provenance, user control, and serendipity; includes expert interviews/use cases and a 10-person user study. [ETH research record](https://www.research-collection.ethz.ch/entities/publication/781b1396-263b-40db-9282-03ded6e9f4bc) · [CHI DOI](https://doi.org/10.1145/3706598.3713715).
- **Xu, K. et al. (2015). “Analytic provenance for sensemaking: A research agenda.” IEEE Computer Graphics and Applications.** Primary research-agenda paper connecting data/reasoning history to reflection, collaboration, and uncertainty; direct precedent for an evidence path as action history. [City Research Online](https://openaccess.city.ac.uk/id/eprint/15535/) · [DOI](https://doi.org/10.1109/mcg.2015.50).
- **Kaur, H. et al. (2022). “Sensible AI: Re-imagining Interpretability and Explainability using Sensemaking Theory.” FAccT 2022.** Theory/design paper arguing for user-, identity-, social-, and context-sensitive explanations rather than artifact-only explanation. [DOI](https://doi.org/10.1145/3531146.3533135).
- **Comes, T. (2026). “Sensemaking AI: Introducing a research and design agenda for human–AI networks.” EPJ Data Science.** Open-access scoping/conceptual agenda based on 101 HCAI papers; useful for role/network/value/dissent boundaries, not causal evidence that a proposed interface works. [Article](https://link.springer.com/article/10.1140/epjds/s13688-026-00634-5) · [DOI](https://doi.org/10.1140/epjds/s13688-026-00634-5).

### Visual cognition, uncertainty, and metaphor

- **Riveiro, M. et al. (2014). “Effects of visualizing uncertainty on decision-making in a target identification scenario.” Computers & Graphics.** Primary study with 22 experienced air-traffic operators; uncertainty changed attempts and risk priorities without a significant performance/confidence difference. [DOI](https://doi.org/10.1016/j.cag.2014.02.006).
- **Korporaal, R. et al. (2020). “Effects of Uncertainty Visualization on Map-Based Decision Making Under Time Pressure.” Frontiers in Computer Science.** Primary time-pressured helicopter-landing experiment; uncertainty changed strategy and avoidance of uncertain options while accuracy was not necessarily improved. [Article](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2020.00032/full) · [DOI](https://doi.org/10.3389/fcomp.2020.00032).
- **Reyes, D. et al. (2025). “Trusting AI: does uncertainty visualization affect decision-making?” Frontiers in Computer Science.** Primary 2025 study with 147 included participants in static game scenarios; effects depended on context, attitude, and encoding, with no universal best visual method. [Article](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1464348/full) · [DOI](https://doi.org/10.3389/fcomp.2025.1464348).
- **MacEachren, A. M. et al. (2012). “Visual Semiotics & Uncertainty Visualization: An Empirical Study.” IEEE Transactions on Visualization and Computer Graphics.** Two empirical studies on matching uncertainty types and semiotic encodings; supports a type-specific visual grammar. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/26357158/) · [DOI](https://doi.org/10.1109/TVCG.2012.279).
- **Hullman, J. et al. (2018). “In Pursuit of Error: A Survey of Uncertainty Visualization Evaluation.” IEEE TVCG.** Survey of 86 user studies; argues for broader evaluation than performance/satisfaction. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/30207956/) · [DOI](https://doi.org/10.1109/TVCG.2018.2864889).
- **Hullman, J. (2020). “Why Authors Don’t Visualize Uncertainty.” IEEE TVCG.** Survey/interview work on norms and assumptions that lead authors to omit uncertainty even when they value it. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/31425093/) · [DOI](https://doi.org/10.1109/TVCG.2019.2934287).
- **Hullman, J. and Diakopoulos, N. (2011). “Visualization Rhetoric: Framing Effects in Narrative Visualization.” IEEE TVCG.** Conceptual/empirical framing account; selection, representation, annotation, and interaction can prioritize interpretations. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/22034342/) · [DOI](https://doi.org/10.1109/TVCG.2011.255).
- **Ziemkiewicz, C. and Kosara, R. (2008). “The Shaping of Information by Visual Metaphors.” IEEE TVCG.** Controlled metaphor experiment; compatible and incompatible verbal metaphors changed how users derived information from graph forms. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/18988973/) · [DOI](https://doi.org/10.1109/TVCG.2008.171).
- **Ghoniem, M., Fekete, J.-D., and Castagliola, P. (2005). “On the Readability of Graphs Using Node-Link and Matrix-Based Representations.” Information Visualization.** Controlled graph-reading experiment; representation performance depends on graph size and task. [DOI](https://doi.org/10.1057/palgrave.ivs.9500092).

## Closing boundary

The strongest adjacent literature does not establish that a named “discrimination layer” improves real decisions. It does establish several constraints that make the thesis more testable:

- acquisition should expose stopping and resource tradeoffs;
- source agreement should not stand in for independence;
- claim/evidence provenance should be linked to actions and omissions;
- explanations should be evaluated for verification and appropriate reliance;
- cue roles and disclosure should adapt to the current decision gap;
- uncertainty must be typed and evaluated for strategy as well as accuracy;
- discovery should preserve branches, serendipity, and unsearched states;
- provenance should carry role, authority, version, and dissent in organizational settings;
- visual metaphors should depict permitted relations and revisable routes, not a one-way pipeline.

The proposed v15 visual language is consequently modest: deterministic HTML/SVG for exact relations and states; one or two labeled editorial images for bounded ambiguity, human responsibility, and the conceptual shift from answer to context; and explicit text equivalents for every mechanism. Those are **[Design hypotheses]** awaiting the smaller studies above.
