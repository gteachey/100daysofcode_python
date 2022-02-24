import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
correct_answers = 0
total_states = len(data)
# print(total_states)
states = data['state'].to_list()
# print( data['state'].to_list() )
guessed_states = []

while correct_answers < 50:
    answer = screen.textinput(title=f"{correct_answers}/{total_states} States Correct", prompt="What's another state "
                                                                                               "name: ").title()
    if answer == "Exit":
        dict_to_csv = {
            "state": [missing_state for missing_state in states if missing_state not in guessed_states]
        }
        output_csv = pandas.DataFrame(dict_to_csv)
        output_csv.to_csv("unknown_states.csv")
        break
    if answer.title() in states and answer not in guessed_states:
        t = turtle.Turtle()
        state = data[data.state == answer]
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.hideturtle()
        t.write(state.state.values[0], align="center")
        correct_answers += 1
        guessed_states.append(answer)

# turtle.mainloop()
# screen.exitonclick()
