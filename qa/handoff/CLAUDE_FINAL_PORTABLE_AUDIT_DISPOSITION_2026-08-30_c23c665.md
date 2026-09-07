# Claude final portable-packet audit — disposition

Date: 2026-08-30  
Reviewed source commit: `c23c6659b31aa008fce41bbf71a714a6a182d3ca`  
Reviewed packet SHA-256: `be1addcd2722e74d62e7ed1f1269036f6c4ee73c2f795dd0361d43ba5a03f0ca`  
Review mode: Claude Code, Opus, maximum effort, read-only isolated extraction

Claude returned a conditional pass with one P1 and four P2 recommendations.
Two independent project red-team lanes then reproduced or challenged each
finding against the locked authority order. This record is advisory review,
not owner approval, human-reader evidence, accessibility evidence, or proof of
effectiveness.

| ID | Claude finding | Disposition | Integrator reason |
| --- | --- | --- | --- |
| CFP-01 | Root `AGENTS.md` can auto-load Pattern Map mutation authority inside a read-only downstream packet | **Accepted with revision (P1)** | Exclude the control file from the selected packet rather than asking an auto-loaded instruction file to disclaim itself. Canonical intent and guardrails remain in non-executable source documents. |
| CFP-02 | Bundled source documents advertise commands that require the full repository | **Accepted with revision (P2)** | Preserve useful provenance documents, but add a generated command-capability table, copyable-prompt warning, and a direct full-checkout qualifier in the canonical handoff. |
| CFP-03 | The embedded verifier treats routine OS metadata as arbitrary injected payload | **Accepted with revision (P2)** | Warn and ignore only exact narrow metadata forms while continuing to fail on arbitrary extras, symlinks, missing files, and changed bytes. |
| CFP-04 | Source-only and manifest-covered file counts appear inconsistent | **Accepted as P3 clarity/test hardening** | Counts were arithmetically correct populations. Add a generated reconciliation and machine-lock their relationship. |
| CFP-05 | Write the sealed commit's latest GitHub readback into tracked branch-state prose | **Rejected** | D-036 and RP-02 require post-seal Git/PR/ZIP facts to remain in the external exact-hash attestation. Writing them back would move the head and recreate a self-referential reseal loop. Fresh readback independently matched the reviewed commit. |

The Claude process had no shell tool and correctly disclosed that it did not
execute the packet verifier, checksums, applied validator, browser, PDF, or
image checks. The primary orchestration path had already run those checks and
repeated them from a clean clone. Accepted corrections receive their own new
exact commit, full suite, push/readback, and generated packet identity; the
reviewed packet remains preserved rather than overwritten.

Manual owner/mentor comprehension and taste, physical keyboard, supported
screen reader, real zoom, forced colors, native print preview, hardware touch,
publication identity/configuration, and any claim of real-world usefulness
remain open.
