## 2025-08-22 - SVG Displacement Map Caching and Canvas Reuse
**Learning:** Generating SVG displacement data URIs via dynamic `<canvas>` elements and `toDataURL()` in `liquid-glass.js` causes significant CPU blocking (~14ms per call) and GC overhead. Reusing a single offscreen canvas and context, along with caching generated data URIs in a bounded LRU cache keyed by canvas parameters, reduces execution overhead to virtually zero (~0.007ms).
**Action:** Always reuse canvas/context instances and cache data URI results when generating SVG filter maps dynamically in JavaScript.
