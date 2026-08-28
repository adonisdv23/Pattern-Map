#!/usr/bin/env python3
"""Build self-contained manuscript HTML snapshots for v14 through v15.2.

The current interactive reader is exported separately. These snapshots exist
to make editorial comparison possible without a development server or a
Markdown application. They intentionally render the versioned manuscripts,
not an invented reconstruction of each historical website.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "v15_2" / "history-html"
GENERATED_ON = "2026-08-19"
SEALED_V15_COMMIT = "82f87b1"


@dataclass(frozen=True)
class VersionSource:
    slug: str
    label: str
    source_description: str
    text: str


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_source(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def git_source(commit: str, relative: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{relative}"], cwd=ROOT, text=True
    )


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def inline_markdown(value: str) -> str:
    """Render the small CommonMark subset used by the manuscripts."""

    code_values: list[str] = []

    def protect_code(match: re.Match[str]) -> str:
        code_values.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{len(code_values) - 1}\x00"

    value = re.sub(r"`([^`]+)`", protect_code, value)
    value = html.escape(value, quote=False)

    # External links remain live. Repository-relative references are rendered
    # visibly as package paths so each snapshot remains honest and standalone.
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def render_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        if target.startswith(("https://", "http://", "mailto:")):
            safe_target = html.escape(target, quote=True)
            return (
                f'<a href="{safe_target}" rel="noreferrer">{label}</a>'
            )
        return (
            f'<span class="local-ref">{label} '
            f'<code>{html.escape(target)}</code></span>'
        )

    value = link_pattern.sub(render_link, value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", value)
    value = re.sub(r"(?<!_)_([^_\n]+)_(?!_)", r"<em>\1</em>", value)

    for index, rendered in enumerate(code_values):
        value = value.replace(f"\x00CODE{index}\x00", rendered)
    return value


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def markdown_to_html(markdown: str) -> tuple[str, list[tuple[int, str, str]]]:
    lines = markdown.replace("\r\n", "\n").split("\n")
    output: list[str] = []
    headings: list[tuple[int, str, str]] = []
    used_ids: dict[str, int] = {}
    index = 0

    if lines and lines[0].strip() == "---":
        end = next(
            (position for position in range(1, len(lines)) if lines[position].strip() == "---"),
            None,
        )
        if end is not None:
            metadata = "\n".join(lines[1:end]).strip()
            output.append(
                '<details class="frontmatter"><summary>Version metadata</summary>'
                f"<pre>{html.escape(metadata)}</pre></details>"
            )
            index = end + 1

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            language = stripped[3:].strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            language_attr = (
                f' data-language="{html.escape(language, quote=True)}"'
                if language
                else ""
            )
            output.append(
                f"<pre{language_attr}><code>{html.escape(chr(10).join(code))}</code></pre>"
            )
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            level = len(heading_match.group(1))
            label = re.sub(r"[*_`]", "", heading_match.group(2)).strip()
            base_id = slugify(label)
            occurrence = used_ids.get(base_id, 0)
            used_ids[base_id] = occurrence + 1
            anchor = base_id if occurrence == 0 else f"{base_id}-{occurrence + 1}"
            headings.append((level, label, anchor))
            output.append(
                f'<h{level} id="{anchor}">{inline_markdown(heading_match.group(2))}</h{level}>'
            )
            index += 1
            continue

        if re.fullmatch(r"(?:-{3,}|\*{3,}|_{3,})", stripped):
            output.append("<hr>")
            index += 1
            continue

        if (
            "|" in line
            and index + 1 < len(lines)
            and is_table_separator(lines[index + 1])
        ):
            header_cells = split_table_row(line)
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append(split_table_row(lines[index]))
                index += 1
            output.append('<div class="table-wrap"><table><thead><tr>')
            output.extend(f"<th>{inline_markdown(cell)}</th>" for cell in header_cells)
            output.append("</tr></thead><tbody>")
            for row in rows:
                normalized = row + [""] * (len(header_cells) - len(row))
                output.append("<tr>")
                output.extend(
                    f"<td>{inline_markdown(cell)}</td>"
                    for cell in normalized[: len(header_cells)]
                )
                output.append("</tr>")
            output.append("</tbody></table></div>")
            continue

        if stripped.startswith(">"):
            quoted: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quoted.append(re.sub(r"^\s*>\s?", "", lines[index]))
                index += 1
            output.append(
                f"<blockquote><p>{inline_markdown(' '.join(quoted))}</p></blockquote>"
            )
            continue

        list_match = re.match(r"^\s*([-+*]|\d+[.)])\s+(.+)$", line)
        if list_match:
            ordered = bool(re.match(r"\d", list_match.group(1)))
            tag = "ol" if ordered else "ul"
            items: list[str] = []
            while index < len(lines):
                current = re.match(r"^\s*([-+*]|\d+[.)])\s+(.+)$", lines[index])
                if not current or bool(re.match(r"\d", current.group(1))) != ordered:
                    break
                item = current.group(2).strip()
                index += 1
                continuation: list[str] = []
                while (
                    index < len(lines)
                    and lines[index].strip()
                    and not re.match(r"^\s*([-+*]|\d+[.)])\s+", lines[index])
                    and not re.match(r"^(#{1,6})\s+", lines[index])
                ):
                    continuation.append(lines[index].strip())
                    index += 1
                if continuation:
                    item += " " + " ".join(continuation)
                items.append(item)
            output.append(f"<{tag}>")
            output.extend(f"<li>{inline_markdown(item)}</li>" for item in items)
            output.append(f"</{tag}>")
            continue

        paragraph = [stripped]
        index += 1
        while index < len(lines) and lines[index].strip():
            candidate = lines[index]
            if (
                candidate.strip().startswith(("```", ">"))
                or re.match(r"^(#{1,6})\s+", candidate)
                or re.match(r"^\s*([-+*]|\d+[.)])\s+", candidate)
                or re.fullmatch(r"(?:-{3,}|\*{3,}|_{3,})", candidate.strip())
                or (
                    "|" in candidate
                    and index + 1 < len(lines)
                    and is_table_separator(lines[index + 1])
                )
            ):
                break
            paragraph.append(candidate.strip())
            index += 1
        output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")

    return "\n".join(output), headings


def page_html(version: VersionSource) -> str:
    article, headings = markdown_to_html(version.text)
    toc_items = [
        f'<li class="level-{level}"><a href="#{anchor}">{html.escape(label)}</a></li>'
        for level, label, anchor in headings
        if level <= 3
    ]
    nav = " · ".join(
        f'<a href="{slug}.html" aria-current="page">{label}</a>'
        if slug == version.slug
        else f'<a href="{slug}.html">{label}</a>'
        for slug, label in (
            ("v14", "v14"),
            ("v15", "v15"),
            ("v15-1", "v15.1"),
            ("v15-2", "v15.2"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>Pattern Recognition — {html.escape(version.label)} manuscript snapshot</title>
<style>
:root {{ color-scheme: light dark; --paper:#f4f0e6; --ink:#211f1a; --muted:#655f54; --line:#c8c0af; --teal:#0d6668; --panel:#fbf8f0; --code:#e8e1d4; }}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{ margin:0; background:var(--paper); color:var(--ink); font:18px/1.68 Georgia, 'Times New Roman', serif; }}
a {{ color:var(--teal); text-underline-offset:.15em; }}
a:focus-visible, summary:focus-visible {{ outline:3px solid #c65332; outline-offset:3px; }}
.release {{ border-bottom:1px solid var(--line); background:color-mix(in srgb, var(--paper) 92%, var(--teal)); font:700 12px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing:.09em; text-transform:uppercase; }}
.release-inner {{ width:min(1120px, calc(100% - 32px)); margin:auto; padding:14px 0; display:flex; flex-wrap:wrap; gap:10px 22px; justify-content:space-between; }}
.version-nav {{ word-spacing:.25em; }}
.version-nav [aria-current="page"] {{ color:var(--ink); text-decoration-thickness:3px; }}
.boundary {{ width:min(1120px, calc(100% - 32px)); margin:24px auto 0; padding:16px 18px; border-left:5px solid var(--teal); background:var(--panel); font:14px/1.55 ui-sans-serif, system-ui, sans-serif; }}
.layout {{ width:min(1120px, calc(100% - 32px)); margin:32px auto 96px; display:grid; grid-template-columns:minmax(0, 760px) minmax(220px, 1fr); gap:64px; align-items:start; }}
main {{ min-width:0; }}
aside {{ position:sticky; top:20px; max-height:calc(100vh - 40px); overflow:auto; padding:18px; border:1px solid var(--line); background:var(--panel); font:13px/1.45 ui-sans-serif, system-ui, sans-serif; }}
aside h2 {{ margin-top:0; font:700 12px/1.2 ui-monospace, monospace; letter-spacing:.12em; text-transform:uppercase; }}
aside ul {{ margin:0; padding-left:18px; }} aside .level-3 {{ margin-left:12px; }}
h1,h2,h3,h4 {{ line-height:1.08; text-wrap:balance; scroll-margin-top:24px; }}
h1 {{ margin:.4em 0 .5em; font-size:clamp(2.4rem, 7vw, 5.6rem); letter-spacing:-.045em; }}
h2 {{ margin:2.15em 0 .65em; font-size:clamp(1.75rem, 4vw, 3rem); border-top:1px solid var(--line); padding-top:.65em; }}
h3 {{ margin:1.8em 0 .5em; font-size:1.5rem; }}
h4 {{ margin:1.5em 0 .4em; font:700 1.05rem/1.3 ui-sans-serif, system-ui, sans-serif; }}
p,li {{ max-width:72ch; }}
blockquote {{ margin:1.5em 0; padding:.15em 0 .15em 1.25em; border-left:6px solid #b74b35; font-size:1.25em; }}
code,pre {{ font-family:ui-monospace, SFMono-Regular, Menlo, monospace; }}
code {{ padding:.08em .28em; background:var(--code); border-radius:3px; font-size:.84em; }}
pre {{ overflow:auto; padding:18px; background:#1f211f; color:#f5f2e9; font-size:.78em; line-height:1.55; }}
pre code {{ padding:0; background:transparent; color:inherit; }}
.frontmatter {{ margin:0 0 2em; border:1px solid var(--line); background:var(--panel); font:14px/1.5 ui-sans-serif, system-ui, sans-serif; }}
.frontmatter summary {{ cursor:pointer; padding:12px 16px; font-weight:700; }}
.frontmatter pre {{ margin:0; border-radius:0; }}
.local-ref {{ text-decoration:underline dotted; text-underline-offset:.15em; }}
.table-wrap {{ overflow-x:auto; margin:1.5em 0; }}
table {{ width:100%; border-collapse:collapse; font:15px/1.45 ui-sans-serif, system-ui, sans-serif; }}
th,td {{ padding:10px 12px; border:1px solid var(--line); text-align:left; vertical-align:top; }}
th {{ background:var(--panel); }}
hr {{ margin:3rem 0; border:0; border-top:4px solid var(--ink); }}
.source-note {{ margin-top:4rem; padding-top:1rem; border-top:1px solid var(--line); color:var(--muted); font:13px/1.5 ui-sans-serif, system-ui, sans-serif; }}
@media (max-width:850px) {{ .layout {{ grid-template-columns:1fr; }} aside {{ position:static; max-height:none; order:-1; }} body {{ font-size:17px; }} }}
@media (prefers-color-scheme:dark) {{ :root {{ --paper:#171713; --ink:#f0ecdf; --muted:#bdb5a6; --line:#4b493f; --teal:#6fc2c0; --panel:#22221d; --code:#35332b; }} }}
@media print {{ :root {{ --paper:#fff; --ink:#000; --muted:#444; --line:#999; --teal:#004d4d; --panel:#fff; --code:#eee; }} .release, aside {{ display:none; }} .boundary,.layout {{ width:auto; margin-left:0; margin-right:0; }} .layout {{ display:block; }} a {{ color:inherit; }} h2 {{ break-before:page; }} table,blockquote,pre {{ break-inside:avoid; }} }}
</style>
</head>
<body>
<header class="release"><div class="release-inner"><span>Pattern Recognition · historical manuscript reader</span><nav class="version-nav" aria-label="Version snapshots">{nav}</nav></div></header>
<div class="boundary"><strong>{html.escape(version.label)} manuscript snapshot.</strong> This is a self-contained editorial comparison page, not a reconstruction of the historical site. It reports no empirical result. Current canonical release: v15.2. Source: {html.escape(version.source_description)}.</div>
<div class="layout">
<main id="main">{article}<p class="source-note">Generated {GENERATED_ON}. Inline CSS; no JavaScript, fonts, images, or local runtime dependencies. Repository-relative links are displayed as paths rather than presented as live standalone links.</p></main>
<aside aria-label="On this page"><h2>On this page</h2><ul>{''.join(toc_items)}</ul></aside>
</div>
</body>
</html>
"""


