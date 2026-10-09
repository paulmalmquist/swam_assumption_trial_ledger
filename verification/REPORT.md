# Verification report

Executed 2026-10-09 in the build environment.

## Passed

`python3 -m unittest discover -s tests -v`: **18 tests passed**.

Coverage: deterministic observations/config hashes; supported/refuted/inconclusive outcomes; missing evidence, minimum sample counts and failed controls; empirical-evidence and expiry gates; positive readiness path and empty/high-risk blockers; mandatory result review; malformed numeric/boolean/evidence inputs; immutable prior versions; approval-before-run and duplicate-run protection; restart persistence; snapshot replay; idempotency-key content binding; stale-write conflicts; transactional validation rollback; hash corruption detection; HTTP assets/export/replay; request-token, Host and Origin rejection; authenticated-to-local-session HTTP mutation.

`node --check web/app.js`: passed.
`python3 -m py_compile server.py domain.py`: passed.
Clean transfer archive extracted and its same 18 tests rerun successfully before delivery.

## Not verified

Visual and real-browser interaction tests could not run: no browser executable was available and the Chromium download returned an invalid/truncated archive. No claim of browser QA is made. Desktop/mobile layout is implemented but visual rendering remains to be checked on the target machine.

This is functional regression testing, not an independently authored held-out study. The proposal's 64-case benchmark, false-block/escape confidence intervals, reviewer-time study, work identity/ACL and production integration are not completed.

## Operating boundary

Local, single-user, synthetic-only. No work-system credentials, network connector, real manufacturing data, model calls, external write or production action. SQLite audit snapshots are hash-linked but not signed or tamper-proof. See README and WORK_HANDOFF for precise scope.
