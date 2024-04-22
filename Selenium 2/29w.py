import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#1.На возможность отправить форму без заполнения
def test_submit_form_without_filling(browser):
    browser.get("https://easysmarthub.ru/contact/")
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    time.sleep(5)
    assert "Пожалуйста, заполните это поле" in browser.page_source

#2.На возможность отправить форму частично заполненную
def test_submit_partial_filled_form(browser):
    browser.get("https://easysmarthub.ru/contact/")
    input_1 = browser.find_element(By.NAME, "your-name")
    input_1.send_keys('Robert')
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    time.sleep(5)
    assert "Пожалуйста, заполните это поле." in browser.page_source

#3.На возможность отправить форму с email в виде обычного текста
def test_submit_form_with_plain_text_email(browser):
    browser.get("https://easysmarthub.ru/contact/")
    input_1 = browser.find_element(By.NAME, "your-name")
    input_1.send_keys('Robert')
    input_2 = browser.find_element(By.NAME, "your-email")
    input_2.send_keys('joker112r')
    input_3 = browser.find_element(By.NAME, "your-subject")
    input_3.send_keys('Kurs')
    input_4 = browser.find_element(By.NAME, "your-message")
    input_4.send_keys('Здравствуйте')
    checkbox = browser.find_element(By.CLASS_NAME, "gdpr-term")
    checkbox.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    time.sleep(5)
    assert "Пожалуйста, введите корректный адрес электронной почты." in browser.page_source

#4.На возможность отправить данные формы без галочки на согласие
def test_submit_form_without_consent(browser):
    browser.get("https://easysmarthub.ru/contact/")
    input_1 = browser.find_element(By.NAME, "your-name")
    input_1.send_keys('Robert')
    input_2 = browser.find_element(By.NAME, "your-email")
    input_2.send_keys('joker112r@gmail.com')
    input_3 = browser.find_element(By.NAME, "your-subject")
    input_3.send_keys('Kurs')
    input_4 = browser.find_element(By.NAME, "your-message")
    input_4.send_keys('Здравствуйте')
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    time.sleep(5)
    assert "Пожалуйста, подтвердите свое согласие с обработкой данных." in browser.page_source

#5.Вся форма заполнена корректно и все галочки приняты.
def test_submit_valid_form(browser):
    browser.get("https://easysmarthub.ru/contact/")
    input_1 = browser.find_element(By.NAME, "your-name")
    input_1.send_keys('Robert')
    input_2 = browser.find_element(By.NAME, "your-email")
    input_2.send_keys('joker112r@gmail.com')
    input_3 = browser.find_element(By.NAME, "your-subject")
    input_3.send_keys('Kurs')
    input_4 = browser.find_element(By.NAME, "your-message")
    input_4.send_keys('Здравствуйте')
    checkbox = browser.find_element(By.CLASS_NAME, "gdpr-term")
    checkbox.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    time.sleep(5)
    assert "Ваше сообщение было успешно отправлено." in browser.page_source
    



