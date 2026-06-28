# 1. function create_boxes():
#    computes boxes (xmin,ymin,xmax, ymax) as well as indices 
#    for those trees with boxes completely within the image
#    Selection is based on pixel coordinates
# 
# input: 
#.       - tiles: output of load_tile_local()
#.       - trees: a geopanda dataframe, output of tree_selection
#            output of trees_geo_to_pixel works too but slower
#.       - target_tile: which of the loaded tiles?
#        - box_width: an integer
#
# output: 
#        - boxes: list with 4 entries per box
#        - valid_indices: which rows of trees are within tile?
#
#
#
#
# 2. function plot_boxes_on_tile():
#    plots boxes on top of the target_tile
# 
# output: 
#        - an image file saved in your current folder
#

# # # # create boxes if box is completely within tile  # # # #
# #                                                        # #
#                                                            #

def create_boxes(tiles, trees,target_tile, box_width):

    tile = tiles[target_tile]["data"]
    img_width  = tile.width
    img_height = tile.height

    half_box  = box_width/2

    
    boxes = []

    valid_indices = []

    for idx, row in trees.iterrows():

        x = row["pixel_x"]
        y = row["pixel_y"]

        xmin = x - half_box
        ymin = y - half_box
        xmax = x + half_box
        ymax = y + half_box


        # complete box within tile image?
        if (
            xmin >= 0 and
            ymin >= 0 and
            xmax < img_width and
            ymax < img_height
        ):

            boxes.append(
                [xmin, ymin, xmax, ymax]
            )

            valid_indices.append(idx)
    
    
    return boxes, valid_indices
    
#                                                            #
# #                                                        # #
# # # # # end box creation # # # # # # # # # # # # # # # # # # 





# # # # # # # # plot boxes on tile # # # # # # # # # # # # # #
# #                                                        # #
#                                                            #

def plot_boxes_on_tile(tiles,
                       target_tile,
                       boxes,
                       output_path):

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np


    # Parameter
    #output_path = "tile_with_boxes_boxwidth120.png"

    box_colors = {
        40: "lime",
        60: "yellow",
        80: "red",
        120: "blue",
        160: "purple"
    }

    line_width = 1


    # load image
    tmp_image = tiles[target_tile]["data"].read()
    tmp_rgb = np.transpose(tmp_image[:3], (1,2,0))


    # create plot
    fig, ax = plt.subplots(figsize=(10,10))

    ax.imshow(tmp_rgb)
    ax.axis("off")


    # draw boxes
    for box in boxes:

        xmin, ymin, xmax, ymax = box

        box_width = xmax - xmin

        color = box_colors.get(
            box_width
        )

        rect = patches.Rectangle(
            (xmin, ymin),
            box_width,
            box_width,
            fill=False,
            linewidth=line_width,
            edgecolor=color
        )

        ax.add_patch(rect)


    # Save
    fig.savefig(
        output_path,
        dpi=1200,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close(fig)

    print(f"saved: {output_path}")
    
#                                                            #
# #                                                        # #
# # # # # end plot boxes # # # # # # # # # # # # # # # # # # # 