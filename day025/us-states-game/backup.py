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
answer = screen.textinput(title=f"{correct_answers}/{total_states} States Correct",
                          prompt="What's another state name: ")
print(answer)

turtle.mainloop()

screen.exitonclick()
