## 2026-03-30 - Shared Canvas & Map Data URL Caching in Liquid Glass Filter
**Learning:** Re-creating dynamic canvas elements and performing `canvas.toDataURL()` on every SVG filter refresh causes significant GC pressure and CPU bottlenecking. Reusing a module-level shared canvas and storing Data URIs in a bounded Map LRU cache eliminates unnecessary allocations and redraw operations.
**Action:** Always reuse canvas contexts when generating transient image/SVG data, and cache serialized data URIs when input parameters repeat.
