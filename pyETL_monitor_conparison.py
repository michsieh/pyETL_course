import requests
from bs4 import BeautifulSoup
import re
import json
import time
import os
from selenium.webdriver import Chrome

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
monitor_buyer_url = 'https://monitor.buyerguide.info/'
req = requests.get(url=monitor_buyer_url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
brand = soup.select('#__next > div > nav > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span.jsx-173834137.brand-title')

for brand_name in brand :
    print(brand_name.text)