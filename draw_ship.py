import turtle
from random import randint


class Ship:
    def __init__(self):
    # Get dimensions
        self.draw = turtle.Turtle()
        self.draw.speed(10)
        self.win = self.draw.getscreen()
        self.width = self.win.window_width()
        self.height = self.win.window_height()

    def run(self):
        self.outline(self.draw, self.width, self.height)
        self.draw.hideturtle()

    def draw_oval(self, x, y, big_radius, small_radius, tilt):
        self.draw.up()
        self.draw.goto(x, y)
        self.draw.down()
        self.draw.seth(-45 + tilt)
        # self.draw.color('red')
        self.draw.circle(big_radius, 90)
        # self.draw.color('blue')
        self.draw.circle(small_radius, 90)
        # self.draw.color('red')
        self.draw.circle(big_radius, 90)
        # self.draw.color('blue')
        self.draw.circle(small_radius, 90)

    # move point without drawing
    def move(self, len_x, len_y):
        self.draw.penup()
        newx = self.draw.xcor() + self.width / len_x
        newy = self.draw.ycor() + self.height / len_y
        self.draw.setposition(newx, newy)
        self.draw.pendown()

    def outline(self, draw, width, height):
        # start pos
        x_start = -1 * width / 3
        y_start = height / 5
        draw.penup()
        draw.setpos(x_start, y_start)

        draw.pendown()

        draw.fillcolor("grey")
        draw.begin_fill()
        self.draw_oval(draw.xcor(),draw.ycor(),width/8,width/100,20)
        draw.end_fill()

        # draw circles
        self.move(50, -300)
        draw.fillcolor("red")
        draw.begin_fill()
        draw.circle(5)
        draw.end_fill()

        draw.begin_fill()
        self.move(30, -200)
        draw.circle(5)
        draw.end_fill()

        draw.begin_fill()
        self.move(30, 400)
        draw.circle(5)
        draw.end_fill()

        draw.begin_fill()
        self.move(30, 40)
        draw.circle(5)
        draw.end_fill()

        draw.begin_fill()
        self.move(30, 20)
        draw.circle(5)
        draw.end_fill()

        draw.fillcolor("black")
        draw.begin_fill()
        self.draw_oval(draw.xcor() - width/8, draw.ycor()-height/50, width / 16, width / 100, 20)
        draw.end_fill()
