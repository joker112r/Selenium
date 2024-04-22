from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setting up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Going to the website
driver.get("https://easysmarthub.ru/shop")

# Adding the first product to the cart
product_1 = driver.find_element(By.CSS_SELECTOR, "a[href='?add-to-cart=1008']")
product_1.click()

# Waiting for 5 seconds
time.sleep(5)

# Continuing shopping
continue_shopping_button = driver.find_element(By.CLASS_NAME, "page-template-default")
continue_shopping_button.click()

# Adding the second product to the cart
product_2 = driver.find_element(By.CSS_SELECTOR, "a[href='?add-to-cart=1009']")
product_2.click()

# Waiting for 5 seconds
time.sleep(5)

# Continuing shopping
continue_shopping_button = driver.find_element(By.CLASS_NAME, "page-template-default")
continue_shopping_button.click()

# Adding the third product to the cart
product_3 = driver.find_element(By.CSS_SELECTOR, "a[href='?add-to-cart=1011']")
product_3.click()

# Waiting for 5 seconds
time.sleep(5)

# Going to the checkout page
checkout_button = driver.find_element(By.CLASS_NAME, "page-template-default")
checkout_button.click()

# Closing the browser
driver.quit()
