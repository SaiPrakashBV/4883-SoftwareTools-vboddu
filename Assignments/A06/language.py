from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Create a new instance of the WebDriver
driver = webdriver.Chrome()

# Open the Amazon website
driver.get('https://www.amazon.com')
dropdown_element = driver.find_element(By.ID,'icp-nav-flyout')
dropdown_element.click()
time.sleep(10)
# radiobox_element =driver.find_element(By.XPATH,'//input[@type="radio" and @name="lop" and @value="es_US"]')
# radiobox_element.click()
# time.sleep(5)

submit_button=driver.find_element(By.ID,'icp-save-button')
submit_button.click()
time.sleep(5)
