from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Products").click()
time.sleep(5)
driver.find_element(By.NAME,"search").send_keys("tshirt") #search for a product by keyword
driver.find_element(By.ID,"submit_search").click()
expected_url = "https://automationexercise.com/products?search=tshirt"
Actual_url = driver.current_url
assert expected_url in Actual_url
message = driver.find_element(By.NAME,"search").get_attribute("value")
assert "tshirt" in message

#add category filter

driver.find_element(By.LINK_TEXT,"MEN").click()

category_jeans = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"JEANS"))
);category_jeans.click()

product_detail = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//a[@href = '/product_details/33']")));product_detail.click()
product_details = driver.find_element(By.XPATH,"//div[@class = 'product-information']/h2").text #verify product details
print(product_details)


wait = WebDriverWait(driver, 15)