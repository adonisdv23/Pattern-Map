# Owner-package control ultra QA — 2026-08-30

Status: **accepted with revision at the source/pre-seal boundary — no remaining
P0/P1; final exact-commit manifest, clean-suite run, upstream readback, and ZIP
attestation are terminal external steps**

## Scope and authority

This lane began from exact clean checkpoint
`76ade6e2c255151e32ddd9cbb3d4650cf46570d1` on
`codex/pattern-map-v16-ultra-finalization`. It answers a narrow transfer
question: can an owner receive one complete deterministic ZIP from an exact
committed tree, verify the original container, verify a copied extraction
without Git, distinguish that result from the complete Git-only suite, and
see every remaining human/publication gate?

The locked owner-intent checksum passed before and after the source review.
The lane made no change under `archive/**`, the curated Echo sources, or
`handoff/signal-foundry/**`; the selected Signal Foundry packet remains sealed
at `529852497109dc152928de642038d07b109a52e2`. No merge, deployment,
publication, Release, research/provider/model/participant run, purchase,
dataset acquisition, preregistration, or outreach occurred.

This report records source and adversarial-control evidence. It is not an
authenticity signature, recipient comprehension result, or publication
authorization. Final remote and ZIP observations are deliberately external to
the manifest-covered narrative so they cannot create a self-referential seal.

## Resulting control model

The repository now distinguishes two complementary manifests:

1. `handoff/OWNER_REVIEW_MANIFEST_V16.json` is a bounded selected-artifact
   manifest. Its checked-in verifier has a recipient-only default and one
   author-only write mode guarded by an exact confirmation token, a named
   feature branch, and a completely clean tracked/untracked checkout.
2. `FULL_PAYLOAD_MANIFEST.json` is generated at the owner ZIP wrapper root and
   covers every regular file read from one exact Git tree plus strict metadata
   and generated controls. `VERIFY_PACKAGE.py` validates a copied extraction
   without `.git`; the separately delivered `.zip.sha256` binds the original
   ZIP bytes.

The package builder stages bytes from Git objects rather than the working
tree, requires the requested commit to equal the current clean named
non-default branch tip, optionally requires the upstream tip to match, and
verifies the committed bounded manifest inside the staged `repository/` before
producing package metadata. The staged bounded verifier must byte-match the
trusted builder-adjacent verifier, and the locked owner-intent bytes must match
the fixed owner identity.

The package has one enclosing directory, deterministic timestamps and
permissions, branch-name-independent metadata, sorted strict JSON records,
and a copied-location verification rehearsal before publication. Publication
to the output directory uses an exclusive build lock and exclusive hard-link
creation; it never overwrites an existing ZIP or sidecar. Cleanup removes only
paths whose inode is still owned by the invocation.

## Blue-team findings and dispositions

