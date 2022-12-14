from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import glob
import time
from selenium.webdriver.chrome.options import Options
import random

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
options = Options()
while True:
    user_agent = random.choice(user_agent_list)
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome('PATH_TO_CHROMEDRIVER', options=options)
    driver.get("URL")
    os.system('sleep 7')
    driver.close()
