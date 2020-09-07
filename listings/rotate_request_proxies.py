from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from validate_ip import validIPAddress, validPortNumber
import logging

'''
Code sourced from https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
'''

def get_proxies(headers):
    url = 'https://hidemy.name/en/proxy-list/?country=CAUS&maxtime=1500&type=s&anon=234#list'
    response = requests.get(url, headers=headers)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        ip_addr = i.xpath('.//td[1]/text()')[0]
        port = i.xpath('.//td[2]/text()')[0]
        logging.info(f'ip_addr: {ip_addr}, port: {port}')
        if validIPAddress(ip_addr) and validPortNumber(port):
            proxy = ":".join([ip_addr, port])
            proxies.add(proxy)
    return proxies

def cycle_proxies(proxies, url, headers={}):
    proxy_pool = cycle(proxies)

    logging.info(f'URL: {url}')
    logging.info(f'HEADERS: {headers}')
    # url = 'https://httpbin.org/ip'
    for i in range(1,len(proxies)+1):
        #Get a proxy from the pool
        proxy = next(proxy_pool)
        logging.info(f'Proxy {i}: {proxy}')

        try:
            response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
            return response
        except:
            # most free proxies will often get connection errors.
            # retry the entire request using another proxy to work. 

            if i == (len(proxies)):
                logging.error(f'URL FAILED after {i} proxy attempts: {url}')
