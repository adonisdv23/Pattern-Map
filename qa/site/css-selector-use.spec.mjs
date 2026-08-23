/**
 * Keep the authored stylesheet aligned with the generated site.
 *
 * This is deliberately a reachability check, not a style preference check:
 * selectors for a removed coordinate system can remain syntactically valid
 * while silently styling a later component with the same class name. The
 * generated routes and standalone export are the source of truth for classes
 * rendered today; classes added by site.js are included as runtime allowances.
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const css = fs.readFileSync(path.join(ROOT, "site", "src", "site.css"), "utf8");
const script = fs.readFileSync(path.join(ROOT, "site", "src", "site.js"), "utf8");
const distDir = path.join(ROOT, "site", "dist");
const standalonePath = path.join(ROOT, "site", "exports", "standalone", "pattern-map-v16.html");

assert.ok(fs.existsSync(distDir), "run `npm run build` in site/ before this check");

const htmlFiles = [];
const walk = (directory) => {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(fullPath);
    else if (entry.name.endsWith(".html")) htmlFiles.push(fullPath);
  }
};
walk(distDir);
if (fs.existsSync(standalonePath)) htmlFiles.push(standalonePath);
assert.ok(htmlFiles.length > 0, "no generated pages found to check stylesheet selectors");

const renderedClasses = new Set();
for (const filePath of htmlFiles) {
  const html = fs.readFileSync(filePath, "utf8");
  for (const match of html.matchAll(/class="([^"]*)"/g)) {
    for (const name of match[1].trim().split(/\s+/)) if (name) renderedClasses.add(name);
  }
}

const runtimeClasses = new Set(["js", "no-js"]);
for (const match of script.matchAll(/classList\.(?:add|remove|toggle)\(\s*["'`]([\w-]+)["'`]/g)) {
  runtimeClasses.add(match[1]);
}

// Remove comments and declaration blocks, leaving selector text. This is
// intentionally conservative: a false positive makes a stale selector
// visible for review; it does not delete anything automatically.
const selectorText = css
  .replace(/\/\*[\s\S]*?\*\//g, " ")
  .replace(/\{[^{}]*\}/g, "{}")
  .replace(/@(?:media|supports|container)[^{]*/g, " ");

const referencedClasses = new Map();
for (const match of selectorText.matchAll(/\.(-?[_a-zA-Z][\w-]*)/g)) {
  const name = match[1];
  referencedClasses.set(name, (referencedClasses.get(name) ?? 0) + 1);
}

const unreachable = [...referencedClasses.keys()]
  .filter((name) => !renderedClasses.has(name) && !runtimeClasses.has(name))
  .sort();

assert.deepEqual(
  unreachable,
  [],
  `stylesheet selectors target classes absent from generated markup/runtime state: ${unreachable.join(", ")}`,
);

// The Map is a normal-flow relationship view. No current map geometry may
// carry fixed coordinates or absolute positioning back into the stylesheet.
const mapGeometrySelectors = [
  ".map-canvas",
  ".map-node",
  ".map-start",
  ".map-family-grid",
  ".map-family-node",
  ".map-record-row",
  ".map-record-tray",
  ".map-relationship-bands",
  ".relationship-band",
];
const hasFixedCoordinate = (declarations) => [...declarations.matchAll(/(?:^|;)\s*(top|right|bottom|left)\s*:\s*([^;}]*)/g)]
  .some((match) => match[2].trim() !== "auto");
for (const selector of mapGeometrySelectors) {
  for (const match of css.matchAll(new RegExp(`\\${selector}\\s*\\{([^}]*)\\}`, "g"))) {
    const declarations = match[1];
    assert.equal(/position\s*:\s*absolute/.test(declarations), false, `${selector} must stay in normal flow`);
    assert.equal(hasFixedCoordinate(declarations), false, `${selector} must not carry fixed coordinates`);
  }
}

console.log(`PASS stylesheet selector reachability (${referencedClasses.size} classes, ${renderedClasses.size} rendered, ${runtimeClasses.size} runtime)`);
