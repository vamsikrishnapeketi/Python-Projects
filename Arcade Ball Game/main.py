from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()


screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_game_on = True

while is_game_on:
    screen.update() 
    time.sleep(ball.ball_speed)
    ball.move()

    #collision of ball with the top and the bottom wall 
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.collision_with_y()
        ball.move()

    #detection of ball with the paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.collision_with_x()
        ball.move()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.collision_with_x()
        ball.move()     

    #detection if the ball goes out of bounds
    if ball.xcor() > 380 :
        ball.reset_pos()
        score.l_score_inc()
        score.update()

    if ball.xcor() < -380:
        ball.reset_pos()   
        score.r_score_inc()  
        score.update()
    

screen.exitonclick()