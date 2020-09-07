from expressvpn import wrapper
import logging
import random
import logging
from time import sleep
import requests
import subprocess

alias_list = [
    'usny',     # USA - New York
    'ussf',     # USA - San Francisco
    'usla',     # USA - Los Angeles
    'usla2',    # USA - Los Angeles - 2
    'uswd',     # USA - Washington DC
    'usda',     # USA - Dallas
    'usmi2',    # USA - Miami - 2
    'usse'      # USA - Seattle
]

class BannedException(Exception):
    pass

def scrape():
    if random.choice([True, False]):
        raise BannedException('Scrape failed.')

def main():
    logging.basicConfig(filename='test_expressvpn_wrapper.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    while True:
        try:
            sleep(5)
            scrape()
        except BannedException as be:
            logging.info('BANNED EXCEPTION in __MAIN__')
            logging.info(be)
            logging.info('Lets change our PUBLIC IP GUYS!')
            change_ip()
        except Exception as e:
            logging.error('Exception raised.')
            logging.error(e)


def change_ip():
    max_attempts = 10
    attempts = 0
    while True:
        attempts += 1
        try:
            logging.info('GETTING NEW IP')
            # wrapper.connect_alias(random.choice(alias_list))
            subprocess.call('sudo kill -9 $(pgrep expressvpn)', shell=True)
            # sleep 2 seconds while expressvpn daemon service restarts automatically
            sleep(2)
            # subprocess.call('sudo systemctl restart expressvpn', shell=True)
            subprocess.call(f'expressvpn connect {random.choice(alias_list)} ', shell=True)
            logging.info('SUCCESS')
            ip = requests.get('https://api.ipify.org').text
            logging.info(f'Public IP address is: {ip}')
            return
        except Exception as e:
            if attempts > max_attempts:
                logging.error('Max attempts reached for VPN. Check its configuration.')
                logging.error('Browse https://github.com/philipperemy/expressvpn-python.')
                logging.error('Program will exit.')
                exit(1)
            logging.error(e)
            logging.error('Skipping exception.')

if __name__ == "__main__":
    main()
