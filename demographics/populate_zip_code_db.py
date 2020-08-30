import csv
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import sys
from db_config.db_config import config, createTables

STATES_ABREVIATION_LIST = [
   'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
   'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
   'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
   'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

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
   'area_land',
   'area_water'
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

# postgres database connection
db_connection = None

# postgres database cursor
db_cursor = None

def dbCleanUp():
   """ close the communication with the PostgreSQL """
   if db_connection is not None:
      db_connection.close()
   if db_cursor is not None:
      db_cursor.close()

def connectDb():
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
      dbCleanUp()
      sys.exit(error)

def insertDb(insertCmd, columns, values):
   try:
      db_cursor.execute(insertCmd, (AsIs(','.join(columns)), tuple(values)))
      db_connection.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(f'columns: {columns}')
      logging.error(f'values: {values}')
      logging.error(error)
      dbCleanUp()
      sys.exit(error)

def getValue(csv_row, column):
   val = csv_row[column]
   return val if len(val) > 0 else None

def useZip(csv_row):
   return csv_row['type'] in ['STANDARD', 'PO BOX', 'UNIQUE']

def insertRowIntoTable(csv_row, table_name, columns):
   """ Insert zip code data info into database at specified table """
   if (not useZip(csv_row)):
      return

   values = [getValue(csv_row, columns[column_num]) for column_num in range(0, len(columns))]
   insert_cmd = f'INSERT INTO {table_name} (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDb(insert_cmd, columns, values)

def populateZipDb():
   with open('./demographics/zip_code_data.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')
      for row in reader:
         insertRowIntoTable(row, 'zip_codes', ZIP_CODES_COLUMNS)
         insertRowIntoTable(row, 'zip_demographics', ZIP_DEMOGRAPHICS_COLUMNS)
         insertRowIntoTable(row, 'zip_households', ZIP_HOUSEHOLDS_COLUMNS)
         insertRowIntoTable(row, 'zip_population_history', ZIP_POPULATION_HISTORY_COLUMNS)

def db_populated():
   ret = False
   try:
      query = 'SELECT COUNT(*) FROM zip_codes'
      db_cursor.execute(query)
      countZipCodes = db_cursor.fetchone()
      ret = True if countZipCodes == 42632 else False
   except (Exception, psycopg2.DatabaseError) as error:
      dbCleanUp()
      sys.exit(error)
   return ret

def main():
   connectDb()
   if not db_populated():
      logging.info('Populating database with zip code data')
      populateZipDb()
   else:
      logging.info('Database already populated with zip code data')

if __name__ =='__main__':
   logFileName = f'log/populate_zip_code_db_{str(datetime.now()).replace(" ", "_")}.log'
   logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
   main()