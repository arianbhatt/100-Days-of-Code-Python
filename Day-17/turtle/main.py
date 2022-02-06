# Creating a Million Dollar Painting 
import turtle as t
import random
shiro=t.Turtle()

#shiro.pensize(10)
rgb_colors=[(228, 226, 223), (232, 167, 61), (52, 110, 156), (211, 122, 163), 
(119, 148, 202), (17, 128, 95), (149, 20, 59), (4, 176, 143), 
(177, 45, 85), (223, 202, 119), (224, 77, 115), (160, 165, 36),
 (40, 164, 209), (28, 34, 83), (226, 90, 44), (119, 172, 116), 
 (215, 63, 34)]

t.colormode(255) # Changing the color mode

shiro.speed("fastest") # to make a fast 

def random_color():
    i= random.choice(rgb_colors)
    return i

random_color()

shiro.penup() # so that no lines
shiro.setheading(225)
shiro.forward(300)
shiro.setheading(0)
def row_change():
    shiro.setheading(90)
    shiro.forward(50)
    shiro.setheading(180)
    shiro.forward(500)
    shiro.setheading(0)

def draw_painting(number_of_dots):
    for dot_count in range(1,number_of_dots+1):
        shiro.dot(20,random_color())
        shiro.forward(50)
        if(dot_count%10==0):
            row_change()
draw_painting(100)
shiro.hideturtle()
screen=t.Screen() # so it stays
screen.exitonclick() # stays until we click on exit


