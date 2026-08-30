# Enterprise translation and limits

Status: requirements-oriented translation, not enterprise readiness or validation.

The framework could be relevant wherever an AI assistant is asked to assemble context for a consequential decision. That possibility is useful only if the organization treats selection as a governed decision rather than a hidden retrieval score.

## Candidate contexts

| Context | Bounded use | Particular risk |
| --- | --- | --- |
| Internal research | Build a traceable packet of relevant internal and external sources before synthesis. | Sensitive documents may be over-shared or stale; organizational consensus may be mistaken for truth. |
| Decision support | Separate evidence support, uncertainty, values, and action options. | A technically supported claim can still lead to a poor decision under the wrong objective. |
| Competitive intelligence | Track claims, origins, recurrence, and change over time. | Coordinated promotion, rumor, selective disclosure, and legal restrictions. |
| Policy and compliance research | Preserve jurisdiction, effective date, authority, exceptions, and version. | A source authoritative in one jurisdiction or date may be irrelevant in another. Human legal review remains necessary. |
| Product discovery | Group recurring needs and objections while preserving source and owner context. | Engagement and frequency can be mistaken for demand or value. |
| Technical evaluation | Compare vendor claims, benchmarks, methods, and implementation constraints. | Vendor-authored evidence may support a narrow description but not independent effectiveness. |
| Knowledge management | Maintain identity, provenance, derivation, retention, and revision state. | Old summaries can launder stale or low-authority information into trusted memory. |
| Incident and risk analysis | Assemble timelines, contradictions, gaps, and hypotheses without overwriting raw evidence. | Temporal leakage, access restrictions, legal holds, and premature causal claims. |
| Evidence-sensitive AI assistance | Give generation a bounded, cited, revisable context packet. | Retrieved relevance may be confused with permission, support, or authority. |

## Minimum enterprise control envelope

### Authorization and access

- Define who may acquire, inspect, enrich, retain, export, or act on each source class.
- Keep role-based access separate from epistemic authority: permission to read a record says nothing about whether it supports a claim.
- Preserve tenant, team, matter, and purpose boundaries; deny cross-boundary retrieval by default.
- Record human overrides with role, rationale, time, and scope.

### Privacy and sensitive-source handling

- Classify content before retrieval and before model exposure.
- Minimize copied content; prefer pointers and redacted extracts where a full artifact is unnecessary.
- Define consent, purpose limitation, retention, deletion, legal hold, and incident response.
- Treat private, deleted, unavailable, and unauthorized sources as typed gaps—not factual absences.
- Prevent sensitive inputs from becoming reusable model memory without explicit authority.

### Lineage and reproducibility

- Preserve source identity, artifact identity, version, content digest, observation time, event time, and transformations.
- Record model, prompt, retrieval policy, tool, parser, and framework versions for derived output.
- Keep raw observations immutable; append corrections, interpretations, and dispositions.
- Reproduce a decision from the exact evidence snapshot and exclusion log that existed at the time.

### Cost and stopping

- Allocate money, latency, token, human-attention, and privacy budgets to a named decision.
- Define safe retry, quota, cooldown, and failure behavior.
- Use a reasoned stopping policy; do not present budget exhaustion as evidentiary sufficiency.
- Escalate low-probability, high-severity gaps even when average value-of-information appears low.

### Review, action, and failure

- Separate evidence quality from decision utility and authorization to act.
- Support accept, reject, defer, request-more-evidence, override, and abstain states.
- Preserve disagreement and minority evidence instead of forcing premature consensus.
- Fail closed on broken identity, provenance, access, or receipt checks for consequential actions.
- Provide rollback and correction paths for parsers, providers, source identities, prompts, models, and policies.

### Common origin and coordinated amplification

- Track syndication, citations, shared datasets, ownership changes, and apparent copying.
- Represent independence as `INDEPENDENT`, `RELATED`, or `UNKNOWN`; never infer independence from source count alone.
- Treat coordination as a hypothesis requiring evidence. Authentic collective action and legitimate consensus are not automatically manipulation.
- Test whether summaries or trusted tools strip origin and elevate low-authority material.

### Outcome measurement

Measure outcomes tied to the actual decision rather than system activity:

- supported-claim and unsupported-claim rates;
- appropriate abstention and over-refusal;
- reviewer agreement on framework dimensions;
- time to correction;
- source diversity and common-origin errors;
- provenance completeness;
- cost and lead time per accepted decision packet;
- missed high-value or high-severity evidence;
- override frequency and override outcomes;
- calibration and drift by task, source class, and affected group.

Throughput, document count, retrieval count, queue completion, or model fluency are not sufficient outcome measures.

## Tensions that cannot be solved by adding controls

- Immutable audit history conflicts with deletion and minimization requirements.
- Broad retrieval improves recall but increases privacy exposure, cost, and noise.
- Authority priors can improve efficiency while entrenching institutional bias.
- Common-origin discounting can reduce false corroboration while hiding real consensus.
- Human approval can improve accountability while creating delay or rubber-stamping.
- Standardization improves repeatability while suppressing domain-specific judgment.

An enterprise implementation must make these trade-offs explicit for a named use case. The framework does not supply a universal policy.

## Maturity statement

No enterprise pilot, security assessment, privacy assessment, compliance opinion, human-factors study, or decision-quality evaluation was performed in this run. The material above is a requirements map and research agenda. It does not support claims of readiness, compliance, security, reliability, return on investment, or validation.
