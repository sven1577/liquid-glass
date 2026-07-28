## 2026-07-28 - Optimizing Dynamic Canvas & Layout Thrashing in Liquid Glass SVG Filter
**Learning:** High-frequency layout changes and rapid event loops (e.g., resizing or drag actions triggering canvas updates) face critical performance bottlenecks due to:
1. GC pressure caused by dynamic allocation/garbage collection of new canvas elements and 2D contexts inside `makeMap()`.
2. Heavy CPU cost of serializing the canvas with `.toDataURL()` on every draw.
3. Layout thrashing and browser reflows caused by calling `getComputedStyle(el)` frequently inside the resize loop.

**Action:**
1. Re-use a single `sharedCanvas` and `sharedCtx` at the module level.
2. Cache generated maps inside a fixed-size LRU `mapCache` (Map-based with a size limit of 50) to skip `.toDataURL()`.
3. Cache raw `borderTopLeftRadius` style values locally on the instance scope so we only read `getComputedStyle` once (or when explicitly forced using `refresh(true)`).
