/**
 * Pattern Map v16 — rendered layout and interaction probe.
 *
 * This file exists because a CSS-source assertion is not a layout result. The
 * repository's own evidence rules forbid presenting an inference as a
 * measurement, so responsive claims in the QA record must come from measured
 * boxes in a real engine at a real viewport size.
 *
 * Usage: paste this file into a browser console (or evaluate it through any
 * CDP-style driver) against a served route, then call:
 *
 *     patternMapLayoutProbe()            // measure the current viewport
 *     patternMapLayoutProbe({label: "821x844"})
 *
 * It never mutates the page beyond reading geometry, and it reports raw
 * numbers alongside verdicts so a reviewer can disagree with the thresholds.
 */
globalThis.patternMapLayoutProbe = (options = {}) => {
  const round = (value) => Math.round(value * 100) / 100;
  const box = (element) => {
    const rect = element.getBoundingClientRect();
    return {
      x: round(rect.x),
      y: round(rect.y + window.scrollY),
      w: round(rect.width),
      h: round(rect.height),
      right: round(rect.right),
      bottom: round(rect.bottom + window.scrollY),
    };
  };
  // Content inside a closed <details> still reports a stale bounding box in
  // Chromium, so geometry alone would report collapsed disclosures as visible
  // overflow. checkVisibility is authoritative where it exists; the closed
  // ancestor walk is the fallback for engines without it.
  const insideClosedDisclosure = (element) => {
    for (let node = element.parentElement; node; node = node.parentElement) {
      if (node.tagName === "DETAILS" && !node.open) return true;
    }
    return false;
  };
  const visible = (element) => {
    if (typeof element.checkVisibility === "function") {
      if (!element.checkVisibility({ checkVisibilityCSS: true, contentVisibilityAuto: true })) return false;
    } else {
      const style = getComputedStyle(element);
      if (style.display === "none" || style.visibility === "hidden") return false;
    }
    if (insideClosedDisclosure(element)) return false;
    const rect = element.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  };
  const describe = (element) => {
    const id = element.id ? `#${element.id}` : "";
    const cls = typeof element.className === "string" && element.className
      ? `.${element.className.trim().split(/\s+/).slice(0, 2).join(".")}`
      : "";
    return `${element.tagName.toLowerCase()}${id}${cls}`;
  };
  const all = (selector) => [...document.querySelectorAll(selector)].filter(visible);

  // Two boxes overlap only when they share area on both axes. A one-pixel
  // shared edge is tolerated because subpixel layout routinely produces it.
  const TOLERANCE = 1;
  const overlaps = (a, b) =>
    a.x < b.right - TOLERANCE &&
    b.x < a.right - TOLERANCE &&
    a.y < b.bottom - TOLERANCE &&
    b.y < a.bottom - TOLERANCE;

  const collisionsAmong = (elements) => {
    const measured = elements.map((element) => ({ name: describe(element), rect: box(element) }));
    const found = [];
    for (let i = 0; i < measured.length; i += 1) {
      for (let j = i + 1; j < measured.length; j += 1) {
        if (overlaps(measured[i].rect, measured[j].rect)) {
          found.push({ a: measured[i].name, b: measured[j].name, aRect: measured[i].rect, bRect: measured[j].rect });
        }
      }
    }
    return found;
  };

  const root = document.documentElement;
  const horizontalOverflow = round(root.scrollWidth - root.clientWidth);
  // A wide table inside its own scroll container is correct responsive
  // behaviour, not page overflow, so only elements with no clipping or
  // scrolling ancestor are counted against the page.
  const CONTAINED_OVERFLOW = new Set(["auto", "scroll", "hidden", "clip"]);
  const hasScrollContainer = (element) => {
    for (let node = element.parentElement; node && node !== root; node = node.parentElement) {
      if (CONTAINED_OVERFLOW.has(getComputedStyle(node).overflowX)) return true;
    }
    return false;
  };
  const overflowingElements = [...document.querySelectorAll("body *")]
    .filter((element) => {
      if (!visible(element)) return false;
      const rect = element.getBoundingClientRect();
      if (rect.right <= root.clientWidth + TOLERANCE && rect.left >= -TOLERANCE) return false;
      return !hasScrollContainer(element);
    })
    .slice(0, 12)
    .map((element) => ({ name: describe(element), rect: box(element) }));

  // Map regions are measured as stacked bands: each must finish before the
  // next begins, which is the property the 821–1100px cascade defect broke.
  const mapRegions = [
    [".map-start", ".map-node.map-start"],
    ["order-note", ".map-order-note"],
    ["family-grid", ".map-family-grid"],
    ["record-tray", ".map-record-tray"],
    ["relationship-bands", ".map-relationship-bands"],
    ["focus-detail", ".map-focus-detail"],
    ["text-equivalent", ".map-text-equivalent"],
  ]
    .map(([name, selector]) => {
      const element = document.querySelector(selector);
      return element && visible(element) ? { name, rect: box(element) } : null;
    })
    .filter(Boolean);

  const stackingFaults = [];
  for (let i = 1; i < mapRegions.length; i += 1) {
    const previous = mapRegions[i - 1];
    const current = mapRegions[i];
    if (current.rect.y + TOLERANCE < previous.rect.bottom) {
      stackingFaults.push({
        after: previous.name,
        before: current.name,
        previousBottom: previous.rect.bottom,
        currentTop: current.rect.y,
      });
    }
  }

  const familyNodes = all(".map-family-node");
  const familyRows = [...new Set(familyNodes.map((node) => Math.round(node.getBoundingClientRect().top)))].length;
  const familyCards = all("[data-family-card]");

  // Discrete controls carry the project's 44x44 CSS-pixel target. Inline links
  // inside running prose are excluded on purpose: inflating them would damage
  // the reading line the target is meant to protect.
  const discreteControls = all(
    "button, .door-card, .family-strip-item, .orientation-link, .example-family-return, .guided-index a, .reading-index a",
  ).filter((element) => !element.closest(".source-markdown, .reading-column, p.hero-term-line"));

  // A control inside running prose may keep a small painted box and expand its
  // hit area with an absolutely positioned pseudo-element, so the reading line
  // is not pushed open every time the control appears. The target that matters
  // is the one a finger can land on, so measure the union of the painted box
  // and any such overlay rather than the painted box alone.
  const effectiveTarget = (element) => {
    const rect = box(element);
    const overlay = getComputedStyle(element, "::after");
    if (!overlay || overlay.content === "none" || overlay.position !== "absolute") {
      return { ...rect, source: "painted box" };
    }
    const overlayWidth = parseFloat(overlay.width);
    const overlayHeight = parseFloat(overlay.height);
    if (!Number.isFinite(overlayWidth) || !Number.isFinite(overlayHeight)) {
      return { ...rect, source: "painted box" };
    }
    return {
      ...rect,
      w: round(Math.max(rect.w, overlayWidth)),
      h: round(Math.max(rect.h, overlayHeight)),
      paintedW: rect.w,
      paintedH: rect.h,
      source: "painted box expanded by an ::after overlay",
    };
  };

  const smallControls = discreteControls
    .map((element) => ({
      name: describe(element),
      text: (element.textContent || "").trim().slice(0, 40),
      rect: effectiveTarget(element),
    }))
    .filter((entry) => entry.rect.w < 44 || entry.rect.h < 44);

  const termHelp = [...document.querySelectorAll(".term-help")].map((element) => ({
    term: element.querySelector("dfn")?.textContent ?? "",
    inlineDefinitionVisible: Boolean(element.querySelector(".term-inline")) && visible(element.querySelector(".term-inline")),
    triggerPresent: Boolean(element.querySelector("[data-term-trigger]")),
    panelHidden: element.querySelector(".term-popover")?.hidden ?? null,
  }));

  const observed = {};
  for (const [key, selector] of Object.entries({
    execution: "[data-observed-execution]",
    stop: "[data-observed-stop]",
    outcome: "[data-observed-outcome]",
    learning: "[data-observed-learning]",
    human: "[data-observed-human]",
  })) {
    const element = document.querySelector(selector);
    if (element) observed[key] = element.textContent.trim();
  }

  const report = {
    probeVersion: 4,
    label: options.label ?? `${window.innerWidth}x${window.innerHeight}`,
    url: location.pathname + location.search + location.hash,
    viewport: { width: window.innerWidth, height: window.innerHeight, dpr: window.devicePixelRatio },
    documentHeight: round(root.scrollHeight),
    enhanced: root.dataset.enhanced === "true",
    horizontalOverflow,
    overflowingElements,
    map: {
      regionsMeasured: mapRegions.length,
      regions: mapRegions,
      stackingFaults,
      familyNodeCount: familyNodes.length,
      familyGridRows: familyNodes.length ? familyRows : 0,
      familyNodeCollisions: collisionsAmong(familyNodes),
      recordCollisions: collisionsAmong(all(".map-record")),
      bandCollisions: collisionsAmong(all(".relationship-band")),
      focusFieldCount: document.querySelectorAll("#map-focus-detail dl > div").length,
      textEquivalentItems: document.querySelectorAll(".map-text-equivalent ol > li").length,
      textEquivalentRelationships: document.querySelectorAll(".map-text-equivalent ul > li").length,
    },
    familyCardsVisible: familyCards.length,
    familyControlsReachable: all("[data-map-family], [data-family-focus]").length,
    smallControls,
    termHelp: {
      count: termHelp.length,
      missingInlineDefinition: termHelp.filter((entry) => !entry.inlineDefinitionVisible).map((entry) => entry.term),
      openPanelsOnLoad: termHelp.filter((entry) => entry.panelHidden === false).map((entry) => entry.term),
    },
    apply: Object.keys(observed).length ? observed : null,
  };

  report.verdict = {
    noHorizontalOverflow: horizontalOverflow <= TOLERANCE && overflowingElements.length === 0,
    noMapStackingFault: stackingFaults.length === 0,
    noNodeCollision:
      report.map.familyNodeCollisions.length === 0 &&
      report.map.recordCollisions.length === 0 &&
      report.map.bandCollisions.length === 0,
    allFamilyControlsReachable: familyNodes.length === 0 || familyNodes.length === 6,
    allDiscreteControlsMeetTarget: smallControls.length === 0,
    everyTermHasVisibleInlineDefinition: report.termHelp.missingInlineDefinition.length === 0,
    noTermPanelOpenOnLoad: report.termHelp.openPanelsOnLoad.length === 0,
    observedStateUnchanged:
      report.apply === null ||
      (observed.execution === "NOT_RUN" &&
        observed.stop === "NOT_TRIGGERED" &&
        observed.outcome === "NOT_OBSERVED" &&
        observed.learning === "NOT_AVAILABLE" &&
        observed.human === "NOT_RECORDED"),
  };
  report.pass = Object.values(report.verdict).every(Boolean);
  return report;
};
