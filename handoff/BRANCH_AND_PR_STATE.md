# Branch and draft pull-request state

Status date: 2026-08-20

## Checkpoint register

This table is the **only** place in the repository that states a current
checkpoint hash. Every other document points here instead of repeating one.

That rule exists because of a defect found in this package and recorded as
D-025. The round-one correction package named two checkpoints —
`5eb860e8d691…` and `bfaa62e7c186…` — as the corrected implementation and
corrected evidence commits, and described them as pushed. Neither object has
ever existed in this repository or on the remote; the work they described was
real but uncommitted, and fifteen files inherited the invented hashes. A
publication about not mistaking a plan for an event cannot ship a handoff that
mistakes an intended commit for a made one.

| Checkpoint | Commit | What it carries |
| --- | --- | --- |
| Reviewed predecessor | `cc5547d` | The exact state the independent ChatGPT Pro round-one review inspected |
| Round-one correction and round-two verification | `7202746a9a211233fc3b614b87d497046eeacda4` | Planning-only Apply semantics, the line-free responsive Map, Guided route, term help, Stage 0, plus the rendered-measurement evidence and the corrections it produced |

The round-one/round-two hash above was verified to resolve with `git cat-file -t`
after the commit was made, not before. Until a checkpoint row shows a real
commit, no document may claim one.
`handoff/verify_owner_review_package.py` reads `CONTENT_CHECKPOINT` from this
same value and fails when the manifest disagrees with the artifact bytes.

## Branches

| Role | Branch | Integrated checkpoint | State |
| --- | --- | --- | --- |
| Primary orchestration and owner-review package | `codex/pattern-map-v16-foundation` | `7202746` | Draft PR #1 open and unmerged |
| The Echo Problem / Track 01 | `codex/echo-problem-track-01` | `90c64ad` | Pushed; integrated into foundation |
| Manuscript and mentor reader | `codex/pattern-map-v16-manuscript` | `74f0392` | Pushed; integrated into foundation |
| Applied framework and agent playbook | `codex/pattern-map-v16-playbook` | `fccfceb` | Pushed; integrated into foundation |
| Site and visual system | `codex/pattern-map-v16-site` | `932366a` | Pushed; integrated into foundation |
| Authored site and interaction polish | `codex/pattern-map-v16-site-polish` | `85dff94` | Pushed; integrated into foundation |
| Protected destination | `main` | `5eea238` at orchestration start | Not merged or modified by this work |

Every hash in the branch table was verified to resolve with `git cat-file -t`
on 2026-08-20. A hash that does not resolve is a defect, not a typo.

## Draft pull request

[#1 — Pattern Map v16 — canonical owner-review candidate](https://github.com/adonisdv23/Pattern-Map/pull/1)

- Base: `main` at `5eea2381c86400bacc1bc2a6df0e3af78bd6330a` when opened.
- Head branch: `codex/pattern-map-v16-foundation`.
- State: open and draft; not merged.

The PR tracks the head branch. The routed-site screenshots from `a319794`
remain historical QA; they show the removed connector geometry and the old
event-writing receipt, so they are not current Map or Apply evidence. Current
rendered evidence is `qa/interaction/evidence/`.

The draft PR is an owner-review surface only. It does not authorize merge,
deployment, public-site replacement, publication, GitHub Release creation,
research execution, provider selection/call, spend, data/participant
acquisition, preregistration, or outreach.
