# Ultra-finalization visual-evidence refresh

Status: **exact-source owner-review evidence; not reader, accessibility, or
research results**

## Scope and source binding

- Site/PDF source checkpoint: `2ba89e7958cf01c5f0d44bad2bde8eadcb4df6a4`
- Branch at capture time: `codex/pattern-map-v16-ultra-finalization`
- Public site source: the local generated public build served only at
  `http://127.0.0.1:4174/`
- Browser: Google Chrome `151.0.7922.174`, headless, with background networking
  disabled
- PDF source:
  `site/exports/pattern-map-v16-owner-review.pdf`
- PDF SHA-256:
  `0452239c80da4a34ad1a0fdbf8a9d50480684d078a92b8931ca0cf08a6595efc`
- PDF renderer: Poppler `pdftoppm 26.05.0`

The evidence files are committed after their source checkpoint, so the source
binding names the exact pre-evidence commit rather than claiming a
self-referential final commit. Subsequent ultra-finalization corrections are
confined to the applied outcome/uncertainty contract and unpublished
publication-copy rehearsal. They do not change the captured Home implementation
or the PDF bytes, which remain those of the named checkpoint.

## Corrected principal-door captures

The previous `final-redteam/public-home-reveal-1440x720.jpg` remains historical
evidence for the pre-correction door condition. It must not be used to judge
the corrected principal-door previews.

Current captures:

| Capture | Bytes | SHA-256 | What was inspected |
| --- | ---: | --- | --- |
| `ultra-finalization/public-home-doors-1440x720.jpg` | 135,396 | `2b761536091fe438155d6f70dc2c65150334e9df7bf0f804d452e6debe85c658` | All three desktop doors, aligned preview starts, adjacent Map connectors, reserved captions, and arrow lanes |
| `ultra-finalization/public-home-map-door-390x844.jpg` | 73,005 | `188131ce8abe37cef10a5850a0f9438d6a595bce9b4a7d6876a3985cc4c811bb` | Narrow Map and Apply door composition plus their transition into the bridge |
| `ultra-finalization/public-home-apply-door-390x844.jpg` | 84,038 | `41a4889dbbc0a754768fc41938987cba72d659c0f81f90544744d33c40598743` | Narrow Apply preview, caption, arrow lane, bridge, and following progressive-disclosure links |

The screenshot run used Chrome DevTools Protocol device-metric overrides at
`1440 × 720` and `390 × 844`, navigated only to the local public Home route,
and captured JPEG at quality 92 after moving the named door into view. Direct
visual inspection found no detached Map traces, caption/arrow collision,
clipping, unreadable glyphs, or horizontal overflow in the captured regions.

Computed geometry from the same source checkpoint reported:

- at 1440 pixels, identical preview top positions across all three doors,
  `0px` caption/arrow overlap, and `22.36px` caption/arrow gaps; and
- at 390 pixels, `0px` caption/arrow overlap and `18.36px` caption/arrow gaps
  for all three doors.

These values agree with the broader ten-route, ten-width headless audit. They
are DOM/computed-style proxies, not physical-keyboard, real-zoom,
screen-reader, forced-colors, native-print, or hardware-touch evidence.

## Exact-current PDF renders

The exact PDF was rendered with:

```sh
pdftoppm -png -r 144 \
  site/exports/pattern-map-v16-owner-review.pdf \
  page
```

All six `1224 × 1584` page images were visually inspected at original detail.
No clipping, overlap, black-square artifact, broken table, unreadable glyph,
or off-page content was observed. Pages 1–4 and 6 reproduce the retained
renders byte-for-byte; page 5 is refreshed because the current PDF contains
the complete Stage 0 predicate and current ordinary-route wording.

| Render | Bytes | SHA-256 |
| --- | ---: | --- |
| `pdf-renders-final-v16-polish/page-1.png` | 184,057 | `23ace092d3106681761702dedcfd103e3187c1878ce102871dde9e2e04daaefc` |
| `pdf-renders-final-v16-polish/page-2.png` | 245,176 | `7aeecb15a0184eeeafa347ea063a07a02899a34272be25f84e436f76d4b88057` |
| `pdf-renders-final-v16-polish/page-3.png` | 180,335 | `a8cf5eb40a67dfba78e42bf9530fa4fe837c9687d04946fa80bcce841be68830` |
| `pdf-renders-final-v16-polish/page-4.png` | 197,201 | `2c3dbcb0625fb848c1d718b2afa1d1705ba57e31d9753922bdf99ba2e6e0714a` |
| `pdf-renders-final-v16-polish/page-5.png` | 250,242 | `fe1f56661b8b99303c2355cb111b4f1469b4f67c89492944fb54beb91ef44814` |
| `pdf-renders-final-v16-polish/page-6.png` | 264,394 | `8fb0c560d4ac5ab9444cc80d1156adf300750dcdb5ea80ec566dca6018ca1b2e` |

The PDF remains an intentionally untagged secondary visual companion. Semantic
headings, landmarks, links, and assistive-technology navigation belong to the
standalone HTML; this render pass does not close those manual accessibility
gates.

## Controlled disposition

| Finding | Disposition | Reason | Affected files | Governing requirement |
| --- | --- | --- | --- | --- |
| The visual index called a pre-door-correction Home capture current | **Accepted with revision** | A reviewer could otherwise encounter the exact defect that the current site fixed | New `ultra-finalization/` captures and `qa/visual/README.md` | A06, A13, source/evidence lineage |
| The retained page-5 image differed from the current PDF while the matrix called all six renders current | **Accepted with revision** | Exact-current render provenance is required for the visual acceptance claim | `pdf-renders-final-v16-polish/page-5.png`, this record, and `qa/visual/README.md` | A13, binary-artifact policy, source/evidence lineage |
| Reopen the three-door architecture or redesign the PDF | **Rejected** | Exact-current site/PDF inspection reproduced no corresponding implementation defect | None | Owner intent, A04, A06, anti-churn rule |

## Evidence boundary

This refresh establishes only exact-source local render evidence within the
named viewports and PDF pages. It does not establish reader comprehension,
persuasion, accessibility conformance, behavioral effectiveness, model
quality, publication readiness, or research results. No deployment,
publication, external browser navigation, or provider-backed run occurred.
