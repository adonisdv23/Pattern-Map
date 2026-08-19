# Implementation choices

The framework is useful only if its amount of structure matches the decision.
Choose the smallest route that leaves the important distinctions inspectable.
No stack, provider, model, graph, database, or service is mandatory.

## Three implementation levels

| Level | Best fit | Inputs | Outputs | Typical cost | Stop condition | Main risk |
| --- | --- | --- | --- | --- | --- | --- |
| Lightweight | Low-stakes, short-lived, supplied-material tasks where a wrong answer is easy to correct | A question, a small evidence set, one permission note, and a time limit | One decision brief, one evidence/uncertainty table, one disconfirmation note, one influence receipt | Minutes and ordinary human attention; no new software required | One alternate route or one comparison is complete, or the stated time limit is reached | Too little traceability when consequences rise |
| Moderate | Repeated work or decisions where identity, comparison, and correction matter | Stable IDs, source/artifact records, typed relationships, budget, human checkpoint | Versioned evidence register, comparison/gap record, context packet, disposition, outcome review | Setup and review overhead; documents, spreadsheets, or a small store | Route-specific marginal value is low, budget is reached, or human gate is required | Ceremony and stale records |
| Advanced | Consequential, high-volume, or long-lived workflows with approved engineering capacity | Structured data, access policy, provenance, relationship and time-series views, routing policy, review roles | Queryable lineage, typed graphs, policy receipts, replayable packets, versioned learning proposals | Engineering, privacy, security, operations, and evaluation cost | Hard safety/permission stop, policy threshold, or approved matched-budget evaluation boundary | False precision, automation bias, and expensive bureaucracy |

## Lightweight route

Use this route when the task is reversible, the evidence is bounded, no
sensitive or paid acquisition is needed, and a person can quickly correct the
answer.

1. Write the decision and intended use in two sentences.
2. State what is allowed, what is not allowed, and the time limit.
3. List the default path and one bounded alternate path.
4. Record each source’s role and what it actually supports.
5. Compare at least one relevant peer, period, or alternative explanation, or
   state why no comparison is possible.
6. Record one missing expected item and call it unknown when the boundary does
   not support an absence claim.
7. Search for one strongest disconfirming or limiting item.
8. Give a provisional answer or stop with the uncertainty visible.

The lightweight route is not “skip all discipline.” It is the minimum set of
records that prevents a low-stakes task from turning a fluent guess into an
uninspectable fact.

## Moderate route

Use this route when the work repeats, multiple people review it, the source
set changes over time, or the decision deserves a reproducible packet.

- assign decision, source, artifact, claim, route, and packet IDs;
- retain capture and failure receipts;
- separate source authority, claim support, relevance, origin, and permission;
- preserve a comparison matrix and typed gap states;
- record a route proposal and stop reason;
- require human disposition before consequential influence or action;
- retain the original packet and create a later outcome review.

Suitable representations include a set of Markdown files, a spreadsheet,
ordinary database tables, a document store, or a small application. The
representation matters less than keeping the fields and relationships
inspectable.

## Advanced route

Use this route only when the cost of hidden upstream mistakes justifies the
engineering and governance burden. Add capabilities selectively:

- source/artifact/version/derivation lineage;
- claim and relationship storage with explicit UNKNOWN states;
- baseline and time-series views;
- access, retention, and disclosure policy checks;
- route planning with action, cost, consequence, and stop fields;
- review queues with correction and override history;
- packet replay from the exact evidence snapshot;
- outcome review and approved policy-update workflow;
- evaluation that includes ordinary baselines and harmful or over-refusal
  outcomes.

Advanced does not mean autonomous. A service may propose a route while a human
still authorizes acquisition, disclosure, or externally consequential action.

## Selection rubric

Choose a higher level only when at least one condition is true:

- the decision is difficult to reverse;
- the cost of a wrong or unsupported claim is material;
- multiple sources or contributors must be reconciled;
- the evidence changes and must be re-run or audited;
- a missing perspective or origin relation could change the decision;
- the output will be reused as memory;
- a human must review or authorize the route;
- later outcomes are important enough to compare with expectations.

Stay lightweight or do not use the framework when:

- the task is a creative transformation of supplied text and no factual claim
  is added;
- the output is disposable and easily corrected;
- the user has supplied the complete bounded context and asks only for
  formatting or translation;
- no new acquisition, comparison, or external influence decision is needed;
- the cost of recording the route exceeds the consequence of being wrong.

## Stack-neutral interface

Any implementation should be able to expose these logical interfaces:

| Interface | Minimum question |
| --- | --- |
| Brief | What are we deciding, for whom, with what authority and budget? |
| Acquire | What did we try, was it permitted, and did it succeed? |
| Evidence | What exact item supports which claim, and what is unknown? |
| Compare | Which records are being compared, under which definition and baseline? |
| Route | Why this next action, and why stop or escalate now? |
| Influence | What was allowed to shape the answer, and what was withheld? |
| Disposition | Who accepted, rejected, held, corrected, or overrode what? |
| Outcome | What was expected, what happened, and what bounded update is proposed? |

If a technology cannot expose these questions, adding it does not by itself
create a discrimination layer.
