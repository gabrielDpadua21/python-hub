import colorgram
from turtle import Turtle, Screen, colormode
from random import choice


def get_colors():
    colors = colorgram.extract('image.jpg', 10)
    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def draw_paint(my_turtle, size):
    colors = get_colors()
    for _ in range(10):
        for _ in range(size):
            my_turtle.dot(20, choice(colors))
            my_turtle.forward(40)
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(400)
        my_turtle.setheading(0)
        


if __name__ == "__main__":
    my_turtle = Turtle()
    colormode(255)
    my_turtle.pensize(10)
    my_turtle.speed("fast")
    my_turtle.penup()
    my_turtle.setheading(225)
    my_turtle.forward(300)
    my_turtle.setheading(0)
    draw_paint(my_turtle, 10)
    


    screen = Screen()
    screen.exitonclick() 
    
    