# CSCI 1100 Gateway to Computer Science
#
# Bob Muller
#
# The simplest example, a circle moving left to right.
from animate import *

# draw : model -> image
def draw(x):
    backing = Image.rectangle(800, 800, Color.White)
    circle  = Image.circle(200, Color.Orange)
    return Image.placeImage(circle, (x, 200), backing)

# finished : model -> boolean
def finished(x):
    return x > 600

# onTick : model -> model
def onTick(x):
    return x + 5

def go():
    Animate.start(
        model=0,
        view=draw,
        viewLast=draw,
        tickUpdate=onTick,
        stopWhen=finished)

go()

