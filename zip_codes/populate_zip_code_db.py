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
      dbCleanUp()
      sys.exit(error)

def useZip(row):
   return (row['type'] == 'STANDARD' or row['type'] == 'PO BOX') and row['state'] in STATES_ABREVIATION_LIST

def insertZipCodeDB(csv_row):
   # do not insert it zip code not usable
   if (not useZip(csv_row)):
      return
   """ Insert zip code info into database """
   columns = ['zip_code', 'primary_city', 'state', 'county', 'latitude', 'longitude']
   values = [csv_row['zip'], csv_row['primary_city'], csv_row['state'], csv_row['county'], csv_row['latitude'], csv_row['longitude']]
   insert_cmd = 'INSERT INTO zip_codes (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDb(insert_cmd, columns, values)

def populateZipDb():
   with open('./db_config/zip_codes.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')
      for row in reader:
         insertZipCodeDB(row)

def main():
    createTables()
    connectDb()
    populateZipDb()

if __name__ =='__main__':
   logFileName = f'log/populate_zip_code_db_{str(datetime.now()).replace(" ", "_")}.log'
   logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
   main()