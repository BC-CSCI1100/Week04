# CSCI 1100 Gateway to Computer Science
#
# Bob Muller
#
# The simplest example, shades of gray.
#
# run: python3 shades.py N

from animate import *
import sys

DISPLAYWIDTH = 800
DISPLAYHEIGHT = DISPLAYWIDTH

# draw : model -> image
def draw(n):
    width = DISPLAYWIDTH // n
    shade = 255 // n
    image = Image.rectangle(DISPLAYWIDTH, DISPLAYHEIGHT, Color.White)
    for i in range(n):
        gray  = i * shade
        color = Color.make(gray, gray, gray)
        x = i * width
        stripe = Image.rectangle(width, DISPLAYHEIGHT, color)
        image  = Image.placeImage(stripe, (x, 0), image)
    return image

# finished : model -> boolean
def finished(model):
    return True

# go : int -> unit
def go(n):
    Animate.start(
        model=n,
        view=draw,
        viewLast=draw,
        stopWhen=finished)

go(int(sys.argv[1]))

