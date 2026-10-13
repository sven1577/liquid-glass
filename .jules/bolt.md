# Bolt's Journal - Critical Learnings

## 2025-05-18 - Dynamic Canvas Allocation & toDataURL Bottlenecks in Canvas Displacement Generators
**Learning:** Dynamic canvas allocation on every displacement map generation causes unnecessary GC pressure, while repeated `canvas.toDataURL()` calls dominate CPU time during window resizing or re-renders. Reusing a shared module-level canvas and caching data URIs in a bounded LRU cache significantly improves performance. Persistent style caching (e.g., WeakMap for computed border-radius) was avoided due to potential cache invalidation bugs when element styles change dynamically.
**Action:** When generating procedural image maps or data URIs in canvas-based UI libraries, reuse a single static offscreen canvas and context, and cache generated data URIs using a bounded LRU cache keyed by render parameters.
