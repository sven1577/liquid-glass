# Bolt's Journal

## 2026-03-06 - Shared Canvas and Map LRU Caching in Liquid Glass
**Learning:** Dynamic creation of canvas elements and repeated calls to `canvas.toDataURL()` during liquid glass map generation cause GC pressure and unnecessary CPU usage when dimensions or options remain static.
**Action:** Reuse a shared offscreen canvas instance, cache generated data URIs in a bounded LRU Map cache, and cache measured dimensions on instances before re-rendering maps.
