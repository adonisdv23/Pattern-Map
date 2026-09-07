# V15.2 accession verification report

Status: **PASS — local preservation check**

Verification date: 2026-08-19, America/New_York

## Evidence

| Check | Result |
| --- | --- |
| Manifest-listed payload paths | 239 present; no missing or extra payload files |
| Extracted payload bytes | 48,717,432 |
| Per-file byte counts | PASS for all 239 entries |
| Per-file SHA-256 values | PASS for all 239 entries |
| Copied external manifest | 69,680 bytes; SHA-256 `05aedafc2f5cb3f589cfdc69d1eff5c854c3bef97071324f9845d63a7a1028eb` |
| Copied ZIP sidecar | Byte-for-byte match with source sidecar; SHA-256 `2eef19557580340df49cf95ad7d5ebe23c3bc2f350c29d7d992ad3bedc6b6870` |
| Source ZIP | 41,436,496 bytes; SHA-256 `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5` |
| ZIP member set | PASS: 239 payload members plus one embedded package-manifest member |
| ZIP CRC/data test | PASS |
| Embedded package manifest | Byte-for-byte match with external manifest |

## Command

```sh
python3 archive/transfers/v15.2-owner-handoff/verify_accession.py \
  --source-zip /Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight/output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip
```

The command is intentionally parameterized with the external ZIP. The exact
container is not in Git, so a clone without that local source can still verify
the extracted accession but cannot claim the source-container check passed.

## Interpretation boundary

This is an integrity and preservation result, not a research result. It does
not execute the origin-accounting harness, call a model or provider, acquire a
dataset, contact participants, or establish effectiveness.
