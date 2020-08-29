#!/usr/bin/env python3
import requests
from datetime import datetime
import logging
import random
import psycopg2
import sys
import json
from db_config.db_config import config, createTables
import time
import concurrent.futures

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

TOKEN = 'QYumHTESHvMktBsArZIjYseYqPxbHiom'

def getDbCursor():
   """ Connect to the PostgreSQL database server and insert zip code info """
   try:
      # read connection parameters
      params = config()

      # connect to the PostgreSQL server
      global dbConnection
      dbConnection = psycopg2.connect(**params)
      return dbConnection.cursor()

   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(error);
      sys.exit(error)

def get_results(res):
   if res.status_code == 200:
      res_dict = json.loads(res.text)
      if 'results' in res_dict:
         return res_dict['results']

def get_stations_for_state(state_id, dataset_id, start_date, end_date, datatypeid):
   url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid={state_id}&datasetid={dataset_id}&startdate={start_date}&enddate={end_date}&limit=1000&datatypeid={datatypeid}'
   res = requests.get(url, headers={'token': TOKEN})
   stations_list = get_results(res)
   return stations_list if stations_list else []

def get_state_info_list():
   url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=55'
   res = requests.get(url, headers={'token': TOKEN})
   states_list = get_results(res)
   states_list = states_list if states_list else []
   return [state for state in states_list if state['name'] != "District of Columbia"]

def get_avg_temp_station(station):
   # TODO
   print(station)

def get_mean(num_list):
   return sum(num_list) / len(num_list)
   
def get_standard_dev(num_list):
   mean = get_mean(num_list)
   variance = sum([((x - mean) ** 2) for x in num_list]) / len(num_list) 
   return variance ** 0.5
   
def write_stations_count_by_datatype_to_file():
   states_list = get_state_info_list()
   # stations_by_state = {}
   with open('./noaa_weather/noaa_states_stations_count_by_datatype.txt', 'w') as stations_file:
      for state in states_list:
         print(state['name'])
         stations_file.write('\n')
         stations_file.write(f'{state["name"]}')
         stations_file.write('\n')
         state_stations_count_list = []
         datatype_list = ['TMIN', 'TMAX', 'TAVG', 'MMNT', 'MMXT', 'MNTM', 'PRCP', 'SNOW']

         for datatypeid in datatype_list:
            state_stations_list = get_stations_for_state(state['id'], 'GHCND', '2015-01-01', '2020-01-01', datatypeid)
            state_stations_count_list.append({'id': datatypeid, 'count': len(state_stations_list)})
            # stations_by_state[state['name']] = state_stations_list

         for datatype_count in sorted(state_stations_count_list, key=lambda k: k['count']) :
            stations_file.write(f'{datatype_count["id"]} station count: {datatype_count["count"]}')
            stations_file.write('\n')

         monthly_mean_list = [d['count'] for d in state_stations_count_list if d['id'] in ['MMNT', 'MMXT', 'MNTM']]
         daily_temp_list = [d['count'] for d in state_stations_count_list if d['id'] in ['TMIN', 'TMAX', 'TAVG']]

         standard_dev_monthly_mean = get_standard_dev(monthly_mean_list)
         standard_dev_daily_tmp = get_standard_dev(daily_temp_list)

         stations_file.write(f'Standard Dev MMNT, MMXT, MNTM: {standard_dev_monthly_mean}')
         stations_file.write('\n')
         stations_file.write(f'Standard Dev TMIN, TMAX, TAVG: {standard_dev_daily_tmp}')
         stations_file.write('\n')
         stations_file.write(f'Standard Dev % of MMNT, MMXT, MNTM average: {standard_dev_monthly_mean/get_mean(monthly_mean_list)*100}')
         stations_file.write('\n')
         stations_file.write(f'Standard Dev % of TMIN, TMAX, TAVG average: {standard_dev_daily_tmp/get_mean(daily_temp_list)*100}')
         stations_file.write('\n')

         # print(f'{state["name"]} first station: {stations_by_state[state["name"]][0]}')
         """
         EXAMPLE:
            Alabama first station:
            {'elevation': 249.3, 'mindate': '1938-03-01', 'maxdate': '2020-08-22', 'latitude': 34.2553, 'name': 'ADDISON, AL US', 'datacoverage': 0.4768, 'id': 'GHCND:USC00010063', 'elevationUnit': 'METERS', 'longitude': -87.1814}
         """

def main():
   """
   Need following datatypes:
      PRCP: precipitation
      SNOW: snow
      TMIN: temperature minimum
      TMAX: temperature maximum
   """
   states_list = get_state_info_list()
   # stations_by_state = {}
   for state in states_list:
      state_stations_list = get_stations_for_state(state['id'], 'GHCND', '2015-01-01', '2020-01-01', 'TMIN')
      print(f'{state["name"]} stations count: {len(state_stations_list)}')

      """
      EXAMPLE:
         Alabama first station:
         {'elevation': 249.3, 'mindate': '1938-03-01', 'maxdate': '2020-08-22', 'latitude': 34.2553, 'name': 'ADDISON, AL US', 'datacoverage': 0.4768, 'id': 'GHCND:USC00010063', 'elevationUnit': 'METERS', 'longitude': -87.1814}
      """

      # TODO remove
      if state['name'] == 'California':
         break

if __name__ =='__main__':
   # TODO enable logs
   # logFileName = f'log/noaa_weather_by_zip_{str(datetime.now()).replace(" ", "_")}.log'
   # logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
   main()
