import csv
import psycopg2
from psycopg2.extensions import AsIs
from datetime import datetime
import logging
import sys
from config.db_config import db_config, get_db_cursor, query_db
from config.utils import log_config

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