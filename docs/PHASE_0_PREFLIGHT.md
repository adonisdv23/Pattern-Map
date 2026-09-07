# Phase 0 preflight record

Date: 2026-08-19
Branch: `codex/pattern-map-v16-foundation`

## Destination repository

- Repository: `/Users/gpt/Documents/Codex/projects/Pattern-Map`
- GitHub: `https://github.com/adonisdv23/Pattern-Map`
- Baseline commit: `5eea2381c86400bacc1bc2a6df0e3af78bd6330a`
- Baseline branch state: `main` tracking `origin/main`, zero ahead and zero
  behind, clean working tree.
- Authenticated GitHub identity: `adonisdv23`, with admin and push permission.
- Push-path dry run before the handoff: success, everything up to date.
- Repository-specific `AGENTS.md` before foundation: none.

## V14 transfer

- Original root folder contained 430 files and occupied 91,184 KiB on disk.
- Transfer manifest records packaging commit `d0d26e2` and artifact baseline
  `261c516`.
- `shasum -a 256 -c 00_START_HERE/SHA256SUMS.txt`: pass for every entry.
- The folder was moved with `git mv` to
  `archive/transfers/v14-complete-2026-08-18/`.

## V15.2 source and owner archive

- Source checkout was clean at
  `36568cb6e8afce9544606c968319b063fc9b79ce`.
- The source repository has no configured Git remote, making canonical
  accession especially important.
- ZIP size: 41,436,496 bytes.
- ZIP SHA-256 matched the owner-provided value and original sidecar.
- Package manifest parses as JSON and declares 239 selected payload files,
  48,717,432 payload bytes, no empirical results, no study run, and no prior
  external publication/deployment/push.
- `unzip -t`: pass; no compressed-data errors.

## Binary-policy finding

Git LFS is not installed. The ZIP is below GitHub's 50 MiB warning threshold
and 100 MiB hard block, but exceeds the recommended ordinary-object size. Git
LFS has included allowances but is a metered service after quota; actual account
usage and budget settings could not be read with the existing GitHub scope, so
adopting it cannot presently guarantee zero hidden cost.

The four authorized candidates were compared explicitly. One blob and chunks
both add the full opaque payload to Git; chunks add reconstruction burden without
reducing history. Extracted source is materially better here: 102 of the 239
payload files, representing 30,298,057 of 48,717,432 bytes (62.19%), already
exist byte-for-byte in the v14 transfer and can be deduplicated by Git. The
accepted strategy is therefore verified extracted payload plus the unchanged
sidecar and manifest and a precise accession record. The exact ZIP remains
untouched at its verified source path until the owner authorizes an LFS or
Release channel with known budget controls.

## Prohibited actions confirmed

No source archive was deleted or rewritten. No merge, deployment, publication,
Release, study, provider call, participant activity, dataset acquisition,
preregistration, outreach, or spend occurred during preflight.
