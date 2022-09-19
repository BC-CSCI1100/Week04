# CSCI 1100 Gateway to Computer Science
#
# Bob Muller
#
# The simplest example, a stationary circle.

from animate import *

def draw(ignored):
    backing = Image.rectangle(800, 800, Color.White)
    circle  = Image.circle(200, Color.Orange)
    return Image.placeImage(circle, (0, 200), backing)

def finished(ignored):
    return False

def go():
    Animate.start(
        view=draw,
        stopWhen=finished)

go()

