from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(5)


def move_backwards():
    turtle.backward(5)


def turn_right():
    turtle.right(10)



def turn_left():
    turtle.left(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


if __name__ == "__main__":
    screen.listen()
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_right, "d")
    screen.onkey(turn_left, "a")
    screen.onkey(clear, "c")

    screen.exitonclick()




