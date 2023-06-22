"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function
from string import *
from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(3)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML


def get_data(input_page):
    soup = BeautifulSoup(input_page, 'html.parser')
    history = soup.find('lib-city-history-observation')
    title=history.find('div',class_='observation-title')
    table_headings = history.find_all('div', class_=lambda value: value and 'mat-sort-header-content ng-tns-c144-' in value)
    tr_element = history.find_all('tr', class_='mat-row cdk-row ng-star-inserted')
    
    headers=[]
    row_data=[]
    rows=[]
    for th in table_headings:
         data=th.text
         headers.append(data)
         
    nheaders=len(headers)
    
    # Find all td elements within the tr element
    for e in tr_element:
        td_elements = e.find_all('td')
        for td in td_elements:
        
        # Extract the text content of each td element
            data = td.get_text()
            row_data.append(data)
            #print(data +" ")
        rows.append(row_data)
        row_data=[]
    
    return (title.text, headers, rows)
if __name__=='__main__':

    
    url = 'https://www.wunderground.com/history/daily/mx/mexico-city/MMMX/date/2000-4-19'

    # get the page source HTML from the URL
    #page = asyncGetWeather(url)
    #a,b,c= get_data(page)