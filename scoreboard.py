from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
# 親クラスの初期化メソッドを呼び出しタートル機能の継承
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.update_score()

        # 現在のスコア表示
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # スコアを1か算する
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()