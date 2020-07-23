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

NL='\n'

STATES_LIST = [
   'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
   'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
   'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
   'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
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

def getPropertyInfo(property_card_el, state, zip_code):
   price_el = property_card_el.find('div', {'class': 'property-card--price'})
   price_el_text = price_el.get_text()
   price = int(price_el_text[price_el_text.index('$')+1::].replace(',', ''))
   stats_el = property_card_el.find('div', {'class': 'property-card--quick-stats'})
   acres_text = stats_el.span.get_text()
   acres_str = acres_text[:acres_text.index('acres')].strip()
   acres = float(acres_str)
   return {
      'id': property_card_el['data-mappable-property-id'],
      'price': price,
      'acres': acres,
      'latitude': property_card_el['data-mappable-latitude'],
      'longitude': property_card_el['data-mappable-longitude'],
      'zip_code': zip_code
   }

def insertDB(insert_cmd):
   try:
      db_cursor.execute(insert_cmd, (AsIs(','.join(columns)), tuple(values)))
      db_connection.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      clean_up()
      sys.exit(error)

def insertListingDB(property_info):
   """ Insert property info listings into database """
   columns = ['id', 'price', 'acres', 'geog', 'insert_date', 'zip']
   values = [
      property_info['id'],
      property_info['price'],
      property_info['acres'],
      f'ST_SetSRID(ST_MakePoint({property_info["longitude"]}, {property_info["latitude"]}),4326)',
      property_info[''],
      property_info['zip_code'],
   ]
   insert_cmd = 'insert into listings (%s) values %s'
   insertDB(insert_cmd)

def insertZipCodeDB(csv_row):
   """ Insert zip code info into database """
   columns = ['zip_code', 'primary_city', 'state', 'county']
   values = [csv_row['zip'], csv_row['primary_city'], csv_row['state'], csv_row['county']]
   insert_cmd = 'insert into zip_codes (%s) values %s'
   insertDB(insert_cmd)

def connectDB():
   """ Connect to the PostgreSQL database server and insert zip code info """
   try:
      # read connection parameters
      params = config()

      # connect to the PostgreSQL server
      db_connection = psycopg2.connect(**params)

      # create a cursor
      db_cursor = db_connection.cursor()

   except (Exception, psycopg2.DatabaseError) as error:
      clean_up()
      # exit and display error
      sys.exit(error)

def useZip(row):
   return row['type'] == 'STANDARD' and row['state'] in STATES_LIST

def main():
   BASE_URL = 'https://www.landandfarm.com/search/'
   min_acre = 5
   max_acre = 40
   min_price = 5000
   max_price = 20000
   headers = {'User-Agent': 'Mozilla/5.0 (X11: Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
   num_zip_codes = 0;

   create_tables()

   with open('../zip_code_database.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')

      # get number of valid zip codes to search
      num_zip_codes = sum([1 if useZip(row) else 0 for row in reader])
      print(f'num_zip_codes: {num_zip_codes}')

      # init progressBar
      printProgressBar(0, num_zip_codes, prefix='Progress', suffix='Complete', length=50)

      # reset csv iterator
      csvfile.seek(0);

      index = 0
      for row in reader:
         if useZip(row):
            # request_url = f'{BASE_URL}{row["state"]}/{row["zip"]}-land-for-sale/?MinPrice={min_price}&MaxPrice={max_price}'
            request_url = f'https://www.landandfarm.com/search/CO/80465-land-for-sale'
            req = requests.get(request_url, headers=headers)

            if req.status_code == 200:
               soup = BeautifulSoup(req.text, 'html.parser')
               if not soup.findAll(text='No Results Found For Your Current Search'):
                  results_el = soup.find('div', {'id': 'searchResultsGrid'})
                  property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
                  propertyInfoList = [getPropertyInfo(prop_el, row['state'], row['zip']) for prop_el in property_card_el_list]

                  writeToDB(propertyInfoList)

                  printProgressBar(index, num_zip_codes, prefix='Progress', suffix='Complete', length=50)
                  index += 1

                  # temporary for debugging purposes
                  break
      # progress complete
      printProgressBar(num_zip_codes, num_zip_codes, prefix='Progress', suffix='Complete', length=50)

      clean_up()

if __name__ =='__main__':
    main()

