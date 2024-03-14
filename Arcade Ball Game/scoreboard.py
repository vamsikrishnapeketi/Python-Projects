from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def l_score_inc(self):
        self.l_score += 1

    def r_score_inc(self):
        self.r_score += 1  

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font= ("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font= ("Courier", 50, "normal"))
