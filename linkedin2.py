from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import os

def linkedin_job_search(ln_company_name):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    url = "https://www.linkedin.com/search/results/companies/?keywords=appzone"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BINARY")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=options)
    """options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")"""
     
    # to open chrome webbrowser and maximize the window
    #driver = webdriver.Chrome(executable_path="data/chromedriver.exe", chrome_options=options)
    driver.maximize_window()
     
    #Implicit Wait when element is taking time to load
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    a = driver.find_element_by_id('username')
    a.send_keys('bilesanmifaruk@gmail.com')
    b = driver.find_element_by_id('password')
    b.send_keys('Okikiola1')
    c = driver.find_element_by_tag_name('button')
    c.click()
    first_part  = 'https://www.linkedin.com/search/results/companies/?keywords='
    link = first_part+ln_company_name
    print(link)
    driver.get(link)
    time.sleep(10)
    result = driver.find_elements_by_tag_name("h3")

    print ("aaa "+str(len(result)))
    """result = driver.find_element_by_css_selector("h3.search-results__total").text
    result_one = result.split()
    
    result_two = int(result_one[1])
    if (result_two > 2):
        return "The company is on Linkedin and analysis shows it is a big company"
    elif (result_two == 1 or result_two == 2):
        return "The company is on Linkedin and analysis shows it is a small company"
    else:
        return "The company is not on Linkedin it mostly likely does not exist" """



