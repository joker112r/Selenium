import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

class RegTestForm(unittest.TestCase):

    def test_registration_form_on_valible(self):

        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

        try:
            browser = webdriver.Chrome()
            browser.get("https://suninjuly.github.io/get_attribute.html")

            x_element = browser.find_element(By.TAG_NAME, "img")
            x = x_element.get_attribute("valuex")
            y = calc(x)

            input1 = browser.find_element(By.ID, "answer")
            input1.send_keys(y)
            option1 = browser.find_element(By.ID, "robotCheckbox")
            option1.click()
            option2 = browser.find_element(By.ID, "robotsRule")
            option2.click()
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

        finally:
            time.sleep(5)
            browser.quit()

if __name__ == "__main__":
    unittest.main()