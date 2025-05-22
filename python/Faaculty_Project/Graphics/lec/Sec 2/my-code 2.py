import turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)


def draw_branch(length):
    if length < 5:
        return
    t.forward(length)
    t.left(30)
    draw_branch(length - 15)
    t.right(60)
    draw_branch(length - 15)
    t.left(30)
    t.backward(length)


t.penup()
t.goto(0, -200)
t.pendown()
draw_branch(100)
turtle.done()
