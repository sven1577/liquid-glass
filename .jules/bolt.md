## 2025-05-10 - Liquid Glass Map Generation & Refresh Optimization
**Learning:** Generating displacement maps in `liquid-glass.js` via dynamic `canvas` creation and `toDataURL()` serialization on every `refresh()` call causes unnecessary CPU spikes and GC pressure.
**Action:** Reuse a single shared canvas context, cache generated data URIs in a bounded LRU Map, and short-circuit `refresh()` when element dimensions (`w`, `h`, `radius`) haven't changed.
