# Bolt's Journal

## 2025-05-18 - Canvas Reuse and LRU Data URL Caching for SVG Filters
**Learning:** In liquid glass SVG filter generation, creating dynamic `<canvas>` elements and calling `canvas.toDataURL()` on every update causes significant GC churn and CPU spikes. Reusing a single shared canvas context and caching generated data URIs in a bounded LRU cache (indexed by dimensions and border-radius/blur parameters) drastically improves responsiveness during resize and element recalculation events.
**Action:** Always reuse canvas contexts for offscreen filter image generation and memoize static image representations using bounded LRU caches when generating SVG data URIs.
