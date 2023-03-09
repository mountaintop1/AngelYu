"""US State Game - Day 25 - Intermediate - Part 2 2021-07-26"""
import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
image = r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) # r is for raw string

data = pandas.read_csv(r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\us_states_game\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        states_to_learn = r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\us_states_game\states_to_learn.csv"
        new_data.to_csv(states_to_learn)
        break

    # if answer_state in data.state.to_list():
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
