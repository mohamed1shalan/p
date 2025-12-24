from turtle import *
t = Turtle()
t.speed(0)

angle = 0


def make_circle(t, size, angle):
    t.left(angle)
    for i in range(33):
        t.circle(size - i * 3)
        t.right(2)
    t.left(66)


for i in range(4):
    make_circle(t, 100, angle)
    angle += 90
done()
