from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
from email.mime.text import MIMEText

# Setting up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Going to the website
driver.get("https://easysmarthub.ru/shop")

# Adding the first product to the cart
product_1 = driver.find_element(By.CLASS_NAME, "product-tile__container").find_element(By.TAG_NAME, "a")
product_1.click()
add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-primary")
add_to_cart_button.click()

# Continuing shopping
continue_shopping_button = driver.find_element(By.CLASS_NAME, "btn-secondary")
continue_shopping_button.click()

# Adding the second product to the cart
product_2 = driver.find_element(By.CLASS_NAME, "product-tile__container").find_element(By.TAG_NAME, "a")
product_2.click()
add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-primary")
add_to_cart_button.click()

# Continuing shopping
continue_shopping_button = driver.find_element(By.CLASS_NAME, "btn-secondary")
continue_shopping_button.click()

# Going to the checkout page
checkout_button = driver.find_element(By.CLASS_NAME, "btn-primary")
checkout_button.click()

# Filling in the required fields
first_name_field = driver.find_element(By.ID, "checkout_shipping_address_first_name")
first_name_field.send_keys("John")

last_name_field = driver.find_element(By.ID, "checkout_shipping_address_last_name")
last_name_field.send_keys("Doe")

email_field = driver.find_element(By.ID, "checkout_shipping_address_email")
email_field.send_keys("john.doe@example.com")

address_field = driver.find_element(By.ID, "checkout_shipping_address_address1")
address_field.send_keys("123 Main St")

city_field = driver.find_element(By.ID, "checkout_shipping_address_city")
city_field.send_keys("Anytown")

state_field = driver.find_element(By.ID, "checkout_shipping_address_province")
state_field.send_keys("CA")

zip_code_field = driver.find_element(By.ID, "checkout_shipping_address_zip")
zip_code_field.send_keys("12345")

phone_field = driver.find_element(By.ID, "checkout_shipping_address_phone")
phone_field.send_keys("555-123-4567")

# Going to the payment page
continue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
continue_button.click()

# Filling in the payment fields
card_number_field = driver.find_element(By.ID, "credit_card_number")
card_number_field.send_keys("4111 1111 1111 1111")

expiration_month_field = driver.find_element(By.ID, "credit_card_month")
expiration_month_field.send_keys("01")

expiration_year_field = driver.find_element(By.ID, "credit_card_year")
expiration_year_field.send_keys("2025")

cvv_field = driver.find_element(By.ID, "credit_card_verification_value")
cvv_field.send_keys("123")

# Placing the order
place_order_button = driver.find_element(By.CLASS_NAME, "btn-primary")
place_order_button.click()

# Verifying that the test was successful
time.sleep(10)  # Wait for the email to arrive

# Checking the email
email_address = "john.doe@example.com"
email_password = "password"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_address, email_password)

    _, emails = smtp.search(None, f"FROM:'EasySmartHub' TO:'{email_address}' SUBJECT:'Your order confirmation'")

    for email_id in emails:
        _, msg = smtp.fetch(email_id, "(RFC822)")
        msg_text = msg[0][1].decode("utf-8")

        if "Your order has been placed successfully" in msg_text:
            print("Test passed! Order confirmation email received.")
            break
    else:
        print("Test failed. Order confirmation email not received.")

# Closing the browser
driver.quit()