# Pattern Map v16 owner visual/export closeout

Status: **source corrections implemented; no deployment or publication**

Reviewed branch: `codex/pattern-map-v16-foundation`

Starting checkpoint: `eca11399bc8ec156e16bf33a732168511b6873bf`

This record adjudicates the owner's attached PDF, the current routed and
standalone site, and the request for another Claude review. It is visual and
implementation QA. It is not reader testing, accessibility certification,
model-quality evidence, or a research result.

## Artifact identity

The attached file
`AI-slop-often-begins-before-the-model-writes-a-word-—-Pattern-Map-v16-08-23-2026_06_37_PM.pdf`
is not the repository's dedicated owner-review companion.

| Artifact | SHA-256 | Producer | Pages / size | Role |
| --- | --- | --- | --- | --- |
| Owner-attached browser-style export | `527ca8238df91eeb68865ae1d9ef776c823685c37e5d3090f3804301d005df76` | jsPDF 2.5.1 | 11 pages, each 3572 × 14400 pt; 83,215,636 bytes | Evidence of an unsafe alternate/full-page export path |
| Repository companion | `31f701ce11fc0b727eb958ec17c483ce6e4e2af8c6abb0ed3ff9c1851b7f655b` | ReportLab | 6 US-letter pages; 18,199 bytes | Deliberately composed secondary review companion |

All 11 attached pages and all six repository-companion pages were rendered and
inspected. The attached artifact has real visible failures: Sources and
Research collide on page 8; History collapses into a narrow left strip on pages
9–11; wide lineage/source tables become microtype; and the common-origin fan of
lines crosses and overshoots on page 6. A later standalone-DOM red team traced
the narrow-column failure to malformed generated HTML: an extra closing
`</div>` in the Boundaries route let later sections escape `.page-content`.
The dedicated six-page companion does not reproduce those failures.

## Browser-rendering boundary

The requested signed-in in-app Browser connection failed before tab attachment
with the app's trusted-runtime error for `browser-service.mjs`. The same failure
prevented direct reading or posting in the named Claude web thread. No claim is
made that the authenticated web conversation was read or answered.

After that supported path failed, an isolated Chromium renderer was used for
the local site only. This was real DOM rendering, interaction, responsive
layout, print-media emulation, and scrolling—not screenshot-only inference. It
did not inspect cookies, storage, credentials, or an authenticated web page.

The routed Sources, Research, History, Examples, and Map pages were scrolled at
1440 × 900. Sources, Research, and History were also scrolled at 390 × 844.
Those routed pages were healthy, but a separate standalone pass reproduced the
owner-visible collapse at 1440 and 821 px. After the generator repair, the
standalone `.page-frame` has exactly two children—the orientation rail and
`.page-content`—and Sources, Research, and History are all direct children of
the latter. Their widths are 1174.4 px at 1440, 621 px at 821, and 370 px at
390; document scroll width equals viewport width at all three sizes.

## Findings and dispositions

