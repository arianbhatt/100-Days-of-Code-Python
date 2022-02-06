# Creating a Spirograph

import turtle as t
import random
shiro=t.Turtle()
shiro.shape("turtle")
colours=["CornflowerBlue",'DarkOrchid',"IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
#shiro.pensize(10)

t.colormode(255) # Changing the color mode

shiro.speed("fastest") # to make a fast 
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        shiro.color(random_color())
        shiro.circle(100)
        shiro.setheading(shiro.heading()+size_of_gap)
        # shiro.setheading(random.randint(0,360))

draw_spirograph(5)
screen=t.Screen() # so it stays
screen.exitonclick() # stays until we click on exit

