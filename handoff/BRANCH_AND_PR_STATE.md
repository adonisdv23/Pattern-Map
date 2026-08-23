# Branch and draft pull-request state

Status date: 2026-08-23

| Role | Branch | Integrated/pushed checkpoint | State |
| --- | --- | --- | --- |
| Primary orchestration and owner-review package | `codex/pattern-map-v16-foundation` | `ad964dd` canonical converged source; evidence/checksum commit follows | Authorized push target; draft PR #1 remains open and unmerged; final metadata readback occurs after the evidence push |
| The Echo Problem / Track 01 | `codex/echo-problem-track-01` | `90c64ad` | Pushed; integrated into foundation |
| EP v1.1 design checkpoint | `codex/pattern-map-v16-echo-v1-1` | `c141eac` | Integrated into foundation as `9fa2355`; local source branch not required by the downstream handoff |
| Manuscript and mentor reader | `codex/pattern-map-v16-manuscript` | `74f0392` | Pushed; integrated into foundation |
| Applied framework and agent playbook | `codex/pattern-map-v16-playbook` | `fccfceb` | Pushed; integrated into foundation |
| Site and visual system | `codex/pattern-map-v16-site` | `932366a` | Pushed; integrated into foundation |
| Authored site and interaction polish | `codex/pattern-map-v16-site-polish` | `85dff94` | Pushed; integrated into foundation |
| Protected destination | `main` | `5eea238` at orchestration start | Not merged or modified by this work |

Draft pull request: [#1 — Pattern Map v16 — canonical owner-review candidate](https://github.com/adonisdv23/Pattern-Map/pull/1)

- Base: `main` at `5eea2381c86400bacc1bc2a6df0e3af78bd6330a` when opened.
- Head branch: `codex/pattern-map-v16-foundation`.
- Canonical converged source checkpoint:
  `ad964dd91eff521b0442f613c55bc4e9e97c2f2a`.
- Round 2 correction implementation checkpoint:
  `c88926034cd75773dcc42d3842983c879dda5b58` (review history).
- Round 2 reviewed predecessor:
  `4d2505e7f3d325fe7b8ef5e2e5c3a634a11aa9fe`.
- State: open and draft; not merged.

The PR tracks the head branch. The canonical source checkpoint above includes
the bounded ChatGPT Pro corrections, site hygiene, Signal handoff, and EP v1.1;
the following handoff and verification commit records current evidence and
refreshes the bounded package manifest. After that final push, the PR body is
read back from GitHub so no self-referential file is mistaken for proof of its
later metadata state. The routed-site screenshots from
`a319794` remain historical QA, not current Map/Apply evidence.

The draft PR is an owner-review surface only. It does not authorize merge,
deployment, public-site replacement, publication, GitHub Release creation,
research execution, provider selection/call, spend, data/participant
acquisition, preregistration, or outreach.
