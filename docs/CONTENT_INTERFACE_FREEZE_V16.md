# V16 content interface freeze

Status: **FROZEN FOR LOCAL SITE IMPLEMENTATION**

Freeze basis: `2b8bd1b1c93ab5e38ecc60bf940e0519c537bb73`

This contract is the handoff between the converged human, builder, agent, and
research artifacts and the local v16 site. It freezes meaning and hierarchy,
not a visual layout or JavaScript architecture. The site may improve
navigation, pacing, responsive presentation, and plain connective copy. It may
not introduce a different thesis, rename or reorder the six-family public map,
turn The Echo Problem into the opening, imply validation, or make technical
popovers necessary to understand the idea.

The machine-readable companion is
[`CONTENT_INTERFACE_V16.json`](CONTENT_INTERFACE_V16.json). When this document
and the JSON disagree, the locked owner intent and canonical source artifacts
govern; the disagreement must be corrected before site integration.

The JSON is a complete explicit manifest for the site-facing source files at
this checkpoint, not merely a list of directory indexes. Adding or removing a
canonical site source requires updating both forms and passing the content-
interface validator.

## First screen

The first screen must begin with the human problem and broad upstream-choice
thesis. It may not lead with a protocol, disclaimer, literature defense,
provenance graph, research status, or Echo example.

**Approved headline**

> AI slop often begins before the model writes a word.

**Approved standfirst**

> A polished answer can still feel generic when the system follows the obvious
> search path, misses a specialist perspective, skips a useful comparison,
> overlooks an expected absence, or forgets what happened before. The answer
> inherits those upstream choices. Pattern Recognition is the discipline of
> improving them.

This is owner-approved conceptual framing, not a measured prevalence or model-
internal causality claim. The site must not present it as a research result.

The first screen must also expose all three principal doors. On a desktop they
should be visible in the initial composition; on narrow screens they may stack
immediately after the standfirst without forcing decorative media ahead of
them.

## Three principal doors

### 1. Read the idea

**Promise:** Continue the coffee conversation: why choices made before
generation shape what an answer can become.

**Canonical sources, in order:**

1. `manuscript/NINETY_SECOND_VERSION.md` for the cumulative short entry;
2. `manuscript/PATTERN_RECOGNITION_V16.md` for the complete thought piece;
3. `manuscript/MENTOR_COVER_NOTE.md` as a distinct personal handoff, not the
   public article opening; and
4. `manuscript/PUBLIC_ABSTRACT.md` for metadata and concise public context.

The full essay remains the canonical human piece. It may be divided into
semantic sections for navigation, but the site may not silently abridge it or
interleave builder protocol into its reading flow.

### 2. Explore the map

**Promise:** See six ways to improve what the system notices, compares,
preserves, questions, and learns from.

**Canonical sources:**

- `framework/SIX_FAMILIES.json` for IDs, slugs, names, questions, boundaries,
  and ordering;
- `framework/SIX_FAMILIES.md` for the complete reader/builder explanation;
- `framework/RELATIONSHIP_MAP.md` for the current v16 topology; and
- `framework/GLOSSARY.md` for optional plain-language and technical detail.

The public order is fixed:

1. F1 — Peripheral signal;
2. F2 — Source weighing;
3. F3 — Velocity / motion;
4. F4 — Absence + memory;
5. F5 — Structured patterns; and
6. F6 — Learning loop.

The map should teach a connected movement: widen the aperture, weigh what
enters, compare across time and structure, preserve meaningful gaps and prior
state, then learn without rewriting history. It is not a mandatory sequential
pipeline.

### 3. Apply it

**Promise:** Turn the idea into a proportionate workflow, from one decision
brief to an inspectable agent procedure.

**Canonical sources:**

- `framework/OPERATOR_PLAYBOOK.md`;
- `framework/IMPLEMENTATION_CHOICES.md`;
- `framework/BOUNDARIES_AND_FAILURES.md`;
- `framework/agent-playbook/QUICKSTART.md`;
- `framework/agent-playbook/FULL_OPERATING_GUIDE.md`;
- `framework/agent-playbook/COPYABLE_AGENT_BRIEF.md`;
- `framework/agent-playbook/PREFLIGHT_CHECKLIST.md`;
- `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md`; and
- `framework/templates/**`.

The ordinary, lightweight, moderate, and advanced routes must stay visible.
The site must not suggest that every task needs the full framework or that one
stack, database, graph, provider, or custom model is required.

## Secondary routes

The site may expose these after or alongside the three doors:

