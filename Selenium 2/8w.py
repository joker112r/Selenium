from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for i, element in enumerate(elements, start=1):
        element.send_keys(f'Robert{i}')
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()