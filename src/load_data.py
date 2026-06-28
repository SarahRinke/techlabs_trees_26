# 1. function load_tile_local():
#    loads n tiles of the aerial data from your local computer.
# 
# input: 
#        - data_path: a pathlib.PoxisPath  
#          Either complete path or relative (e.g.: "../DATA/tile1.tif")
#.       - ntiles: number of tiles you want to load
#
# output: 
#        - tile: dicitionary datatype 
#
#
# 2. function load_trees_local():
#    loads n tiles of the aerial data from your local computer.
# 
# input: 
#        - data_path: a pathlib.PoxisPath  
#          Either complete path or relative (e.g.: "../DATA/tile1.tif")
#
#
# output: 
#        - trees: a geopandas dataframe 



# # # # # # # # # load data of tiles # # # # # # # # # # # # #
# #                                                        # #
#                                                            #

def load_tile_local(data_path, ntiles):

    # import rasterio
    import os
    import rasterio

    # get a list of all files of the requested format. 
    # Put them in a list called tilenames
    filenames = os.listdir(data_path)

    tilenames = [
        data_path / filename
        for filename in filenames
        if filename.endswith(".tif")
    ]


    # open ntiles tiles
    tiles = []

    for tilename in tilenames[0:ntiles]:
        data = rasterio.open(tilename)
        tiles.append({
            "name": tilename.name,
            "data": data
        })

    return tiles
    
#                                                            #
# #                                                        # #
# # # # # # # # # end load data of tiles # # # # # # # # # # #






# # # # # # # # # load data of trees # # # # # # # # # # # # #
# #                                                        # #
#                                                            #

def load_trees_local(data_path):

    # import os, geopandas
    import os
    import geopandas as gpd

    # get a list of all files in the folder. 
    # Select corresponding file based on file extension
    filenames = os.listdir(data_path)
    tree_file = [
        data_path / filename
        for filename in filenames
        if filename.endswith("opendata.geojson")
    ];
    
    tree_file = tree_file[0]
                        
    # open geojson file using geopandas
    trees = gpd.read_file(tree_file)

    return trees
    
#                                                            #
# #                                                        # #
# # # # # # # # # end load data of trees # # # # # # # # # # #