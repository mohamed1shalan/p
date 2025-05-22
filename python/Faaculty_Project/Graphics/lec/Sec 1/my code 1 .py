from graphics import *


class maina_windw:
    def __init__(self):
        self.win = GraphWin("My Window", 500, 500)

    def make_line(self):
        point1 = Point(250, 0)
        point2 = Point(250, 400)
        line = Line(point1, point2)
        line.setOutline("red")
        line.setWidth(5)
        line.setArrow("both")
        line.draw(self.win)

    def nake_regtangel(self):
        point1 = Point(100, 100)
        point2 = Point(400, 400)
        regtangel = Rectangle(point1, point2)
        regtangel.setFill("blue")
        regtangel.draw(self.win)

    def make_text(self):
        text = Text(Point(250, 100), "Hello World")
        centerPoint = text.getAnchor()
        text.draw(self.win)
        print(centerPoint)

    def input(self):
        enter = Entry(Point(250, 200), 20)
        enter.draw(self.win)
        self.win.getMouse()
        enter_VALUE = enter.getText()
        print(enter_VALUE)

    def end(self):
        self.win.getMouse()
        self.win.close()


window = maina_windw()
window.nake_regtangel()
window.input()
window.make_line()
window.make_text()
window.end()
