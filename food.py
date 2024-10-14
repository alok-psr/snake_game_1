from random import randint
from turtle import Turtle

SHAPE='circle'
COLOR='yellow'
SHAPE_SIZE=(0.5,0.5)
BOUNDS=(-280,280)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.speed('fastest')
        self.shapesize(*SHAPE_SIZE)
        self.ramo()

    def ramo(self):
        self.rax = randint(*BOUNDS)
        self.ray = randint(*BOUNDS)
        self.goto(self.rax,self.ray)
