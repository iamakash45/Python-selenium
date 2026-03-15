import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1" ))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
time.sleep(5)
