from turtle import Turtle, Screen

my_turtle = Turtle()

size = 15

for _ in range(10):
    my_turtle.pendown()
    my_turtle.forward(size)
    my_turtle.penup()
    my_turtle.forward(size)



screen = Screen()
screen.exitonclick() 

