import csv
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import sys
from db_config.db_config import config, createTables

STATES_LIST = [
   {'state_abrev': 'AL', 'state_name': 'Alabama'},
   {'state_abrev': 'AK', 'state_name': 'Alaska'},
   {'state_abrev': 'AZ', 'state_name': 'Arizona'},
   {'state_abrev': 'AR', 'state_name': 'Arkansas'},
   {'state_abrev': 'CA', 'state_name': 'California'},
   {'state_abrev': 'CO', 'state_name': 'Colorado'},
   {'state_abrev': 'CT', 'state_name': 'Connecticut'},
   {'state_abrev': 'DE', 'state_name': 'Delaware'},
   {'state_abrev': 'DC', 'state_name': 'Washington DC'},
   {'state_abrev': 'FL', 'state_name': 'Florida'},
   {'state_abrev': 'GA', 'state_name': 'Georgia'},
   {'state_abrev': 'HI', 'state_name': 'Hawaii'},
   {'state_abrev': 'ID', 'state_name': 'Idaho'},
   {'state_abrev': 'IL', 'state_name': 'Illinois'},
   {'state_abrev': 'IN', 'state_name': 'Indiana'},
   {'state_abrev': 'IA', 'state_name': 'Iowa'},
   {'state_abrev': 'KS', 'state_name': 'Kansas'},
   {'state_abrev': 'KY', 'state_name': 'Kentucky'},
   {'state_abrev': 'LA', 'state_name': 'Louisiana'},
   {'state_abrev': 'ME', 'state_name': 'Maine'},
   {'state_abrev': 'MD', 'state_name': 'Maryland'},
   {'state_abrev': 'MA', 'state_name': 'Massachusetts'},
   {'state_abrev': 'MI', 'state_name': 'Michigan'},
   {'state_abrev': 'MN', 'state_name': 'Minnesota'},
   {'state_abrev': 'MS', 'state_name': 'Mississippi'},
   {'state_abrev': 'MO', 'state_name': 'Missouri'},
   {'state_abrev': 'MT', 'state_name': 'Montana'},
   {'state_abrev': 'NE', 'state_name': 'Nebraska'},
   {'state_abrev': 'NV', 'state_name': 'Nevada'},
   {'state_abrev': 'NH', 'state_name': 'New Hampshire'},
   {'state_abrev': 'NJ', 'state_name': 'New Jersey'},
   {'state_abrev': 'NM', 'state_name': 'New Mexico'},
   {'state_abrev': 'NY', 'state_name': 'New York'},
   {'state_abrev': 'NC', 'state_name': 'North Carolina'},
   {'state_abrev': 'ND', 'state_name': 'North Dakota'},
   {'state_abrev': 'OH', 'state_name': 'Ohio'},
   {'state_abrev': 'OK', 'state_name': 'Oklahoma'},
   {'state_abrev': 'OR', 'state_name': 'Oregon'},
   {'state_abrev': 'PA', 'state_name': 'Pennsylvania'},
   {'state_abrev': 'RI', 'state_name': 'Rhode Island'},
   {'state_abrev': 'SC', 'state_name': 'South Carolina'},
   {'state_abrev': 'SD', 'state_name': 'South Dakota'},
   {'state_abrev': 'TN', 'state_name': 'Tennessee'},
   {'state_abrev': 'TX', 'state_name': 'Texas'},
   {'state_abrev': 'UT', 'state_name': 'Utah'},
   {'state_abrev': 'VT', 'state_name': 'Vermont'},
   {'state_abrev': 'VA', 'state_name': 'Virginia'},
   {'state_abrev': 'WA', 'state_name': 'Washington'},
   {'state_abrev': 'WV', 'state_name': 'West Virginia'},
   {'state_abrev': 'WI', 'state_name': 'Wisconsin'},
   {'state_abrev': 'WY', 'state_name': 'Wyoming'},
   {'state_abrev': 'PR', 'state_name': 'Puerto Rico'},
   {'state_abrev': 'VI', 'state_name': 'Virgin Islands'},
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
   """ Connect to the PostgreSQL database server """
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

def populateStatesDb():
   columns = ['state_abrev', 'state_name']
   for state in STATES_LIST:
      values = [state['state_abrev'], state['state_name']]
      insert_cmd = f'INSERT INTO states (%s) VALUES %s ON CONFLICT DO NOTHING'
      insertDb(insert_cmd, columns, values)

def db_populated():
   ret = False
   try:
      query = 'SELECT COUNT(*) FROM states'
      db_cursor.execute(query)
      countStates = db_cursor.fetchone()
      ret = True if countStates == len(STATES_LIST) else False
   except (Exception, psycopg2.DatabaseError) as error:
      dbCleanUp()
      sys.exit(error)
   return ret

def main():
   connectDb()
   if not db_populated():
      logging.info('Populating database with states data')
      populateStatesDb()
   else:
      logging.info('Database already populated with states data')

if __name__ =='__main__':
   logFileName = f'log/populate_states_db_{str(datetime.now()).replace(" ", "_")}.log'
   logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
   main()