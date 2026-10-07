## 2025-05-18 - ARIA Live Region Announcement Lifecycle
**Learning:** Overwriting a form's `innerHTML` with a newly created element containing `aria-live="polite"` prevents screen readers (VoiceOver, NVDA) from announcing status updates because the live region was not present in the DOM prior to the text update.
**Action:** Keep the `aria-live="polite"` container in the DOM at all times (using `hidden` attribute or empty state) and update its text content directly upon status changes.
