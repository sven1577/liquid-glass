# Bolt's Journal

## 2025-08-07 - Canvas Creation and DataURL Caching
**Learning:** Frequent canvas creation in requestAnimationFrame / ResizeObserver causes high garbage collection pressure. Additionally, calling `canvas.toDataURL()` is highly CPU-intensive and slow.
**Action:** Reused a module-level shared canvas and implemented a size-limited Map cache for generated displacement maps to bypass canvas operations entirely for repeated or shared glass dimensions.
