# Reader outcome and reading-path contract - v15.2

Status: `CURRENT OWNER-REVIEW CONTRACT`

Recorded: 2026-08-19

This contract governs the v15.2 manuscript, current four-route site, and
standalone review export. It does not establish scientific novelty,
effectiveness, usability, or empirical validation. It defines what a reader
should understand, how quickly the public argument should deliver it, and when
technical detail belongs behind progressive disclosure.

The v15.1 contract is preserved as history. Where its time budgets conflict
with this file, this v15.2 contract controls.

## North-star takeaway

> An AI answer inherits earlier choices about what information was found,
> treated as separate evidence, allowed to influence the answer, or left out.
> Those choices should be visible and correctable. Repetition should not be
> mistaken for independent support.

A non-specialist should be able to restate the idea without using
`discrimination layer`, `provenance`, `F0/F1/F2`, `FC_cons`, or `VOR`.

## What the framework adds

The framework proposes one inspectable responsibility before generation:

1. preserve what was observed and what is known about its origin path;
2. keep different judgments separate, especially recurrence, origin relation,
   claim support, authority, relevance, permission, action priority, and the
   owner's decision; and
3. leave a record that a person can question, correct, hold, or defer.

It does not make truth automatic. Its present value is the visibility and
correctability of the path to a bounded answer or action.

## Cumulative public reading stops

| Reader stop | Target time | Required outcome |
| --- | ---: | --- |
| First impression | 60-90 seconds | Understand the concrete nine-reports/one-announcement error; read the `09 / 01 / 00 / HOLD` receipt; understand that zero separately rooted support is a reason to hold or verify, not proof the claim is false. |
| Essential argument | About 4 minutes cumulative | Understand the three governing questions, the AI consequence, the correction invariant, the recorded human next step, and the fact that the framework is proposed rather than validated. |
| Complete public essay | About 9 minutes cumulative | Understand the loops, use boundary, main objections, bounded cases, proposed research bridge, historical v13 anchor, and the promise to preserve unfavorable research outcomes. |

These are cumulative stopping points in one complete argument, not separate
documents and not measurements from a completed reader study. The first stop
must feel useful on its own; the four-minute stop must contain the essential
argument; the nine-minute stop must complete the public essay.

## Optional deeper routes

| Route | Editorial estimate | Role |
| --- | ---: | --- |
| Explore | 15-25 minutes | Inspect the detailed receipt, six families, eleven records, two loops, explanatory visuals, objections, and bounded cases. |
| Lab | 10-20 minutes | Inspect the proposed F0/F1/F2 study, exact measures, all open gates, and locked unfavorable-result interpretations. No result exists. |
| Sources | 10-20 minutes | Inspect prior-art status, source records, the expanded glossary, and the historical record. |
| PDF companion | 15-25 minutes | Review visual hierarchy and research boundaries quickly. HTML and Markdown remain canonical. |

No deeper route may be required to understand the main proposition. Lab must
read as an honest proposed test, never as the thought piece's conclusion or a
results surface.

## Plain-language-first rule

Every visible sentence must remain understandable if the interactive
explanation is ignored. A popup or glossary may deepen comprehension; it may
not rescue opaque prose.

| Avoid as the first explanation | Use first | Technical detail may then reveal |
| --- | --- | --- |
| `F0/F1/F2` | three versions of the same fictional evidence task | descriptive baseline, rule-only comparator, and supplied-origin-label condition |
| `T1` | an optional later real-syndication transfer check | descriptive, rights- and annotation-gated transfer challenge outside confirmatory denominators |
| `A=300` or `N=300` | 300 planned fictional test cases | assigned primary denominator and provisional planning value, not a result |
| `M=75` | a fixed planned 75-case safety subset inside the 300 cases | frozen restricted-manifest membership, safety denominator, and unresolved interval/coverage gate |
| `FC_cons` | a conservative risk measure that counts invalid answers and valid overclaims separately | all-assigned composite and required decomposition |
| `VOR` | a safety check for whether the answer still uses at least two test-stipulated support roots where the fixed subset says they exist | benchmark-scoped valid-origin recall guardrail; not real-world independence |
| `locked negative-result commitment` | a promise made before the study to keep and report failure, harm, or shortcut use as honestly as success | null, rule-only, invalidity-driven, harmful, unstable, fragile, non-transfer, audit-failure, and quarantine dispositions |
| `provenance audit` | an inspection of where material came from and how it changed | origin, custody, derivation, agent, transformation, and time |
| `system runtime` | actual running software | an implemented system rather than an illustration, protocol, or generated mockup |
| `disposition` | a recorded human decision such as accept, reject, hold, or defer | typed owner-disposition state |
| `DPND / INDP / UNKN` | shared or derived path / separate only by the fictional benchmark's stipulation / unresolved | relation-state codes; unresolved is never guessed into independence |
| `offline harness` | local test machinery that has not called a model | generator, parser, validators, scoring, diagnostics, and receipts |

