import csv
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import sys
from config.db_config import get_db_cursor, query_db
from config.utils import log_config
import os
import json

STATES_LIST = json.loads(os.environ['STATES_LIST'])

def populate_states_db():
   db_cursor = get_db_cursor()
   columns = ['state_abrev', 'state_name']
   for state in STATES_LIST:
      values = [state['state_abrev'], state['state_name']]
      insert_cmd = f'INSERT INTO states (%s) VALUES %s ON CONFLICT DO NOTHING'
      query_db(db_cursor, insert_cmd, columns, values)

def db_populated():
   ret = False
   db_cursor = get_db_cursor()
   try:
      query = 'SELECT COUNT(*) FROM states'
      db_cursor.execute(query)
      countStates = db_cursor.fetchone()
      ret = True if countStates == len(STATES_LIST) else False
   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(error)
      sys.exit(0)
   db_cursor.close()
   return ret

def main():
   if not db_populated():
      logging.info('Populating database with states data')
      populate_states_db()
   else:
      logging.info('Database already populated with states data')

if __name__ =='__main__':
   log_config('populate_state_db')
   main()