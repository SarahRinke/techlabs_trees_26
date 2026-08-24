# 1. function tree_selection():
#    selects those trees that are within one tile.
#    Selection is based on pixel coordinates
# 
# input: 
#.       - trees: output of trees_geo_to_pixel() 
#
# output: 
#        - trees_within_tile: a gpd that contains all trees that
#                             are located in tiles[0]
#

# 2. function remove_non_trees():
#    removes entries that Heidi identified as non-trees
# 
# input: 
#.       - file_path: path to gpkg file of Heidi 
#.       - trees: output of unify_crs() or load_trees_local() 
#
# output: 
#        - trees: less entries
#




# # # # # # select trees that are within a tile  # # # # # # #
# #                                                        # #
#                                                            #

def tree_selection(tiles, trees,target_tile):

    tile = tiles[target_tile]["data"]
    max_pix_x = tile.width
    max_pix_y = tile.height

    logical_index = (
        (trees["pixel_x"] >= 0) &
        (trees["pixel_y"] >= 0) &
        (trees["pixel_x"] < max_pix_x) &
        (trees["pixel_y"] < max_pix_y)
    )

    trees_within_tile = trees[logical_index]
    
    
    return trees_within_tile
    
#                                                            #
# #                                                        # #
# # # # # end tree selection # # # # # # # # # # # # # # # # # 




# # # # # # remove non-tree entries  # # # # # # # # # # # # # 
# #                                                        # #
#                                                            #

def remove_non_trees(file_path, trees):

    import geopandas as gpd
    trees_filtered = gpd.read_file(file_path)

    assert len(trees) == len(trees_filtered) # check that 
                                             # same files 
    
    trees["isTrue"] = trees_filtered["is_True"]
    trees = trees[trees["isTrue"] == 1]
    
    return trees
    
#                                                            #
# #                                                        # #
# # # # # end non_trees  # # # # # # # # # # # # # # # # # # # 