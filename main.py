from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Muncher Snake")
screen.tracer(0)#画面更新を止めアニメーションをスムーズに
screen._root.resizable(False, False)  # ウィンドウのサイズ変更を無効にする

snake = Snake()
food = Food()
score = Scoreboard()

# 蛇のコントロール
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# ゲームのループ
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # 蛇の動きの処理をクラスのメソッドとして呼び出す
    snake.move()

    # 蛇と食べ物が重なったときの処理
    if snake.head.distance(food) < 15: #食べ物との距離が15ピクセル以下の時
        food.refresh()
        snake.extend()
        score.increase_score()

    # 壁との衝突の検知処理
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    # 尻尾と衝突の検知処理
    # どのセグメントにぶつかっても処理される
    # スライスを使ったセグメント
    for segment in snake.segments[1:]:
        if snake.head .distance(segment) < 10:
            game_on = False
            score.game_over()

screen.mainloop()