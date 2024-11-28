from turtle import Screen
from snake import Snake
import time

# snake_game
# 1. create a snake body
# 2. move the snake
# 3. control the snake
# 4. detect collision with food
# 5. create a scoreboard
# 6. detect collision with wall
# 7. detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()




screen.exitonclick()
