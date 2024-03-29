from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.y_move = 10
        self.x_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def collision_with_y(self):
        self.y_move *= -1

    def collision_with_x(self):
        self.x_move *= -1    
        self.ball_speed *= 0.90

    def reset_pos(self):
        self.goto(0, 0)
        self.collision_with_x()
        self.ball_speed = 0.1
