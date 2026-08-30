# Handoff and owner review

This directory contains the local owner-review handoff:

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
- `../site/exports/standalone/pattern-map-v16.html` — direct-open owner-review
  composition;
- `../site/exports/standalone/pattern-map-v16-public.html` — direct-open
  prose-first public preview generated from the same canonical sources;
- `OWNER_REVIEW_MANIFEST_V16.json` — checksums for the bounded review package;
- `verify_owner_review_package.py` — deterministic manifest writer/verifier.

An owner-review release is not a publication, deployment, GitHub Release,
empirical result, or authorization to merge.
