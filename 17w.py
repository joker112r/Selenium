from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "\$100")
    )

button = browser.find_element(By.ID, "book")
button.click()

alert = browser.switch_to.alert
x = alert.text.split(" ")[-1]
y = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(y)
alert.accept()


