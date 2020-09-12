import os
import matplotlib.pyplot as plt
import geopandas as gpd
# import earthpy as et
# import numpy as np

def intersect_state_drought_monitor(state):
    # drought_monitor_gdf = gpd.read_file('zip:./usdm_20200901/USDM_20200901.shp')
    drought_monitor_gdf = gpd.read_file('zip://./data/drought_monitor/USDM_20200908_M.zip')
    states_us_gdf = gpd.read_file('zip://./data/census_boundaries_2019/states.zip')
    counties_us_gdf = gpd.read_file('zip://./data/census_boundaries_2019/counties.zip')
    fig, ax = plt.subplots(figsize=(12, 8))
    state_gdf = states_us_gdf[states_us_gdf['NAME'] == state]
    dm_reproj_gdf = drought_monitor_gdf.to_crs('epsg:4269')
    intersection_gdf = gpd.overlay(state_gdf, dm_reproj_gdf, how='intersection')
    intersection_gdf = gpd.overlay(intersection_gdf, counties_us_gdf, how='intersection')
    intersection_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax, alpha=.5, edgecolor='black')
    plt.savefig(f'./data/graphs/{state.lower()}_drought_monitor.png')

def main():
    state = 'Colorado'
    intersect_state_drought_monitor(state)

if __name__ == '__main__':
    main()