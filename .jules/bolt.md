## 2026-11-03 - Shared Canvas and Map LRU Caching in liquid-glass.js
**Learning:** In liquid-glass.js, generating SVG displacement maps on every `refresh()` call created GC pressure and CPU overhead from repeated `<canvas>` allocations and synchronous `canvas.toDataURL()` PNG encoding.
**Action:** Reuse a single module-level `<canvas>` and 2D context, cache generated data URIs in a Map-based bounded LRU cache (keyed by dimensions and parameters), and cache element dimensions on instance `refresh()` calls to short-circuit redundant recalculations.
