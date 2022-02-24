import random
from turtle import Turtle, Screen


def off_to_the_races():
    colors = ['red', 'blue', 'purple', 'orange', 'gray', 'green']
    all_turtles = []
    x_start = -250
    y_start = -115
    screen = Screen()
    screen.colormode(255)
    width = 500
    height = 400
    screen.screensize(width, height)

    for num in range(0, 6):
        race_turtle = Turtle()  # red
        race_turtle.shape("turtle")
        race_turtle.penup()
        race_turtle.setposition(x_start, y_start)
        race_turtle.color(colors[num])
        all_turtles.append(race_turtle)
        y_start += 50

    user_bet = screen.textinput(title="Who wins?", prompt="Which color will win the race?")
    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 360:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    turtle.setposition(-200, 0)
                    print("You've won! {} turtle won the race".format(winning_color).title())
                    turtle.write("You've won! {} turtle was the winner".format(winning_color).title(),
                                 font=("Verdana",
                                       15, "normal"))
                    break
                else:
                    print("You've lost...{} turtle was the winner".format(winning_color).title())
                    turtle.setposition(-200, 0)
                    turtle.write("You've lost...{} turtle was the winner".format(winning_color).title(),
                                 font=("Verdana",
                                       15, "normal"))
                    break
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    print(user_bet)

    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    off_to_the_races()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
