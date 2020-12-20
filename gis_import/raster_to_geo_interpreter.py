from gis_import.plot_counties_whp import get_reproj_raster, get_geodataframe
import geopandas as gpd
import geopy as gpy
import random
import numpy as np
import itertools
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

# Absolute path location of Esri GRID file. Directory contains multiple '.adf' resources.
RASTER_FILE = '//home/enigmaticmustard/projects/landwatch/data/whp_2018_classified/whp2018_cls'
RASTER_REPROJ_FILE = '/tmp/reproj.tif'
SHAPE_FILE = 'zip:///home/enigmaticmustard/projects/landwatch/data/census_boundaries_2019/zip_code_tabulation_areas.zip'

rstr_dataset = get_reproj_raster()
zip_codes = get_geodataframe()
zip_code_95444 = zip_codes.loc[zip_codes['ZCTA5CE10'] == '95444']
zip_code_95444_coords = list(zip(*zip_code_95444.geometry.iloc[0].exterior.coords.xy))
zip_min_long_lat = tuple(map(min, zip(*zip_code_95444_coords)))
zip_max_long_lat = tuple(map(max, zip(*zip_code_95444_coords)))

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
print(
f'min_long_lat:\n{min_long_lat}\n\n'
f'max_long_lat:\n{max_long_lat}\n\n'
f'raster_max_row_col:\n{raster_max_row_col}\n\n'
f'raster_min_row_col:\n{raster_min_row_col}\n\n'
f'row_list:\n{row_list}\n\n'
f'col_list:\n{col_list}\n\n'
f'raster_row_col_in_bb:\n{raster_row_col_in_bb}\n\n'
f'raster_pts_in_bb:\n{raster_pts_in_bb}\n\n'
)
return raster_pts_in_bb

def lat_long_in_poly(lat, long, poly):
print(f'lat: {lat}, long: {long}\n')
pnt = Point(lat, long)
return pnt.within(poly)

# get list of raster coordinates within the zip code's bounding box
raster_lat_long_in_bb = get_lat_long_list_in_bb(rstr_dataset, zip_min_long_lat, zip_max_long_lat)

# filter list of raster coordinates within zip code's bouding box for coordinates within the geometry of the zip code
raster_lat_long_in_bb = [lat_long for lat_long in raster_lat_long_in_bb if lat_long_in_poly(*lat_long[::-1], zip_code_95444.geometry.iloc[0])]

# get values for each point
raster_point_value_list = [(lat_long, rstr_dataset.sample([lat_long])) for lat_long in raster_lat_long_in_bb]
print(f'raster_point_value_list:\n{raster_point_value_list}\n\n')
