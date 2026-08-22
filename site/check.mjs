import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SITE_DIR = path.dirname(fileURLToPath(import.meta.url));
const DIST_DIR = path.join(SITE_DIR, "dist");
const EXPORT_PATH = path.join(SITE_DIR, "exports", "standalone", "pattern-map-v16.html");
const CSS_PATH = path.join(SITE_DIR, "src", "site.css");

const requiredRoutes = [
  "index.html",
  "read/index.html",
  "map/index.html",
  "apply/index.html",
  "guided/index.html",
  "examples/index.html",
  "boundaries/index.html",
  "sources/index.html",
  "research/index.html",
  "history/index.html",
];

const assert = (condition, message) => {
  if (!condition) throw new Error(message);
};

const read = (filePath) => fs.readFileSync(filePath, "utf8");

const localLinksIn = (html) => [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map((match) => match[1]);

const idsIn = (html) => new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]));

const idListIn = (html) => [...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);

const relativeLuminance = (hex) => {
  const channels = [1, 3, 5].map((index) => Number.parseInt(hex.slice(index, index + 2), 16) / 255);
  const linear = channels.map((value) => value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4);
  return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2];
};

const contrastRatio = (first, second) => {
  const values = [relativeLuminance(first), relativeLuminance(second)].sort((a, b) => b - a);
  return (values[0] + 0.05) / (values[1] + 0.05);
};

const cssHexVariable = (css, name) => {
  const value = css.match(new RegExp(`--${name}:\\s*(#[0-9a-f]{6})`, "i"))?.[1];
  assert(value, `missing hexadecimal CSS variable: --${name}`);
  return value;
};

const checkLink = (fromFile, href) => {
  if (!href || /^(https?:|mailto:|tel:|data:|javascript:)/i.test(href)) return;
  if (href.startsWith("#")) {
    const fragment = decodeURIComponent(href.slice(1));
    assert(!fragment || idsIn(read(fromFile)).has(fragment), `${fromFile} points to missing fragment: ${href}`);
    return;
  }
  const [withoutHash, fragment = ""] = href.split("#");
  const [filePart] = withoutHash.split("?");
  if (!filePart) return;
  const target = path.resolve(path.dirname(fromFile), filePart);
  assert(target.startsWith(`${DIST_DIR}${path.sep}`), `${fromFile} escapes dist: ${href}`);
  assert(fs.existsSync(target), `${fromFile} points to missing local target: ${href}`);
  if (fragment && target.endsWith(".html")) {
    assert(idsIn(read(target)).has(decodeURIComponent(fragment)), `${fromFile} points to missing target fragment: ${href}`);
  }
};

