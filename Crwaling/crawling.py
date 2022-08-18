from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pandas.io.html import read_html
import time
import pandas as pd
import numpy as np
import requests


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return web_driver


url = "https://www.hjnc.co.kr/esvc/vessel/berthScheduleT"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'html.parser')
# temp = soup.find('table', {'id': 'tblMaster'})
#
# table = parser.make2d(temp)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

