## 2025-05-10 - SVG Displacement Map LRU Caching & Shared Canvas Reuse

**Learning:** SVG displacement filter map generation in liquid-glass.js using `canvas.toDataURL()` and dynamic `<canvas>` creation generates significant garbage collection (GC) pressure and main-thread execution time during frequent `refresh()` or resize calls. Because many elements share identical dimensions and refraction/blur properties, generated maps can be cached in a Map-based LRU cache. Additionally, canvas elements can be reused since resizing canvas dimensions (`canvas.width = w`) automatically clears context state synchronously in single-threaded JS.

**Action:** Reuse a single shared canvas instance and wrap displacement map generation in a Map-based LRU cache (capped at 20 entries). On `refresh()`, short-circuit map generation if element dimensions and computed border radius match the last recorded state.
