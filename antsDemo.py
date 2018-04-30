#James Roth
#4/30/18
#antsDemo.py - graphics and lists

from ggame import *
from random import randint

ANTS=10
WIDTH=800
HEIGHT=500

if __name__ == "__main__":
    red=Color(0xff0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)
    for i in range(ANTS):
        Sprite(ant)
    
    App().run()
