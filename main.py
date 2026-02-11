import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 states guessed",
        prompt="What's another state's name",
    ).title()
    if answer_state == "Exit":
        missing_states = []
        for states in state_list:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States-to-learn.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)
        guessed_state.append(answer_state)
