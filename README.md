# Pattern Map

Pattern Map is the canonical project home for two related but permanently
separate bodies of work:

1. **Pattern Recognition / The Discrimination Layer v16** — a human-first
   thought piece, six-family framework, builder system, and operational
   AI-agent playbook about the decisions that shape an answer before
   generation.
2. **The Echo Problem / Research Track 01 / ECHO-01** — a standalone thought
   piece, origin-accounting framework, and unrun controlled research protocol
   for preventing repeated or derived reports from being misrepresented as
   independent corroboration.

The project is in owner-review development. A materially authored local v16
site now provides shared-source owner-review and public-preview modes,
persistent review orientation, an interactive six-family
relationship map, inline term explainers, an optional continuous Guided read,
and a provider-free Apply studio that begins with the Stage 0 evidence-selection
gate and separates planning recommendations from unrun and unobserved states. A
deterministic teaching reveal shows how upstream choices change what becomes
visible without calling a model or claiming a result. Direct-open semantic
review/public HTML exports and a secondary
PDF companion also exist, but no public site has been deployed or substituted
for the historical reference. The framework is not empirically validated and
no study run is authorized.

## Current state

The repository now has a reproducible canonical root, immutable historical
transfers, a locked v16 intent, a converged manuscript, a stable six-family
framework, an operational agent companion, bounded cases, a separate EP v0.1
Echo project with an EP v1.1 design-only successor checkpoint, an explicitly
unrun broader research agenda, and a ten-route local owner-review site
including an optional Guided read. Structural, responsive, no-script, export,
108-case planning-state, interaction, visual, Echo implementation, and final
independent proxy/operator checks pass within their stated artifact
boundaries. Owner/mentor judgment plus manual
physical-keyboard, supported screen-reader, real-zoom, forced-colors, browser
print-preview, and hardware-touch confirmation remain open.
The current public/transfer owner-review surface is draft pull request
[#2](https://github.com/adonisdv23/Pattern-Map/pull/2), layered on the preserved
foundation review in draft pull request
[#1](https://github.com/adonisdv23/Pattern-Map/pull/1). Neither is authorization
to merge or publish.

Start with:

1. [`docs/OWNER_INTENT_V16.md`](docs/OWNER_INTENT_V16.md)
2. [`docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`](docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md)
3. [`docs/ARTIFACT_BOUNDARIES.md`](docs/ARTIFACT_BOUNDARIES.md)
4. [`docs/V16_ACCEPTANCE_CRITERIA.md`](docs/V16_ACCEPTANCE_CRITERIA.md)
5. [`docs/SOURCE_AUTHORITY_AND_LINEAGE.md`](docs/SOURCE_AUTHORITY_AND_LINEAGE.md)
6. [`docs/V13_TO_V16_FIDELITY_MATRIX.md`](docs/V13_TO_V16_FIDELITY_MATRIX.md)
7. [`docs/V16_ROADMAP.md`](docs/V16_ROADMAP.md)
8. [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md)
9. [`docs/REVIEW_AND_DISPOSITION_PROTOCOL.md`](docs/REVIEW_AND_DISPOSITION_PROTOCOL.md)
10. [`docs/ADVISORY_REVIEW_DISPOSITIONS.md`](docs/ADVISORY_REVIEW_DISPOSITIONS.md)
11. [`docs/CONTENT_INTERFACE_FREEZE_V16.md`](docs/CONTENT_INTERFACE_FREEZE_V16.md)
12. [`docs/CLAIMS_AND_SOURCE_LEDGER_V16.md`](docs/CLAIMS_AND_SOURCE_LEDGER_V16.md)
13. [`docs/PUBLIC_AND_TRANSFER_HARDENING_PLAN_V16.md`](docs/PUBLIC_AND_TRANSFER_HARDENING_PLAN_V16.md)

For the local review surface:

```sh
cd site
npm run build
npm run check
npm run dev
```

Then open <http://127.0.0.1:4173/>. The direct-open HTML export is
[`site/exports/standalone/pattern-map-v16.html`](site/exports/standalone/pattern-map-v16.html),
the public-preview export is
[`site/exports/standalone/pattern-map-v16-public.html`](site/exports/standalone/pattern-map-v16-public.html),
and the review companion is
[`site/exports/pattern-map-v16-owner-review.pdf`](site/exports/pattern-map-v16-owner-review.pdf).
These are local artifacts, not a deployment or publication. To inspect the
public adapter as routed pages, stop the review server and run
`npm run dev:public`; it remains `noindex,nofollow` with publication identity
unset.

For the downstream Signal Foundry handoff, give the next operator these two
files together:

1. [`handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md`](handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md)
2. [`handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md`](handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md)

They identify the exact Pattern Map and Signal Foundry checkpoints, explain
the recoverable local audit branch, and make clear that no V14 deep link,
Pattern Map classifier, schema mutation, or app integration should be
invented.

Run the complete provider-free repository verification with:

```sh
qa/run_owner_review_checks.sh
```

Pass `--source-zip PATH` only when the separately preserved exact v15.2 ZIP is
available and its container hash should also be checked.

## Repository map

- `docs/` — governing contracts, lineage, roadmap, decisions, and editorial
  review records.
- `manuscript/` — the v16 essay, short version, mentor note, and public abstract.
- `framework/` — the six-family specification, mechanisms, templates, and agent
  playbook.
- `cases/` — bounded applications, including Signal Foundry and domain-neutral
  examples.
- `site/` — local, accessible, printable interactive reader and exports.
- `research/` — the broader research agenda and the separate Echo Problem
  project.
- `assets/` — historical assets, code-native diagram sources, and generated
  candidates with a complete use ledger.
- `archive/` — immutable historical transfers and version checkpoints.
- `qa/` — editorial, applied, research, site, and visual acceptance evidence.
- `handoff/` — owner-review packets, package maps, and release checksums.

## Non-result boundary

The six-family framework is an operating philosophy and design proposal, not a
settled scientific result. Signal Foundry and all other cases are illustrations,
not validation. The Echo Problem study is specified but unrun. Null, harmful,
shortcut-driven, fragile, non-transfer, and stopped outcomes must remain
reportable if a future study is ever separately authorized.

## External-action boundary

Feature branches, isolated worktrees, commits, pushes, and draft pull requests
are authorized for this roadmap. The owner later exactly authorized a
ChatGPT Pro advisory review loop on the existing account; that exception does not
authorize a study, a research-provider selection, or incremental spend.
Merging to `main`, deployment, publication, GitHub Releases, empirical or
participant activity, other provider calls, spending, external-dataset
acquisition, preregistration, and outreach are not authorized.
