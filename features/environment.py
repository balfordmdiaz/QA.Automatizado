import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.pages.home_page import HomePage
from features.pages.edicion_page import EdicionPage
from features.pages.base_page import BasePage

def prepare_pages(context, driver):
    context.base_page = BasePage(driver)
    context.home_page = HomePage(driver)
    context.edicion_page = EdicionPage(driver)

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.set_page_load_timeout(20)
    context.driver.implicitly_wait(20)
    context.driver.maximize_window()
    prepare_pages(context, context.driver)

def after_step(context, step):
    time.sleep(3)

def after_all(context):
    context.driver.quit()