from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_guest_should_see_button(browser):
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'There is no button'
