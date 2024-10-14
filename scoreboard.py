import tkinter
from turtle import *

POSI=(0,300)
ALIGN='center'
COLOR='white'
FONT=('Arial', 20, 'normal')
TEXT='SCORE :'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.shapesize(2)
        self.goto(*POSI)
    def sh_sc(self):

        self.clear()
        self.write(arg=f'{TEXT} {self.score}', align=ALIGN, font=FONT)

    def inc_sc(self):
        self.score+=1
    def go(self):
        tkinter.messagebox.showinfo(title='LMAOOO you suck🤣🤣', message=f'game over your score  {self.score}')
