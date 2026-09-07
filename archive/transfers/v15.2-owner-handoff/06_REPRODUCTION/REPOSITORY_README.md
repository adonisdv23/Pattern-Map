# Pattern Recognition / The Discrimination Layer - v15.2

This repository contains the canonical **local owner-review** candidate for
v15.2: a plain-language thought piece, a four-route interactive reader, four
self-contained current-route exports, four self-contained historical
manuscript pages, a structured framework, a visually inspected PDF companion,
and a reproducible but **unrun** research program.

The central idea is:

> An AI answer inherits earlier choices about what information was found,
> treated as separate evidence, allowed to influence the answer, or left out.
> Those choices should be visible and correctable. Repetition should not be
> mistaken for independent support.

The concrete example is deliberately simple: nine articles may still trace to
one launch announcement. The correction is not to discard eight reports. It is
to preserve all nine observations while refusing to describe them as nine
independent supports.

V15.2 is a convergence and hardening release, not a conceptual reset. It opens
with the counting error, reduces taxonomy in the public argument, makes the AI
consequence explicit, adds CSS-native explanatory visuals, expands technical
explanations, corrects the public protocol surface, and preserves all
unfavorable-result and authorization boundaries. It contains **no empirical
result**.

## Start here

| Need | Open | Expected time |
| --- | --- | ---: |
| Understand the idea | [`output/v15_2/standalone/index.html`](output/v15_2/standalone/index.html) and choose the 60-90 second, about-four-minute, or about-nine-minute stop | 1-9 min |
| Review the recommendation | [`handoff/OWNER_REVIEW_PACKET_V15_2.md`](handoff/OWNER_REVIEW_PACKET_V15_2.md) | 12-15 min |
| Skim visually | `output/pdf/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf` | 15-25 min |
| Compare manuscript versions | [`output/v15_2/history-html/index.html`](output/v15_2/history-html/index.html) | 20-40 min |
| Inspect the full argument | [`source/THOUGHT_PIECE_V15_2.md`](source/THOUGHT_PIECE_V15_2.md) | About 9 min |
| Inspect the proposed study | [`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`](research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md) | +10–15 min |
| Hand the project to another GPT | [`handoff/PACKAGE_MAP_V15_2.md`](handoff/PACKAGE_MAP_V15_2.md) and the owner ZIP | - |

`source/THOUGHT_PIECE_V15.md` remains the sealed v15.1 compatibility source.
The current manuscript is the explicitly versioned
`source/THOUGHT_PIECE_V15_2.md`.

## Canonical v15.2 surfaces

| Surface | Canonical artifact | Role |
| --- | --- | --- |
| Owner decision path | [`handoff/OWNER_REVIEW_PACKET_V15_2.md`](handoff/OWNER_REVIEW_PACKET_V15_2.md) | Answer-first recommendation, timing, limits, and next choices |
| Interactive reader | [`site/`](site/) | Canonical editable Essay / Explore / Lab / Sources experience |
| Standalone review reader | [`output/v15_2/standalone/`](output/v15_2/standalone/) | Four self-contained HTML pages with no runtime dependency |
| Historical manuscript reader | [`output/v15_2/history-html/`](output/v15_2/history-html/) | Separate self-contained v14, v15, v15.1, and v15.2 manuscript pages |
| Conceptual manuscript | [`source/THOUGHT_PIECE_V15_2.md`](source/THOUGHT_PIECE_V15_2.md) | Canonical long-form argument |
| Reader contract | [`source/READER_OUTCOME_AND_READING_PATH_V15_2.md`](source/READER_OUTCOME_AND_READING_PATH_V15_2.md) | Current takeaway, 60-90-second / four-minute / nine-minute stops, and explanation requirements |
| Framework map | [`source/FRAMEWORK_COMPONENT_MAP.json`](source/FRAMEWORK_COMPONENT_MAP.json) | Machine-readable C01–C11 / F1–F6 map |
| Research prospectus | [`research/PAPER_PROSPECTUS_V1.md`](research/PAPER_PROSPECTUS_V1.md) | Narrow scientific-paper opportunity |
| Frozen protocol | [`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`](research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md) | F0/F1/F2 design and pre-run gates |
| Offline scaffold | [`research/origin_accounting/`](research/origin_accounting/) and [`tools/origin_accounting/`](tools/origin_accounting/) | Fictional generation, validation, parsing, diagnostics, and planning simulations |
| Prior-art boundary | [`research/PRIOR_ART_DELTA_V1.md`](research/PRIOR_ART_DELTA_V1.md) and [`reports/V15_1_PRIOR_ART_DISPOSITION.md`](reports/V15_1_PRIOR_ART_DISPOSITION.md) | What is established, adjacent, and still testable |
| Integration ledger | [`reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md`](reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md) | Accepted, modified, deferred, and rejected lane work |
| Overnight program | [`reports/overnight/v15_2/`](reports/overnight/v15_2/) and [`research/overnight/v15_2/`](research/overnight/v15_2/) | Research, editorial, design, owner-reader, methods, and accessibility lanes |
| Final validation | [`reports/overnight/v15_2/FINAL_INTEGRATION_AND_QA_REPORT.md`](reports/overnight/v15_2/FINAL_INTEGRATION_AND_QA_REPORT.md) | Final release receipt and residual manual checks |
| Repository checkpoint | [`reports/GITHUB_CHECKPOINT_RECOMMENDATION_V15_1.md`](reports/GITHUB_CHECKPOINT_RECOMMENDATION_V15_1.md) | Read-only migration recommendation |

