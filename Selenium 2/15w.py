from selenium import webdriver
import time
import math
from selenium.webdriver.common.alert import Alert

url = "https://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()
driver.get(url)

try:
    driver.find_element("css selector", "button[type='submit']").click()
    confirm = Alert(driver)
    confirm.accept()

    input_value = driver.find_element("id", "input_value").text
    result = str(math.log(abs(12*math.sin(int(input_value)))))
    driver.find_element("id", "answer").send_keys(result)
    
    driver.find_element("css selector", "button[type='submit']").click()

finally:
    time.sleep(10)
    driver.quit()