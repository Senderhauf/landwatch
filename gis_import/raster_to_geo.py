from gis_import.plot_counties_whp import get_reproj_raster, get_geodataframe
import pandas as pd
import geopandas as gpd
import geopy as gpy
import random
import numpy as np
import itertools
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

# Absolute path location of Esri GRID file. Directory contains multiple '.adf' resources.
RASTER_FILE = '//home/enigmaticmustard/projects/landwatch/data/whp_2018_classified/whp2018_cls'
SHAPE_FILE = 'zip:///home/enigmaticmustard/projects/landwatch/data/census_boundaries_2019/counties.zip'
RASTER_REPROJ_FILE = '/tmp/reproj.tif'

def get_lat_long_list_in_bb(raster, min_long_lat, max_long_lat):
    # get nearest raster pixel point to max and min coords of bounding box
    # rasterio.io.DatasetReader.index(long, lat) returns (row, col)
    # rasterio.io.DatasetReader.xy() returns (long, lat)
    # any reference to 'min' in a variable denotes the BOTTOM RIGHT of a bounding box
    # any reference to 'max' in a variable denotes the TOP LEFT of a bounding box
    raster_max_row_col = raster.index(*max_long_lat)
    raster_min_row_col = raster.index(*min_long_lat)
    row_list = [row for row in range(raster_max_row_col[0], raster_min_row_col[0])]
    col_list = [col for col in range(raster_min_row_col[1], raster_max_row_col[1])]
    raster_row_col_in_bb = list(itertools.product(row_list, col_list))
    raster_pts_in_bb = [raster.xy(*row_col)[::-1] for row_col in raster_row_col_in_bb]
    # print(
    # f'min_long_lat:\n{min_long_lat}\n\n'
    # f'max_long_lat:\n{max_long_lat}\n\n'
    # f'raster_max_row_col:\n{raster_max_row_col}\n\n'
    # f'raster_min_row_col:\n{raster_min_row_col}\n\n'
    # f'row_list:\n{row_list}\n\n'
    # f'col_list:\n{col_list}\n\n'
    # f'raster_row_col_in_bb:\n{raster_row_col_in_bb}\n\n'
    # f'raster_pts_in_bb:\n{raster_pts_in_bb}\n\n'
    # )
    return raster_pts_in_bb

def lat_long_in_poly(lat, long, poly):
    # print(f'lat: {lat}, long: {long}\n')
    pnt = Point(lat, long)
    return pnt.within(poly)

def get_point_val_raster_gdf_intersect(rstr_dataset, geodataframe):
    geodataframe_coords = list(zip(*geodataframe.geometry.iloc[0].exterior.coords.xy))
    min_long_lat = tuple(map(min, zip(*geodataframe_coords)))
    max_long_lat = tuple(map(max, zip(*geodataframe_coords)))

    # get list of raster coordinates within the geodataframe's bounding box
    raster_lat_long_in_bb = get_lat_long_list_in_bb(rstr_dataset, min_long_lat, max_long_lat)

    # filter list of raster coordinates within geodataframe's bounding box for coordinates within the geometry of the geodataframe
    raster_lat_long_in_geom = [lat_long for lat_long in raster_lat_long_in_bb if lat_long_in_poly(*lat_long[::-1], geodataframe.geometry.iloc[0])]

    # get values for each point
    raster_point_value_list = [(lat_long, next(rstr_dataset.sample([lat_long[::-1]]))[0]) for lat_long in raster_lat_long_in_geom]
    # print(f'raster_point_value_list:\n{raster_point_value_list}\n\n')
    return raster_point_value_list

def get_pnt_val_to_gdf(pnt_val_list):
    # convert (point,value) list data to pandas dataframe
    df = pd.DataFrame({
        'Value': [val for point,val in pnt_val_list],
        'Latitude': [point[0] for point,val in pnt_val_list],
        'Longitude': [point[1] for point,val in pnt_val_list]})

    # convert pandas dataframe to geopandas dataframe
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    return gdf

# TODO
def get_avg_in_gdf(gdf, field, ignore_val=[]):
    cnt = 0
    total = sum([gdf])

def main():
    rstr_dataset = get_reproj_raster(RASTER_FILE, SHAPE_FILE)
    shp_gdf = get_geodataframe(SHAPE_FILE)
    # use only shasta county for now
    shp_gdf = shp_gdf.loc[shp_gdf['NAME'] == 'Tooele']
    raster_pnt_val_in_geom = get_point_val_raster_gdf_intersect(rstr_dataset, shp_gdf)
    raster_gdf = get_pnt_val_to_gdf(raster_pnt_val_in_geom)
    return raster_gdf

if __name__ == '__main__':
    main()

'''
Legend:
    1 = very low    (0-44 percentile)
    2 = low         (45-67 percentile)
    3 = moderate    (68-84 percentile)
    4 = high        (85-96 percentile)
    5 = very high   (96+ percentile)
    6 = non-burnable
    7 = water
'''