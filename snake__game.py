import tkinter.messagebox
from time import sleep
from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from boundry import Boundry

BG_COLOR='black'
SCREEN_SIZE=(600,600)

s=Screen()
s.setup=SCREEN_SIZE
s.bgcolor(BG_COLOR)
s.tracer(0)

bo=Boundry()
snake=Snake(segs=8)
food=Food()
scp=ScoreBoard()

s.listen()
s.onkey(key='Up', fun=snake.Up)
s.onkey(key='Down', fun=snake.Down)
s.onkey(key='Left', fun=snake.Left)
s.onkey(key='Right', fun=snake.Right)

s.update()


# to make the snake move till game over
game_on=True
scp.sh_sc()
while game_on:
    s.update() # we are updating here to make all the segments show up at
               # the same time after they are to their new pos
    sleep(0.1) #by changing sleep we can change the speed of the snake as
               # we are jaan boojke stopping the snake after each movement
    snake.move()

    # food collision using distance method in Turtle class
    if snake.head.distance(food)<15:
        scp.inc_sc()
        scp.sh_sc()
        food.ramo()
        snake.extend()
    x=snake.head.xcor()
    y=snake.head.ycor()
    if x>350 or x<-350 or y>350 or y<-350:
        game_on=False
        scp.go()
    for i in snake.tail:
        if snake.head.distance(i)<15:
            scp.go()
            game_on=False
    # if game_on==False:
    #     s.textinput(title='do you want to retry', prompt='yes(y) or no(n)' ).lower()
    #     if s == 'y' or s=='yes':
    #         snake.retry()




s.exitonclick()