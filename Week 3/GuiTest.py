
# GuiTest.py
# This sample program demonstrates drawing shapes
# on a canvas using some Gui tools.
#
# This program is not interactive.  It draws the same
# picture every time it is executed.
#
# To run this program, you must save the file Gui.py
# in the same folder as this program.
#
# You can use this sample as starter code for drawing-related
# lab exercises and homework assignments.  Just save a copy of
# the file with a new name, add your own function definitions,
# and change the code in the 'main' function.
#
# Pay careful attention to the use of [] to specify points
# and lists of points.  We'll talk more about this later...
#
# CSC 110
# Sp'11

# Required import statement for Gui tools
import Gui

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section -- add your function definitions here
def main():
    # draw things on the canvas
    canvas.circle([0,0], 25, 'blue')
    canvas.rectangle([[0,0],[50, 50]], fill='green', outline='red')
    canvas.polygon([[-50, -50], [50, -50], [-50, 50]], outline='cyan', width=3)
    canvas.line([[25, 62], [75, 42]], width=4)
    canvas.line([[-65, 40], [-55, 20], [-65, 0], [-55, -20], [-65, -40]], \
                fill='magenta', width=2)
    canvas.oval([[-50, -55], [50, -75]], fill='gray', width=0)

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

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html

