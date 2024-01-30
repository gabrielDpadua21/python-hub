from turtle import Turtle, Screen


my_turtle = Turtle()
size = 100

sides = [
    {"size": 3, "color": "red"},
    {"size": 4, "color": "blue"},
    {"size": 5, "color": "green"},
    {"size": 6, "color": "yellow"},
    {"size": 7, "color": "orange"},
    {"size": 8, "color": "purple"},
    {"size": 9, "color": "pink"},
    {"size": 10, "color": "black"},
]

for side in sides:
    for _ in range(side['size']):
        my_turtle.color(side['color'])
        my_turtle.forward(size)
        my_turtle.right(360 / side['size'])



screen = Screen()
screen.exitonclick() 