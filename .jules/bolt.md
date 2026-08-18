## 2026-08-18 - Shared Canvas and Map Caching for Glassmorphic Displacement Maps
**Learning:** Re-allocating canvas elements and calling `toDataURL()` on every filter refresh causes GC pressure and CPU overhead during resize/re-render operations.
**Action:** Use a single shared canvas/context and a bounded LRU `Map` cache for data URIs based on dimensions, radius, border, and map blur parameters.
