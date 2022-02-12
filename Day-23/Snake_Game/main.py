import time
from scoreboard import Score
from snake import Snake
from food import Food
from turtle import Screen
screen=Screen()
screen.setup(width=600,height=600) # setting window resolution
screen.bgcolor("black") # setting screen bg
screen.title("Snake Xenzia") # Title of the Game window

screen.tracer(0) # closes the animation

starting_position=[(0,0),(-20,0),(-40,0)]

# Creating a snake and food
snake=Snake()
food=Food()
scorecard=Score()
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
    # Detecting Collision with food
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scorecard.increase_score()
        
    # Detecting Collision with wall
    if(snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 ):
        scorecard.reset()
        snake.reset()
        time.sleep(1)
    for segment in snake.segments[1:]: # slicing
        if snake.head.distance(segment)<10:
            scorecard.reset()
            snake.reset()
            time.sleep(1)
    # Detect collision with tail
    # if head collides with any segment in the tail. 
screen.exitonclick()