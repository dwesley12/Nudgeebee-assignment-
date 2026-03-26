import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/category_products/6")

driver.find_element(By.XPATH, "//a[@data-product-id='33']").click()


btn_success = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"add-to-cart")) #Add product to cart
    );btn_success.click()


#verify cart quantity
view_cart = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "View Cart"))
    );view_cart.click()

cart_quantity = driver.find_element(By.XPATH,"//td[@class = 'cart_quantity']/button").text
print(cart_quantity)

#verify product details
Cart_item_description = driver.find_element(By.XPATH, "//a[@href = '/product_details/33']").text
print(Cart_item_description)

Cart_item_price = driver.find_element(By.XPATH,"//td[@class = 'cart_price']").text
print(Cart_item_price)

Cart_total = driver.find_element(By.XPATH,"//p[@class = 'cart_total_price']").text
print(Cart_total)

remove_cart = WebDriverWait(driver,10).until(                      #remove product from cart and verify cart is empty
    EC.presence_of_element_located((By.CLASS_NAME,"fa-times"))
);remove_cart.click()
time.sleep(3)
cart_empty = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-center b"))
);
assert "Cart is empty!" in cart_empty.text
print(cart_empty)
driver = WebDriverWait(driver, 15)