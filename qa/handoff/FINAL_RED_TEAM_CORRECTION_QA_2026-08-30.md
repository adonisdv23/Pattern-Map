# Final red-team correction QA — 2026-08-30

## Status and scope

Three independent read-only lanes reviewed exact clean checkpoint
`d40ca61c7b64ce89aabac2e36170e701b69c94d6` against locked owner intent:

- intent / cold reader;
- applied framework / interactive site;
- research / claims / provenance.

Their preserved reports are advisory evidence, not owner approval, reader or
participant results, accessibility results, literature completeness, or proof
that Pattern Map improves answers. The primary integrator reproduced every
accepted material finding before changing source.

## Accepted correction set

1. **Strict Stage 0 and layered input surfaces.** The recommendation module now
   accepts only the exact declared fields. Route, evidence, stop, execution,
   outcome, learning, influence, permission-alias, and human-disposition
   injections fail closed.
2. **Exact learning state machine.** Planned, pending, reviewed, and
   not-applicable outcome records have distinct exact key sets. Result, review,
   disposition, or update fields cannot appear before a reviewed state.
3. **One Advanced definition.** Consequential work, high uncertainty, and
   substantial separately approved capacity are jointly required. Volume,
   reuse, and longevity may shape capabilities but do not independently select
   Advanced.
4. **Executable F2 receipts.** Source role, relevant track record,
   claim-scoped authority, support, recurrence, origin, relevance, provenance,
   and permission remain distinct in the validated evidence record.
5. **No-script precedence.** Permission controls first, then the separate human
   action gate, then capacity mismatch, then the base planning action. Lower
   states remain visible.
6. **Public release-host gate.** Obvious local, internal, private, loopback,
   unspecified, link-local, and reserved example/test destinations cannot
   enable release metadata. Reachability still requires publication-time
   checking.
7. **Cold-reader entrance.** Public mode begins with ordinary-language meaning;
   its Read door stands alone; Home and Guided no longer repeat the same
   release example adjacently within their respective routed compositions.
   Review mode retains the mentor-continuation context.
8. **F2 public language.** The stable question is now: “For this claim, what
   can each source actually tell us—and how did the information reach us?” Its
   purpose supplies the boundary instead of repeating the question.
9. **Common-origin visual.** Nine observations and one known shared origin are
   retained, while independent corroboration for the broad validation claim is
   labeled `NOT ESTABLISHED`, not counted as zero.
10. **Precision and semantics.** The upstream-choice explainer states an
    inspectability limit rather than an absolute model-capability claim, and
    multi-clause “when not to use” guidance is a semantic list.
11. **Terminal process.** Research unit tests are part of the canonical runner;
    post-seal remote/PR/ZIP observations remain external exact-hash
    attestations rather than invalidating a self-hashed narrative.
12. **Collision-safe route anchors.** A live browser audit found that three
    repeated headings in the Examples source produced the same two IDs on a
    routed page even though the standalone normalizer later repaired them.
    The Markdown renderer now allocates deterministic `-2` and `-3` suffixes
    within a source fragment, shares that allocator with nested blockquotes,
    and preserves the first stable anchor. Review and public checks now reject
    duplicate IDs on every route; the semantic Python audit independently
    enforces the same contract.

The historical `qa/site/PUBLIC_MODE_BROWSER_QA_2026-08-30.md` statement that
public mode has no “route index” refers to removal of the owner-review global
route/orientation index. Guided intentionally retains a within-route authored
reading index. The historical exact-checkpoint record is preserved; this
successor note supplies the precise distinction.

## Focused verification completed before final sealing

- `node qa/interaction/apply-state-contract.spec.mjs`: one ordinary plus 144
  layered combinations pass; adversarial extra fields fail closed.
- `node qa/interaction/apply-cross-artifact-contract.spec.mjs`: ordinary,
  permission, human gate, capacity, no-script precedence, and Advanced parity
  pass across canonical artifacts.
- `PYTHONDONTWRITEBYTECODE=1 python3 qa/applied/validate_framework.py`: all six
  structural/procedural groups pass, including outcome and F2 receipt
  mutations.
- `node qa/site/public-mode-contract.spec.mjs`: shared-source public adapter,
  public-host gate, self-contained entrance, deduplicated examples, Stage 0,
  no-script precedence, F2 copy, and recurrence semantics pass.
- `cd site && npm run build && npm run check`: ten review routes, ten public
  routes, both standalones, 145 Apply states, Map/term geometry, no-script,
  hierarchy, links, contrast, and selector reachability pass.
- `PYTHONDONTWRITEBYTECODE=1 python3 qa/site/audit_site.py`: semantic and
  structural audit passes.
