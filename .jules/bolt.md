## 2026-07-09 - Shared Canvas & Displacement Map LRU Caching
**Learning:** Dynamic canvas allocation (`document.createElement('canvas')`) and synchronous `toDataURL()` in glassmorphic displacement map generation cause significant GC pressure and CPU frame drops during resizes or dynamic updates.
**Action:** Reuse a single shared offscreen canvas context and cache generated data URIs in a bounded Map LRU cache keyed by size and filter parameters.
