## 2025-02-14 - Shared Canvas & Map Caching in liquid-glass.js
**Learning:** Generating SVG displacement maps via Canvas 2D and `toDataURL()` on every element refresh creates significant GC pressure (from canvas DOM allocations) and CPU work. Reusing a shared canvas element and context eliminates canvas allocations, while an LRU map cache bypasses data URI encoding and rendering for repeated or identical dimensions.
**Action:** When working with canvas-backed SVG filters or dynamic data URIs, reuse canvas instances globally and cache serialized output by parameter signatures.
