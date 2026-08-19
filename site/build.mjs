import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SITE_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SITE_DIR, "..");
const DIST_DIR = path.join(SITE_DIR, "dist");
const EXPORT_DIR = path.join(SITE_DIR, "exports", "standalone");
const HISTORICAL_DIAGRAM = "historical-v13-pattern-recognition-diagram-v12.png";

const readText = (relativePath) =>
  fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const readJson = (relativePath) => JSON.parse(readText(relativePath));

const escapeHtml = (value) =>
  String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");

const escapeAttribute = (value) => escapeHtml(value).replaceAll("\n", " ");

const slugify = (value) =>
  String(value)
    .toLowerCase()
    .replace(/<[^>]+>/g, "")
    .replace(/&[^;]+;/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "") || "section";

const familySource = readJson("framework/SIX_FAMILIES.json");
const contentInterface = readJson("docs/CONTENT_INTERFACE_V16.json");
const essaySource = readText("manuscript/PATTERN_RECOGNITION_V16.md");
const glossarySource = readText("framework/GLOSSARY.md");
const styles = fs.readFileSync(path.join(SITE_DIR, "src", "site.css"), "utf8");
const scripts = fs.readFileSync(path.join(SITE_DIR, "src", "site.js"), "utf8");

const ROUTES = {
  read: { label: "Read the idea", directory: "read" },
  map: { label: "Explore the map", directory: "map" },
  apply: { label: "Apply it", directory: "apply" },
  examples: { label: "Examples", directory: "examples" },
  boundaries: { label: "Boundaries", directory: "boundaries" },
  sources: { label: "Sources", directory: "sources" },
  research: { label: "Research", directory: "research" },
  history: { label: "History", directory: "history" },
};

const routeHref = (ctx, route, fragment = "") => {
  if (ctx.standalone) {
    return fragment ? `#${fragment}` : `#${route}`;
  }
  const target = route === "home" ? "index.html" : `${ROUTES[route].directory}/index.html`;
  return `${ctx.base}${target}${fragment ? `#${fragment}` : ""}`;
};

const externalHref = (href) =>
  /^https?:\/\//i.test(href) || /^mailto:/i.test(href) || /^tel:/i.test(href);

const sourceRouteFor = (href) => {
  const normalized = href.toLowerCase();
  const mappings = [
    ["pattern_recognition_v16", "read"],
    ["ninety_second_version", "read"],
    ["mentor_cover_note", "read"],
    ["public_abstract", "read"],
    ["six_families", "map"],
    ["relationship_map", "map"],
    ["glossary", "map"],
    ["operator_playbook", "apply"],
    ["implementation_choices", "apply"],
    ["boundaries_and_failures", "boundaries"],
    ["agent-playbook", "apply"],
    ["framework/templates", "apply"],
    ["cases/", "examples"],
    ["signal-foundry", "examples"],
    ["general-research", "examples"],
    ["product-and-process", "examples"],
    ["sources_and_research_route", "sources"],
    ["claims_and_source_ledger", "sources"],
    ["the_discrimination_layer_research_agenda", "research"],
    ["future-studies", "research"],
    ["the-echo-problem", "research"],
    ["origin_note", "history"],
    ["source_authority_and_lineage", "history"],
    ["archive/", "history"],
  ];
  return mappings.find(([needle]) => normalized.includes(needle))?.[1] ?? null;
};

const siteSourceHref = (href, ctx) => {
  if (externalHref(href)) return href;
  if (href.startsWith("#")) return href;
  const [withoutQuery, query = ""] = href.split("?");
  const [withoutFragment, fragment = ""] = withoutQuery.split("#");
  const route = sourceRouteFor(withoutFragment);
  if (!route) return ctx.standalone ? `#source-${slugify(withoutFragment)}` : `${ctx.base}index.html`;
  return routeHref(ctx, route, fragment || query || "");
};

const applyEmphasis = (value) =>
  value
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/__([^_]+)__/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/_([^_]+)_/g, "<em>$1</em>");