def index_html(versions: list[VersionSource]) -> str:
    cards = "".join(
        f'<li><a href="{version.slug}.html"><strong>{html.escape(version.label)}</strong>'
        f'<span>{html.escape(version.source_description)}</span></a></li>'
        for version in versions
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Pattern Recognition — historical standalone HTML</title><style>
:root{{color-scheme:light dark;--bg:#f4f0e6;--ink:#211f1a;--panel:#fbf8f0;--line:#c8c0af;--teal:#0d6668}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:18px/1.6 Georgia,serif}}main{{width:min(900px,calc(100% - 32px));margin:7vh auto 12vh}}h1{{font-size:clamp(2.5rem,8vw,5.5rem);line-height:.98;letter-spacing:-.045em}}p{{max-width:65ch}}ul{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:3rem 0}}li a{{display:block;height:100%;padding:22px;border:1px solid var(--line);background:var(--panel);color:inherit;text-decoration:none}}li a:hover,li a:focus-visible{{border-color:var(--teal);outline:3px solid var(--teal);outline-offset:2px}}li strong{{display:block;font:700 1.5rem/1.2 ui-sans-serif,system-ui,sans-serif;color:var(--teal)}}li span{{display:block;margin-top:.65rem;font:14px/1.5 ui-sans-serif,system-ui,sans-serif}}code{{font-size:.85em}}@media(prefers-color-scheme:dark){{:root{{--bg:#171713;--ink:#f0ecdf;--panel:#22221d;--line:#4b493f;--teal:#6fc2c0}}}}</style></head><body><main><p>Pattern Recognition / The Discrimination Layer</p><h1>Standalone manuscript history</h1><p>Open any version directly. Each page contains its manuscript and styles in one HTML file; no server, JavaScript, font, image, or local stylesheet is required. These are editorial manuscript renderings, not reconstructions of each historical site.</p><ul>{cards}</ul><p><strong>Current final interactive reader:</strong> <code>../standalone/index.html</code>. <strong>Historical v13 rendered snapshot:</strong> packaged separately under <code>05_HISTORY_AND_VISUALS/v13-anchor/</code>.</p><p>Status: local owner review · no empirical results · not published.</p></main></body></html>"""


def main() -> None:
    versions = [
        VersionSource(
            "v14",
            "v14",
            "source/THOUGHT_PIECE_V14.md in the v15.2 release tree",
            current_source("source/THOUGHT_PIECE_V14.md"),
        ),
        VersionSource(
            "v15",
            "v15",
            f"sealed commit {SEALED_V15_COMMIT}:source/THOUGHT_PIECE_V15.md",
            git_source(SEALED_V15_COMMIT, "source/THOUGHT_PIECE_V15.md"),
        ),
        VersionSource(
            "v15-1",
            "v15.1",
            "source/THOUGHT_PIECE_V15.md in the v15.2 release tree",
            current_source("source/THOUGHT_PIECE_V15.md"),
        ),
        VersionSource(
            "v15-2",
            "v15.2",
            "source/THOUGHT_PIECE_V15_2.md in the v15.2 release tree",
            current_source("source/THOUGHT_PIECE_V15_2.md"),
        ),
    ]

    OUTPUT.mkdir(parents=True, exist_ok=True)
    output_records: list[dict[str, str | int]] = []
    for version in versions:
        rendered = page_html(version).encode("utf-8")
        destination = OUTPUT / f"{version.slug}.html"
        destination.write_bytes(rendered)
        output_records.append({
            "version": version.label,
            "file": destination.name,
            "source": version.source_description,
            "source_sha256": sha256(version.text.encode("utf-8")),
            "html_sha256": sha256(rendered),
            "bytes": len(rendered),
        })

    landing = index_html(versions).encode("utf-8")
    (OUTPUT / "index.html").write_bytes(landing)
    readme = """# Historical standalone manuscript HTML

Open `index.html` for the comparison menu, or open any version directly.

- `v14.html`
- `v15.html`
- `v15-1.html`
- `v15-2.html`

Each version file contains the manuscript and all CSS in one document. These
are deliberately manuscript renderings, not reconstructions of prior site
interfaces. The current interactive v15.2 reader is in `../standalone/`.

Local repository references are displayed as visible paths. External source
links remain clickable. No JavaScript, external fonts, local images, or runtime
dependencies are required.

Status: local owner review; no empirical results; not published.
"""
    (OUTPUT / "README.md").write_text(readme, encoding="utf-8")
    manifest = {
        "schema_version": "1.0",
        "generated_on": GENERATED_ON,
        "status": "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED",
        "role": "self-contained manuscript comparison; not historical site reconstruction",
        "landing_file": "index.html",
        "landing_sha256": sha256(landing),
        "versions": output_records,
    }
    (OUTPUT / "HISTORY_HTML_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
