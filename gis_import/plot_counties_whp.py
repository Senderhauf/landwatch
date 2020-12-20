import numpy as np
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import geopandas
from distutils.version import LooseVersion
import numpy as np
import geopandas
import matplotlib.pyplot as plt
import rasterio.plot as rio_plt

# Absolute path location of Esri GRID file. Directory contains multiple '.adf' resources.
RASTER_FILE = '//home/enigmaticmustard/projects/landwatch/data/whp_2018_classified/whp2018_cls'
RASTER_REPROJ_FILE = '/tmp/reproj.tif'
SHAPE_FILE = 'zip:///home/enigmaticmustard/projects/landwatch/data/census_boundaries_2019/zip_code_tabulation_areas.zip'

def reproject_raster_from_shp_crs(rstr_file=RASTER_FILE, shp_file=SHAPE_FILE, rstr_rprj_file=RASTER_REPROJ_FILE):
    '''
    Reproject raster to shapefile's coordinate reference system and save in .tif file. 

    Parameters:
        rstr_file (str): Absolute path to raster resources for creating rasterio.io.DatasetReader.
        shp_file (str): Absolute path to shapefile resources for creating geopandas.GeoDataFrame.
        rstr_rprj_file (str): Absolute path to save reprojected raster .tif file. 

    Returns:
        None   
    '''
    gdf = geopandas.read_file(shp_file)
    if LooseVersion(rasterio.__gdal_version__) >= LooseVersion("3.0.0"):
        dst_crs = rasterio.crs.CRS.from_wkt(gdf.crs.to_wkt())
    else:
        dst_crs = rasterio.crs.CRS.from_wkt(gdf.crs.to_wkt("WKT1_GDAL"))

    with rasterio.open(rstr_file) as src:
        transform, width, height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': dst_crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        destination = np.zeros(src.shape, np.uint8)

        with rasterio.open(
            RASTER_REPROJ_FILE,
            'w',
            driver='GTiff',
            height=destination.shape[0],
            width=destination.shape[1],
            count=1,
            dtype=destination.dtype,
            crs='+proj=latlong',
            transform=transform,
        ) as dst:
            # dst.write(destination, 1)

            reproject(
                source=rasterio.band(src, 1),
                destination=rasterio.band(dst, 1),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)

def get_reproj_raster(rstr_file=RASTER_FILE, shp_file=SHAPE_FILE, rstr_rprj_file=RASTER_REPROJ_FILE):
    '''
    Return rasterio.io.DatasetReader of reprojected raster to shapefile's coordinate reference system. 

    Parameters:
        rstr_file (str): Absolute path to raster resources for creating rasterio.io.DatasetReader.
        shp_file (str): Absolute path to shapefile resources for creating geopandas.GeoDataFrame.
        rstr_rprj_file (str): Absolute path to save reprojected raster .tif file. 

    Returns:
        (rasterio.io.DatasetReader): Dataset for reprojected raster
    '''
    reproject_raster_from_shp_crs(rstr_file, shp_file, rstr_rprj_file)
    return rasterio.open(rstr_rprj_file)

def get_geodataframe(shp_file=SHAPE_FILE):
    '''
    Parameters:
        shp_file (str): Absolute path to shapefile resources for creating geopandas.GeoDataFrame.
    
    Returns:
        (geopandas.GeoDataFrame): GeoDataFrame for specified shapefile.
    '''
    return geopandas.read_file(shp_file)

def get_datasets():
    '''Return tuple(geopandas.GeoDataFrame, rasterio.io.DatasetReader) for default shapefile and raster resources'''
    return (geopandas.read_file(shp_file), get_reproj_raster())

def plot_superimpose(rstr_file=RASTER_FILE, shp_file=SHAPE_FILE):
    gdf = geopandas.read_file(shp_file)
    raster = rasterio.open(rstr_file)

    fig, ax = plt.subplots(figsize=(15, 15))
    rasterio.plot.show(raster, ax=ax)
    gdf.plot(ax=ax, facecolor='none', edgecolor='black')
    # plt.savefig('/home/enigmaticmustard/projects/landwatch/data/graphs/counties.png')
    plt.show()

# TODO
def get_values_raster(rstr_dataset):
    x_range = int(abs(rstr_dataset.bounds.left) + abs(rstr_dataset.bounds.right))
    y_range = int(abs(rstr_dataset.bounds.bottom) + abs(rstr_dataset.bounds.top))

    for i in range(x_range):
        for j in range(y_range):
            rstr_dataset.sample([(i, j)])

# TODO
def add_raster_to_geopandas():
    '''
    for bonding box in zip codes:
        get all pixels
        get all values for pixels
        get avg of all vals   
    '''
    
    dataset = rasterio.open(RASTER_REPROJ_FILE)

    # Extract feature shape`s and values from the array.
    for geom, val in rasterio.features.shapes(dataset.dataset_mask(), transform=dataset.transform):

        # Print GeoJSON shapes to stdout.
        print(geom)

if __name__ == '__main__':
    # reproject_raster_from_shp_crs(raster_file, shp_file)
    plot_superimpose(RASTER_REPROJ_FILE, SHAPE_FILE)