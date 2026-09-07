# Wave 2 human-correction PDF evidence

Status: **exact-byte pre-integration visual evidence; not reader,
accessibility, publication, or research results**

## Source and artifact identity

- Starting Git checkpoint:
  `9916076c2fba4fb70fa125e70e8632f2b8046904`
- Exact PDF producer/integration checkpoint:
  `385af09679bac12d8ce807bda6c3d4ee3f143723`
- PDF generator: `site/scripts/generate_review_pdf.py`
- Generator SHA-256:
  `14f8e48b3eb88d307f8084615915b44662f15e1d866d09b810411df969aad076`
- Content-interface source: `docs/CONTENT_INTERFACE_V16.json`
- Content-interface SHA-256:
  `9b01c7adbe4656f16ff9c366d5bebf99b51032a0d3b56a73594ac730030df174`
- Generated PDF: `site/exports/pattern-map-v16-owner-review.pdf`
- PDF bytes: `18,373`
- PDF SHA-256:
  `372b7b5fd3ad9a8838eb832b5c44ea83593622138a44b6c16c15b1688a52f25d`
- Renderer: Poppler `pdftoppm 26.05.0`

The producer checkpoint above contains the exact generator, PDF, page-2 render,
site/copy correction, successor evidence record, and regenerated standalone
bytes. Later packaging/disposition commits may bind this checkpoint without
changing its PDF identity.

The predecessor exact-source record remains
`ULTRA_FINALIZATION_EVIDENCE_REFRESH_2026-08-30_2ba89e7.md`. It records PDF
SHA-256
`0452239c80da4a34ad1a0fdbf8a9d50480684d078a92b8931ca0cf08a6595efc`
and is preserved unchanged.

## Bounded correction

Page 2 now describes Guided as one **authored** 8-12-minute path rather than a
generated path. This aligns the PDF companion with the public and review site
language and avoids suggesting that the deterministic Guided composition is a
model-generated or personalized manuscript.

No other PDF source copy changed. Deterministic comparison confirmed pages 1
and 3-6 reproduce the predecessor renders byte-for-byte; only page 2 changed.

## Render method and exact outputs

The exact PDF was rendered at 144 DPI with:

```sh
pdftoppm -png -r 144 \
  site/exports/pattern-map-v16-owner-review.pdf \
  page
```

| Render | Bytes | SHA-256 |
| --- | ---: | --- |
| `pdf-renders-final-v16-polish/page-1.png` | 184,057 | `23ace092d3106681761702dedcfd103e3187c1878ce102871dde9e2e04daaefc` |
| `pdf-renders-final-v16-polish/page-2.png` | 245,077 | `1280271dbd6275d03aa6f751d5e9753a6e18debdc1dacce25ee38adf0bb28dde` |
| `pdf-renders-final-v16-polish/page-3.png` | 180,335 | `a8cf5eb40a67dfba78e42bf9530fa4fe837c9687d04946fa80bcce841be68830` |
| `pdf-renders-final-v16-polish/page-4.png` | 197,201 | `2c3dbcb0625fb848c1d718b2afa1d1705ba57e31d9753922bdf99ba2e6e0714a` |
| `pdf-renders-final-v16-polish/page-5.png` | 250,242 | `fe1f56661b8b99303c2355cb111b4f1469b4f67c89492944fb54beb91ef44814` |
| `pdf-renders-final-v16-polish/page-6.png` | 264,394 | `8fb0c560d4ac5ab9444cc80d1156adf300750dcdb5ea80ec566dca6018ca1b2e` |

All six `1224 x 1584` renders were inspected at original detail. No clipping,
overlap, black-square artifact, broken table, unreadable glyph, or off-page
content was observed. Page 2 retains its three-door row, complete Guided
description, claim-boundary bullets, checkpoint tag, footer, and page number
without reflow or crowding.

The reopened six-page PDF has no encryption, JavaScript, or form. Text
extraction succeeded on every page, and no extracted glyph box fell outside
the page media box.

## Evidence boundary

This record establishes deterministic local source/artifact identity and visual
render quality for the named bytes. It does not establish reader comprehension,
persuasion, accessibility conformance, semantic PDF navigation, behavioral
effectiveness, publication readiness, or research results. The PDF remains an
intentionally untagged visual companion; the standalone HTML remains the
semantic route. Physical keyboard, supported screen-reader, real zoom,
forced-colors, native print-preview, hardware-touch, owner/mentor, and
publication-time gates remain open.
