# Start here — Pattern Map v16 private owner review

Status: **private owner-review candidate**. This package has not been merged,
deployed, published, released, or empirically validated. Opening or verifying
it authorizes none of those actions.

This guide distinguishes three checks that answer different questions. A PASS
in one mode must not be relabeled as a PASS in another.

## 1. Check the original ZIP before extraction

Keep the ZIP and its separately delivered `.zip.sha256` sidecar together. From
their containing directory on macOS or Linux, run:

```sh
shasum -a 256 -c PATTERN_MAP_V16_OWNER_REVIEW_<date>_<commit>.zip.sha256
```

The sidecar binds the exact delivered ZIP bytes. Confirm the expected digest
through the owner's trusted delivery channel if authenticity matters. A hash
and an embedded verifier are not a digital signature; someone able to replace
the ZIP, verifier, manifest, and sidecar together could reseal different bytes.

## 2. Verify a clean extraction without Git

Extract into a **new empty directory**. The deterministic package has one
enclosing directory named `Pattern-Map-v16-<12-character-commit>/`. Enter that
directory and run:

```sh
python3 VERIFY_PACKAGE.py
```

This standard-library check rejects missing, extra, changed, duplicate,
unsafe, symlinked, or non-regular payloads and verifies the byte count and
SHA-256 of every shipped Git file plus the generated controls. It does not
need `.git`, Node, a provider, a model, a network connection, or a study.

The author-side builder also rejects a deliberately narrow set of high-signal
credential paths and private-key markers. That hygiene guard is not a general
secret scanner and cannot prove that arbitrary repository prose contains no
sensitive value; the exact committed tree remains the author's review boundary.

The full repository payload is under `repository/`. If the local Python and
Node prerequisites are available, the extracted artifact/implementation suite
can additionally be run with:

```sh
cd repository
sh qa/run_owner_review_checks.sh --extracted-package
```

That mode must label Git-only source-tip, canonical Signal-packet, and authored-
diff checks **NOT RUN**. It may never report the complete Git suite as passed.

Do **not** run `handoff/verify_owner_review_package.py --write` on a received
package. Writing is an author-only sealing operation, not verification.

## 3. Run the complete suite in a Git clone or worktree

Only a clean Git clone/worktree can check exact repository identity, the
canonical historical Signal packet commit, and authored export diffs. From the
repository root, run:

```sh
sh qa/run_owner_review_checks.sh
```

The runner fails early with a pointer back to this guide if `.git` is absent.
No reported CI checks currently substitute for this exact local evidence.

## Two manifests, two scopes

- `FULL_PAYLOAD_MANIFEST.json` at the extracted wrapper root covers every file
  shipped from the exact committed Git tree and is checked by
  `VERIFY_PACKAGE.py`.
- `repository/handoff/OWNER_REVIEW_MANIFEST_V16.json` is intentionally bounded
  to selected canonical review artifacts plus the ledgers/verifiers that govern
  much larger immutable archives. It is not a full ZIP inventory.

Archive payloads remain governed by their own immutable manifests. The
historical v13 map is an origin artifact, not the current topology. The Echo
Problem remains a separate, unrun research track with no results. The sealed
Signal Foundry packet remains fixed at its recorded checkpoint and grants no
downstream mutation authority.

## Suggested reading path

1. `repository/manuscript/NINETY_SECOND_VERSION.md`
2. `repository/manuscript/MENTOR_COVER_NOTE.md`
3. `repository/manuscript/PATTERN_RECOGNITION_V16.md`
4. `repository/site/exports/standalone/pattern-map-v16.html`
5. Optional builder and agent detail under `repository/framework/`
6. Package status, open decisions, and residuals under `repository/handoff/`

The routed site and semantic standalone HTML are the primary review surfaces.
The PDF is a secondary untagged visual companion.

## Gates that remain human or publication-time work

- owner/mentor comprehension, voice, naming, and taste;
- physical keyboard, supported screen reader, real 200% zoom, forced colors,
  native print preview, and hardware touch;
- license/copyright and historical/social-image rights;
- byline, canonical URL, destination, publication metadata, and link recheck;
- exact integration route and explicit merge/publication authorization.

Package verification is evidence about bytes and structural contracts. It is
not reader comprehension, accessibility acceptance, framework effectiveness,
research evidence, permission, publication, or release.
