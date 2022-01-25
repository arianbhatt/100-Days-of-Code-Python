"""
list of predefined functions
move()
turn_left()
take()
put()
toss()
build_wall()
pause()
done()
think(100)
sound(true)
World()
UsedRobot()
no_highlight()
"""
# function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
# Make Our Robot Make a Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
# Robot Hurdle Challange 1
# number of hurdles=6
num=int(input("Enter the Number of Hurdles: "))
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left

for i in range(0,num):
    jump()

# Hurdle2 New Hurdle with while loop flag can be anywhere new funtion at_goal()
while not at_goal():
    jump()

# Hurdle3 Wall Placement is now random new function front_is_clear() or wall_in_front(), at_goal()
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
# Hurdle4 walls are now variable positions are random also number of hurdles is also random.
"""
Things we can check 
at_goal()
front_is_clear()
right_is_clear()
wall_in_front()
wall_on_right()
object_here()
carries_object()
is_facing_north()
"""
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

