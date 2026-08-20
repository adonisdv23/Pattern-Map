/**
 * Pattern Map v16 — enhancement, focus, and fallback probe.
 *
 * Companion to `layout-probe.js`. This one exercises behaviour rather than
 * geometry: focus order, focus indicators, the term-help contract, the
 * no-script fallback, and the print cascade.
 *
 * Two honesty boundaries are built into the report rather than left to prose:
 *
 *   - `focusOrder` inspects the sequential focus set and moves focus
 *     programmatically. It is not a physical keyboard traversal, and the
 *     report says so in `method`.
 *   - `printSimulation` applies the stylesheet's own `@media print` rules in
 *     screen context. It is not a browser print preview, and the report says
 *     so in `method`.
 *
 * Usage: evaluate this file against a served route, then call
 * `patternMapEnhancementProbe()`. It restores everything it changes.
 */
globalThis.patternMapEnhancementProbe = () => {
  const root = document.documentElement;
  const round = (value) => Math.round(value * 100) / 100;
  const describe = (element) => {
    const id = element.id ? `#${element.id}` : "";
    const cls = typeof element.className === "string" && element.className
      ? `.${element.className.trim().split(/\s+/).slice(0, 2).join(".")}`
      : "";
    return `${element.tagName.toLowerCase()}${id}${cls}`;
  };
  const rendered = (element) =>
    typeof element.checkVisibility === "function"
      ? element.checkVisibility({ checkVisibilityCSS: true, contentVisibilityAuto: true })
      : getComputedStyle(element).display !== "none";

  // ---- focus order -------------------------------------------------------
  const FOCUSABLE =
    'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), summary, details > summary, [tabindex]:not([tabindex="-1"])';
  const focusable = [...document.querySelectorAll(FOCUSABLE)].filter(rendered);
  const positiveTabindex = focusable
    .filter((element) => Number(element.getAttribute("tabindex")) > 0)
    .map(describe);
  const focusableHiddenFromView = [...document.querySelectorAll(FOCUSABLE)]
    .filter((element) => !rendered(element))
    .length;

  // Chromium does not apply :focus-visible to script-driven focus, so a
  // computed-style read alone would report every control as unindicated. Where
  // the pseudo-class does not engage, the check falls back to asking whether a
  // :focus-visible rule in the page's own stylesheets actually selects this
  // element and declares a visible indicator.
  const focusVisibleRules = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try {
      rules = sheet.cssRules;
    } catch {
      continue;
    }
    const collect = (list) => {
      for (const rule of list) {
        if (rule.cssRules) collect(rule.cssRules);
        if (!rule.selectorText || !rule.selectorText.includes(":focus-visible")) continue;
        const declaresIndicator =
          (rule.style.outlineStyle && rule.style.outlineStyle !== "none") ||
          rule.style.outline ||
          rule.style.boxShadow ||
          rule.style.textDecoration ||
          rule.style.borderColor ||
          rule.style.backgroundColor;
        if (!declaresIndicator) continue;
        for (const selector of rule.selectorText.split(",")) {
          const bare = selector.replaceAll(":focus-visible", "").trim();
          if (bare) focusVisibleRules.push(bare);
        }
      }
    };
    collect(rules);
  }
  const declaredIndicatorFor = (element) =>
    focusVisibleRules.find((selector) => {
      try {
        return element.matches(selector);
      } catch {
        return false;
      }
    });

  const previousFocus = document.activeElement;
  const indicatorFailures = [];
  let indicatorsFromLiveStyle = 0;
  let indicatorsFromDeclaredRule = 0;
  const sampled = focusable.filter((_, index) => index % Math.max(1, Math.ceil(focusable.length / 40)) === 0);
  for (const element of sampled) {
    element.focus({ preventScroll: true });
    const style = getComputedStyle(element);
    const outlineWidth = parseFloat(style.outlineWidth) || 0;
    const liveIndicator =
      (outlineWidth > 0 && style.outlineStyle !== "none") ||
      style.boxShadow !== "none" ||
      style.textDecorationLine.includes("underline");
    if (liveIndicator) {
      indicatorsFromLiveStyle += 1;
      continue;
    }
    const declared = declaredIndicatorFor(element);
    if (declared) {
      indicatorsFromDeclaredRule += 1;
      continue;
    }
    indicatorFailures.push({ element: describe(element), outline: style.outline, boxShadow: style.boxShadow });
  }
  if (previousFocus instanceof HTMLElement) previousFocus.focus({ preventScroll: true });
  else document.activeElement?.blur?.();

  // ---- family focus must not steal the caret -----------------------------
  let familyFocusStealsCaret = null;
  const firstFamilyControl = document.querySelector("[data-map-family], [data-family-focus]");
  if (firstFamilyControl) {
    firstFamilyControl.focus({ preventScroll: true });
    firstFamilyControl.click();
    familyFocusStealsCaret = document.activeElement !== firstFamilyControl;
    firstFamilyControl.click();
  }

  // ---- term help ---------------------------------------------------------
  const termTrigger = document.querySelector("[data-term-trigger]");
  let termContract = null;
  if (termTrigger) {
    const panel = document.getElementById(termTrigger.getAttribute("aria-controls"));
    const inline = termTrigger.closest(".term-help")?.querySelector(".term-inline");
    const hiddenBefore = panel?.hidden;
    termTrigger.click();
    const openedByClick = panel?.hidden === false && termTrigger.getAttribute("aria-expanded") === "true";
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    const closedByEscape = panel?.hidden === true && termTrigger.getAttribute("aria-expanded") === "false";
    const focusReturned = document.activeElement === termTrigger;
    termContract = {
      inlineDefinitionRenderedWithoutOpening: Boolean(inline) && rendered(inline),
      panelHiddenOnLoad: hiddenBefore === true,
      openedByClick,
      closedByEscape,
      focusReturnedToTrigger: focusReturned,
      panelIsInFlow: panel ? getComputedStyle(panel).position !== "fixed" : null,
    };
  }

  // ---- no-script fallback -------------------------------------------------
  const enhancedBefore = root.dataset.enhanced === "true";
  const classesBefore = root.className;
  root.className = "no-js";
  const studio = document.querySelector("[data-route-studio]");
  const recommendation = document.querySelector("[data-route-recommendation]");
  const staticGuide = document.querySelector(".static-route-equivalent");
  const noScriptNote = document.querySelector(".no-script-note");
  const anyTermTrigger = document.querySelector("[data-term-trigger]");
  const noScript = {
    studioPresent: Boolean(studio),
    studioRenderedWithoutScript: studio ? rendered(studio) : null,
    recommendationRenderedWithoutScript: recommendation ? rendered(recommendation) : null,
    staticGuideRenderedWithoutScript: staticGuide ? rendered(staticGuide) : null,
    noScriptNoteRenderedWithoutScript: noScriptNote ? rendered(noScriptNote) : null,
    termTriggerRenderedWithoutScript: anyTermTrigger ? rendered(anyTermTrigger) : null,
    familyCardsStillRendered: [...document.querySelectorAll("[data-family-card]")].filter(rendered).length,
    mapTextEquivalentStillRendered: rendered(document.querySelector(".map-text-equivalent") ?? document.body),
  };
  root.className = classesBefore;

  // ---- print cascade -------------------------------------------------------
  const printRules = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try {
      rules = sheet.cssRules;
    } catch {
      continue;
    }
    for (const rule of rules) {
      if (rule.type === CSSRule.MEDIA_RULE && rule.conditionText.includes("print")) {
        for (const inner of rule.cssRules) printRules.push(inner.cssText);
      }
    }
  }
  const printStyle = document.createElement("style");
  printStyle.textContent = printRules.join("\n");
  document.head.append(printStyle);
  const printSimulation = {
    method: "stylesheet @media print rules applied in screen context; not a browser print preview",
    ruleCount: printRules.length,
    mapTextEquivalentPrinted: rendered(document.querySelector(".map-text-equivalent") ?? document.body),
    mapFamilyNodesPrinted: [...document.querySelectorAll(".map-family-node")].filter(rendered).length,
    staticGuidePrinted: staticGuide ? rendered(staticGuide) : null,
    orientationRailPrinted: rendered(document.querySelector(".orientation-rail") ?? document.createElement("div")),
    horizontalOverflowUnderPrintRules: round(root.scrollWidth - root.clientWidth),
  };
  printStyle.remove();

  // ---- colour is not the only carrier of family identity -------------------
  const familyIdentity = [...document.querySelectorAll("[data-family-card], [data-map-family]")].map((element) => ({
    family: element.dataset.familyCard ?? element.dataset.mapFamily,
    hasTextIdentifier: /F[1-6]/.test(element.textContent ?? ""),
  }));

  const report = {
    probe: "enhancement",
    probeVersion: 2,
    url: location.pathname + location.search + location.hash,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    enhancedFlagSet: enhancedBefore,
    focusOrder: {
      method: "sequential focusable set in DOM order, focus moved programmatically; not a physical keyboard traversal",
      focusableCount: focusable.length,
      sampledForIndicator: sampled.length,
      focusVisibleRuleCount: focusVisibleRules.length,
      indicatorsFromLiveStyle,
      indicatorsFromDeclaredRule,
      positiveTabindex,
      focusableButNotRendered: focusableHiddenFromView,
      indicatorFailures,
    },
    familyFocusStealsCaret,
    termContract,
    noScript,
    printSimulation,
    familyIdentityWithoutColour: {
      checked: familyIdentity.length,
      missingTextIdentifier: familyIdentity.filter((entry) => !entry.hasTextIdentifier).map((entry) => entry.family),
    },
  };

  report.verdict = {
    noPositiveTabindex: positiveTabindex.length === 0,
    everySampledControlShowsAFocusIndicator: indicatorFailures.length === 0,
    familyFocusKeepsCaret: familyFocusStealsCaret === null || familyFocusStealsCaret === false,
    termInlineMeaningIndependentOfPopover: !termContract || termContract.inlineDefinitionRenderedWithoutOpening,
    termPopoverClosedOnLoad: !termContract || termContract.panelHiddenOnLoad,
    termPopoverOpensAndEscapeCloses: !termContract || (termContract.openedByClick && termContract.closedByEscape),
    termFocusReturns: !termContract || termContract.focusReturnedToTrigger,
    noDeadStudioWithoutScript: !noScript.studioPresent || noScript.studioRenderedWithoutScript === false,
    staticGuideSurvivesWithoutScript: !noScript.studioPresent || noScript.staticGuideRenderedWithoutScript === true,
    termTriggerHiddenWithoutScript: noScript.termTriggerRenderedWithoutScript !== true,
    printKeepsMapMeaning:
      printSimulation.mapTextEquivalentPrinted !== false || document.querySelector(".map-text-equivalent") === null,
    printDropsNavigationChrome: printSimulation.orientationRailPrinted === false,
    familyIdentityNeverColourOnly: report.familyIdentityWithoutColour.missingTextIdentifier.length === 0,
  };
  report.pass = Object.values(report.verdict).every(Boolean);
  return report;
};
