#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time


def test_eception1():
    try:
        browser = webdriver.Chrome()
        browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR,"[id='molodec1']") #не верный - то есть будет зеленым так как кнопки нету на сайте
            pytest.fail('Не должна отображаться кнопка ЧУДО на странице1')


    finally:
        browser.quit()


def test_eception2():
    try:
        browser = webdriver.Chrome()
        browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR,"[id='molodec']") #верный - то есть будет красным поскольку кнопка действительно есть на сайте
            pytest.fail('Не должна отображаться кнопка ЧУДО на странице1')


    finally:
        browser.quit()

        