## Current status and claim boundary

- Status: `LOCAL OWNER REVIEW - CONCEPTUAL SYNTHESIS - UNRUN RESEARCH PROGRAM - NOT PUBLISHED`.
- The thought piece is a credible authored framework and practitioner-design
  candidate.
- The empirical paper is a promising **question**, not a completed paper: no
  model is selected, no primary study has run, and no effect has been observed.
- The framework does not claim to invent provenance, copying detection,
  deduplication, truth discovery, retrieval diversity, claim graphs, or
  evidence synthesis.
- The residual test is narrow: whether supplied origin-relation labels change
  origin-aware evidence aggregation beyond an explicit counting rule.
- A null, negative, harmful, unstable, or shortcut-driven result must remain in
  the record rather than being hidden because it weakens the project.
- Signal Foundry is a bounded application case, not independent proof.

## Interactive explanations

The reader explains technical terms in ordinary language before exposing their
short labels. High-friction terms - including the three experimental versions,
the optional transfer check, planned sample and safety-subset sizes, endpoint
and safety-check names, provenance audit, system runtime, human disposition,
relation codes, and the negative-result commitment - open into explanations
with examples and boundaries.

The popups deepen comprehension; they are not required to rescue opaque prose.
Definitions, examples, and "does not mean" boundaries are also available in the
expanded glossary on `/sources`. Static accessibility checks pass. Fresh
keyboard, assistive-technology, viewport, collision, and print-preview checks
remain an explicit manual owner-acceptance step for this build.

## Local reader

The reader is local-only and marked `noindex, nofollow`.

```sh
cd site
npm ci
npm run dev -- --hostname 127.0.0.1 --port 8773
```

Open `http://127.0.0.1:8773/`. Routes are:

- `/` - 60-90-second, about-four-minute, and about-nine-minute cumulative stops;
- `/explore` — framework, component records, loops, cases, and objections;
- `/lab` — the proposed study, in plain language, with no results surface; and
- `/sources` — sources and compact/expanded glossaries.

Validate with:

```sh
cd site
npm run lint
npm test
```

No deployment command is part of this release.

## Offline research scaffold

The scaffold is standard-library Python and has no model/provider integration.

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m compileall -q tools/origin_accounting tests
python3 -m tools.origin_accounting.cli parser-fixtures
python3 -m tools.origin_accounting.cli smoke --out /private/tmp/oa-v15-1-smoke
python3 -m tools.origin_accounting.cli generate --out /private/tmp/oa-v15-1-full
python3 -m tools.origin_accounting.cli power \
  --out /private/tmp/oa-v15-1-power \
  --repetitions 1 \
  --bootstrap-repetitions 5 \
  --vor-bootstrap-repetitions 5 \
  --vor-n 10
```

`generate` creates fictional deterministic bundles and receipts. The reduced
power command checks wiring only. Neither command calls a model or produces an
empirical finding.

## History and future repository

- V15.2 supersedes v15.1 for owner review; v15 and v15.1 remain sealed checkpoints.
- The recovered v13 diagram remains byte-for-byte unchanged at
  `archive/v13/pattern-recognition-diagram-v12.png`, SHA-256
  `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.
- The current public `adonisdv23/Pattern-Map` repository is best preserved as a
  v14 archive before a curated v15.2 root is introduced.
- No GitHub push, tag, release, default-branch change, deployment, or
  publication has been performed.

## Authorization boundary

The repository is ready for owner review and a later curated GitHub checkpoint,
not external execution. A new explicit instruction is required before selecting
or paying for a model, running a pilot or primary study, preregistering,
recruiting people, acquiring external datasets, publishing, deploying, pushing,
opening a PR, merging, or changing repository settings. The Sites hosting
manifest is preserved for reproducibility; no deployment was performed.
