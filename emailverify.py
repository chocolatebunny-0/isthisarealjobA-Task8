from selenium import webdriver
import time
import os

def scrape():
    result = []
    #email = input("Enter the email you want to check: ")
    email = "aaaa"
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BINARY")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
     
    # to open chrome webbrowser and maximize the window

    browser = webdriver.Chrome(chrome_options=options)
    #browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    #browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options = options)
    browser.get("https://verify-email.org/")
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("verifyBtn").click();
    time.sleep(5)
    x = browser.find_element_by_id("result-email").text
    result = x
    return result
#print(x)

if __name__ == "__main__":
    print(scrape())

