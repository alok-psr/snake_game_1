from turtle import *
COLOR='white'

class Boundry(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-350,350)
        self.pendown()
        self.pensize(3)
        self.color(COLOR)
        self.hideturtle()
        self.square()
    def square(self):
        self.goto(350,350)
        self.goto(350,-350)
        self.goto(-350,-350)
        self.goto(-350,350)