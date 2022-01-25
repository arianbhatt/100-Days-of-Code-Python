"""
just follow along the right wall (basically a algorithm)
turn right if it can elif front else left
functions available
move()
turn_left()
front_is_clear()
wall_in_front()
right_is_clear()
wall_on_right()
at_goal()
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif(front_is_clear):
        move()
    else:
        turn_left()

