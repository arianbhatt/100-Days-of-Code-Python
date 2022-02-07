from turtle import Turtle, Screen
import random

from numpy import ravel
screen=Screen()

is_race_on=False

colors=['red','orange','yellow','green','blue','purple']
turtles=[]
for i in range(0,len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your Bet",
prompt="Which turtle will win the race? Enter a color")
if user_bet:
    is_race_on=True

def start(list_turtles):
    n=-150
    for racer in list_turtles:
        racer.penup()
        racer.goto(x=-230,y=n)
        n+=60    

def move(turtle_name):
    turtle_name.forward(random.randint(0,10))
    if turtle_name.xcor()>230:
        winning_color=turtle_name.pencolor()
        if winning_color==user_bet:
            print(f"You've won the {winning_color} is the winning turtle")
        else:
            print(f"You've lost the {winning_color} is the winning turtle")
        return False
    return True

start(turtles)

while(is_race_on):
    for racer in turtles:
       is_race_on=move(racer)
       if is_race_on==False:
           break
        

screen.exitonclick()