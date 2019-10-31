# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:37:40 2019

@author: LEKE ARIYO
"""
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import requests





def name_verification(company_name):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path ='data/chromedriver.exe',chrome_options = options)
    browser.get("https://publicsearch.cac.gov.ng/")
    time.sleep(3)
    browser.find_element_by_tag_name('input').send_keys(company_name)

    service_key = "bbe6a315a8fe6d4d30654708b014d5dc"
    google_site_key = '6LdLdSATAAAAAEQbhjzklHtmcPds-hJMT51aHC9m'

    url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key+"&pageurl="+browser.current_url
    resp = requests.get(url) 
    captcha_id = resp.text[3:]
    print(captcha_id)
    fetch_url = "http://2captcha.com/res.php?key="+service_key+"&action=get2&id="+captcha_id
    time.sleep(50)
    global token
    for i in range(1,20):
        response = requests.get(fetch_url)
        if response.text[0:2] == 'OK':
            token = response.text.split("|")[1]
            break
                    
            
                
                
    browser.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")
    browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"'%token)
    time.sleep(3)                      
    action_chains = ActionChains(browser)          
    submit = browser.find_element_by_xpath("//*[@id='content2']/div/form/div[1]/div/input[2]")
    action_chains.move_to_element(submit)
    submit.click()
    time.sleep(3)
    check_table = browser.find_element_by_tag_name('table')
    if (check_table == None):
        return "company records are not found on CAC page"
    else:
        return "company records are found on CAC page" 

#browser.quit()
    


