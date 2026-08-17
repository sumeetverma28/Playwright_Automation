from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
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
    page.locator("//span[@class='oxd-userdropdown-tab']").click()
    page.locator("//ul[@class='oxd-dropdown-menu']").locator("//a[@href='/web/index.php/auth/logout']").click()
        
    # Invalid Username and Password
    page.locator("//input[@name='username']").fill("Invalidusername")
    page.locator("//input[@name='password']").fill("admin123")
    page.locator("//button[@type='submit']").click()
    page.wait_for_load_state()
    page.locator("//p[text()='Invalid credentials']").get_attribute("textContent")
    page.wait_for_timeout(5000)

    # Valid Username and Invalid Password
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("Invalidpassword")
    page.locator("//button[@type='submit']").click()
    page.wait_for_load_state()
    page.locator("//p[text()='Invalid credentials']").get_attribute("textContent")
    page.wait_for_timeout(5000)

    # Blank Username and Password
    page.locator("//input[@name='username']").fill("")  
    page.locator("//input[@name='password']").fill("")
    page.locator("//button[@type='submit']").click()
    page.wait_for_load_state()
    page.wait_for_timeout(5000)
    

    browser.close()