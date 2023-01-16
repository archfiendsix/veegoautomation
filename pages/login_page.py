from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.sign_in_button = (By.XPATH, "//button[text()='Sign in']")
        self.dashboard_header = (By.XPATH, "//h1")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()

    def wait_for_dashboard(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.dashboard_header, "Dashboard")
        )

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.dashboard_header).text == "Dashboard"