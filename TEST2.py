import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
link = 'https://easysmarthub.ru/shop'


class TestEasysmarthub(unittest.TestCase):
    def test_1_all(self):
        try:
            driver = webdriver.Chrome()
            driver.get(link)
            add_to_cart_button_1 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1008"]')
            add_to_cart_button_1.click()
            continue_shopping_button = driver.find_element(By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]')
            continue_shopping_button.click()
            add_to_cart_button_2 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1009"]')
            add_to_cart_button_2.click()
            continue_shopping_button = driver.find_element(By.CSS_SELECTOR, '[class="button wc-forward wp-element-button"]')
            continue_shopping_button.click()
            add_to_cart_button_3 = driver.find_element(By.CSS_SELECTOR, '[data-product_id="1011"]')
            add_to_cart_button_3.click()

            checkout_button = driver.find_element(By.CSS_SELECTOR, '[href="https://easysmarthub.ru/checkout/"]')
            checkout_button.click()
            first_name_field = driver.find_element(By.ID,'billing_first_name')
            first_name_field.send_keys()
            last_name_field = driver.find_element(By.ID,'billing_last_name')
            last_name_field.send_keys()
            phone_field = driver.find_element(By.ID,'billing_phone')
            phone_field.send_keys()
            email_field = driver.find_element(By.ID,'billing_email')
            email_field.send_keys()
            time.sleep(5)
            place_order_button = driver.find_element(By.NAME,'woocommerce_checkout_place_order')
            place_order_button.click()
            error_message = driver.find_element(By.CSS_SELECTOR,'[role="alert"]').text
            self.assertEqual(error_message, 'является обязательным полем.')
            print('good')



        finally:
            time.sleep(20)
            driver.quit()

if __name__ =="__main__":
    unittest.main()
