import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const css = read("site/src/site.css");
const homes = [
  ["review", read("site/dist/index.html")],
  ["public", read("site/public-dist/index.html")],
];

assert.match(
  css,
  /\.door-card\s*\{[^}]*grid-template-rows:\s*auto auto minmax\(0,\s*1fr\) 4\.35rem;[^}]*align-content:\s*stretch;/s,
  "door cards must reserve one equal footer track instead of distributing unequal previews with space-between",
);
assert.match(
  css,
  /\.door-preview\s*\{[^}]*min-height:\s*4\.35rem;[^}]*padding-right:\s*2\.45rem;/s,
  "every door preview must use the shared footer height and reserve the arrow lane",
);
assert.match(
  css,
  /\.preview-caption\s*\{[^}]*right:\s*2\.45rem;[^}]*bottom:\s*0\.1rem;/s,
  "absolute preview captions must end before the arrow lane",
);
assert.doesNotMatch(
  css,
  /\.door-preview-map \.preview-caption\s*\{[^}]*bottom:\s*-/s,
  "the map caption must not be pushed below its own footer",
);
assert.match(
  css,
  /\.preview-map-node:not\(:nth-of-type\(6\)\)::after\s*\{[^}]*left:\s*100%;[^}]*width:\s*calc\(0\.28rem \+ 1px\);/s,
  "the six map nodes must connect through their grid gaps",
);
assert.match(
  css,
  /\.door-preview-map \.preview-map-link\s*\{\s*display:\s*none;\s*\}/s,
  "legacy diagonal preview traces must remain hidden",
);
assert.match(
  css,
  /@media \(forced-colors: active\)[\s\S]*?\.preview-map-node::after\s*\{\s*background:\s*CanvasText;\s*\}/,
  "map-preview gap connectors must remain visible in forced-colors mode",
);
assert.match(
  css,
  /\.door-preview-apply \.preview-caption\s*\{[^}]*position:\s*static;[^}]*grid-column:\s*1 \/ -1/s,
  "the Apply caption must remain in flow below its planning rows",
);

for (const [label, html] of homes) {
  assert.equal((html.match(/class="door-card /g) ?? []).length, 3, `${label} home must render exactly three principal door cards`);
  assert.equal((html.match(/class="door-preview /g) ?? []).length, 3, `${label} home must render one preview per principal door`);
  assert.equal((html.match(/class="preview-caption"/g) ?? []).length, 3, `${label} home must render one caption per principal preview`);
  assert.equal((html.match(/class="door-arrow"/g) ?? []).length, 3, `${label} home must render one reserved arrow per principal door`);
}

console.log("PASS door-card preview footer and connector contract");