| ID | Severity | Finding | Disposition | Correction |
| --- | --- | --- | --- | --- |
| OPC-01 | P1 | `source_ref` made same-commit ZIP bytes branch-name dependent | **Accepted with revision** | Removed from package metadata; the author-facing summary may still name the branch. Renamed-branch ZIP and sidecar are byte-identical. |
| OPC-02 | P1 | An existence-check/replace race could overwrite and then delete another actor's artifact | **Accepted** | Exclusive lock, hard-link publication, inode/type checks, and owned-inode-only cleanup; both ZIP+sidecar and sidecar-only races preserve foreign sentinel bytes. |
| OPC-03 | P1 | The full builder could ship a stale bounded selected-artifact manifest | **Accepted** | Require and run the exact trusted bounded verifier inside staged payload; locked owner identity is checked; stale manifest and changed-owner controls block construction. |
| OPC-04 | P1 | Critical new package controls were outside bounded coverage | **Accepted** | START_HERE, both complete-package programs, their adversarial test, and the final QA evidence enter `REQUIRED_PATHS`; prose does not hard-code a brittle file count. |
| OPC-05 | P1 | A literal private-key test fixture in the exact repository made the all-payload guard reject production input | **Accepted with revision** | One exact path plus exact SHA-256 exception preserves the sealed fixture; byte drift or relocation fails. No sealed file was edited. |
| OPC-06 | P2 | Portable-path checks missed later colons, device names, trailing dot/space, controls, `?`, and Unicode-normalization aliases | **Accepted** | Reject absolute/parent/dot/backslash/repeated-separator forms, forbidden characters, controls, reserved device basenames, trailing dot/space, case aliases, and NFC/NFD aliases; reject symlink, gitlink, special-mode, and non-UTF-8 entries. |
| OPC-07 | P2 | Common extraction can drop an executable bit, making a direct shell invocation unusable | **Accepted with revision** | Recipient commands use `sh qa/run_owner_review_checks.sh`; the full manifest still records the canonical Git mode. |
| OPC-08 | P2 | Boolean `true` could equal schema version `1`, and regex-shaped impossible dates could pass | **Accepted** | Require exact integer types and calendar-valid canonical ISO dates in builder and verifier. |
| OPC-09 | P2 | Extra empty directories were outside file-only inventory | **Accepted** | Derive and require the exact directory set and reject missing/extra directories and symlink directories. |
| OPC-10 | P2 | The full runner could do expensive work on a dirty checkout and formerly could report a complete PASS after unbounded dirt | **Accepted with revision** | Normal mode now fails before stage 1 if any tracked/untracked state exists and rechecks at stage 12 to detect suite-created mutation. Extracted mode labels Git-only stages `NOT RUN`. |
| OPC-11 | P3 | Credential/marker scanning could be overread as comprehensive secret detection | **Rejected** | Add `.netrc` and `.pypirc` to the narrow high-signal path guard and explicitly state that arbitrary-secret absence is not proved. General token-shape scanning is not added. |
| OPC-12 | P3 | Production exact-tree preflight has nontrivial time and memory cost | **Accepted with revision** | The builder uses one binary-safe `git cat-file --batch`; current one-time local owner-package cost is acceptable. No persistent cache or dependency is added. |
| OPC-13 | P1 | The builder executed an exact-commit `VERIFY_PACKAGE.py` without binding it to the trusted builder-adjacent verifier | **Accepted** | Require byte identity with a non-symlink, stable-inode trusted adjacent verifier before staging or execution; a committed PASS stub now blocks construction. |
| OPC-14 | P1 | A source swap during hard-link publication or a final-ZIP replacement before sidecar completion could return success with foreign bytes | **Accepted** | Require destination/source inode identity immediately after each link, re-open the exact published inodes without following symlinks, rehash the final ZIP, and compare exact sidecar bytes before success. Both injected races fail while unowned bytes are preserved. |
| OPC-15 | P2 | An extracted repository nested inside an unrelated Git checkout could be misclassified as the real project Git root | **Accepted** | Normal mode now requires the physical `git --show-toplevel` path to equal the physical Pattern Map root; nested extractions fail before stage 1 and point to extracted mode. |
| OPC-16 | P2 | The bounded recipient verifier could follow a symlinked control manifest | **Accepted** | The manifest and every parent component must remain local, non-symlink, and regular before parse or author write; the symlink mutation fails. |
| OPC-17 | P2 | Authoring prose claimed a feature-branch boundary while detached HEAD and default branches were accepted in some paths | **Accepted with revision** | Both bounded-manifest writing and full-package construction now require a clean named non-default branch; explicit `main` and detached-HEAD controls fail. |
| OPC-18 | P1 | ZIP-member portability validation reapplied active-tree cache exclusions after adding the wrapper prefix, so an allowed immutable archived `__pycache__` path would block the real package | **Accepted** | Separate cross-platform path validation from repository hygiene policy and include an immutable archived-cache path in every complete fixture build. |

The blue team independently reproduced each P1/P2 before correction. Its first
recheck isolated the late dirty-tree P2; a deeper final pass then reproduced
OPC-13–OPC-18. The integrator converted each reproduction into a permanent
negative control and reran the complete hostile suite. After those revisions,
no reproduced P0/P1 remains. OPC-11 and OPC-12 remain explicit P3 boundaries.

