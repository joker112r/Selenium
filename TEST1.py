import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера Selenium
driver = webdriver.Chrome()
driver.maximize_window()

# Переход на сайт
driver.get("https://easysmarthub.ru/shop")

# Добавление первого товара в корзину
product_1 = driver.find_element(By.CSS_SELECTOR, ".product-card__button")
product_1.click()

# Нажатие на кнопку "Продолжить покупки"
continue_shopping_button = driver.find_element(By.CSS_SELECTOR, ".btn-continue-shopping")
continue_shopping_button.click()

# Добавление второго товара в корзину
product_2 = driver.find_element(By.CSS_SELECTOR, ".product-card__button")
product_2.click()

# Нажатие на кнопку "Продолжить покупки"
continue_shopping_button = driver.find_element(By.CSS_SELECTOR, ".btn-continue-shopping")
continue_shopping_button.click()

# Добавление третьего товара в корзину
product_3 = driver.find_element(By.CSS_SELECTOR, ".product-card__button")
product_3.click()

# Переход к оформлению заказа
checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn-checkout")
checkout_button.click()

# Заполнение полей оформления заказа
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("joker112r@gmail.com")

name_field = driver.find_element(By.ID, "name")
name_field.send_keys("Robert")

second_name_field = driver.find_element(By.ID, "billing_last_name")
second_name_field.send_keys("Razuvaev")

phone_field = driver.find_element(By.ID, "phone")
phone_field.send_keys("+79990000000")

# Переход к оплате
submit_order_button = driver.find_element(By.CSS_SELECTOR, ".btn-submit-order")
submit_order_button.click()

# Заполнение полей оплаты
card_number_field = driver.find_element(By.ID, "card-number")
card_number_field.send_keys("5555555555554477")

card_expiration_date_field = driver.find_element(By.ID, "card-expiration-date")
card_expiration_date_field.send_keys("04/28")

card_cvv_field = driver.find_element(By.ID, "card-cvv")
card_cvv_field.send_keys("333")

# Проверка успешности теста
confirmation_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".confirmation-message"))
)

assert "Ваш заказ успешно оформлен" in confirmation_message.text

driver.quit()
