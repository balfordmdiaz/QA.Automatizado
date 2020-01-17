from features.pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class EdicionLocator(object):
    CAMPO_CORREO = (By.CSS_SELECTOR, "input#email")


class EdicionPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)

    def llenamos_campo_correo(self, value):
        self.fill_field(value, *EdicionLocator.CAMPO_CORREO)
        time.sleep(8)
