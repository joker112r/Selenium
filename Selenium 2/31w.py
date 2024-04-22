import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestEasysmarthub(unittest.TestCase):

    # Отправить форму без заполненных полей
    def test_empty_form_without_fields(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")

            # Найдите кнопку "Отправить"
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

            # Выполните JavaScript-код для клика на кнопку
            browser.execute_script("arguments[0].click();", button_submit)

            # Ожидайте появления сообщения об ошибке
            T112 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))

            # Проверьте текст сообщения об ошибке
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", T112.text, "should be equal")

        finally:
            browser.quit()

    # Отправить форму без файла
    def test_empty_form_without_file(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")

            # Найдите кнопку "Отправить"
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

            # Выполните JavaScript-код для клика на кнопку
            browser.execute_script("arguments[0].click();", button_submit)

            # Ожидайте появления сообщения об ошибке
            T112 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))

            # Проверьте текст сообщения об ошибке
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", T112.text, "should be equal")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
