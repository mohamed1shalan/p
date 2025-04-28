from turtle import *

t = Turtle()

t.fillcolor("yellow")

t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()


done()
