## 2025-05-18 - Canvas Reuse and Map Caching in Liquid Glass Filter Generation
**Learning:** SVG displacement map generation in `liquid-glass.js` suffered from significant Garbage Collection (GC) overhead due to transient `<canvas>` element allocations on every map generation, combined with repeated CPU-heavy `toDataURL()` calls for identical element dimensions.
**Action:** Reuse a single shared module-level canvas/context and maintain a bounded LRU cache for displacement data URLs keyed by element dimensions and map parameters.
