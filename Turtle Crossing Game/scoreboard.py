from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)


    def game_over(self):    
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=FONT)

    def lev_inc(self):
        self.level += 1
        self.display()