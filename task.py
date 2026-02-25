from playwright.sync_api import sync_playwright

EXPECTED_TITLE = "Fast and reliable end-to-end testing for modern web apps | Playwright"

def run_test(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        
        actual_title = page.title()
        assert actual_title == EXPECTED_TITLE
        
        browser.close()


def test_title_chromium():
    run_test("chromium")


def test_title_firefox():
    run_test("firefox")
