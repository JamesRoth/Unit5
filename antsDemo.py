#James Roth
#4/30/18
#antsDemo.py - graphics and lists

from ggame import *
from random import randint

def step(): #moves each ant randomly
    for ant in data["antlist"]:
        ant.x+=randint(-4,3)
        ant.y+=randint(-4,3)

ANTS=50 #constants
WIDTH=800
HEIGHT=500

if __name__ == "__main__":
    
    data={}
    data["antlist"]=[]
    
    red=Color(0xff0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)
    
    for i in range(ANTS): #sprites ants on the screen
        data["antlist"].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
