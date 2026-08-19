# Applied final regression check — `2a54b24`

**Review target:** exact integrated commit `2a54b24ec01707bb2a73032ab3f662cd995669ae`

**Comparison base:** `8aa5f949e9fffed0e4b8bc14c7f71887d3adb842`

**Scope:** narrow follow-up to the prior applied/rendered review. This check
verifies that the subsequent reader and accessibility changes did not regress
the A07/A08/A09 implementation surfaces, that prior `RESID-01` duplicate
standalone IDs are resolved, and that local fragments and semantic source
routes remain accurate. It does not re-litigate the canonical framework,
cases, or the prior acceptance evidence.

## Verdict

**Overall regression verdict: PASS.**

| Gate | Final regression verdict | Basis at the exact target |
| --- | --- | --- |
| A07 — concrete implementation paths | **PASS retained** | The regenerated Apply route still exposes the implementation surfaces and source-route wayfinding; `qa/applied/validate_framework.py` and all site/content validators pass. No `framework/agent-playbook/**`, implementation-choice, or `cases/**` source was changed in `8aa5f94..2a54b24`. |
| A08 — observable agent behavior | **PASS retained** | Apply, Examples, and standalone output preserve exact route/stop/learning/capture/status identifiers and the source records remain intact. The applied validator and rendered site checks pass. This is artifact/markup fidelity evidence, not evidence of live-agent behavior. |
| A09 — Signal Foundry bounded illustration | **PASS retained** | All 36 rendered mentions remain bounded by illustration/fixture/non-validation language; there are zero Signal Foundry-targeted anchors or `href` values. No implementation, permission, runtime, study, or effectiveness claim is inferred. |

**New regression findings:** none. No new finding ID is opened. The prior
`RESID-01` is verified closed below.

## Evidence boundary and exact-commit control

The audit ran in a detached temporary worktree at the exact target commit. It
used only repository files, generated local HTML, local validators, and static
parsing. No provider, model, participant, study, private/runtime data, external
dataset, browsing, deployment, publication, or live-compliance/effectiveness
activity was performed.

The owner-intent checkpoint passed without refresh:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

The target diff passed `git diff --check`. Its source changes relevant to this
follow-up are reader/accessibility and rendered-output changes; it does not
modify `framework/agent-playbook/**`, the implementation-choice source, or
`cases/**`. I did not edit, stage, revert, or include any pre-existing or
sibling-task worktree changes; the only file attributable to this follow-up is
this advisory report.

## Local validation and regenerated-output checks

All checks below passed at `2a54b24`:

```text
cd site && npm run build
Built 9 routes to site/dist
Built standalone export to site/exports/standalone/pattern-map-v16.html

cd site && npm run check
PASS routes: 9
PASS exact first-screen framing, non-result boundary, and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS external Markdown links preserve URLs and safe anchor attributes
PASS exact underscore-bearing state vocabulary and standalone fragments
PASS standalone heading hierarchy and unique IDs
PASS responsive/no-script navigation and active-route semantics
PASS normal-text and dual-focus contrast thresholds
PASS standalone export exists

python3 qa/site/audit_site.py
PASS all route semantic/accessibility checks
PASS standalone HTML is self-contained with one h1, unique IDs, and named route sections
PASS exact underscore-bearing state vocabulary and standalone fragment integrity

python3 qa/editorial/validate_content_interface.py
PASS immutable owner-intent checkpoint and content-interface JSON
PASS exact three-door, secondary-route, and source manifests
PASS locked six-family identity, questions, boundaries, and invariants
PASS human-problem first screen, examples, and late Echo placement
PASS claim, no-script, visual, output, and external-action obligations

python3 qa/applied/validate_framework.py
PASS six-family JSON and schema contract
PASS artifact inventory and boundary language
PASS receipt fixtures through preflight/stop logic
PASS focused applied QA complete (structural/procedural only)
```

The rebuilt standalone SHA-256 was
`4d9cf2bac4f60c1045517dfcffde30720dc52cb75d346235f4243119a1812e0d`, equal
to the `site/exports/standalone/pattern-map-v16.html` bytes stored in the
target commit. This confirms the audit used the integrated export, not a stale
build directory.

## Prior `RESID-01` duplicate-ID verification

`RESID-01` was the prior low-severity standalone semantic residue: route
concatenation left three duplicate non-route ID values in the `8aa5f94`
export. It was an A13-only residue and was explicitly not an A07, A08, or A09
failure.

**Prior finding ID:** `RESID-01`

**Prior severity:** Low / P3

**Gates:** A13 standalone semantic quality only; not A07, A08, or A09

**Current status:** Resolved at `2a54b24`

**Evidence:** The exact old-versus-current ID and heading counts below; current
fragment checks also return zero missing or duplicate targets.

**Bounded fix:** Route-scoped standalone ID normalization in
`site/build.mjs:678-708`, with duplicate-ID, one-`h1`, named-section, and
fragment assertions in `site/check.mjs` and `qa/site/audit_site.py`.

An exact old-versus-current parse found:

| Export | Total IDs | Unique IDs | Duplicate values | Level-one headings |
| --- | ---: | ---: | --- | ---: |
| `8aa5f94` | 281 | 276 | `short-pattern-recognition-the-discrimination-layer` ×2; `ordinary-ordinary-path-illustration` ×3; `ordinary-discrimination-layer-illustration` ×3 | 10 |
| `2a54b24` | 282 | 282 | none | 1 |

The current export also contains all nine named route sections (`home`,
`read`, `map`, `apply`, `examples`, `boundaries`, `sources`, `research`, and
`history`). The route-prefixing/normalization path is in
`site/build.mjs:678-708`; duplicate-ID and one-`h1` assertions are enforced by
`site/check.mjs:121-131` and `qa/site/audit_site.py:170-183`.

