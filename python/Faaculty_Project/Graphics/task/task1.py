from graphics import *


class House:
    def __init__(self):
        self.win = GraphWin("House", 400, 400)

    def triangle(self):
        p1 = Point(200, 50)
        p2 = Point(100, 150)
        p3 = Point(300, 150)
        triangle = Polygon(p1, p2, p3)
        triangle.setFill("brown")
        triangle.draw(self.win)

    def rectangle(self):
        p1 = Point(100, 150)
        p2 = Point(300, 300)
        rectangle = Rectangle(p1, p2)
        rectangle.setFill("yellow")
        rectangle.draw(self.win)

    def windows(self, p1, p2):
        window = Rectangle(p1, p2)
        window.setFill("white")
        window.draw(self.win)

    def doorandpoint(self, p1, p2, point):
        door = Rectangle(p1, p2)
        door.setFill("brown")
        door.draw(self.win)
        circle = Circle(point, 3)
        circle.setFill("black")
        circle.draw(self.win)


house = House()
house.triangle()
house.rectangle()
house.windows(Point(120, 170), Point(160, 210))
house.windows(Point(240, 170), Point(280, 210))
house.doorandpoint(Point(180, 250), Point(220, 300), Point(215, 280))
house.win.getMouse()
house.win.close()
