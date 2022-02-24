from turtle import Turtle

GAME_OVER = "GAME OVER"

ALIGN = "center"
SCORE_BOARD_ = "ScoreBoard: {} High Score: {}"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as get_high_score:
            self.high_score = int(get_high_score.read())
            print(self.high_score)
        self.ht()
        self.penup()
        self.pencolor("white")
        self.setposition(-30, 260)
        self.speed("fastest")
        self.reset_score()
        self.write(SCORE_BOARD_.format(self.score, self.high_score), align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(SCORE_BOARD_.format(self.score, self.high_score), align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            with open("data.txt", mode="w") as record_score:
                record_score.write(str(self.high_score))
            self.write(SCORE_BOARD_.format(self.score, self.high_score), align=ALIGN, font=FONT)
            self.score = 0
# def game_over(self):
#     self.setposition(-30,0)
#     self.write(GAME_OVER, align=ALIGN, font=FONT)
