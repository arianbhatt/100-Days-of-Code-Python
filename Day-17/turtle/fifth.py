# Creating a random walk
from turtle import Turtle, Screen
import random
shiro=Turtle()
shiro.shape("turtle")
colours=["CornflowerBlue",'DarkOrchid',"IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
shiro.pensize(10)
shiro.speed("fastest") # to make a fast 
for i in range(200):
    shiro.color(random.choice(colours))
    shiro.forward(30)
    shiro.setheading(random.choice(directions))


screen=Screen() # so it stays
screen.exitonclick() # stays until we click on exit

