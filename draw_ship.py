import turtle

class Ship:
    def __init__(self):
    # Get dimensions
        self.draw = turtle.Turtle()
        self.win = self.draw.getscreen()
        self.width = self.win.window_width()
        self.height = self.win.window_height()
    def run(self):
        self.outline(self.draw, self.width, self.height)

    def outline(self, draw, width, height):
        # start pos
        x_start = -1 * width / 2
        y_start = height / 4
        draw.penup()
        draw.setpos(x_start, y_start)

        draw.pendown()
        draw.left(45)
        draw.forward(100)