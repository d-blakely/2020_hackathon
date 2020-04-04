import turtle
import draw_mountain
import draw_trees
import draw_ship

screen = turtle.Screen()

mountain = draw_mountain.Mountain()
mountain.run()
screen.bgcolor("#99ebff")

ship = draw_ship.Ship()
ship.run()

tree = draw_trees.Tree()
tree.run()

turtle.done()