import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://peps.python.org/topic/release/')
print("titulo de pagina " + driver.title)
element = driver.find_element(By.ID ,"APjFqb")
element.clear()
element.send_keys("Python")
time.sleep(2)
element2 = driver.find_element(By.CLASS_NAME ,"gNO89b")
element2.click()
time.sleep(2)
#element3 = driver.find_element(By.CLASS_NAME ,"LC20lb MBeuO DKV0Md")
#element3.click()
#time.sleep(5)
driver.quit()