
# SchoolBus.py
#
# To run this program, you must save the file Gui.py
# in the same folder as this program.
#
# CSC 110
# Sp'11

# Required import statement for Gui tools
import Gui

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section
def draw_window(wx1, wy1, size):
    # draw trunk
    wx2 = wx1 + size
    wy2 = wy1 + size
    facex = wx1 + 0.3 * size
    facey = wy1 + 0.3 * size
    eyex = wx1 + 0.4 * size
    eyey = wy1 + 0.4 * size
    mouthx1 = eyex
    mouthx2 = mouthx1 + 0.2 * size
    mouthy = wy1 + 0.2 * size
    # draw window frame
    canvas.rectangle([[wx1,wy1], [wx2,wy2]], fill='white')
    # draw face
    canvas.circle([facex,facey], 0.3 * size, fill='brown', width=0)
    canvas.circle([eyex,eyey], 0.05 * size, fill='black')
    canvas.line([[mouthx1,mouthy], [mouthx2,mouthy]])

def draw_schoolbus(x, y, length, door_color):
    # draw wheels first
    canvas.circle([x+0.2*length,y], 0.1*length, 'black')
    canvas.circle([x+0.8*length,y], 0.1*length, 'black')
    # draw bus chassis
    canvas.rectangle([[x,y], [x+length,y+0.5*length]], fill='yellow')
    # draw windows
    wax = x + 0.1 * length
    wbx = x + 0.4 * length
    wy = y + 0.2 * length
    wsize = 0.2 * length
    draw_window(wax, wy, wsize)
    draw_window(wbx, wy, wsize)
    # draw door
    dx1 = x + 0.8 * length
    dx2 = x + 0.95 * length
    dy2 = y + 0.3 * length
    canvas.rectangle([[dx1,y], [dx2,dy2]], fill=door_color)

def draw_bus_cluster(x, y, size, door_color):
    draw_schoolbus(x, y, size, door_color)
    draw_schoolbus(x + 1.2 * size, y, size, door_color)
    draw_schoolbus(x + 2.4 * size, y, size, door_color)

def main():
    # draw things on the canvas
    draw_window(50, 120, 100)
    draw_schoolbus(-180, -200, 400, 'red')
    draw_schoolbus(-280, 40, 120, 'green')
    draw_schoolbus(-120, 40, 120, 'orange')

    draw_bus_cluster(-330, 140, 80, 'pink')
    draw_bus_cluster(-270, 190, 60, 'blue')
#    draw_schoolbus(-330, 140, 80, 'gray')
#    draw_schoolbus(-220, 140, 80, 'blue')
#    draw_schoolbus(-110, 140, 80, 'pink')

#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui.Gui()
win.title('Riding the bus to school...')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html