## Adversarial coverage

The standard-library unit suite covers:

- author-only bounded-manifest writing from a clean named non-default branch;
- strict manifest keys, duplicate JSON keys, nonfinite values, Boolean schema
  versions, symlink controls, and calendar-invalid dates;
- exact-commit, named non-default branch, detached/default-branch, dirty-tree,
  local-ahead/upstream, older-commit, output-inside-repository, existing-target,
  and output-race rejection;
- same-commit determinism across branch names;
- trusted-inode binding for both executable verifiers plus staged bounded-
  manifest and owner-intent verification;
- complete payload byte counts, SHA-256 values, canonical Git modes, generated
  control schemas, and one enclosing ZIP root;
- absolute, parent, dot, repeated-separator, backslash, drive-prefix, collision,
  duplicate, symlink, FIFO/special, and corrupt-CRC ZIP adversaries;
- portable wrapper paths that retain an allowed immutable archived-cache
  artifact without weakening the active-tree cache/dependency exclusion;
- changed, missing, and extra files; extra empty directories; symlinked
  extraction paths; false merged/released status; extra/missing control keys;
  removed manual gates; and changed generated controls;
- exact private-key-marker fixture identity and path containment;
- source-swap and post-publish ZIP replacement races with final digest/sidecar
  revalidation; and
- the no-Git and nested-unrelated-Git handoffs plus dual normal-mode cleanliness
  checks.

The production exact-HEAD path/payload preflight also passes for the current
tracked tree. That preflight is source hygiene and package feasibility, not a
claim that arbitrary content is safe, true, licensed, or authorized.

## Recipient truth table

| Context | Command | Truthful claim |
| --- | --- | --- |
| Original ZIP plus external sidecar | `shasum -a 256 -c …zip.sha256` | Exact ZIP bytes match the separately supplied digest; authenticity still depends on a trusted digest channel |
| New clean extraction, wrapper root | `python3 VERIFY_PACKAGE.py` | Every shipped path/control matches the strict embedded full manifest and schema |
| Extracted `repository/` without Git | `sh qa/run_owner_review_checks.sh --extracted-package` | Artifact/implementation checks passed; Git-only stages 10 and 12 are explicitly `NOT RUN` |
| Clean named Git clone/worktree | `sh qa/run_owner_review_checks.sh` | Complete twelve-stage local source/artifact suite passed at that exact clean checkout |

No mode may be relabeled as another. An embedded manifest and verifier prove
consistency, not authorship. A coordinated ZIP/verifier/manifest/sidecar
replacement can reseal different bytes; no digital-signature infrastructure
is claimed or introduced.

## Publication and human gates preserved

The package carries explicit unresolved gates for owner/mentor comprehension,
voice, naming, physical keyboard, supported screen reader, real 200% zoom,
forced colors, native browser print preview, hardware touch, byline, canonical
URL, social image and alternative text, copyright/license selection,
historical-image and social-image rights, publication destination, live links,
and explicit merge/publication authorization. No license was selected and no
rights clearance was inferred from repository presence.

## Terminal sequence after source freeze

1. Commit all source/evidence bytes.
2. Run the bounded author-only manifest writer from that clean named
   non-default feature branch, then commit only the regenerated manifest.
3. Push and read back the exact upstream tip.
4. Run the complete twelve-stage suite from the exact clean checkout.
5. Build outside the repository with `--require-upstream` into a new output
   directory that contains no target artifact.
6. Verify the original sidecar, copy/extract elsewhere, run wrapper-root
   `VERIFY_PACKAGE.py`, and run the extracted partial suite with `sh`.
7. Record exact commit, remote/PR state, ZIP digest, and copied-extraction
   observations externally rather than rewriting this manifest-covered report.

Until those terminal observations exist, this is a source/pre-seal control
PASS, not a claim that the final transmitted ZIP has already been delivered.
