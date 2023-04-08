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


url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
browser = set_chrome_driver()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

login_id = browser.find_element("#id")
login_id.click()
login_id.send_keys("wobo5695")