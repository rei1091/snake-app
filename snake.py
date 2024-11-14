from turtle import Turtle
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
# 蛇の体を作成
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in range(3):
            self.add_segment((pos*-20,0))

    def add_segment(self, pos):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def extend(self):
        # セグメントの追加
        self.add_segment(self.segments[-1].position())

    def move(self):
        # 蛇の動きの処理
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE)

    # 蛇のコントロール処理
    def up(self):
        if self.head.heading() != DOWN: #もし今の頭の向きが下に向いていなければ上を向ける
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)