import os
from playwright.sync_api import sync_playwright, expect

def verify_ux():
    print("Starting Playwright verification...")
    # Get absolute path to demo/index.html
    demo_path = os.path.abspath("demo/index.html")
    file_url = f"file://{demo_path}"
    print(f"Loading {file_url}")

    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        # Force a reasonable viewport
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Navigate
        page.goto(file_url)

        # Locate the card
        card = page.locator("#card")
        expect(card).to_be_visible()

        # Take a screenshot of default state
        print("Taking initial screenshot...")
        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/initial.png")

        # Programmatically focus the card
        print("Focusing the card...")
        card.focus()

        # Verify card is focused
        expect(card).to_be_focused()

        # Take screenshot of focused state (should show focus outline)
        print("Taking focused card screenshot...")
        page.screenshot(path="verification/focused_card.png")

        # Store initial position from styling or transform
        transform_initial = card.evaluate("el => el.style.transform")
        print(f"Initial transform: {transform_initial}")

        # Trigger Arrow key presses to move the card right and down
        print("Pressing ArrowRight and ArrowDown keys...")
        card.press("ArrowRight")
        card.press("ArrowRight")
        card.press("ArrowDown")

        # Let physics animate for a short while
        page.wait_for_timeout(1000)

        # Retrieve transform again to check movement
        transform_after = card.evaluate("el => el.style.transform")
        print(f"Transform after Arrow keys: {transform_after}")

        # We expect position to have changed from initial position (or we check coords or transform updates)
        assert transform_initial != transform_after, f"Expected card transform to change! Before: {transform_initial}, After: {transform_after}"
        print("Keyboard-driven physics verified successfully!")

        # Move focus to text input
        email_input = page.get_by_label("Email address")
        email_input.focus()
        expect(email_input).to_be_focused()
        print("Taking focused email input screenshot...")
        page.screenshot(path="verification/focused_input.png")

        # Focus switch checkbox/track
        # The checkbox has focus but we styled its sibling switch-track.
        checkbox = page.locator("input[type='checkbox']")
        checkbox.focus()
        expect(checkbox).to_be_focused()
        print("Taking focused switch track screenshot...")
        page.screenshot(path="verification/focused_switch.png")

        # Clean up browser
        browser.close()
        print("Verification complete!")

if __name__ == "__main__":
    verify_ux()
