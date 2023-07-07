from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def search_amazon(keyword):
    # Specify the path to your ChromeDriver executable
    driver_path = './chromedriver'  # Update this with the correct path
    # Create a new instance of the Chrome driver
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=service,options=options)
    

    # Navigate to Amazon
    driver.get("https://www.amazon.com/")
    time.sleep(5)

    # Find the search input field and enter the keyword
    search_field = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_field.send_keys(keyword)
    search_field.send_keys(Keys.RETURN)
    time.sleep(5)

    # Get the page source after the search results are loaded
    page_source = driver.page_source
    time.sleep(5)
    
    
    # Close the browser
    driver.quit()
    time.sleep(5)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the first search result
    first_result = soup.find('div', {'data-component-type': 's-search-result'})

    # Retrieve the details of the first search result
    title = first_result.find('h2').find('span').text.strip()

    try:
        price = first_result.find('span', {'class': 'a-offscreen'}).text.strip()
    except AttributeError:
        price = "Price not available"

    try:
        rating = first_result.find('span', {'class': 'a-icon-alt'}).text.strip()
    except AttributeError:
        rating = "Rating not available"

    try:
        # Retrieve the specifications from the product page
        product_url = first_result.find('a', {'class': 'a-link-normal'}).get('href')
        product_url = "https://www.amazon.com" + product_url
        driver = webdriver.Chrome(service=service)
        driver.get(product_url)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')

        specifications = soup.find('div', {'id': 'poExpander'})
        if specifications:
            specifications = '\n'.join([line.strip() for line in specifications.stripped_strings])
        else:
            specifications = "Specifications not available"

    except AttributeError:
        specifications = "Specifications not available"

    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("Specifications:")
    print(specifications)

print("Enter the item:")
item=input()
search_amazon(item)
