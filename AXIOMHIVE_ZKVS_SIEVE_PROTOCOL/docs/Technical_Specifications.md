# Technical Specifications

## System Topology
- ZKVSNodePrime: Single-file core, self-attesting
- Layered: Cerebrum, Hadrian, Dagger, AxiomEnforcement, TrustMetrics, ComplexitySieve, Moat

## AxiomShards-Catalyst
- ToST-linear: Token-Oriented Stream Transformer, O(N) linear statistics
- Replaces vanilla transformer quadratic attention; explicit RAM bound (≤18MB)

## Security Protocols
- QRGM: L1C Timing Differential
- FHE sandbox: Zero persistent secret leakage (see threat model)
- RLEX Mesh: Pre-propagation override (indistinguishable traffic)

## State Transitions
- See logic in src/sovereign_core.py, transitions for code, key, and provenance

## Invariants & Acceptance Gates
- Invariants I1–I7, Gates G1–G4, see [Advanced Threat Model](../../docs/advanced-threat-modeling.md)

## Key Terms
- See [AXIOM_LEXICON](AXIOM_LEXICON.md)
