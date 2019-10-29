# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:37:40 2019

@author: jayanwana
"""

import requests
from bs4 import BeautifulSoup


def scrape(company_name):
    cn = company_name.split()
    cn = '+'.join(cn)
    url = f"https://www.nairaland.com/search?q={cn}&board=0"
    links = [url]
    posts = []
    header = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    scraped = requests.get(url, headers=header)
    page = scraped.content
    soup = BeautifulSoup(page, 'html.parser')
    p = soup.find('p')
    a = p.find_all('a')
    for link in a:
        a_tag = link.get('href')
        if str(a_tag).startswith("https://www.nairaland.com/search"):
            links.append(a_tag)
    for link in links:
        scraped = requests.get(link, headers=header)
        page = scraped.content
        soup = BeautifulSoup(page, 'html.parser')
        nar = soup.find_all('div', {'class': "narrow"})
        for i in range(len(nar)):
            post = nar[i].text
            posts.append(post)
    return posts

