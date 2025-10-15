# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project scope
- Primary module: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL (pure-Python, zero runtime deps).
- Docs: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs and top-level docs/.
- CI: .github/workflows/ci.yml (Python 3.11, pytest only).

Core commands
- Run CLI (from AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/):
```bash path=null start=null
python src/cli.py --intent "Architect unassailable market dominance through verifiable systems."
```
- Run all tests (pytest, quiet, short trace):
```bash path=null start=null
pytest -q --tb=short
```
- Run a single test file:
```bash path=null start=null
pytest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/tests/unit/test_sovereign_core.py -q
```
- Run a single test by name (example):
```bash path=null start=null
pytest -k "test_basic_flow" -q
```
- unittest equivalents (if preferred):
```bash path=null start=null
python -m unittest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL.tests.unit.test_sovereign_core
python -m unittest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL.tests.unit.test_sovereign_core.TestSovereignCore.test_basic_flow
```
- Lint/typecheck: none configured in repo (no pyproject/ruff/flake8/mypy). CI installs pytest only.

High-level architecture
- Entry points
  - src/cli.py: Minimal CLI that instantiates ZKVSNodePrime and prints execution report.
  - src/sovereign_core.py: ZKVSNodePrime orchestrates the system.
- Orchestration pipeline (sovereign_core.ZKVSNodePrime.execute_mandate)
  1) Token stream stats: axiomshards_catalyst.ToSTLinear ingests tokens from the intent to maintain O(N) streaming stats.
  2) Intent processing: praetorian_layers.CerebrumLayer.process_intent filters noise per axioms.
  3) Task planning: praetorian_layers.HadrianLayer.orchestrate_task produces sub_tasks and binds dagger agents.
  4) Execution: praetorian_layers.DaggerLayer.execute_task runs agents and collates results.
  5) Safety/ethics gate: axiom_lattice.AxiomEnforcement.validate_ethical_and_safety checks output, densify_output shortens report.
  6) ZK proof stamp: sovereign_core._zk_compute adds a sha256-based “_zk_validated” marker.
  7) Trust metrics: axiom_lattice.TrustMetricsEngine aggregates simple in-memory metrics and applies a trust threshold.
  8) Data moat: data_moat.DynamicMoatCultivationEngine updates internal moat state and yields impact metrics (PSI/MCV/UAM).
  9) Complexity optimization: axiom_lattice.ComplexitySieveModule emits a small optimization report.
  10) Report: Return a multi-line summary including DOMINION status, ZK-PROVEN marker, VAMP, G-CONVEX flag, proof trace, and AxiomShards stats.
- Agents (src/dagger_agents.py)
  - DataSieveAgent: Text densification using DENSITY axiom; outputs summarized ‘sieved’ data snippet.
  - ZKProofAgent: Derives a deterministic sha256 as a mock “proof.”
  - MarketAnalysisAgent: Emits a deterministic strategic analysis string.
  - DaggerAgentUtils: integrity checks, text densification, deterministic hashing.
- Layers (src/praetorian_layers.py)
  - CerebrumLayer: token filtering/noise reduction.
  - HadrianLayer: builds a deterministic task_id and sub_tasks based on intent keywords; holds agent registry.
  - DaggerLayer: executes agents, handles missing agents and exceptions, concatenates results.
- Enforcement/assurance (src/axiom_lattice.py)
  - AxiomEnforcement: simple content filter + sovereignty check; densify_output truncates long strings.
  - TrustMetricsEngine: computes coarse metrics (robustness, uptime, error rate, latency, accountability index) and validates against threshold.
  - ComplexitySieveModule: toggles flags like monolithic_process/has_legacy_code and records changes.
- Streaming catalyst (src/axiomshards_catalyst.py)
  - ToSTLinear: O(N) feature accumulator with mean/min/max/count used for AxiomShards stats.
- Data moat (src/data_moat.py)
  - DynamicMoatCultivationEngine: updates moat strength and computes impact metrics based on outputs.

Tests
- Style: unittest modules collected by pytest in CI.
- Key checks: end-to-end DOMINION report, VAMP/G-CONVEX presence, safety/violation retries, invariants proxies (timing/KS distance), ledger growth without CRITICAL events.
- Useful invocations:
```bash path=null start=null
pytest -q --tb=short --maxfail=1
pytest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/tests/unit/test_sovereign_core.py::TestSovereignCore::test_basic_flow -q
```

Docs to consult frequently
- AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs/Technical_Specifications.md: topology, invariants (I1–I7), gates (G1–G4), ToST-linear.
- AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs/AXIOM_LEXICON.md: glossary.
- docs/advanced-threat-modeling.md: operational invariants, controls, acceptance, and evidence artifacts.
- README in AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/: quickstart and CI-aligned test command.

CI expectations
- Python 3.11.
- Minimal dependency install: pytest only.
- Command used in CI: `pytest -q --tb=short --no-header --maxfail=1`.

Deployment
- Container hardening guidance and process are described in AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/infrastructure/deploy.yaml (compose-like spec with strict runtime constraints). Adapt to your environment as needed.
