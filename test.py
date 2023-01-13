from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = "/Users/mikee/Downloads/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://care.dev.env.veego.io/TZYSH9ACPDW/")
print(driver.title)
driver.implicitly_wait(10)
usernameTextbox = driver.find_element(By.XPATH,'//*[@id="username"]')
usernameTextbox.send_keys("GG-ext-qa")
passwordTextbox = driver.find_element(By.ID,'password')
passwordTextbox.send_keys("bawal123")
driver.implicitly_wait(10)
passwordTextbox = driver.find_element(By.ID,'kc-login')
passwordTextbox.click()
driver.implicitly_wait(30000)
time.sleep(45)