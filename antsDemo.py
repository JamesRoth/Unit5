#James Roth
#4/30/18
#antsDemo.py - graphics and lists

from ggame import *
from random import randint

ANTS=10
WIDTH=800
HEIGHT=500

if __name__ == "__main__":
    
    data={}
    data["antlist"]=[]
    
    red=Color(0xff0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)
    
    for i in range(ANTS):
        data["antlist"],append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run()
