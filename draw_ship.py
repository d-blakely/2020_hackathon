import turtle

def draw():
    draw = turtle.Turtle()

    # Get dimensions
    win = draw.getscreen()
    width = win.window_width()
    height = win.window_height()

    print(height)

    # start pos
    x_start = -1 * width / 2
    y_start = height / 4
    draw.penup()
    draw.setpos(x_start, y_start)

    draw.pendown()
    draw.left(45)
    draw.forward(100)