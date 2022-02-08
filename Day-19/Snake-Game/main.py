import time
from snake import Snake
from turtle import Turtle, Screen, color
screen=Screen()
screen.setup(width=600,height=600) # setting window resolution
screen.bgcolor("black") # setting screen bg
screen.title("Snake Xenzia") # Title of the Game window

screen.tracer(0) # closes the animation

starting_position=[(0,0),(-20,0),(-40,0)]

# Creating a snake
snake=Snake()

screen.update() # update the changes
 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1) # 1 second delay

    snake.move()
        

screen.exitonclick()