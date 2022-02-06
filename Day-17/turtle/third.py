# Creating a dashed line
from turtle import Turtle, Screen
shiro=Turtle()
shiro.shape("turtle")
shiro.color("red")
for i in range(15):
    shiro.forward(10)
    shiro.penup()
    shiro.forward(10)
    shiro.pendown()

screen=Screen() # so it stays
screen.exitonclick() # stays until we click on exit

