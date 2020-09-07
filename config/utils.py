#!/usr/bin/env python3
import logging
import sys
import requests
import random
from datetime import datetime
import time

USER_AGENT_LIST = [
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (X11; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
   'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
]

def get_user_agent():
    return random.choice(USER_AGENT_LIST)

def get_request(url, headers={}):
    headers['User-Agent'] = get_user_agent()
    res = None
    for i in range(3):
        # sleep for random amount (between .5 and 1.5 seconds) to prevent rate limiting
        time.sleep(random.random() * (1.5 - .5) + .5)

        retry = False if i == 0 else True
        res = requests.get(url, headers=headers)
        logging.info(f'Request Status {"(Retry)" if retry else ""} {res.status_code}: {url}')
        if res.status_code == 200:
            break
    return res

def log_config(module_name):
    log_file_name = f'log/{module_name}_{str(datetime.now()).replace(" ", "_")}.log'
    logging.basicConfig(filename=log_file_name, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    # print logs to both stdout and log file
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))