from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Ждем, пока цена станет равной 100$
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "\$100")
        )

    # Нажимаем на кнопку "Book" после того, как цена стала \$100
    button = browser.find_element(By.ID, "book")
    button.click()

    # Получаемаемаем значение x из алерта
    alert = browser.switch_to.alert
    x = alert.text.split()[-1]
    alert.accept()

    # Вычисляем результат и вводим его в поле
    y = str(math.log(abs(12 * math.sin(float(x)))))
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отправляем форму
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Ждем некоторое время, прежде чем закрыть браузер
    time.sleep(5)
    browser.quit()