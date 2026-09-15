## 2025-05-18 - Shared Canvas Allocation & Displacement Map Caching
**Learning:** Dynamic creation of Canvas elements and `toDataURL()` calls during filter map creation in `liquid-glass.js` introduce heavy GC pressure and CPU overhead. Using a shared canvas instance, caching data URIs in a bounded LRU Map, and early-exiting `refresh()` on unchanged element dimensions completely eliminates redundant rendering costs.
**Action:** When working with canvas-generated SVG displacement maps or dynamic data URIs, reuse offscreen canvas contexts and implement LRU data URI caching.