**RESID-01 status: Resolved at `2a54b24`.** The bounded fix is the route-scoped
standalone ID normalization plus the duplicate-ID regression assertions. No
canonical framework or case wording was changed to obtain this result.

## Same-document, local-fragment, and source-route audit

An independent parser checked all nine generated route documents and the
standalone export. It resolved **439 local anchor/target links**, including
**211 fragment-bearing links**. Missing target files and missing target IDs:
**0**. The standalone export has no `href="#source-..."` fragments, and every
standalone fragment resolves to an ID that occurs exactly once.

The current route-prefix behavior is intentional: standalone IDs retain the
route namespace, so the correct destinations now include `#apply-apply`,
`#sources-sources`, and `#research-echo` rather than the unscoped fragments
used by the prior export.

| Source/reference checked | Multi-page rendered destination | Standalone rendered destination | Semantic result |
| --- | --- | --- | --- |
| `framework/templates/OUTCOME_REVIEW.md` | `../apply/index.html` from the Apply route | `#apply-apply` | Apply route; target exists and is unique |
| `docs/OWNER_INTENT_V16.md` and `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md` | `../sources/index.html` from the Sources route | `#sources-sources` | Sources route; target exists and is unique |
| Echo `RELATION_TO_V16.md`, `STATUS_AND_BOUNDARIES.md`, `PRESERVED_V15_2_INDEX.md`, `FUTURE_EXECUTION_PLAN.md`, and `qa/EP_V0_1_QA.md` | `../research/index.html#echo` | `#research-echo` | Separate Echo research section, with status/relation kept subordinate to v16 |
| Echo `VERSION_HISTORY.md` and immutable v15.2 accession | `../history/index.html` | `#history` from the Research section | Lineage/history wayfinding, not the Echo status section |
| v13 recovery/intent material and historical references | `../history/index.html` | `#history` from the Sources section | Historical route; current-topology distinction remains visible |
| Research agenda and future-study specification | `../research/index.html` | `#research-research` where the route-local section is the target | Research planning route; no study/result claim is created |

The explicit source mapping and fail-on-unmapped-link behavior remain in
`site/build.mjs:63-125`; route-local fragment checks remain in
`site/check.mjs:146-153`. The rendered links are wayfinding pointers to local
owner-review surfaces, not fresh external-source verification.

## Exact rendered vocabulary regression check

The prior applied audit's canonical vocabulary set remains contiguous in the
current output. On the exact regenerated HTML:

- Apply contains all 9 route values (`ACQUIRE`, `COMPARE`, `CLARIFY`,
  `ANSWER`, `ANSWER_PROVISIONALLY`, `HOLD`, `DEFER`, `ESCALATE`, `REFUSE`),
  all 5 stop values (`CONTINUE`, `COMPLETE`, `STOPPED_BUDGET`,
  `STOPPED_DEADLINE`, `STOPPED_OTHER`), all 4 learning values, all 10 audited
  capture/failure values, and all 9 audited uncertainty values.
- Examples preserves the route values used by its bounded procedure,
  `FAILED_CAPTURE`, and the exact machine-readable Signal Foundry status
  `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`; it does not introduce
  fabricated stop/learning fields into that case surface.
- History preserves the exact historical status
  `HISTORICAL ORIGIN / PARTIAL RECOVERY / NOT CURRENT TOPOLOGY` and does not
  mutate it into an applied route/stop/learning status.
- Standalone contains the complete combined vocabulary and historical status.
  None of its two intended plain-word `<em>` elements contains an underscore;
  no underscore-bearing identifier is split by emphasis.

This is rendered-token fidelity only. It is not a test of whether a live agent
will follow, emit, or correctly interpret the vocabulary.

## Signal Foundry mention and cross-link inspection

Every rendered `Signal Foundry` occurrence was searched case-insensitively in
all nine route files and the standalone export. Counts were 18 mentions across
`site/dist/**` and 18 in standalone. The distribution is: home 1, Read 1,
Examples 11, Boundaries 2, Sources 2, Research 1, and none in Map, Apply, or
History; standalone contains the concatenated route set. All mentions are
plain text in bounded context; **zero** anchor labels and **zero** `href`
values contain `Signal Foundry` or `signal-foundry`.

The exact rendered checks confirm that:

- Home says “bounded Signal Foundry illustration.”
- Read says a bounded design illustration cannot validate the framework.
- Examples retains the human-readable
  `ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION` header and the exact body
  status `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION`, along with
  fixture-only, no-runtime, no-provider/private-data, illustrative
  cost/stop, and no-permission language.
- Boundaries, Sources, and Research retain their respective “bounded
  illustration, not validation,” `ILLUSTRATIVE_CASE`, and no-product-
  implementation/validation boundaries.
- Standalone preserves the same embedded case and boundaries; no new direct
  case link can detach a mention from its bounded Examples context.

The two neutral cases remain separate from Signal Foundry in the Examples
surface. These are fixture/markup boundary checks only; they establish neither
Signal Foundry runtime behavior nor framework/product effectiveness.

## Final disposition

`2a54b24` introduces no regression to the prior A07/A08/A09 PASS. The prior
`RESID-01` duplicate standalone IDs are resolved, local fragments remain
complete, semantic source routing remains accurate, exact state/status labels
remain intact, and Signal Foundry remains a bounded fixture-only illustration.

This report records implementation and rendered-output QA only. It does not
claim live compliance, reader comprehension, agent behavior, product
behavior, or effectiveness.
