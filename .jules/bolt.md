## 2025-08-21 - Canvas Allocation & Dimension Caching in SVG Displacement Filters
**Learning:** In SVG displacement map generation, creating dynamic `<canvas>` elements on every refresh causes high GC pressure and unnecessary `toDataURL()` computations, even when element dimensions haven't changed.
**Action:** Re-use a single module-level canvas instance and cache element width, height, and computed radius to exit early during redundant `refresh()` calls.
