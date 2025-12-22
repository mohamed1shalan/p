from turtle import *
t = Turtle()
t.speed(0)
t.penup()
t.goto(-300, 250)
t.pendown()
size = 500
angle = 6
scla_change = 0.9
for i in range(60):
    for _ in range(4):
        t.forward(size)
        t.right(90)

    t.forward(size*(1-scla_change))
    t.right(angle)
    size *= scla_change

done()
