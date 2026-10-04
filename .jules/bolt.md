## 2025-02-18 - Canvas Context Reuse & Data URI LRU Caching in SVG Filters
**Learning:** Dynamic canvas allocation in tight animation/render loops creates severe GC pressure and main-thread execution lag during canvas.toDataURL(). In SVG-based glassmorphic filters, inputs (dimensions, border-radius, mapBlur) frequently repeat across elements or frames.
**Action:** Share a single module-scoped offscreen canvas context and apply a bounded LRU cache (e.g. Map with max size 20) for generated data URIs to make instantiation ~12x faster and refresh calls ~1,000x faster.
