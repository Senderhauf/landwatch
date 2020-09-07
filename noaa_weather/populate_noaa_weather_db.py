#!/usr/bin/env python3
import logging
import random
import json
from config.db_config import get_db_cursor, query_db
from config.utils import log_config, get_request
from datetime import datetime
from dateutil.relativedelta import relativedelta
import concurrent.futures
import os

TOKEN_LIST = json.loads(os.environ['NOAA_API_TOKEN_LIST'])

MAX_THREADS = int(os.environ['MAX_THREADS'])

def get_results(res):
   results_list = []
   if res.status_code == 200:
      res_dict = json.loads(res.text)
      if 'results' in res_dict:
         results_list = res_dict['results'] if len(res_dict['results']) else []
   return results_list

def get_results_set_count(res):
   results_count = 0
   if res.status_code == 200:
      res_dict = json.loads(res.text)
      if 'metadata' in res_dict:
         if 'resultset' in res_dict['metadata']:
            if 'count' in res_dict['metadata']['resultset']:
               results_count = res_dict['metadata']['resultset']['count']
   return results_count

def get_stations_for_state(state, dataset_id, start_date, end_date, datatypeid_list=[]):
   state_id = state['id']
   url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid={state_id}&datasetid={dataset_id}&startdate={start_date}&enddate={end_date}&limit=1000'
   for datatypeid in datatypeid_list:
      url = url + f'&datatypeid={datatypeid}'
   res = get_request(url, {'token': random.choice(TOKEN_LIST)})
   stations_list = get_results(res)
   insert_stations_db(stations_list, state)
   return stations_list

def get_state_info_list():
   url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=55'
   res = get_request(url, {'token': random.choice(TOKEN_LIST)})
   states_list = get_results(res)
   states_list = states_list if states_list else []
   return [state for state in states_list if state['name'] != "District of Columbia"]

def insert_datapoint_db(values):
   db_cursor = get_db_cursor()
   columns = ['station_id', 'month', 'year', 'data_type', 'value']
   insert_cmd = 'INSERT INTO noaa_monthly_averages (%s) VALUES %s ON CONFLICT DO NOTHING'
   query_db(db_cursor, insert_cmd, columns, values)

def get_station_data(params):
   station_id = params['station_id']
   dataset_id = params['data_params']['dataset_id']
   start_date = params['data_params']['start_date']
   end_date = params['data_params']['end_date']
   datatypeid_list = params['data_params']['datatypeid_list']
   
   logging.info(f'Getting {start_date.year} info for station: {station_id} ...')
   start_date_str = start_date.strftime('%Y-%m-%d')
   end_date_str = end_date.strftime('%Y-%m-%d')
   url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?stationid={station_id}&datasetid={dataset_id}&startdate={start_date_str}&enddate={end_date_str}&units=standard&limit=1000'
   for datatypeid in datatypeid_list:
      url = url + f'&datatypeid={datatypeid}'
   res = get_request(url, {'token': random.choice(TOKEN_LIST)})
   datapoints = get_results(res)
   result_set_count = get_results_set_count(res)
   while len(datapoints) < result_set_count:
      res = get_request(url+f'&offset={len(datapoints)}', {'token': random.choice(TOKEN_LIST)})
      datapoints = datapoints + get_results(res)
   insert_monthly_avg_db(datapoints, station_id)

def insert_stations_db(station_list, state):
   db_cursor = get_db_cursor();
   for station in station_list:
      # get postgis geogrpahy value for station 
      geometry_cmd = f'SELECT ST_SetSRID(ST_MakePoint({station["longitude"]}, {station["latitude"]}),4326)'
      db_cursor.execute(geometry_cmd)
      geometry = db_cursor.fetchone()
      columns = [
         'station_id', 'elevation', 'min_date', 'max_date', 'name', 
         'data_coverage', 'elevation_unit', 'geog', 'latitude', 'longitude',
         'state_name', 'state_fips_id'
      ]
      values = [
         station['id'],
         station['elevation'],
         station['mindate'],
         station['maxdate'],
         station['name'],
         station['datacoverage'],
         station['elevationUnit'],
         geometry,
         station['latitude'],
         station['longitude'],
         state['name'],
         state['id']
      ]
      insert_cmd = 'INSERT INTO noaa_weather_stations (%s) VALUES %s ON CONFLICT DO NOTHING'
      query_db(db_cursor, insert_cmd, columns, values)

