#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver
#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import Select


import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")


    span_element_1 = browser.find_element(By.ID, "num1")
    text_from_span_1 = span_element_1.text
    number_from_span_1 = int(text_from_span_1)
    print(number_from_span_1)
    span_element_2 = browser.find_element(By.ID, "num2")
    text_from_span_2 = span_element_2.text
    number_from_span_2 = int(text_from_span_2)
    print(number_from_span_2)
    span_sums = number_from_span_1 + number_from_span_2
    print(span_sums)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(span_sums))
    btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    btn.click()


   


   
   
finally:
    time.sleep(5)
    browser.quit()










