## 2026-08-02 - Style Caching and Memory Management with WeakMap in Shared DOM Libraries
**Learning:** When building shared UI libraries that cache DOM element properties (like `border-radius` to avoid layout thrashing), caching DOM elements as keys in a standard `Map` introduces severe memory leaks because strong references prevent elements removed from the DOM from being garbage collected.
**Action:** Always use `WeakMap` instead of standard `Map` when caching properties associated with DOM nodes as keys so garbage collection can clean them up automatically when removed from the DOM.
