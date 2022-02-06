# Creating a random walk with a random color everytime

import turtle as t
import random
shiro=t.Turtle()
shiro.shape("turtle")
colours=["CornflowerBlue",'DarkOrchid',"IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
shiro.pensize(10)

t.colormode(255) # Changing the color mode

shiro.speed("fastest") # to make a fast 
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

for i in range(200):
    shiro.color(random_color())
    shiro.forward(30)
    shiro.setheading(random.choice(directions))


screen=t.Screen() # so it stays
screen.exitonclick() # stays until we click on exit

