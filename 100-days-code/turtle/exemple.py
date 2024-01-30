from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.color("blue")
size = 300

for i in range(4):
    my_turtle.forward(size)
    my_turtle.right(90)



screen = Screen()
screen.exitonclick()