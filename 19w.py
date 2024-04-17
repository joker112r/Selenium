from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class RegTestForm(unittest.TestCase):
    def test_registration_form_on_valible(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        
        first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        
        first_name.send_keys("Robert")
        last_name.send_keys("Robert2")
        email.send_keys("joker112r@gmail.com")
        
        submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_button.click()
        
        success_message = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(success_message, "Congratulations! You have successfully registered!")

        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()



