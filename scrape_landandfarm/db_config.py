#!/usr/bin/env python3
import psycopg2
from configparser import ConfigParser
import sys

def config(filename='database.ini', section='postgresql'):
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
        CREATE TABLE IF NOT EXISTS zip_codes (
            zip_code CHAR(5) PRIMARY KEY,
            primary_city VARCHAR(50),
            state CHAR(2) NOT NULL,
            county VARCHAR(20) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS listings (
            listing_id INTEGER PRIMARY KEY,
            price INTEGER NOT NULL,
            acres NUMERIC(4,2) NOT NULL,
            geog GEOGRAPHY NOT NULL UNIQUE,
            insert_date TIMESTAMP NOT NULL,
            zip_code CHAR(5) NOT NULL,
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
