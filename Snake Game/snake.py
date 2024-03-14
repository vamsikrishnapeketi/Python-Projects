from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.snake[0]    

    def move(self):
        for seg in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg-1].xcor()
            new_y = self.snake[seg-1].ycor()
            self.snake[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)  

    def add_segment(self,position):
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(position)
        self.snake.append(snake_part)    

    def extend(self):
        self.add_segment(self.snake[-1].position())               

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:    
            self.head.setheading(180)        
    def right(self):
        if self.head.heading() != 180:    
            self.head.setheading(0)    