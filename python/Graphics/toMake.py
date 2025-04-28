from graphics import *


def main():
    win = GraphWin("My Window", 500, 500)

    text = Text(Point(100, 100), "Hello World")
    text.setFace("arial")
    text.draw(win)

    win.getMouse()
    win.close()


main()
