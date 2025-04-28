from turtle import *
t = Turtle()
s = Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)
list_colors = ['red', 'blue', 'green', 'yellow',
               'purple', 'orange']
m = 0
for i in range(5, 300, 2):
    if (m == 6):
        m = 0
    t.color(list_colors[m])
    t.forward(i)
    t.left(61)
    m += 1

done()
