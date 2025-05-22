from turtle import *
t = Turtle()
t.speed(0)
t.pensize(2)


def circle_tow_color(t, size, angle):
    t.color("red")
    t.circle(size, extent=90)
    t.color("black")
    t.circle(size, extent=180)
    t.color("red")
    t.circle(size, extent=90)
    t.left(90)
    t.penup()
    t.forward(size * 2)
    t.pendown()
    t.left(90)
    t.color("black")
    t.circle(size/2, extent=90)
    t.color("red")
    t.circle(size/2, extent=180)
    t.color("black")
    t.circle(size/2, extent=90)
    t.left(90)
    t.penup()
    t.forward(size * 2)
    t.pendown()


for i in range(12):

    circle_tow_color(t, 100, 0)
    t.left(30)

done()
