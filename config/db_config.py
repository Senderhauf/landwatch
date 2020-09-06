#!/usr/bin/env python3
import psycopg2
from configparser import ConfigParser
import sys
import logging
from .utils import log_config
import psycopg2
from psycopg2.extensions import AsIs

def db_config(filename='./config/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE EXTENSION IF NOT EXISTS postgis;
        """,
        """
        CREATE TABLE IF NOT EXISTS states (
            state_abrev CHAR(2) PRIMARY KEY,
            state_name TEXT NOT NULL,
            UNIQUE (state_name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS zip_codes (
            zip_code CHAR(5) PRIMARY KEY,
            primary_city TEXT,
            county TEXT,
            type TEXT NOT NULL,
            decommissioned BOOLEAN,
            acceptable_cities TEXT,
            unacceptable_cities TEXT,
            state_abrev CHAR(2),
            timezone TEXT,
            area_codes TEXT,
            approximate_latitude DOUBLE PRECISION NOT NULL,
            approximate_longitude DOUBLE PRECISION NOT NULL,
            polygon_offset_latitude DOUBLE PRECISION,
            polygon_offset_longitude DOUBLE PRECISION,
            internal_point_latitude DOUBLE PRECISION,
            internal_point_longitude DOUBLE PRECISION,
            latitude_min DOUBLE PRECISION,
            latitude_max DOUBLE PRECISION,
            longitude_min DOUBLE PRECISION,
            longitude_max DOUBLE PRECISION,
            area_land_sqaure_meters BIGINT,
            area_water_sqaure_meters BIGINT,
            FOREIGN KEY (state_abrev)
                REFERENCES states (state_abrev)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS zip_demographics (
            zip_code CHAR(5) PRIMARY KEY,
            white INTEGER,
            black_or_african_american INTEGER,
            american_indian_or_alaskan_native INTEGER,
            asian INTEGER,
            native_hawaiian_and_other_pacific_islander INTEGER,
            other_race INTEGER,
            two_or_more_races INTEGER,
            total_male_population INTEGER,
            total_female_population INTEGER,
            pop_under_10 INTEGER,
            pop_10_to_19 INTEGER,
            pop_20_to_29 INTEGER,
            pop_30_to_39 INTEGER,
            pop_40_to_49 INTEGER,
            pop_50_to_59 INTEGER,
            pop_60_to_69 INTEGER,
            pop_70_to_79 INTEGER,
            pop_80_plus INTEGER,
            population_count INTEGER,
            population_center_latitude DOUBLE PRECISION,
            population_center_longitude DOUBLE PRECISION,
            housing_count INTEGER,
            median_household_income INTEGER,
            median_gross_rent INTEGER,
            median_home_value INTEGER,
            percent_population_in_poverty REAL,
            median_earnings_past_year INTEGER,
            percent_high_school_graduate REAL,
            percent_bachelors_degree REAL,
            percent_graduate_degree REAL,
            FOREIGN KEY (zip_code)
                REFERENCES zip_codes (zip_code)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS zip_households (
            zip_code CHAR(5) PRIMARY KEY,
            irs_estimated_households_2015 INTEGER,
            irs_estimated_households_2014 INTEGER,
            irs_estimated_households_2013 INTEGER,
            irs_estimated_households_2012 INTEGER,
            irs_estimated_households_2011 INTEGER,
            irs_estimated_households_2010 INTEGER,
            irs_estimated_households_2009 INTEGER,
            irs_estimated_households_2008 INTEGER,
            irs_estimated_households_2007 INTEGER,
            irs_estimated_households_2006 INTEGER,
            irs_estimated_households_2005 INTEGER,
            acs_estimated_households_2016 INTEGER,
            acs_estimated_households_2016_margin INTEGER,
            acs_estimated_households_2015 INTEGER,
            acs_estimated_households_2015_margin INTEGER,
            acs_estimated_households_2014 INTEGER,
            acs_estimated_households_2014_margin INTEGER,
            acs_estimated_households_2013 INTEGER,
            acs_estimated_households_2013_margin INTEGER,
            acs_estimated_households_2012 INTEGER,
            acs_estimated_households_2012_margin INTEGER,
            acs_estimated_households_2011 INTEGER,
            acs_estimated_households_2011_margin INTEGER,
            FOREIGN KEY (zip_code)
                REFERENCES zip_codes (zip_code)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS zip_population_history (
            zip_code CHAR(5) PRIMARY KEY,
            irs_estimated_population_2015 INTEGER,
            irs_estimated_population_2014 INTEGER,
            irs_estimated_population_2013 INTEGER,
            irs_estimated_population_2012 INTEGER,
            irs_estimated_population_2011 INTEGER,
            irs_estimated_population_2010 INTEGER,
            irs_estimated_population_2009 INTEGER,
            irs_estimated_population_2008 INTEGER,
            irs_estimated_population_2007 INTEGER,
            irs_estimated_population_2006 INTEGER,
            irs_estimated_population_2005 INTEGER,
            acs_estimated_population_2016 INTEGER,
            acs_estimated_population_2016_margin INTEGER,
            acs_estimated_population_2015 INTEGER,
            acs_estimated_population_2015_margin INTEGER,
            acs_estimated_population_2014 INTEGER,
            acs_estimated_population_2014_margin INTEGER,
            acs_estimated_population_2013 INTEGER,
            acs_estimated_population_2013_margin INTEGER,
            acs_estimated_population_2012 INTEGER,
            acs_estimated_population_2012_margin INTEGER,
            acs_estimated_population_2011 INTEGER,
            acs_estimated_population_2011_margin INTEGER,
            FOREIGN KEY (zip_code)
                REFERENCES zip_codes (zip_code)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS listings (
            listing_id INTEGER PRIMARY KEY,
            price INTEGER NOT NULL,
            acres NUMERIC(4,2) NOT NULL,
            geog GEOGRAPHY NOT NULL,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            insert_date TIMESTAMPTZ NOT NULL,
            zip_code CHAR(5) NOT NULL,
            price_per_acre INTEGER NOT NULL,
            url TEXT NOT NULL,
            FOREIGN KEY (zip_code)
                REFERENCES zip_codes (zip_code)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS noaa_weather_stations (
            station_id VARCHAR(50) PRIMARY KEY,
            elevation DECIMAL,
            min_date DATE,
            max_date DATE,
            name TEXT,
            data_coverage DECIMAL,
            elevation_unit TEXT,
            geog GEOGRAPHY NOT NULL,
            latitude DOUBLE PRECISION NOT NULL,
            longitude DOUBLE PRECISION NOT NULL,
            state_name TEXT NOT NULL,
            state_fips_id CHAR(7) NOT NULL,
            FOREIGN KEY (state_name)
                REFERENCES states (state_name)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS noaa_monthly_averages (
            station_id VARCHAR(50),
            month INTEGER,
            year INTEGER,
            data_type CHAR(4),
            value DECIMAL,
            PRIMARY KEY (station_id, month, year, data_type),
            FOREIGN KEY (station_id)
                REFERENCES noaa_weather_stations (station_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        # read the connection parameters
        params = db_config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            logging.info(f'Executing command: {command}')
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        sys.exit(error)
    finally:
        if conn is not None:
            conn.close()

def get_db_cursor():
   """ Connect to the PostgreSQL database server and insert zip code info """
   try:
      # read connection parameters
      params = db_config()

      # connect to the PostgreSQL server
      global db_connection
      db_connection = psycopg2.connect(**params)
      return db_connection.cursor()

   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(error);
      sys.exit(error)

def query_db(db_cursor, insert_cmd, columns, values):
   try:
      db_cursor.execute(insert_cmd, (AsIs(','.join(columns)), tuple(values)))
      db_connection.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      logging.error(f'Insert Command: {insert_cmd}')
      logging.error(f'Insert Command Values: {values}')
      sys.exit(error)

def main():
    create_tables()
    
if __name__ =='__main__':
    log_config('db_config')
    main()
