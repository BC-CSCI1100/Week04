# CSCI 1100 Gateway to Computer Science
#
# Bob Muller
#
# The simplest example, a circle moving along the diagonal.

from animate import *

# draw : model -> image
def draw(model):
    (x, y) = model
    backing = Image.rectangle(800, 800, Color.White)
    circle  = Image.circle(200, Color.Orange)
    return Image.placeImage(circle, (x, y), backing)

# finished : model -> boolean
def finished(model):
    (x, y) = model
    return x > 600

# onTick : model -> model
def onTick(model):
    (x, y) = model
    return (x + 5, y + 5)

def go():
    Animate.start(
        model=(0, 0),
        view=draw,
        viewLast=draw,
        tickUpdate=onTick,
        stopWhen=finished)

go()

