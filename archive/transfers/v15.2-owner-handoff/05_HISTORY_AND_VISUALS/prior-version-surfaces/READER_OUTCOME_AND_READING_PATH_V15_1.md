# Reader outcome and reading-path contract — v15.1

Status: `OWNER_APPROVED_DIRECTION`

Recorded: 2026-08-18

This contract governs the v15.1 manuscript and site. It does not establish that
the framework is scientifically novel or effective. It defines what a reader
should understand, how quickly they should be able to understand it, and when
technical detail belongs behind progressive disclosure.

## North-star takeaway

> An AI answer inherits earlier decisions about what information was found,
> treated as separate evidence, allowed to influence the answer, or left out.
> Those decisions should be visible and correctable. Repetition should not be
> mistaken for independent support.

The reader should be able to restate that idea without using the phrases
`discrimination layer`, `provenance`, `F0/F1/F2`, or `origin accounting`.

## What the framework adds

The framework proposes one inspectable responsibility before generation:

1. preserve what was observed and where it came from;
2. keep different judgments separate, especially repetition, support,
   authority, relevance, permission, and action; and
3. leave a record that a person can question, correct, or hold.

The framework does not claim to make truth automatic. Its value is the
visibility and correctability of the path to a bounded answer or action.

## Reading paths and time budgets

| Reader path | Target time | Required outcome |
| --- | ---: | --- |
| First impression | 60–90 seconds | Understand that many answer failures begin before generation and that nine reports can still trace to one origin. |
| Essential argument | About 5 minutes | Understand the thesis, the worked receipt, the key distinction between recurrence and independent support, and the fact that the framework is proposed rather than validated. |
| Conceptual exploration | 15–20 minutes total | Understand the six families, why the judgments stay separate, the human correction point, and the strongest objections. |
| Research track | Additional 10–15 minutes | Understand the proposed experiment in ordinary language, what remains unfinished, and what outcomes would narrow or reject the tested mechanism. |
| Full technical review | 30–45 minutes or more | Inspect records, protocol details, prior art, receipts, and implementation constraints. This is optional and must not be required to understand the idea. |

The website must make these paths visibly optional. A longer technical route
must never make the five-minute route feel incomplete.

## Plain-language-first rule

The visible sentence must remain understandable if every interactive
definition is ignored. A glossary interaction may deepen comprehension; it may
not rescue otherwise opaque prose.

Required rewrites include:

| Avoid as first explanation | Use first | Technical detail may then reveal |
| --- | --- | --- |
| `F0/F1/F2` | three versions of the same evidence task | baseline, rule-only, and supplied-origin-label conditions |
| `T1` | an optional real-world transfer check | descriptive real-syndication transfer arm |
| `N=300` | 300 test cases | planned primary sample size and experimental unit |
| `locked negative-result commitment` | a promise made in advance to report failure or harm as honestly as success | null, harmful, unstable, and shortcut-driven dispositions |
| `provenance audit` | an inspection of where material came from and how it changed | origin, custody, derivation, agent, transformation, and time |
| `system runtime` | actual running software | the implemented system rather than an illustration or protocol |
| `disposition` | a recorded human decision such as accept, reject, hold, or defer | the typed owner-disposition state |
| `offline harness` | local test machinery that has not called a model | generator, parser, validators, scoring, and receipts |

## Interactive explanation contract

Use progressive disclosure only for terms that are important and reasonably
likely to interrupt a thoughtful non-specialist.

Each interactive explanation must contain:

1. a one-sentence plain-language definition;
2. one concrete example grounded in the nine-reports/one-origin case;
3. a boundary explaining what the term does not mean; and
4. an optional compact visual only when the relationship is clearer visually.

The interaction must:

- work with keyboard, touch, and screen readers;
- identify itself as an explanation rather than an external link;
- open at the first or highest-value occurrence, not every repetition;
- preserve reading position;
- close with Escape and an explicit close control;
- avoid hover-only behavior; and
- remain understandable when JavaScript is unavailable wherever practical.

Useful micro-visuals include:

- nine report tiles converging on one origin;
- three side-by-side task conditions with only the added instruction/labels
  highlighted;
- a 300-case grid grouped into four equal sets of 75;
- a human decision fork showing accept, reject, hold, and defer; and
- a source-to-copy-to-summary lineage showing what a provenance inspection
  follows.

Do not create a visual merely because a term is technical. Definitions such as
`system runtime` need a sentence, not a diagram.

## Reader acceptance test

After the five-minute route, a reader unfamiliar with the project should be
able to answer:

1. What problem is the framework trying to prevent?
2. Why can nine reports fail to provide nine independent supports?
3. What does the proposed responsibility make visible?
4. Who can correct or hold the resulting judgment?
5. Has the framework or its research mechanism been empirically validated?

The minimum passing response is:

> The framework makes the hidden choices before an AI answer inspectable. It
> preserves repeated reports without pretending that copies are independent
> support, and it leaves the resulting judgment open to human correction. The
> idea is developed and testable, but it has not yet been validated by the
> proposed study.

If readers cannot give a materially equivalent answer, the problem is content
or information architecture—not glossary coverage.

## Longer-term value ladder

The project can support several distinct outputs. They must not borrow evidence
from one another silently.

| Output | Current status | What would make it stand on its own |
| --- | --- | --- |
| Authored thought piece | Promising owner-review beta | Distinctive voice, five-minute argument, honest prior-art boundary, and a memorable worked example |
| Practitioner framework | Plausible and close | Reusable receipt/template, two or three bounded field cases, and evidence that other practitioners can apply it consistently |
| Open design/tooling project | Plausible | Stable schemas, examples, tests, documentation, and a curated public repository |
| Empirical research paper | Promising but unproven | Locked study, adequate power, actual model results, transparent null/harm reporting, and replication artifacts |
| Product capability | Plausible opportunity, not validated | Integration into a real workflow plus measured benefit, cost, failure modes, and human correction behavior |

The thought piece should not pretend to be the paper. The paper should not
pretend to validate the full framework. A product should not inherit authority
from either without operational evidence.