def get_avg(num_list):
   return (sum(num_list) / len(num_list)) if len(num_list) else None

def insert_monthly_avg_db(datapoints, station_id):
   if not len(datapoints): return
   cur_year = datetime.strptime(datapoints[0]['date'], '%Y-%m-%dT%H:%M:%S').year
   for cur_month in range(1,13):
      datapoints_cur_month = [dp for dp in datapoints if datetime.strptime(dp['date'], '%Y-%m-%dT%H:%M:%S').month == cur_month]
      snow_avg = get_avg([dp['value'] for dp in datapoints_cur_month if dp['datatype'] == 'SNOW'])
      prcp_avg = get_avg([dp['value'] for dp in datapoints_cur_month if dp['datatype'] == 'PRCP'])
      tmin_avg = get_avg([dp['value'] for dp in datapoints_cur_month if dp['datatype'] == 'TMIN'])
      tmax_avg = get_avg([dp['value'] for dp in datapoints_cur_month if dp['datatype'] == 'TMAX'])
      tavg = get_avg([dp['value'] for dp in datapoints_cur_month if dp['datatype'] == 'TMIN' or dp['datatype'] == 'TMAX'])
      
      # station_id, month, year, data_type, value
      insert_datapoint_db([station_id, cur_month, cur_year, 'SNOW', snow_avg])
      # logging.info(f'{cur_month}/{cur_year} SNOW avg for station {station_id}: {snow_avg}')
      insert_datapoint_db([station_id, cur_month, cur_year, 'PRCP', prcp_avg])
      # logging.info(f'{cur_month}/{cur_year} PRCP avg for station {station_id}: {prcp_avg}')
      insert_datapoint_db([station_id, cur_month, cur_year, 'TMIN', tmin_avg])
      # logging.info(f'{cur_month}/{cur_year} TMIN avg for station {station_id}: {tmin_avg}')
      insert_datapoint_db([station_id, cur_month, cur_year, 'TMAX', tmax_avg])
      # logging.info(f'{cur_month}/{cur_year} TMAX avg for station {station_id}: {tmax_avg}')
      insert_datapoint_db([station_id, cur_month, cur_year, 'TAVG', tavg])
      # logging.info(f'{cur_month}/{cur_year} TAVG avg for station {station_id}: {tavg}')

def main():
   """
   Need following datatypes:
      PRCP: precipitation
      SNOW: snow
      TMIN: temperature minimum
      TMAX: temperature maximum
   """
   logging.info('Getting list of states info...')
   states_list = get_state_info_list()
   for state in states_list:
      start_time = datetime.now()
      logging.info(f'Getting info for state: {state["name"]} ...')
      dataset_id = 'GHCND'
      datatypeid_list = ['TMIN', 'TMAX', 'PRCP', 'SNOW']
      num_stations_state_total = 0

      # get last 5 years worth of data
      start_date = datetime.today().replace(day=1)
      for i in range(5):
         end_date = start_date
         start_date = end_date - relativedelta(years=1)
         start_date_str = start_date.strftime('%Y-%m-%d')
         end_date_str = end_date.strftime('%Y-%m-%d')
         # leave out SNOW datatype when getting stations as we still want stations that have only data for TMIN, TMAX, and PRCP
         state_station_list = get_stations_for_state(state, dataset_id, start_date_str, end_date_str, datatypeid_list[:3])
         data_params = {'dataset_id': dataset_id, 'start_date': start_date, 'end_date': end_date, 'datatypeid_list': datatypeid_list}
         get_station_data_params_list = [{'station_id': station['id'], 'data_params': data_params} for station in state_station_list]
         num_stations = len(state_station_list)
         num_stations_state_total = num_stations_state_total + num_stations
         threads = min(MAX_THREADS, num_stations)
         logging.info(f'{state["name"]} has {num_stations} stations. Getting data for {start_date.year}...')
         with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(get_station_data, get_station_data_params_list)
      end_time = datetime.now()
      logging.info(f'Time elapsed for {state["name"]}: {str(end_time - start_time)}')
      logging.info(f'Amount of seconds per station for {state["name"]}: {(end_time - start_time).total_seconds() / num_stations_state_total}')

if __name__ =='__main__':
   log_config('populate_noaa_weather_db')
   main()
