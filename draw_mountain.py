import turtle

class Mountain:
    def __init__(self):
    # Get dimensions
        self.draw = turtle.Turtle()
        self.draw.speed(10)
        self.win = self.draw.getscreen()
        self.width = self.win.window_width()
        self.height = self.win.window_height()

    def run(self):
        self.outline(self.draw, self.width, self.height)
        self.ground(self.draw, self.width, self.height)
        self.draw.hideturtle()

    # draws a line of window_width/len at angle
    def line(self,len,angle=0):
        self.draw.setheading(angle)
        self.draw.forward(self.width/len)

    # move point without drawing
    def move(self, len_x, len_y):
        self.draw.penup()
        newx = self.draw.xcor() + self.width / len_x
        newy = self.draw.ycor() + self.height / len_y
        self.draw.setposition(newx, newy)
        self.draw.pendown()

    def ground(self, draw, width, height):
        # start pos
        x_start = -1 * width / 2
        y_start = -1 * height / 4
        draw.penup()
        draw.setpos(x_start, y_start)

        draw.pendown()
        draw.fillcolor("#004d00")
        draw.begin_fill()
        draw.right(170)
        draw.circle(1000,-200)
        draw.end_fill()

        draw.setheading(0)
        draw.penup()
        draw.setposition(width/2, y_start)
        draw.begin_fill()
        draw.pendown()
        draw.left(170)
        draw.circle(1600, 200)
        draw.end_fill()

    def outline(self, draw, width, height):
        # start pos
        x_start = -1 * width / 2
        y_start = -1 * height / 5
        draw.penup()
        draw.setpos(x_start, y_start)

        draw.pendown()
        draw.fillcolor("white")
        draw.begin_fill()
        # up left side
        self.line(12, 25)
        self.line(8, 35)
        self.line(30, -10)
        self.line(30, 32)
        self.line(30, 2)

        # draw ridges
        temp_pos = self.draw.pos() # save current position
        self.line(20, -130)
        self.line(8, -155)

        self.move(width/20, -width/20)

        self.line(40, 45)
        self.line(16, 30)

        self.draw.penup() # move back to saved position
        self.draw.setposition(temp_pos)
        self.draw.pendown()
        # End ridge

        self.line(30, 32) # shastina peak
        self.line(40)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(30, -70)
        self.line(25, -150)
        self.line(20, -130)

        self.move(8, -55)
        self.line(40, 155)
        self.line(16, 140)

        self.move(100, -50)
        self.line(60, 170)

        self.move(100, -50)
        self.line(-25, 25)
        self.line(-30, 35)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        #  down shastina
        self.line(32, -30)
        self.line(20, -38)
        self.line(50)

        # up shasta
        self.line(12, 25)
        self.line(10, 40)

        # top of mt
        self.line(40, -17)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(10, -140)
        self.line(16, -150)
        self.line(20, -120)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(30, 30)
        self.line(55, 10)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(15, -60)
        self.line(30, 120)
        self.line(30, -110)
        self.line(30, -75)
        self.line(15, -130)
        self.line(30, 50)
        self.line(20, -55)
        self.line(25,-30)
        self.move(-15, 8)
        self.line(15, -140)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(50, -20)
        self.line(75, 50)

        # down shasta (right)
        self.line(40, -20)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(20, -30)
        self.draw.goto(temp_pos)
        self.line(25, -45)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(33, -5)
        self.line(20, -30)
        self.line(25, -10)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(20, -135)
        self.draw.goto(temp_pos)
        self.line(25, -130)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(20, -50)
        self.line(25, -43)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(30, -100)
        self.line(30, -60)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(30, -54)

        # draw ridges
        temp_pos = self.draw.pos()  # save current position
        self.line(20, -75)
        self.line(25, -60)

        self.draw.penup()
        self.draw.goto(temp_pos)
        self.draw.pendown()
        # End ridges

        self.line(25, -25)
        self.line(20, -20)
        self.line(3, -2)
        draw.goto(draw.xcor(),y_start)

        draw.pencolor("white")
        self.line(1,-90)
        self.line(.5,180)
        self.line(1,90)
        self.line(.5)
        draw.pencolor("black")
        draw.end_fill()