## 2026-08-29 - Shared Canvas & LRU Caching for Dynamic SVG Displacement Maps
**Learning:** In canvas-to-SVG displacement workflows (like `liquid-glass.js`), creating canvas elements dynamically and invoking `.toDataURL()` on every update loop/resize causes significant memory allocation churn and CPU overhead.
**Action:** Reuse a single module-scoped offscreen canvas context and cache generated data URIs using a Map-based LRU cache. Additionally, early-return in element refresh functions when dimensions (`w`, `h`, `radius`) have not changed.
