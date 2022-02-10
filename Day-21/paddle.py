from turtle import Turtle
MOVE_DISTANCE=20

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    def up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        if(new_y<275):
            self.move(new_y)
    def down(self):
        new_y=self.ycor()-MOVE_DISTANCE
        if new_y>-275:
            self.move(new_y)    
    def move(self,y):
        self.goto(self.xcor(),y)