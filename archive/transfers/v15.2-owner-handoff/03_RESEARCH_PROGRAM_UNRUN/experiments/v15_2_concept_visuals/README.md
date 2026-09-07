# v15.2 concept visuals: accessible term-popover candidates

This is a lane-owned prototype lab for Pattern Map v15.2. It contains four
standalone HTML files that test the smallest useful visual explanation for
terms that interrupt a non-specialist reader. Each file is intentionally
boring in the best way: semantic HTML carries the meaning, CSS supplies the
shape, and no image, font, JavaScript, package, or network request is needed.

## Open and review

Open any file directly in a browser. The files are design candidates only;
they are not wired into the v15.1 site and no production/canonical file was
changed by this lab.

Suggested order:

1. `01-origin-vs-report-count.html` — nine report observations versus one
   known common origin, with two illustrative comparison roots.
2. `02-f0-f1-f2.html` — three plain-language versions of one planned task;
   only the intentional difference changes across the cards.
3. `03-provenance-unknown-hold.html` — provenance trace separated from claim
   support, with UNKNOWN preserved and a consequential human HOLD.
4. `04-sample-size-negative-result.html` — 300 planned fictional bundles and
   four predeclared ways the result can be null, rule-only, harmful, or
   shortcut-driven.

The files are not browser-QA evidence. Before integration, run the target
site's normal responsive, keyboard, screen-reader, reduced-motion, print, and
contrast checks against the chosen implementation.

## Design decision

The shortlist deliberately excludes a decorative “framework map” and a
diagram for `system runtime`. The former repeats the existing Explore map and
the latter needs only a sentence. These four visuals each answer a question a
reader can otherwise misread:

| Candidate | Question it answers | Keep / change / delete | Integration rank |
| --- | --- | --- | ---: |
| Origin count | Are nine observations nine roots? | **Keep, adapt** to the receipt or first glossary occurrence | 1 |
| F0/F1/F2 | What changed between the planned conditions? | **Keep, adapt** to the Lab term explanation | 2 |
| Provenance + UNKNOWN + HOLD | Does a trace prove a claim, and what happens when relation is unresolved? | **Keep, adapt** to the receipt / provenance-audit term | 3 |
| Sample + negative result | Is `N=300` a result, and what happens if the test disappoints? | **Keep only in Lab**; sentence-first fallback if space is tight | 4 |

## Shared accessibility intent

- Every visual has a heading, a prose lead, and a text-equivalent caption or
  summary before the visual details.
- Ordered lists, definition lists, `figure`/`figcaption`, and `aside` carry
  relationships; connector lines, dots, color, and borders are supplemental.
- Status is written as words (`DEPENDENT`, `UNKNOWN`, `HOLD`, `NULL`, and so
  on), not only encoded by color.
- The layout collapses to one column at narrow widths, and each prototype
  remains readable when color, hover, or generated imagery is unavailable.
- There is no motion to suppress. A production popover should still honor the
  site's `prefers-reduced-motion` contract and must not rely on hover.
- Print CSS removes the decorative connector treatment while preserving the
  labels and summaries. A production integration should verify actual print
  output on the target browser.

## Integration guardrails

Treat these as visual content inside an existing semantic term explanation,
not as replacement UI chrome. The production `Term` interaction currently
returns focus on Escape/Close but does not move focus into a dialog, trap focus,
or provide a no-JavaScript expanded fallback. If a candidate is integrated,
retain a visible plain-language definition in the surrounding prose and add a
real keyboard/screen-reader check for the final popover behavior.

Image provenance: this lab intentionally uses no bitmap. The v15.1 selected
worked-example raster and historical v13 anchor remain separately classified
in `assets/imagegen/IMAGE_SELECTION_LEDGER.md`; neither is required to
interpret these microvisuals.

