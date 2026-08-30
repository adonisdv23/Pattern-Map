(() => {
  document.querySelectorAll("[data-progressive-static-guide]").forEach((guide) => {
    guide.open = false;
  });

  const familyGrid = document.querySelector(".family-grid");
  const focusStatus = document.querySelector("#family-focus-status");
  const familyCards = [...document.querySelectorAll("[data-family-card]")];
  const focusButtons = [...document.querySelectorAll("[data-family-focus]")];
  const mapStage = document.querySelector("[data-map-stage]");
  const mapButtons = [...document.querySelectorAll("[data-map-family]")];
  const clearButton = document.querySelector("[data-family-clear]");
  const mapFocusTitle = document.querySelector("[data-map-focus-title]");
  const mapFocusQuestion = document.querySelector("[data-map-focus-question]");
  const mapFocusInputs = document.querySelector("[data-map-focus-inputs]");
  const mapFocusComparison = document.querySelector("[data-map-focus-comparison]");
  const mapFocusRecord = document.querySelector("[data-map-focus-record]");
  const mapFocusBoundary = document.querySelector("[data-map-focus-boundary]");
  const mapFocusConnections = document.querySelector("[data-map-focus-connections]");
  const mapFocusStatus = document.querySelector("[data-map-focus-status]");

  const mapButtonFor = (family) => mapButtons.find((button) => button.dataset.mapFamily === family);
  const cardFor = (family) => familyCards.find((card) => card.dataset.familyCard === family);

  const clearFamilyFocus = (announce = true) => {
    familyGrid?.classList.remove("has-focus");
    mapStage?.classList.remove("has-map-focus");
    if (mapStage) delete mapStage.dataset.activeFamily;
    familyCards.forEach((card) => card.classList.remove("is-focused"));
    focusButtons.forEach((button) => button.setAttribute("aria-pressed", "false"));
    mapButtons.forEach((button) => {
      button.setAttribute("aria-pressed", "false");
      button.classList.remove("is-selected");
    });
    if (mapFocusTitle) mapFocusTitle.textContent = "All six families remain in view.";
    if (mapFocusQuestion) mapFocusQuestion.textContent = "Choose a family to inspect it. Focus adds emphasis; it never hides essential meaning.";
    if (mapFocusInputs) mapFocusInputs.textContent = "decision, permission, evidence, baselines, gaps, comparisons, or observed outcomes";
    if (mapFocusComparison) mapFocusComparison.textContent = "the comparison changes with the family; no single score governs the map";
    if (mapFocusRecord) mapFocusRecord.textContent = "records are created only when the task warrants them";
    if (mapFocusBoundary) mapFocusBoundary.textContent = "unknown relations stay unknown; candidates do not become truth by status";
    if (mapFocusConnections) mapFocusConnections.textContent = "baseline, common-origin, influence-gate, and conditional-learning relationships remain explicit";
    if (mapFocusStatus) mapFocusStatus.textContent = "All six families are available for comparison.";
    if (announce && focusStatus) focusStatus.textContent = "All six families are visible. Focus controls add emphasis; they never hide essential meaning.";
  };

  const focusFamily = (family, sourceButton) => {
    const card = cardFor(family);
    const mapButton = mapButtonFor(family);
    if (!card || !mapButton) return;
    const alreadyFocused = card.classList.contains("is-focused");
    clearFamilyFocus(false);
    if (alreadyFocused) {
      if (focusStatus) focusStatus.textContent = "All six families are visible. Focus controls add emphasis; they never hide essential meaning.";
      return;
    }
    familyGrid?.classList.add("has-focus");
    mapStage?.classList.add("has-map-focus");
    if (mapStage) mapStage.dataset.activeFamily = family;
    card.classList.add("is-focused");
    focusButtons.find((button) => button.dataset.familyFocus === family)?.setAttribute("aria-pressed", "true");
    mapButtons.forEach((button) => {
      const selected = button === mapButton;
      button.setAttribute("aria-pressed", String(selected));
      button.classList.toggle("is-selected", selected);
    });

    if (mapFocusTitle) mapFocusTitle.textContent = `${mapButton.dataset.mapFamily} · ${mapButton.dataset.mapName}`;
    if (mapFocusQuestion) mapFocusQuestion.textContent = mapButton.dataset.mapQuestion;
    if (mapFocusInputs) mapFocusInputs.textContent = mapButton.dataset.mapInputs;
    if (mapFocusComparison) mapFocusComparison.textContent = mapButton.dataset.mapComparison;
    if (mapFocusRecord) mapFocusRecord.textContent = mapButton.dataset.mapRecords;
    if (mapFocusBoundary) mapFocusBoundary.textContent = mapButton.dataset.mapBoundary;
    if (mapFocusConnections) mapFocusConnections.textContent = mapButton.dataset.mapConnections;
    if (mapFocusStatus) mapFocusStatus.textContent = `${family} is focused. Question, inputs, comparison, record, boundary, and connections are shown separately.`;
    if (focusStatus) focusStatus.textContent = `${family} is focused. The other families remain visible for comparison.`;
    sourceButton?.setAttribute("aria-pressed", "true");
  };

  focusButtons.forEach((button) => {
    button.addEventListener("click", () => focusFamily(button.dataset.familyFocus, button));
  });
  mapButtons.forEach((button) => {
    button.addEventListener("click", () => focusFamily(button.dataset.mapFamily, button));
  });
  clearButton?.addEventListener("click", () => clearFamilyFocus());

  const moreButton = document.querySelector(".nav-more");
  const secondary = document.querySelector(".secondary-nav-wrap");
  const setMoreOpen = (isOpen, moveFocus = false) => {
    moreButton?.setAttribute("aria-expanded", String(isOpen));
    secondary?.classList.toggle("is-open", isOpen);
    if (isOpen && moveFocus) secondary?.querySelector("a")?.focus();
  };
  moreButton?.addEventListener("click", () => {
    const isOpen = moreButton.getAttribute("aria-expanded") === "true";
    setMoreOpen(!isOpen, !isOpen);
  });

  const termTriggers = [...document.querySelectorAll("[data-term-trigger]")];
  const positionTermPanel = (trigger, panel) => {
    if (!trigger || !panel) return;
    panel.style.removeProperty("--term-popover-shift");
    panel.style.removeProperty("--term-popover-block-shift");
    if (!window.matchMedia("(min-width: 1101px)").matches) return;
    const geometry = globalThis.PatternMapTermPopoverGeometry?.translateTermPanel;
    if (!geometry) return;
    const translation = geometry({
      panel: panel.getBoundingClientRect(),
      trigger: trigger.getBoundingClientRect(),
      viewportWidth: window.innerWidth,
    });
    panel.style.setProperty("--term-popover-shift", `${translation.inline}px`);
    panel.style.setProperty("--term-popover-block-shift", `${translation.block}px`);
  };
  const closeTerm = (trigger, restoreFocus = false) => {
    const panel = trigger?.getAttribute("aria-controls")
      ? document.getElementById(trigger.getAttribute("aria-controls"))
      : null;
    trigger?.setAttribute("aria-expanded", "false");
    if (panel) {
      panel.hidden = true;
      panel.style.removeProperty("--term-popover-shift");
      panel.style.removeProperty("--term-popover-block-shift");
    }
    if (restoreFocus) trigger?.focus();
  };
  const closeOtherTerms = (except) => {
    termTriggers.forEach((trigger) => {
      if (trigger !== except && trigger.getAttribute("aria-expanded") === "true") closeTerm(trigger);
    });
  };
  termTriggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const panel = document.getElementById(trigger.getAttribute("aria-controls"));
      if (!panel) return;
      const opening = trigger.getAttribute("aria-expanded") !== "true";
      closeOtherTerms(trigger);
      trigger.setAttribute("aria-expanded", String(opening));
      panel.hidden = !opening;
      if (opening) positionTermPanel(trigger, panel);
    });
  });

  window.addEventListener("resize", () => {
    const openTrigger = termTriggers.find((trigger) => trigger.getAttribute("aria-expanded") === "true");
    if (!openTrigger) return;
    positionTermPanel(
      openTrigger,
      document.getElementById(openTrigger.getAttribute("aria-controls")),
    );
  });

  document.addEventListener("click", (event) => {
    if (event.target.closest?.("[data-term-help]")) return;
    closeOtherTerms(null);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    const openTerm = termTriggers.find((trigger) => trigger.getAttribute("aria-expanded") === "true");
    if (openTerm) {
      closeTerm(openTerm, true);
      return;
    }
    if (moreButton?.getAttribute("aria-expanded") === "true") {
      setMoreOpen(false);
      moreButton.focus();
    }
  });

  const readingRoutes = [...document.querySelectorAll("[data-reading-route]")];
  readingRoutes.forEach((route) => {
    const readingSections = [...route.querySelectorAll("[data-reading-section]")];
    const readingLinks = [...route.querySelectorAll("[data-reading-link]")];
    const progress = route.querySelector("[data-reading-progress]");
    const progressValue = route.querySelector("[data-reading-progress-value]");
    if (!readingSections.length) return;
    const setReadingActive = (id) => {
      readingLinks.forEach((link) => {
        const active = link.getAttribute("href") === `#${id}`;
        link.classList.toggle("is-current", active);
        if (active) link.setAttribute("aria-current", "location");
        else link.removeAttribute("aria-current");
      });
    };
    const updateReadingProgress = () => {
      if (!progress) return;
      const start = route.getBoundingClientRect().top + window.scrollY;
      const end = start + route.scrollHeight - window.innerHeight;
      const percent = end <= start ? 100 : Math.max(0, Math.min(100, ((window.scrollY - start) / (end - start)) * 100));
      progress.querySelector("span")?.style.setProperty("width", `${percent}%`);
      progress.setAttribute("aria-valuenow", String(Math.round(percent)));
      progress.setAttribute("aria-valuetext", `${Math.round(percent)} percent of this reading path`);
      if (progressValue) progressValue.textContent = `${Math.round(percent)}%`;
    };
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver((entries) => {
        const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]?.target.id) setReadingActive(visible[0].target.id);
      }, { rootMargin: "-18% 0px -68% 0px", threshold: 0 });
      readingSections.forEach((section) => observer.observe(section));
    }
    window.addEventListener("scroll", updateReadingProgress, { passive: true });
    window.addEventListener("resize", updateReadingProgress);
    updateReadingProgress();
  });

  const routeStudio = document.querySelector("[data-route-studio]");
  const recommendationCard = document.querySelector("[data-route-recommendation]");
  if (routeStudio && recommendationCard) {
    const recommendationApi = globalThis.PatternMapRecommendation;
    if (!recommendationApi?.recommend || !recommendationApi?.INITIAL_OBSERVED_STATE) return;

    const fieldValue = (name) => routeStudio.querySelector(`input[name="${name}"]:checked`)?.value ?? "";
    const setCardText = (selector, value) => {
      const element = recommendationCard.querySelector(selector);
      if (element) element.textContent = value;
    };
    const stageZeroStatus = routeStudio.querySelector("[data-stage0-status]");
    const stageZeroDependent = [...routeStudio.querySelectorAll("[data-stage0-dependent]")];
    const ordinaryDefaults = Object.freeze({ consequence: "reversible", uncertainty: "low", budget: "quick" });
    const syncStageZeroApplicability = () => {
      const ordinary = fieldValue("evidenceSelection") === "none";
      if (ordinary) {
        for (const [name, value] of Object.entries(ordinaryDefaults)) {
          const input = routeStudio.querySelector(`input[name="${name}"][value="${value}"]`);
          if (input) input.checked = true;
        }
      }
      stageZeroDependent.forEach((fieldset) => {
        fieldset.disabled = ordinary;
        fieldset.dataset.applicability = ordinary ? "not-applicable" : "active";
      });
      if (stageZeroStatus) {
        stageZeroStatus.textContent = ordinary
          ? "Consequence, uncertainty, and evidence-route budget are not applicable while Stage 0 remains supplied-material only."
          : "Evidence selection is in scope. Choose consequence, uncertainty, and an evidence-route budget before building the recommendation.";
      }
    };
    const renderObservedState = () => {
      const observed = recommendationApi.INITIAL_OBSERVED_STATE;
      setCardText("[data-observed-execution]", observed.executionState);
      setCardText("[data-observed-stop]", observed.stopOutcome);
      setCardText("[data-observed-outcome]", observed.outcomeState);
      setCardText("[data-observed-learning]", observed.learningReview);
      setCardText("[data-observed-human]", observed.humanDisposition);
    };
    const resetSimulation = () => {
      setCardText("[data-simulation-state]", "NOT_SIMULATED");
      setCardText("[data-simulation-reason]", "Use the controls only to inspect example state changes. They do not record a real person, run, stop, or outcome.");
      setCardText("[data-simulation-time]", "NOT_RECORDED");
      recommendationCard.dataset.simulation = "none";
    };
    const renderRecommendation = () => {
      let plan;
      try {
        plan = recommendationApi.recommend({
          evidenceSelection: fieldValue("evidenceSelection"),
          consequence: fieldValue("consequence"),
          uncertainty: fieldValue("uncertainty"),
          budget: fieldValue("budget"),
          permission: fieldValue("permission"),
        });
      } catch {
        setCardText("[data-recommendation-status]", "Choose one valid option in all five groups before building a recommendation.");
        return;
      }
      setCardText("[data-recommendation-level]", plan.recommendedLevel);
      setCardText("[data-recommendation-title]", plan.title);
      setCardText("[data-recommendation-summary]", plan.summary);
      setCardText("[data-recommendation-action]", plan.recommendedAction);
      setCardText("[data-recommendation-gate]", plan.requiredGate);
      setCardText("[data-recommendation-stop]", plan.plannedStopCondition);
      setCardText("[data-recommendation-learning]", plan.learningOption);
      setCardText("[data-recommendation-status]", `${plan.recommendedLevel} route recommendation built; no execution or human decision has been recorded.`);
      recommendationCard.dataset.level = plan.recommendedLevel;
      renderObservedState();
      resetSimulation();
    };

    routeStudio.addEventListener("submit", (event) => {
      event.preventDefault();
      syncStageZeroApplicability();
      renderRecommendation();
    });
    routeStudio.querySelectorAll('input[name="evidenceSelection"]').forEach((input) => {
      input.addEventListener("change", () => {
        syncStageZeroApplicability();
        renderRecommendation();
      });
    });
    routeStudio.querySelector("[data-route-reset]")?.addEventListener("click", () => {
      routeStudio.reset();
      syncStageZeroApplicability();
      renderRecommendation();
    });
    recommendationCard.querySelectorAll("[data-simulation-action]").forEach((button) => {
      button.addEventListener("click", () => {
        const action = button.dataset.simulationAction;
        if (action === "reset") {
          resetSimulation();
          setCardText("[data-recommendation-status]", "Simulation reset; observed state remains not run and not observed.");
          return;
        }
        const details = {
          hold: {
            state: "SIMULATED_HOLD",
            reason: "Example only: a person pauses influence pending review. This is not a real human disposition.",
          },
          clarify: {
            state: "SIMULATED_CLARIFICATION_RECEIVED",
            reason: "Example only: clarification is supplied for reconsideration. It does not itself grant permission.",
          },
        }[action];
        if (!details) return;
        setCardText("[data-simulation-state]", details.state);
        setCardText("[data-simulation-reason]", details.reason);
        setCardText("[data-simulation-time]", new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" }));
        setCardText("[data-recommendation-status]", `${details.state} displayed as a local simulation; observed state remains unchanged.`);
        recommendationCard.dataset.simulation = action;
      });
    });
    syncStageZeroApplicability();
    renderRecommendation();
  }

  document.documentElement.classList.remove("no-js");
  document.documentElement.classList.add("js");
  document.documentElement.dataset.enhanced = "true";
})();
