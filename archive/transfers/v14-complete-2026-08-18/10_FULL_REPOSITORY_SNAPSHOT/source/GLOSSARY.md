# Working glossary

Status: `PROVISIONAL_RECONCILED_WITH_LIVE_V13_REFERENCE_EXACT_BYTES_PENDING`

This glossary is the compact reference for v14 drafting and implementation discussion. The fuller terminology rationale and decision receipt are in `THESIS_AND_TERMINOLOGY_CONTRACT.md`. It has been reconciled with the rendered live v13 reference; exact standalone-source comparison remains pending.

| Term | Working meaning | Boundary |
| --- | --- | --- |
| Acquisition | Authorized retrieval or collection of an information candidate. | Acquiring is not accepting, believing, or publishing. |
| Action priority | Task-scoped ordering of possible next actions using consequence, uncertainty, cost, and permission. | Not a factual verdict. |
| Artifact | A bounded retrievable object or captured representation, identified independently of its source. | One source can issue many artifacts; one event can produce many reports. |
| Attention priority | Task-scoped urgency or salience for inspection. | Not truth, authority, or universal importance. |
| Authority | Domain- and claim-scoped competence or standing of a source. | Not universal trust and not operational authorization. |
| Claim | A proposition capable of being supported, contradicted, qualified, or left unresolved. | Not identical to a document, passage, or model response. |
| Claim support | Typed relationship between a claim and evidence. | Not source popularity, recurrence, or confidence alone. |
| Cohort | A role or analytical grouping assigned under explicit criteria. | Need not be a separate storage system or permanent identity. |
| Common origin | A shared upstream report, study, event, press release, dataset, or information pathway. | Different URLs or wording do not establish independence. |
| Comparison | Deliberate alignment of comparable claims, observations, sources, or alternatives. | Juxtaposition alone does not establish equivalence. |
| Context | Material made available for a bounded task. | Context is not automatically evidence. |
| Cost boundary | A stated limit on money, time, latency, tokens, compute, privacy exposure, or human attention. | A budget does not itself define the right utility. |
| Discrimination | Technical differentiation, selection, and judgment among information and actions. | Does not denote social discrimination or protected-class treatment here. |
| Disposition | Explicit human or policy state such as accept, reject, hold, defer, override, or request enrichment. | Not proof or a timeless preference. |
| Enrichment | Authorized work that adds context, metadata, structure, or evidence. | Its priority is not acceptance; it must have a stopping condition. |
| Enrichment value | Expected task-specific benefit of one more permitted operation, considered with cost and risk. | Not action priority, acceptance, certainty, or authorization. |
| Evidence | Material used in a typed relationship to support, refute, or qualify a claim under an explicit standard. | Not all context is evidence. |
| Evidence spine | Identity, capture, version, custody, derivation, and citation records that let evidence be traced. | Traceability does not establish correctness. |
| Gap | Missing expected material relative to an explicit baseline or comparison frame. | Absence without a baseline is not meaningful absence. |
| Independence | Distinctness of origin, method, or information pathway. | Not the number of sources or repetitions. |
| Influence | The bounded effect allowed to a context item on routing, judgment, or generation. | Influence is not permanent trust or permission to act. |
| Memory | Versioned retained observations, dispositions, outcomes, and interpretations with provenance. | Not a timeless fact store; prior states should not be silently overwritten. |
| Normalization | Creation of comparable representations while preserving original identity and transformation history. | Must not erase material differences or provenance. |
| Observed metadata | Attributes recorded as observed, with source and time. | Not interpretation or prediction. |
| Operational authorization | Permission to acquire, process, disclose, retain, or act. | Not evidence of truth or source competence. |
| Outcome | Defined consequence observed in a specified measurement window and linked to a decision. | Not necessarily causal proof. |
| Provenance | Origin, custody, derivation, agent, transformation, and time relationships. | Not truth, support, relevance, independence, or authorization. |
| Recurrence | Repeated appearance across observations. | Not independent corroboration. |
| Relevance | Usefulness to the present question, decision, or constraint. | Not general importance or truth. |
| Signal candidate | Derived proposition that a pattern may warrant attention or testing. | Not a folder, verified event, or conclusion. |
| Source | An agent, organization, system, or origin that issues or makes an artifact available. | Source identity is distinct from artifact identity. |
| Stopping rule | An inspectable policy for ending acquisition or computation given expected value, uncertainty, and cost. | Stopping does not imply certainty. |
| Withholding | Deliberate exclusion from influence or output for a stated reason. | Does not require deleting the underlying evidence. |

## Preferred state words

Use explicit states instead of vague labels such as “good,” “trusted,” or “important”:

- `OBSERVED`, `IDENTIFIED`, `RELATED`, `ASSESSED`
- `AUTHORIZED`, `NOT_AUTHORIZED`, `HELD`, `EXCLUDED`
- `SUPPORTED`, `CONTRADICTED`, `INSUFFICIENT`, `UNKNOWN`
- `ACCEPTED`, `REJECTED`, `DEFERRED`, `OVERRIDDEN`
- `PROVISIONAL`, `STALE`, `SUPERSEDED`, `FAILED`

State vocabularies may differ by object type. A source should not be marked `SUPPORTED`; a claim should not be marked `AUTHORIZED` when what is meant is that an operation on it is permitted.
