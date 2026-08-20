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

The register names the **content** checkpoint. A commit that updates this file
cannot name itself, so the branch tip may sit one or two metadata commits ahead
of the register while it refreshes this page and the manifest. That gap is
expected; a hash that does not resolve is not.

## Branches

| Role | Branch | Integrated checkpoint | State |
| --- | --- | --- | --- |
| Primary orchestration and owner-review package | `codex/pattern-map-v16-foundation` | `7202746` + `6711b3b` | **Committed locally, not yet pushed.** Draft PR #1 is open and unmerged, and still shows `cc5547d` |
| The Echo Problem / Track 01 | `codex/echo-problem-track-01` | `90c64ad` | Pushed; integrated into foundation |
| Manuscript and mentor reader | `codex/pattern-map-v16-manuscript` | `74f0392` | Pushed; integrated into foundation |
| Applied framework and agent playbook | `codex/pattern-map-v16-playbook` | `fccfceb` | Pushed; integrated into foundation |
| Site and visual system | `codex/pattern-map-v16-site` | `932366a` | Pushed; integrated into foundation |
| Authored site and interaction polish | `codex/pattern-map-v16-site-polish` | `85dff94` | Pushed; integrated into foundation |
| Protected destination | `main` | `5eea238` at orchestration start | Not merged or modified by this work |

Every hash in the branch table was verified to resolve with `git cat-file -t`
on 2026-08-20. A hash that does not resolve is a defect, not a typo.

### The round-two work is committed but not pushed

A push was attempted and refused: the stored GitHub credential for
`adonisdv23` is invalid (`gh auth status` reports the token in the default
account as invalid). Re-authenticating requires the owner's own credentials, so
it was not attempted.

This row therefore says "not yet pushed," which is the state that exists. The
defect this whole register was created for (D-025) was a package claiming a
push that had not happened; recording an intended push as a completed one here
would repeat it exactly.

To publish the branch to the open draft PR, the owner runs:

```sh
gh auth login -h github.com && git push origin codex/pattern-map-v16-foundation
```

After the push, change this row's state to `Pushed` and nothing else — the
hashes are already correct.

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
