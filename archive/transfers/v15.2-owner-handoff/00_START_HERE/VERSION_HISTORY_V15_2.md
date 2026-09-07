# Pattern Map version history - v15.2 checkpoint

This table distinguishes sealed sources, generated review exports, and known
historical gaps. A generated manuscript page is not represented as an exact
reconstruction of a former site.

| Version | Source checkpoint | Canonical text/surface in this archive | Standalone HTML status | PDF status | Supersession state |
| --- | --- | --- | --- | --- | --- |
| v13 | Live historical reference; exact original HTML bytes unavailable | `05_HISTORY_AND_VISUALS/v13-anchor/live-v13-rendered-dom-snapshot.html`; byte-verified v12 diagram PNG | Rendered DOM recovery snapshot only; external dependencies may be missing; not labeled standalone | No sealed v13 PDF | Historical origin anchor only |
| v14 | `d0d26e28236e50d49e57bea9554e2a3a7b392198` | v14 Markdown and historical artifacts | `prior-standalone-html/v14.html`, generated from the sealed manuscript | `01_THOUGHT_PIECE_V14.pdf` in the PDF review ZIP | Superseded; retained for audit |
| v15 | `82f87b1d57414d4e7b1d2637a8fa53799d5ccf4d` | Sealed v15 manuscript recovered from Git history | `prior-standalone-html/v15.html`, generated from the sealed v15 commit | `02_THOUGHT_PIECE_V15.pdf` | Superseded; retained for audit |
| v15.1 | `22f232701184812489843731b6fe27592118eb29` | `THOUGHT_PIECE_V15_1.md` compatibility source and sealed handoff records | `prior-standalone-html/v15-1.html`, generated from the sealed compatibility manuscript | `03_PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf` | Direct baseline for v15.2; sealed and superseded |
| v15.2 | Release commit recorded in `00_START_HERE/PACKAGE_MANIFEST.json` | `01_FINAL_OUTPUT/` and `THOUGHT_PIECE_V15_2.md` | Four current route exports plus `prior-standalone-html/v15-2.html` manuscript rendering | `04_PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf` | Current local owner-review candidate |

The historical HTML manifest records source and output hashes for v14 through
v15.2. The package manifest records the SHA-256 and source path of every file
in the owner archive.

No version in this table is published by this checkpoint.
