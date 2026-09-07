# Owner-reported principal-door correction

Date: 2026-08-30

Starting checkpoint: `adbaae39701861987871dedcdaccf835063884ce`

Surface: locally served public-preview Home route

Status: source correction implemented; deterministic and live-browser recheck passed

## Why this correction exists

During direct review in the in-app Browser, the owner marked the lower portion
of the three principal door cards as buggy. Reproducing the exact live layout
confirmed a real defect that the earlier route, overflow, and content contracts
did not measure.

At 1440 pixels:

- the Read and Map previews began at `y=874.92`, while the taller Apply preview
  began at `y=848.88`—a `26.04px` footer-start mismatch;
- each preview caption overlapped its arrow horizontally by `16.81px` and
  vertically by `8.91–10.50px`;
- the map preview used two detached diagonal traces behind six nodes, making a
  simple relationship preview look visually broken;
- only `13.59px` separated the card row from the conceptual bridge below it.

The same caption/arrow collision reproduced at 390 pixels. This was not a
local-server or export-only artifact.

## Accepted correction

The principal cards now:

- use four explicit grid rows with one shared `4.35rem` preview/footer track;
- stretch that track instead of using `align-content: space-between` to hide
  unequal preview heights;
- reserve a `2.45rem` arrow lane so captions and arrows cannot occupy the same
  horizontal space;
- keep the Apply caption in normal grid flow below its planning rows;
- replace the Map preview's detached diagonal traces with short connectors that
  live in the actual gaps between adjacent F1–F6 nodes; and
- give the transition into the conceptual bridge a clearer block gap.

## Recheck evidence

After rebuilding both presentation modes, live computed geometry showed:

- `0px` preview-start spread across all three cards at 1440 pixels;
- `0px` caption/arrow horizontal overlap for every card at 1440 and 390 pixels;
- a `21.59px` card-row-to-bridge gap at 1440 pixels;
- document scroll width equal to viewport width at 1440, 390, and 320 pixels;
- at 320 pixels, each caption retains an `18.38px` horizontal gap before its
  arrow and every card's scroll width equals its client width.

`qa/site/door-card-preview-contract.spec.mjs` preserves the shared footer,
reserved arrow lane, in-flow Apply caption, flow-native Map connectors, and
three-card/three-preview structure. It is part of `npm run check`.

An independent read-only agent rechecked the complete diff, source/built CSS
byte parity, both generated Home routes, the focused contract, and the full
site suite. Disposition: **Accepted**—no P0, P1, or P2 finding. Its P3 note that
the source contract is declarative rather than a rendering engine is accepted
as a scope boundary, not treated as visual certification; the live geometry
and manual residuals remain necessary.

## Evidence boundary

This is local source, generated-output, DOM, and computed-geometry evidence. It
does not replace the remaining physical keyboard, supported screen-reader,
real zoom, forced-colors, native print-preview, hardware-touch, owner/mentor
comprehension, or publication-time checks. No deployment or publication
occurred.
