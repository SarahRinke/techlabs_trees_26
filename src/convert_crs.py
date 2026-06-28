# 1. function unify_crs():
#    converts crs of tree data to the same of the aerial data.
# 
# input: 
#        - tiles: output of load_tile_local()
#.       - trees: output of load_trees_local() 
#
# output: 
#        - trees: with modified epsg 
#
#
# 2. function trees_geo_to_pixel():
#    converts geo data of trees to pixel data relative to one
#    specific tile. Adds pixel values to gpd dataframe trees 
# 
# input: 
#        - tiles: output of load_tile_local()
#.       - trees: output of unify_crs() 
#
# output: 
#        - trees: with list 'pixels' added to gpd dataframe 
#                 additionally, pixel_x and _y are added 
#                  separately


# # # # # # convert crs of trees to aerial data  # # # # # # # 
# #                                                        # #
#                                                            #

def unify_crs(tiles, trees):

    # get crs of tiles
    for tile in tiles:
        tiledata = tile["data"]
        tile_crs = tiledata.crs
    
    # get crs of trees
    tree_crs = trees.crs.to_epsg()
    
    # unify if not the same already
    if tree_crs != tile_crs:
        trees = trees.to_crs(tile_crs)
    
    # return
    return trees
    
#                                                            #
# #                                                        # #
# # # # # end convert crs of trees to aerial data  # # # # # #





# # # # # # convert geodata of trees to pixel  # # # # # # # # 
# #                                                        # #
#                                                            #

def trees_geo_to_pixel(tiles, trees, target_tile):

    from rasterio.transform import rowcol

    pixels = []
    tile   = tiles[target_tile]["data"]

    for point in trees.geometry:

        row, col = rowcol(
            tile.transform,
            point.x,
            point.y
        )

        pixels.append(
            (col, row)
        )
        
    trees['pixels'] = pixels;
    
    trees["pixel_x"] = trees["pixels"].apply(lambda p: p[0])
    trees["pixel_y"] = trees["pixels"].apply(lambda p: p[1])
    
    return trees
    
#                                                            #
# #                                                        # #
# # # # # end convert crs of trees to aerial data  # # # # # # 