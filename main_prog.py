
import turtle
import draw_mountain
import draw_ship
import  draw_trees

screen = turtle.Screen()
screen.bgcolor("#00b8e6")
mountain = draw_mountain.Mountain()
mountain.run()

tree = draw_trees.Tree()
tree.run()

# ship = draw_ship.Ship()
# ship.run()

turtle.done()