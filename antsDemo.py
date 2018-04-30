#James Roth
#4/30/18
#antsDemo.py - graphics and lists

from ggame import *

ANTS=10

if __name__ == "main":
    red=Color(0xff0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)
    Sprite(ant)
    
    App().run()
