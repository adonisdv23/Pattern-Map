# EP v0.1 QA and status evidence

Status: **PASS for preservation and scope containment; no research run**
Date: 2026-08-19, America/New_York

## Checks

| Check | Result |
| --- | --- |
| Owner-intent lock | `OWNER_INTENT_V16.md: OK` before editing |
| Source checkout | Clean at `36568cb6e8afce9544606c968319b063fc9b79ce` |
| Accession verifier | PASS: 239 payload files, 48,717,432 payload bytes, source ZIP 41,436,496 bytes, 240 ZIP members |
| Source ZIP hash | PASS: `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5` |
| Copied manifest | PASS: 69,680 bytes; `05aedafc2f5cb3f589cfdc69d1eff5c854c3bef97071324f9845d63a7a1028eb` |
| Copied sidecar | PASS: byte-for-byte match; sidecar SHA-256 `2eef19557580340df49cf95ad7d5ebe23c3bc2f350c29d7d992ad3bedc6b6870` |
| Preserved-source verifier | PASS: curated copies match accessioned bytes and hashes |
| Offline harness test | PASS: 15 deterministic local unittest cases; not a study or result |
| Model/provider calls | 0 |
| Empirical/participant studies | 0 |
| External dataset acquisition | false |

`git diff --check` is clean for newly authored EP v0.1 text, JSON, and Python
files. Git reports trailing whitespace or a blank final line in a small number
of copied v15.2 payload files; those bytes are intentionally preserved and were
not normalized because the accession policy requires exact source fidelity.

## Reproducible commands

From the repository root:

```sh
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
python3 archive/transfers/v15.2-owner-handoff/verify_accession.py \
  --source-zip /Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight/output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip
python3 research/the-echo-problem/qa/verify_preserved_sources.py
```

The source ZIP remains outside Git and untouched. The first command protects
the v16 contract; the second protects the accession; the third protects the
curated successor's exact copies. None runs a model or participant study.

## Advisory disposition

| Finding | Disposition | Reason and affected paths |
| --- | --- | --- |
| Preserve v15.2 as exact extracted source | Accepted | Required by `docs/BINARY_ARTIFACT_POLICY.md`; `archive/transfers/v15.2-owner-handoff/**`. |
| Treat EP as a separate successor beginning at v0.1 | Accepted | Required by the owner intent and artifact firebreak; `research/the-echo-problem/**`. |
| Carry forward every unfavorable-result class | Accepted | Required no-results boundary; `STATUS_AND_BOUNDARIES.md` and `FUTURE_EXECUTION_PLAN.md`. |
| Run the proposed model/empirical/participant study now | Rejected | Prohibited by the owner boundary; no model/provider/participant action occurred. |
| Treat QA or offline tests as evidence of effectiveness | Rejected | Integrity and implementation checks cannot establish a research result. |

## Residual issue

The exact ZIP container is intentionally not in Git. A clone without the local
source path can verify the extracted payload, manifest, and sidecar format but
cannot independently re-run the source-container hash check until an exact
owner-authorized storage route exists. The accession record states this
limitation explicitly.