| Route | Purpose | Canonical source |
| --- | --- | --- |
| Examples | Show peripheral/specialist signal, velocity or expected absence, common-origin recurrence, Signal Foundry, and two neutral cases | Essay worked examples; `cases/**`; agent ordinary-vs-layered example |
| Boundaries | State when the framework should shrink or disappear and preserve permission, uncertainty, human authority, and claim limits | `framework/BOUNDARIES_AND_FAILURES.md`; `docs/ARTIFACT_BOUNDARIES.md` |
| Sources | Offer a targeted, non-exhaustive route without turning the essay into a literature review | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md`; `docs/CLAIMS_AND_SOURCE_LEDGER_V16.md` |
| Research | Explain the unrun research agenda and link to Echo as separate Track 01 | `research/README.md`; broader agenda; future protocol; Echo README/status |
| History | Explain v13 continuity and the v14–v15.2 lineage | `manuscript/ORIGIN_NOTE.md`; `docs/SOURCE_AUTHORITY_AND_LINEAGE.md`; archive indexes |

## Progressive disclosure

The essential idea must survive with JavaScript disabled, popovers closed, and
the page printed. A reader must be able to understand the human problem, the
definition, all six family names and questions, the human-judgment boundary,
and the three application levels from visible text.

Popovers or expandable details may explain terms such as evidence spine,
typed relationship, influence receipt, cost-bounded route, versioned memory,
common origin, and human disposition. Their public explanations must derive
from `framework/GLOSSARY.md`. A closed popover may never hide a qualification
needed to keep a visible claim accurate.

Technical state vocabularies belong on the Apply route or in progressive
detail. They do not belong in the hero or replace plain language on the map.

## Examples and Echo placement

The site must include at least these three teaching patterns:

1. a peripheral or specialist candidate that still requires weighing and
   disconfirmation;
2. velocity or expected absence against an explicit baseline; and
3. recurrence where several reports may share one origin and therefore do not
   automatically supply independent corroboration.

The common-origin example must appear only after the broad thesis and complete
six-family map are available. Every Signal Foundry cross-link must say that it
is an illustration, not validation. Every Echo link must describe it as a
separate, unrun, no-results project. Removing Echo and its explicit example
must leave the Read, Explore, and Apply routes coherent.

## History and visual hierarchy

The recovered v13 map may appear only with this visible label or a semantically
equivalent one:

> Historical v13 origin — not the current v16 topology.

The current relationship map must be visually distinguishable from the
historical map. Code-native diagrams and microvisuals are preferred when they
teach comparison, motion, absence, recurrence, or learning. Bitmap generation
may begin only after `qa/visual/VISUAL_NEEDS.md` records a material need; every
candidate then requires an entry in `assets/IMAGE_USE_LEDGER.md` as used,
unused, or archived with a reason.

## Accessibility, print, and export obligations

The implementation must provide:

- semantic landmarks and heading order;
- a skip link and complete keyboard operation;
- visible focus and non-color-only state communication;
- labels/descriptions for interactive map and glossary controls;
- reduced-motion behavior and no essential hover-only interaction;
- usable reflow at 200% zoom and mobile/tablet/desktop widths;
- a no-script reading path;
- print styles that retain the thesis, family labels, examples, boundaries,
  sources, and URLs where useful;
- a standalone HTML export that does not require a deployed server; and
- a visually inspected PDF companion derived from canonical content.

Automated checks do not substitute for the recorded keyboard, responsive,
print, and rendered-PDF inspections required by A13.

## Claim and action boundaries

Every site surface inherits these constraints:

- the six families are an arrangement and operating proposal, not a novelty
  claim;
- peripheral is a candidate state, not truth;
- provenance is not correctness;
- recurrence is not independent corroboration;
- access is not permission;
- a fixture, validator, protocol, design, or advisory review is not a result;
- Signal Foundry is not validation;
- The Echo Problem and DL-PLAYBOOK-01 are unrun and have no results;
- human judgment and consequential authority are not delegated by this site;
  and
- building, exporting, testing, or packaging the local site does not authorize
  merge, deployment, publication, GitHub Release, study execution, provider
  calls, dataset acquisition, participant activity, or spend.

## Change control

The site task may make local copy edits for navigation or accessibility only
when they preserve the source meaning and status. Any change to the headline,
standfirst proposition, six-family names/order/questions, artifact hierarchy,
Echo placement, historical label, or claim/action boundary requires an entry
in `docs/DECISION_LOG.md` and primary-orchestrator review. A change to locked
owner intent still requires a new explicit owner instruction.
