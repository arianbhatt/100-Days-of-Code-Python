# Creating lot of shapes 3 to 10
from turtle import Turtle, Screen
shiro=Turtle()
shiro.shape("turtle")
shiro.color("red")
for i in range(3,11):
    turn=360//i
    for j in range(i):
        shiro.forward(100)
        shiro.right(turn)

screen=Screen() # so it stays
screen.exitonclick() # stays until we click on exit

