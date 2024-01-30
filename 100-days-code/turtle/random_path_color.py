from turtle import Turtle, Screen, colormode
from random import choice, randint

ANGLES = [0, 90, 180, 270]


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def random_path(my_turtle, path, size):
    for _ in range(path):
        my_turtle.pencolor(random_color())
        my_turtle.forward(size)
        my_turtle.setheading(choice(ANGLES))



if __name__ == "__main__":
    my_turtle = Turtle()
    colormode(255)
    my_turtle.pensize(5)
    my_turtle.speed("fast")
    random_path(my_turtle, 200, 30)

    screen = Screen()
    screen.exitonclick() 