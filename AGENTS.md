# Pattern Map repository instructions

These rules apply to every task and agent working in this repository. More
specific instructions may narrow a task's file ownership, but may not weaken
these boundaries.

## Read before editing

Read these files in order when present:

1. `docs/OWNER_INTENT_V16.md`
2. `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`
3. `docs/ARTIFACT_BOUNDARIES.md`
4. `docs/SOURCE_AUTHORITY_AND_LINEAGE.md`
5. `docs/V16_ACCEPTANCE_CRITERIA.md`
6. `docs/DECISION_LOG.md`

Then inspect `git status`, the current branch, and any task-specific ownership
instructions. Never assume that a detailed historical or model-generated file
is current authority.

## Authority order

1. The owner's approved v16 handoff and later explicit owner instructions.
2. `docs/OWNER_INTENT_V16.md`.
3. Recovered v13 material for historical idea, ambition, six families, and
   reader problem.
4. V14/v15 material for rigor, limits, terminology, implementation patterns,
   accessibility, prior art, and design lessons.
5. V15.2 for The Echo Problem and selectively reusable interface or research
   patterns only.
6. Agent and model reviews as advisory material, never evidence or authority by
   virtue of detail.

If sources conflict, preserve the conflict and follow this order. Do not
silently rewrite historical files to match later decisions.

## Permanent project split

- V16 is the broad Pattern Recognition / Discrimination Layer work and begins
  from v13 intent and all six families.
- The Echo Problem is the separate origin-accounting project derived from the
  exact v15.2 checkpoint. Origin accounting is a worked example and research
  track inside the broader history; it is not the definition of v16.

Do not collapse the human essay, builder framework, agent companion, Echo
research track, and historical archive into one artifact.

## Archive and provenance rules

- Treat everything under `archive/` as immutable after accession.
- Moves into `archive/` must preserve bytes and history. Use `git mv` for
  tracked material.
- Never edit an archived file to update terminology or status. Add adjacent
  accession metadata or a new curated successor instead.
- Record source path, source commit, byte size, SHA-256 where available,
  authority role, and verification status.
- Preserve the v13 diagram byte-for-byte and label it historical, never current
  topology.
- Preserve the exact v15.2 no-results state and all unfavorable-result classes.

## Editing and ownership

- Work on the assigned feature branch in an isolated worktree.
- Edit only the paths explicitly assigned to the task. The primary orchestrator
  is the sole integrator of cross-task changes.
- Preserve user and sibling-task changes. Do not stage unrelated files.
- Prefer the smallest coherent commit and name the governing requirement in
  review or handoff notes.
- Record advisory findings as `Accepted`, `Accepted with revision`, `Deferred`,
  or `Rejected`, with reason, affected files, and governing requirement.

## Research and claims

- Never present a protocol, fixture, planning simulation, model review, or
  design illustration as an empirical result.
- Do not claim that the six families or their mechanisms are newly invented.
- Do not equate peripheral with true, recurrence with independent support,
  provenance with correctness, access with permission, or a human disposition
  with a fact.
- Keep unknown relations unknown. Keep observation separate from interpretation.
- Research may constrain claims; it may not silently redefine owner intent.
- Signal Foundry and domain examples are bounded illustrations, not validation.

## Site and visuals

- The first screen begins with the human problem, not a protocol, disclaimer, or
  literature defense.
- Use progressive disclosure for technical detail.
- Prefer semantic HTML and code-native microvisuals when they teach the idea.
- Generated imagery requires a documented need, multiple candidates where
  justified, and a complete used/unused/archived decision in
  `assets/IMAGE_USE_LEDGER.md`.
- The recovered v13 map is historical origin, never the current system map.
- Local build and export work is allowed. Deployment and publication are not.

## Security, generated files, and dependencies

Never commit secrets, credentials, cookies, auth databases, environment values,
private keys, dependency directories, caches, or generated build directories.
Use locked installs when dependencies are required. Follow
`docs/BINARY_ARTIFACT_POLICY.md` for binaries and owner archives.

## Authorized and prohibited external actions

Authorized: feature branches, isolated Git worktrees, scoped commits, pushes of
coherent feature branches, and draft pull requests for owner review.

Not authorized: merge to `main`; deploy or replace a public site; publish;
create a GitHub Release; run a model, empirical, pilot, or participant study;
select or call a paid provider; spend money; acquire external datasets;
preregister; contact people; or imply any unrun research produced results.
