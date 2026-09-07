# Owner intent — Pattern Map v16

Status: **OWNER-LOCKED INTENT CONTRACT**

Effective date: 2026-08-19

This document records the owner's approved intent for Pattern Recognition / The
Discrimination Layer v16. Agents may improve wording, organization, examples,
implementation detail, and visual treatment, but may not change the underlying
proposition, audiences, six-family scope, two-project separation, or external-
action boundaries without a new explicit owner instruction.

## North star

V16 should feel like an intelligent continuation of the original coffee
conversation. It should help the mentor understand what the author was trying
to express, give the mentor something substantial to challenge or expand, stand
independently for a public reader, help builders design better AI workflows,
and give AI agents a practical alternative to default retrieval-and-generation
behavior. It should remain ambitious without presenting an operating philosophy
as settled science.

## Why v16 exists

The project began as an attempt to continue and clarify a conversation between
the author and his mentor. The author wanted to articulate an idea he had not
fully expressed: stronger AI-assisted work depends not only on generation, but
on the pattern recognition and judgment applied to what is noticed, acquired,
compared, preserved, challenged, and allowed to influence generation.

The early piece later became useful as context for AI tasks. It encouraged
agents to pursue less conventional but still grounded routes: look beyond the
default information path, compare structures, find missing perspectives,
observe motion and expected absence, preserve memory, and learn from outcomes.
The same idea should stand on its own for a thoughtful human reader and should
be operational enough to guide real projects such as Signal Foundry.

V14 through v15.2 increased rigor, research precision, accessibility, and
implementation depth. They also overcorrected. Origin accounting—memorably
illustrated by nine reports tracing to one announcement—became the opening and
apparent definition of the whole framework. V16 must not repeat that drift.
Origin accounting remains a valuable example and separate research track; it
does not govern the broad thesis.

## Primary human reader

The primary reader is the author's intelligent mentor or a thoughtful general
reader. No machine-learning, software-architecture, or research-methodology
expertise should be required. The piece should reward intelligence and
curiosity without making specialist vocabulary the price of entry.

## Secondary readers

Secondary readers include:

- AI product builders and operators;
- researchers and designers;
- people delegating autonomous work to Codex, ChatGPT, Claude, or related
  agents; and
- practitioners deciding how much structure a consequential AI-assisted task
  actually warrants.

## What a human reader must understand

V16 must help a reader understand:

- why generic AI output often begins with generic inputs and default search
  behavior;
- why decisions before generation matter;
- what pattern recognition means operationally;
- what the six historical families do;
- why peripheral material is a candidate starting point, not automatic truth;
- how comparison, motion, absence, memory, source structure, and feedback can
  improve the information environment;
- what decomposable parts of expertise can be scaffolded;
- what remains human judgment; and
- how the framework can be useful without becoming mandatory bureaucracy.

## The six-family lock

All six original families remain visible and meaningful in v16:

1. **Peripheral signal** — deliberately look beyond the obvious or dominant
   information path while treating underweighting as a reason to inspect, not a
   reason to believe.
2. **Source weighing** — distinguish recurrence, source role, track record,
   authority for a claim, origin relation, and actual support rather than using
   one universal trust score.
3. **Velocity / motion** — notice unusual rates or directions of change against
   a relevant history or comparison set; motion is a prompt for examination,
   not a conclusion.
4. **Absence + memory** — notice expected-but-missing material against an
   explicit baseline and preserve prior observations, decisions, and context so
   the present is not interpreted without history.
5. **Structured patterns** — compare peers, periods, attributes, structures,
   and relationships explicitly enough to expose recurrence, difference, and
   missing perspective without forcing unlike cases into false equivalence.
6. **Learning loop** — compare later outcomes with recorded expectations and
   propose bounded updates without silently rewriting the original evidence or
   turning local preference into fact.

V14/v15 operational components may sit beneath or across these families. They
must not replace the six families as the reader-facing map.

## What builders must receive

V16 must let builders translate the idea into:

- a process;
- an agent workflow;
- a context or evidence layer;
- inspectable records and decision points;
- bounded product capabilities; and
- testable research questions.

