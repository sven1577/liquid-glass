## 2025-05-18 - Canvas Reuse and LRU Data URI Caching for SVG Displacement Maps
**Learning:** In liquid-glass.js, dynamic canvas creation on every `.update()` call caused GC pressure, while repeated `toDataURL()` calls were heavy on the CPU. Reusing a module-level offscreen canvas and context, paired with a bounded LRU cache for data URIs based on displacement map dimensions, eliminates allocations and redundant image encoding.
**Action:** Always reuse canvas/context instances for recurring texture generation and cache data URI exports by generation parameters.
