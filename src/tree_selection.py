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