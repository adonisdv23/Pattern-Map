import assert from "node:assert/strict";
import fs from "node:fs";

const short = fs.readFileSync(new URL("../../manuscript/NINETY_SECOND_VERSION.md", import.meta.url), "utf8");
const build = fs.readFileSync(new URL("../../site/build.mjs", import.meta.url), "utf8");
const words = short.match(/\b[\w’'-]+\b/g) ?? [];
const normalizedShort = short.replace(/\s+/g, " ");

assert.ok(words.length >= 220 && words.length <= 250, `90-second version is ${words.length} words; expected 220–250`);
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
assert.ok(build.includes("Every essential definition remains visible at first use"), "term meaning depends on an optional popover");

console.log(`PASS reader-language contract (${words.length} words, six families, guided and term-help routes)`);
