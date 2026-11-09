# Palette's Journal - UX & Accessibility Learnings

## 2025-05-18 - Keyboard Navigation in Spring-Physics Draggable Floating Cards
**Learning:** Adding keyboard accessibility to interactive floating cards powered by pointer-driven spring physics requires checking `e.target !== containerElement` on container `keydown` listeners. Otherwise, arrow key navigation inside nested inputs (like email fields or textareas) bubbles up to the card, causing unintended physics displacement and breaking text editing cursor movement.
**Action:** When adding arrow-key positioning to custom draggable container components that host interactive child elements, always guard with `if (e.target !== containerElement) return;` and update physics target positions (`tx`/`ty`) to preserve fluid spring animation.
