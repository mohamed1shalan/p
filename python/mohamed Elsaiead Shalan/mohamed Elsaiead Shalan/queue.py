from libarary import *


class qeueu:
    def __init__(self):
        self.que = []


class stackqueu:
    def __init__(self):
        self.items = 0
        self.new = qeueu()

    def add(self, data):
        self.new.que.append(data)
        self.items += 1

    def pop(self):
        self.new.que.pop(0)
        self.items -= 1

    def printq(self):
        print(*self.new.que, sep=' ')
        print()
