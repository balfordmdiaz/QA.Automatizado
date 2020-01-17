from features.pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HomeLocator(object):
    MODULO_EDICION = (By.CSS_SELECTOR, "li:nth-of-type(1) > .maxheight.wp-categories-link")
    MODULO_BUTTON = (By.CSS_SELECTOR, "li:nth-of-type(2) > .maxheight.wp-categories-link")


class HomePage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)

    def click_modulo_edicion(self):
        self.driver.find_element(*HomeLocator.MODULO_EDICION).click()

