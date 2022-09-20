# CSCI 1100 Gateway to Computer Science
#
# Bob Muller
#
# The simplest example, a circle moving along the diagonal, 
# pausing on Touch.Up.

from animate import *

# draw : model -> image
def draw(model):
    (paused, x, y) = model
    backing = Image.rectangle(800, 800, Color.White)
    circle  = Image.circle(200, Color.Orange)
    return Image.placeImage(circle, (x, y), backing)

# finished : model -> boolean
def finished(model):
    (paused, x, y) = model
    return x > 600

# onTick : model -> model
def onTick(model):
    (paused, x, y) = model
    return model if paused else (paused, x + 5, y + 5)

# handleTouch: model * xy * event -> model
def handleTouch(model, xy, event):
    (paused, x, y) = model
    return (not(paused), x, y) if event == Touch.Up else model

def go():
    Animate.start(
        model=(True, 0, 0),
        view=draw,
        viewLast=draw,
        tickUpdate=onTick,
        touchUpdate=handleTouch,
        stopWhen=finished)

go()
