## 2026-09-27 - Shared Canvas and Map LRU Caching in liquid-glass.js
**Learning:** In liquid-glass.js, generating SVG displacement maps on every `refresh()` call created massive CPU spikes (~14.4ms/call) due to repeated `<canvas>` allocations and synchronous `canvas.toDataURL()` PNG encoding.
**Action:** Reuse a single module-level `<canvas>` and context, store generated data URIs in a Map-based LRU cache (keyed by dimensions and map parameters), and cache element dimensions on instance `refresh()` calls to bypass redundant executions.
