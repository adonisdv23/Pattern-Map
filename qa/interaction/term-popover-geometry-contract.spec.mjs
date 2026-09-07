import assert from "node:assert/strict";

await import(new URL("../../site/src/term-popover-geometry.js", import.meta.url));

const translate = globalThis.PatternMapTermPopoverGeometry?.translateTermPanel;
assert.equal(typeof translate, "function", "term-panel geometry API is unavailable");

const assertClearance = ({ panel, trigger, viewportWidth }) => {
  const translation = translate({ panel, trigger, viewportWidth });
  assert.ok(
    panel.left + translation.inline >= 16,
    "translated panel crosses the left viewport inset",
  );
  assert.ok(
    panel.right + translation.inline <= viewportWidth - 16,
    "translated panel crosses the right viewport inset",
  );
  assert.ok(
    panel.top + translation.block >= trigger.bottom + 8,
    "translated panel does not clear its trigger by eight pixels",
  );
  return translation;
};

// Exact pre-repair audit geometry for the first 1440px term helper.
assert.deepEqual(
  assertClearance({
    panel: { left: 249.59, right: 745.59, top: 765.29 },
    trigger: { bottom: 771.70 },
    viewportWidth: 1440,
  }),
  { inline: 0, block: 15 },
);

// Exact pre-repair right-edge geometry before the existing -26px shift.
assert.deepEqual(
  assertClearance({
    panel: { left: 953.48, right: 1449.48, top: 1048.42 },
    trigger: { bottom: 1056.18 },
    viewportWidth: 1440,
  }),
  { inline: -26, block: 16 },
);

assert.deepEqual(
  assertClearance({
    panel: { left: 4, right: 500, top: 120 },
    trigger: { bottom: 100 },
    viewportWidth: 1440,
  }),
  { inline: 12, block: 0 },
);

assert.throws(
  () => translate({ panel: {}, trigger: {}, viewportWidth: 1440 }),
  /finite numeric bounds/,
);

console.log("PASS desktop term panels clear their triggers and viewport insets");
