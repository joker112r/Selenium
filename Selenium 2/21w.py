from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time


def test_button_molodec():
    try:
        browser = webdriver.Chrome()
        browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
        browser.find_element(By.ID, 'molodec')

    finally:
        time.sleep(5)
        browser.quit()