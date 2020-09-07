#!/usr/bin/env python3
import sys
from random import randrange
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from noaa_weather.noaa_weather_by_zip import get_stations_for_state, get_state_info_list, get_results
import numpy as np

def create_voronoi_for_state(state_name, points):
    vor = Voronoi(points)
    fig = voronoi_plot_2d(vor)
    plt.savefig(f'{state_name}.png')

def main():
    states_list = get_state_info_list()
    lat_long_arr = []
    for state in states_list[45:]:
        dataset_id = 'GHCND'
        start_date = '2019-01-01'
        end_date = '2020-01-01'
        datatypeid_list = ['TMIN', 'TMAX', 'PRCP']
        state_station_list = get_stations_for_state(state['id'], dataset_id, start_date, end_date, datatypeid_list)
        lat_long_arr = lat_long_arr + [[station['longitude'], station['latitude']] for station in state_station_list]
    # create_voronoi_for_state('all_states_voronoi', lat_long_arr)

    lat_long_np_arr = np.array(lat_long_arr)
    plt.scatter(*zip(*lat_long_np_arr))
    plt.savefig('all_stations_scatter.png')


if __name__=='__main__':
    main()