## 2026-09-18 - Displacement Map Caching & Canvas Reuse in LiquidGlass

**Learning:** `LiquidGlass` displacement map generation calls `document.createElement('canvas')` and CPU-intensive `canvas.toDataURL()` on every update. In animated/interactive standard layouts or window resizes, this produces garbage collection pressure and CPU frame drops. Furthermore, calling `refresh()` when element dimensions haven't changed results in redundant SVG DOM updates.

**Action:** Reuse a single shared canvas instance for offscreen displacement rendering, cache generated map data URIs using a bounded LRU cache (keyed by map parameters), and track last-measured element dimensions (`lastW`, `lastH`, `lastRadius`) to skip redundant `refresh()` executions.
