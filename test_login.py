from pages.login_page import LoginPage
from selenium import webdriver
import time
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://care.dev.env.veego.io/TZYSH9ACPDW/")

    login_page = LoginPage(driver)
    login_page.enter_username("ace.simon.g@gmail.com")
    login_page.enter_password("Qazwsx123!@#")
    login_page.click_sign_in()
    login_page.wait_for_dashboard()

    assert login_page.is_dashboard_displayed()
    time.sleep(30)
    driver.quit()

test_login()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()

# # Enter "ace.simon.g@gmail.com" to an input with id "username"
# driver.find_element_by_id("username").send_keys("ace.simon.g@gmail.com")

# # Enter "Qazwsx123!@#" to password input with id "password"
# driver.find_element_by_id("password").send_keys("Qazwsx123!@#")

# # Click on a button with "Sign in" label
# driver.find_element_by_xpath("//button[text()='Sign in']").click()

# # Wait until the page loads after slicking the sign in button
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

# # Check for if page's <h1></h1> element has the text "Dashboard"
# assert driver.find_element_by_tag_name("h1").text == "Dashboard"

# driver.quit()