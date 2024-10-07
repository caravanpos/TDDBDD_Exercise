from os import getenv
from selenium import webdriver

WAIT_SECONDS =int(getenv('WAIT_SECONDS','60'))
BASE_URL = getenv('BASE_URL', 'https://www.google.com.gt')

def before_all(context):
    """Execute once before all tests"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox") #Bypass OS security model
    context.driver = webdriver.Firefox(options=options)
    context.wait_seconds = WAIT_SECONDS
    context.driver.implicitly_wait(context.wait_seconds) #seconds
    context.base_url = BASE_URL

def after_all(context):
    """ Execute after all test"""
    context.driver.quit()

