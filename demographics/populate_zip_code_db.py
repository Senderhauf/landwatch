import csv
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import sys
from config.db_config import get_db_cursor, query_db
from config.utils import log_config
import json
import os

STATES_ABREV_LIST = [state['state_abrev'] for state in json.loads(os.environ['STATES_LIST'])]

ZIP_CODES_COLUMNS = [
   'zip_code',
   'primary_city',
   'county',
   'type',
   'decommissioned',
   'acceptable_cities',
   'unacceptable_cities',
   'state_abrev',
   'timezone',
   'area_codes',
   'approximate_latitude',
   'approximate_longitude',
   'polygon_offset_latitude',
   'polygon_offset_longitude',
   'internal_point_latitude',
   'internal_point_longitude',
   'latitude_min',
   'latitude_max',
   'longitude_min',
   'longitude_max',
   'area_land_sqaure_meters',
   'area_water_sqaure_meters'
]

ZIP_DEMOGRAPHICS_COLUMNS = [
   'zip_code',
   'white',
   'black_or_african_american',
   'american_indian_or_alaskan_native',
   'asian',
   'native_hawaiian_and_other_pacific_islander',
   'other_race',
   'two_or_more_races',
   'total_male_population',
   'total_female_population',
   'pop_under_10',
   'pop_10_to_19',
   'pop_20_to_29',
   'pop_30_to_39',
   'pop_40_to_49',
   'pop_50_to_59',
   'pop_60_to_69',
   'pop_70_to_79',
   'pop_80_plus',
   'population_count',
   'population_center_latitude',
   'population_center_longitude',
   'housing_count',
   'median_household_income',
   'median_gross_rent',
   'median_home_value',
   'percent_population_in_poverty',
   'median_earnings_past_year',
   'percent_high_school_graduate',
   'percent_bachelors_degree',
   'percent_graduate_degree'
]

ZIP_HOUSEHOLDS_COLUMNS = [
   'zip_code',
   'irs_estimated_households_2015',
   'irs_estimated_households_2014',
   'irs_estimated_households_2013',
   'irs_estimated_households_2012',
   'irs_estimated_households_2011',
   'irs_estimated_households_2010',
   'irs_estimated_households_2009',
   'irs_estimated_households_2008',
   'irs_estimated_households_2007',
   'irs_estimated_households_2006',
   'irs_estimated_households_2005',
   'acs_estimated_households_2016',
   'acs_estimated_households_2016_margin',
   'acs_estimated_households_2015',
   'acs_estimated_households_2015_margin',
   'acs_estimated_households_2014',
   'acs_estimated_households_2014_margin',
   'acs_estimated_households_2013',
   'acs_estimated_households_2013_margin',
   'acs_estimated_households_2012',
   'acs_estimated_households_2012_margin',
   'acs_estimated_households_2011',
   'acs_estimated_households_2011_margin'
]

ZIP_POPULATION_HISTORY_COLUMNS = [
   'zip_code',
   'irs_estimated_population_2015',
   'irs_estimated_population_2014',
   'irs_estimated_population_2013',
   'irs_estimated_population_2012',
   'irs_estimated_population_2011',
   'irs_estimated_population_2010',
   'irs_estimated_population_2009',
   'irs_estimated_population_2008',
   'irs_estimated_population_2007',
   'irs_estimated_population_2006',
   'irs_estimated_population_2005',
   'acs_estimated_population_2016',
   'acs_estimated_population_2016_margin',
   'acs_estimated_population_2015',
   'acs_estimated_population_2015_margin',
   'acs_estimated_population_2014',
   'acs_estimated_population_2014_margin',
   'acs_estimated_population_2013',
   'acs_estimated_population_2013_margin',
   'acs_estimated_population_2012',
   'acs_estimated_population_2012_margin',
   'acs_estimated_population_2011',
   'acs_estimated_population_2011_margin'
]

def get_value(csv_row, column):
   val = csv_row[column]
   return val if len(val) > 0 else None

def use_zip(csv_row):
   return csv_row['type'] in ['STANDARD', 'PO BOX', 'UNIQUE'] and csv_row['state_abrev'] in STATES_ABREV_LIST

def insert_row_into_table(db_cursor, csv_row, table_name, columns):
   """ Insert zip code data info into database at specified table """
   if (not use_zip(csv_row)):
      return

   values = [get_value(csv_row, columns[column_num]) for column_num in range(0, len(columns))]
   insert_cmd = f'INSERT INTO {table_name} (%s) VALUES %s ON CONFLICT DO NOTHING'
   query_db(db_cursor, insert_cmd, columns, values)

def populate_zip_db():
   with open('./demographics/zip_code_data.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')
      db_cursor = get_db_cursor()
      for row in reader:
         insert_row_into_table(db_cursor, row, 'zip_codes', ZIP_CODES_COLUMNS)
         insert_row_into_table(db_cursor, row, 'zip_demographics', ZIP_DEMOGRAPHICS_COLUMNS)
         insert_row_into_table(db_cursor, row, 'zip_households', ZIP_HOUSEHOLDS_COLUMNS)
         insert_row_into_table(db_cursor, row, 'zip_population_history', ZIP_POPULATION_HISTORY_COLUMNS)

def db_populated():
   ret = False
   db_cursor = get_db_cursor()
   try:
      query = 'SELECT COUNT(*) FROM zip_codes'
      db_cursor.execute(query)
      countZipCodes = db_cursor.fetchone()
      ret = True if countZipCodes == 42632 else False
   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(error)
      sys.exit(error)
   db_cursor.close()
   return ret

def main():
   if not db_populated():
      logging.info('Populating database with zip code data...')
      populate_zip_db()
   else:
      logging.info('Database already populated with zip code data...')

if __name__ =='__main__':
   log_config('populate_zip_code_db')
   main()