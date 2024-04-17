from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class RegTestForm(unittest.TestCase):
    def test_registration_form_on_valid(self):
        # Запускаем WebDriver (Chrome в данном случае)
        driver = webdriver.Chrome()
        try:
            # Открываем страницу регистрации
            driver.get("http://suninjuly.github.io/registration1.html")
            
            # Находим поля ввода
            first_name = driver.find_element(By.CSS_SELECTOR, "input.first[required]")
            last_name = driver.find_element(By.CSS_SELECTOR, "input.second[required]")
            email = driver.find_element(By.CSS_SELECTOR, "input.third[required]")
            
            # Вводим данные в поля
            first_name.send_keys("JohnJohnJohn")
            last_name.send_keys("Doe")
            email.send_keys("john.doe@example.com")
            
            # Находим и нажимаем кнопку отправки формы
            submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()
            
            # Проверяем успешную регистрацию
            success_message = driver.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(success_message, "Congratulations! You have successfully registered!")

        finally:
            # Закрываем браузер после выполнения теста
            driver.quit()

if __name__ == "__main__":
    unittest.main()