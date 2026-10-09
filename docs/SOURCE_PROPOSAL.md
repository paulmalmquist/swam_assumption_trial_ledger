# Paul OS App Scout — October 8, 2026

## Daily card — Swarm Assumption Trial Ledger

**One-sentence benefit:** Turn consequential swarm recommendations into owned, falsifiable assumptions with the smallest safe validation trial, then preserve positive, negative, and inconclusive outcomes for reuse.

**Work problem:** A polished Paul OS recommendation can hide the premises that must be true for it to work. Those premises may be implicit, stale, unmeasured, or supported only by simulation. When a trial fails, the failure and exact conditions can disappear into chat or a ticket, causing another agent to repeat it.

**How it augments Paul OS:** Add an assumption/trial card to Swarm Court nodes. Every material recommendation can bind versioned claims, evidence, uncertainty, expiry, a named owner, and an approved probe. Dreamcatcher shows the assumption graph and trial queue. Markdown, skills, plans, governed analytics, and the actual source systems remain authoritative.

**Why now:** Latent Space's October 8 Periodic Labs interview makes the mechanism explicit: intelligence is not enough; conjectures must meet physical experiments, noisy measurements require replicates and multimodal evidence, and negative results plus full process lineage are valuable data. The October 3 Cognitive Revolution robotics interview adds that multi-step reliability compounds and that retry-tolerant and irreversible tasks need different policies. Noam Brown's September 17 discussion cautions that one spectacular data point is not a methodical ablation. These are speaker claims and design cues, not proof that this app will improve Relativity decisions. [Latent Space](https://www.latent.space/p/periodic) · [The Cognitive Revolution](https://www.cognitiverevolution.ai/one-brain-any-body-google-deepmind-s-keerthana-on-gemini-robotics-2-cross-embodiment-humanoids/) · [Dwarkesh](https://www.dwarkesh.com/p/noam-brown)

**Estimated effort:** **1–3 engineering days** for a portable synthetic demo; **1–2 weeks** for a read-only work pilot after repository, identity, runner, context-index, governed BigQuery, and Dreamcatcher inventory. These are unvalidated planning estimates.

**Single success metric:** **Unsupported-promotion escape rate** on a frozen held-out case set: recommendations incorrectly marked eligible for promotion while at least one required assumption is refuted, expired, inconclusive, or untested, divided by all cases that should be blocked. Report false-block rate and reviewer minutes as guardrails.

**Recommendation:** Extend the repository that owns Swarm Court node state and review routing. Use the slug `paulos-swarm-assumption-trial-ledger` only for an isolated portable module if inventory finds a real ownership or deployment boundary. The unresolved inventory check is whether Paul OS already has stable assumption IDs, falsifier/probe contracts, negative-result capture, and promotion gates—not merely evidence links or checklists.

**Why a thin extension beats configuration alone:** A Markdown checklist can ask for assumptions, but it cannot reliably maintain claim/probe/result identity across runs, enforce expiry and prerequisite states, deduplicate previously attempted trials, preserve null results with exact conditions, or replay promotion policy. Reuse existing experiment tracking, evidence receipts, approvals, and queues if they already cover these functions; implement only the missing joins and review surface.

---

## Idea manifest

```yaml
idea_id: paulos-app-2026-10-08-swarm-assumption-trial-ledger
title: Swarm Assumption Trial Ledger
repository_slug: paulos-swarm-assumption-trial-ledger
state: proposed
type: extension
proposal_date: 2026-10-08
timezone: America/New_York
proposal_file: PaulOS-Podcast-App-2026-10-08-paulos-swarm-assumption-trial-ledger.md
research_mode: fresh_release_synthesis
primary_metric: unsupported_promotion_escape_rate
metric_guardrails:
  - false_block_rate
  - median_reviewer_minutes
  - forbidden_side_effect_count
default_mode: offline_synthetic
work_pilot_mode: read_only_shadow
portable_data: synthetic_only
portable_external_writes: forbidden
default_model_calls: 0
authoritative_content: existing_markdown_skills_plans_and_work_systems
persistence: reuse_existing_approved_store_or_sqlite
supabase: forbidden
demo_estimate: 1-3 engineering days
pilot_estimate: 1-2 weeks after inventory
estimate_status: unvalidated
github_publication: separately_authorized
deployment: separately_authorized
```

---

# BUILD PROMPT — give this entire section to Claude Code or Codex

You are the implementation agent for Paul Malmquist, Principal #DATA Architect at Relativity Space. Build the smallest verifiable **Swarm Assumption Trial Ledger** extension described below. This document is a proposal: every repository path, adapter, endpoint, runner, deployment, model entitlement, and work integration must be discovered. Do not invent company paths, credentials, APIs, data, provider prices, or concurrency allowances.

## 1. Stable identity and constraints

```yaml
idea_id: paulos-app-2026-10-08-swarm-assumption-trial-ledger
title: Swarm Assumption Trial Ledger
repository_slug: paulos-swarm-assumption-trial-ledger
state: proposed
type: extension
source_proposal: PaulOS-Podcast-App-2026-10-08-paulos-swarm-assumption-trial-ledger.md
primary_metric: unsupported_promotion_escape_rate
default_mode: shadow
portable_demo: synthetic_only
```

Build an evidence-linked ledger that makes the assumptions behind a Paul OS recommendation explicit, plans the smallest safe probe that could disconfirm each material assumption, records the result and conditions, and deterministically decides whether the recommendation is eligible for human promotion review. It must preserve negative and inconclusive results. It must not autonomously authorize a manufacturing, quality, safety, financial, personnel, production, or source-system action.

Hard constraints:

- Extend Paul OS, Swarm Court, and Dreamcatcher; do not replace them.
- Keep original Markdown, skills, plans, code, governed definitions, and work systems authoritative. The ledger stores projections and receipts with immutable references and hashes.
- No Supabase. Prefer existing approved persistence; otherwise use SQLite for the portable demo.
- Company context, real identifiers, credentials, connectors, and work data stay inside the approved work environment. Portable fixtures are synthetic.
- Discover the approved local Claude/Codex runner and its actual authentication, usage, timeout, cancellation, and concurrency behavior. A Work/Claude subscription does not establish API credits or unlimited parallel execution. Do not invent prices.
- Use deterministic code for schemas, hashes, state transitions, prerequisite evaluation, policy gates, metrics, replay, and exports. Use an agent only to draft or explain a claim/probe where semantic judgment is necessary, and validate its output against a strict schema.
- Agent agreement, a fluent rationale, a passing simulation, or a model-generated confidence number is never treated as empirical support.
- Portable mode performs no external writes. Work pilot starts read-only and shadow-only.

## 2. First action: inspect and reuse before coding

Before any implementation edit:

1. Find and read every applicable `AGENTS.md` from the workspace root to the proposed edit path.
2. Inspect accessible Paul OS, Swarm Court, Dreamcatcher, skills, Markdown, configs, schemas, tests, dependency locks, deployment files, and existing plan/run records.
3. Search for existing stable run/entity/node IDs, evidence receipts, assumption or risk registers, experiment/DOE tracking, evaluation datasets, feature flags, approvals, queues, outcomes, observability, replay, promotions, and rollback receipts.
4. Inspect relevant prior proposals if present: Counterfactual Workbench, Regression Forge, Confidence Gate, Evidence Invalidation Queue, Convergence Governor, and Change Collision Radar. Do not assume proposals were implemented.
5. Run the smallest safe existing help/test command and record the baseline.
6. Write `docs/WORK_HANDOFF.md` and `docs/INVENTORY.md` before integration coding. Include discovered paths, APIs, reusable modules, ownership, access limits, gaps, and the recommended repository placement. Mark unresolved bindings `REPLACE_AT_WORK`.
7. Prefer: (a) a module in the repository owning Swarm Court node/review state; then (b) a Dreamcatcher app package if that is the discovered UI boundary; create a new repository only if a demonstrated ownership, dependency, or deployment boundary requires it.
8. If work access is absent, continue. Build and verify the complete portable synthetic demo behind adapters and leave concrete work discovery tasks.

Do not modify unrelated dirty work. Do not deploy, publish a GitHub repository, open a pull request, or change work configuration without Paul's separate destination and authorization.

## 3. Objective, user, example, metric, and baseline

### Objective

Given a versioned recommendation, its evidence, and its intended action, produce a reviewable set of material assumptions; bind each to an owner, scope, expiry, falsifier, and validation trial; record trial observations and outcomes; and issue a deterministic promotion-readiness receipt.

### Intended user

Paul is the primary operator. Secondary users are the engineering, data, manufacturing, quality, and operations owners who can validate assumptions and approve trials. The first work pilot must have one willing process/metric owner and one explicitly authorized read-only decision workflow.

### Example input → workflow → concrete output

Use a synthetic governed-manufacturing analytics scenario:

**Input:** A Swarm Court node recommends prioritizing an additional inspection for a synthetic batch because a temperature excursion appears associated with later failures.

The recommendation depends on three assumptions:

1. the temperature reading is correctly aligned to the batch and operation;
2. the apparent relationship remains after accounting for material lot and machine configuration;
3. the proposed inspection can detect the relevant failure mode without changing acceptance requirements.

**Workflow:**

1. Parse an approved recommendation Markdown file and create stable claim records.
2. Link each claim to evidence, owner, scope, risk tier, expiry, and a machine-checkable falsifier.
3. Generate candidate probes deterministically from registered templates where possible; optionally use an agent to draft a probe explanation, never to approve it.
4. Score candidate probes using configured, visible fields: coverage of required claims, reversibility, allowed data access, estimated elapsed time, resource class, and information value label. Do not invent causal effect sizes or costs.
5. A named human approves one probe or records a justified waiver. The portable demo uses a synthetic offline trial.
6. Ingest observations with exact dataset/config/instrument versions and negative controls. Evaluate the predeclared criterion.
7. Mark each claim `supported`, `refuted`, `inconclusive`, `expired`, or `waived`; recompute the recommendation state.
8. Export a compact evidence packet linked to the Swarm Court node. No production write or physical actuation occurs.

**Concrete output:**

```json
{
  "recommendation_id": "rec_demo_0008",
  "recommendation_version": 1,
  "readiness": "blocked",
  "owner_ref": "owner_synthetic_quality",
  "required_claims": [
    {
      "claim_id": "claim_alignment_001",
      "state": "supported",
      "result_id": "result_alignment_001"
    },
    {
      "claim_id": "claim_confounding_002",
      "state": "inconclusive",
      "result_id": "result_matched_cohort_002"
    },
    {
      "claim_id": "claim_detection_003",
      "state": "untested",
      "result_id": null
    }
  ],
  "blocking_reasons": [
    "required_claim_inconclusive:claim_confounding_002",
    "required_claim_untested:claim_detection_003"
  ],
  "next_safe_action": "review_probe_probe_detection_003",
  "policy_version": "demo-policy-v1",
  "evidence_refs": ["fixture://batch-telemetry-v3", "fixture://inspection-outcomes-v2"]
}
```

### Primary metric

```text
unsupported_promotion_escape_rate =
  recommendations_incorrectly_marked_eligible /
  all_recommendations_that_should_be_blocked
```

For the frozen held-out set, a recommendation should be blocked if a required claim is refuted, expired, inconclusive without an approved policy exception, untested, missing current authorization, or backed by an invalid result. A crash, timeout, partial record, or missing prerequisite on such a case counts as an escape.

Always report numerator, denominator, case-set version, policy version, and a Wilson interval. Guardrails: false-block rate on fully supported cases, median reviewer minutes, duplicate-trial rate, and forbidden-side-effect count. A zero-escape policy that blocks everything fails the false-block guardrail.

### Baselines

Discover actual work behavior. Portable evaluation must compare:

1. `rationale_present`: any non-empty recommendation rationale passes;
2. `evidence_link_present`: at least one evidence reference passes;
3. `required_checkbox`: all manually checked assumptions pass;
4. `candidate_ledger`: the proposed versioned claim/trial policy.

All baselines receive the same cases and permissions. Freeze rules before running held-out cases. Do not describe a synthetic baseline as Paul's current workflow.

### Falsifiable product hypothesis

On the held-out synthetic set, the candidate ledger will reduce unsupported-promotion escapes relative to the strongest applicable baseline without exceeding the predeclared false-block and reviewer-time guardrails. This is a testable hypothesis, not a promised improvement.

## 4. Source-to-feature rationale

| Source observation | Evidence status | Proposed feature | What must be measured |
|---|---|---|---|
| Periodic Labs, Latent Space, Oct. 8: conjectures require experiments; physical observations are noisy, incomplete, and sometimes inconsistent across machines | Guest account in publisher transcript | Claims have falsifiers, replicates, instrument/config versions, uncertainty, and explicit inconclusive state | Seeded noisy/ambiguous cases never become silently supported |
| Periodic Labs, Oct. 8: negative controls, null results, and the whole process lineage are valuable | Guest account in publisher transcript | Preserve trial attempts, conditions, null results, negative controls, and process lineage | Duplicate-trial rate and recovery of prior negative results |
| Cognitive Revolution, Oct. 3: reliability compounds across multi-step physical tasks; retry-tolerant and irreversible failures differ | Guest account in publisher-labeled automatic transcript | Risk tiers, reversibility field, retry policy, and fail-closed promotion gate | Irreversible/high-risk seeded cases require stronger evidence and never auto-promote |
| Dwarkesh, Sep. 17: a spectacular result is one data point; methodical ablation is expensive but necessary | Guest account in publisher transcript | Baseline, comparison group, frozen criterion, and explicit single-case limitation | Single anecdotes cannot satisfy multi-case trial contracts |
| ThursdAI, page labeled Oct. 9 but accessible Oct. 8 New York time: 722 manuscripts create a verification burden | Publisher show notes, not counted as transcript inspection | Queue, prioritization, and bounded review packet | Reviewer throughput without lowering evidence requirements |
| JSON Schema 2020-12 | Primary specification | Strict versioned records and validation errors | Malformed cases fail deterministically |
| SQLite transactions, foreign keys, and WAL documentation | Primary technical documentation | Portable append-only inbox, normalized state, and outbox | Crash/replay yields no duplicate applied transitions |
| This proposal | Unvalidated design | State machine, policy, UI, fixtures, metrics | Held-out evaluation decides whether a work pilot is justified |

Podcast statements motivate the mechanism; they do not validate this implementation or establish transfer to aerospace manufacturing. A null result is not proof that a claim can never be true. A supported claim is scoped to its recorded conditions and expiry.

## 5. Tight MVP scope and non-goals

### MVP

- Import/create one recommendation and 1–8 claims.
- Require each material claim to have scope, owner, importance, falsifier, expiry, and evidence references.
- Create candidate probes from versioned templates; allow an optional agent-drafted description behind strict validation.
- Human-approve, reject, or waive a probe with reason and expiry.
- Run deterministic synthetic probes and ingest work results through an adapter.
- Record observations, negative controls, uncertainty, missing data, and outcome.
- Recompute claim and recommendation states deterministically.
- Search prior trials by claim fingerprint and scoped conditions.
- Show exact blockers, ball-in-court owner, and links to evidence, code, plans, and source Markdown.
- Replay all events and export a promotion-readiness packet without applying a work change.

### Non-goals

- A replacement for Swarm Court, Paul OS, Dreamcatcher, MES, QMS, PLM, OpenMetadata, BigQuery, a laboratory information system, or an experiment platform.
- Automatic experiment design for arbitrary science.
- Autonomous physical experiments, manufacturing control, disposition, release, acceptance, certification, or source-system write-back.
- Causal inference from observational data without a declared identification strategy and owner review.
- Treating simulations as empirical outcomes.
- Training or fine-tuning a model.
- A universal truth engine, agent-voting system, or generic risk register.
- Uploading company data to a portable demo or personal service.

## 6. Screens and interactions

Reuse the established dark/purple Paul OS visual language if available. Every visual element must correspond to real state. Support keyboard navigation and reduced motion.

1. **Trial inbox** — filter by owner, recommendation, risk, due/expiry, state, and work node. Show the ball in court and exact blocking reason.
2. **Recommendation map** — recommendation at the center; required/optional claim nodes; evidence, probe, and result edges; links to plan/code/Markdown. No decorative graph animation.
3. **Claim editor/review** — statement, scope, type, owner, required flag, falsifier, expiry, prior related trials, and evidence. Draft claims are never authoritative.
4. **Probe planner** — compare up to five candidate probes by claim coverage, reversibility, elapsed-time class, resource class, authorization requirements, and uncertainty. All estimates are labeled.
5. **Trial run/results** — predeclared criterion, observations, controls, missingness, config versions, deviations, and outcome. Preserve raw allowed evidence references; never copy restricted payloads into the UI cache.
6. **Promotion receipt** — `eligible`, `blocked`, or `manual_exception_required`; exact rule evaluations; owner; evidence; policy/config versions; rollback target; export only.
7. **Replay/evaluation lab** — baseline versus candidate results on synthetic cases with the primary metric and guardrails.

## 7. Proposed architecture

Reuse the discovered stack. If an isolated demo is required, use a small Python service and CLI, SQLite, local JSON/Markdown fixtures, and the existing front-end framework if one is present. If no front-end framework exists, a minimal React/TypeScript UI is acceptable. Pin dependencies and make the offline demo run after installation with no model credentials or network access.

Components:

- `RecommendationAdapter`: reads authoritative Markdown/Swarm Court nodes; writes no source changes in MVP.
- `ClaimRegistry`: validates and fingerprints scoped claims.
- `EvidenceResolver`: stores references, content hashes, versions, authorization metadata, and freshness—not copied restricted payloads.
- `ProbeTemplateRegistry`: deterministic templates for join validation, matched-cohort check, schema/data-quality check, replay test, negative control, and owner attestation.
- `ProbePlanner`: validates prerequisites and produces a ranked, explainable candidate list. Ranking is deterministic configuration; an agent may only draft prose.
- `TrialRunnerAdapter`: runs the synthetic fixture or submits/observes an approved work trial.
- `OutcomeEvaluator`: applies the frozen result criterion and records `supported`, `refuted`, or `inconclusive`.
- `ReadinessPolicy`: evaluates required claims, expiry, permissions, waivers, and result validity.
- `ProjectionStore`: durable append-only events plus query projections.
- `ReplayEngine`: rebuilds state from events and verifies decision hashes.
- `ExportAdapter`: writes Markdown/JSON evidence packets to an approved location only after user action; portable mode writes locally.

Suggested event flow:

```text
recommendation.imported
  -> claim.drafted
  -> claim.reviewed
  -> probe.proposed
  -> probe.approved | probe.rejected | claim.waived
  -> trial.queued
  -> trial.started
  -> observation.recorded*
  -> trial.completed | trial.failed | trial.cancelled
  -> claim.supported | claim.refuted | claim.inconclusive
  -> recommendation.readiness_evaluated
  -> export.created
```

## 8. Explicit schemas

Implement JSON Schema files under `schemas/` and migrations under `migrations/`. Use opaque stable IDs (UUIDv7/ULID or the discovered house standard). Timestamps are UTC RFC 3339 with timezone preserved in display. Nullable is not zero or false.

### Recommendation

```json
{
  "recommendation_id": "rec_...",
  "version": 1,
  "source_ref": "markdown://...",
  "source_hash": "sha256:...",
  "node_ref": "swarm-court://...",
  "title": "Prioritize synthetic inspection",
  "intended_action_class": "read_only_advisory",
  "owner_ref": "owner_...",
  "risk_tier": "low|medium|high|prohibited",
  "created_at": "...",
  "config_version": "..."
}
```

### Claim

```json
{
  "claim_id": "claim_...",
  "recommendation_id": "rec_...",
  "version": 1,
  "statement": "Temperature signal is aligned to the batch operation",
  "claim_type": "identity|measurement|causal|constraint|capability|policy|economic|schedule",
  "scope": {"entity_type": "synthetic_batch", "population_ref": "fixture://...", "time_window": "..."},
  "required": true,
  "owner_ref": "owner_...",
  "falsifier": {"criterion": "join_mismatch_rate > 0", "evaluator_ref": "evaluator://join-v1"},
  "evidence_refs": ["fixture://..."],
  "uncertainty": {"status": "unknown", "notes": null},
  "expires_at": "...",
  "fingerprint": "sha256:...",
  "state": "draft|pending_review|untested|supported|refuted|inconclusive|expired|waived"
}
```

### Probe

```json
{
  "probe_id": "probe_...",
  "version": 1,
  "claim_ids": ["claim_..."],
  "template_ref": "probe-template://matched-cohort-v1",
  "hypothesis": "...",
  "predeclared_result_criterion": "...",
  "negative_controls": ["..."],
  "required_inputs": ["..."],
  "allowed_data_classes": ["synthetic"],
  "reversibility": "reversible|partially_reversible|irreversible",
  "elapsed_time_class": "minutes|hours|days|unknown",
  "resource_class": "local_cpu|approved_query|human_review|unknown",
  "authorization_ref": null,
  "owner_ref": "owner_...",
  "state": "draft|pending_approval|approved|rejected|queued|running|completed|failed|cancelled"
}
```

### Trial, observation, and result

```json
{
  "trial_id": "trial_...",
  "probe_id": "probe_...",
  "run_id": "run_...",
  "mode": "synthetic|shadow_work",
  "runner_version": "...",
  "dataset_versions": ["..."],
  "config_hash": "sha256:...",
  "started_at": "...",
  "finished_at": "...",
  "deviations": [],
  "observations": [
    {"observation_id": "obs_...", "metric": "join_mismatch_rate", "value": 0, "unit": "ratio", "evidence_ref": "fixture://...", "quality_flags": []}
  ],
  "result": {
    "result_id": "result_...",
    "claim_id": "claim_...",
    "outcome": "supported|refuted|inconclusive",
    "criterion_version": "...",
    "uncertainty": "...",
    "review_status": "unreviewed|accepted|rejected",
    "reviewer_ref": null
  }
}
```

### Event

```json
{
  "event_id": "evt_...",
  "aggregate_type": "recommendation|claim|probe|trial|result|export",
  "aggregate_id": "...",
  "sequence": 1,
  "event_type": "claim.drafted",
  "occurred_at": "...",
  "actor_ref": "...",
  "correlation_id": "...",
  "causation_id": null,
  "idempotency_key": "...",
  "payload": {},
  "schema_version": "1"
}
```

Never overwrite historical results. Corrections create a superseding version and preserve the earlier as-of state.

## 9. State transitions and invariants

Allowed claim transitions:

```text
draft -> pending_review -> untested
untested -> supported | refuted | inconclusive | waived
supported -> expired | untested
inconclusive -> untested | waived
refuted -> untested only through a new version with changed scope/conditions
waived -> expired
```

Recommendation readiness:

- `eligible_for_human_promotion_review` only when every required claim is currently `supported` or has a valid, policy-allowed waiver; evidence and identity authorization are current; no result is rejected; and no prohibited action class is present.
- `blocked` when any required claim is `refuted`, `expired`, `untested`, or invalid.
- `manual_exception_required` only for an explicit policy path with named owner, reason, expiry, and evidence. Portable mode cannot exercise this path.
- Readiness never directly performs the action.

Invariants:

- Every result references the exact claim version, probe version, evaluator version, dataset/config versions, and evidence.
- A result outside the claim scope cannot support the claim.
- A simulation result is labeled simulation and cannot satisfy a policy requiring empirical evidence.
- Missing measurement is `inconclusive`, not zero, pass, or failure unless the predeclared criterion explicitly defines it.
- Negative controls and deviations are immutable after completion; corrections supersede.
- Duplicate idempotency keys do not create duplicate events or trials.
- Current caller authorization is checked at view, run, replay, and export time.
- No agent output can mutate readiness without deterministic validation and policy evaluation.

## 10. API and CLI contracts

Implement or map these contracts. Exact framework and paths follow inventory.

```text
POST   /api/recommendations/import
GET    /api/recommendations/{id}
POST   /api/recommendations/{id}/claims
POST   /api/claims/{id}/review
GET    /api/claims/{id}/related-trials
POST   /api/claims/{id}/probes:plan
POST   /api/probes/{id}/approve
POST   /api/probes/{id}/run
POST   /api/trials/{id}/observations
POST   /api/trials/{id}/complete
POST   /api/recommendations/{id}/evaluate-readiness
POST   /api/recommendations/{id}/export
GET    /api/events?aggregate_id=...
POST   /api/replay
```

Every mutation requires identity, idempotency key, expected aggregate version, and correlation ID. Return structured 409 conflicts for stale versions and 403 for authorization failure. Do not retry non-idempotent work silently.

CLI:

```text
paulos-trials demo seed
paulos-trials validate fixtures/
paulos-trials import recommendation.md
paulos-trials plan-probes --recommendation rec_demo_0008
paulos-trials run --probe probe_demo_0008 --mode synthetic
paulos-trials evaluate --recommendation rec_demo_0008
paulos-trials replay --all --verify-hashes
paulos-trials eval --dataset eval/cases.jsonl --policy demo-policy-v1
paulos-trials export --recommendation rec_demo_0008 --format markdown,json
```

Implement equivalent project-native commands if a house CLI exists; document the mapping.

## 11. Local persistence and retrieval fit

SQLite portable schema: `recommendations`, `claims`, `claim_dependencies`, `evidence_refs`, `probe_templates`, `probes`, `probe_claims`, `trials`, `observations`, `results`, `reviews`, `waivers`, `events`, `outbox`, and `schema_migrations`.

- Enable foreign keys explicitly and use transactions for event plus projection updates.
- Use WAL only if supported by the actual deployment filesystem; document the choice.
- Store content hashes and source/version references, not duplicated authoritative Markdown or restricted payloads.
- Provide schema migrations and deterministic seed data.
- If approved Postgres already owns Swarm Court state, add tables there only after inventory and migration review; do not introduce another database by default.

Local vector retrieval remains a discovery/input adapter. Index only approved, reviewed summaries and references. Apply identity/ACL filters before retrieval. Draft claims, unreviewed results, and restricted evidence are not promoted to authoritative context. When a result supersedes an earlier one, preserve history and update the derived index through the discovered mechanism.

## 12. Work adapter contracts and REPLACE_AT_WORK tasks

```text
RunnerAdapter.capabilities() -> RunnerCapabilities
RunnerAdapter.start(trial_spec, limits, idempotency_key) -> RunHandle
RunnerAdapter.poll(run_handle, cursor) -> EventBatch
RunnerAdapter.cancel(run_handle, reason) -> CancellationResult
RunnerAdapter.collect(run_handle) -> TrialArtifacts

ContextIndexAdapter.search(query, identity, filters, limit) -> EvidenceRefs
ContextIndexAdapter.index(reviewed_summary, identity, source_refs) -> IndexReceipt
ContextIndexAdapter.invalidate(source_ref, reason) -> InvalidationReceipt

BigQueryAdapter.dry_run(query_ref, identity, limits) -> DryRunReceipt
BigQueryAdapter.execute_read_only(query_ref, parameters, identity, limits, labels) -> QueryReceipt
BigQueryAdapter.snapshot_ref(query_receipt) -> EvidenceRef

IdentityAdapter.current_actor() -> Actor
IdentityAdapter.authorize(actor, action, resource) -> AuthorizationDecision

DreamcatcherAdapter.manifest() -> PackagingContract
DreamcatcherAdapter.link(node_ref, app_route) -> LinkReceipt
```

Concrete discovery tasks:

- `REPLACE_AT_WORK_RUNNER`: find the approved local runner, auth method, executable/API, supported models, structured output, timeouts, cancellation, metering, and concurrency. Do not assume subscription entitlements.
- `REPLACE_AT_WORK_CONTEXT_INDEX`: find local vector index write/read APIs, source/version metadata, ACL enforcement, deletion/supersession, and review promotion.
- `REPLACE_AT_WORK_BIGQUERY`: find governed read-only dev connector, project/dataset/region, authorized views, identity propagation, dry-run/query limits, job labels, retention, and approved synthetic or de-identified pilot data.
- `REPLACE_AT_WORK_IDENTITY`: find user/service identity, role mapping, current authorization checks, audit identity, and reviewer resolution.
- `REPLACE_AT_WORK_DREAMCATCHER`: find app manifest, framework, package location, route conventions, design tokens, persistence rules, authentication, tests, and deployment/rollback process.
- `REPLACE_AT_WORK_SWARM_COURT`: find node, ownership, evidence, event, review, feature-flag, and promotion contracts.
- `REPLACE_AT_WORK_EXPERIMENT_SYSTEM`: find any existing DOE, experiment, QMS/LIMS/MES, issue, or evaluation system appropriate for linking trials. Do not build a replacement or write to it in the pilot.

If an adapter is unavailable, mark it `unavailable` and keep the demo functioning with synthetic/local implementations. Never silently substitute a personal SaaS or API.

## 13. Budgets, concurrency, observability, and recovery

Portable defaults (configuration, not provider pricing):

- zero required model calls;
- at most one optional reasoning call per claim draft and one per probe explanation;
- concurrency `1` by default and hard maximum `2` until the discovered runner permits more;
- 120-second per reasoning-call timeout;
- 10-minute synthetic trial timeout;
- maximum 8 claims and 5 probe candidates per recommendation;
- maximum 100 events returned per page;
- maximum 2 MiB imported fixture and 256 KiB per evidence summary;
- reject raw secrets and unapproved binary payloads.

Enforce limits deterministically where possible. If token counts or cancellation are unavailable, label the limit unenforceable and fail closed for promotion. Do not convert usage to dollars without an approved pricing source and version.

Emit structured logs/metrics with `correlation_id`, `recommendation_id`, `claim_id`, `probe_id`, `trial_id`, `run_id`, `owner_ref`, policy/config versions, mode, latency, result, and error code. Redact payloads by policy. Minimum metrics:

- claims by state/risk/owner;
- age to first reviewed probe;
- trial completion and inconclusive rates;
- duplicate-trial detection rate;
- unsupported-promotion escape and false-block rates;
- reviewer minutes;
- model calls and provider-reported usage when available;
- replay hash mismatches;
- authorization failures and forbidden-side-effect attempts.

Recovery:

- use inbox/outbox plus idempotency for mutation delivery;
- resume polling from cursors;
- mark stale running trials and require owner recovery;
- never infer a successful trial from timeout or missing events;
- replay projections from the event log and verify deterministic decision hashes;
- quarantine malformed/unknown schema versions without discarding raw allowed records;
- allow human cancellation with durable reason and owner.

## 14. Policy boundaries, promotion, and rollback

- MVP/shadow pilot is advisory and read-only.
- No recommendation can authorize quality acceptance, material disposition, part release, manufacturing parameter change, source-system update, deployment, credential use, or external message.
- High-risk or irreversible probes require an existing approved work process and named human authority; the app only links to it.
- Work data access uses current caller identity and least privilege; no cross-user leakage through summaries, indexes, logs, caches, or exports.
- A waiver is not support. Show it separately with reason, owner, scope, and expiry.
- Promotion path: synthetic eval pass -> security/data review -> read-only shadow pilot -> owner review -> separately approved feature-flagged eligibility gate. No automatic rollout.
- Candidate policy versions are immutable. Promotion records dataset, metrics, reviewers, config, and code revision.
- Rollback disables the candidate feature flag, returns to the previous readiness policy, preserves history, cancels only safe pending runs, and verifies the prior policy by replay.
- Rollback must be tested in the synthetic demo.

## 15. Evaluation dataset and acceptance criteria

Create `eval/cases.jsonl` with **64 synthetic cases**, split before tuning into 40 development and 24 held-out cases. Include at least:

- 8 fully supported recommendations;
- 8 refuted required claims;
- 8 inconclusive/noisy measurements;
- 6 expired support records;
- 6 missing/unauthorized evidence cases;
- 6 simulation-only results where empirical evidence is required;
- 6 valid and invalid waivers;
- 6 duplicate/near-duplicate prior trials with changed scope;
- 4 negative-control failures;
- 4 late/out-of-order/duplicate events;
- 2 malformed or unknown schema versions.

Each case has independently authored expected readiness, claim states, blocking reason set, authorized evidence set, and allowed next actions. Keep expected outputs out of model prompts. Freeze the held-out set and policy before evaluation.

Acceptance criteria:

1. All schemas validate; malformed records fail with stable error codes and JSON paths.
2. Event replay from an empty database produces byte-identical normalized projections and decision hashes.
3. Duplicate and out-of-order events do not duplicate trials or change final state.
4. Every held-out blocked case is included in the unsupported-promotion denominator; crashes and timeouts count as escapes.
5. Candidate results are compared with all three baselines using identical cases; no improvement is promised.
6. Candidate must have zero forbidden side effects in tests.
7. Candidate must meet a predeclared escape-rate target chosen in config before held-out execution and must not exceed the predeclared false-block or reviewer-time guardrails. Put the chosen values and rationale in `eval/policy.yaml`; do not hard-code flattering values after seeing results.
8. Simulation-only, expired, unauthorized, and inconclusive evidence never satisfies an empirical required claim unless the test case includes a valid policy exception.
9. All negative/null results remain searchable by fingerprint, scope, conditions, and version.
10. Current identity is checked before view, run, replay, and export.
11. UI shows exact state, owner, evidence, uncertainty, versions, blockers, and as-of time; no fake progress or activity.
12. Synthetic demo starts without cloud/model credentials and completes from a clean checkout.
13. Promotion and rollback are feature-flagged and rollback replay is tested.
14. `verification/REPORT.md` records commands, environment, counts, failures, metrics, limitations, and remaining `REPLACE_AT_WORK` items.

Agent agreement is never a ground-truth label. If results do not beat the strongest baseline within guardrails, recommend configuration/reuse or stopping rather than promoting the feature.

## 16. Repository tree

Adapt to the discovered repository; do not create duplicate top-level tooling. Portable fallback:

```text
paulos-swarm-assumption-trial-ledger/
├── AGENTS.md                         # only if required by discovered conventions
├── README.md
├── BUILD_PROMPT.md
├── APP_SPEC.md
├── idea.yaml
├── pyproject.toml                    # or discovered project manifest
├── package.json                      # only if UI is separate and required
├── config/
│   ├── demo-policy.yaml
│   ├── limits.example.yaml
│   └── probe-templates/
├── schemas/
│   ├── recommendation.schema.json
│   ├── claim.schema.json
│   ├── probe.schema.json
│   ├── trial.schema.json
│   └── event.schema.json
├── migrations/
├── src/
│   ├── domain/
│   ├── policy/
│   ├── persistence/
│   ├── replay/
│   ├── adapters/
│   ├── api/
│   └── cli/
├── ui/
├── fixtures/
│   ├── synthetic/
│   └── recommendations/
├── eval/
│   ├── cases.jsonl
│   ├── policy.yaml
│   └── expected/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── policy/
│   ├── replay/
│   └── e2e/
├── docs/
│   ├── sources.md
│   ├── INVENTORY.md
│   ├── WORK_HANDOFF.md
│   ├── SECURITY.md
│   └── RUNBOOK.md
└── verification/
    └── REPORT.md
```

## 17. Ordered implementation backlog

1. Inventory repositories, AGENTS.md, tests, runner, IDs, state, approvals, adapters, UI/package conventions; write inventory and reuse decision.
2. Create schemas, domain invariants, migrations, seed fixtures, and config validation.
3. Implement event store, projections, idempotency, optimistic concurrency, replay, and decision hashes.
4. Implement deterministic readiness policy and three baselines.
5. Implement claim fingerprints and prior-trial lookup with scope/condition comparison.
6. Implement probe templates and deterministic planner; keep optional agent drafting behind a disabled-by-default adapter.
7. Implement synthetic runner, observation evaluator, negative-control/deviation capture, and result versioning.
8. Implement CLI and API with identity/authorization hooks.
9. Implement the seven UI surfaces using discovered design tokens and ownership/evidence links.
10. Build 64 cases, freeze the held-out split and thresholds, run baseline/candidate evaluation.
11. Add failure injection, duplicate/out-of-order event tests, crash recovery, authorization, security, and rollback tests.
12. Add discovered work adapters without company data in the portable repository; keep shadow mode.
13. Complete README, specs, source ledger, work handoff, runbook, verification report, and issue body.
14. Stop if reuse/configuration already covers the complete flow; document the smallest missing change instead.

## 18. Commands to implement and verify

Use equivalent house commands if discovered; document exact substitutions.

```bash
make setup
make lint
make typecheck
make test
make test-replay
make test-security
make demo
make eval
make verify
```

Expected portable behavior:

```bash
paulos-trials demo seed
paulos-trials demo serve
paulos-trials eval --dataset eval/cases.jsonl --policy config/demo-policy.yaml
paulos-trials replay --all --verify-hashes
```

`make verify` must fail on schema error, replay mismatch, forbidden side effect, missing held-out denominator, leaked secret fixture, or unacknowledged `REPLACE_AT_WORK` item classified as resolved.

## 19. Required deliverables and handoff artifacts

Create and populate:

- `README.md`
- `BUILD_PROMPT.md`
- `APP_SPEC.md`
- `idea.yaml`
- `docs/sources.md`
- `docs/INVENTORY.md`
- `docs/WORK_HANDOFF.md`
- `docs/SECURITY.md`
- `docs/RUNBOOK.md`
- all relevant schemas, migrations, and config examples
- runnable synthetic demo and 64-case evaluation dataset
- automated tests and exact commands
- `verification/REPORT.md`

`docs/WORK_HANDOFF.md` must list actual discovered paths and APIs, reusable components, unresolved adapters, work owners, access needs, data boundaries, pilot recommendation, and rollout/rollback steps. The research proposal does not claim these artifacts already exist; you are to create them.

## 20. Definition of done

Done means a clean checkout can run the offline demo and held-out evaluation without model or cloud credentials; a reviewer can trace every readiness decision to claims, probes, results, policies, code/config versions, evidence references, and owner; replay is deterministic; null/negative results are preserved; forbidden actions are impossible in portable mode; and the verification report honestly compares the candidate to baselines.

If actual work integrations are unavailable, deliver the verified portable demo and a precise `REPLACE_AT_WORK` handoff. If existing work capabilities already provide the full loop, configure/reuse them and implement only missing Paul OS/Swarm Court/Dreamcatcher bindings.

---

## Pasteable promotion instruction

> Read `PaulOS-Podcast-App-2026-10-08-paulos-swarm-assumption-trial-ledger.md` and implement the BUILD PROMPT as a thin extension of the existing Swarm Court/Paul OS repository after completing the required inventory. Reuse existing experiment, evidence, approval, identity, persistence, and Dreamcatcher components; keep the portable demo synthetic and offline; leave all unresolved work bindings as `REPLACE_AT_WORK`; run the complete test/evaluation suite; and produce every required handoff artifact plus `verification/REPORT.md`. Do not deploy, publish, or write to production systems without separate authorization.

---

## Issue-ready body

### Goal

Add a shadow-mode Swarm Court extension that makes material recommendation assumptions explicit, binds them to falsifiable trials, preserves negative/inconclusive results, and deterministically reports whether the recommendation is ready for human promotion review.

### Scope

- Stable recommendation, claim, probe, trial, result, review, and event records.
- Deterministic readiness policy, expiry, waivers, replay, and exports.
- Synthetic offline demo with 64 evaluation cases and three baselines.
- Dreamcatcher-compatible review surface using discovered Paul OS design conventions.
- Work adapters for runner, context index, governed BigQuery, identity, Swarm Court, and packaging, with unresolved bindings marked `REPLACE_AT_WORK`.

### Acceptance checklist

- [ ] Applicable `AGENTS.md` and repositories inspected; `docs/INVENTORY.md` records actual paths and reuse.
- [ ] Markdown/skills/work systems remain authoritative; no Supabase.
- [ ] Demo runs offline with synthetic data and no model credentials.
- [ ] Strict schemas, migrations, idempotency, concurrency guards, and deterministic replay exist.
- [ ] Required claims cannot be satisfied by missing, expired, unauthorized, simulation-only, or inconclusive evidence unless a valid policy exception exists.
- [ ] Negative controls, null results, deviations, and superseding versions are preserved.
- [ ] Readiness never performs the recommended action.
- [ ] Current identity is enforced at view, run, replay, and export.
- [ ] 64 cases are split/frozen before held-out evaluation; candidate is compared with all baselines.
- [ ] Primary metric and guardrails include exact counts and limitations.
- [ ] Failure recovery, security boundaries, promotion, and rollback tests pass.
- [ ] README, BUILD_PROMPT, APP_SPEC, idea.yaml, sources, work handoff, schemas/config, runnable demo, and verification report are complete.
- [ ] No deployment, GitHub publication, or production write occurs without separate authorization.

---

# Research, coverage, and novelty ledger

## Intake summary

- **Core roster checked:** all 10 requested shows.
- **Candidates retained:** **35** episodes/items dated January 22–October 8, 2026; **30** were within the preceding 30 calendar days.
- **Selected transcript inspection:** **8 distinct episodes across 5 shows**. No audio listening and no end-to-end transcript-read claim.
- **Newest evidence:** Latent Space, October 8, 2026. The ThursdAI page available during the run displays a publication label of October 9; it was treated as publisher notes available on October 8 New York time, not as a transcript read.
- **Limitations:** the newest No Priors and TWIML items exposed publisher descriptions/show notes but no publisher transcript body; ThursdAI's October 8 program page was detailed notes rather than a clearly verbatim speaker transcript; The Gradient podcast archive remained stale (latest relevant podcast found January 22); Practical AI 374's transcript route did not yield transcript text in this run; Cognitive Revolution transcripts are explicitly automatic; transcript production methods for several other publishers were not established. No paywall was bypassed.

## Candidate discovery by show

| Show | Candidates retained | Date range | Latest/relevant items and access note |
|---|---:|---|---|
| Dwarkesh Podcast | 3 | Aug. 11–Oct. 1 | Si Sheppard (Oct. 1, transcript, not directly relevant); Noam Brown (Sep. 17, transcript); Ryan Greenblatt (Aug. 11, transcript). |
| Latent Space | 6 | Sep. 16–Oct. 8 | Periodic Labs (Oct. 8, transcript); Alex Zhang/RLM (Oct. 2, transcript); DevDay computer use (Sep. 30, transcript); Thariq Shihipar (Sep. 29, transcript); Jev (Sep. 21, transcript); AIUC (Sep. 16, transcript). |
| The Cognitive Revolution | 4 | Oct. 1–Oct. 8 | AI:AM (Oct. 8); OutSystems (Oct. 7, automatic transcript); Gemini Robotics 2 (Oct. 3, automatic transcript); AI:AM (Oct. 1, automatic transcript). |
| Practical AI | 4 | Sep. 3–Oct. 1 | Physical AI/NVIDIA #374 (Oct. 1, notes; transcript route unavailable); AGENTS.md to Enterprise #373 (Sep. 24, transcript); AI search #372 (Sep. 17, notes); Architecture #370 (Sep. 3, notes/transcript route unreliable). |
| No Priors | 4 | Sep. 10–Oct. 2 | Frontier Chips (Oct. 2), Re-Founding Incumbents (Sep. 24), Diffusion Inference (Sep. 18), Coinbase (Sep. 10); newest official transcript body unavailable, third-party transcript index used only for discovery. |
| ThursdAI | 3 | Sep. 24–Oct. 9 page label | Oct. 8 program page (available Oct. 8 New York; detailed publisher notes), Oct. 1 program, Sep. 24 program. |
| The Gradient Podcast | 1 | Jan. 22 | Archive checked; no fresh podcast release found in the priority window. |
| TWIML AI Podcast | 4 | Sep. 9–Oct. 6 | Jev #779 (Oct. 6, publisher notes), Math/Navier-Stokes #778 (Sep. 29), Voice Agents #777 (Sep. 16), Tokenomics #776 (Sep. 9). |
| MLOps Community / Agentic AI Foundation | 4 | Sep. 28–Oct. 5 | Logistics/FinOps (Oct. 5, transcript), Caveman Prompting (Oct. 1, notes), AGENTS.md speaks UNIX (Sep. 29, article), AWS APIs/MCP (Sep. 28, transcript). |
| Lex Fridman | 2 | Feb.–Aug. 26 | DHH #501 (Aug. 26, transcript with publisher caveat in prior inspection); State of AI #490 (older transcript). Checked for relevant newer research interviews; none displaced the fresher sources. |

## Transcript-section inspection ledger

| Show / episode / guest | Published | Canonical and transcript URL | Sections inspected | Access status | What was learned |
|---|---|---|---|---|---|
| Latent Space — *Synthesis Superintelligence* — Liam Fedus & Ekin Doğuş Çubuk | 2026-10-08 | https://www.latent.space/p/periodic | 00:00:13–00:06:30; 00:22:18–00:27:10; 00:50:02–00:58:13; 01:02:17–01:07:55 | Selected publisher transcript sections | Physical experiments are ultimate evidence; measurements are noisy/partial; use replicates and multiple modalities; preserve negative controls, null results, and the process lineage; automate bottlenecks rather than autonomy for its own sake. |
| The Cognitive Revolution — *One Brain, Any Body* — Keerthana Gopalakrishnan | 2026-10-03 | https://www.cognitiverevolution.ai/one-brain-any-body-google-deepmind-s-keerthana-on-gemini-robotics-2-cross-embodiment-humanoids/ | 11:50–17:44; 51:xx–54:20; 01:03:26–01:13:35 | Selected publisher-labeled automatic transcript sections | Real-world reliability differs by task; errors compound across sequences; retries may be safe for some tasks and unacceptable for others; safety includes stopping when sensing is degraded. Wording may be uncertain. |
| Dwarkesh Podcast — *Agent swarms, alignment, & recursive self-improvement* — Noam Brown | 2026-09-17 | https://www.dwarkesh.com/p/noam-brown | Approx. 00:00–00:15:28 | Selected publisher transcript section | Parallelism benefits vary by domain; single spectacular results do not replace methodical ablation; agents sometimes proceed by making assumptions when clarification is absent. |
| Latent Space — *Academia is for Ambition* — Alex Zhang | 2026-10-02 | https://www.latent.space/p/rlm | 00:46:06–00:53:57; later convergence/selection passages from 01:09:57 onward | Selected publisher transcript sections | Persistent/external context enables long work, but harness design and result selection remain explicit problems; not all swarm work is useful. |
| Latent Space — *Why Dwarkesh is Wrong about Computer Use* — Ari Weinstein & Nikunj Handa | 2026-09-30 | https://www.latent.space/p/devday-2026 | 00:06:04–00:17:31; 00:19:14–00:37:13 | Selected publisher transcript sections | Better representations, event-driven tools, async calls, steering, caching, and compaction improve agents; permissions and harness boundaries remain separate from model ability. |
| MLOps Community — *How a Logistics Giant Keeps AI Data Locked Down* — Jason Ward & Alex Salkever | 2026-10-05 | https://home.mlops.community/public/videos/how-a-logistics-giant-keeps-ai-data-locked-down | 00:00–00:18:20 | Selected publisher transcript sections | Ownership tags, trace context, and workload-specific baselines are prerequisites; prompt bloat and context starvation can both cause retry waste; metrics need local validation. |
| Practical AI #373 — *From AGENTS.md to Enterprise Deployment* — Nick Kuhn, Daniel Whitenack & Chris Benson | 2026-09-24 | https://practicalai.show/373 · https://practicalai.show/373/transcript | 19:13–24:21; 33:07–38:12 | Selected publisher transcript sections | Approved runners/models/tools, MCP gateways, isolation, incremental rollout, existing enterprise teams, and governance should be reused rather than bypassed. |
| Latent Space — *Claude Code's Next Era* — Thariq Shihipar | 2026-09-29 | https://www.latent.space/p/thariq | 00:06:xx–00:29:29 | Selected publisher transcript sections | Explicit unknowns, durable artifacts, decision/implementation notes, domain-specific effort, and retained experiment logs make agent work more reviewable. |

## Supporting pages not counted as transcript inspection

| Source | Published | Access | Use |
|---|---|---|---|
| TWIML #779, *Why Jev Is Changing How We Build With AI*, Diogo Almeida | 2026-10-06 | Publisher show notes only | Calibration/reliability and engineered model-plus-code systems; not used as proof of this ledger. |
| ThursdAI, *Oct 8 — OpenAI drops 722 math papers...* | Page labels 2026-10-09; available during Oct. 8 NY run | Detailed publisher notes, not treated as verbatim transcript | Illustrates verification burden from high-volume output; also reports a cross-agent data-leak anecdote, reinforcing composition-aware policy. |
| No Priors, *Frontier Chips for Frontier AI Labs*, Walter Goodwin | 2026-10-02 | Official episode/show notes; third-party transcript index for discovery only | More trials/shots-on-goal under long physical lead times; not a direct feature source. |
| Practical AI #374, *Open models and the future of Physical AI*, Ming-Yu Liu | 2026-10-01 | Publisher notes; transcript body unavailable in this run | Sim-to-real and policy comparison; already covered by the distinct Counterfactual Workbench proposal, so not reused as the winning mechanism. |

## Independently checked technical references

- JSON Schema 2020-12 specification: https://json-schema.org/draft/2020-12
- SQLite foreign-key documentation: https://www.sqlite.org/foreignkeys.html
- SQLite transaction documentation: https://www.sqlite.org/lang_transaction.html
- SQLite WAL documentation: https://www.sqlite.org/wal.html
- Google Cloud BigQuery dry-run guidance (implementation agent must verify current work connector/version): https://cloud.google.com/bigquery/docs/best-practices-costs#estimate_query_costs

These references establish available technical mechanisms, not that they are installed or approved at work.

## Novelty and selection

All **12** retrievable prior `PaulOS-Podcast-App` proposal files were opened and compared by problem, mechanism, inputs, and output:

| Prior proposal | Primary mechanism | Why this winner is distinct |
|---|---|---|
| Swarm Parallelism Lab | Compare one/two/four agents and export routing policy | This ledger validates the premises of a recommendation; it does not choose worker count. |
| Swarm Regression Forge | Turn reviewed failures into regression tests and skill diffs | Forge starts after a known failure and outputs a test/patch. This ledger starts before promotion, preregisters falsifiers, and records empirical/null outcomes. It can feed failures to Forge. |
| Mission Context Compiler | Assemble minimum permission-aware context before a run | The ledger does not select context; it determines whether material claims have been tested. |
| Swarm Workflow Crystallizer | Convert stable traces into deterministic workflows | The ledger does not compile workflows; it can require a crystallized workflow to prove its assumptions. |
| Swarm Confidence Gate | Calibrate bounded model decisions and abstain/escalate | Confidence Gate evaluates a decision backend's error/coverage. The ledger evaluates world/process assumptions with explicit trials; calibrated confidence cannot substitute for evidence. |
| Swarm Tool Path Observatory | Improve tool contracts from runtime traces | The ledger may use trace evidence but does not optimize tools. |
| Swarm Counterfactual Workbench | Simulate and compare candidate actions | Counterfactual Workbench ranks modeled alternatives. The ledger records which assumptions still require real validation and prevents simulation-only evidence from satisfying empirical claims. |
| Swarm Delegation Contract Gate | Formalize handoffs and acceptance contracts | The ledger may assign trial ownership but focuses on claims/falsifiers/results, not delegation quality. |
| Swarm Evidence Invalidation Queue | Revalidate outputs when supporting evidence changes | Invalidation reacts to changed/withdrawn evidence. The ledger creates and evaluates new evidence for an initially uncertain assumption. |
| Swarm Convergence Governor | Stop/merge/escalate live runs when marginal verified progress stalls | The ledger governs evidence readiness across trials, not live swarm resource control. |
| Swarm Metric Reconciliation Desk | Diagnose conflicting metric definitions with witness records | Reconciliation compares two implementations. The ledger manages the broader assumption-to-trial lifecycle and can consume a reconciliation result. |
| Swarm Change Collision Radar | Detect overlapping change intents before parallel work | Collision Radar protects shared resources; the ledger tests whether a recommendation's premises hold. |

No same-date/same-idea Library file was found before creation. Repository-level duplication and implementation status remain unresolved; the build agent must inventory work code before coding.

Four candidates were ranked internally using work value (30%), Paul OS fit (25%), verifiability (20%), build effort/operating cost (15%), and novelty (10%): Assumption Trial Ledger; Negative Result Memory; Probe Prioritization Queue; and Real-vs-Sim Drift Receipt. The Assumption Trial Ledger won because it connects the full lifecycle—claim, falsifier, owner, trial, negative result, readiness—without duplicating the Counterfactual Workbench or Evidence Invalidation Queue. The ranking is editorial prioritization, not empirical validation.

