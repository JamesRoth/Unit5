#James Roth
#4/23/18
#betterColoredWindow.py - function that changes a window's color

from random import randint
from ggame import *

outline=LineStyle(1,Color(0x00ffff, 1))

colors=[0x00ff00,0xff0000,0x0000ff,0x00ffff,0xff00ff,0xffffff]

def mouseClick(event):
    color=colors[0:randint(len(colors)-1)]
    
    rectangle=RectangleAsset(1000, 2000, outline, color)
    Sprite(rectangle)

App().listenMouseEvent("click", mouseClick)
App().run()

