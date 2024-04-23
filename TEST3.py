import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://easysmarthub.ru/shop")

try:
    product_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-product_id="1008"] a'))
    )
    product_1.click()

    continue_shopping_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]'))
    )
    continue_shopping_button.click()

    product_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-product_id="1009"] a'))
    )
    product_2.click()

    continue_shopping_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]'))
    )
    continue_shopping_button.click()

    product_3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-product_id="1011"] a'))
    )
    product_3.click()

     promo_code_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "coupon_code"))
    )
    promo_code_field.send_keys("ERIK_CAT")

    apply_promo_code_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "apply_coupon"))
    )
    apply_promo_code_button.click()
  
    checkout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'[href="https://easysmarthub.ru/checkout/"]'))
    )
    checkout_button.click()

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'billing_email'))
    )
    email_field.send_keys("joker112r@gmail.com")

    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'billing_first_name'))
    )
    name_field.send_keys("Robert")

    second_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "billing_last_name"))
    )
    second_name_field.send_keys("Razuvaev")

    phone_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'billing_phone'))
    )
    phone_field.send_keys("+79990000000")
    time.sleep(5)

    submit_order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,'woocommerce_checkout_place_order'))
    )
    submit_order_button.click()

    card_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[autocomplete="cc-number"]'))
    )
    card_number_field.send_keys("5555555555554477")

    card_expiration_date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[autocomplete="cc-exp-month"]'))
    )
    card_expiration_date_field.send_keys("04")

    card_expiration_date_field_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[autocomplete="cc-exp-year"]'))
    )
    card_expiration_date_field_2.send_keys("28")

    card_cvv_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="CVC"]'))
    )
    card_cvv_field.send_keys("333")

    chek_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'send-email-invoice'))
    )
    chek_1.click()

    emlg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa-bankcard-field-name="invoice-email"]'))
    )
    emlg.send_keys('joker112r@gmail.com')

    subm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
    )
    subm.click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".confirmation-message"))
    )

    assert "Ваш заказ успешно оформлен" in confirmation_message.text

finally:
    driver.quit()
