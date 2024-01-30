from turtle import Turtle, Screen
from random import choice

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black"]
angles = [0, 90, 180, 270]

my_turtle = Turtle()
my_turtle.pensize(5)
my_turtle.speed("fast")
size = 30
path = 500

for _ in range(500):
    my_turtle.color(choice(colors))
    my_turtle.forward(size)
    my_turtle.setheading(choice(angles))



screen = Screen()
screen.exitonclick() 