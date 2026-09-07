import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const css = read("site/src/site.css");
const publicHome = read("site/public-dist/index.html");
const reviewHome = read("site/dist/index.html");

assert.match(
  css,
  /\.mode-public \.primary-nav\s*\{\s*gap:\s*0\.6rem;\s*\}/,
  "public navigation must have a readable wide-screen separation",
);
assert.match(
  css,
  /@media \(max-width: 480px\)[\s\S]*?\.mode-public \.primary-nav\s*\{\s*gap:\s*0\.18rem;\s*\}/,
  "public navigation must retain a fit-preserving narrow-screen separation",
);
assert.doesNotMatch(
  css,
  /\.mode-review \.primary-nav/,
  "review mode should keep its existing navigation density rather than inherit a public-only selector",
);

for (const [label, html, mode] of [["public", publicHome, "public"], ["review", reviewHome, "review"]]) {
  assert.match(html, new RegExp(`data-presentation-mode="${mode}"`), `${label} home mode marker is missing`);
  for (const [route, href] of [["Read the idea", "read/index.html#read-idea"], ["Explore the map", "map/index.html#map"], ["Apply it", "apply/index.html#apply"]]) {
    assert.match(html, new RegExp(`href="${href}"[^>]*>${route}</a>`), `${label} home lost principal route ${route}`);
  }
}

console.log("PASS public-only nav spacing contract at wide and narrow CSS breakpoints");
