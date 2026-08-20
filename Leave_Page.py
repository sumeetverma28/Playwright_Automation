from playwright.sync_api import sync_playwright  # type: ignore[import-not-found]

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    context = browser.new_context(viewport=None)
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

   
    def test_login():
        # Login with valid credentials
        #page.goto(")
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
        page.wait_for_timeout(3000)
        page.wait_for_load_state()
        page.wait_for_timeout(3000)
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[1]").clear()
        page.wait_for_timeout(3000)
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[1]").fill("2024-06-01")
        page.wait_for_timeout(3000)
        txt=page.locator("//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][1]").get_text_content()
        print(txt)
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[2]").clear()
        page.locator("(//input[@placeholder='yyyy-dd-mm'])[2]").fill("2024-06-30")
        page.wait_for_timeout(3000)
        browser.close()


test_login()
