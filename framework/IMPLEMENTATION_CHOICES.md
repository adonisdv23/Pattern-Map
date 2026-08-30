# Implementation choices

The framework is useful only if its amount of structure matches the decision.
Choose the smallest route that leaves the important distinctions inspectable.
No stack, provider, model, graph, database, or service is mandatory.

Ordinary is valid only for a reversible transformation of user-supplied
material that requires no material claim judgment, comparison, selection or
withholding, permission resolution, memory reuse, new acquisition, or
externally consequential influence. The four-field ordinary record is
terminal; it is not an ANSWER, route, stop, learning, or influence receipt.
Stage 0 grants no external-action authority; externally consequential action
remains with an explicitly authorized human.

A budget records capacity and constraint; it cannot independently justify
advanced machinery. Advanced is justified only when consequence is high,
uncertainty is high, and substantial capacity has been separately approved;
volume, reuse, or longevity may shape capabilities inside the chosen level but
do not independently select it. Choose the smallest level from those rules,
then use the approved capacity to bound it.

## Three implementation levels

| Level | Best fit | Inputs | Outputs | Typical cost | Stop condition | Main risk |
| --- | --- | --- | --- | --- | --- | --- |
| Lightweight | Low-stakes, short-lived layered tasks where bounded material still requires claim judgment, comparison, selection/withholding, or another Stage 0 disqualifier | A question, a small evidence set, one permission note, and a time limit | One decision brief, one evidence/uncertainty table, one disconfirmation note, one influence receipt | Minutes and ordinary human attention; no new software required | One alternate route or one comparison is complete, or the stated time limit is reached | Too little traceability when consequences rise |
| Moderate | Repeated work or decisions where identity, comparison, and correction matter | Stable IDs, source/artifact records, typed relationships, budget, human checkpoint | Versioned evidence register, comparison/gap record, context packet, disposition, outcome review | Setup and review overhead; documents, spreadsheets, or a small store | Route-specific marginal value is low, budget is reached, or human gate is required | Ceremony and stale records |
| Advanced | Consequential, high-uncertainty layered work with substantial separately approved capacity; all three conditions are required | Structured data, access policy, provenance, relationship and time-series views, routing policy, review roles | Queryable lineage, typed graphs, policy receipts, replayable packets, versioned learning proposals | Engineering, privacy, security, operations, and evaluation cost | Hard safety/permission stop, policy threshold, or approved matched-budget evaluation boundary | False precision, automation bias, and expensive bureaucracy |

These levels preserve v13's practical range without preserving a hierarchy.
They may be realized as a team process, an intermediary reasoning/context or
evidence workflow, or—only with separately approved data, budget, governance,
and evaluation—model adaptation. No path is inherently deeper, more
defensible, or required, and the levels can combine when the decision warrants
it.

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

Use this route only when the work is consequential, uncertainty is high, and
substantial capacity has been separately approved. All three conditions are
required. High volume, long life, repeated use, or available infrastructure
may shape which capabilities are useful after the level is chosen; none of
them independently upgrades a task to Advanced. Add capabilities selectively:

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

After Stage 0 requires a layered path, use these conditions to identify what
must remain inspectable:

- the decision is difficult to reverse;
- the cost of a wrong or unsupported claim is material;
- multiple sources or contributors must be reconciled;
- the evidence changes and must be re-run or audited;
- a missing perspective or origin relation could change the decision;
- the output will be reused as memory;
- a human must review or authorize the route;
- later outcomes are important enough to compare with expectations.

Use Lightweight when the layered task remains reversible and neither high
consequence nor high uncertainty is present. Use Moderate when consequence is
high or uncertainty is high but the complete Advanced conjunction is not met.
Use Advanced only when consequence is high, uncertainty is high, and
substantial capacity is separately approved. The other conditions above shape
the records and capabilities within that level; they do not independently
select Advanced.

Stay lightweight or do not use the framework when:

- an exact, reversible supplied-material transformation satisfies the complete
  ordinary eligibility contract above;
- a bounded supplied-material task requires judgment or selection but its low
  consequence and easy correction make the lightweight route sufficient;
- the output is disposable and easily corrected;
- no advanced failure mode is present;
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
