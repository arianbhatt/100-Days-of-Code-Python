from turtle import Turtle, Screen
shiro=Turtle()
shiro.shape("turtle")
shiro.color("red")
# Creating a Square
for i in range(4):
    shiro.forward(100)
    shiro.right(90)

screen=Screen() # so it stays
screen.exitonclick() # stays until we click on exit

