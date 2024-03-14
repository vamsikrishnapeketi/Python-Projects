from turtle import Turtle

class UpperPaddles(Turtle):

    def __init__(self,position,str_x,str_y):
        super().__init__()
        self.color("Green")
        self.shape("square")
        self.shapesize(str_x,str_y)
        self.penup()
        self.goto(position)
 