from turtle import *
t = Turtle()
t.speed(0)


def make_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)


t.pensize(5)
list_colors = ['red', 'blue', 'green', 'yellow',
               'purple', 'orange', 'pink', 'brown',
               'black', 'gray']
for i in range(len(list_colors)):
    t.color(list_colors[i])
    t.right(90)
    make_square(t, 100)
    t.right(90)
    make_square(t, 100)
    t.right(90)
    make_square(t, 100)
    t.right(90)
    make_square(t, 100)
    t.end_fill()
    t.right(i+2 * 10)
done()
