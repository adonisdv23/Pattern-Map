"use client";

import { type CSSProperties, useEffect, useRef } from "react";

type TermProps = {
  id: string;
  children: React.ReactNode;
  label?: string;
  definition: string;
  example?: string;
  boundary?: string;
};

/**
 * A nonmodal, progressively disclosed explanation using the native Popover API.
 * The target and content are present in server HTML, work without hydration,
 * enter the top layer without clipping, and close on Escape or light dismiss.
 */
export default function Term({ id, children, label, definition, example, boundary }: TermProps) {
  const triggerRef = useRef<HTMLButtonElement>(null);
  const popoverRef = useRef<HTMLSpanElement>(null);
  const restoreAfterNativeDismiss = useRef(false);
  const visibleLabel = label ?? (typeof children === "string" ? children : "Term explanation");
  const popoverId = `term-${id}`;
  const headingId = `${popoverId}-heading`;
  const descriptionId = `${popoverId}-description`;
  const anchorName = `--${popoverId.replace(/[^a-zA-Z0-9_-]/g, "-")}`;
  const anchorStyle = { "--term-anchor": anchorName } as CSSProperties;

  const restoreTriggerFocus = () => {
    requestAnimationFrame(() => triggerRef.current?.focus());
  };

  useEffect(() => {
    const panel = popoverRef.current;
    if (!panel) return;

    const beforeToggle = (event: Event) => {
      const nextState = (event as Event & { newState?: string }).newState;
      if (nextState === "closed") {
        restoreAfterNativeDismiss.current = panel.contains(document.activeElement);
      }
    };
    const afterToggle = (event: Event) => {
      const nextState = (event as Event & { newState?: string }).newState;
      if (nextState === "closed" && restoreAfterNativeDismiss.current) {
        restoreAfterNativeDismiss.current = false;
        restoreTriggerFocus();
      }
    };

    panel.addEventListener("beforetoggle", beforeToggle);
    panel.addEventListener("toggle", afterToggle);
    return () => {
      panel.removeEventListener("beforetoggle", beforeToggle);
      panel.removeEventListener("toggle", afterToggle);
    };
  }, []);

  return (
    <span className="term-wrap">
      <button
        ref={triggerRef}
        className="term-trigger"
        type="button"
        style={anchorStyle}
        aria-label={`Explain ${visibleLabel}`}
        popoverTarget={popoverId}
        popoverTargetAction="toggle"
      >
        {children}
      </button>
      <span
        ref={popoverRef}
        className="term-popover"
        style={anchorStyle}
        id={popoverId}
        popover="auto"
        role="region"
        aria-labelledby={headingId}
        aria-describedby={descriptionId}
      >
        <span className="term-popover-head">
          <strong id={headingId} role="heading" aria-level={3}>{visibleLabel}</strong>
          <button
            className="term-close"
            type="button"
            aria-label={`Close ${visibleLabel} explanation`}
            popoverTarget={popoverId}
            popoverTargetAction="hide"
            onClick={restoreTriggerFocus}
          >
            ×
          </button>
        </span>
        <span className="term-description" id={descriptionId}>
          <span className="term-definition">{definition}</span>
          {example && <span className="term-example"><strong>Example:</strong> {example}</span>}
          {boundary && <span className="term-boundary"><strong>What it does not mean:</strong> {boundary}</span>}
        </span>
      </span>
    </span>
  );
}
