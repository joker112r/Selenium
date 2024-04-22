import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file_path = r"CC:\Users\AuroraPC\Desktop\Selenium\Selenium\T112.jpg"
file_input = browser.find_element(By.ID, 'kurs-zakonchilsya')
            file_input.send_keys(file_path)


class TestEasysmarthub(unittest.TestCase):

    # Заполнить все поля, кроме Email (jpg картинка) и чекбокс
    def test_partially_filled_form_without_email(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")

            # Заполните поля "Имя", "Тема" и "Сообщение"
            input_name = browser.find_element(By.NAME, 'your-name')
            input_name.send_keys("Robert")
            input_subject = browser.find_element(By.NAME, 'your-subject')
            input_subject.send_keys("Robert1")
            input_message = browser.find_element(By.NAME, 'your-message')
            input_message.send_keys("Kurs")

            # Ожидайте появления сообщения об ошибке
            error_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))

            # Проверьте текст сообщения об ошибке
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", error_message.text, "should be equal")

            # Найдите кнопку "Отправить"
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

            # Выполните JavaScript-код для клика на кнопку
            browser.execute_script("arguments[0].click();", button_submit)

            # Ожидайте появления сообщения об ошибке
            error_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))

            # Проверьте текст сообщения об ошибке
            self.assertEqual("The e-mail address entered is invalid.", error_message.text, "should be equal")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
