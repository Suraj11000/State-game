from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()

screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 state correct",
                                    prompt="Guess another satate?").title()
    if answer_state in all_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States to learn.csv")
        break
    if answer_state in all_state:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

