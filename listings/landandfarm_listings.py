#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import random
import sys
from config.db_config import get_db_cursor, query_db
from config.utils import log_config, get_request
import time
import concurrent.futures
import json
import os

NL='\n'

STATES_LIST = json.loads(os.environ['STATES_LIST'])

MAX_THREADS = int(os.environ['MAX_THREADS'])

def getAttribute(element, attribute):
   try:
      return element[attribute]
   except KeyError:
      return None

def getPropertyZipCode(propertyCardElement, stateAbrev):
   addressElement = propertyCardElement.find('address', {'class': 'location'})
   addressText = addressElement.text
   nums = re.findall(r'\d+', addressText[addressText.index(stateAbrev):])
   return next((num for num in nums if len(num)==5), '')

def getPropertyInfo(propertyCardElement, state):
   zipCode = getPropertyZipCode(propertyCardElement, state['state_abrev'])
   urlElement = propertyCardElement.find('a', {'class': 'property-card--property-link'})
   url = f'www.landandfarm.com{urlElement["href"]}'
   priceElement = propertyCardElement.find('div', {'class': 'property-card--price'})
   priceElementText = priceElement.get_text()
   price = int(priceElementText[priceElementText.index('$')+1::].replace(',', ''))
   statsElement = propertyCardElement.find('div', {'class': 'property-card--quick-stats'})
   acresText = statsElement.span.get_text()
   acresString = acresText[:acresText.index('acres')].strip()
   acres = float(acresString)
   listingIdElement = propertyCardElement.find('div', {'class': 'property-card--saved-indicator'})
   listingId = listingIdElement['data-savable-property-id']
   return {
      'listing_id': listingId,
      'price': price,
      'acres': acres,
      'latitude': getAttribute(propertyCardElement, 'data-mappable-latitude'),
      'longitude': getAttribute(propertyCardElement, 'data-mappable-longitude'),
      'zip_code': zipCode,
      'url': url
   }

def insertListingDB(property_info):
   """ Insert property info listings into database """
   db_cursor = get_db_cursor()

   # check zip_code is valid
   db_cursor.execute(f'SELECT approximate_latitude, approximate_longitude FROM zip_codes WHERE zip_code LIKE \'{property_info["zip_code"]}\'')
   lat_long = db_cursor.fetchone()
   
   if (lat_long):
      columns = ['listing_id', 'price', 'acres', 'geog', 'latitude', 'longitude', 'insert_date', 'zip_code', 'price_per_acre', 'url']
      # get geometry value from lat and long
      geometry = None;
      if property_info['longitude'] is None or property_info['latitude'] is None:
         latitude = lat_long[0]
         longitude = lat_long[1]
         geometry_cmd = f'SELECT ST_SetSRID(ST_MakePoint({longitude}, {latitude}),4326)'
         db_cursor.execute(geometry_cmd)
         geometry = db_cursor.fetchone();
      else:
         geometry_cmd = f'SELECT ST_SetSRID(ST_MakePoint({property_info["longitude"]}, {property_info["latitude"]}),4326)'
         db_cursor.execute(geometry_cmd)
         geometry = db_cursor.fetchone()
      values = [
         property_info['listing_id'],
         property_info['price'],
         property_info['acres'],
         geometry,
         property_info['latitude'],
         property_info['longitude'],
         datetime.utcnow(),
         property_info['zip_code'],
         property_info['price']/property_info['acres'],
         property_info['url']
      ]
      insert_cmd = 'INSERT INTO listings (%s) VALUES %s ON CONFLICT DO NOTHING'
      query_db(db_cursor, insert_cmd, columns, values)
   else:
      logging.error('Error at landandfarm_listings.insertListingDB')
      logging.error(f'Zip code {property_info["zip_code"]} does not exist in zip_code database. url: {property_info["url"]}')

def getPagination(url):
   """get pagination if available"""
   numPages = 1
   res = get_request(url)
   if res.status_code == 200:
      soup = BeautifulSoup(res.text, 'html.parser')
      if not soup.findAll(text='No Results Found For Your Current Search'):
         headerText = soup.find('span', {'id': 'searchHeader'}).text
         pages = re.findall(r'\d+', headerText[headerText.index('Page 1 of')+9:]) if 'Page 1 of' in headerText else []
         
         try:
            numPages = int(pages[0]) if len(pages) else 1
         except ValueError as e:
            logging.error('Error at landandfarm_listings.getPagination')
            logging.error(e)
            sys.exit(e)
         
   return numPages

def scrapeListingPage(stateUrlParam):
   res = get_request(stateUrlParam['url'])
   if res.status_code == 200:
      soup = BeautifulSoup(res.text, 'html.parser')
      if not soup.findAll(text='No Results Found For Your Current Search'):
         resultsElement = soup.find('div', {'id': 'searchResultsGrid'})
         propertyCardElementList = resultsElement.find_all('article', {'class': 'property-card'})
         propertyInfoList = [getPropertyInfo(propertyElement, stateUrlParam['state']) for propertyElement in propertyCardElementList]
         for propInfo in propertyInfoList:
            insertListingDB(propInfo)

def scrapeStatePages(state):
   logging.info(f'Scrape {state["state_name"]} Pages...')

   BASE_URL = 'https://www.landandfarm.com/search/'
   min_acre = 5
   max_acre = 60
   min_price = 5000
   max_price = 30000
   request_url = f'{BASE_URL}{state["state_name"]}-land-for-sale/?MinAcreage={min_acre}&MaxAcreage={max_acre}&MinPrice={min_price}&MaxPrice={max_price}'
   scrapeListingPage({'state': state, 'url': request_url})

   # if this is the first page check for pagination and scrape the next pages results
   pagination = getPagination(request_url)

   threads = min(MAX_THREADS, pagination)
   with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
      mapList = list(map(lambda num: {'state': state, 'url': request_url+f'&CurrentPage={num}'}, range(2, pagination+1)))
      executor.map(scrapeListingPage, mapList)
      # executor.shutdown(wait=True)

def main():
   for state in STATES_LIST:
      scrapeStatePages(state)

if __name__ =='__main__':
   log_config('landandfarm_listings')
   main()
