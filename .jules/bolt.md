## 2024-08-05 - Avoid dynamic canvas allocation and toDataURL cost
**Learning:** Canvas allocation inside drawing loops causes significant Garbage Collection overhead, and `toDataURL` is highly expensive due to encoding. Dimension checks on instance refresh calls can completely bypass these when no layout change has occurred.
**Action:** Always reuse a shared canvas for synchronous image generation tasks, use an LRU cache for generated data URLs, and cache dimensions on instances to guard DOM/attribute updates.
