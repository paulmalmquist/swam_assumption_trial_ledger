# Portable API

All endpoints are loopback-only. GET `/api/state` returns the current global version, recommendations with computed states, and the per-process mutation token. Local audit actors are self-declared names.

- GET `/api/events`: chronological audit metadata.
- GET `/api/replay`: verify all stored snapshot hashes and chain links; return current state hash.
- GET `/api/export`: full JSON packet with snapshots, trial observations and freshly computed receipts.
- POST `/api/command`: `Content-Type: application/json`, `X-Ledger-Token` from state.

Request envelope:

```json
{
  "action": "create",
  "data": {"title":"Fixture recommendation","rationale":"Test the premise","owner":"Demo owner","node_ref":"fixture://node/1","risk":"low"},
  "actor": "Local reviewer",
  "key": "unique-request-id",
  "expected_version": 1
}
```

Actions: `create`, `add_claim`, `revise`, `approve`, `run`, `review`. Domain field contracts are in `domain.py:new_claim` and `domain.py:mutate`; examples are exercised in the tests. `add_claim` and `revise` receive all claim fields plus recommendation_id and, for revision, claim_id. Approval requires reason. Review requires trial_id, decision (accept/reject) and reason. Invalid requests return 400; request protection returns 403; stale global versions and reused keys with changed payload return 409. Idempotent retries return the current projection without repeating a mutation.

The browser uses these exact contracts. They intentionally differ from the larger research proposal's granular REST routes. Adapt them to existing work services after inventory.
