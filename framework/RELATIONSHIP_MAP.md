# Relationship map

Status: current v16 applied-framework topology. This map is a teaching and
implementation aid, not a required sequential architecture. A lightweight
operator may realize it as a few tables; an advanced builder may distribute it
across services. The recovered v13 diagram is historical origin material and is
not reproduced here as the current topology.

## Current v16 map

~~~mermaid
flowchart TD
    A["Decision brief + permission envelope"] --> B["F1 Peripheral signal"]
    A --> C["F2 Source weighing"]
    A --> D["F3 Velocity / motion"]
    A --> E["F4 Absence + memory"]
    A --> F["F5 Structured patterns"]
    B --> G["Evidence register + capture receipts"]
    C --> G
    D --> H["Baseline and motion record"]
    E --> I["Gap and memory record"]
    F --> J["Comparison and origin record"]
    G --> C
    G --> F
    H --> F
    I --> F
    J --> C
    C --> K["Disconfirmation + uncertainty review"]
    F --> K
    K --> L{"Bounded route"}
    L -->|"ACQUIRE / COMPARE / CLARIFY"| B
    L -->|"HOLD / DEFER / ESCALATE / REFUSE"| M["Human disposition"]
    L -->|"ANSWER / ANSWER_PROVISIONALLY"| N["Influence receipt + context packet"]
    M --> N
    N --> O["Generation or human decision"]
    O --> P["Recorded expectation + outcome window"]
    P --> Q["F6 Learning loop"]
    Q -->|"propose bounded update"| M
    M --> A
~~~

The edge labels leaving `Bounded route` are canonical route-field values.
`ANSWER` may produce a packet and `ANSWER_PROVISIONALLY` may produce a
provisional packet, but `packet` and `provisional packet` are output
descriptions, not additional routes. Stop status and learning status remain
separate fields.

## What the arrows mean

| Relationship | Operational meaning | Receipt evidence |
| --- | --- | --- |
| Brief → every family | The decision, audience, stakes, permissions, baseline, and budget scope the work | Versioned decision brief |
| F1 → evidence register | An alternate route creates candidates and capture/failure records | Query/route and acquisition receipt |
| F2 ↔ F5 | Source roles and origin relations change how a comparison is interpreted; neither collapses into the other | Source-role and comparison records |
| F3 → F5 | Motion becomes meaningful through a peer, period, or baseline comparison | Time-series/baseline record |
| F4 → F5 | A gap or prior state can change the comparison set and interpretation | Gap and memory record |
| F5 → F2 | A comparison may expose that two reports share an origin or support different claims | Typed relationship and claim records |
| F2/F5 → disconfirmation | Candidate interpretations are challenged with contrary, missing, or differently rooted material | Disconfirmation log |
| Disconfirmation → route | The next action depends on unresolved uncertainty, consequence, permission, and cost | Route/stop receipt |
| Route → influence packet | Only selected, authorized material and explicit uncertainties are allowed to shape generation | Context/influence receipt |
| Human disposition → any prior stage | A reviewer may correct a relation, revise a brief, change a permission, or override a route; history remains | Disposition and correction event |
| Outcome → F6 | A defined later observation is compared with the earlier expectation and route | Outcome review |
| F6 → disposition | Learning is a proposed, bounded change, not a silent rewrite of policy or fact | Update proposal and approval |

## Family interaction matrix

| Family | Supplies | Receives | Typical question it cannot answer alone |
| --- | --- | --- | --- |
| Peripheral signal | Candidate routes and overlooked material | Decision scope, permission, source weighing | Whether the candidate is true or relevant |
| Source weighing | Claim-scoped roles, support, contradiction, permission state | Exact artifacts, comparisons, domain standard | Whether more acquisition is worth the cost |
| Velocity / motion | Time-relative change prompt | Repeated observations and baseline | Why the change occurred or what will happen next |
| Absence + memory | Gap and prior-state context | Expected baseline, observation boundary, versioned records | Whether a missing item exists outside the boundary |
| Structured patterns | Explicit similarities, differences, and origin relations | Comparable records, definitions, time windows | Whether a pattern is causal or valuable |
| Learning loop | Outcome comparison and bounded update proposal | Pre-outcome expectation, later observation, attribution boundary | Whether a change should be applied without disposition |

## Shared mechanisms across the map

The following mechanisms cross family boundaries:

1. **Decision brief and permission envelope.** Defines the real decision,
   intended use, owner, allowed operations, sensitive-source rules, budget,
   baseline, and escalation condition.
2. **Evidence spine.** Distinguishes source, artifact, capture, version,
   transformation, and exact evidence span. Provenance supports inspection; it
   does not establish correctness.
3. **Typed relationships.** Records support, contradiction, qualification,
   recurrence, common origin, comparison, and unknown separately.
4. **Bounded routing.** Chooses among acquire, compare, clarify, answer,
   provisional answer, hold, defer, escalate, and refuse under cost and
   consequence constraints.
5. **Human disposition.** Allows accept, reject, defer, hold, override, request
   enrichment, correct, or revoke permission; it does not turn a preference
   into an objective fact.
6. **Versioned memory.** Retains prior observations, decisions, corrections,
   and outcomes without making old summaries timeless.
7. **Influence receipt.** Records what was allowed to influence generation,
   what was withheld, why, under which permission, and with what uncertainty.

## Minimum and expanded routes

### Lightweight route

Use one decision brief, one evidence register, one comparison or
expected/observed table, one disconfirmation note, and one influence receipt.
Skip families that have no observable input, but record why they were skipped.

### Moderate route

Add stable IDs, source/artifact identities, typed relationship states, a
versioned context packet, human disposition, and an outcome review.

### Advanced route

Add queryable provenance and claim relationships, time-series or gap tooling,
policy-based routing, access controls, structured review, and approved
matched-budget evaluation. Advanced machinery does not authorize external
action and does not turn a case into validation.

## Removal test

If the common-origin example is removed, this map still has six complete
families, a human permission boundary, comparison, uncertainty, stopping, and
learning. Common-origin analysis is one structured-pattern mechanism and one
worked example, not the definition of the framework.
