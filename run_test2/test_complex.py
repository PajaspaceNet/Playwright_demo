# run_test2/test_complex.py
import pytest
from playwright.sync_api import sync_playwright

def run_test_in_browser(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.example.com")
        assert "Example Domain" in page.title()
        print(f"✅ Test passed on {browser_name}")
        browser.close()

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_run_in_browser(browser_name):
    run_test_in_browser(browser_name)
