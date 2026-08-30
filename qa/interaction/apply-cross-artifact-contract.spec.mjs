import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../..");
const read = (relative) => fs.readFileSync(path.join(root, relative), "utf8");

await import("../../site/src/recommendation.js");
const api = globalThis.PatternMapRecommendation;

const ordinaryTemplate = read("framework/templates/ORDINARY_RECORD.md");
const quickstart = read("framework/agent-playbook/QUICKSTART.md");
const applyHtml = read("site/public-dist/apply/index.html");
const siteScript = read("site/src/site.js");

for (const phrase of ["Supplied scope", "Material assumptions", "Unchecked boundaries", "Output"]) {
  assert.match(ordinaryTemplate, new RegExp(`- ${phrase}:`));
  assert.match(applyHtml, new RegExp(phrase, "i"), `public Apply lost ordinary field ${phrase}`);
}
assert.match(ordinaryTemplate, /terminal; it is not an ANSWER, route, stop,\s*learning, or influence receipt/);
assert.match(ordinaryTemplate, /Do not add layered evidence, outcome, or\s*six-family fields/);
assert.match(quickstart, /use the ordinary path[\s\S]*supplied scope[\s\S]*material assumptions[\s\S]*unchecked boundaries[\s\S]*output[\s\S]*stop/i);

const ordinary = api.recommend({ evidenceSelection: "none" });
assert.equal(ordinary.recommendedAction, "ORDINARY_RECORD");
assert.match(ordinary.learningOption, /LEARNING_NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-action>ORDINARY_RECORD</);
assert.match(applyHtml, /four-field ordinary record/i);
assert.doesNotMatch(applyHtml.match(/<tr><th scope="row">ordinary<\/th>[\s\S]*?<\/tr>/)?.[0] ?? "", /<code>ANSWER<\/code>/);

for (const state of ["AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"]) {
  assert.match(quickstart, new RegExp(`\\b${state}\\b`));
  assert.match(applyHtml, new RegExp(`name="permission" value="${state}"`));
}
for (const stale of ['value="supplied"', 'value="restricted"', 'value="human-gate"']) {
  assert.equal(applyHtml.includes(stale), false, `public Apply retained stale permission value ${stale}`);
}
assert.match(applyHtml, /name="humanActionGate" value="NOT_REQUIRED"/);
assert.match(applyHtml, /name="humanActionGate" value="REQUIRED"/);
assert.match(applyHtml, /Permission state[\s\S]*Separate human action gate/);
assert.match(applyHtml, /data-recommendation-permission>NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-human-gate>NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-capacity>NOT_APPLICABLE/);

for (const dependent of ["consequence", "uncertainty", "budget", "permission", "humanActionGate"]) {
  assert.match(applyHtml, new RegExp(`data-stage0-dependent="${dependent}"[^>]*disabled`));
}
assert.match(siteScript, /evidenceSelection === "none"[\s\S]*?\? \{ evidenceSelection \}/);
assert.match(siteScript, /humanActionGate: fieldValue\("humanActionGate"\)/);

const substantialCapacityOnly = api.recommend({
  evidenceSelection: "needed",
  consequence: "reversible",
  uncertainty: "mixed",
  budget: "substantial",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(substantialCapacityOnly.recommendedLevel, "lightweight");
assert.equal(substantialCapacityOnly.capacityFit, "EXCEEDS_WARRANTED_SCOPE");
const insufficientCapacity = api.recommend({
  evidenceSelection: "needed",
  consequence: "consequential",
  uncertainty: "high",
  budget: "bounded",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(insufficientCapacity.recommendedLevel, "moderate");
assert.equal(insufficientCapacity.capacityFit, "NARROW_OR_ESCALATE");
assert.equal(insufficientCapacity.recommendedAction, "CLARIFY");
assert.match(`${insufficientCapacity.requiredGate} ${insufficientCapacity.plannedStopCondition}`, /narrow|capacity|resource boundary/i);
const advanced = api.recommend({
  evidenceSelection: "needed",
  consequence: "consequential",
  uncertainty: "high",
  budget: "substantial",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(advanced.recommendedLevel, "advanced");
assert.equal(advanced.capacityFit, "WITHIN_SELECTED_BOUNDARY");
assert.match(applyHtml, /consequential \+ high uncertainty \+ substantial approved capacity/);
assert.match(applyHtml, /capacity[^.]*never (?:makes Advanced appropriate|justifies it) by itself/i);
assert.match(applyHtml, /Capacity mismatch:[\s\S]*Do not silently under-scope/);

console.log("PASS Apply cross-artifact parity: ordinary exit, typed permission, human gate, and proportional Advanced trigger");
