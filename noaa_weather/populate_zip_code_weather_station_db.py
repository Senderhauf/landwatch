#!/usr/bin/env python3
import logging
from config.db_config import get_db_cursor, query_db
from config.utils import log_config
import concurrent.futures
import json
import os

MAX_THREADS = int(os.environ['MAX_THREADS'])

STATES_ABREV_LIST = [state['state_abrev'] for state in json.loads(os.environ['STATES_LIST'])]

def insert_db(db_cursor, station_id, zip_code):
    columns = ['station_id', 'zip_code']
    values = [station_id, zip_code]
    insert_cmd = 'INSERT INTO zip_code_noaa_weather_stations (%s) VALUES %s ON CONFLICT DO NOTHING'
    query_db(db_cursor, insert_cmd, columns, values)

def get_nearest_noaa_weather_station(zip_code):
    db_cursor = get_db_cursor()
    query_cmd = (
        f'SELECT stations.station_id FROM noaa_weather_stations as stations '
        f'ORDER BY stations.geog <-> '
        f'(SELECT approximate_geog FROM zip_codes where zip_code like \'{zip_code}\') '
        f'LIMIT 1;'
    )
    db_cursor.execute(query_cmd)
    station_id = db_cursor.fetchone()[0]
    logging.info(f'Inserting station id {station_id} for zip code {zip_code} ...')
    insert_db(db_cursor, station_id, zip_code)
    db_cursor.close()

def get_zip_code_list():
    db_cursor = get_db_cursor()
    db_cursor.execute('SELECT zip_code, state_abrev FROM zip_codes')
    query_results = db_cursor.fetchall()
    zip_code_list = [zip_code for (zip_code, state_abrev) in query_results if state_abrev in STATES_ABREV_LIST]
    db_cursor.close()
    return zip_code_list

def main():
    logging.info('Populating database with nearest weather stations for each zip code ...')
    zip_code_list = get_zip_code_list()
    logging.info(f'Number of zip codes: {len(zip_code_list)}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(get_nearest_noaa_weather_station, zip_code_list)

if __name__ =='__main__':
    log_config('populate_zip_code_weather_station_db')
    main()
