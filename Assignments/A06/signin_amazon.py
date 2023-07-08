from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Create a new instance of the WebDriver
driver = webdriver.Chrome()

# Open the Amazon website
driver.get('https://www.amazon.com')
account_list_dropdown=driver.find_element(By.ID,'nav-link-accountList')
account_list_dropdown.click()
time.sleep(7)
# dropdown_element = driver.find_element(By.ID,'icp-nav-flyout')
# dropdown_element.click()
# time.sleep(10)
# email_box=driver.find_element(By.ID,'ap_email')
# email_box.click()
# time.sleep(15)
email_field = driver.find_element(By.ID,'ap_email')
email_field.send_keys('vboddu1107@my.msutexas.edu')
email_field.send_keys(Keys.RETURN)
time.sleep(7)

password_field = driver.find_element(By.ID,'ap_password')
password_field.send_keys('**************')
time.sleep(7)


# driver = webdriver.Chrome()

# # Open the Amazon website
# driver.get('https://www.amazon.com')
# dropdown_element = driver.find_element(By.ID,'icp-nav-flyout')
# dropdown_element.click()
# time.sleep(10)
# # radiobox_element =driver.find_element(By.XPATH,'//input[@type="radio" and @name="lop" and @value="es_US"]')
# # radiobox_element.click()
# # time.sleep(5)

# submit_button=driver.find_element(By.ID,'icp-save-button')
# submit_button.click()
# time.sleep(5)

# Specify the path to your ChromeDriver executable
# driver_path = './chromedriver'  # Update this with the correct path
# # Create a new instance of the Chrome driver
# service = Service(driver_path)
# options = webdriver.ChromeOptions()
# options.add_argument('--log-level=3')
# driver = webdriver.Chrome(service=service,options=options)


# # Navigate to Amazon
# driver.get("https://www.amazon.com/")
# time.sleep(5)

# # Find the search input field and enter the keyword
# search_field = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
# search_field.send_keys(keyword)
# search_field.send_keys(Keys.RETURN)
# time.sleep(5)

# # Get the page source after the search results are loaded
# page_source = driver.page_source
# time.sleep(5)


# # Close the browser
# driver.quit()



password_field.send_keys(Keys.RETURN)
time.sleep(7)

# checkbox_element =driver.find_element(By.XPATH,'//input[@type="checkbox" and @name="rememberMe" and @value="true"]')
# checkbox_element.click()
# time.sleep(5)
# submit_button=driver.find_element(By.ID,'icp-save-button')
# submit_button.click()
# time.sleep(5)

