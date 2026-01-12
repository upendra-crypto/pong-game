from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        self.limit = self.screen.numinput(
            "Score Limit",
            "Enter score limit:",
            5, 1, 15
        )

        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Impact", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Impact", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def game_over(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER\n{winner} WINS",
            align="center",
            font=("Impact", 60, "normal")
        )
