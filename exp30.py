import turtle
import itertools
colors = ['red', 'green', 'blue', 'yellow', 'magenta']
color_cycle = itertools.cycle(colors)
t = turtle.Turtle()
t.speed(0)
for i in range(37):
    t.color(next(color_cycle))   
    t.circle(50)            
    t.left(20)                  
turtle.done()
