#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import time
import math
import os


try:
    browser = webdriver.Chrome()
    #говорим webdriver искать каждый элемент в течени 5 секунд
   
    browser.get("http://suninjuly.github.io/wait2")
   
    btn = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,'verify')))
    btn.click()
    message = browser.find_element(By.ID, 'verify_message')
    assert 'successful' in message.text
 
finally:
    time.sleep(5)
    browser.quit()