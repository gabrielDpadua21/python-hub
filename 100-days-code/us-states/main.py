import pandas
import turtle


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = 'blank_states_img.gif'
    screen.addshape(image)
    screen.setup(width=725, height=491)
    turtle.shape(image)
    states_list = []

    while len(states_list) < 50:
        answer = screen.textinput(title=f"{len(states_list)}/50 States Correct", prompt="What's another state's name?").title()
        
        data = pandas.read_csv('50_states.csv')
        state = data[data.state == answer]

        if answer == 'Exit':
            missing_states = []
            for state in data.state.to_list():
                if state not in states_list:
                    missing_states.append(state)
            missing_data = pandas.DataFrame(missing_states)
            missing_data.to_csv('missing_states.csv')
            exit()

        if not state.empty:
            states_list.append(answer)
            state_turtle = turtle.Turtle()
            state_x = int(state.x)
            state_y = int(state.y)

            state_turtle.penup()
            state_turtle.hideturtle()
            state_turtle.goto(state_x, state_y)
            state_turtle.write(answer)


    screen.exitonclick()