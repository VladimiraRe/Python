from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
FONT_GAME_OVER = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

