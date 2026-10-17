## 2025-05-18 - Canvas Reuse and LRU Caching for SVG Displacement Maps
**Learning:** In liquid-glass.js, dynamic canvas allocations and repeated `canvas.toDataURL()` PNG serializations in `makeMap()` create significant GC pressure and main thread stalls. Caching data URIs with an LRU Map and reusing a single module-scoped hidden canvas eliminates memory allocations while preserving SVG filter rendering correctness.
**Action:** Always reuse canvas/context instances and cache heavy pixel/dataURL serializations when generator inputs (dimensions, radii, blur) are discrete and frequently repeated.
