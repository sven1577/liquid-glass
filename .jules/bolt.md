# Bolt's Journal - Critical Performance Learnings

## 2025-02-23 - Shared Canvas & Data URI Caching for SVG Displacement
**Learning:** Dynamic canvas allocation and repeated `toDataURL()` calls during animations produce significant GC pressure and main-thread CPU load. Reusing a single shared canvas context and caching generated data URIs in a bounded LRU cache drastically reduces frame render time and memory allocations. Furthermore, element dimension checks (`lastW`, `lastH`, `lastRadius`) prevent unnecessary displacement map regenerations during filter refreshes.
**Action:** When working with canvas-generated SVG filter maps or dynamic textures, always reuse canvas elements across renders, cache data URIs with an LRU cache, and short-circuit refreshes when element dimensions have not changed.
