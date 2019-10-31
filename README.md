# isthisarealjobA-Task8


## About Project
### IS THIS A REAL JOB this is a website to help individuals from falling victims to scams,we used ML approach to optimizse the website


## Approach Worked On
### 1. Does address exist(using the map)
### 2. Does company/job opening exist (using LinkedIn , nairaland etc)
### 3. Is email real ?
### 4. Optical Character Recognition
### 5. Sentiments analyzer based on google invite mail
### 6. We can build a system to analyze say the first 10 comments with the sentiment analyzer too . It is not enough to say a job is real or fake because of the number of comments . We should analyze the comments too
### 7. Building the APIs
### 8. Scraping CAC website

## Approach 1.
### addresschecker.py file in the repo

### About 
### An address checker script that used google maps app to check the geo code of the address to check if it’s available

### Installation
### googlemaps

### Prerequisites
### Getting an Apikey form Google Cloud 
### Enable Geocoding API

## Approach 2.
### linkedin.py file in the repo

### About
### A LinkedIn scraper that scrapers data from LinkedIn 

### Installation and Imports
### import time
### import random
### from selenium import webdriver
### from selenium.webdriver.chrome.options import Options
### from selenium.common.exceptions import TimeoutException
### from selenium.webdriver.common.keys import Keys
### from bs4 import BeautifulSoup
### import pyautogui
### from tkinter import filedialog, Tk
### import tkinter.messagebox as tm
### import os
### from urllib.request import urlopen
### import pandas as pd
### import numpy as np
### import requests
### import csv
### import datetime

### nairaland_aj.py file in the repo

### About
### A nairaland scraper that scrapers data from nairaland

### Installation and Imports
### import requests
### from bs4 import BeautifulSoup


## Approach 3.
### emailverify.py file in the repo

### About
### Checks the validity of an email address To see if it’s fake or not

### Installation and Imports
### from selenium import webdriver
### import time
### import os


## Approach 4.
### OCR folder in the repo the folder contains a test picture

### About
### Converts image to string

### Installation and Imports
### from PIL import Image
### except ImportError:
### import Image
### import pytesseract


## Approach 8.
### cac_john.py in the repo

### About
### Scrape CAC website for company info using anti-captcha API to bypass recaptcha. 

### Installation and Imports
### import time
### from selenium import webdriver
### import pandas as pd
### from selenium.webdriver.common.by import By
### from selenium.webdriver.support.ui import WebDriverWait
### from selenium.webdriver.support import expected_conditions as ec
### from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
### import itertools
### import argparse

### Note Anticaptcha is a paid service 

### cac_leke.py files in the repo

### About
### Scrape CAC website for company info using 2captcha API to bypass recaptcha. 

### Installation and Imports
### from selenium import webdriver
### import time
### from selenium.webdriver import ActionChains
### import requests
### import os

### Note this search on cac is real time









