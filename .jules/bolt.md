## 2025-02-23 - Reuse canvas & LRU map caching in liquid-glass.js
**Learning:** Recreating dynamic `<canvas>` elements and executing `canvas.toDataURL()` during element updates/resizes introduces heavy GC pressure and CPU bottlenecks.
**Action:** Use a module-scoped shared canvas/2D context, store generated data URIs in a bounded LRU Map cache, and short-circuit instance `refresh()` calls when element dimensions and corner radius haven't changed.
