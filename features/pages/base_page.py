from selenium.webdriver.common.keys import Keys
import time

class BasePage(object):
    def __init__(self, browser):
        self.driver = browser

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def fill_field(self, value, *locator):
        elemento = self.get_element(*locator)
        elemento.send_keys(Keys.CONTROL + "a")
        elemento.send_keys(Keys.DELETE)
        elemento.send_keys(value)