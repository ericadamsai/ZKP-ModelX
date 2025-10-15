# ZKP-ModelX: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL

Quantum‑resistant, RAM‑bounded, zero‑dependency execution engine with layered orchestration and verifiable reporting. This repository hosts the AXIOMHIVE_ZKVS_SIEVE_PROTOCOL implementation and supporting docs.

Highlights
- Pure Python runtime (no external deps); tests use pytest.
- O(N) streaming catalyst (ToST-linear) for token processing.
- Layered pipeline: Cerebrum (intent filter) → Hadrian (planner) → Dagger (agents) → Enforcement/Trust/Complexity → Report.
- CI on Python 3.11 runs pytest with minimal setup.

Requirements
- Python 3.11
- Optional (tests): pytest

Quickstart
- Run the CLI:
```bash path=null start=null
python AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/src/cli.py --intent "Architect unassailable market dominance through verifiable systems."
```
- Expected: multi‑line report including STATUS, ZK‑PROVEN marker, VAMP, G‑CONVEX flag, and proof trace.

Testing
- Install test dependency:
```bash path=null start=null
pip install pytest
```
- Run all tests:
```bash path=null start=null
pytest -q --tb=short
```
- Run a single test file:
```bash path=null start=null
pytest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/tests/unit/test_sovereign_core.py -q
```
- Run a single test:
```bash path=null start=null
pytest AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/tests/unit/test_sovereign_core.py::TestSovereignCore::test_basic_flow -q
```

Architecture (big picture)
- Entry points
  - AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/src/cli.py: CLI wrapper for the core engine.
  - AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/src/sovereign_core.py: ZKVSNodePrime orchestrates the full mandate execution.
- Core flow (execute_mandate)
  1) Token streaming stats via axiomshards_catalyst.ToSTLinear.
  2) Intent cleanup via praetorian_layers.CerebrumLayer.
  3) Task segmentation/agent plan via praetorian_layers.HadrianLayer.
  4) Agent execution via praetorian_layers.DaggerLayer (DataSieve, ZKProof, MarketAnalysis in src/dagger_agents.py).
  5) Safety/ethics check + densification via axiom_lattice.AxiomEnforcement.
  6) ZK-stamped hash, trust metrics (axiom_lattice.TrustMetricsEngine).
  7) Data moat cultivation + impact metrics (src/data_moat.py).
  8) Complexity optimization (axiom_lattice.ComplexitySieveModule).
  9) Consolidated report (status, metrics, proof trace, shard stats).

Continuous Integration
- Workflow: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/.github/workflows/ci.yml
- Python 3.11; installs pytest only; runs: `pytest -q --tb=short --no-header --maxfail=1`

Documentation
- Technical specifications: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs/Technical_Specifications.md
- Lexicon: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs/AXIOM_LEXICON.md
- User guide: AXIOMHIVE_ZKVS_SIEVE_PROTOCOL/docs/User_Guide.md
- Advanced threat modeling: docs/advanced-threat-modeling.md

License
- MIT (LICENSE)