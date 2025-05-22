# import math
# from turtle import *


# def hh(k):
#     return 15*math.sin(k)**3


# def hhh(k):
#     return 12*math.cos(k)-5 *\
#         math.cos(2*k)-2 *\
#         math.cos(3*k) -\
#         math.cos(4*k)


# speed(1000000000)
# bgcolor("black")

# for i in range(6000000000):
#     goto(hh(i)*20, hhh(i)*20)
#     for j in range(5):
#         color("red")
#     goto(0, 0)
# done()


number = 0


class member:

    def __init__(self, frist, medile, last, gender):
        self.fname = frist
        self.mname = medile
        self.lname = last
        self.gender = gender
        self.fullname = frist+medile+last

    def welcom_massege(self):
        if self.gender == "male":
            return f"hallo Mr: {self.fname}"
        else:
            return f"hallo Miss: {self.fname}"


mo1 = member('mohamed', 'elsaiead', 'shalan', 'male')

mo2 = member('ahmad', 'elsaiead', 'shalan', 'male')
print(mo1.welcom_massege())


# class Fruit:
#     name = "apple"
#     price = 10

#     def eat_fruit(self):
#         print("Fruit has been eaten")


# f = Fruit()
# f.eat_fruit()
# print(f.name)
# print(f.price)
