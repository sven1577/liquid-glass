# Bolt's Journal - Critical Learnings Only

## 2026-03-06 - Reducing GC Pressure and Forced Reflows in liquid-glass.js
**Learning:** Instantiating new canvases and repeatedly converting to data URLs creates significant GC pressure. Additionally, querying DOM layout dimensions (`offsetWidth`, `offsetHeight`) and computing styles inside `ResizeObserver` callbacks or during continuous frames can trigger forced synchronous layouts (reflows). Avoiding these by reusing a shared canvas, caching generated maps using a bounded LRU cache, and caching layout measurements at the instance level drastically improves frame-rate and layout stability.
**Action:** Share a single canvas instance globally, cache data URLs in a bounded native Map (LRU), and keep track of measured width and height inside each liquid-glass instance closure to skip rendering if the size hasn't changed.
