from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def draw_circle(my_turtle, graph, size):
    for _ in range(int(360 / graph)):
        my_turtle.pencolor(random_color())
        my_turtle.circle(size)
        my_turtle.setheading(my_turtle.heading() + graph)



if __name__ == "__main__":
    my_turtle = Turtle()
    colormode(255)
    my_turtle.speed("fastest")
    draw_circle(my_turtle, 5, 100)

    screen = Screen()
    screen.exitonclick() 