#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv
from configparser import ConfigParser
import psycopg2
from psycopg2.extensions import AsIs
from db_config import config, create_tables
from progress_bar import printProgressBar
import sys
from datetime import datetime
from rotate_request_proxies import cycle_proxies, get_proxies
import logging
import random

NL='\n'

STATES_LIST = [
   # 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
   # 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
   # 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
   # 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
   'CA', 'CO', 'KY', 'MN', 'NV', 'NM', 'NY', 'NC', 'OR', 'PA', 'TN', 'UT', 'VT', 'VA', 'WA', 'WY'
]

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

# postgres database connection
db_connection = None
# postgres database cursor
db_cursor = None

def clean_up():
   """ close the communication with the PostgreSQL """
   if db_connection is not None:
      db_connection.close()
   if db_cursor is not None:
      db_cursor.close()


def getZipGeography(zip_code):
   db_cursor.execute(f'SELECT latitude, longitude FROM zip_codes WHERE zip_code LIKE \'{zip_code}\'')
   lat_long = db_cursor.fetchone()
   latitude = lat_long[0]
   longitude = lat_long[1]
   # print(f'latitude: {latitude}')
   # print(f'longitude: {longitude}')
   geometry_cmd = f'SELECT ST_SetSRID(ST_MakePoint({longitude}, {latitude}),4326)'
   db_cursor.execute(geometry_cmd)
   return db_cursor.fetchone();
   
def getAttribute(element, attribute):
   try:
      return element[attribute]
   except KeyError:
      return None

def getPropertyInfo(property_card_el, state, zip_code):
   price_el = property_card_el.find('div', {'class': 'property-card--price'})
   price_el_text = price_el.get_text()
   price = int(price_el_text[price_el_text.index('$')+1::].replace(',', ''))
   stats_el = property_card_el.find('div', {'class': 'property-card--quick-stats'})
   acres_text = stats_el.span.get_text()
   acres_str = acres_text[:acres_text.index('acres')].strip()
   acres = float(acres_str)
   listing_id_el = property_card_el.find('div', {'class': 'property-card--saved-indicator'})
   listing_id = listing_id_el['data-savable-property-id']
   # print(f'listing_id: {listing_id}   zip_code: {zip_code}   price: {price}   acres: {acres}')
   return {
      'listing_id': listing_id,
      'price': price,
      'acres': acres,
      'latitude': getAttribute(property_card_el, 'data-mappable-latitude'),
      'longitude': getAttribute(property_card_el, 'data-mappable-longitude'),
      'zip_code': zip_code
   }

def insertDB(insert_cmd, columns, values):
   try:
      db_cursor.execute(insert_cmd, (AsIs(','.join(columns)), tuple(values)))
      db_connection.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      clean_up()
      sys.exit(error)

def insertListingDB(property_info):
   """ Insert property info listings into database """
   columns = ['listing_id', 'price', 'acres', 'geog', 'insert_date', 'zip_code']
   # get geometry value from lat and long
   geometry = None;
   if property_info['longitude'] is None or property_info['latitude'] is None:
      geometry = getZipGeography(property_info['zip_code'])
   else:
      geometry_cmd = f'SELECT ST_SetSRID(ST_MakePoint({property_info["longitude"]}, {property_info["latitude"]}),4326)'
      db_cursor.execute(geometry_cmd)
      geometry = db_cursor.fetchone()
   values = [
      property_info['listing_id'],
      property_info['price'],
      property_info['acres'],
      geometry,
      datetime.utcnow(),
      property_info['zip_code'],
   ]
   insert_cmd = 'INSERT INTO listings (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDB(insert_cmd, columns, values)

def insertZipCodeDB(csv_row):
   """ Insert zip code info into database """
   columns = ['zip_code', 'primary_city', 'state', 'county', 'latitude', 'longitude']
   values = [csv_row['zip'], csv_row['primary_city'], csv_row['state'], csv_row['county'], csv_row['latitude'], csv_row['longitude']]
   insert_cmd = 'INSERT INTO zip_codes (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDB(insert_cmd, columns, values)

def connectDB():
   """ Connect to the PostgreSQL database server and insert zip code info """
   try:
      # read connection parameters
      params = config()

      # connect to the PostgreSQL server
      global db_connection
      db_connection = psycopg2.connect(**params)

      # create a cursor
      global db_cursor
      db_cursor = db_connection.cursor()

   except (Exception, psycopg2.DatabaseError) as error:
      clean_up()
      sys.exit(error)

def useZip(row):
   return row['type'] == 'STANDARD' and row['state'] in STATES_LIST

def main():
   BASE_URL = 'https://www.landandfarm.com/search/'
   min_acre = 5
   max_acre = 100
   min_price = 5000
   max_price = 40000
   num_zip_codes = 0

   create_tables()
   connectDB()

   with open('../zip_code_database.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')

      # get number of valid zip codes to search
      num_zip_codes = sum([1 if useZip(row) else 0 for row in reader])

      # init progressBar
      printProgressBar(0, num_zip_codes, prefix='Progress', suffix='Complete', length=50)

      # reset csv iterator
      csvfile.seek(0);

      # TODO: REMOVE!!!!
      # temporarily jump to item 6880 as that's where error occured last night
      # csvfile.seek(6880);
      # num_zip_codes -= 6880

      # init proxies list
      proxies = get_proxies({'User-Agent': random.choice(USER_AGENT_LIST)})

      index = 0
      for row in reader:
         if useZip(row):
            insertZipCodeDB(row)
            request_url = f'{BASE_URL}{row["state"]}/{row["zip"]}-land-for-sale/?MinAcreage={min_acre}&MaxAcreage={max_acre}&MinPrice={min_price}&MaxPrice={max_price}'
            # get random user-agent
            headers = {'User-Agent': random.choice(USER_AGENT_LIST)}
            # get proxies intermittently
            if index % 100:
               proxies = get_proxies(headers)
            # use cycle_proxies to get request object from proxied server
            req = cycle_proxies(proxies, request_url, headers)

            if req.status_code == 200:
               soup = BeautifulSoup(req.text, 'html.parser')
               if not soup.findAll(text='No Results Found For Your Current Search'):
                  results_el = soup.find('div', {'id': 'searchResultsGrid'})
                  property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
                  property_info_list = [getPropertyInfo(prop_el, row['state'], row['zip']) for prop_el in property_card_el_list]
                  for prop_info in property_info_list:
                     insertListingDB(prop_info)

                  printProgressBar(index, num_zip_codes, prefix='Progress', suffix='Complete', length=50)
                  index += 1
            else:
               logging.error(f'Request not 200: {request_url}')

      # progress complete
      printProgressBar(num_zip_codes, num_zip_codes, prefix='Progress', suffix='Complete', length=50)

      clean_up()

if __name__ =='__main__':
   logging.basicConfig(filename='scrape_landandfarm.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
   logging.info('TEST LOGGING')
   main()

