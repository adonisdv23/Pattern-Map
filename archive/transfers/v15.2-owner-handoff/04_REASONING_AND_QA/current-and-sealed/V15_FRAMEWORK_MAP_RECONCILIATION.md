# V15 framework-map reconciliation

Status: `COMPLETE · CONCEPTUAL CANONICALIZATION ONLY`

## Decision

The component map is canonical for the v15 owner-review package as a
**conceptual synthesis**, not as a validated mechanism or an exact-byte
reconstruction of the historical v13 site. This resolves a stale v14-era
status without enlarging the framework's evidentiary claim.

## Reconciled facts

- `archive/v13/pattern-recognition-diagram-v12.png` is the recovered original
  1024×1536 diagram. Its SHA-256 is
  `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`,
  exactly matching the owner-supplied expected hash.
- `archive/v13/live-v13-rendered-dom-snapshot.html` is a rendered-state
  reference with SHA-256
  `3c7a191ac44404828309cbfd8c58fa04eb9742bbbebe96879dd640a94e3645ec`.
  It is not the original standalone HTML and does not verify that missing
  file's expected hash.
- The standalone v13 HTML, `Research.zip`, and the named migration packet
  remain unavailable. Their absence stays visible and can still narrow a
  later historical interpretation.

## Compatibility and terminology disposition

- Component IDs `C01`–`C11`, family IDs `F1`–`F6`, and judgment-dimension IDs
  `D01`–`D08` are unchanged for audit compatibility.
- `D04` is now named `origin_relation`. The former `independence` name is
  retained in an explicit `legacy_compatibility_name` field instead of being
  silently erased.
- Reader-facing prose now distinguishes recurrence from a declared origin
  relation or stipulated distinctness. It does not equate that construct with
  real-world causal, editorial, methodological, or epistemic independence.
- The narrative's “nine core questions” are enumerated exactly; the additional
  machine-readable human-decision, cost, provenance, and open-question fields
  are named separately.

No component, causal condition, study denominator, empirical result, or
deployment claim changed in this reconciliation.
