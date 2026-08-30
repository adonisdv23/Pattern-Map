# Loop 1 cross-lane challenge: public and mentor rehearsal kit

Status: **READ-ONLY ADVISORY — exact public commit reviewed; no publication,
mentor contact, deployment, merge, or external action**

This report is the agent/operator/transfer lane's Loop 1 challenge of the
public/mentor lane. It inspects the actual files in exact commit
`f2311d095d0afc094356e222624cff3aa1e3b939` rather than relying on the public
lane summary. It does not edit that commit's `publication/**`, `site/**`, or
`framework/**` files. The only file added by this task is this advisory report
under `qa/applied/advisory/`.

## Verdict

| Severity | Verdict | Meaning here |
| --- | --- | --- |
| P0 | **0** | No authority, data-loss, security, or boundary failure reproduced. |
| P1 | **0** | No release, public-surface, human-authority, or evidence-boundary failure reproduced. |
| P2 | **0** | No material functional or usability defect remains in the reviewed added surfaces. |
| P3 | **3 non-blocking dispositions** | Discoverability, future channel scoping, and test-maintenance risks are recorded below; none authorizes changing the current candidate or external action. |

The four-file kit is useful as optional owner-facing convenience packaging. It
does not merely restate the essay: it supplies a bounded mentor conversation
sequence, unsent platform-copy rehearsal, and a human release gate while
pointing back to canonical prose/framework/site sources. It is not a
project-use adapter and must not be made one. The existing owner packet and
site remain the substantive review path.

The public-only navigation correction is proportionate and correct: it repairs
a reproduced public header-spacing defect, leaves review density unchanged, and
is covered by a focused contract. The release checklist is fail-closed and does
not grant authority. A later channel-specific publication decision should scope
manual gates to the proposed artifact, but that is a future owner decision, not
a current release defect.

## Review identity and authority

