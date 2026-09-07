# Council Ultra advisory code review

Reviewed 2026-09-07 by the Pattern Map development/review subagent.
Role: Codex advisory reviewer, **not Council's formal Auditor**.
Head: ea707b2595c8d686c672321c85770f0654752d9f.
Base: 1e82adaaa99a9b497f26aeb9cd7ce31447e1c43b.
Worktree: /Users/gpt/Documents/Codex/worktrees/council-pattern-map-ultra-2026-09-07.
The checkout was clean before and after review; no Council files were changed.

**Finding: no blocking or actionable defect found in the reviewed scope.**
Recommend retaining this bounded change for root integration review. This is
not merge authorization, an independent formal Auditor verdict, or evidence
that any recorded independence judgment is factually correct.

## Evidence supporting the assessment

- **Current independence binding:** council_desk/opportunities.py:381–412
  binds the normalized decision specification and complete evidence set.
  State/lifecycle bookkeeping is intentionally excluded. The convergence path
  at lines 416–490 requires both the current binding and scoped, explicit
  assessments; it does not upgrade unknown or conflicting origin members.
  Evidence order is normalized. The service accepts only an explicitly
  submitted matching binding (council_desk/service.py:550–555); the read-only
  context command does not record review (lines 590–602).
- **Stale projection, rank and discrimination:** service.py:1750–1758 requires
  the new evaluation contract and a current deterministic evaluation digest.
  Lines 1765–1770 reconstruct authored fields instead of leaking old derived
  fields from transition revisions. Ranking consumes the filtered projections
  at lines 1825–1835, and discrimination uses the same currentness check at
  lines 1849–1851. storage.py:1486–1504 recomputes peer factors from current
  inputs without recursive peer evaluation.
- **Weak-warning path:** opportunities.py:507–519 accepts the existing warning
  route only when the exact warning is covered by a current evidence review.
  It preserves the distinction between zero independently assessed origins and
  a deliberately reviewed weak-evidence exception. Other readiness conditions
  remain required. The regression at
  tests/test_council_independence_compatibility.py:213–226 covers expiry after
  a claim change and restoration through explicit review.
- **Experiment append boundary:** service.py:649–675 checks the recorded
  lifecycle, reevaluates current prerequisites, and carries the opportunity
  revision/evidence-link bindings into append. storage.py:1621–1635 compares
  them inside the write transaction; connection() begins IMMEDIATE at
  storage.py:560–561. A competing revision or link addition cannot pass between
  that comparison and INSERT. The injected race regressions at
  tests/test_council_independence_compatibility.py:256–272 produce no experiment
  record. This guard specifically protects opportunity/evidence prerequisites;
  it does not promise an atomic snapshot of every peer, memory or track-record
  input used for the descriptive evaluation.
- **History:** old evaluation records remain stored. Tests exercise stale
  display removal without overwriting the original evaluation, no-op updates,
  review restoration, preservation of conflicting origin members, and explicit
  supersession. The compatibility document accurately distinguishes local
  migration guidance from a production migration.

## Independent checks

Read AGENTS.md, the verified Context Pack, Codex handoff, independence contract,
changed product source and compatibility regressions. The Context Pack verifier
returned CONTEXT_PACK_FRESH with digest
03491dd6980a147cec05fd5608d1ba50729c6fe8c0587a8c617654522df15bc4.
Its process-state snapshot is
COUNCIL_COMMAND_CENTER_COMPLETION_CONTRACT_MERGED_MAIN_RECONCILED_001;
this review makes no product-readiness inference from that state.

Executed with the repository's existing Python environment:

    PYTHONDONTWRITEBYTECODE=1 /Users/gpt/Documents/Codex/projects/Council-of-Reeds/.venv/bin/python -m pytest -q tests/test_council_independence_compatibility.py tests/test_council_opportunities.py tests/test_council_service.py --basetemp /Users/gpt/.codex/tmp/council-ultra-independent-advisory

Result: **70 passed in 9.89 seconds**. These are deterministic tests using
disposable stores under /Users/gpt, not empirical or operator-history evidence.
I did not rerun the broader 250-test product suite reported by the implementer.
No production store, provider, study, external mutation or publication was used.

## Residual judgment

The review digest records an explicitly submitted judgment; it does not verify
authorship, understanding, source truth or action permission. The public text
states that boundary. The append check is intentionally narrower than a general
authorization or serializable evaluation service. I found no requirement in the
assigned change that warrants expanding it into either.

Next action: root should inspect and disposition this advisory review alongside
the exact Council commit; Council's formal Auditor/Operator merge process remains
separate.
