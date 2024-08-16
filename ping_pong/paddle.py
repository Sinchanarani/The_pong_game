from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up_r(self):
        new_y = self.ycor() + 20
        self.goto(350, new_y)

    def go_down_r(self):
        new_y = self.ycor() - 20
        self.goto(350, new_y)

    def go_up_l(self):
        new_y = self.ycor() + 20
        self.goto(-350, new_y)

    def go_down_l(self):
        new_y = self.ycor() - 20
        self.goto(-350, new_y)
