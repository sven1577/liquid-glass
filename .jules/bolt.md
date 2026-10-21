## 2026-07-09 - Reuse shared canvas and LRU cache for SVG displacement map generation
**Learning:** Generating displacement maps dynamically created short-lived HTMLCanvasElement objects and triggered expensive canvas 2D rendering and `toDataURL()` serialization on every `refresh()`.
**Action:** Reuse a module-scoped shared 2D canvas context and cache `toDataURL()` results in a Map-based bounded LRU cache. Cache element dimensions (`lastW`, `lastH`, `lastRadius`) on instances to short-circuit `refresh()` when layout is unchanged.