## Interactive explanation contract

Use progressive disclosure only for concepts that are important and likely to
interrupt a thoughtful non-specialist.

Each explanation contains:

1. a one-sentence plain-language definition;
2. one concrete example grounded in the nine-reports/one-announcement case;
3. a boundary explaining what the term does not mean; and
4. a compact visual only when a relationship becomes materially clearer.

The interaction must:

- use semantic, keyboard-focusable controls;
- work without hover and remain useful on touch devices;
- expose expanded state and an explicit close control;
- return focus to the trigger after Escape or close;
- preserve reading position;
- have an in-flow fallback where native popover behavior is unavailable;
- avoid requiring JavaScript for the core explanation; and
- remain legible in print and forced-color contexts.

The v15.2 code-native visuals are supplementary. Generated rasters may
illustrate a bounded example or preserve history, but they must not define a
current component, mandatory pipeline, truth state, or empirical result.

## Reader acceptance test

After the four-minute stop, a reader unfamiliar with the project should be
able to answer:

1. What mistake does the framework try to prevent?
2. Why can nine reports fail to provide nine separately rooted supports?
3. Why does `00` support lead to `HOLD` rather than `FALSE`?
4. What should become visible and correctable before an AI answer is written?
5. Who can correct, hold, or defer the resulting judgment?
6. Has the framework or proposed mechanism been empirically validated?

The minimum passing response is materially equivalent to:

> The framework makes hidden choices before an AI answer inspectable. It keeps
> all nine observations while refusing to treat copied or derived reports as
> separate corroboration. If the broad claim lacks separately rooted support,
> it holds or verifies instead of automatically declaring the claim false. A
> person can correct the record or next action. The idea is developed and
> testable, but the proposed model study has not run.

If readers cannot give an equivalent answer, the problem is content or
information architecture, not glossary coverage.

## Research-status acceptance test

A reader who opens Lab must be able to state all of the following:

- no model or tokenizer is selected;
- no pilot or primary study has run;
- `A=300` and `M=75` are provisional design values, not findings;
- protocol v1.0 remains canonical and v1.1 is a non-authorizing amendment
  draft;
- every material gate remains open;
- a complete gate receipt does not itself authorize execution; and
- null, rule-only, invalidity-driven, harmful, shortcut, audit-failure,
  unstable, fragile, non-transfer, and stopped outcomes remain reportable.

Failure on any item blocks a claim that the research surface is ready for
owner review.

## Longer-term value ladder

| Output | Current status | What would make it stand on its own |
| --- | --- | --- |
| Authored thought piece | Strong local owner-review candidate | Owner voice/comprehension pass, several real cold readers, and final copy edit |
| Practitioner framework | Credible proposal | Reusable receipt/template plus evidence that other practitioners apply it consistently |
| Open design/tooling project | Strong candidate | Curated repository, stable schema, examples, tests, documentation, license, and contribution rules |
| Empirical research paper | Serious narrow program; no result | Accepted protocol amendments, closed gates, selected/frozen model and tokenizer, registration, completed run, full unfavorable-result reporting, and replication artifacts |
| Product capability | Promising design hypothesis | Bounded workflow integration measuring benefit, cost, error, and human correction behavior |

The thought piece must not pretend to be the paper. The paper must not claim to
validate the full framework. A product must not inherit authority from either
without operational evidence.
