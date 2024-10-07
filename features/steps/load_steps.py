from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I am on the "Home Page"')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given I am on the "Home Page"')
    driver = webdriver.Firefox()
    driver.get('https://www.python.org/')
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME ,"docs-meta")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT ,"What's new in Python 3.12?")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT, "PEP 693")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT, "Release")
    element.click()
    time.sleep(2)
    #assert(driver.title, 'Release PEPs | peps.python.org')
    driver.quit()

@when(u'I set the "Category" to "dog"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I set the "Category" to "dog"')
    #driver = webdriver.Firefox()
    #driver.get('https://www.google.com.gt')
    #print(driver.title)
    #time.sleep(1)
    #element = driver.find_element(By.ID ,"APjFqb")
    #element.send_keys("Python")
    #time.sleep(1)
    #element = driver.find_element(By.CLASS_NAME ,"gNO89b")
    #element.click()
    #driver.quit()

@when(u'I click the "Search" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Search" button')

@then(u'I should see the message "Success"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the message "Success"')


@then(u'I should see "Fide" in the results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Fide" in the results')