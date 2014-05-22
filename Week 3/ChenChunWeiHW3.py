# ChenChunWeiHW3.py

# Drawing a scene

# This program demonstrates drawing a scene om a canvas by using Gui tools.

# Chun-Wei Chen
# CSC 110.03
# Spring 2011/04/25

# Import statement for Gui tools
import Gui

# Named Constants
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section
def draw_tree(base_x, base_y, height):
    # draw trunk
    truck_x1 = base_x - height * 0.05
    truck_x2 = base_x + height * 0.05
    truck_y1 = base_y
    truck_y2 = base_y + height / 3.0
    canvas.rectangle([[truck_x1, truck_y1], [truck_x2, truck_y2]], \
                     fill = 'brown', width = 0)
    # draw leaves(the crown)
    # the polygon consists of three points, peak, lower left, and lower right
    # I use three polygons to make leaves(the crown)
    leaf_x1 = base_x - height * 0.15
    leaf_x2 = base_x + height * 0.15
    leaf_y1 = base_y + height * 0.25
    leaf_y2 = base_y + height * 0.55
    leaf_x3 = base_x - height * 0.15
    leaf_x4 = base_x + height * 0.15
    leaf_y3 = base_y + height * 0.5
    leaf_y4 = base_y + height * 0.8
    leaf_x5 = base_x - height * 0.15
    leaf_x6 = base_x + height * 0.15
    leaf_y5 = base_y + height * 0.75
    leaf_y6 = base_y + height
    canvas.polygon([[leaf_x1, leaf_y1], [leaf_x2, leaf_y1], \
                    [base_x, leaf_y2]], fill = 'darkgreen', width = 0)
    canvas.polygon([[leaf_x3, leaf_y3], [leaf_x4, leaf_y3], \
                    [base_x, leaf_y4]], fill = 'darkgreen', width = 0)
    canvas.polygon([[leaf_x5, leaf_y5], [leaf_x6, leaf_y5], \
                    [base_x, leaf_y6]], fill = 'darkgreen', width = 0)

def draw_tree_cluster(x, y, size):
    # combine three trees in a definition
    draw_tree(x, y, size * 0.5)
    draw_tree(x - size * 0.15, y - size * 0.4, size * 0.75)
    draw_tree(x + size * 0.15, y - size * 0.4, size * 0.75)
    
def draw_snowman(body_x, body_y, radius):
    # draw snowman's hands
    hand_x1 = body_x
    hand_x2 = body_x - radius
    hand_x3 = body_x + radius
    hand_y1 = body_y
    hand_y2 = body_y + radius
    canvas.line([[hand_x1, hand_y1], [hand_x2, hand_y2]], fill = 'brown', \
                width = 2)
    canvas.line([[hand_x1, hand_y1], [hand_x3, hand_y2]], fill = 'brown', \
                width = 2)
    # draw snowman's body
    canvas.circle([body_x, body_y], radius, fill = 'white', width = 0)
    # draw snowman's head
    head_x = body_x
    head_y = body_y + radius * 1.4
    canvas.circle([head_x, head_y], radius * 0.6, fill = 'white', width = 0)
    # draw snowman's eyes
    eye_x1 = body_x - radius * 0.2
    eye_x2 = body_x + radius * 0.2
    eye_y = body_y + radius * 1.6
    canvas.circle([eye_x1, eye_y], radius * 0.1, fill = 'black')
    canvas.circle([eye_x2, eye_y], radius * 0.1, fill = 'black')
    # draw snowman's nose
    nose_x1 = body_x
    nose_x2 = body_x - radius * 0.1
    nose_x3 = body_x + radius * 0.1
    nose_y1 = body_y + radius * 1.4
    nose_y2 = body_y + radius * 1.2
    canvas.polygon([[nose_x1, nose_y1], [nose_x2, nose_y2], \
                    [nose_x3, nose_y2]], fill = 'orange', width = 0)

def draw_snowman_cluster(x, y, size):
    # combine three snowmen in a definition
    draw_snowman(x, y, size * 0.75)
    draw_snowman(x - size, y - size * 0.5, size * 0.5)
    draw_snowman(x + size, y - size * 0.5, size * 0.5)

def draw_house(corner_x1, corner_y1, height):
    # draw the bottom of the house
    corner_x2 = corner_x1 + height * 1.5
    corner_y2 = corner_y1 + height * 1.1
    canvas.rectangle([[corner_x1, corner_y1], [corner_x2, corner_y2]], \
                     fill = 'coral', width = 0)
    # draw chimney
    chimney_x1 = corner_x1 + height * 1.15
    chimney_x2 = corner_x1 + height * 1.3
    chimney_y1 = corner_y1 + height * 1.1
    chimney_y2 = corner_y1 + height * 1.75
    canvas.rectangle([[chimney_x1, chimney_y1], [chimney_x2, chimney_y2]], \
                     fill = 'gray', width = 0)
    # draw roof
    roof_x1 = corner_x1 - height * 0.2
    roof_x2 = corner_x1 + height * 1.7
    roof_x3 = corner_x1 + height * 0.75
    roof_y1 = corner_y1 + height
    roof_y2 = corner_y1 + height * 1.75
    canvas.polygon([[roof_x1, roof_y1], [roof_x2, roof_y1], \
                    [roof_x3, roof_y2]], fill = 'darkred', width = 0)
    # draw door
    door_x1 = corner_x1 + height * 0.65
    door_x2 = corner_x1 + height * 0.85
    door_y1 = corner_y1
    door_y2 = corner_y1 + height * 0.5
    canvas.rectangle([[door_x1, door_y1], [door_x2, door_y2]], fill = 'brown', \
                     width = 0)
    # draw windows
    window_x1 = corner_x1 + height * 0.2
    window_x2 = corner_x1 + height * 0.35
    window_x3 = corner_x1 + height * 0.5
    window_x4 = corner_x1 + height
    window_x5 = corner_x1 + height * 1.15
    window_x6 = corner_x1 + height * 1.3
    window_y1 = corner_y1 + height * 0.5
    window_y2 = corner_y1 + height * 0.8
    canvas.rectangle([[window_x1, window_y1], [window_x2, window_y2]], \
                     fill = 'white')
    canvas.rectangle([[window_x2, window_y1], [window_x3, window_y2]], \
                     fill = 'white')
    canvas.rectangle([[window_x4, window_y1], [window_x5, window_y2]], \
                     fill = 'white')
    canvas.rectangle([[window_x5, window_y1], [window_x6, window_y2]], \
                     fill = 'white')

def main():
    # draw things on the canvas
    draw_tree(-250, 0, 200)
    draw_tree(-50, 0, 200)
    draw_tree_cluster(50, 100, 150)
    draw_house(120, 50, 100)
    draw_snowman(-150, 0, 50)
    draw_tree_cluster(-150, -100, 150)
    draw_tree_cluster(195, -150, 180)
    draw_snowman_cluster(0, -50, 50)
    draw_snowman_cluster(195, 0, 50)
    
#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()
