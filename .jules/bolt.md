# Bolt's Journal - Critical Learnings Only

## 2025-05-18 - Displacement Map Generation and Data URL Bottleneck
**Learning:** In liquid-glass SVG filter generation, `canvas.toDataURL()` accounts for >90% of frame time (~11ms out of ~12.6ms per displacement map update). Additionally, allocating new `<canvas>` elements on every resize or layout change induces GC pauses. Reusing a single shared canvas and caching generated data URIs in a bounded LRU cache reduces cached map retrieval time from ~12.6ms to ~0.18ms (>98% speedup), while instance-level dimension guards bypass redundant calculations entirely (~0.006ms).
**Action:** When working with canvas-backed SVG filters or procedural textures, always reuse offscreen canvas/context instances and LRU-cache the resulting data URIs keyed by geometric parameters.
