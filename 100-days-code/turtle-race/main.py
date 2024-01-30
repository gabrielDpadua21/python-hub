from turtle import Turtle, Screen
from random import randint

TURTLE = []
turtles_infos = [
    {"color": "red", "position": 100},
    {"color": "green", "position": 50},
    {"color": "blue", "position": 0},
    {"color": "purple", "position": -50},
    {"color": "orange", "position": -100},
]


def position_turtles():
    for info in turtles_infos:
        TURTLE.append(Turtle(shape="turtle"))
        TURTLE[-1].color(info["color"])
        TURTLE[-1].penup()
        TURTLE[-1].setposition(x=-240, y=-info["position"])


def race(bet):
    for turtle in TURTLE:
        if turtle.xcor() > 230:
            finished_race(turtle, bet)
            return
        turtle.forward(randint(0, 10))
    race(bet)


def finished_race(winner_turtle, bet):
    message = Turtle()
    message.hideturtle()
    if winner_turtle.pencolor() == bet:
        message.write("You won", align="center", font=("Arial", 24, "bold"))
    else:
        message.write("You lost", align="center", font=("Arial", 24, "bold"))


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Choose a turtle color: (red/green/blue/purple/orange)")

    position_turtles()
    race(user_bet)
    screen.exitonclick()