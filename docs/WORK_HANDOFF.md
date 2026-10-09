# Work handoff
Copy this folder into a new repository or the repository owning Swarm Court review state. First inspect its AGENTS.md and reuse existing identity, event, review and persistence components.

REPLACE_AT_WORK: authenticated identity/roles; Swarm Court node identifiers; approved data connector and query limits; evidence ACL/version invalidation; Dreamcatcher manifest/routes; approved experiment system; runner cancellation/metering if agents are introduced.

This package is a single-user, loopback-only synthetic prototype. Display names are audit labels, not authenticated identities. No empirical ingestion, manufacturing action, source write, waiver, cloud deployment or production approval is implemented. A synthetic-ready receipt only means the synthetic workflow passed. Empirical requirements deliberately stay blocked.

Before a work pilot: replace local audit identities with SSO, enforce per-resource permissions on every endpoint/export, integrate approved read-only evidence snapshots, validate process-specific probe criteria with owners, move persistence to the approved store if required, and perform multi-user/security review. Keep shadow mode and human ownership.

The full research proposal is a roadmap, not a claim that all listed features are implemented. See README for delivered scope and omissions.
