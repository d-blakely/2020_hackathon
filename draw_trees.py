import turtle
from random import randint


class Tree:
    def __init__(self):
    # Get dimensions
        self.draw = turtle.Turtle()
        self.draw.color("#00cc00")
        self.draw.speed(10)
        self.win = self.draw.getscreen()
        self.width = self.win.window_width()
        self.height = self.win.window_height()

    def run(self):
        self.outline(self.draw, self.width, self.height)
        self.draw.hideturtle()

    # draws a line of window_width/len at angle
    def line(self, len, angle=0):
        self.draw.setheading(angle)
        self.draw.forward(self.width / len)

    # recursively draw tree
    def tree(self, len, a, f):
        """
        len is length of branch
        a is initial position
        f is factor by which branch is shortened
        from level to level."""
        if len < 100:
            temp_pos = self.draw.pos()
            self.line(len, -135)
            self.draw.penup()
            self.draw.goto(temp_pos)
            self.draw.pendown()
            self.line(len, -45)
            self.draw.penup()
            self.draw.goto(temp_pos)
            self.line(160, 90)
            self.draw.pendown()
            self.tree(len/f, a, f)
        else:
            # draw trunk
            self.draw.penup()
            self.draw.goto(a)
            self.draw.color("brown")
            self.draw.pensize(3)
            self.draw.pendown()
            self.line(50, -90)
            self.draw.color("#00cc00")
            self.draw.pensize(1)



    def outline(self, draw, width, height):
         # start pos
        # x_start = -1 * width / 2
        y_lim = -1 * height / 4

        for i in range(25):
            draw.penup()
            draw.setpos(randint(-1 * width/2, width/2), randint(-1 * height/2, int(y_lim)))
            draw.pendown()
            self.tree(25, self.draw.position(), .8)