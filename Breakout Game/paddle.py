from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,9)
        self.penup()
        self.goto(position)
        self.step = 30
        self.paddle_speed = 1.1


    def left(self):
        self.backward(self.step)

    def right(self):
        self.forward(self.step)

    def update_speed(self):
        self.step *= self.paddle_speed