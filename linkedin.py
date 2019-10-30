import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pyautogui
from tkinter import filedialog, Tk
import tkinter.messagebox as tm
import os
from urllib.request import urlopen
import pandas as pd
import numpy as np
import requests
import csv
import datetime


# pyinstaller --onefile --icon=app.ico scrapejobs.py

class EasyApplyBot:

    MAXI_APPLICATIONS = 2000

    def __init__(self,username,password, language, position, location): #, resumeloctn):

        dirpath = os.getcwd()

        self.language = language
        self.options = self.browser_options()
        self.browser = webdriver.Chrome(chrome_options=self.options, executable_path = dirpath + "\chromedriver.exe")
        self.start_linkedin(username,password)


    def browser_options(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("user-agent=Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        #options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        return options

    def start_linkedin(self,username,password):
    #    self.browser.get("https://linkedin.com/uas/login")
    #def login(driver): #, username, password):
        print("\nLogging in.....\n \nPlease wait :) \n ")
        self.browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        time.sleep(7)
        try:
            user_field = self.browser.find_element_by_id("username")
            pw_field = self.browser.find_element_by_id("password")
            login_button = self.browser.find_element_by_tag_name("button")
            user_field.send_keys(username)
            user_field.send_keys(Keys.TAB)
            time.sleep(1)
            pw_field.send_keys(password)
            time.sleep(1)
            login_button.click()
        except TimeoutException:
            print("TimeoutException! Username/password field or login button not found")

    def wait_for_login(self):
       
        title = "Sign In to LinkedIn"

        time.sleep(1)

        while True:
            if self.browser.title != title:
                print("\nStarting LinkedIn bot\n")
                break
            else:
                time.sleep(1)
                print("\nPlease Login to your LinkedIn account\n")

    def fill_data(self):
        self.browser.set_window_size(0, 0)
        self.browser.set_window_position(2000, 2000)
        os.system("reset")

        self.position = position
        self.location = "&location=" + location
        #self.resumeloctn = resumeloctn
        #print(self.resumeloctn)

    def start_apply(self):
        self.fill_data()
        self.applications_loop()

    def applications_loop(self):

        count_application = 1
        count_job = 0
        jobs_per_page = 0

        os.system("reset")

        print("\nLooking for jobs.. Please wait..\n")

        self.browser.set_window_position(0, 0)
        self.browser.maximize_window()
        self.browser, _ = self.next_jobs_page(jobs_per_page)
        
        print("\nLooking for jobs.. Please wait..\n")

        """self.browser.find_element_by_class_name(
            "jobs-search-dropdown__trigger-icon"
            ).click()
        
        self.browser.find_element_by_class_name(
            "jobs-search-dropdown__option"
            ).click()"""

        while count_application < self.MAXI_APPLICATIONS:
            # sleep to make sure everything loads, add random to make us look human.
            time.sleep(random.uniform(3.5, 6.9))
            self.load_page(sleep=1)
            page = BeautifulSoup(self.browser.page_source, 'lxml')

            jobs = self.get_job_links(page)

            if not jobs:
                print("Jobs not found")
                break

            for job in jobs:
                temp = {}

                count_job += 1
                job_page = self.get_job_page(job)

                #position_number = str(count_job + jobs_per_page)
                position_number = str(count_application)
                print(f"\nPosition {position_number}:\n {self.browser.title} \n") # {string_easy} \n")
                print(job,'\n')

                now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                temp ['timestamp'] = str(now)
                temp ['url'] = ('https://www.linkedin.com'+job)




                """
                click button see more
                """
                
                try :
                    self.browser.find_element_by_xpath(
                        '//button[@aria-controls="job-details"]'
                        ).click()
                    self.browser.find_element_by_class_name(
                        'view-more-icon'
                        ).click()
                    self.load_page(sleep=1)
                except:
                    print('Details not uploaded\n')



                """
                Get data
                """     

                # position
                try:
                    temp['position'] = self.browser.find_element_by_xpath(
                        '//h1[@class="jobs-top-card__job-title t-24"]'
                        ).text.strip()
                except:
                    temp['position'] = None
                
                # company
                try:
                    temp['company'] = self.browser.find_element_by_xpath(
                        '//span[contains(text(),"Company Name")]/following::a'
                        ).text.strip()
                except:
                    temp['company'] = None        
                
                # location
                try:
                    temp['location'] = self.browser.find_element_by_xpath(
                        '//span[contains(text(),"Company Location")]/following::span'
                        ).text.strip()
                except:
                    temp['location'] = None  
                
                # post date
                try:
                    temp['post date'] = self.browser.find_element_by_xpath(
                        '//span[contains(text(),"Posted Date")]/following::span'
                        ).text.strip()
                except:
                    temp['post date'] = None  
                
                # no. of applicants
                try:
                    temp['no. applicants']  = self.browser.find_element_by_xpath(
                        '//span[contains(text(),"Number of applicants")]/following::span'
                        ).text.strip()
                except:
                    temp['no. applicants'] = None  

                # job details
                try:
                    temp['job description'] = self.browser.find_element_by_xpath(
                        '//div[@id="job-details"]'
                        ).text.strip().replace('\n', ', ')
                except:
                    temp['job description'] = None  
                
                # seniority level
                try:
                    temp['seniority'] = self.browser.find_element_by_xpath(
                        '//h3[contains(text(),"Seniority Level")]/following::*'
                        ).text.strip()
                except:
                    temp['seniority'] = None  
                
                # Industry
                try:
                    temp['industry'] = self.browser.find_element_by_xpath(
                        '//h3[contains(text(),"Industry")]/following::*'
                        ).text.strip()
                except:
                    temp['industry'] = None  
                
                # Employment Type
                try:
                    temp['employment type'] = self.browser.find_element_by_xpath(
                        '//h3[contains(text(),"Employment Type")]/following::*'
                        ).text.strip()
                except:
                    temp['employment type'] = None  
                
                #Job Functions
                try:
                    temp['functions'] = self.browser.find_element_by_xpath(
                        '//h3[contains(text(),"Job Functions")]/following::*'
                        ).text.strip()
                except:
                    temp['functions'] = None  

                # company description
                try:
                    temp['company description'] = self.browser.find_element_by_id(
                        'company-description-text'
                        ).text.strip()
                except:
                    temp['company description'] = None




                """
                Write to file
                """

                data = temp
                with open('output.csv', 'a', newline='') as f:
                    try:
                        writer = csv.writer(f)
                        writer.writerow(data.values())
                        print('Job added to output.csv')
                    except:
                        print('Error while printing csv')

                


                """
                Count application and set sleep time
                """
                count_application = count_application + 1

                if count_application % 20 == 0:
                    sleepTime = random.randint(590, 900)
                    print('\n\n****************************************\n\n')
                    print('see you later')
                    print('\n\n****************************************\n\n')
                    time.sleep (sleepTime)

                if count_job == len(jobs):
                    jobs_per_page = jobs_per_page + 25
                    count_job = 0
                    print('\n\n****************************************\n\n')
                    print('Going to next jobs page!')
                    print('\n\n****************************************\n\n')
                    self.browser, jobs_per_page = self.next_jobs_page(jobs_per_page)



        self.finish_apply()

    def get_job_links(self, page):
        links = []
        for link in page.find_all('a'):
            url = link.get('href')
            if url:
                if '/jobs/view' in url:
                    links.append(url)
        return set(links)

    def get_job_page(self, job):
        root = 'www.linkedin.com'
        if root not in job:
            job = 'https://www.linkedin.com'+job
        self.browser.get(job)
        self.job_page = self.load_page(sleep=0.5)
        return self.job_page

    def got_easy_apply(self, page):
        button = page.find("button", class_="jobs-s-apply__button js-apply-button")
        return len(str(button)) > 4

    def get_easy_apply_button(self):
        button_class = "jobs-s-apply--top-card jobs-s-apply--fadein inline-flex mr2 jobs-s-apply ember-view"
        button = self.job_page.find("div", class_=button_class)
        return button

    def easy_apply_xpath(self):
        button = self.get_easy_apply_button()
        button_inner_html = str(button)
        list_of_words = button_inner_html.split()
        next_word = [word for word in list_of_words if "ember" in word and "id" in word]
        ember = next_word[0][:-1]
        xpath = '//*[@'+ember+']/button'
        return xpath

    def click_button(self, xpath):
        triggerDropDown = self.browser.find_element_by_xpath(xpath)
        time.sleep(0.5)
        triggerDropDown.click()
        time.sleep(1)

    def load_page(self, sleep=1):
        scroll_page = 0
        while scroll_page < 4000:
            self.browser.execute_script("window.scrollTo(0,"+str(scroll_page)+" );")
            scroll_page += 200
            time.sleep(sleep)

        if sleep != 1:
            self.browser.execute_script("window.scrollTo(0,0);")
            time.sleep(sleep * 3)

        page = BeautifulSoup(self.browser.page_source, "lxml")
        return page


    def next_jobs_page(self, jobs_per_page):
        self.browser.get(
            #"https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=" +
            "https://www.linkedin.com/jobs/search/?keywords=" +
            self.position + self.location + "&start="+str(jobs_per_page))
        self.load_page()
        return (self.browser, jobs_per_page)

    def finish_apply(self):
        self.browser.close()


if __name__ == '__main__':


    if False == False:

        username = ''
        password = ''
        language = 'english'
        position = 'appzone'
        location = 'nigeria'

    # print input
    print("\nThese is your input:")

    print  ("\nUsername:  "+ username,
        "\nPassword:  "+ password,
        "\nLanguage:  "+ language,
        "\nPosition:  "+ position,
        "\nLocation:  "+ location)
    
    print("\nLet's scrape some jobs!\n")
    
    # start bot
    bot = EasyApplyBot(username,password, language, position, location) #, resumeloctn)
    bot.start_apply()
