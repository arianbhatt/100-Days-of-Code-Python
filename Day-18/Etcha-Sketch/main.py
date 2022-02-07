from turtle import Turtle, Screen

shiro= Turtle()
screen=Screen()

# TO listen to the keystrokes by the user we use the .onkey(fun,key) function. takes a key and function
def move_forward():
    shiro.forward(10)
def move_backward():
    shiro.backward(10)
def move_right():
    shiro.right(10)
def move_left():
    shiro.left(10)
def clear():
    shiro.clear()
    shiro.penup()
    shiro.home()
    shiro.penup()


# Starts Listening
screen.listen() 
screen.onkey(move_forward,"w")

# when passing fuction to function we don't use ()
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")

# Higher Order Function: Function which can work with other function.
screen.exitonclick()
