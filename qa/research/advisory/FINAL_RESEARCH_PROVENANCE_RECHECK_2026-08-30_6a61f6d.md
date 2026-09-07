# Final research / provenance recheck — exact `6a61f6d`

Status: **PASS WITH ONE P1 PROVENANCE CORRECTION**

This was an independent read-only review of exact clean checkpoint
`6a61f6da9b2c1f0255dd5d8a15e596c88b031f36`. It is advisory model evidence,
not literature completeness, an empirical result, owner approval, or proof of
effectiveness.

## Finding

**RP-R2-01 — P1, accepted.** `handoff/verify_owner_review_package.py` still
attributed the current owner-review PDF to `72a672c`, although the current PDF
bytes first appear at exact `6a61f6d`. A regenerated manifest could therefore
pass byte verification while carrying false producer provenance. Update the
fixed PDF checkpoint to the full `6a61f6d` hash, preserve the historical
`72a672c` disposition as superseded provenance, confirm the PDF bytes remain
unchanged after the correction, and regenerate the owner manifest only after
all source and evidence stop moving.

The integrator accepted this finding with a necessary sequencing revision:
the separately accepted Stage 0 correction changes page 5 and therefore
changes the PDF bytes after `6a61f6d`. The terminal seal must use two commits:
the first owns the regenerated PDF bytes; a successor then records that exact
producer commit in the manifest writer before final manifest generation.

Implementation: exact commit
`06c61680f709861ccd3ffd2df5029e04c63cb450` owns the regenerated PDF bytes;
its successor binds that producer value without self-reference.

## Confirmed strengths

The first-wave research-suite inclusion, bounded manifest scope, Echo
separation, no-results status, claim ceiling, and external-attestation rule
were all confirmed. No additional research, novelty, origin-accounting,
archive-integrity, or prohibited-action defect was found.
