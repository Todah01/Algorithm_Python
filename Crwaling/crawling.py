from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pandas.io.html import read_html
import time
import pandas as pd
import numpy as np
import requests
import random


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return web_driver


url = "https://swarfarm.com/bestiary/?page=1&sort=name%3Basc"

dr = set_chrome_driver()
dr.get(url)

act = ActionChains(dr)

columns_selectors = dr.find_elements(By.CLASS_NAME, 'form-check-input checked')

print(columns_selectors)

for selector in columns_selectors:
    print(selector)

# soup = BeautifulSoup(req.text, 'html.parser')
# temp = soup.find('table', {'id': 'tblMaster'})
#
# table = parser.make2d(temp)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

# order_number_list = []
# order_number = 0
# idx = 0
#
# for i in range(4):
#     while order_number in order_number_list or idx < 100:
#         order_number = random.randint(0, 4)
#         idx += 1
#     order_number_list.append(order_number)
    # print(order_number)