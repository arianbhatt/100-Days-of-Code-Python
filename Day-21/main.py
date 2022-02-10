from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
sc=Screen()
sc.setup(height=600,width=800)
sc.title(titlestring="Pong Game")
sc.bgcolor("black")
sc.tracer(0)

pad_1=Paddle((350,0))
pad_2=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
sc.listen()

sc.onkey(pad_1.up, "Up")
sc.onkey(pad_1.down, "Down")
sc.onkey(pad_2.up,"w")
sc.onkey(pad_2.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    # check the collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_wall()
    # check collision with the paddle
    if (ball.distance(pad_1)<50 and ball.xcor()>330) or (ball.distance(pad_2)<50 and ball.xcor()<-330):
        ball.bounce_pad()

    # miss the ball paddle
    if(ball.xcor()>380):
        ball.reset_position()
        scoreboard.l_point()
    if(ball.xcor()<-380):
        ball.reset_position()
        scoreboard.r_point()
    
sc.exitonclick()