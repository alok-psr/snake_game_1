
from turtle import *
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
SNAKE_SHAPE='square'
SNAKE_COLOR='white'


class Snake:

    def __init__(self,segs=5):

        self.segments = []
        self.segs=segs
        self.create(self.segs)
        self.head=self.segments[0]
        self.tail=self.segments[1:-1]


    def create(self, segs = 5):
        for i in range(segs):
            self.add_seg(post=i)

    def add_seg(self,post):
        new_seg = Turtle(SNAKE_SHAPE)
        new_seg.penup()
        new_seg.goto(-20 * post, 0)
        new_seg.color(SNAKE_COLOR)

        self.segments.append(new_seg)


    def extend(self):

        self.add_seg(900)

    def move(self):

        for i in range(len(self.segments)-1,0,-1):
            x,y=self.segments[i-1].pos()
            self.segments[i].goto(x,y) # starting position of snake
        self.segments[0].forward(DISTANCE)


    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)






