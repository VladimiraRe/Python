import turtle
import pandas

FONT = "Arial", 8, "normal"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("50_states.csv")
states_list = data_states["state"].to_list()
guessed_states = []

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

while len(guessed_states) < 50:
    answer = screen.textinput(title=f" {len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states_list:

        row = data_states[data_states.state == answer]

        turtle.goto(x=int(row.x), y=int(row.y))
        turtle.write(answer, align="left", font=FONT)

        guessed_states.append(answer)



