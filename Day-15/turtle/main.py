from turtle import Turtle, Screen

# Docs at docs.python.org/3/library/turtle.html
# Constructed an object

shiro = Turtle()
# Screen represents the window where the turtle shows up.
shiro.shape("turtle")
shiro.color("blue")
my_screen = Screen()
shiro.forward(100)
shiro.left(100)
shiro.left(100)
shiro.backward(100)
shiro.right(100)
shiro.backward(100)
shiro.backward(100)
#print(my_screen.canvheight)
my_screen.exitonclick()
