import assert from "node:assert/strict";
import fs from "node:fs";

const build = fs.readFileSync(new URL("../../site/build.mjs", import.meta.url), "utf8");
const css = fs.readFileSync(new URL("../../site/src/site.css", import.meta.url), "utf8");

assert.equal(build.includes('class="relationship-connectors"'), false, "current map must not render detachable connector lines");
assert.equal(/@media\s*\(min-width:\s*821px\)[\s\S]{0,500}\.map-family-grid\s*\{\s*top:/m.test(css), false, "late desktop coordinates can collide with tablet layout");
assert.match(css, /@media\s*\(min-width:\s*601px\)\s*and\s*\(max-width:\s*1100px\)/, "medium-width map contract is missing");
assert.match(css, /@media\s*\(max-width:\s*600px\)[\s\S]*\.map-family-grid[^}]*grid-template-columns:\s*1fr/m, "narrow map must reflow to one column");

for (const phrase of [
  "No required starting order",
  "REQUIRES A BASELINE",
  "CAN REVEAL A SHARED PATH",
  "CONSTRAINS INFLUENCE",
  "MAY UPDATE AFTER AN OUTCOME",
]) {
  assert.ok(build.includes(phrase), `map relationship meaning missing: ${phrase}`);
}

for (const field of ["question", "inputs", "comparison", "record", "boundary", "connections"]) {
  assert.ok(build.includes(`data-map-focus-${field}`), `map focus field missing: ${field}`);
}

console.log("PASS line-free map semantics and wide/medium/narrow layout contracts");
