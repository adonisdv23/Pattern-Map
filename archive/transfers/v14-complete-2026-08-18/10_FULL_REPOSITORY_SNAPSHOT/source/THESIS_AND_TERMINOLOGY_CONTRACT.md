# Thesis and terminology contract

Status: `PROVISIONAL_RECONCILED_WITH_LIVE_V13_REFERENCE_EXACT_BYTES_PENDING`

Recorded: 2026-08-17

This contract preserves the owner's current intent and has been reconciled with the complete rendered content of the owner-designated live v13 reference. It is a writing and review constraint, not a declaration that the thesis has been proven. The expected standalone HTML and diagram bytes remain unavailable, so exact-hash and byte-level historical claims are still excluded.

## Provisional thesis under test

> Advanced AI systems need an explicit discrimination layer that decides what information should be acquired, identified, preserved, compared, enriched, weighted, withheld, and updated before generation—and those decisions must remain inspectable, cost-bounded, source-aware, and revisable.

This is the owner's test thesis. The strongest presently defensible research wording is narrower:

> Some evidence-sensitive AI workflows may benefit from an explicit, inspectable responsibility for deciding what context to acquire, compare, enrich, admit, withhold, and update before generation. Whether that responsibility improves outcomes enough to justify its cost is an empirical question.

The difference matters. The first sentence is a serious proposition worth developing; the second is the current maximum claim.

## Central question

> How should an AI system decide what context deserves acquisition, comparison, enrichment, and influence before generation, and how can those decisions be made auditable, economical, and correctable by a human?

Subquestions that operationalize it:

1. Which entities and relationships must remain distinct so that recurrence, authority, support, relevance, and action are not collapsed into one score?
2. Under what task, cost, privacy, and uncertainty conditions should a system acquire more information, answer provisionally, ask for clarification, hold, defer, or refuse?
3. What provenance must survive retrieval, transformation, summarization, and memory updates for a human to inspect and correct the result?
4. What evidence would show that the added layer outperforms simpler retrieval, citation, and review workflows under matched constraints?

## Working title decision

### Main title

**Pattern Recognition: The Discrimination Layer**

### Provisional subtitle

**A visual systems framework for deciding what information deserves acquisition, comparison, enrichment, and influence before AI generates.**

### Serious alternatives

- **Before Generation: A Framework for Context Judgment**
- **Pattern Recognition: An Evidence-Selection Framework for AI**
- **The Context Judgment Layer: What AI Should Notice Before It Answers**

These are alternatives for reader testing, not replacements selected by model preference. No model-generated title score is used.

## Terminology decision receipt

| Field | Receipt |
| --- | --- |
| Current decision | `KEEP_PROVISIONALLY` |
| Term | `discrimination layer` |
| Technical meaning | A bounded responsibility for differentiation, selection, and judgment among information candidates and possible next actions before generation. |
| Meaning explicitly excluded | Social classification, protected-class differentiation, discriminatory treatment, or a claim that the system has human-like discernment. |
| Why retain it now | It is part of the owner's stated framing, appears throughout the live v13 reference, and names the act of keeping unlike judgments separate. |
| Principal risk | In ordinary language, “discrimination” can foreground unjust social treatment or suggest a single ranking function. Both readings could obscure the intended thesis. |
| Mitigation | Define the technical meaning at first use; make the excluded meaning explicit; never use the term to excuse unfair classification; keep the underlying dimensions visible rather than collapsing them into a master score. |
| Evidence available | Owner premise; complete rendered live v13 content, which uses the term for pre-generation sifting and weighting; adjacent-field evidence showing established precedents for the component responsibilities. |
| Evidence still required | Exact standalone v13 byte comparison; representative reader comprehension; accessibility and sensitivity review; comparison with the serious alternatives. |
| Rename trigger | Rename if the exact archive materially contradicts this meaning, readers persistently infer a materially different thesis after the definition, the term hides rather than clarifies the separations, or a less ambiguous term preserves the historical idea without loss. |
| Keep trigger | Keep if exact-source review remains consistent with the live reference and target readers can accurately restate both the pre-generation responsibility and the distinction between its separate judgments. |
| Decision authority | Owner after reviewing the recovered v13 material and the local five-minute reader experience. |
| Next review point | After the five-minute local reader test; repeat if the exact standalone archive arrives. |

### Title problem versus thesis problem

A **title problem** exists if the underlying proposition is understandable but the phrase “discrimination layer” causes avoidable confusion. It may be addressed by retitling and a terminology note.

A **thesis problem** exists if the proposed responsibility cannot be distinguished from ordinary retrieval, ranking, provenance, verification, or human review; if no coherent boundary can be specified; or if evaluation shows that separating the responsibility adds cost without meaningful benefit. A new title cannot solve that.

## Non-negotiable distinctions

