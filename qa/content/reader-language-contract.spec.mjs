import assert from "node:assert/strict";
import fs from "node:fs";

const short = fs.readFileSync(new URL("../../manuscript/NINETY_SECOND_VERSION.md", import.meta.url), "utf8");
const build = fs.readFileSync(new URL("../../site/build.mjs", import.meta.url), "utf8");
const styles = fs.readFileSync(new URL("../../site/src/site.css", import.meta.url), "utf8");
const words = short.match(/\b[\w’'-]+\b/g) ?? [];
const normalizedShort = short.replace(/\s+/g, " ");
const shortHeading = short.match(/^#\s+(.+)$/m)?.[1] ?? "";

assert.ok(words.length >= 220 && words.length <= 250, `90-second version is ${words.length} words; expected 220–250`);
assert.equal(shortHeading, "Improve the room before the answer", "90-second heading does not lead with the human function");
for (const internalName of ["Pattern Recognition", "Discrimination Layer"]) {
  assert.equal(shortHeading.includes(internalName), false, `90-second heading exposes the internal name before ordinary-language meaning: ${internalName}`);
  assert.ok(
    short.indexOf(internalName) > short.indexOf("Those checks do not decide the answer; they improve the information available to it."),
    `90-second version names ${internalName} before explaining the human function`,
  );
}
const questions = [
  "What might the obvious path have missed?",
  "What can each source actually support?",
  "What is changing against a useful baseline?",
  "What expected information is missing, and what should memory preserve?",
  "What appears when peers, periods, structures, or origins are compared?",
  "After a defined outcome, what bounded update should be proposed?",
];
let previous = -1;
for (const question of questions) {
  const position = short.indexOf(question);
  assert.ok(position > previous, `six-family question missing or out of order: ${question}`);
  previous = position;
}
for (const boundary of [
  "candidate for inspection, not a truth signal",
  "Technical access is not permission",
  "People retain judgment and authority",
  "design proposal, not a settled empirical result",
]) {
  assert.ok(normalizedShort.includes(boundary), `reader boundary missing: ${boundary}`);
}
assert.equal(short.slice(0, short.indexOf("Its six families ask:")).toLowerCase().includes("echo"), false, "origin-accounting track displaced the broad opening");
assert.ok(build.includes("const renderGuided"), "continuous guided reading route is missing");
assert.ok(build.includes("data-term-trigger"), "interactive term-help contract is missing");
assert.ok(build.includes('aria-label="Explain ${escapeAttribute(term.label)}"'), "term triggers do not expose their concept in the accessible name");
assert.ok(build.includes("Every essential definition remains visible at first use"), "term meaning depends on an optional popover");
assert.ok(styles.includes(".no-js .term-popover-trigger") && styles.includes(".no-js .reading-progress-wrap"), "no-script mode leaves optional controls visible");
assert.match(styles, /@media \(min-width: 601px\) and \(max-width: 1100px\)[\s\S]*?\.term-popover\s*\{[^}]*position:\s*static/i, "term popovers are not flow-native at medium widths");
assert.equal(/@media\s*\(max-width:\s*600px\)[\s\S]{0,2400}?\.route-brief\s*\{[^}]*grid-template-columns:\s*repeat\(3/i.test(styles), false, "narrow route briefs use compressed columns");

console.log(`PASS reader-language contract (${words.length} words, six families, guided and accessible term-help routes)`);
