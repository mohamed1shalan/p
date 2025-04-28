from libarary import *


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.items = 0

    def add(self, data):
        if (data > self.data):
            if self.right == None:
                self.right = Tree(data)
                self.right.items += self.items
            else:
                self.right.add(data)
        else:
            if self.left == None:
                self.left = Tree(data)
                self.left.items += self.items
            else:
                self.left.add(data)

    def printtree(self):
        if (self.left != None and self.right != None):
            print(self.data)
            self.left.printtree()
            self.right.printtree()
        elif (self.left != None):
            # print(self.left.data)
            print(self.data)
            self.left.printtree()
        elif (self.right != None):
            print(self.data)
            # print(self.right.data)
            self.right.printtree()
        elif (self.left == None and self.right == None):
            print(self.data)
