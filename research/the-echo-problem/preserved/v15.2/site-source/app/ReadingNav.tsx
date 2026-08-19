"use client";

import { useEffect, useState } from "react";

const items = [
  { id: "start", label: "Start", route: "/", target: "" },
  { id: "stop-60-90", label: "60–90 sec", route: "/", target: "#stop-60-90" },
  { id: "stop-5", label: "About 4 min", route: "/", target: "#stop-5" },
  { id: "stop-12-15", label: "About 9 min", route: "/", target: "#stop-12-15" },
  { id: "deep-receipt", label: "Explore · receipt", route: "/explore", target: "#deep-receipt" },
  { id: "map", label: "Explore · map", route: "/explore", target: "#map" },
  { id: "mechanisms", label: "Explore · records", route: "/explore", target: "#mechanisms" },
  { id: "connections", label: "Explore · loops", route: "/explore", target: "#connections" },
  { id: "example", label: "Illustration", route: "/explore", target: "#example" },
  { id: "challenges", label: "Objections", route: "/explore", target: "#challenges" },
  { id: "cases", label: "Cases", route: "/explore", target: "#cases" },
  { id: "lab", label: "Lab · no results", route: "/lab", target: "#lab" },
  { id: "sources", label: "Sources", route: "/sources", target: "#sources" },
] as const;

export default function ReadingNav({ initialActive }: { initialActive: (typeof items)[number]["id"] }) {
  const [active, setActive] = useState<string>(initialActive);

  useEffect(() => {
    const currentPath = window.location.pathname.replace(/\/$/, "") || "/";
    const currentItems = items.filter((item) => item.route === currentPath);
    const sections = items
      .filter((item) => item.route === currentPath)
      .map((item) => document.getElementById(item.id))
      .filter((element): element is HTMLElement => Boolean(element));

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]?.target.id) setActive(visible[0].target.id);
      },
      { rootMargin: "-18% 0px -70% 0px", threshold: 0 },
    );

    sections.forEach((section) => observer.observe(section));
    const syncHash = () => {
      const hash = window.location.hash.slice(1);
      if (currentItems.some((item) => item.id === hash)) setActive(hash);
      else if (currentPath !== "/") setActive(currentItems[0]?.id ?? "start");
    };
    window.addEventListener("hashchange", syncHash);
    syncHash();
    return () => {
      observer.disconnect();
      window.removeEventListener("hashchange", syncHash);
    };
  }, []);

  return (
    <nav aria-label="Primary reading navigation">
      {items.map(({ id, label, route, target }) => (
        <a key={id} href={`${route}${target}`} aria-current={active === id ? "location" : undefined}>
          {label}
        </a>
      ))}
    </nav>
  );
}
