from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 40)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 40)
