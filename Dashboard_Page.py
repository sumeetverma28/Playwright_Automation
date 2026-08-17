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
        page.locator("//span[text()='Dashboard']")
        page.locator("//span[@class='oxd-userdropdown-tab']").click()
        page.locator("//ul[@class='oxd-dropdown-menu']").locator("//a[@href='/web/index.php/auth/logout']").click()
    
    test_login()
    browser.close()