The framework must offer lightweight, moderate, and advanced implementation
choices. It must include failure modes, stopping rules, cost boundaries, and
clear guidance about when not to use it. A named technical layer, service,
graph, model, or prompt is never mandatory merely because the framework can be
implemented that way.

## What agents must be able to do

The agent companion must specify observable procedures rather than inspirational
commands to “think differently.” It must tell an agent to:

1. define the real decision;
2. search beyond the obvious;
3. identify missing perspectives;
4. compare relevant peers, periods, structures, and sources;
5. examine velocity and expected absence;
6. separate observation from interpretation;
7. trace recurrence and common origin where relevant;
8. seek disconfirming material;
9. preserve uncertainty instead of filling gaps;
10. decide whether more research is worth its cost;
11. record why material influenced the answer; and
12. compare later outcomes with expectations and propose bounded updates.

The companion must also define acquisition, comparison, disconfirmation,
uncertainty, escalation, cost, stop, and learning procedures; distinguish
permission from technical ability; and leave externally consequential actions
under explicit human authority.

## Human judgment boundary

V16 may scaffold decomposable practices such as comparison, source tracing,
baseline construction, memory, gap detection, and outcome review. It must not
claim to replace expertise, taste, accountability, contextual judgment, or
novel-situation sensemaking. Raising a floor of disciplined practice is not the
same as automating the ceiling of expert judgment.

## Provisional editorial center

> AI slop often begins before the model writes a word. It begins with
> predictable search paths, familiar sources, flattened context, missing
> comparisons, unexamined assumptions, and no memory of what previously worked
> or failed. The answer inherits those upstream choices. Pattern recognition is
> the discipline of improving those choices. The Discrimination Layer is the
> explicit, inspectable, and correctable responsibility for deciding what the
> system should notice, compare, preserve, question, and allow to influence
> generation.

The writing team may improve this wording, but it may not change the underlying
proposition without recording the proposed change, explaining the governing
reason, and obtaining a new explicit owner instruction.

## Voice and reading experience

The piece should feel like a thoughtful person continuing a serious
conversation—not like an academic committee document, a software sales page,
a protocol preamble, or a machine-generated taxonomy. The human problem comes
first. Concrete experience precedes technical abstraction. Counterarguments and
research boundaries arrive after the reader understands the idea. Technical
depth remains available through progressive disclosure rather than crowding the
main line of thought.

The canonical essay should take roughly 10–15 minutes to read. A cumulative
60–90-second version should carry the broad idea without reducing it to origin
accounting. The mentor cover note should invite challenge and expansion rather
than announce a finished theory.

## Permanent separation from The Echo Problem

V15.2 is the source checkpoint for **The Echo Problem: When Repetition
Masquerades as Corroboration**, internal code ECHO-01. V15.2 remains historically
unchanged. The curated successor begins at EP v0.1 and preserves its no-results
boundary, protocol, harness, fixtures, prior art, and every unfavorable-result
class.

V16 may link to The Echo Problem and may use common-origin recurrence as one
worked example. A reader must still be able to understand the broad v16 thesis,
all six families, and the agent workflow if that example is removed.

## Non-goals

V16 is not:

- a claim that the six families are newly invented;
- a completed empirical paper;
- a universal mandatory architecture;
- a provenance-only or origin-accounting-only framework;
- a magical-creativity prompt;
- a replacement for human expertise;
- a claim that peripheral material is true or better because it is peripheral;
- an authorization to deploy, publish, merge, run research, or act externally.

## External-action boundary

Repository organization, feature branches, isolated worktrees, scoped commits,
pushes, and draft pull requests are authorized for owner review. Merging to
`main`, deployment, public-site replacement, publication, a GitHub Release,
empirical or participant study activity, provider/model selection or calls,
spending, external-dataset acquisition, preregistration, outreach, and any
representation of unrun research as a result remain prohibited without a later
exact owner instruction.

## Change control

Any proposed intent change must be entered in `docs/DECISION_LOG.md` as
`PROPOSED — OWNER DECISION REQUIRED`, quote the affected clause, explain the
reason and downstream impact, and leave canonical artifacts unchanged until
the owner explicitly decides. No agent review, empirical concern, design
preference, or implementation convenience can silently unlock this contract.
