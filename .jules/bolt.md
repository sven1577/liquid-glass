## 2025-02-18 - Optimized Canvas and Layout Thrashing in Liquid Glass
**Learning:** Dynamic creation of canvas elements and repeated calls to toDataURL() cause heavy garbage collection and CPU overhead. Also, layout querying like getComputedStyle() on ResizeObserver callbacks triggers layout thrashing.
**Action:** Reused a single module-scoped canvas element, cached the toDataURL() results using an LRU Map, cached getComputedStyle() results using a WeakMap, and stored previous element dimensions to skip redundant rendering on identical sizes.
