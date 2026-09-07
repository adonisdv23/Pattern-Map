# GitHub checkpoint recommendation — v15.1

Status: `READ_ONLY_REPOSITORY_ORIENTATION_COMPLETE_NO_REMOTE_WRITE_AUTHORIZED`

Recorded: 2026-08-18

Repository reviewed: `adonisdv23/Pattern-Map`

## Answer first

The repository is an appropriate long-term home for the curated Pattern Map
project, but its current `main` branch should be treated as a historical v14
transfer checkpoint rather than the structure onto which v15.1 is appended.

No push, default-branch change, tag, release, or repository setting change is
authorized by this recommendation.

## Current remote state

- Visibility: public.
- Default branch: `main`.
- Two commits were visible at review time.
- The principal commit adds the complete v14 transfer package.
- The repository root contains a single large
  `Discrimination-Layer-V14-Complete-Transfer-2026-08-18/` directory rather
  than a reader-facing project root.
- No root `README.md` or root `package.json` was present.
- The transfer contains duplicated repository snapshots, intermediate review
  logs, generated images, PDF page renders, and other archival evidence useful
  for recovery but unsuitable as the primary public navigation structure.

## Recommended checkpoint

1. Preserve the current remote `main` exactly as the v14 historical checkpoint.
2. When the owner authorizes GitHub writes, create a durable tag or branch such
   as `archive/v14-transfer-2026-08-18` at the current remote commit.
3. Prepare v15.1 in a clean branch whose root is the actual project rather than
   another dated transfer directory.
4. Review the curated branch locally before any push.
5. After owner approval, push the branch and open a draft pull request or make
   it the candidate default branch in a separate explicitly authorized step.

Because the local v15 history and remote v14 transfer history were created
independently, do not perform an automatic unrelated-history merge. Prefer a
curated v15.1 root plus an explicit pointer to the immutable v14 checkpoint.

## Recommended public root

```text
README.md
site/
source/
framework/
research/
tools/
tests/
docs/decisions/
archive/v13/
LICENSE
CITATION.cff
```

Large owner ZIPs, intermediate PDFs, page-by-page render images, raw model
transcripts, and repeated full repository snapshots should move to GitHub
Releases, a private archive, or an external evidence bundle. They should not
dominate the normal source tree.

## Public/private boundary to decide before migration

The current repository is public. Before making it canonical, review whether
raw model reviews, owner-only decision notes, historical chat artifacts, and
large QA evidence are intended for public release. The recommended public
repository contains the curated argument, current site, research protocol,
reproducible code, tests, citations, and bounded decision records. Internal
review history can remain in the local owner package.

## Why the checkpoint is timely

V15 has a verified clean package, a working site, a stable conceptual map, an
explicit research boundary, and reproducible offline scaffolding. V15.1 is a
convergence release rather than another recovery pass. That is the right point
to establish a durable project identity and stop treating each version as a
standalone transfer folder.
