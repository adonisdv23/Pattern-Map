# Applied-framework glossary

Status: v16 working vocabulary for builders and operators. Terms describe
records and decisions; none is a universal truth score.

| Term | Working meaning | Boundary |
| --- | --- | --- |
| Acquisition | Authorized retrieval or collection of an information candidate | Acquiring is not accepting, believing, publishing, or acting |
| Action priority | Task-scoped ordering of possible next actions using consequence, uncertainty, cost, and permission | Not a factual verdict |
| Artifact | A bounded retrievable or captured object identified separately from its source | One source can issue many artifacts; one event can produce many reports |
| Attention priority | Task-scoped urgency or salience for inspection | Not truth, authority, or universal importance |
| Authority | Domain- and claim-scoped competence or standing of a source | Not universal trust and not operational authorization |
| Baseline | The explicit prior period, peer set, expected field, or comparison frame against which motion or absence is assessed | A baseline chosen after seeing the result can bias the interpretation |
| Candidate signal | A derived proposition that a pattern may warrant attention or testing | Not a verified event, conclusion, score, or action authorization |
| Claim | A proposition capable of support, contradiction, qualification, or unresolved status | Not identical to a document, passage, or model response |
| Common origin | A shared upstream report, study, event, release, dataset, or information pathway | Different URLs, publishers, or wording do not establish independence |
| Comparison | Deliberate alignment of comparable claims, observations, sources, or alternatives | Juxtaposition does not establish equivalence or causation |
| Context | Material made available to a human or model for a bounded task | Context is not automatically evidence |
| Cost boundary | Stated limit on money, time, latency, tokens, compute, privacy exposure, and human attention | A budget does not by itself define value or sufficiency |
| Disconfirmation | A bounded attempt to find contrary, missing, differently rooted, or limiting material | Failure to find a counterpoint is not proof of the leading interpretation |
| Discrimination Layer | The explicit, inspectable, cost-bounded, and correctable responsibility for differentiating among information candidates and possible next actions before generation | In this project it does not mean protected-class differentiation, discriminatory treatment, or human-like discernment |
| Disposition | An explicit human or policy state such as accept, reject, hold, defer, override, or request enrichment | Not proof, truth, or a timeless preference |
| Enrichment | Authorized work that adds context, metadata, structure, or evidence | Priority is not acceptance; enrichment needs a stop condition |
| Evidence | Material used in a typed relationship to support, refute, or qualify a claim under an explicit standard | Not all context is evidence |
| Evidence spine | Identity, capture, version, custody, derivation, and citation records that let evidence be traced | Traceability does not establish correctness |
| Expected baseline | A declared set of material or condition that should be present for a narrow observation boundary | An unspecified expectation manufactures an absence |
| Gap | Missing expected material relative to an explicit baseline or comparison frame | Absence without a baseline is not meaningful absence |
| Influence | The bounded effect allowed to a context item on routing, judgment, or generation | Influence is not permanent trust or permission to act |
| Independence | Distinctness of origin, method, or information pathway | Not the number of sources, URLs, or repetitions |
| Learning update | A proposed bounded change to a query, baseline, routing rule, source policy, or review rule after an outcome comparison | It is not automatically applied and does not rewrite history |
| Memory | Versioned retained observations, decisions, outcomes, and interpretations with provenance and scope | Not a timeless fact store or permission to overwrite evidence |
| Motion | A rate, direction, or change observed across comparable time-stamped observations against a baseline | Not a forecast, cause, or truth signal |
| Normalization | Creation of comparable representations while preserving original identity and transformation history | Must not erase material differences or provenance |
| Observation | A recorded attribute or event with source and time | Not an interpretation, prediction, or causal explanation |
| Operational authorization | Permission to acquire, transform, disclose, retain, or act on information in a defined context | Not evidence of truth or source competence |
| Origin relation | A typed assertion about shared upstream material or information path, with evidence and uncertainty | Provenance or similarity alone may be insufficient to establish origin |
| Outcome | A defined consequence observed in a specified window and linked to a decision or route | Not necessarily causal proof or user satisfaction alone |
| Permission envelope | Versioned constraints on who or what may acquire, process, retain, disclose, or act | Technical access does not imply permission |
| Provenance | Origin, custody, derivation, agent, transformation, and time relationships | Not truth, support, relevance, independence, or authorization |
| Recurrence | Repeated appearance across observations | Not independent corroboration |
| Relevance | Usefulness to the present question, decision, or constraint | Not general importance, truth, or owner endorsement |
| Route | A bounded next action such as acquire, compare, answer, hold, defer, escalate, or refuse | A route recommendation is not permission to execute externally consequential action |
| Source | An agent, organization, system, or origin that issues or makes an artifact available | Source identity is distinct from artifact identity |
| Stop rule | An inspectable policy for ending acquisition or computation given expected benefit, uncertainty, consequence, and cost | Stopping does not imply certainty |
| Uncertainty | An explicit state about what is unknown, contested, ambiguous, stale, or weakly supported | Not a single model-confidence number |
| Withholding | Deliberate exclusion from influence or output for a stated reason | Does not require deleting the underlying evidence |

## Preferred state words

Use object-appropriate state words instead of vague labels such as good,
trusted, or important:

- Record state: OBSERVED, IDENTIFIED, VERSIONED, RELATED, SUPERSEDED, STALE,
  FAILED
- Permission state: AUTHORIZED, NOT_AUTHORIZED, UNKNOWN, REVOKED
- Claim state: SUPPORTED, CONTRADICTED, QUALIFIED, INSUFFICIENT, UNKNOWN
- Route state: PROPOSED, ALLOWED, HELD, ESCALATED, STOPPED, REFUSED
- Disposition state: ACCEPTED, REJECTED, DEFERRED, OVERRIDDEN,
  REQUEST_ENRICHMENT

Do not mark a source as SUPPORTED, a claim as AUTHORIZED, or a human
preference as FACT. A single record can have one state in each relevant
vocabulary.

## Plain-language translations

| Technical phrase | Plain-language explanation |
| --- | --- |
| Evidence spine | Keep track of what the item is, where it came from, when it was seen, and how it changed |
| Typed relationship | Say exactly whether two things support, contradict, copy, compare, or merely resemble each other |
| Influence receipt | Show what shaped the answer, what was left out, and why |
| Cost-bounded route | Decide what one more search or comparison is worth before spending the time |
| Versioned memory | Keep old observations and corrections visible while making the current view clear |
| Human disposition | Give an accountable person a recorded choice to accept, hold, reject, correct, or ask for more |
