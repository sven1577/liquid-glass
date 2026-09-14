## 2026-09-14 - Canvas Reuse & Map LRU Caching in SVG Glass Filters
**Learning:** Re-allocating canvas elements and calling `toDataURL()` during element resize or filter updates creates severe GC pressure and main-thread blocking. A shared single canvas instance combined with a bounded Map-based LRU cache for data URIs eliminates dynamic allocation and redundant SVG map rasterizations.
**Action:** Use a module-level shared canvas and an LRU cache keyed by parameters when generating dynamic image assets for SVG filters.
