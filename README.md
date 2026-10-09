# Swarm Assumption Trial Ledger

A transferable, local application for testing the premises behind agent recommendations. Python 3.10+ and a browser are all you need. No install, API key, Node build, cloud service, or Supabase.

## Start

Unzip, open a terminal in this folder, then:

```bash
python3 server.py
```

On Windows use `py server.py`. Open **http://127.0.0.1:8765**. Stop with Ctrl+C. Pick another port with `python3 server.py --port 8766`.

The first run creates `data/ledger.sqlite` with three synthetic recommendations and seven actual local simulation results. Your changes persist across restarts. Back up the database with the server stopped. Export JSON from the app to move evidence packets; packet re-import is not implemented. To transfer the entire workspace, copy the stopped app folder including its database. Do not commit runtime databases to Git.

## Try it

1. Open **Telemetry join alignment**. Observe the two empirical-evidence blockers despite a synthetic result.
2. Open **Metric definition reconciliation**. Inspect a refuted denominator assumption and its observations.
3. Create a low-risk recommendation and add a required assumption. Defaults generate 200 successful synthetic observations and use a 95% confidence lower-bound criterion of 95%.
4. Approve the probe, run the trial, then accept the result with a reason. It becomes ready for **demo review**.
5. Revise the claim with a lower simulated probability, missing observations, or a failed control. The new version needs approval and a new run; historical results remain visible.
6. Verify the saved history and export the full JSON packet.

## Delivered

- Responsive dark/purple inbox, claim detail, searchable trial history, audit/replay screen.
- Create recommendations and up to eight scoped claims each.
- Frozen trial settings per version; owner, expiry, source reference, empirical requirement, and required/optional flags.
- Deterministic seeded Bernoulli probes with Wilson intervals, minimum sample count and negative-control check. Missing observations remain inconclusive.
- Probe approval, immutable result review, superseding claim versions, retained negative/null results.
- Readiness computed on the server; no required claims, high risk, unreviewed, rejected, expired and empirical-only claims block readiness.
- SQLite transactional event/snapshot storage, optimistic concurrency and idempotency-key protection.
- Hash-verified snapshot replay and complete JSON export including raw synthetic observations, provenance, versioned snapshots and readiness receipts.
- Offline tests; CI workflow; integration handoff and original proposal.

## Scope and limits

This is a **single-user synthetic prototype**, not a manufacturing or quality authority. Reviewer names are local labels, not verified identities. It binds only to loopback and rejects unexpected hosts/origins; do not expose it with a proxy or tunnel. The per-process request token prevents casual cross-site writes but is not authentication. No telemetry or external requests are made.

The trial is a reproducible statistical teaching fixture, not a calibrated process simulator or causal experiment. The optional negative-control flag is configured fixture truth. Empirical evidence cannot be ingested in this version and therefore never becomes supported through synthetic runs.

The event store uses complete snapshots with hashes: it restores exact saved state, not re-execution of every historical command. Hashes detect accidental corruption, not a malicious database rewrite. Data grows with snapshots; production retention and pagination need work. Seed fixtures are recorded as one initialization event, with their approvals explicitly labeled demo curator.

Not implemented from the broader proposal: work connectors/SSO/ACL, waiver workflow, autonomous agent drafting, arbitrary experiment planning, multi-claim dependency graphs, Markdown import, empirical result ingestion, 64-case independently authored held-out benchmark, promotion/rollback deployment flags, and model/runner budgets. See `docs/WORK_HANDOFF.md` before adapting to a real environment.

## Verify

```bash
python3 -m unittest discover -s tests -v
python3 server.py --replay
```

## Add to your repository

Create your empty repository, unzip this package, and run inside its folder:

```bash
git init
git add .
git commit -m "Add portable Assumption Trial Ledger prototype"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

If the repository already has files, copy the package into that checkout and review the diff first. The database is ignored. No license grant is assumed; choose your repository's license.

## Handoff prompt

“Inspect this app and your repository's instructions. Read README.md, docs/INVENTORY.md, docs/WORK_HANDOFF.md and docs/SOURCE_PROPOSAL.md. Run the tests before changes. Integrate this as a shadow-only extension to the existing Swarm Court/Dreamcatcher contracts. Discover and reuse identity, persistence, evidence and review infrastructure. Preserve old results and version bindings. Do not reinterpret synthetic readiness as empirical support. Complete the REPLACE_AT_WORK inventory before adding connectors. Report actual implemented scope and tests.”