const main = () => {
  for (const route of requiredRoutes) assert(fs.existsSync(path.join(DIST_DIR, route)), `missing built route: ${route}`);
  assert(fs.existsSync(EXPORT_PATH), "missing committed standalone export; run build first");
  const root = read(path.join(DIST_DIR, "index.html"));
  const map = read(path.join(DIST_DIR, "map/index.html"));
  const readRoute = read(path.join(DIST_DIR, "read/index.html"));
  const apply = read(path.join(DIST_DIR, "apply/index.html"));
  const guided = read(path.join(DIST_DIR, "guided/index.html"));
  const examples = read(path.join(DIST_DIR, "examples/index.html"));
  const sources = read(path.join(DIST_DIR, "sources/index.html"));
  const research = read(path.join(DIST_DIR, "research/index.html"));
  const history = read(path.join(DIST_DIR, "history/index.html"));
  const css = read(CSS_PATH);
  const headline = "AI slop often begins before the model writes a word.";
  const standfirst = "A polished answer can still feel generic when the system follows the obvious search path";
  const conceptualBridge = "This is a broad proposal about the room before the answer";
  assert(root.includes(headline), "root headline missing");
  assert(root.includes(standfirst), "root standfirst missing");
  assert(root.includes(conceptualBridge), "root conceptual-framing bridge missing");
  for (const door of ["Read the idea", "Explore the map", "Apply it"]) assert(root.indexOf(door) >= 0, `principal door missing: ${door}`);
  assert(root.includes("Take the guided read"), "optional continuous reading path missing from home");
  assert(root.includes("A QUICK EXAMPLE") && root.indexOf("A QUICK EXAMPLE") < root.indexOf("Three principal doors"), "concrete example does not arrive before the route doors");
  assert(root.includes("data-term-trigger") && root.includes("term-inline"), "first-use term help is missing visible meaning or an optional explainer");
  const termTriggerTags = [...[root, map, apply, guided].join("\n").matchAll(/<button\b[^>]*data-term-trigger[^>]*>/g)].map((match) => match[0]);
  assert(termTriggerTags.length > 0, "no contextual term triggers were rendered");
  const termTriggerNames = termTriggerTags.map((tag) => tag.match(/\baria-label="([^"]+)"/)?.[1] ?? "");
  assert(termTriggerNames.every((name) => /^Explain\s+\S/.test(name)), "a contextual term trigger lacks a descriptive accessible name");
  assert(new Set(termTriggerNames).size >= 6, "contextual term triggers do not expose distinct concept names");
  const doorEnd = root.indexOf("</nav>", root.indexOf('<nav class="door-grid"'));
  const echoIndex = root.indexOf("Echo");
  assert(doorEnd > 0 && (echoIndex < 0 || echoIndex > doorEnd), "Echo appears before principal doors");
  const firstScreen = root.slice(0, doorEnd).toLowerCase();
  for (const prohibitedClaim of ["study shows", "measured prevalence", "proven improvement", "causes the model"]) {
    assert(!firstScreen.includes(prohibitedClaim), `first screen presents conceptual framing as a result: ${prohibitedClaim}`);
  }
  const familyOrder = ["F1", "F2", "F3", "F4", "F5", "F6"].map((id) => map.indexOf(`id="family-${id}"`));
  assert(familyOrder.every((position) => position >= 0), "one or more family cards missing");
  assert(familyOrder.every((position, index) => index === 0 || position > familyOrder[index - 1]), "family card order changed");
  for (const familyName of ["Peripheral signal", "Source weighing", "Velocity / motion", "Absence + memory", "Structured patterns", "Learning loop"]) assert(map.includes(familyName), `family name missing: ${familyName}`);
  assert(!map.includes('class="relationship-connectors"'), "current map still renders detachable connector lines");
  for (const relationship of ["REQUIRES A BASELINE", "CAN REVEAL A SHARED PATH", "CONSTRAINS INFLUENCE", "MAY UPDATE AFTER AN OUTCOME"]) assert(map.includes(relationship), `map relationship band missing: ${relationship}`);
  for (const plainPurpose of [
    "Look beyond the obvious path, but treat what you find as something to inspect—not a shortcut to truth.",
    "Ask what each source can and cannot tell us about this exact claim",
    "Notice a change against a stated baseline before calling it meaningful.",
    "Notice what should be present but is not",
    "preserve important differences",
    "Compare what you expected with what happened",
  ]) assert(map.includes(plainPurpose), `plain-language family bridge missing: ${plainPurpose}`);
  assert(!/<p class="boundary"><strong>Boundary:<\/strong>\s*<\/p>/.test(map), "Map glossary contains an empty boundary");
  assert(!/<details class="glossary-item">[\s\S]*?<p><\/p>/.test(map), "Map glossary contains an empty technical meaning");
  for (const level of ["ordinary", "lightweight", "moderate", "advanced"]) assert(apply.toLowerCase().includes(level), `implementation level missing: ${level}`);
  const recommendationStart = apply.indexOf('<aside class="route-recommendation-card"');
  const recommendationEnd = apply.indexOf("</aside>", recommendationStart);
  assert(recommendationStart >= 0 && recommendationEnd > recommendationStart, "Apply planning recommendation card missing");
  const recommendationMarkup = apply.slice(recommendationStart, recommendationEnd);
  for (const eventToken of ["COMPLETE", "STOPPED_", "HUMAN_DISPOSITION_RECORDED", "LEARNING_PENDING_OUTCOME", "LEARNING_REVIEWED"]) {
    assert(!recommendationMarkup.includes(eventToken), `planning recommendation fabricates observed event state: ${eventToken}`);
  }
  for (const initialState of ["NOT_RUN", "NOT_TRIGGERED", "NOT_OBSERVED", "NOT_AVAILABLE", "NOT_RECORDED"]) assert(recommendationMarkup.includes(initialState), `initial observed state missing: ${initialState}`);
  assert(apply.includes("complete static decision guide") && apply.includes("data-route-studio"), "Apply no-script equivalent or enhanced form contract missing");
  assert(apply.includes('name="evidenceSelection"') && apply.includes("Stage 0 comes first"), "Apply does not encode the Stage 0 evidence-selection gate");
  const applyPreview = root.match(/<span class="door-preview door-preview-apply"[\s\S]*?<\/span><\/span>/)?.[0] ?? "";
  assert(applyPreview.includes("TASK CONDITIONS") && applyPreview.includes("recommendation") && applyPreview.includes("planned boundary"), "Home Apply preview does not use planning semantics");
  assert(!applyPreview.includes("DECISION BRIEF") && !applyPreview.includes("human disposition"), "Home Apply preview still implies completed records or decisions");
  for (const guidedSection of ["guided-opening", "guided-families", "guided-relations", "guided-apply", "guided-examples", "guided-boundary"]) assert(guided.includes(`id="${guidedSection}"`), `Guided route section missing: ${guidedSection}`);
  assert(guided.includes("Approximately 8–12 minutes; editorial estimate only."), "Guided route reading-time caveat missing");
  for (const example of ["specialist signal", "explicit baseline", "independence: UNKNOWN"]) assert(examples.includes(example), `teaching pattern missing: ${example}`);
  assert(examples.includes("ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION"), "Signal Foundry status missing");
  assert(examples.includes("The Echo Problem</strong> is a separate project"), "late Echo boundary missing from examples");
  assert(research.includes("UNRUN") && research.includes("NO RESULTS") && research.includes("NO PROVIDER OR MODEL SELECTED"), "research no-results status missing");
  assert(research.includes("separate project — unrun — no results"), "Echo status missing from research route");
  assert(research.includes('id="echo"'), "Echo section has no stable route fragment");
  assert(research.includes('href="../research/index.html#echo"'), "Echo source route does not target the separate Echo section");
  assert(history.includes("Historical v13 origin — not the current v16 topology."), "historical label missing");
  assert(history.includes("current relationship view"), "current/historical distinction missing");
  const metareasoningHref = 'href="https://doi.org/10.1016/0004-3702(91)90015-C"';
  assert(sources.includes(metareasoningHref), "parenthesized external URL was not preserved");
  const standalone = read(EXPORT_PATH);
  const standaloneIds = idListIn(standalone);
  assert(standaloneIds.length === new Set(standaloneIds).size, "standalone export contains duplicate IDs");
  assert((standalone.match(/<h1\b/g) ?? []).length === 1, "standalone export must contain exactly one level-one heading");
  assert((standalone.match(/<aside class="orientation-rail"/g) ?? []).length === 1, "standalone export must contain one publication rail");
  assert((standalone.match(/<details class="orientation-mobile"/g) ?? []).length === 1, "standalone export must contain one mobile route guide");
  assert((standalone.match(/<div class="page-frame"/g) ?? []).length === 1, "standalone export contains nested publication frames");
  assert(standalone.includes("<strong>All routes</strong>"), "standalone orientation must describe the complete route set");
  assert(!standalone.includes('aria-current="location"'), "standalone orientation must not falsely mark one route as current");
  const headingLevels = [...standalone.matchAll(/<h([1-6])\b/g)].map((match) => Number(match[1]));
  for (let index = 1; index < headingLevels.length; index += 1) {
    assert(headingLevels[index] <= headingLevels[index - 1] + 1, `standalone heading level jumps from h${headingLevels[index - 1]} to h${headingLevels[index]}`);
  }
  for (const section of ["home", "read", "map", "apply", "guided", "examples", "boundaries", "sources", "research", "history"]) {
    assert(standalone.includes(`<section class="standalone-section" id="${section}"`), `standalone route section missing: ${section}`);
  }
  for (const html of [sources, standalone]) {
    assert(!/<a\b[^>]*<(?:\/?em|\/?strong|\/?code)\b/i.test(html), "inline markup corrupted an anchor start tag");
    for (const match of html.matchAll(/<a href="https?:[^"]+"([^>]*)>/g)) {
      assert(match[1].includes('target="_blank"'), "external link is missing target=_blank");
      assert(match[1].includes('rel="noreferrer"'), "external link is missing rel=noreferrer");
    }
  }
  for (const token of ["STOPPED_BUDGET", "LEARNING_NOT_APPLICABLE", "NOT_AUTHORIZED_OR_AMBIGUOUS"]) {
    assert(apply.includes(token), `Apply route mutated state token: ${token}`);
    assert(standalone.includes(token), `standalone export mutated state token: ${token}`);
  }
  const signalFoundryStatus = "ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION";
  assert(examples.includes(signalFoundryStatus), "Examples route mutated Signal Foundry status");
  assert(standalone.includes(signalFoundryStatus), "standalone export mutated Signal Foundry status");
  const htmlFiles = requiredRoutes.map((route) => path.join(DIST_DIR, route));
  for (const filePath of htmlFiles) for (const href of localLinksIn(read(filePath))) checkLink(filePath, href);
  for (const href of localLinksIn(standalone)) {
    if (!href.startsWith("#")) continue;
    const fragment = decodeURIComponent(href.slice(1));
    assert(!fragment || idsIn(standalone).has(fragment), `standalone export points to missing fragment: ${href}`);
  }
  assert(!standalone.includes('href="#source-'), "standalone export contains an unresolved source fragment");
  assert(readRoute.includes('aria-current="page"'), "active principal route lacks aria-current=page");
  assert(research.includes('aria-current="page"'), "active secondary route lacks aria-current=page");
  assert(root.includes("<noscript><style>.secondary-nav-wrap { display: block; }") && root.includes(".no-script-note { display: block !important; }"), "no-script navigation or Apply fallback missing");
  assert(!/\.primary-nav\s+a\s*\{[^}]*display:\s*none/i.test(css), "mobile CSS hides principal route links");
  assert(css.includes(".no-js .term-popover-trigger") && css.includes(".no-js .reading-progress-wrap"), "no-script mode leaves optional term or progress controls visible");
  assert(/@media \(min-width: 601px\) and \(max-width: 1100px\)[\s\S]*?\.term-popover\s*\{[^}]*position:\s*static/i.test(css), "medium-width term popovers are not flow-native");
  assert(!/@media\s*\(max-width:\s*600px\)[\s\S]{0,2400}?\.route-brief\s*\{[^}]*grid-template-columns:\s*repeat\(3/i.test(css), "narrow route brief regressed to three compressed columns");
  assert(/\.primary-nav a,[^\n]*\.secondary-nav a,[^\n]*\.orientation-link,[^\n]*\.orientation-mobile > summary\s*\{\s*min-height:\s*2\.75rem/i.test(css), "route controls do not share the 44px minimum target contract");
  const paper = cssHexVariable(css, "paper");
  for (const token of ["muted", "teal", "green", "purple", "orange", "ochre", "blue"]) {
    const ratio = contrastRatio(cssHexVariable(css, token), paper);
    assert(ratio >= 4.5, `--${token} text contrast is ${ratio.toFixed(2)}:1; expected at least 4.5:1`);
  }
  assert(contrastRatio(cssHexVariable(css, "focus-dark"), paper) >= 3, "dark focus ring lacks 3:1 contrast on paper");
  assert(contrastRatio(cssHexVariable(css, "focus-light"), cssHexVariable(css, "navy")) >= 3, "light focus ring lacks 3:1 contrast on dark surfaces");
  console.log(`PASS routes: ${requiredRoutes.length}`);
  console.log("PASS exact first-screen framing, non-result boundary, and principal-door presence");
  console.log("PASS six-family order/names, implementation levels, teaching patterns");
  console.log("PASS Signal Foundry, Echo, and historical/current topology boundaries");
  console.log("PASS local route/assets link integrity");
  console.log("PASS external Markdown links preserve URLs and safe anchor attributes");
  console.log("PASS exact underscore-bearing state vocabulary and standalone fragments");
  console.log("PASS standalone heading hierarchy and unique IDs");
  console.log("PASS responsive/no-script navigation and active-route semantics");
  console.log("PASS Stage 0, descriptive term controls, mobile route brief, and medium-popover contracts");
  console.log("PASS normal-text and dual-focus contrast thresholds");
  console.log("PASS standalone export exists");
};

main();