| Item | Value |
| --- | --- |
| Reviewed commit | `f2311d095d0afc094356e222624cff3aa1e3b939` |
| Reviewed commit parent / lane baseline | `d05aca58910b4463e5afb69b10558b662a446278` |
| Reviewed worktree | `/Users/gpt/Documents/Codex/worktrees/pattern-map-v16-loop-public` |
| Reviewed branch | `codex/pattern-map-v16-loop-public` |
| Reporting branch | `codex/pattern-map-v16-loop-agent` |
| Reporting branch HEAD before this report | `9ed522afcacaa45e9bfa5950f03f454a87e3dd92` |
| Governing scope | Loop 1 agent/operator challenge; read-only review of the public/mentor commit |
| Owner-intent checkpoint | `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — pass before this report |

The required governing documents, including the complete decision log and
`docs/OPPORTUNITY_EXPANSION_LOOPS_V16.md`, were read in the repository-required
order before task actions. The locked owner intent, broad coffee-conversation
thesis, exact six families, permanent Echo separation, ordinary Stage 0 escape,
human authority, no-results boundary, and proportionality remain the authority.

## Exact artifacts inspected

### Added public/mentor files

- `f231:publication/README.md` — 77 lines, 558 words. Three moves, source map,
  unresolved fields, evidence boundary, and a direct removal test.
- `f231:publication/MENTOR_REVIEW_SEQUENCE_V16.md` — 84 lines, 844 words.
  Six passes, response sheet, stop conditions, and “cannot establish” limits.
- `f231:publication/X_COPY_VARIANTS_V16.md` — 80 lines, 622 words. Three
  single-post drafts and a four-post thread, all explicitly unsent.
- `f231:publication/RELEASE_DECISION_CHECKLIST_V16.md` — 106 lines, 818 words.
  Owner/content, provenance/link, manual, action/claim, and decision gates.

Together these are 347 lines / 2,842 words. They are larger than a one-line
pointer but remain focused notes, not another essay or framework.

### Existing owner and site surfaces

- `f231:handoff/OWNER_REVIEW_PACKET_V16.md` — 319 lines, 2,454 words. Its
  recommended path already covers the 60–90-second version, cover note, essay,
  build/check commands, review/public site modes, framework, cases, Echo
  boundaries, QA, and open manual gates (`:79-116`, `:270-290`).
- `f231:handoff/PACKAGE_MAP_V16.md` — the canonical map of human, builder,
  agent, local-site, Echo, research, archive, and final-review artifacts. It
  names the six agent entry points (`:51-60`) but does not name the optional
  publication kit.
- `f231:README.md` — root entry points and repository map. It describes the
  local review/public modes and handoff, but has no link to `publication/`.
- `f231:site/README.md` — exact build/check/dev commands, public-mode
  distinction, semantic standalone boundary, and release behavior (`:34-78`).
- `f231:site/publication.config.json` — schema v1, `LOCAL_PREVIEW_UNSET`, null
  author/handle/canonical/social fields, and an explicit later-authorization
  boundary (`:1-9`).
- `f231:site/src/publication-config.mjs` — release status and URL/host
  validation; metadata requires an explicit release request and a valid full
  configuration (`:1-3`, `:79-137`).
- `f231:handoff/signal-foundry/build_portable_bundle.py` — explicit selected
  downstream paths and intentional exclusion of public-review-only artifacts
  (`:54-147`, `:255-265`).

### Focused tests and generated public surface

- `f231:qa/publication/publication-kit-contract.spec.mjs` — required-file,
  fail-closed-token, draft-length, no-URL/handle, null-config, no-bitmap, and
  relative-link checks (`:9-100`).
- `f231:qa/site/public-nav-spacing-contract.spec.mjs` — public-only wide/narrow
  gap declarations, review non-inheritance, generated mode markers, and the
  three principal links (`:10-35`).
- `f231:site/src/site.css`, both standalone exports, and `site/package.json` —
  the public-only spacing rule, regenerated exports, and focused test wired into
  `npm run check`.

## Does the kit help an owner act, or restate the essay?

### Finding CL-PUB-01 — four-file kit actionability

**Disposition: Accepted (optional convenience packaging). Severity: no P0/P1/P2.**

The index is not a second essay. `publication/README.md:16-26` gives three
bounded moves: run a private owner-led mentor sequence, rehearse unsent copy,
and use the release checklist only after an exact later owner instruction. Its
canonical source map (`:38-46`) routes the broad idea to the manuscript and
short version, the mentor context to the existing cover note, six-family
material to the existing specification/site, boundaries to governing claims
records, and release state to the existing configuration. It explicitly says
the kit must not become a second map, framework, source ledger, or canonical
publication page (`:48-51`).

The owner packet already supplies the substantive review sequence, so the kit
does not make the repository's core review possible. It does make a narrower
owner action legible: “what do I do for a private challenge conversation, a
future copy rehearsal, or a later release decision?” That is a real but optional
friction reduction. Removing the index leaves the three notes usable; it loses
their safe order, source map, and unresolved-field warning. Removing all four
files leaves the site and owner packet usable, which confirms that this is
convenience packaging rather than a required authority layer.

The kit is not a project-use bridge. A future project needs the agent/operator
entry path and existing records, not publication copy. Adding project intake,
family selection, permission, route, stop, or receipt instructions here would
duplicate or blur the framework boundary.

### P3 disposition CL-PUB-01a — discoverability from the owner packet

**Disposition: Deferred.**

The exact owner packet, package map, root README, and Signal Foundry selected
path list do not link to `publication/README.md`. A reader who starts at the
canonical owner packet can complete the existing review path without finding
the optional kit, while a reader who is handed the `publication/` directory can
use it directly. This is an integration/discoverability gap, not a correctness
failure.

If the owner wants the kit to be discoverable in the owner-review package, the
primary integrator may add one pointer to its index in a later owner-packet or
root-navigation update, then refresh any package manifest that is intended to
cover it. Do not duplicate the kit's prose in the packet, and do not add it to a
downstream project bundle merely to make the pointer convenient. Until that
owner decision, the correct status is local optional material.

## Do mentor and X rehearsals preserve actionable next steps?

### Finding CL-PUB-02 — mentor sequence

**Disposition: Accepted. Severity: no P0/P1/P2.**

The mentor note preserves an action without creating release ceremony:

- Before the conversation it says to build/check the current branch, use the
  public Read route or short version, keep Map/Boundaries as optional follow-up,
  and start a fresh response sheet (`f231:publication/MENTOR_REVIEW_SEQUENCE_V16.md:16-29`).
- The six passes enter through the human problem, delay the Map until after the
  opening, test breadth/proportion/examples/claim ceiling, and close by asking
  for a challenge or expansion (`:31-43`).
- The response table separates the reader's words from author interpretation and
  gives only `OPEN`, `OWNER DECISION REQUIRED`, or `FOLLOW-UP CHECK` as next
  dispositions (`:45-60`).
- The stop conditions explicitly pause on origin-counting reduction, peripheral
  truth inflation, plan-as-result language, requests to post/contact, or making
  the full framework mandatory (`:62-77`).
- The final section says the sequence cannot establish mentor agreement,
  comprehension, effectiveness, source correctness, or publication readiness
  (`:79-84`).

This is a useful conversation-sized adapter over the cover note and site. It
does not claim that a conversation occurred, and it keeps the next step as a
human challenge, bounded edit, or unresolved owner decision.

### Finding CL-PUB-03 — X copy rehearsal

**Disposition: Accepted with revision already embodied in the reviewed file. Severity: no P0/P1/P2.**

`X_COPY_VARIANTS_V16.md:11-21` sets the right ceiling: human problem first,
all-six-family breadth, peripheral-as-candidate, no validation/effectiveness/
novelty/audience/study claim, human authority, separate unrun Echo, and a
fresh platform/link/metadata/source check before any later authorized use.
Variants A–C and the four-post thread (`:23-66`) are actual copy candidates,
not an essay pasted into a channel. The unresolved table and closing warning
(`:68-80`) preserve the next action as owner selection/revision/rejection;
they do not silently invent a URL, handle, byline, image, CTA, or destination.

The absence of a link or CTA is therefore a deliberate fail-closed property,
not a missing publication step. The note is actionable for rehearsal (choose,
edit, rerun channel checks) while correctly not actionable for posting. A later
owner-authorized channel step may add identity and destination; the current
branch must not.

## Does the release checklist overconstrain or imply authority?

### Finding CL-PUB-04 — fail-closed human release gate

**Disposition: Accepted. Severity: no P0/P1/P2.**

The checklist does not imply authority. Its status and opening say “RELEASE NOT
AUTHORIZED” and “not permission to publish, post, deploy, merge, or contact”
(`f231:publication/RELEASE_DECISION_CHECKLIST_V16.md:1-8`). Section 0 leaves the
exact commit, artifacts, owner instruction, identity, destination, and
authorization unresolved, and says an unknown field stops at `HOLD` (`:10-28`).
The decision enum makes `GO` conditional on every gate and a separately
authorized owner action (`:94-106`). The publication config remains
`LOCAL_PREVIEW_UNSET` with null fields, and the site release implementation
requires both an explicit release request and a valid configuration.

The content, provenance/link, manual, action, and claim gates are appropriate
for a later public-site/publication decision. They preserve human authority,
typed uncertainty at the publication boundary, source/link recheck, the
human-first opening, all six families, three bounded examples, Echo's separate
unrun state, and the no-merge/no-deploy/no-study/no-spend boundary.

The checklist is not a command to run a release: it has no executable release
action, does not edit config, and explicitly leaves the current choice
`HOLD / NOT AUTHORIZED`. The site checks independently reproduce the same
boundary: an ordinary public preview remains `noindex,nofollow`, while an
unset or malformed release configuration fails closed.

### P3 disposition CL-PUB-04a — future channel-specific gate scope

**Disposition: Deferred to the owner at the later release decision.**

The current checklist combines site/manual gates (keyboard, screen reader,
200% zoom, forced colors, native print, touch) with identity and social-copy
fields (`f231:publication/RELEASE_DECISION_CHECKLIST_V16.md:65-78`). If a later
owner instruction authorizes only an X post and no site artifact, requiring
every site gate would be more ceremony than that action warrants. The
`proposed artifact(s)` field provides a place to scope the decision, but the
current checklist does not spell out a channel-specific `NOT APPLICABLE` path.

This is not a present P2: no `GO` is available, no release is authorized, and
the current candidate is explicitly a combined public-review/release aid. At
the later owner decision, either use only the gates relevant to the exact
artifact and record why others are not applicable, or prepare a bounded
channel-specific checklist. Do not weaken the current fail-closed status or
turn `GO` into agent authority.

## Public-only navigation correction

### Finding CL-SITE-01 — header spacing

**Disposition: Accepted with revision already embodied in the reviewed file. Severity: no P0/P1/P2.**

The public QA report reproduced a real baseline defect: at 1280px the public
principal-link gap was 4.8px, and at 390px it was 0px with touching rectangles
(`f231:qa/publication/OPPORTUNITY_EXPANSION_PUBLIC_MENTOR_REHEARSAL_QA_2026-08-30_d05aca5.md:40-51`).
The commit adds only `.mode-public .primary-nav { gap: 0.6rem; }` and a narrow
`.mode-public .primary-nav { gap: 0.18rem; }`. At the default 16px root this is
9.6px wide and 2.88px narrow. The default review `.primary-nav` gap remains
0.3rem / 4.8px because no `.mode-review` selector was added.

Both standalone exports contain the same public-only rule, and the focused test
checks the wide and narrow declarations, review non-inheritance, generated mode
markers, and all three principal links. This is a small reversible correction,
not a new route or publication mechanism. Removing the rule restores the
measured concatenation; keeping it does not alter thesis, six-family topology,
Stage 0, or public authorization.

## Removal, proportionality, and fail-closed tests

### Removal matrix

| Candidate | Read-only removal result | Cross-lane disposition |
| --- | --- | --- |
| `publication/README.md` | Site and owner packet remain usable; three focused notes remain findable only by direct path. Safe order/source map/unresolved warning are lost. | Retain as optional index; defer one future discoverability pointer. |
| `publication/MENTOR_REVIEW_SEQUENCE_V16.md` | Site, cover note, and owner packet remain usable; the compact challenge/response workflow is lost. | Retain; it supplies a distinct conversation-sized next step. |
| `publication/X_COPY_VARIANTS_V16.md` | No site or owner-packet behavior changes; only platform-copy rehearsal is lost. | Retain as unsent optional rehearsal; no portable inclusion. |
| `publication/RELEASE_DECISION_CHECKLIST_V16.md` | Machine release gate remains; the human identity/manual/action gate becomes easier to mistake for a build command. | Retain fail-closed; defer channel-specific scoping. |
| Public nav CSS rule and generated export delta | Reverting restores the measured 4.8px/0px public spacing defect. | Retain public-only fix and focused contract. |
| Dedicated Publication site route/release machinery | No substantive reader behavior is lost; existing ten-route public adapter remains intact. | Reject; it would put release ceremony in the reader path. |
| New visual/bitmap/social-card candidate | Existing code-native Home reveal, Map, semantic standalone, and untagged PDF remain teachable. | Reject current candidate; defer any social-image decision to owner-authorized release. |
| Generic adoption/conformance layer in this lane | Existing agent/project-use work remains separate and the public kit does not need it to act. | Reject here; keep adoption work in the agent lane and subject to repeated-friction evidence. |

The removal test supports keeping the focused notes only as optional packaging;
it does not support promoting them into a required seventh family, route,
ledger, score, or project protocol.

### Contract and fail-closed results

The exact public worktree was clean at the reviewed commit. After rebuilding
that worktree, all of the following passed:

1. `npm run build` from `f231:site/` — ten review routes, review standalone,
   ten public routes, and public standalone rebuilt.
2. `node ../qa/publication/publication-kit-contract.spec.mjs` from `f231:site/`
   context — required kit files, source links, unresolved fields, local copy
   lengths, no invented URL/handle, and no-bitmap gate passed.
3. `node ../qa/site/public-nav-spacing-contract.spec.mjs` — public-only wide /
   narrow spacing, review non-inheritance, mode markers, and principal links
   passed.
4. `npm run check` from `f231:site/` — route, content, public-mode, release-gate,
   Stage 0, permission, human-action, interaction, map, term, reader-language,
   and selector checks all passed.
5. Targeted `git grep` outside `publication/**` and `qa/publication/**` found no
   runtime, owner-packet, root-navigation, framework, or Signal Foundry bundle
   dependency on the four optional publication files. This confirms that their
   removal is reversible and that they are not hidden mandatory inputs.
6. `f231:site/public-dist/build-manifest.json` and `dist/build-manifest.json`
   both report `release_build: false`, identical ten route IDs and canonical
   source hashes. Generated public Home reports
   `LOCAL_PREVIEW_UNSET` and `noindex,nofollow`, with no canonical or author
   metadata.

No physical deletion was performed in the reviewed worktree; the removal
matrix is a reversible dependency/behavior test. The contract itself is
allowed to fail if its optional kit is removed, while the core site check does
not import the kit. That separation is the proportional behavior expected of
an optional package.

## P3 maintenance coupling in the focused tests

### Finding CL-QA-01 — exact draft lengths and global image assertion

**Disposition: Deferred; retain the current contract for this candidate.**

`publication-kit-contract.spec.mjs` uses exact character counts for the three
single-post drafts and four thread posts (`f231:qa/publication/publication-kit-contract.spec.mjs:44-59`).
It also asserts a global zero-candidate image ledger and empty generated-candidate
directory (`:86-91`). The length checks are useful local copy aids and catch an
accidental edit before a future authorized channel check, but they necessarily
fail on any intentional copy revision. The image assertion can also become
coupled to an unrelated future asset candidate.

This is a P3 maintenance risk, not a current boundary or behavior failure:
the test does not assert the whole essay, does not authorize a post, and is not
wired into the core site `npm run check`; the public-nav test is the only new
publication-related test added to that command. Keep the fail-closed token,
metadata, source-link, and no-URL/handle assertions now. If copy or visual
work later changes, the owner/integrator may replace exact counts with a
channel-limit assertion and compare image state against a declared baseline,
but must not solve this by adding a second schema or release authority.

## Project-use bridge and Signal Foundry recommendation

### Finding CL-TRANSFER-01 — do not merge publication rehearsal with project use

**Disposition: Rejected for this lane; project-use work remains in the agent lane.**

The public commit's portable builder explicitly selects the agent-facing
Quickstart, full guide, copyable brief, preflight, decision receipt, and
ordinary/layered examples (`f231:handoff/signal-foundry/build_portable_bundle.py:95-110`).
It intentionally excludes the public adapter, publication configuration,
public-mode QA, visual captures, and future-study decision memo
(`:255-265`). The publication kit is absent from the selected `SOURCE_PATHS`,
and the owner packet describes those public artifacts as repository review
material rather than Signal Foundry implementation inputs.

There is therefore no missing project-use bridge in the public kit: adding one
would mix the reader/public channel with the observable agent/operator contract,
manufacture cross-lane ceremony, and risk implying transfer validation. The
project-use starter on the agent lane is the appropriate bridge for a materially
different future project. It should remain repo-only unless repeated real-project
friction and a later owner decision justify a separately reviewed transfer
subset. Specifically, the accepted starter should remain out of the existing
Signal Foundry portable selection for now; that bundle should continue to carry
the already-selected agent entry points and typed applied fixtures, not
publication copy or release gates.

If the owner wants a human to discover both paths, add a single cross-reference
at a future owner-review index boundary. Do not put publication files into the
Signal Foundry bundle, do not put project intake into `publication/`, and do not
make either path a universal conformance requirement.

## Complete disposition ledger

| Finding / source-lane item | Disposition | Severity | Affected files or paths | Governing reason |
| --- | --- | --- | --- | --- |
| `PUB-01` four-file entry point | **Accepted with revision** | none | `publication/README.md` | Useful safe order/source map; optional convenience, not a second authority. Discoverability deferred separately as `CL-PUB-01a`. |
| `PUB-02` mentor sequence | **Accepted** | none | `publication/MENTOR_REVIEW_SEQUENCE_V16.md` | Distinct challenge/response action; no contact, sign-off, or comprehension claim. |
| `PUB-03` X copy | **Accepted with revision** | none | `publication/X_COPY_VARIANTS_V16.md` | Useful channel rehearsal; no URL/handle/CTA or posting authorization. |
| `PUB-04` release checklist | **Accepted with revision** | none | `publication/RELEASE_DECISION_CHECKLIST_V16.md` | Joins human identity, source, manual, claim, and action gates while staying HOLD/NOT AUTHORIZED. Channel scoping deferred as `CL-PUB-04a`. |
| `PUB-05` Publication route/release machinery | **Rejected** | none | `site/**` | Duplicates the ten-route reader surface and pollutes human-first entry with release ceremony. |
| `PUB-06` one-page visual candidate | **Rejected** | none | `assets/diagrams/publication/**` | Existing code-native reveal, Map, standalone, and PDF suffice; removal changes no teaching capability. |
| `PUB-07` bitmap/social card | **Rejected for current need; social-image decision Deferred** | none | `assets/generated-candidates/**`, image ledger | No written bitmap need or authorized destination; no candidate was created. |
| `PUB-08` public nav spacing | **Accepted with revision** | none | `site/src/site.css`, standalone exports, nav contract | Reproduced public-only defect; narrow reversible CSS fix, review unaffected. |
| `PUB-09` generic adoption/conformance artifact | **Deferred** | none | `framework/**`, portable bundle | D-031/D-033/D-034 keep adoption work gated on repeated materially different project friction. |
| `CL-PUB-01a` kit not linked from owner packet/root | **Deferred** | P3 | owner packet/root index (future) | Optional convenience is usable directly; future discoverability pointer needs owner/package decision. |
| `CL-PUB-04a` all manual gates on every future channel | **Deferred** | P3 | release checklist (future) | Scope gates to exact artifact at later owner decision; current HOLD remains correct. |
| `CL-QA-01` exact lengths/global image assertion | **Deferred** | P3 | publication contract (future) | Current sentinel contract is safe; future copy/image changes may warrant lower-coupling assertions. |
| `CL-TRANSFER-01` project-use bridge in publication/Signal Foundry | **Rejected** | none | `publication/**`, portable `SOURCE_PATHS` | Wrong artifact boundary; retain agent starter repo-only and out of portable selection. |

## Remaining boundary

This report does not establish mentor agreement, reader comprehension, public
engagement, publication readiness, framework effectiveness, project transfer,
Signal Foundry behavior, or any empirical result. It does not authorize a
byline, handle, URL, social image, post, message, mentor contact, deployment,
merge, Release, study, provider, corpus, spend, or external dataset. The
reviewed public candidate remains local and noindex/nofollow; the reviewed
release checklist remains HOLD / NOT AUTHORIZED.

The public/mentor lane is therefore acceptable for owner review as an optional
rehearsal package, with only the three nonblocking P3 follow-ups above. The
project-use bridge remains the separate agent-lane concern and should not be
folded into this public kit or the existing Signal Foundry portable selection.