| ID | Finding | Disposition | Reason and implementation |
| --- | --- | --- | --- |
| OVE-01 | Sources/Research collision in the attached PDF | **Accepted** | Routed pages were healthy, but standalone screen rendering exposed a real structural defect. The stray Boundaries `</div>` is removed; standalone content extraction now uses explicit generator markers instead of a greedy closing-tag regex; and checks require balanced main markup plus every route inside `.page-content`. |
| OVE-02 | History collapse and unusable lineage/source tables | **Accepted** | The structural repair restores normal standalone screen width, while print media independently removes inherited width constraints, makes wrappers visible rather than horizontally scrollable, gives tables a fixed full-width print layout, and allows long anchors to wrap. In Chromium print media at 1056 px, Sources, Research, and History each measured 1056 px wide with no document overflow; representative tables measured 1019–1056 px and used `table-layout: fixed`. |
| OVE-03 | Nine rotated common-origin lines are visually misleading | **Accepted** | The legacy fan is no longer painted. The example now uses a flow-native three-part reading—nine observations, “trace known paths,” one known shared path—with the existing counts and `independence: UNKNOWN` boundary. At 1440 px the bridge is a normal 173 px grid region, all nine legacy lines compute to `display: none`, and the document width remains 1440 px. At 390 px the visual becomes one column and the redundant bridge hides. |
| OVE-04 | Complex term microvisuals may be cramped on small screens | **Accepted with revision** | At 480 px and below, chain/candidate/authority/learning/stop/origin microvisuals become one-column sequences and directional arrows rotate. At 390 px the inspected chain computed to one column and the document width remained 390 px. Plain-language meaning remains adjacent and canonical. |
| OVE-05 | A desktop term panel near the right edge may be clipped | **Accepted** | Optional panels now have a viewport-safe maximum width. On opening and resize, the enhancement calculates only the bounded horizontal shift needed at widths above 1100 px. The baseline panel at 1440 px shifted `-26px`, occupied x=927.48–1423.48, retained the 16 px viewport guard, and did not enlarge document width. Medium/narrow panels remain flow-native. |
| OVE-06 | Redesign the current site broadly because the attached export is broken | **Rejected** | Current screen routes, hierarchy, navigation, three doors, Guided path, line-free Map, and planning-only Apply are coherent and pass their contracts. The PDF mismatch does not justify replacing the authored publication with a simpler text/PDF surface or a new architecture. |
| OVE-07 | Generate bitmap diagrams or decorative imagery | **Rejected for this checkpoint** | The confirmed problems are geometry, responsive flow, and export containment. Semantic HTML/CSS is more inspectable, responsive, printable, and accessible. The visual-needs gate therefore remains closed and the generated-image ledger remains at zero. |
| OVE-08 | Regenerate the dedicated six-page PDF | **Rejected as unnecessary** | The dedicated companion is clean, unchanged, and intentionally separate from browser print. The source correction affects the interactive/standalone recurrence visual and browser-print resilience; it does not alter the ReportLab companion's composed content. |

## Claude review status

Two safe attempts were made without repairing or exposing credentials:

1. the web session identifier and exact title were offered to the local Claude
   Code resume command, but neither mapped to a resumable local session; and
2. a new read-only Opus/max Plan review was attempted with the current handoff,
   repository, and attached PDF, but Claude Code returned `401 OAuth access
   token has been revoked`.

No successful Claude review is claimed. No credential, cookie, token, provider
response, or paid API path was inspected or repaired. Independent Luna Max
audits remain advisory and are separately dispositioned before integration.

## Executable checks

After the source changes:

```text
npm run build
PASS built 10 routes and refreshed the standalone export

npm run check
PASS 10-route content/link/standalone/contrast contracts
PASS Apply Stage 0 and planning-state contract across 108 combinations
PASS line-free Map wide/medium/narrow contracts
PASS reader-language contract (249 words, all six families)
PASS stylesheet selector reachability

git diff --check
PASS
```

New source checks require the flow-native recurrence bridge, hidden legacy
traces, viewport-bounded term panels, narrow microvisual stacking, print route
page breaks, full-width evidence routes, the fixed table print contract,
balanced standalone main markup, and containment of all ten standalone routes
inside `.page-content`.

Post-repair Chromium standalone measurements:

```text
1440 px: Sources / Research / History x=249.6, width=1174.4
 821 px: Sources / Research / History x=184,   width=621
 390 px: Sources / Research / History x=10,    width=370
all: parent=.page-content; document scroll width=viewport width
print 1056 px: all three routes width=1056; break-before=page;
               representative tables width=1019–1056, table-layout=fixed
```

## Remaining honest gates

- Physical keyboard traversal and hardware touch.
- VoiceOver/NVDA or another supported screen reader.
- Real browser/OS 200% zoom and forced-colors mode.
- Native browser print-preview inspection in the owner's target browser.
- Owner/mentor visual taste and comprehension judgment.
- Publication-time external-link and metadata checks.

These residuals do not authorize deployment, publication, a merge to `main`, a
provider/model/research run, dataset acquisition, or spend.