| Term | Working definition | Must not silently become |
| --- | --- | --- |
| Attention priority | The urgency or salience of inspecting an item within a bounded task. | Truth, authority, or importance in every context. |
| Source authority | A source's domain- and claim-scoped competence or standing. | Universal trustworthiness or permission for the system to act. |
| Operational authorization | Permission to acquire, transform, disclose, retain, or act on information in a defined context. | Evidence that a claim is true or that a source is authoritative. |
| Claim support | The relationship between a specific claim and cited evidence, including support, contradiction, insufficiency, or uncertainty. | Source popularity, document-level reputation, or model confidence. |
| Independence | The degree to which observations or reports arise from distinct origins, methods, or information pathways. | Mere difference in URLs, publishers, or wording. |
| Recurrence | Repeated appearance of a claim, entity, event, or pattern across observations. | Independent corroboration. |
| Relevance | Usefulness to the current question, decision, or constraint. | General importance, truth, or owner endorsement. |
| Action priority | The order or urgency of possible next actions given expected consequence, uncertainty, cost, and authorization. | A factual conclusion about the underlying claim. |
| Owner disposition | An explicit human choice such as accept, reject, defer, hold, override, or request more work. | Proof, objective truth, or permanent preference. |
| Observed metadata | Recorded attributes of an artifact or event as observed, with time and source. | An interpretation, prediction, or derived conclusion. |
| Provenance | Traceable origin, custody, transformation, derivation, agent, and time relationships. | Correctness, authority, independence, or permission. |
| Evidence | Material used to support, refute, or qualify a specific claim under an explicit standard. | Any contextual item placed near a prompt. |
| Context | Material made available to a human or model for a bounded task. | Evidence by default. |
| Enrichment | An authorized operation that obtains or derives additional context, metadata, structure, or evidence. | Acceptance of the enriched material or an unbounded search mandate. |
| Gap | A missing expected perspective, field, observation, or evidence type relative to an explicit baseline. | Any absence noticed without a baseline. |
| Signal candidate | A derived analytical proposition that a pattern may warrant attention or further testing. | A storage folder, a verified event, or a final conclusion. |
| Memory | Versioned retained observations, decisions, outcomes, and/or interpretations with origin and update rules. | A timeless fact store or permission to overwrite prior evidence. |
| Outcome | A defined, observed consequence linked to a prior decision and measurement window. | User satisfaction alone, hindsight narrative, or proof of causality. |

## Layer boundary

“Layer” describes an explicit systems responsibility, not necessarily a single service, model, database, or sequential box. An implementation may distribute it across retrieval, evidence-management, policy, user-interface, and memory components. Conversely, adding a component named `discrimination` does not establish that the responsibility is coherent or effective.

The layer may recommend or route an action. It does not inherit authority to execute an externally consequential action. Domain source authority and operational authorization remain separate.

## What is settled, provisional, and testable

### Settled from the owner's current authorization

- The inquiry concerns judgment before generation, not generation quality alone.
- Decisions should remain inspectable, cost-bounded, source-aware, and human-correctable.
- Historical `Pattern Recognition` terminology must be preserved and examined rather than casually discarded.
- The title and thesis must be evaluated separately.
- Alpha Solver and Signal Foundry are bounded illustrations, not validation.
- Publication is not authorized in this run.

“Settled” here means settled as project intent, not established as a scientific finding.

### Provisional design synthesis

- One explicit responsibility should connect authorization, evidence identity, relationships, multidimensional assessment, routing, human disposition, and outcome feedback.
- Those judgments should remain typed and inspectable rather than compressed into a universal score.
- Raw evidence should remain distinguishable from derived interpretation and later memory.
- A bounded context packet should carry selected content together with reasons, provenance, exclusions, uncertainties, and budgets.

### Empirical hypotheses

- Separating authority, support, independence, relevance, and action priority will improve correction and decision quality relative to a single ranking score.
- Common-origin analysis will reduce false corroboration without suppressing genuine independent recurrence.
- Explicit acquisition and stopping rules will improve evidence quality per unit of time, money, tokens, or reviewer attention.
- Versioned outcome feedback will improve future routing and calibration without laundering owner preference into factual belief.

None of these hypotheses has been tested in this project.

## Prior-art and novelty boundary

The framework does not claim to invent information foraging, relevance feedback, source credibility, claim verification, provenance, evidence synthesis, common-origin control, mixed initiative, value of information, retrieval-augmented generation, context engineering, agent memory, calibration, organizational learning, or decision quality.

Its plausible contribution is the explicit integration of these responsibilities while preserving distinctions that production systems often blur, plus a testable evaluation program for the decision before generation. That contribution is not established until comparison against both the scholarly literature and simpler baselines is complete.

## Exact-archive reconciliation protocol

1. Hash and archive the standalone v13 HTML and diagram byte-for-byte if they arrive.
2. Compare their complete content and rendering with the already inspected live v13 reference.
3. Extract any differing historical terms and claims with exact locations; do not infer owner intent from later project files.
4. Mark material differences in this contract `CONFIRMED`, `NARROWED`, `REPLACED`, or `NOT_PRESENT_IN_EXACT_ARCHIVE`.
5. Preserve important historical wording separately even when it is not retained in v14.
6. Resolve title and terminology only after the owner can review the differences.
7. Record the decision, evidence, dissent, and date without deleting this provisional receipt.

Until that protocol is complete, this file may guide v14 drafting and may cite the live page as the historical reference, but it may not claim exact-byte recovery or equivalence with the expected standalone HTML.
