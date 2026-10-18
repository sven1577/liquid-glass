## 2025-05-18 - Keyboard Navigation for Interactive Physics Containers & Pre-existing Live Regions

**Learning:** When adding keyboard navigation (e.g. arrow keys) to an interactive physics container that contains child form controls, always check `if (e.target !== containerElement) return;` to prevent arrow keys typed inside child inputs/buttons from triggering container displacement physics or preventing standard text input behavior. Additionally, `aria-live` elements must be initialized empty in the DOM rather than injected dynamically for screen readers to reliably announce status updates.
**Action:** Guard container-level keyboard event listeners against bubbling child events and initialize persistent live status containers in static markup.
