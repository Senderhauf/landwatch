#!/bin/sh

# remove all log files older than 2 days old
find /usr/src/app/log/*.log -mtime +2 -exec rm {} \;

# create database tables
python3 -m config.db_config

if [ "$INITIALIZE_STATES" = true ]
then
    # initialize states data
    python3 -m demographics.populate_states_db
fi

if [ "$INITIALIZE_ZIP_CODE" = true ]
then
    # initialize zip code data
    python3 -m demographics.populate_zip_code_db
fi

if [ "$INITIALIZE_WEATHER" = true ]
then
    # initialize weather data
    python3 -m noaa_weather.populate_noaa_weather_db
    
    # link zip codes to nearest weather station
    python3 -m noaa_weather.populate_zip_code_weather_station_db
fi

if [ "$INITIALIZE_LISTINGS" = true ]
then
    # scrape landandfarm listings
    python3 -m listings.landandfarm_listings
fi
