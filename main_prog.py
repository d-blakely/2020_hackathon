
import turtle
import draw_mountain
import  draw_trees

screen = turtle.Screen()

mountain = draw_mountain.Mountain()
mountain.run()
screen.bgcolor("#99ebff")
tree = draw_trees.Tree()
tree.run()

turtle.done()