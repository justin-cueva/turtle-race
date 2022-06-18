from turtle import Turtle, Screen
import random

screen = Screen()
screen_width = 600
screen_height = 400
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)

turtle_starting_x = -screen_width/2 + screen_width * 0.05


turtle_colors = ['red', 'blue', 'orange', 'green', 'purple']

tim = Turtle()
bob = Turtle()
joe = Turtle()
alex = Turtle()
phil = Turtle()

all_turtles = [tim, bob, joe, alex, phil]


def init_turtle(turtle, turtle_number, turtle_color):
    turtle_starting_y = -screen_height / 6 + (25 * turtle_number)
    turtle.color(turtle_color)
    turtle.shape('turtle')
    turtle.penup()
    turtle.setx(turtle_starting_x)
    turtle.sety(turtle_starting_y)


number_of_turtles = len(all_turtles)
for turtle_number in range(number_of_turtles):
    init_turtle(turtle=all_turtles[turtle_number], turtle_number=turtle_number, turtle_color=turtle_colors[turtle_number])

screen.exitonclick()
