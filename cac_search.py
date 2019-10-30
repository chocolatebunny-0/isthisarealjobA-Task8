"""
@author: jayanwana
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask


def get_token(url, site_key, invisible, client):
    task = NoCaptchaTaskProxylessTask(
        website_url=url,
        website_key=site_key,
        is_invisible=invisible
    )
    job = client.createTask(task)
    job.join()
    return job.get_solution_response()


def get_sitekey(driver):
    return driver.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')


def process(driver, url, invisible_captcha, term, client):
    driver.get(url)
    site_key = get_sitekey(driver)
    print("Found site-key", site_key)
    print("Send challenge")
    token = get_token(url, site_key, invisible_captcha, client)
    print("Found token", token)
    driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='{}';".format(token))
    time.sleep(5)
    try:
        driver.find_element_by_css_selector('input.field').send_keys(term)
        driver.find_element_by_class_name('button2').click()
        print("Form submitted")
        table = driver.find_element_by_id('directorsTbl')
        return table
    except NoSuchElementException as exception:
        print("search failed")
        print(exception)
        return None


class WebTable:
    def __init__(self, webtable):
        self.table = webtable

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        row = self.table.find_elements_by_xpath("//tr["+str(row_number)+"]/td")
        r_data = []
        for webElement in row:
            r_data.append(webElement.text)

        return r_data

    def column_data(self, column_number):
        col = self.table.find_elements_by_xpath("//tr/td["+str(column_number)+"]")
        r_data = []
        for webElement in col:
            r_data.append(webElement.text)
        return r_data


def join_db(db):
    cac_db = pd.read_csv(r'data\cac_db.csv')
    cac_db_main = pd.concat([cac_db, db])
    cac_db_main = cac_db_main.drop_duplicates()
    cac_db_main.sort_values(by='COMPANY NAME', inplace=True)
    cac_db_main.reset_index(drop=True, inplace=True)
    cac_db_main.to_csv(r'data\cac_db.csv', index=None, header=True)


def cac_search(term):
    api_key = '5e4a13666ac564d7d353cd69b5fa926f'
    invisible_captcha = True
    client = AnticaptchaClient(api_key)
    chrome_path = r"data\chromedriver.exe"
    url = 'http://publicsearch.cac.gov.ng/comsearch/'
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)
    data = []
    table = process(driver, url, invisible_captcha, term, client)
    if table is not None:
        cac_table = WebTable(table)
        if cac_table.get_row_count() >= 1:
            db = []
            print(f'collecting {term} data')
            for i in range(cac_table.get_row_count()):
                row = i + 1
                row_data = cac_table.row_data(row)
                db.append(row_data[:-1])
            data.append(db)
        cac_data = []
        for _ in data:
            for d in _:
                cac_data.append(d)
        col_names = ['RC NUMBER', 'COMPANY NAME', 'ADDRESS']
        cac_db = pd.DataFrame(cac_data, columns=col_names)
        join_db(cac_db)
        return cac_db
    else:
        return None
