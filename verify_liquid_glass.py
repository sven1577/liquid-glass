import os
import sys
from playwright.sync_api import sync_playwright, expect

def main():
    print("Starting Playwright validation...")

    # Locate the absolute path of demo/index.html
    html_path = os.path.abspath("demo/index.html")
    if not os.path.exists(html_path):
        print(f"Error: Could not find demo index file at {html_path}")
        sys.exit(1)

    url = f"file://{html_path}"
    print(f"Navigating to: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Listen for console errors or exceptions
        errors = []
        page.on("pageerror", lambda err: errors.append(err))

        page.goto(url)

        # Wait for the card to be visible
        card = page.locator("#card")
        expect(card).to_be_visible(timeout=5000)

        # Take an initial screenshot
        os.makedirs("verification", exist_ok=True)
        screenshot_path = "verification/verification.png"
        page.screenshot(path=screenshot_path)
        print(f"Saved initial screenshot to {screenshot_path}")

        # Verify no console errors occurred during page load
        if errors:
            print("Errors detected during page load:")
            for err in errors:
                print(err)
            sys.exit(1)

        print("Success: Page loaded without console errors!")
        browser.close()

if __name__ == "__main__":
    main()
