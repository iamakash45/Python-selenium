import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("akashkulkarni@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
time.sleep(4)
