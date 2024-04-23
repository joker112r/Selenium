import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://easysmarthub.ru/shop")

product_1 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1008"]')
product_1.click()

continue_shopping_button = driver.find_element(By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]')
continue_shopping_button.click()

product_2 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1009"]')
product_2.click()

continue_shopping_button = driver.find_element(By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]')
continue_shopping_button.click()

product_3 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1011"]')
product_3.click()

checkout_button = driver.find_element(By.CSS_SELECTOR,'[href="https://easysmarthub.ru/checkout/"]')
checkout_button.click()

# Заполнение полей оформления заказа
email_field = driver.find_element(By.ID,'billing_email')
email_field.send_keys("joker112r@gmail.com")

name_field = driver.find_element(By.ID,'billing_first_name')
name_field.send_keys("Robert")

second_name_field = driver.find_element(By.ID, "billing_last_name")
second_name_field.send_keys("Razuvaev")

phone_field = driver.find_element(By.ID,'billing_phone')
phone_field.send_keys("+79990000000")
time.sleep(5)

submit_order_button = driver.find_element(By.NAME,'woocommerce_checkout_place_order')
submit_order_button.click()
driver.implicitly_wait(7)

card_number_field = driver.find_element(By.CSS_SELECTOR, '[autocomplete="cc-number"]')
card_number_field.send_keys("5555555555554477")

card_expiration_date_field = driver.find_element(By.CSS_SELECTOR, '[autocomplete="cc-exp-month"]')
card_expiration_date_field.send_keys("04")

card_expiration_date_field_2 = driver.find_element(By.CSS_SELECTOR, '[autocomplete="cc-exp-year"]')
card_expiration_date_field_2.send_keys("28")

card_cvv_field = driver.find_element(By.CSS_SELECTOR, '[placeholder="CVC"]')
card_cvv_field.send_keys("333")
chek_1 = driver.find_element(By.ID, 'send-email-invoice')
chek_1.click()
time.sleep(5)
emlg = driver.find_element(By.CSS_SELECTOR, '[data-qa-bankcard-field-name="invoice-email"]')
emlg.send_keys('joker112r@gmail.com')
subm = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
subm.click()
# Проверка успешности теста
confirmation_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".confirmation-message"))
)

assert "Ваш заказ успешно оформлен" in confirmation_message.text

driver.quit()

