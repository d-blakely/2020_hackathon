import turtle

class Mountain:
    def __init__(self):
    # Get dimensions
        self.draw = turtle.Turtle()
        self.win = self.draw.getscreen()
        self.width = self.win.window_width()
        self.height = self.win.window_height()

    def run(self):
        self.outline(self.draw, self.width, self.height)


    def line(self,len,angle=0):
        self.draw.setheading(angle)
        self.draw.forward(self.width/len)

    def outline(self, draw, width, height):
         # start pos
        x_start = -1 * width / 2
        y_start = -1 * height / 5
        draw.penup()
        draw.setpos(x_start, y_start)

        draw.pendown()

        # up left side
        self.line(12, 25)
        self.line(8, 35)
        self.line(30, -10)
        self.line(30, 32)
        self.line(30, 2)

        self.line(30, 32) # shastina peak
        self.line(40)

        #  down shastina
        self.line(32, -22)
        self.line(20, -38)
        self.line(50)

        # up shasta
        self.line(12, 25)
        self.line(10, 40)

        # top of mt
        self.line(40, -17)
        self.line(30, 30)
        self.line(55, 10)
        self.line(50, -20)
        self.line(75, 50)

        # down shasta (right)
        self.line(40, -20)
        self.line(33, -5)
        self.line(20, -30)
        self.line(25, -10)
        self.line(20, -50)
        self.line(25, -43)
        self.line(30, -54)
        self.line(25, -25)
        self.line(20, -20)
        self.line(1, -2)