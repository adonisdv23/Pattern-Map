# Branch and draft pull-request state

Status date: 2026-08-30

| Role | Branch | Integrated/pushed checkpoint | State |
| --- | --- | --- | --- |
| Primary orchestration and owner-review package | `codex/pattern-map-v16-foundation` | `874a0a8` canonical content checkpoint; `c86e537` post-Ultracode contract source; current evidence head resolves from Git or sealed packet metadata | Authorized push target; draft PR #1 was open, draft, and unmerged at the 2026-08-28 readback; resolve its current head at use |
| Public and transfer hardening | `codex/pattern-map-v16-public-transfer-hardening` | Phase 0 baseline `37c7c85`; initial three-lane convergence `cbc89db`; corrections through `c0b006f`; current head resolves from Git or sealed packet metadata | Authorized push target; draft PR #2 was opened against the foundation branch and read back open, draft, clean, and unmerged on 2026-08-30 |
| The Echo Problem / Track 01 | `codex/echo-problem-track-01` | `90c64ad` | Pushed; integrated into foundation |
| EP v1.1 design checkpoint | `codex/pattern-map-v16-echo-v1-1` | `c141eac` | Integrated into foundation as `9fa2355`; local source branch not required by the downstream handoff |
| Manuscript and mentor reader | `codex/pattern-map-v16-manuscript` | `74f0392` | Pushed; integrated into foundation |
| Applied framework and agent playbook | `codex/pattern-map-v16-playbook` | `fccfceb` | Pushed; integrated into foundation |
| Site and visual system | `codex/pattern-map-v16-site` | `932366a` | Pushed; integrated into foundation |
| Authored site and interaction polish | `codex/pattern-map-v16-site-polish` | `85dff94` | Pushed; integrated into foundation |
| Protected destination | `main` | `5eea238` at orchestration start | Not merged or modified by this work |

Current hardening draft pull request: [#2 — Pattern Map v16 — public and transfer hardening](https://github.com/adonisdv23/Pattern-Map/pull/2)

- Base branch: `codex/pattern-map-v16-foundation` at
  `4d2e11ceb26b36fd7428dc7de963c135802a8dea` when opened.
- Head branch: `codex/pattern-map-v16-public-transfer-hardening`.
- Initial pushed source/evidence checkpoint:
  `72a672c5172ff5212e29f01ba2277dd49cc6ea98`.
- State observed on 2026-08-30: open, draft, merge-state clean, and unmerged.
  Resolve the current remote head at use; the generated Signal Foundry packet
  binds the later exact sealed commit in `BUNDLE_METADATA.json.source_commit`.

Foundation draft pull request: [#1 — Pattern Map v16 — canonical owner-review candidate](https://github.com/adonisdv23/Pattern-Map/pull/1)

- Base: `main` at `5eea2381c86400bacc1bc2a6df0e3af78bd6330a` when opened.
- Head branch: `codex/pattern-map-v16-foundation`.
- Canonical converged source checkpoint:
  `874a0a8e09f0bde11532cf873087865addb7d973`.
- Post-Ultracode reusable-contract checkpoint:
  `c86e53764f6e33b62097f0424125b5922441ce58`.
- Immediate predecessor before terminal geometry, vocabulary, portability, and
  package corrections:
  `bc7e7c5f95c85b8f6f969ed87ff7fa81cdb2ae91` (review history).
- Earlier converged source checkpoint before the owner visual/export repair:
  `ad964dd91eff521b0442f613c55bc4e9e97c2f2a` (review history).
- Round 2 correction implementation checkpoint:
  `c88926034cd75773dcc42d3842983c879dda5b58` (review history).
- Round 2 reviewed predecessor:
  `4d2505e7f3d325fe7b8ef5e2e5c3a634a11aa9fe`.
- State observed on 2026-08-28: open and draft; not merged. Resolve the
  current remote head and state at use rather than treating this tracked file
  as self-referential proof of a later push.

Both draft PRs track their named head branches. The canonical foundation
source checkpoint above includes
the bounded ChatGPT Pro corrections, site hygiene, Signal handoff, EP v1.1,
the owner visual/export repair that restores standalone route containment,
the desktop term-panel clearance regression, canonical operator tokens,
path-neutral downstream guidance, and the exact-commit portable builder. The
post-Ultracode checkpoint adds scoped F2 track record, reviewed-learning and
permission guards, a genuine ordinary receipt, exact schema identity,
all-payload package hygiene, and fresh-clone-safe Signal Foundry inputs. Exact
sealed-package identity belongs in generated `BUNDLE_METADATA.json` and
`START_HERE.md`; current remote state belongs to a fresh Git/GitHub readback.
This tracked narrative deliberately does not hard-code its own later commit.
The routed-site screenshots from
`a319794` remain historical QA, not current Map/Apply evidence.

The draft PR is an owner-review surface only. It does not authorize merge,
deployment, public-site replacement, publication, GitHub Release creation,
research execution, provider selection/call, spend, data/participant
acquisition, preregistration, or outreach.
