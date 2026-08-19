from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def test_login():
        # Login with valid credentials
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_load_state()
        page.wait_for_timeout(5000)
        print(page.title())
        page.locator("//input[@name='username']").fill("Admin")
        page.locator("//input[@name='password']").fill("admin123")
        page.locator("//button[@type='submit']").click()
        page.wait_for_load_state()
        page.wait_for_timeout(5000)
        page.locator("//span[text()='Dashboard']").click()
        page.wait_for_timeout(8000)
        page.locator("//span[text()='Leave']").click()
        page.wait_for_load_state()
        page.wait_for_timeout(3000)
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[1]").clear()
        page.wait_for_timeout(3000)
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[1]").fill("2024-06-01")
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[2]").fill("2024-06-30")
        page.wait_for_timeout(3000)
        browser.close()


    test_login()
