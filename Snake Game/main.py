from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()   

    #when the snake eats the food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        is_game_on = False
        score.game_over()    

    #detect collision with itself:
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()  






screen.exitonclick()