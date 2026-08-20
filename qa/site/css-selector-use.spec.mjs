/**
 * Dead-selector guard for the local site stylesheet.
 *
 * Motivation: the round-one correction removed the absolutely positioned map
 * nodes but left their rules behind. One of those orphans, `.map-route`, still
 * matched — because `map-route` is also the class on the whole Map page
 * section. The result was a 2px navy border and a pale panel wrapped around
 * the entire route. Source review and the passing contract checks both missed
 * it, because nothing was checking that a rule still describes something real.
 *
 * This check compares every class selector in `site/src/site.css` against the
 * classes that actually appear in the generated pages, allowing for classes the
 * site's own JavaScript adds at runtime. A class that no rule can reach is
 * dead weight; worse, it can silently start matching something else.
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const css = fs.readFileSync(path.join(ROOT, "site", "src", "site.css"), "utf8");
const script = fs.readFileSync(path.join(ROOT, "site", "src", "site.js"), "utf8");
const distDir = path.join(ROOT, "site", "dist");

const htmlFiles = [];
const walk = (dir) => {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.name.endsWith(".html")) htmlFiles.push(full);
  }
};
assert.ok(fs.existsSync(distDir), "run `npm run build` in site/ before this check");
walk(distDir);
// The standalone export composes the same components into one document and can
// legitimately carry classes the routed pages do not.
const standalone = path.join(ROOT, "site", "exports", "standalone", "pattern-map-v16.html");
if (fs.existsSync(standalone)) htmlFiles.push(standalone);
assert.ok(htmlFiles.length > 0, "no generated pages found to check selectors against");

const renderedClasses = new Set();
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  for (const match of html.matchAll(/class="([^"]*)"/g)) {
    for (const name of match[1].trim().split(/\s+/)) if (name) renderedClasses.add(name);
  }
}

// Classes the page never carries in markup because JavaScript applies them.
const runtimeClasses = new Set(["js", "no-js"]);
for (const match of script.matchAll(/classList\.(?:add|remove|toggle)\(\s*["'`]([\w-]+)["'`]/g)) {
  runtimeClasses.add(match[1]);
}
for (const match of script.matchAll(/classList\.toggle\(\s*["'`]([\w-]+)["'`]/g)) {
  runtimeClasses.add(match[1]);
}

// Strip declaration blocks and at-rule preludes so only selectors remain.
const selectorText = css
  .replace(/\/\*[\s\S]*?\*\//g, " ")
  .replace(/\{[^{}]*\}/g, "{}")
  .replace(/@media[^{]*/g, " ")
  .replace(/@supports[^{]*/g, " ");

const referenced = new Map();
for (const match of selectorText.matchAll(/\.(-?[_a-zA-Z][\w-]*)/g)) {
  const name = match[1];
  if (!referenced.has(name)) referenced.set(name, 0);
  referenced.set(name, referenced.get(name) + 1);
}

const unreachable = [...referenced.keys()]
  .filter((name) => !renderedClasses.has(name) && !runtimeClasses.has(name))
  .sort();

assert.deepEqual(
  unreachable,
  [],
  `stylesheet rules target classes that no generated page contains: ${unreachable.join(", ")}. ` +
    "Remove the rule, or restore the markup it was written for. A rule kept past the markup it described " +
    "is how `.map-route` ended up styling the entire Map page.",
);

// The specific collision that motivated this check: route-section classes are
// layout groupings, and no rule may give one of them a node-like decoration.
const ROUTE_SECTION_CLASSES = [
  "map-route",
  "apply-route",
  "reading-route",
  "guided-route",
  "examples-route",
  "boundaries-route",
  "sources-route",
  "research-route",
  "history-route",
];
for (const routeClass of ROUTE_SECTION_CLASSES) {
  const solitaryRule = new RegExp(`(^|[,{}])\\s*\\.${routeClass}\\s*\\{([^}]*)\\}`, "g");
  for (const match of css.matchAll(solitaryRule)) {
    const declarations = match[2];
    assert.ok(
      !/\bborder\s*:\s*[^;]*\d/.test(declarations) && !/\bbackground\s*:\s*#|\bbackground-color\s*:/.test(declarations),
      `.${routeClass} is a whole-page section; a rule gives it a node-level border or background: ${declarations.trim()}`,
    );
  }
}

console.log(
  `PASS stylesheet selector reachability (${referenced.size} classes referenced, ${renderedClasses.size} rendered, ${runtimeClasses.size} runtime)`,
);
