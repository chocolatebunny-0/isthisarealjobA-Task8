from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

def linkedin_job_search(ln_company_name):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BINARY")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    a = driver.find_element_by_id('username')
    a.send_keys('lexmill99@gmail.com')
    b = driver.find_element_by_id('password')
    b.send_keys('akanke1965')
    c = driver.find_element_by_tag_name('button')
    c.click()
    first_part  = 'https://www.linkedin.com/search/results/companies/?keywords='
    driver.get(first_part+ln_company_name)
    time.sleep(15)
    result = driver.find_element_by_tag_name("h3").text
    print ("result is "+result)
    result_one = result.split()
    print (result_one)
    result_two = int(result_one[1])
    if (result_two > 2):
        return "The company is on Linkedin and analysis shows it is a big company"
    elif (result_two == 1 or result_two == 2):
        return "The company is on Linkedin and analysis shows it is a small company"
    else:
        return "The company is not on Linkedin it mostly likely does not exist" """



