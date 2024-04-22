import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

class RegTestForm(unittest.TestCase):

    def test_registration_form_on_valible(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")

            first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
            first_name.send_keys("Robert1")
    
            last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
            last_name.send_keys("Robert2")
    
            email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
            email.send_keys("joker112r@gmail.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Неверный текст приветствия")
        finally:
            time.sleep(5)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
