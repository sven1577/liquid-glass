# Bolt's Journal

## 2024-08-09 - Reusable Shared Canvas and Map Caching
**Learning:** Instantiating a new HTML5 Canvas on every map regeneration causes substantial GC pressure and CPU load, especially during high-frequency resize or drag-triggered redraws. Also, calling `toDataURL()` is highly expensive. Reusing a single module-level hidden canvas and caching map results using an LRU/LRU-like cache or key-based map prevents redundant rendering and reduces overall runtime latency.
**Action:** Use a module-level variable for a shared canvas instance and design a lightweight Cache to store and retrieve previously generated `toDataURL()` strings based on the dimensions and parameters.
