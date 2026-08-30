## 2026-08-30 - Shared Canvas and Displacement Map LRU Caching
**Learning:** Generating liquid glass displacement maps via HTML5 Canvas 2D gradients, rounded rect filters, and `.toDataURL()` on every resize event or refresh pass produces noticeable GC pressure and unnecessary CPU rendering work.
**Action:** Reuse a single shared Canvas element across displacement map generations and maintain a bounded LRU cache for data URIs keyed by map dimensions/blur parameters, plus dimension guards on `refresh()`.
