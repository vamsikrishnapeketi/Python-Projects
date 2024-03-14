from turtle import Screen
from paddle import Paddle
from ball import Ball
from upperpaddles import UpperPaddles
import time

screen = Screen()
paddle = Paddle((0,-280))
ball = Ball()
upper_paddles = []

for x_position in range(-300,360,140):
    upaddels = UpperPaddles((x_position,120),2,6)
    upper_paddles.append(upaddels)

for x_position in range(-330,350,120):
    upaddels = UpperPaddles((x_position,170),2,5)
    upper_paddles.append(upaddels)

for x_position in range(-360,360,100):
    upaddels = UpperPaddles((x_position,220),2,4)
    upper_paddles.append(upaddels)

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

screen.listen()
screen.onkey(paddle.left,"Left")
screen.onkey(paddle.right,"Right")

is_game_on = True

while is_game_on:
    screen.update() 
    time.sleep(ball.ball_speed)
    ball.move()

    #collision of ball with the top and the bottom wall 
    if ball.ycor() > 280  :
        ball.collision_with_y()
        ball.move()

    #detection of ball with the side walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.collision_with_x()
        ball.move()     

    #detection of ball with the paddle
    if ball.ycor() < -270 and ball.distance(paddle) < 70:
        ball.collision_with_y()
        paddle.update_speed()
        ball.move()  

    #detection of ball with the upper paddles       
    for pad in upper_paddles:
        if ball.distance(pad) < 70 :
            upper_paddles.remove(pad)
            pad.hideturtle()
            ball.collision_with_y()
        if upper_paddles == []:
            ball.print_text("You Have WON!!")
            is_game_on = False   

    #detection if the ball goes out of bounds
    if ball.ycor() < -285 :
        ball.print_text("GAME OVER")
        is_game_on = False

    

screen.exitonclick()