- `PYTHONDONTWRITEBYTECODE=1 python3 qa/editorial/validate_content_interface.py`:
  locked interface, six families, first-screen, claims, and manuscript-length
  checks pass.
- Research boundary validator and seven research-convergence unit tests pass.

## Live browser and visual evidence after correction

The rebuilt local site was inspected through the in-app Browser at 1440×720
and 390×844. All ten routed pages had exactly one `h1`, zero duplicate IDs,
and document scroll width equal to viewport width. The Examples defect was
therefore reproduced before the generator change and absent after it; this is
not inferred only from generated text.

The all-routes standalone was served over local HTTP and inspected at the same
wide and narrow widths. Sources, Research, and History are direct children of
`.page-content`; at 1440 pixels each measured x=249.59 and width=1174.41, and
at 390 pixels each measured x=10 and width=370. The page had zero duplicate
IDs and no document-level horizontal overflow. This directly rechecks the old
collapsed Sources/History failure rather than relying on the alternate stale
11-page browser export.

Current browser captures are in `qa/visual/final-redteam/`. They cover the
public first screen and teaching reveal, F2 at wide and narrow widths, the
common-origin relationship at wide and narrow widths, an actual Advanced/HOLD
Apply state at wide and narrow widths, and the standalone Sources and History
sections at wide width. Screenshots are visible layout evidence, not reader,
accessibility, or effectiveness results.

The secondary owner-review PDF was regenerated deterministically, rendered to
six page images with Poppler, and visually inspected. It is a clean letter-size
ReportLab companion; it is not the owner's earlier 79 MB, 11-page jsPDF/browser
export. The current PDF remains intentionally untagged, so semantic standalone
HTML is the portable accessibility route.

The package-wide image-signature verifier also found four earlier
`final-convergence/` captures whose bytes were JPEG but whose filenames ended
in `.png`. They were renamed byte-for-byte to `.jpg`, their active QA references
were updated, and no image content was regenerated or reinterpreted.

## Exact-`6a61f6d` recheck and final corrections

Three independent read-only lanes then rechecked exact clean checkpoint
`6a61f6da9b2c1f0255dd5d8a15e596c88b031f36`. Their reports are preserved at:

- `qa/editorial/advisory/FINAL_INTENT_READER_RECHECK_2026-08-30_6a61f6d.md`;
- `qa/site/advisory/FINAL_APPLIED_SITE_RECHECK_2026-08-30_6a61f6d.md`; and
- `qa/research/advisory/FINAL_RESEARCH_PROVENANCE_RECHECK_2026-08-30_6a61f6d.md`.

The intent lane passed without a P0/P1/P2 and supplied two wording corrections.
The applied/site lane reproduced one P1, two P2s, and one P3: Stage 0 copy had
to use the complete disqualifier set on every surface; public-host screening
needed positive IPv6 classification; the essay's capability sentence could not
silently redefine Advanced; and strict JS input records could not accept
hidden, symbol, accessor-shaped, or inherited fields. The research/provenance
lane found one P1: the PDF producer checkpoint was stale.

All were accepted with the revisions recorded in D-040. Exact commit
`06c61680f709861ccd3ffd2df5029e04c63cb450` owns the regenerated six-page PDF
(SHA-256 `0452239c80da4a34ad1a0fdbf8a9d50480684d078a92b8931ca0cf08a6595efc`,
18,371 bytes); its successor binds that producer without self-reference.
Page 5 was rendered with Poppler and inspected after the copy correction. The
table, boundary card, operator path, footer, and complete Stage 0 predicate fit
without clipping or overlap. Repeated generation produced the same hash.

The focused site suite passes 10 review routes, 10 public routes, both
standalones, one ordinary plus 144 layered plans, the hostile input cases, the
expanded release-host matrix, Map/term behavior, selector reachability, and
reader-language contracts. Applied, editorial, research, semantic-site, and
current image-signature validators also pass. These remain structural and
proxy findings; they do not close the manual gates below.

The final intent recheck also identified one non-blocking P3 adjacency: the
complete Stage 0 predicate repeated in consecutive Guided and Apply sections.
The routes retain the complete local rule once, the nested levels point back to
it, and Guided now uses an exact reversible reformat as its ordinary example.
No disqualifier, four-field terminal rule, or independent no-script meaning was
removed.

## Still open by design

The owner/mentor voice and comprehension judgment, physical keyboard and
screen-reader passes, real 200% zoom, real forced-colors, native print preview,
hardware touch, publication identity/URLs/image/link recheck, and any claim of
real-world usefulness remain outside automated approval. No model, provider,
participant, empirical study, deployment, publication, purchase, or outreach
was run or authorized by these corrections.
