export const PUBLICATION_CONFIG_SCHEMA = "pattern-map.publication-config.v1";
export const PUBLICATION_RELEASE_STATUS = "READY_FOR_AUTHORIZED_RELEASE";
export const REQUIRED_RELEASE_FIELDS = ["author_name", "canonical_url", "social_image_url", "social_image_alt"];

const RESERVED_DOMAIN_SUFFIXES = [
  ".localhost", ".local", ".test", ".invalid", ".example",
  ".internal", ".home.arpa",
];
const RESERVED_EXAMPLE_DOMAINS = new Set(["example.com", "example.net", "example.org"]);

const isPublicIpv4 = (hostname) => {
  if (!/^\d{1,3}(?:\.\d{1,3}){3}$/.test(hostname)) return null;
  const octets = hostname.split(".").map(Number);
  if (octets.some((octet) => octet < 0 || octet > 255)) return false;
  const [a, b, c, d] = octets;
  if (a === 0 || a === 10 || a === 127 || a >= 224) return false;
  if (a === 100 && b >= 64 && b <= 127) return false;
  if (a === 169 && b === 254) return false;
  if (a === 172 && b >= 16 && b <= 31) return false;
  if (a === 192 && b === 168) return false;
  if (a === 192 && b === 0 && (c === 0 || c === 2)) return false;
  if (a === 198 && (b === 18 || b === 19 || (b === 51 && c === 100))) return false;
  if (a === 203 && b === 0 && c === 113) return false;
  if (a === 255 && b === 255 && c === 255 && d === 255) return false;
  return true;
};

export const isPublicReleaseHost = (value) => {
  if (typeof value !== "string" || !value) return false;
  const hostname = value.toLowerCase().replace(/^\[|\]$/g, "").replace(/\.$/, "");
  if (!hostname || hostname === "localhost") return false;

  const ipv4 = isPublicIpv4(hostname);
  if (ipv4 !== null) return ipv4;

  if (hostname.includes(":")) {
    if (hostname === "::" || hostname === "::1" || hostname.startsWith("::ffff:")) return false;
    const first = hostname.split(":").find(Boolean) ?? "0";
    const firstValue = Number.parseInt(first, 16);
    if (!Number.isFinite(firstValue)) return false;
    if ((firstValue & 0xfe00) === 0xfc00) return false;
    if ((firstValue & 0xffc0) === 0xfe80) return false;
    if ((firstValue & 0xff00) === 0xff00) return false;
    if (hostname.startsWith("2001:db8:")) return false;
    return true;
  }

  if (!hostname.includes(".") || hostname.split(".").some((label) => !label)) return false;
  if (RESERVED_DOMAIN_SUFFIXES.some((suffix) => hostname.endsWith(suffix))) return false;
  if ([...RESERVED_EXAMPLE_DOMAINS].some((domain) => hostname === domain || hostname.endsWith(`.${domain}`))) return false;
  return true;
};

export const isAbsoluteHttpsUrl = (value) => {
  if (typeof value !== "string" || !value || value !== value.trim() || /[\u0000-\u0020\u007f]/.test(value)) return false;
  try {
    const parsed = new URL(value);
    return parsed.protocol === "https:"
      && Boolean(parsed.hostname)
      && /[a-z0-9:]/i.test(parsed.hostname)
      && isPublicReleaseHost(parsed.hostname)
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
    errors.push("canonical_url must be an absolute https base URL with a syntactically public host, no whitespace or user information, and no query or fragment");
  }
  if (typeof config?.social_image_url === "string" && config.social_image_url.trim() && !isAbsoluteHttpsUrl(config.social_image_url)) {
    errors.push("social_image_url must be an absolute https URL with a syntactically public host, no whitespace, and no user information");
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
