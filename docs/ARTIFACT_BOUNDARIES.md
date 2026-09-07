# Artifact boundaries

Status: **BINDING FIREBREAKS FOR V16 DEVELOPMENT**

This contract prevents the human essay, builder framework, agent companion,
Echo Problem research track, site, and historical archives from silently
collapsing into one artifact again.

## Canonical artifact map

| Artifact | Primary purpose and reader | Canonical paths | May contain | Must not become |
| --- | --- | --- | --- | --- |
| Human thought piece | Continue the coffee conversation for the mentor and a thoughtful general reader | `manuscript/PATTERN_RECOGNITION_V16.md`, short version, cover note, abstract | Broad human problem, six families, three examples, bounded implementation bridge, limitations after comprehension | Protocol, component catalog, literature defense, provenance-only essay, or claim of validation |
| Builder framework | Translate the idea into implementable choices | `framework/**`, `cases/**` | Stable six-family spec, relationships, mechanisms, light/moderate/advanced paths, templates, failure modes, stopping rules, Signal Foundry and neutral cases | One mandatory architecture, product claim, or substitute for the essay |
| Agent companion | Give agents observable operating procedures | `framework/agent-playbook/**` | Preflight, acquisition, comparison, disconfirmation, uncertainty, escalation, cost, stop, receipts, outcome learning, before/after examples | Inspirational prompt, autonomous authority grant, or vague command to be unconventional |
| The Echo Problem | Preserve and advance origin accounting as independent ECHO-01 work | `research/the-echo-problem/**` | EP v0.1 identity, v15.2-derived manuscript/site/protocol/harness/fixtures/prior art, no-results declaration, low/no-cost future plan | Opening or definition of v16, completed study, or retroactive rename of v15.2 |
| Broader research agenda | Define future falsifiable questions about the full playbook | `research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md`, `research/future-studies/**` | Matched-budget comparisons, usefulness, supported novelty, evidence diversity, missing-perspective detection, correction effort, negative results | Empirical result, preregistration, selected provider/model, or authorization to run |
| Interactive site | Teach and connect the approved content through progressive disclosure | `site/**`, `assets/diagrams/**`, `qa/site/**`, `qa/visual/**` | Three doors, glossary/popovers, code-native microvisuals, historical map, examples, sources, research and history links, local exports | Independent source of claims, deployed public replacement, image-led thesis, or protocol-first opening |
| Historical archives | Preserve what existed and how it was transferred | `archive/**` | Exact files, source commits, hashes, manifests, accession notes | Editable current source, rewritten terminology, silent correction, or evidence of effectiveness |
| Owner-review handoff | Package and explain the review candidate | `handoff/**` | Package map, checksums, review guide, known residuals, branch/PR state | Publication, GitHub Release, merge instruction, or claim that owner review occurred when it did not |

## Cross-artifact flow

- `OWNER_INTENT_V16.md` and the thesis/audience contract govern every active
  artifact.
- The human essay defines the public content interface in plain language.
- The framework expands that interface into stable concepts and choices.
- The agent companion turns approved concepts into observable procedures.
- The site presents, links, and progressively reveals canonical content; it
  does not invent a separate thesis.
- The research agenda tests bounded questions and constrains claims; it cannot
  silently redefine the essay.
- The Echo Problem can inform one v16 example and link outward as an independent
  project. Its full protocol and notation stay in its own track.
- Archives provide provenance and source evidence, never automatic current
  authority.

## Five collapse tests

A change must be revised if any answer below is `no`:

1. **Essay independence:** Can the human essay be understood without opening
   the framework, agent guide, Lab, source ledger, or Echo project?
2. **Framework independence:** Can a builder implement a lightweight version
   without adopting the complete research schema or origin-accounting harness?
3. **Agent observability:** Can a reviewer tell whether the agent followed the
   procedure from artifacts and receipts rather than trusting self-description?
4. **Echo separation:** If the common-origin example disappears, do the broad
   thesis and all six families remain coherent?
5. **Archive immutability:** Can current terminology or status be changed
   without editing historical bytes?

## Shared concepts without shared authority

Artifacts may share terminology, examples, and links. They do not inherit one
another's evidentiary status. A polished site does not validate the framework;
a protocol does not make the thought piece a paper; a case does not prove a
product capability; a historical archive does not overrule current owner
intent; and an advisory review does not become a source merely because it is
included in QA.

## Change-control rule

Any proposed cross-boundary move must name the source artifact, destination,
reason, reader benefit, status-language impact, and governing requirement in
`docs/DECISION_LOG.md`. The primary orchestrator decides integration; intent
changes still require a new explicit owner instruction.
