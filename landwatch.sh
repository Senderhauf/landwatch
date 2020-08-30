#!/bin/sh

# create database tables
python3 -m db_config.db_config

# initialize states data
python3 -m demographics.populate_states_db

# initialize zip code data
python3 -m demographics.populate_zip_code_db

# initialize weather data
# python3 -m noaa_weather.populate_noaa_weather_db

# scrape landandfarm listings
# python3 -m scrape_landandfarm.scrape_landandfarm