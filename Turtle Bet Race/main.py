from turtle import Turtle,Screen
import random as r

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet ?", prompt="Which turtle will win the race ? Enter the colour: ")
colours = ["red","orange","yellow","green","blue","purple"]
is_race_on = False
turtles = []

if user_bet:
    is_race_on = True


for i in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=-70+30*i)
    turtles.append(new_turtle)

while is_race_on:
    for i in turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_colour = i.pencolor()
            if winning_colour == user_bet:
                print(f"You have won, The winning colour is {winning_colour}")
            else:
                print(f"You have lost, The winning colour is {winning_colour}")
        steps = r.randint(0,10)
        i.forward(steps)
        