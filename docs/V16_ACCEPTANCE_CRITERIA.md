# V16 acceptance criteria

Status: **BINDING OWNER-REVIEW GATES**

V16 is complete only when every required gate has evidence and no prohibited
action has occurred. `Pass` means the named artifact and check exist; a proxy
review, plan, or assertion does not substitute for the evidence named here.

## Non-negotiable gates

| ID | Gate | Required evidence |
| --- | --- | --- |
| A01 | A 90-second reader can describe the broad Discrimination Layer idea without treating origin accounting as its definition | Short version and first essay/site stop pass a cold-reader rubric: upstream choices, inspectability/correction, human judgment, and breadth beyond origin counting are all present |
| A02 | The first screen begins with the human problem, not a protocol, disclaimer, or literature defense | Rendered first-screen capture and semantic-heading inspection; necessary boundary language follows rather than displaces the problem |
| A03 | All six original families are visible | Essay, map, and framework explicitly include peripheral signal; source weighing; velocity/motion; absence + memory; structured patterns; learning loop |
| A04 | The piece feels like a continuation of a thoughtful conversation, not an academic committee document | Mentor cover note, editorial audit, and cold-reader notes find a direct human voice, intelligible stakes, and an invitation to challenge |
| A05 | The full human essay is approximately 10–15 minutes | Recorded word count and editorial reading estimate, followed by owner/cold-reader confirmation when authorized; timing is not described as measured before then |
| A06 | Technical detail uses progressive disclosure | Essential argument reads coherently without popovers; technical terms have plain-language introductions; print/no-script route retains the core meaning |
| A07 | A builder can identify concrete implementation paths | Framework names lightweight, moderate, and advanced choices with inputs, outputs, trade-offs, failure modes, cost, stop, and when-not-to-use guidance |
| A08 | The agent companion specifies observable behavior | Quickstart and full guide define artifacts/actions for decision framing, acquisition, comparison, disconfirmation, uncertainty, escalation, cost, stopping, influence recording, and learning; examples make compliance inspectable |
| A09 | Signal Foundry is a bounded illustration, not validation | Case header/footer and every cross-link state the boundary; no effectiveness or permission claim relies on the case |
| A10 | The Echo Problem is separate, preserved, and explicitly has no results | EP v0.1 identity and version history; verified v15.2 accession; manuscript/site/protocol/harness/fixtures/prior art; status and no-results declarations; link from v16 as a separate project |
| A11 | Scientific and novelty claims do not exceed evidence | Claims/source ledger, prior-art audit, manuscript search, and research-boundary review find no invented novelty or unrun-result language |
| A12 | Every generated image is recorded as used, unused, or archived with a reason | `assets/IMAGE_USE_LEDGER.md` has one disposition for every generated candidate and derivative, with origin, intended need, and selection/rejection reason |
| A13 | Responsive, keyboard, print, and basic accessibility tests pass | Automated checks plus recorded manual keyboard traversal, supported screen-reader review, 200% zoom/reflow, mobile/tablet/desktop views, forced-colors where practical, and print preview; residuals are explicit |
| A14 | Historical archives are immutable and clearly labeled | Hash/manifests pass; archive diff audit finds no rewritten bytes; history/current-topology labels are visible wherever reused |
| A15 | No prohibited external or research action is implied or performed | Final action audit confirms no deployment, publication, merge, Release, empirical/model/participant run, paid provider, spending, dataset acquisition, preregistration, or outreach |
| A16 | Research may constrain claims but may not silently redefine owner intent | Fidelity audit traces every material research-driven edit to a claim boundary, not a thesis substitution; owner-intent hash/content remains unchanged unless the owner explicitly revises it |
| A17 | No agent changes locked owner intent without explicit owner instruction | Git history and decision log show no unauthorized modification; proposed changes, if any, remain marked owner-decision-required |

## Required human-facing deliverables

- `manuscript/PATTERN_RECOGNITION_V16.md` — canonical 10–15-minute thought
  piece.
- `manuscript/NINETY_SECOND_VERSION.md` — cumulative 60–90-second broad idea.
- `manuscript/MENTOR_COVER_NOTE.md` — concise invitation to challenge and
  expand the thinking.
- `manuscript/PUBLIC_ABSTRACT.md` — standalone public abstract without research
  overclaim.
- A concise origin note and complete six-family map.
- At least three worked examples covering peripheral/specialist signal,
  velocity or expected absence, and common-origin recurrence.
- Counterarguments and limitations after comprehension, with optional deeper
  sources and research routes.

## Required builder-facing deliverables

- Stable Markdown and JSON six-family specifications.
- Relationship map and practical operator playbook.
- Lightweight, moderate, and advanced implementation choices.
- Templates, failure modes, stopping rules, cost boundaries, and when-not-to-use
  guidance.
- Serious bounded Signal Foundry translation and at least two domain-neutral
  examples.

## Required agent-facing deliverables

- `framework/agent-playbook/QUICKSTART.md`
- `framework/agent-playbook/FULL_OPERATING_GUIDE.md`
- `framework/agent-playbook/COPYABLE_AGENT_BRIEF.md`
- `framework/agent-playbook/PREFLIGHT_CHECKLIST.md`
- `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md`
- Ordinary-versus-Discrimination-Layer behavior examples.
- Explicit acquisition, comparison, disconfirmation, uncertainty, escalation,
  cost, stop, and learning procedures.

## Required site and review deliverables

- Three principal doors: Read the idea / Explore the map / Apply it.
- Optional Examples / Boundaries / Sources / Research / History routes.
- Plain-language term explanations and technical popovers.
- Code-native microvisuals only where they materially teach.
- Historical v13 map labeled as origin, never current topology.
- Responsive, keyboard-accessible, screen-reader-conscious, printable behavior.
- Standalone HTML exports and a visually verified PDF review companion.
- Clear link to the separate Echo Problem project.

## Required research containment

The Echo Problem remains Paper/Track 01 candidate and unrun. The broader
research agenda must specify—but not execute—a future matched-budget flagship
study asking whether the operational playbook improves usefulness, supported
novelty, evidence diversity, missing-perspective detection, and human correction
effort relative to ordinary prompting. It must preserve null, harmful,
shortcut, fragility, non-transfer, and stop outcomes.

## Owner-review release rule

The final package requires canonical artifacts, decision and source ledgers,
image ledger, version history, QA evidence, package map, and checksums on pushed
feature branches with draft PRs. Completion does not authorize merge,
deployment, publication, Release creation, or research execution.
