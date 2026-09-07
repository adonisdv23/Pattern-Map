# Handoff and owner review

This directory contains the local owner-review handoff:

- `START_HERE_OWNER_REVIEW.md` — recipient entrypoint distinguishing original-
  ZIP, extracted-package, and Git-checkout verification;
- `OWNER_REVIEW_PACKET_V16.md` — outcome, review path, verification, and owner
  decisions/checks;
- `PACKAGE_MAP_V16.md` — canonical artifact map;
- `BRANCH_AND_PR_STATE.md` — pushed branch and draft-PR state;
- `signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md` — canonical v16 source,
  downstream seam, and orphan-recovery record for Signal Foundry;
- `signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md` — copyable tired-owner
  and Claude Code handoff; give it together with the canonical handoff;
- `signal-foundry/build_portable_bundle.py` — deterministic exact-commit
  cross-computer ZIP/manifest/verifier/sidecar builder;
- `../qa/handoff/advisory/CLAUDE_PUBLIC_TRANSFER_TERMINAL_AUDIT_2026-08-30_fb7d808.md`
  — exact-checkpoint independent sealing audit and limitations;
- `../qa/handoff/ULTRA_FINALIZATION_TERMINAL_QA_2026-08-30.md` — bounded
  finalization corrections, removal decisions, exact producer identity, and
  open manual gates;
- `../qa/handoff/RED_BLUE_ULTRA_FINALIZATION_QA_2026-08-30.md` and
  `../qa/handoff/OWNER_PACKAGE_CONTROL_ULTRA_QA_2026-08-30_76ade6e.md` — final
  rendered/receipt/package convergence, blue-team dispositions, and exact
  terminal sealing sequence;
- `../site/exports/standalone/pattern-map-v16.html` — direct-open owner-review
  composition;
- `../site/exports/standalone/pattern-map-v16-public.html` — direct-open
  prose-first public preview generated from the same canonical sources;
- `OWNER_REVIEW_MANIFEST_V16.json` — checksums for the bounded review package;
- `verify_owner_review_package.py` — strict verifier plus an explicitly author-
  only bounded-manifest writer;
- `build_owner_review_bundle.py` — deterministic exact-clean-commit builder for
  one enclosing-directory full owner ZIP and external SHA-256 sidecar; package
  bytes are independent of the branch name, the committed bounded verifier is
  rerun inside the staged payload, and exclusive publication never overwrites
  an existing ZIP or sidecar; and
- `verify_extracted_owner_bundle.py` — standard-library verifier copied into
  the full bundle as `VERIFY_PACKAGE.py`.

The bounded manifest covers selected canonical review artifacts and the
ledgers/verifiers governing the larger immutable transfers. It is not a full
ZIP inventory. A built owner bundle instead carries
`FULL_PAYLOAD_MANIFEST.json`, which covers every shipped regular file from the
exact Git tree. Its external sidecar binds the original ZIP bytes; neither the
embedded verifier nor sidecar is a digital signature.

Never use `verify_owner_review_package.py --write` to verify received bytes.
That mode requires an exact clean named non-default Git branch and an explicit author
confirmation. Final package construction happens only after source, generated
exports, evidence, dispositions, and the bounded manifest stop moving.
Author-side credential-path and private-key-marker checks are deliberately
high-signal hygiene guards, not proof that arbitrary committed content is
secret-free. The exact committed tree remains the author's review boundary.

An owner-review release is not a publication, deployment, GitHub Release,
empirical result, or authorization to merge.
