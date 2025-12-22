from turtle import *
t = Turtle()
speed(100)


def oneStar(t, size, number):
    if number == 4:
        return
    elif number == 2:
        t.fillcolor("yellow")
        t.begin_fill()
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
    else:
        for _ in range(5):
            t.forward(size)
            oneStar(t, size/3, number + 1)
            t.right(144)


oneStar(t, 200, 0)
done()
