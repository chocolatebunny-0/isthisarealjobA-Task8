# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:37:40 2019

@author: LEKE ARIYO
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
import requests






options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(executable_path ='chromedriver.exe',chrome_options = options)
browser.get('http://publicsearch.cac.gov.ng/ComSearch/index.php')
browser.find_element_by_tag_name('input').send_keys('appzone')

service_key = "bbe6a315a8fe6d4d30654708b014d5dc"
google_site_key = '6LdLdSATAAAAAEQbhjzklHtmcPds-hJMT51aHC9m'

url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key+"&pageurl="+browser.current_url
resp = requests.get(url) 
captcha_id = resp.text[3:]
print(captcha_id)
fetch_url = "http://2captcha.com/res.php?key="+service_key+"&action=get2&id="+captcha_id
global token
for i in range(1,20):
    sleep(5)
    response = requests.get(fetch_url)
    if response.text[0:2] == 'OK':
        token = response.text.split("|")[1]
        break
		
        
            
            
browser.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")
browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"'%token)
sleep(1)                      
action_chains = ActionChains(browser)          
submit = browser.find_element_by_xpath("//*[@id='content2']/div/form/div[1]/div/input[2]")
action_chains.move_to_element(submit)
submit.click()

#browser.quit()
        


