export const PUBLICATION_CONFIG_SCHEMA = "pattern-map.publication-config.v1";
export const PUBLICATION_RELEASE_STATUS = "READY_FOR_AUTHORIZED_RELEASE";
export const REQUIRED_RELEASE_FIELDS = ["author_name", "canonical_url", "social_image_url", "social_image_alt"];

export const isAbsoluteHttpsUrl = (value) => {
  if (typeof value !== "string" || !value || value !== value.trim() || /[\u0000-\u0020\u007f]/.test(value)) return false;
  try {
    const parsed = new URL(value);
    return parsed.protocol === "https:"
      && Boolean(parsed.hostname)
      && /[a-z0-9:]/i.test(parsed.hostname)
      && !parsed.username
      && !parsed.password;
  } catch {
    return false;
  }
};

export const normalizedCanonicalBaseUrl = (value) => {
  if (!isAbsoluteHttpsUrl(value)) return null;
  const parsed = new URL(value);
  if (parsed.search || parsed.hash) return null;
  parsed.pathname = `${parsed.pathname.replace(/\/+$/, "")}/`;
  return parsed.href;
};

export const resolveCanonicalRouteUrl = (canonicalBase, routePath = "") => {
  const normalizedBase = normalizedCanonicalBaseUrl(canonicalBase);
  if (!normalizedBase) return null;
  const relativeRoute = String(routePath).replace(/^\/+/, "");
  return new URL(relativeRoute, normalizedBase).href;
};

export const publicationReleaseErrors = (config) => {
  const errors = [];
  if (!config || config.schema_version !== PUBLICATION_CONFIG_SCHEMA) {
    errors.push(`schema_version must be ${PUBLICATION_CONFIG_SCHEMA}`);
  }
  if (config?.status !== PUBLICATION_RELEASE_STATUS) {
    errors.push(`status must be ${PUBLICATION_RELEASE_STATUS}`);
  }
  for (const field of REQUIRED_RELEASE_FIELDS) {
    if (typeof config?.[field] !== "string" || !config[field].trim()) errors.push(`${field} is unset`);
  }
  if (typeof config?.canonical_url === "string" && config.canonical_url.trim() && !normalizedCanonicalBaseUrl(config.canonical_url)) {
    errors.push("canonical_url must be an absolute https base URL with a nonempty host, no whitespace or user information, and no query or fragment");
  }
  if (typeof config?.social_image_url === "string" && config.social_image_url.trim() && !isAbsoluteHttpsUrl(config.social_image_url)) {
    errors.push("social_image_url must be an absolute https URL with a nonempty host, no whitespace, and no user information");
  }
  return errors;
};

export const publicationReleaseReady = (config) => publicationReleaseErrors(config).length === 0;

export const publicationMetadataEnabled = (config, releaseRequested) =>
  Boolean(releaseRequested) && publicationReleaseReady(config);

export const assertPublicationReleaseConfig = (config) => {
  const errors = publicationReleaseErrors(config);
  if (errors.length) throw new Error(`Public release is gated: ${errors.join("; ")}`);
};
