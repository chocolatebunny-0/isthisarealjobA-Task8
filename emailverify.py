from selenium import webdriver
import time
import os

def scrape(email):
    result = []
    #email = input("Enter the email you want to check: ")
    #email = "aaaa"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
     
    # to open chrome webbrowser and maximize the window

    browser = webdriver.Chrome(chrome_options=options)
    #browser = webdriver.Chrome(executable_path="data/chromedriver.exe", chrome_options=options)
    #browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options = options)
    browser.get("https://verify-email.org/")
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("verifyBtn").click();
    time.sleep(5)
    x = browser.find_element_by_id("result-email").text
    result = x
    return result

if __name__ == "__main__":
    print(scrape())

