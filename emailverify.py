from selenium import webdriver
import time

email = input("Enter the email you want to check: ")
options = webdriver.ChromeOptions()
chrome_options.headless = True
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
browser.get("https://verify-email.org/")
browser.find_element_by_id("email").send_keys(email)
browser.find_element_by_id("verifyBtn").click();
time.sleep(5)
x = browser.find_element_by_id("result-email").text
browser.quit()
print(x)

