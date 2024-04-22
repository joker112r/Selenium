import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ContactFormTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.link = "https://easysmarthub.ru/contact/"

#1.На возможность отправить форму без заполнения
    def test_submit_empty_form(self):
        self.browser.get(self.link)
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        self.assertIn("Пожалуйста, заполните это поле.", self.browser.page_source)

#2.На возможность отправить форму частично заполненную
    def test_submit_partial_form(self):
        self.browser.get(self.link)
        input_1 = self.browser.find_element(By.NAME, "your-name")
        input_1.send_keys('Robert')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        self.assertIn("Пожалуйста, заполните это поле.", self.browser.page_source)

#3.На возможность отправить форму с email в виде обычного текста
    def test_submit_email_as_plain_text(self):
        self.browser.get(self.link)
        input_2 = self.browser.find_element(By.NAME, "your-email")
        input_2.send_keys('joker112r@gmail.com')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        self.assertIn("Пожалуйста, введите корректный адрес электронной почты.", self.browser.page_source)

#4.На возможность отправить данные формы без галочки на согласие
    def test_submit_without_consent_checkbox(self):
        self.browser.get(self.link)
        input_1 = self.browser.find_element(By.NAME, "your-name")
        input_1.send_keys('Robert')
        input_2 = self.browser.find_element(By.NAME, "your-email")
        input_2.send_keys('joker112r@gmail.com')
        input_3 = self.browser.find_element(By.NAME, "your-subject")
        input_3.send_keys('Kurs')
        input_4 = self.browser.find_element(By.NAME, "your-message")
        input_4.send_keys('Здравствуйте')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        self.assertIn("Пожалуйста, подтвердите свое согласие с обработкой данных.", self.browser.page_source)

#5.Вся форма заполнена корректно и все галочки приняты.
    def test_submit_valid_form(self):
        self.browser.get(self.link)
        input_1 = self.browser.find_element(By.NAME, "your-name")
        input_1.send_keys('Robert')
        input_2 = self.browser.find_element(By.NAME, "your-email")
        input_2.send_keys('joker112r@gmail.com')
        input_3 = self.browser.find_element(By.NAME, "your-subject")
        input_3.send_keys('Kurs')
        input_4 = self.browser.find_element(By.NAME, "your-message")
        input_4.send_keys('Здравствуйте')
        checkbox = self.browser.find_element(By.CLASS_NAME, "gdpr-term")
        checkbox.click()
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()
        time.sleep(5)
        self.assertIn("Ваше сообщение было успешно отправлено.", self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()