const inlineMarkdown = (value, ctx) => {
  const tokens = [];
  const storeToken = (html) => {
    const token = `\uE000${tokens.length}\uE001`;
    tokens.push(html);
    return token;
  };
  const restoreTokens = (valueWithTokens) => {
    let restored = valueWithTokens;
    let previous;
    do {
      previous = restored;
      restored = restored.replace(/\uE000(\d+)\uE001/g, (_, index) => tokens[Number(index)]);
    } while (restored !== previous);
    return restored;
  };
  const formatLabel = (label) => restoreTokens(applyEmphasis(escapeHtml(label)));

  let output = String(value);
  output = output.replace(/`([^`]+)`/g, (_, text) =>
    storeToken(`<code>${escapeHtml(text)}</code>`)
  );
  output = output.replace(/!\[([^\]]*)\]\(((?:[^()]|\([^()]*\))*)\)/g, (_, alt, href) =>
    storeToken(`<span class="inline-media-note">[${formatLabel(alt)}: ${escapeHtml(href)}]</span>`)
  );
  output = output.replace(/\[([^\]]+)\]\(((?:[^()]|\([^()]*\))*)\)/g, (_, label, href) => {
    const resolved = siteSourceHref(href, ctx);
    const external = externalHref(href);
    return storeToken(`<a href="${escapeAttribute(resolved)}"${external ? ' target="_blank" rel="noreferrer"' : ""}>${formatLabel(label)}</a>`);
  });
  return restoreTokens(applyEmphasis(escapeHtml(output)));
};

const tableCells = (line) => {
  const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  return trimmed.split("|").map((cell) => cell.trim());
};

const isTableSeparator = (line) => {
  if (!line?.includes("|")) return false;
  return tableCells(line).every((cell) => /^:?-{3,}:?$/.test(cell));
};

const isUnordered = (line) => /^\s*[-*]\s+/.test(line);
const isOrdered = (line) => /^\s*\d+[.)]\s+/.test(line);

const renderMarkdown = (markdown, options = {}) => {
  const {
    ctx = { base: "", standalone: false },
    headingOffset = 0,
    idPrefix = "",
    stripMermaid = false,
  } = options;
  const lines = markdown.replaceAll("\r\n", "\n").split("\n");
  const output = [];
  let paragraph = [];

  const flushParagraph = () => {
    if (!paragraph.length) return;
    output.push(`<p>${inlineMarkdown(paragraph.join(" "), ctx)}</p>`);
    paragraph = [];
  };

  let index = 0;
  while (index < lines.length) {
    const line = lines[index];
    const trimmed = line.trim();

    if (!trimmed) {
      flushParagraph();
      index += 1;
      continue;
    }

    const fence = trimmed.match(/^```(.*)$/);
    if (fence) {
      flushParagraph();
      const language = fence[1].trim();
      const code = [];
      index += 1;
      while (index < lines.length && !/^```\s*$/.test(lines[index].trim())) {
        code.push(lines[index]);
        index += 1;
      }
      if (!(stripMermaid && language.toLowerCase() === "mermaid")) {
        output.push(`<pre class="code-block"><code class="language-${escapeAttribute(language || "text")}">${escapeHtml(code.join("\n"))}</code></pre>`);
      }
      index += 1;
      continue;
    }

    const heading = trimmed.match(/^(#{1,6})\s+(.+?)\s*#*$/);
    if (heading) {
      flushParagraph();
      const level = Math.min(6, heading[1].length + headingOffset);
      const text = inlineMarkdown(heading[2], ctx);
      const id = `${idPrefix}${slugify(heading[2])}`;
      output.push(`<h${level} id="${escapeAttribute(id)}">${text}</h${level}>`);
      index += 1;
      continue;
    }

    if (/^---+$/.test(trimmed) || /^\*\s*\*\s*\*$/.test(trimmed)) {
      flushParagraph();
      output.push("<hr>");
      index += 1;
      continue;
    }

    if (trimmed.startsWith(">")) {
      flushParagraph();
      const quote = [];
      while (index < lines.length && lines[index].trim().startsWith(">")) {
        quote.push(lines[index].trim().replace(/^>\s?/, ""));
        index += 1;
      }
      output.push(`<blockquote>${renderMarkdown(quote.join("\n"), { ctx, headingOffset, idPrefix, stripMermaid })}</blockquote>`);
      continue;
    }

    if (line.includes("|") && isTableSeparator(lines[index + 1])) {
      flushParagraph();
      const header = tableCells(line);
      index += 2;
      const rows = [];
      while (index < lines.length && lines[index].trim() && lines[index].includes("|")) {
        rows.push(tableCells(lines[index]));
        index += 1;
      }
      const headerHtml = header.map((cell) => `<th scope="col">${inlineMarkdown(cell, ctx)}</th>`).join("");
      const rowsHtml = rows.map((row) => {
        const cells = header.map((_, cellIndex) => row[cellIndex] ?? "");
        return `<tr>${cells.map((cell) => `<td>${inlineMarkdown(cell, ctx)}</td>`).join("")}</tr>`;
      }).join("");
      output.push(`<div class="table-wrap"><table><thead><tr>${headerHtml}</tr></thead><tbody>${rowsHtml}</tbody></table></div>`);
      continue;
    }

    if (isUnordered(line) || isOrdered(line)) {
      flushParagraph();
      const ordered = isOrdered(line);
      const items = [];
      while (index < lines.length) {
        const match = lines[index].match(ordered ? /^\s*\d+[.)]\s+(.+)$/ : /^\s*[-*]\s+(.+)$/);
        if (!match) break;
        items.push(match[1]);
        index += 1;
        while (index < lines.length && /^\s{2,}\S/.test(lines[index]) && !isUnordered(lines[index]) && !isOrdered(lines[index])) {
          items[items.length - 1] += ` ${lines[index].trim()}`;
          index += 1;
        }
      }
      const tag = ordered ? "ol" : "ul";
      output.push(`<${tag}>${items.map((item) => `<li>${inlineMarkdown(item, ctx)}</li>`).join("")}</${tag}>`);
      continue;
    }

    paragraph.push(trimmed);
    index += 1;
  }
  flushParagraph();
  return output.join("\n");
};

const extractSection = (markdown, startHeading, endHeading = null) => {
  const start = markdown.indexOf(startHeading);
  if (start < 0) return "";
  const end = endHeading ? markdown.indexOf(endHeading, start + startHeading.length) : -1;
  return markdown.slice(start, end < 0 ? undefined : end).trim();
};

const parseTableAfterHeading = (markdown, heading) => {
  const start = markdown.indexOf(heading);
  if (start < 0) return [];
  const lines = markdown.slice(start).split("\n");
  const headerIndex = lines.findIndex((line, index) => index > 0 && line.includes("|"));
  if (headerIndex < 0 || !isTableSeparator(lines[headerIndex + 1])) return [];
  const headers = tableCells(lines[headerIndex]);
  const rows = [];
  for (let index = headerIndex + 2; index < lines.length; index += 1) {
    if (!lines[index].trim() || !lines[index].includes("|")) break;
    const cells = tableCells(lines[index]);
    rows.push(Object.fromEntries(headers.map((header, cellIndex) => [header.toLowerCase(), cells[cellIndex] ?? ""])));
  }
  return rows;
};

const glossaryRows = parseTableAfterHeading(glossarySource, "# Applied-framework glossary");
const glossaryPlainRows = parseTableAfterHeading(glossarySource, "## Plain-language translations");
const glossaryByTerm = new Map(glossaryRows.map((row) => [row.term, row]));
const glossaryPlainByTerm = new Map(glossaryPlainRows.map((row) => [row["technical phrase"], row["plain-language explanation"]]));

const glossaryTermList = [
  "Evidence spine",
  "Typed relationship",
  "Influence receipt",
  "Cost-bounded route",
  "Versioned memory",
  "Common origin",
  "Human disposition",
];

const renderGlossary = (ctx) => `
  <section class="glossary-section" aria-labelledby="glossary-heading">
    <div class="section-heading compact-heading">
      <p class="eyebrow">OPTIONAL GLOSSARY</p>
      <h2 id="glossary-heading">A few terms, translated before they get technical.</h2>
      <p>These explanations deepen the map. The visible family questions and boundaries remain understandable without opening them.</p>
    </div>
    <div class="glossary-grid">
      ${glossaryTermList.map((term) => {
        const row = glossaryByTerm.get(term) ?? {};
        const plain = glossaryPlainByTerm.get(term) ?? "A bounded record that keeps the route inspectable.";
        return `<details class="glossary-item"><summary>${escapeHtml(term)}</summary><p><strong>Plain language:</strong> ${inlineMarkdown(plain, ctx)}</p><p>${inlineMarkdown(row["working meaning"] ?? "", ctx)}</p><p class="boundary"><strong>Boundary:</strong> ${inlineMarkdown(row.boundary ?? "", ctx)}</p></details>`;
      }).join("")}
    </div>
  </section>`;

const renderSourceManifest = (surfaceId, ctx) => {
  const surface = [...contentInterface.doors, ...contentInterface.secondary_routes].find((item) => item.id === surfaceId);
  if (!surface) return "";
  return `<details class="source-manifest"><summary>Canonical source manifest for this route</summary><ul>${surface.sources.map((source) => `<li><code>${escapeHtml(source)}</code></li>`).join("")}</ul><p class="muted">The site presents these sources through a local owner-review build; it does not replace them as canonical authority.</p></details>`;
};

const renderDoorCard = (id, ctx) => {
  const door = contentInterface.doors.find((item) => item.id === id);
  return `<a class="door-card door-${id}" href="${routeHref(ctx, id, id === "read" ? "read-idea" : id)}">
    <span class="door-number">0${contentInterface.doors.findIndex((item) => item.id === id) + 1}</span>
    <span class="door-title">${escapeHtml(door.label)}</span>
    <span class="door-promise">${escapeHtml(door.promise)}</span>
    <span class="door-arrow" aria-hidden="true">↗</span>
  </a>`;
};

const renderSecondaryNav = (ctx, active = "") => `
  <nav class="secondary-nav" aria-label="Secondary routes">
    ${Object.entries(ROUTES).filter(([key]) => ["examples", "boundaries", "sources", "research", "history"].includes(key)).map(([key, route]) => `<a class="${active === key ? "is-active" : ""}" href="${routeHref(ctx, key, key)}">${escapeHtml(route.label)}</a>`).join("")}
  </nav>`;

const renderHeader = (ctx, active = "") => `
  <header class="site-header">
    <a class="wordmark" href="${routeHref(ctx, "home", "top")}"><span>Pattern Map</span><small>v16 / local owner review</small></a>
    <nav class="primary-nav" aria-label="Principal routes">
      ${contentInterface.doors.map((door) => `<a class="${active === door.id ? "is-active" : ""}" href="${routeHref(ctx, door.id, door.id === "read" ? "read-idea" : door.id)}">${escapeHtml(door.label)}</a>`).join("")}
      <button class="nav-more" type="button" aria-expanded="false" aria-controls="secondary-routes">More <span aria-hidden="true">+</span></button>
    </nav>
    <div class="secondary-nav-wrap" id="secondary-routes">${renderSecondaryNav(ctx, active)}</div>
  </header>`;

const renderFooter = (ctx) => `
  <footer class="site-footer">
    <div><p class="eyebrow">LOCAL OWNER-REVIEW SURFACE</p><p>Built from the frozen v16 content interface. This package is a review candidate, not a deployment or research result.</p></div>
    <div class="footer-links"><a href="${routeHref(ctx, "home", "top")}">Back to the beginning</a><a href="${routeHref(ctx, "sources", "sources")}">Targeted sources</a><a href="${routeHref(ctx, "history", "history")}">Lineage and history</a></div>
  </footer>`;

const renderPage = ({ title, eyebrow, intro, content, ctx, active = "", id = "page" }) => `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Pattern Recognition / The Discrimination Layer v16 — local owner-review site.">
  <title>${escapeHtml(title)} — Pattern Map v16</title>
  ${ctx.standalone ? `<style>${styles}</style>` : `<link rel="stylesheet" href="${ctx.base}assets/site.css">`}
</head>
<body id="${escapeAttribute(id)}">
  <a class="skip-link" href="#main">Skip to main content</a>
  ${renderHeader(ctx, active)}
  <main id="main" tabindex="-1">
    ${eyebrow ? `<section class="route-intro"><p class="eyebrow">${escapeHtml(eyebrow)}</p><h1>${escapeHtml(title)}</h1>${intro ? `<p class="route-lede">${intro}</p>` : ""}</section>` : ""}
    ${content}
  </main>
  ${renderFooter(ctx)}
  ${ctx.standalone ? `<script>${scripts}</script>` : `<script src="${ctx.base}assets/site.js" defer></script>`}
</body>
</html>`;

const renderFamilyCard = (family, ctx) => {
  const colorClass = `family-${family.id.toLowerCase()}`;
  const levels = Object.entries(family.implementation_levels ?? {});
  return `<article id="family-${family.id}" class="family-card ${colorClass}" data-family-card="${escapeAttribute(family.id)}">
    <div class="family-meta"><span class="family-id">${escapeHtml(family.id)}</span><span class="family-dot" aria-hidden="true"></span><button type="button" class="family-focus" data-family-focus="${escapeAttribute(family.id)}" aria-pressed="false">Focus this family</button></div>
    <h3>${escapeHtml(family.name)}</h3>
    <p class="family-question">${escapeHtml(family.reader_question)}</p>
    <p>${inlineMarkdown(family.purpose, ctx)}</p>
    <div class="family-columns"><div><h4>How it works</h4><p>${inlineMarkdown(family.mechanism, ctx)}</p></div><div><h4>Boundary</h4><p>${inlineMarkdown(family.boundaries[0], ctx)}</p></div></div>
    <details class="family-detail"><summary>Implementation detail</summary><dl>${levels.map(([level, description]) => `<div><dt>${escapeHtml(level)}</dt><dd>${inlineMarkdown(description, ctx)}</dd></div>`).join("")}</dl><p class="muted"><strong>When not to use:</strong> ${family.when_not_to_use.map((item) => inlineMarkdown(item, ctx)).join(" ")}</p></details>
  </article>`;
};

const renderCurrentTopology = (ctx) => `
  <section class="topology-section" aria-labelledby="topology-heading">
    <div class="section-heading">
      <p class="eyebrow">CURRENT V16 RELATIONSHIP VIEW</p>
      <h2 id="topology-heading">A connected movement, not a mandatory pipeline.</h2>
      <p>The current map keeps the six families visible while showing the supporting records around them. A lightweight operator may realize this as a few tables; an advanced builder may distribute it across tools. The arrows describe relationships, not an instruction to run every step.</p>
    </div>
    <figure class="topology-figure" aria-labelledby="topology-caption">
      <figcaption id="topology-caption" class="sr-only">Current v16 relationship view. A decision brief and permission envelope shape all six families. Evidence, baselines, gaps, comparisons, and disconfirmation feed a bounded route. Human disposition can correct any stage. Selected material reaches an influence receipt and generation; later outcomes feed the learning loop back to a bounded update.</figcaption>
      <div class="topology-grid">
        <div class="topology-node topology-start"><span class="node-kicker">STARTING CONTEXT</span><strong>Decision brief + permission envelope</strong><small>real decision · audience · stakes · budget · allowed operations</small></div>
        <div class="topology-family-row" aria-label="Six families">
          ${familySource.families.map((family) => `<a class="topology-node topology-family family-${family.id.toLowerCase()}" href="${routeHref(ctx, "map", `family-${family.id}`)}"><span>${escapeHtml(family.id)}</span><strong>${escapeHtml(family.name)}</strong><small>${escapeHtml(family.reader_question)}</small></a>`).join("")}
        </div>
        <div class="topology-records" aria-label="Supporting records">
          <div class="topology-node"><span class="node-kicker">OBSERVE</span><strong>Evidence register + capture receipts</strong><small>what entered, what failed, what remains unknown</small></div>
          <div class="topology-node"><span class="node-kicker">COMPARE</span><strong>Baseline · gap · memory · origin records</strong><small>time, peers, missing expected fields, shared pathways</small></div>
          <div class="topology-node"><span class="node-kicker">CHALLENGE</span><strong>Disconfirmation + uncertainty review</strong><small>contrary, missing, differently rooted, or limiting material</small></div>
        </div>
        <div class="topology-route"><span class="route-arrow" aria-hidden="true">↓</span><div class="topology-node route-node"><span class="node-kicker">BOUNDED ROUTE</span><strong>ACQUIRE · COMPARE · CLARIFY</strong><small>or HOLD · DEFER · ESCALATE · REFUSE</small></div><div class="route-branch"><span>ANSWER / ANSWER_PROVISIONALLY</span><span>HUMAN DISPOSITION</span></div></div>
        <div class="topology-endpoints"><div class="topology-node"><span class="node-kicker">INFLUENCE</span><strong>Influence receipt + context packet</strong><small>selected and withheld material stays inspectable</small></div><div class="topology-node"><span class="node-kicker">LEARN</span><strong>F6 Learning loop</strong><small>recorded expectation → outcome → bounded update proposal</small></div></div>
      </div>
    </figure>
    <p class="topology-note"><strong>Human correction remains in the loop.</strong> A person may revise a brief, correct a relationship, change a permission, hold a route, or override a recommendation. That disposition is a record of a decision, not a new fact.</p>
  </section>`;

const renderRoot = (ctx) => {
  const short = renderMarkdown(readText("manuscript/NINETY_SECOND_VERSION.md"), { ctx, headingOffset: 2, idPrefix: "short-" });
  return `
  <section class="hero" id="top">
    <div class="hero-copy">
      <p class="eyebrow hero-eyebrow">PATTERN RECOGNITION / THE DISCRIMINATION LAYER</p>
      <h1>AI slop often begins before the model writes a word.</h1>
      <p class="standfirst">${escapeHtml(contentInterface.first_screen.standfirst)}</p>
      <p class="hero-bridge">This is a broad proposal about the room before the answer: what gets noticed, compared, preserved, questioned, and allowed to shape generation.</p>
    </div>
    <nav class="door-grid" aria-label="Three principal doors">
      ${renderDoorCard("read", ctx)}${renderDoorCard("map", ctx)}${renderDoorCard("apply", ctx)}
    </nav>
  </section>
  <section class="home-section home-short" aria-labelledby="short-entry-heading">
    <div class="section-heading"><p class="eyebrow">A CUMULATIVE 60–90 SECOND ENTRY</p><h2 id="short-entry-heading">The idea before the machinery.</h2><p>Start here if you want the broad proposition in one sitting. The longer piece remains a human thought piece, not a protocol preamble.</p></div>
    <div class="short-entry reading-column">${short}</div>
    <a class="text-link" href="${routeHref(ctx, "read", "read-idea")}">Continue into the complete thought piece <span aria-hidden="true">→</span></a>
  </section>
  <section class="home-section map-preview" aria-labelledby="map-preview-heading">
    <div class="section-heading"><p class="eyebrow">THE SIX-FAMILY MAP</p><h2 id="map-preview-heading">Six ways to improve the room.</h2><p>The movement is simple enough to remember and careful enough to question: widen the field, weigh what enters, notice motion and gaps, compare explicitly, and learn without rewriting history.</p></div>
    <div class="family-strip">${familySource.families.map((family) => `<a class="family-strip-item family-${family.id.toLowerCase()}" href="${routeHref(ctx, "map", `family-${family.id}`)}"><span>${escapeHtml(family.id)}</span><strong>${escapeHtml(family.name)}</strong></a>`).join("")}</div>
    <a class="text-link" href="${routeHref(ctx, "map", "map")}">Open the current relationship view <span aria-hidden="true">→</span></a>
  </section>
  <section class="home-section application-preview" aria-labelledby="apply-preview-heading">
    <div class="section-heading"><p class="eyebrow">PROPORTION, NOT CEREMONY</p><h2 id="apply-preview-heading">Use the smallest route that leaves the important distinctions visible.</h2><p>A low-stakes rewrite may need almost none. Repeated or consequential work may merit a brief, evidence record, stop rule, human checkpoint, and later outcome review. No particular stack is mandatory.</p></div>
    <div class="level-row"><span class="level-pill level-ordinary">ordinary</span><span class="level-pill level-light">lightweight</span><span class="level-pill level-moderate">moderate</span><span class="level-pill level-advanced">advanced</span></div>
    <a class="text-link" href="${routeHref(ctx, "apply", "apply")}">Choose a proportionate path <span aria-hidden="true">→</span></a>
  </section>
  <section class="home-section late-context" aria-labelledby="late-context-heading">
    <div class="section-heading"><p class="eyebrow">LATER, IF IT HELPS</p><h2 id="late-context-heading">Examples, boundaries, sources, research, and history.</h2><p>These routes deepen the idea after the principal doors. They include a bounded Signal Foundry illustration, the separate unrun Echo project, and the recovered v13 origin map.</p></div>
    ${renderSecondaryNav(ctx)}
  </section>`;
};

const renderRead = (ctx) => {
  const short = renderMarkdown(readText("manuscript/NINETY_SECOND_VERSION.md"), { ctx, headingOffset: 2, idPrefix: "short-" });
  const essay = renderMarkdown(essaySource, { ctx, headingOffset: 1, idPrefix: "essay-" });
  const cover = renderMarkdown(readText("manuscript/MENTOR_COVER_NOTE.md"), { ctx, headingOffset: 2, idPrefix: "cover-" });
  const abstract = renderMarkdown(readText("manuscript/PUBLIC_ABSTRACT.md"), { ctx, headingOffset: 2, idPrefix: "abstract-" });
  return `
  <section class="reading-route" id="read-idea">
    <div class="reading-index" aria-label="Reading path"><span class="is-current">1. Enter in 60–90 seconds</span><span>2. Read the complete thought</span><span>3. Optional mentor handoff</span></div>
    <section class="short-entry reading-column" aria-labelledby="read-short-heading"><p class="eyebrow">CUMULATIVE 60–90 SECOND VERSION</p><h2 id="read-short-heading">The broad idea first.</h2>${short}</section>
    <section class="essay-section" aria-labelledby="complete-essay-heading"><div class="section-heading"><p class="eyebrow">COMPLETE HUMAN THOUGHT PIECE</p><h2 id="complete-essay-heading">Pattern Recognition: The Discrimination Layer</h2><p class="muted">Canonical source: <code>manuscript/PATTERN_RECOGNITION_V16.md</code>. This route keeps the full essay intact and lets technical detail arrive after the reader understands the problem.</p></div><article class="reading-column essay-content">${essay}</article></section>
    <section class="optional-handoff" aria-labelledby="mentor-heading"><details><summary id="mentor-heading">Optional handoff: cover note for mentor review</summary><div class="reading-column">${cover}</div></details></section>
    <section class="abstract-box" aria-labelledby="abstract-heading"><details><summary id="abstract-heading">Public abstract and concise metadata context</summary><div class="reading-column">${abstract}</div></details></section>
    ${renderSourceManifest("read", ctx)}
  </section>`;
};

const renderMap = (ctx) => `
  <section class="map-route" id="map">
    <div class="map-control-bar" aria-labelledby="map-controls-heading"><div><p class="eyebrow">ACCESSIBLE INTERACTIVE MAP</p><h2 id="map-controls-heading">Select a family to focus the reading.</h2><p class="muted" id="family-focus-status" aria-live="polite">All six families are visible. Focus controls add emphasis; they never hide essential meaning.</p></div><button type="button" class="quiet-button" data-family-clear>Show all</button></div>
    <div class="family-grid">${familySource.families.map((family) => renderFamilyCard(family, ctx)).join("")}</div>
    ${renderCurrentTopology(ctx)}
    ${renderGlossary(ctx)}
    <section class="map-boundary callout" aria-labelledby="map-boundary-heading"><p class="eyebrow">MAP BOUNDARY</p><h2 id="map-boundary-heading">The order is a teaching aid, not a compulsory sequence.</h2><p>Skip a family when it has no observable input, record why, and keep unknown relations unknown. Common-origin recurrence is one mechanism inside source weighing and structured patterns; it is not the map's definition.</p></section>
    ${renderSourceManifest("map", ctx)}
  </section>`;

const renderImplementationLevels = (ctx) => `
  <section class="implementation-section" aria-labelledby="levels-heading">
    <div class="section-heading"><p class="eyebrow">FOUR PROPORTIONATE CHOICES</p><h2 id="levels-heading">Choose the smallest route that fits the decision.</h2><p>No provider, model, database, graph, or custom service is required. The ordinary path is a valid choice when the work is reversible and evidence is supplied.</p></div>
    <div class="implementation-grid">
      <article class="implementation-card level-ordinary"><span class="level-pill">ordinary</span><h3>Do less when the task is simple.</h3><p>Use ordinary prompting with a short assumptions note for a creative transformation, direct format conversion, or supplied-input task where no new claim or acquisition decision is needed.</p><p class="card-boundary"><strong>Do not use the full framework</strong> when the record would cost more than the consequence of being wrong.</p></article>
      <article class="implementation-card level-light"><span class="level-pill">lightweight</span><h3>One brief, one alternate route, one clear stop.</h3><p>Best for reversible work with bounded evidence. Record the decision, permission, default path, one peripheral candidate, one comparison, one disconfirmation attempt, and the uncertainty in the answer.</p><p class="card-boundary"><strong>Stop when</strong> the alternate route or comparison is complete, or the stated time limit is reached.</p></article>
      <article class="implementation-card level-moderate"><span class="level-pill">moderate</span><h3>Make repeated work reproducible.</h3><p>Add stable IDs, source and artifact records, typed relationships, versioned evidence, human disposition, a context packet, and an outcome review.</p><p class="card-boundary"><strong>Stop when</strong> route-specific value is low, the budget is reached, or a human gate is required.</p></article>
      <article class="implementation-card level-advanced"><span class="level-pill">advanced</span><h3>Engineer only when hidden mistakes justify it.</h3><p>Add queryable lineage, baselines, time-series and gap views, access policies, routing, review queues, replayable packets, and approved matched-budget evaluation.</p><p class="card-boundary"><strong>Never infer autonomy:</strong> engineering does not authorize acquisition, disclosure, or external action.</p></article>
    </div>
  </section>`;

const renderStateVocabulary = (ctx) => `
  <section class="state-section" aria-labelledby="state-heading">
    <div class="section-heading"><p class="eyebrow">OBSERVABLE BEHAVIOR</p><h2 id="state-heading">Route, stop, and learning are different fields.</h2><p>Keeping these vocabularies separate prevents a fluent answer from hiding why the operator continued, stopped, deferred, or proposed an update.</p></div>
    <div class="state-grid">
      <article><h3>Route</h3><p>Choose the next bounded action.</p><ul><li><code>ACQUIRE</code></li><li><code>COMPARE</code></li><li><code>CLARIFY</code></li><li><code>ANSWER</code> / <code>ANSWER_PROVISIONALLY</code></li><li><code>HOLD</code> / <code>DEFER</code> / <code>ESCALATE</code> / <code>REFUSE</code></li></ul></article>
      <article><h3>Stop status</h3><p>Record why work ended, separately from the route.</p><ul><li><code>CONTINUE</code></li><li><code>COMPLETE</code></li><li><code>STOPPED_BUDGET</code></li><li><code>STOPPED_DEADLINE</code></li><li><code>STOPPED_OTHER</code></li></ul></article>
      <article><h3>Learning status</h3><p>Record whether a defined outcome can inform a bounded proposal.</p><ul><li><code>LEARNING_PLANNED</code></li><li><code>LEARNING_PENDING_OUTCOME</code></li><li><code>LEARNING_REVIEWED</code></li><li><code>LEARNING_NOT_APPLICABLE</code></li></ul></article>
    </div>
    <p class="callout-inline"><strong>Human authority stays explicit.</strong> Technical access is not permission. A route can propose, hold, or escalate; it does not grant authority to disclose, publish, spend, contact, or act.</p>
  </section>`;

const renderTemplateShelf = (ctx) => {
  const templates = [
    ["Decision brief", "framework/templates/DECISION_BRIEF.md"],
    ["Acquisition receipt", "framework/templates/ACQUISITION_RECEIPT.md"],
    ["Evidence register", "framework/templates/EVIDENCE_REGISTER.md"],
    ["Comparison matrix", "framework/templates/COMPARISON_MATRIX.md"],
    ["Disconfirmation log", "framework/templates/DISCONFIRMATION_LOG.md"],
    ["Influence receipt", "framework/templates/INFLUENCE_RECEIPT.md"],
    ["Outcome review", "framework/templates/OUTCOME_REVIEW.md"],
  ];
  return `<section class="template-section" aria-labelledby="template-heading"><div class="section-heading"><p class="eyebrow">COPYABLE RECORDS</p><h2 id="template-heading">Templates keep the route inspectable.</h2><p>Use only the records the decision warrants. A skipped family should be marked skipped or not applicable, not silently inferred.</p></div><div class="template-grid">${templates.map(([label, source]) => `<details class="template-card"><summary>${escapeHtml(label)}</summary><div class="source-markdown">${renderMarkdown(readText(source), { ctx, headingOffset: 2, idPrefix: `template-${slugify(label)}-` })}</div></details>`).join("")}</div></section>`;
};

const renderApply = (ctx) => `
  <section class="apply-route" id="apply">
    ${renderImplementationLevels(ctx)}
    <section class="operator-section" aria-labelledby="operator-heading"><div class="section-heading"><p class="eyebrow">OPERATOR PATH</p><h2 id="operator-heading">Twelve observable moves from decision to learning.</h2><p>Frame the real decision, set permission and cost, widen one bounded route, compare, challenge, route, preserve influence, and close the loop without rewriting the original record.</p></div><div class="operator-steps">${[
      ["01", "Frame the decision", "Write the decision, intended use, audience, consequence, deadline, and useful-answer condition."],
      ["02", "Set permission and cost", "Separate technical reach from authorized acquisition, retention, disclosure, and action."],
      ["03", "Write the default path", "Record the familiar query, sources, vocabulary, time window, or product route."],
      ["04", "Add one bounded peripheral route", "Choose a specialist, alternate vocabulary, dissenting view, adjacent peer set, or low-prominence field."],
      ["05", "Build the evidence register", "Keep source, artifact, version, claim, support, origin, permission, uncertainty, and disposition inspectable."],
      ["06", "Compare before concluding", "Align definitions, periods, peers, denominators, and mark incomparable fields."],
      ["07", "Inspect motion and absence", "Require repeated comparable observations for motion and an explicit expectation for a gap."],
      ["08", "Disconfirm the leading interpretation", "Search for contrary, missing, differently rooted, or limiting material."],
      ["09", "Route, stop, or escalate", "Choose a route and a separate stop status; state the reason, cost, permission, and resume condition."],
      ["10", "Record influence", "List what shaped the answer, what was withheld, why, and with what uncertainty."],
      ["11", "Generate and preserve the boundary", "Separate observation, interpretation, recommendation, and human decision."],
      ["12", "Close the loop", "Compare a recorded expectation with a defined later outcome and propose one bounded update."],
    ].map(([number, title, description]) => `<article class="operator-step"><span class="step-number">${number}</span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(description)}</p></article>`).join("")}</div></section>
    ${renderStateVocabulary(ctx)}
    <section class="agent-section" aria-labelledby="agent-heading"><div class="section-heading"><p class="eyebrow">AGENT COMPANION</p><h2 id="agent-heading">Copyable procedures, not an exhortation to be creative.</h2><p>The agent guide makes acquisition, comparison, disconfirmation, uncertainty, cost, stop, escalation, influence, and learning visible in artifacts another person can inspect.</p></div><div class="agent-docs"><details class="agent-doc agent-quickstart" open><summary>Quickstart — the smallest safe procedure</summary><div class="source-markdown">${renderMarkdown(readText("framework/agent-playbook/QUICKSTART.md"), { ctx, headingOffset: 2, idPrefix: "agent-quickstart-" })}</div></details><details class="agent-doc"><summary>Full operating guide — deeper procedure</summary><div class="source-markdown">${renderMarkdown(readText("framework/agent-playbook/FULL_OPERATING_GUIDE.md"), { ctx, headingOffset: 2, idPrefix: "agent-guide-" })}</div></details><details class="agent-doc"><summary>Copyable agent brief</summary><div class="source-markdown">${renderMarkdown(readText("framework/agent-playbook/COPYABLE_AGENT_BRIEF.md"), { ctx, headingOffset: 2, idPrefix: "agent-brief-" })}</div></details><details class="agent-doc"><summary>Preflight and decision receipt</summary><div class="source-markdown">${renderMarkdown(readText("framework/agent-playbook/PREFLIGHT_CHECKLIST.md"), { ctx, headingOffset: 2, idPrefix: "agent-preflight-" })}${renderMarkdown(readText("framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md"), { ctx, headingOffset: 2, idPrefix: "agent-receipt-" })}</div></details></div></section>
    ${renderTemplateShelf(ctx)}
    ${renderSourceManifest("apply", ctx)}
  </section>`;

const renderExample = (title, eyebrow, content, accent) => `<article class="example-card ${accent ?? ""}"><p class="eyebrow">${escapeHtml(eyebrow)}</p><h3>${escapeHtml(title)}</h3>${content}</article>`;

const renderExamples = (ctx) => {
  const specialist = extractSection(essaySource, "#### Worked example 1: a specialist signal", "### 2. Source weighing");
  const motion = extractSection(essaySource, "#### Worked example 2: motion and expected absence", "### 5. Structured patterns");
  const recurrence = extractSection(essaySource, "## A narrower example: nine reports, one announcement", "## What the Discrimination Layer looks like in practice");
  const ordinary = readText("framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md");
  return `
  <section class="examples-route" id="examples">
    <div class="section-heading"><p class="eyebrow">TEACHING PATTERNS</p><h2>Three ways a pattern can improve the room without becoming a verdict.</h2><p>These are bounded illustrations. They are not validation, and they do not authorize acquisition or action.</p></div>
    <div class="example-grid">
      ${renderExample("A specialist signal is a candidate, not a truth", "01 / PERIPHERAL SIGNAL", `<div class="microvisual specialist-visual" role="img" aria-label="A default path with a smaller specialist route entering as a candidate for inspection"><span class="micro-path main-path">default path</span><span class="micro-path peripheral-path">specialist route</span><span class="micro-node">inspect</span><span class="micro-node">weigh</span><span class="micro-node">disconfirm</span></div><div class="source-markdown">${renderMarkdown(specialist, { ctx, headingOffset: 0, idPrefix: "example-specialist-" })}</div><p class="boundary-line"><strong>Boundary:</strong> underweighted is a reason to inspect, not a reason to believe.</p>`, "example-specialist")}
      ${renderExample("Motion and absence need an explicit baseline", "02 / VELOCITY + EXPECTED ABSENCE", `<div class="microvisual baseline-visual" role="img" aria-label="A baseline with five prior releases, a current packet missing two fields, and a support count rising from five to eighteen"><div class="baseline-bars"><span style="height:32%">5</span><span style="height:38%">6</span><span style="height:35%">5</span><span style="height:42%">7</span><span class="current-bar" style="height:100%">18</span></div><div class="baseline-labels"><span>prior</span><span>prior</span><span>prior</span><span>prior</span><span>current</span></div><p>current packet: exposure present / rollback owner missing / monitoring window missing</p></div><div class="source-markdown">${renderMarkdown(motion, { ctx, headingOffset: 0, idPrefix: "example-motion-" })}</div><p class="boundary-line"><strong>Boundary:</strong> one observation is not velocity; a gap is not proof of nonexistence.</p>`, "example-motion")}
    </div>
    <div class="example-late"><p class="eyebrow">03 / STRUCTURED PATTERNS</p><h2>Recurrence can be one origin wearing nine outfits.</h2><div class="recurrence-visual" role="img" aria-label="Nine report cards point to one shared announcement origin, with independence shown as unknown"><div class="report-cluster">${Array.from({ length: 9 }, (_, index) => `<span class="report-chip">report ${index + 1}</span>`).join("")}</div><span class="origin-arrow" aria-hidden="true">↓</span><span class="origin-chip">one shared announcement</span><span class="unknown-chip">independence: UNKNOWN</span></div><div class="source-markdown">${renderMarkdown(recurrence, { ctx, headingOffset: 1, idPrefix: "example-recurrence-" })}</div><p class="boundary-line"><strong>Boundary:</strong> repeated reports are observations; recurrence is not independent corroboration.</p><p class="echo-label"><span class="status-dot" aria-hidden="true"></span><strong>The Echo Problem</strong> is a separate project — unrun — no results. It is linked here only as a subordinate origin-accounting route.</p></div>
    <section class="case-section" aria-labelledby="cases-heading"><div class="section-heading"><p class="eyebrow">BOUNDED CASES</p><h2 id="cases-heading">From illustration to inspectable practice.</h2><p>Signal Foundry is labeled every time it appears: <strong>ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION.</strong> The neutral cases show how the same records can stay proportionate across domains.</p></div><div class="case-grid"><details class="case-card signal-foundry" open><summary>Signal Foundry — ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION</summary><div class="source-markdown">${renderMarkdown(readText("cases/signal-foundry/README.md"), { ctx, headingOffset: 2, idPrefix: "case-signal-foundry-" })}</div></details><details class="case-card"><summary>Domain-neutral case A — a second weekly session</summary><div class="source-markdown">${renderMarkdown(readText("cases/general-research/README.md"), { ctx, headingOffset: 2, idPrefix: "case-general-" })}</div></details><details class="case-card"><summary>Domain-neutral case B — an intake process</summary><div class="source-markdown">${renderMarkdown(readText("cases/product-and-process/README.md"), { ctx, headingOffset: 2, idPrefix: "case-process-" })}</div></details></div></section>
    <section class="ordinary-contrast" aria-labelledby="ordinary-heading"><details><summary id="ordinary-heading">Ordinary work versus the Discrimination Layer</summary><div class="source-markdown">${renderMarkdown(ordinary, { ctx, headingOffset: 2, idPrefix: "ordinary-" })}</div></details></section>
    ${renderSourceManifest("examples", ctx)}
  </section>`;
};

const renderBoundaries = (ctx) => `
  <section class="boundaries-route" id="boundaries">
    <div class="boundary-banner"><p class="eyebrow">CLAIM + AUTHORITY BOUNDARY</p><h2>Make upstream choices visible without pretending they are settled science.</h2><p>The framework is a design proposal and a set of testable questions. A fixture, validator, protocol, case, or review can establish integrity or inspectability; it is not an effectiveness result.</p></div>
    <div class="source-markdown long-source">${renderMarkdown(readText("framework/BOUNDARIES_AND_FAILURES.md"), { ctx, headingOffset: 1, idPrefix: "boundaries-source-" })}</div>
    <section class="firebreak-grid" aria-label="Permanent project boundaries"><article><p class="eyebrow">TWO PROJECTS</p><h3>V16 is broad.</h3><p>The Echo Problem is a separate origin-accounting research track. Removing it leaves the six-family idea intact.</p></article><article><p class="eyebrow">HUMAN JUDGMENT</p><h3>Scaffold the floor; do not automate the ceiling.</h3><p>Comparison, memory, gap detection, and source tracing can be scaffolded. Taste, accountability, permission, contextual judgment, and consequential authority remain human.</p></article><article><p class="eyebrow">WHEN NOT TO USE IT</p><h3>Ordinary is a valid route.</h3><p>Use less structure for creative transformations, supplied-input formatting, reversible low-stakes work, or any task where the record would cost more than the consequence of being wrong.</p></article></div></section>
    <section class="artifact-boundaries"><details><summary>Artifact firebreaks and the five collapse tests</summary><div class="source-markdown">${renderMarkdown(readText("docs/ARTIFACT_BOUNDARIES.md"), { ctx, headingOffset: 2, idPrefix: "artifact-boundary-" })}</div></details></section>
    ${renderSourceManifest("boundaries", ctx)}
  </section>`;

const renderSources = (ctx) => `
  <section class="sources-route" id="sources">
    <div class="source-notice"><p class="eyebrow">TARGETED, NOT EXHAUSTIVE</p><h2>Sources are a wayfinding route, not a literature-defense opening.</h2><p>The links below inherit their status from the canonical source files. They are not presented as newly reverified for public release. Re-verify links before any future publication.</p></div>
    <div class="source-markdown long-source">${renderMarkdown(readText("manuscript/SOURCES_AND_RESEARCH_ROUTE.md"), { ctx, headingOffset: 1, idPrefix: "sources-route-" })}</div>
    <details class="claims-source"><summary>Claims and source ledger</summary><div class="source-markdown">${renderMarkdown(readText("docs/CLAIMS_AND_SOURCE_LEDGER_V16.md"), { ctx, headingOffset: 2, idPrefix: "claims-ledger-" })}</div></details>
    ${renderSourceManifest("sources", ctx)}
  </section>`;

const renderResearch = (ctx) => `
  <section class="research-route" id="research">
    <div class="research-status"><span class="status-dot" aria-hidden="true"></span><div><p class="eyebrow">RESEARCH ROUTE / STATUS</p><h2>UNRUN · NO RESULTS · NO PROVIDER OR MODEL SELECTED</h2><p>This route describes future questions and boundaries only. It does not authorize a model call, provider selection, participant activity, dataset acquisition, preregistration, publication, deployment, or spend.</p></div></div>
    <div class="source-markdown long-source">${renderMarkdown(readText("research/README.md"), { ctx, headingOffset: 1, idPrefix: "research-readme-" })}${renderMarkdown(readText("research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md"), { ctx, headingOffset: 1, idPrefix: "research-agenda-" })}</div>
    <details class="protocol-source"><summary>Future protocol candidate: DL-PLAYBOOK-01 v0.1 — specification only</summary><div class="source-markdown">${renderMarkdown(readText("research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md"), { ctx, headingOffset: 2, idPrefix: "protocol-" })}</div></details>
    <section class="echo-section" aria-labelledby="echo-heading"><div class="echo-callout"><p class="eyebrow">SEPARATE PROJECT / RESEARCH TRACK 01</p><h2 id="echo-heading">The Echo Problem — separate project — unrun — no results</h2><p>Echo is a v15.2-derived origin-accounting project. Its preserved protocol, fixtures, harness, prior art, and unfavorable-result classes remain in its own track. V16 uses common-origin recurrence as one worked example; it does not borrow results or let Echo define the map.</p></div><details><summary>Read the Echo identity and status boundary</summary><div class="source-markdown">${renderMarkdown(readText("research/the-echo-problem/README.md"), { ctx, headingOffset: 2, idPrefix: "echo-readme-" })}${renderMarkdown(readText("research/the-echo-problem/STATUS_AND_BOUNDARIES.md"), { ctx, headingOffset: 2, idPrefix: "echo-status-" })}</div></details></section>
    ${renderSourceManifest("research", ctx)}
  </section>`;

const renderHistory = (ctx) => {
  const imageSrc = ctx.standalone ? `../../../assets/diagrams/${HISTORICAL_DIAGRAM}` : `${ctx.base}assets/diagrams/${HISTORICAL_DIAGRAM}`;
  return `
  <section class="history-route" id="history">
    <div class="history-intro"><p class="eyebrow">LINEAGE WITHOUT MYTHOLOGY</p><h2>V13 is an origin anchor, not today's topology.</h2><p>V16 returns to the broad reader problem and keeps the six families visible. V14 and v15 contributed rigor and limits; v15.2 is the source checkpoint for the separate Echo project.</p></div>
    <div class="lineage-grid"><article><span class="lineage-step">v13</span><h3>Historical origin</h3><p>Broad reader problem, six-family ambition, and the original visual map. Preserved as historical material.</p></article><article><span class="lineage-step">v14–v15</span><h3>Rigor and restraint</h3><p>Accessibility, terminology, implementation alternatives, prior-art caution, and explicit limits.</p></article><article><span class="lineage-step">v15.2 → EP v0.1</span><h3>Separate Echo track</h3><p>Origin accounting with an explicit no-results boundary. It does not redefine v16.</p></article><article><span class="lineage-step">v16</span><h3>Current broad map</h3><p>Pattern Recognition / The Discrimination Layer, organized around the six families and a human-correctable responsibility.</p></article></div>
    <section class="historical-figure" aria-labelledby="historical-heading"><p class="eyebrow">PRESERVED ASSET / HASH-ANCHORED</p><h2 id="historical-heading">Historical v13 origin — not the current v16 topology.</h2><figure><img src="${escapeAttribute(imageSrc)}" alt="Historical v13 Pattern Recognition diagram showing the original six-family visual map. This image is not the current v16 topology." loading="lazy"><figcaption><strong>Historical v13 origin — not the current v16 topology.</strong> The current relationship view is the code-native map on the Explore route. The recovered asset is shown for continuity only.</figcaption></figure></section>
    <section class="history-notes"><div class="source-markdown long-source">${renderMarkdown(readText("manuscript/ORIGIN_NOTE.md"), { ctx, headingOffset: 1, idPrefix: "origin-note-" })}${renderMarkdown(readText("docs/SOURCE_AUTHORITY_AND_LINEAGE.md"), { ctx, headingOffset: 1, idPrefix: "lineage-" })}</div><details><summary>Archive index and historical recovery note</summary><div class="source-markdown">${renderMarkdown(readText("archive/README.md"), { ctx, headingOffset: 2, idPrefix: "archive-readme-" })}${renderMarkdown(readText("archive/v13/README.md"), { ctx, headingOffset: 2, idPrefix: "archive-v13-" })}</div></details></section>
    ${renderSourceManifest("history", ctx)}
  </section>`;
};

const pageDefinitions = (ctx) => ({
  home: renderPage({ title: "Pattern Recognition / The Discrimination Layer", content: renderRoot(ctx), ctx, id: "home" }),
  read: renderPage({ title: "Read the idea", eyebrow: "PRINCIPAL DOOR 01", intro: "Continue the coffee conversation: why choices made before generation shape what an answer can become.", content: renderRead(ctx), ctx, active: "read", id: "read-page" }),
  map: renderPage({ title: "Explore the map", eyebrow: "PRINCIPAL DOOR 02", intro: "See six ways to improve what the system notices, compares, preserves, questions, and learns from.", content: renderMap(ctx), ctx, active: "map", id: "map-page" }),
  apply: renderPage({ title: "Apply it", eyebrow: "PRINCIPAL DOOR 03", intro: "Turn the idea into a proportionate workflow, from one decision brief to an inspectable agent procedure.", content: renderApply(ctx), ctx, active: "apply", id: "apply-page" }),
  examples: renderPage({ title: "Examples", eyebrow: "SECONDARY ROUTE", intro: "See the distinctions in motion through bounded teaching patterns and illustrative cases.", content: renderExamples(ctx), ctx, active: "examples", id: "examples-page" }),
  boundaries: renderPage({ title: "Boundaries", eyebrow: "SECONDARY ROUTE", intro: "Know when to add structure, when to stop, and what the framework cannot claim or authorize.", content: renderBoundaries(ctx), ctx, active: "boundaries", id: "boundaries-page" }),
  sources: renderPage({ title: "Sources", eyebrow: "SECONDARY ROUTE", intro: "A targeted route for authority, continuity, and claim-constraining prior art.", content: renderSources(ctx), ctx, active: "sources", id: "sources-page" }),
  research: renderPage({ title: "Research", eyebrow: "SECONDARY ROUTE", intro: "Future questions and explicit no-results boundaries, kept subordinate to the human idea.", content: renderResearch(ctx), ctx, active: "research", id: "research-page" }),
  history: renderPage({ title: "History", eyebrow: "SECONDARY ROUTE", intro: "How the broad v16 map returns to the historical origin without redrawing it as current topology.", content: renderHistory(ctx), ctx, active: "history", id: "history-page" }),
});

const writeFile = (filePath, content) => {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, content.replace(/[ \t]+$/gm, ""));
};

const build = () => {
  fs.rmSync(DIST_DIR, { recursive: true, force: true });
  fs.mkdirSync(DIST_DIR, { recursive: true });
  fs.mkdirSync(path.join(DIST_DIR, "assets", "diagrams"), { recursive: true });
  fs.copyFileSync(path.join(SITE_DIR, "src", "site.css"), path.join(DIST_DIR, "assets", "site.css"));
  fs.copyFileSync(path.join(SITE_DIR, "src", "site.js"), path.join(DIST_DIR, "assets", "site.js"));
  const diagramSource = path.join(ROOT, "assets", "diagrams", HISTORICAL_DIAGRAM);
  if (!fs.existsSync(diagramSource)) {
    throw new Error(`Missing historical diagram: ${diagramSource}`);
  }
  fs.copyFileSync(diagramSource, path.join(DIST_DIR, "assets", "diagrams", HISTORICAL_DIAGRAM));

  const rootPages = pageDefinitions({ base: "", standalone: false });
  const nestedPages = pageDefinitions({ base: "../", standalone: false });
  writeFile(path.join(DIST_DIR, "index.html"), rootPages.home);
  Object.entries(nestedPages).filter(([key]) => key !== "home").forEach(([key, html]) => {
    writeFile(
      path.join(DIST_DIR, ROUTES[key].directory, "index.html"),
      html.replaceAll('href="assets/', 'href="../assets/').replaceAll('src="assets/', 'src="../assets/')
    );
  });

  const standalonePages = pageDefinitions({ base: "", standalone: true });
  const standaloneContent = Object.entries(standalonePages).map(([key, html]) => {
    const main = html.match(/<main id="main"[^>]*>([\s\S]*)<\/main>/i)?.[1] ?? "";
    return `<section class="standalone-section" id="standalone-${key}">${main}</section>`;
  }).join("\n");
  const standalone = renderPage({
    title: "Pattern Map v16 — standalone owner-review export",
    eyebrow: "STANDALONE REVIEW EXPORT",
    intro: "A self-contained local HTML companion. All principal doors and secondary routes are included below as readable sections.",
    content: `<div class="standalone-intro"><p class="callout-inline"><strong>Local owner review only.</strong> This file is designed to open directly from disk. It contains no deployed URL, external runtime, or research result.</p></div>${standaloneContent}`,
    ctx: { base: "", standalone: true },
    id: "standalone-export",
  });
  writeFile(path.join(EXPORT_DIR, "pattern-map-v16.html"), standalone.replaceAll("../../../assets/diagrams/", "../../../assets/diagrams/"));
  console.log(`Built ${Object.keys(rootPages).length} routes to ${DIST_DIR}`);
  console.log(`Built standalone export to ${path.join(EXPORT_DIR, "pattern-map-v16.html")}`);
};

build();
