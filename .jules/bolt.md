## 2025-05-10 - Shared Canvas & Map Data Cache for SVG Displacement Maps
**Learning:** Frequent calls to `canvas.toDataURL()` and dynamic `<canvas>` creation during element resizes cause noticeable CPU spikes and GC pressure. Caching data URLs in a bounded Map and reusing a single shared canvas context eliminates allocation overhead without growing memory boundlessly.
**Action:** Reuse module-level canvas/context and cache generated Data URLs by key `(w, h, radius, border, mapBlur)`.
