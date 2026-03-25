import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/") #navigate to login page
driver.maximize_window()


driver.find_element(By.ID, "username").send_keys("student") #login with valid credentials
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME, "btn").click()
message = driver.find_element(By.CLASS_NAME,"post-title").text
assert "Logged In Successfully" in message # verify successful login
driver.find_element(By.LINK_TEXT,"Log out").click()
assert "practice-test-login" in driver.current_url #logout and verify redirect back to the login page
time.sleep(10)