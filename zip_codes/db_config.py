#!/usr/bin/env python3
import psycopg2
from configparser import ConfigParser
import sys

def config(filename='./db_config/database.ini', section='postgresql'):
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

def createTables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE EXTENSION IF NOT EXISTS postgis;
        """,
        """
        CREATE TABLE IF NOT EXISTS states (
            state_abrev CHAR(2) PRIMARY KEY,
            state_name VARCHAR(25) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS zip_codes (
            zip_code CHAR(5) PRIMARY KEY,
            primary_city VARCHAR(50),
            county VARCHAR(50),
            type VARCHAR(8) NOT NULL,
            decommissioned BOOLEAN,
            acceptable_cities TEXT[],
            unacceptable_cities TEXT[],
            state_abrev VARCHAR(2),
            timezone VARCHAR(50),
            area_codes TEXT[],
            county VARCHAR(50),
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
            area_land INTEGER,
            area_water INTEGER,
            FOREIGN KEY (state_abrev)
                REFERENCES states (state_abrev)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IS NOT EXISTS zip_demographics (
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
        CREATE TABLE IF NOT EXISTS population_history (
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
            url VARCHAR(275) NOT NULL,
            FOREIGN KEY (zip_code)
                REFERENCES zip_codes (zip_code)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        sys.exit(error)
    finally:
        if conn is not None:
            conn.close()
