from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_center_line()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def draw_center_line(self):
        line = Turtle()
        line.hideturtle()
        line.color("white")
        line.penup()
        line.goto(0, -300)
        line.setheading(90)

        for _ in range(30):
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.setheading(random.randint(10,20))
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
