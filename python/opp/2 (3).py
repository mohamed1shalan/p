import random
import numpy as np
from numpy import *
import mysql
import mysql.connector
import sqlite3
from py import member

# mohamed = member('mohamed', 'elsaiead', 'shalan', 'male')

# print(member.number)
# ma = sqlite3.connect(database='app.db')
# cor = ma.cursor()
# cor.execute(" SHOW TABLES")
# mo = {
#     "moo": 'skn',
#     "smln": "kdfnjkds"
# }
# print('')

# arra = array([1, 2, 3, 3, 45, 6, 7, 9])
# arr = array(42)
# arr = array([
#             [
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]
#             ],
#             [
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]
#             ],
#             [
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]
#             ],
#             [
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]
#             ],
#             [
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]],
#                 [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]
#             ]
#             ])
# print(arr.ndim)
# mohamed = member('Moahmed', 'Elsaiead', 'Shalan', 'male', 5885)
# ahamad = member('Moahmed', 'Elsaiead', 'Shalan', 'male', 5427)
# mohamed = member('Moahmed', 'Elsaiead', 'Shalan', 'male', 79646)
# mohamed = member('Moahmed', 'Elsaiead', 'Shalan', 'male', 745)

# print(mohamed.id)
# print(mohamed.myid())

# arr = array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print('5th element on 2nd row: ', arr[1, 4])
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-2:7:2])
# print(cos(pi))
# a = random.random((4, 5))
# print(a)
# print(random.randint(140, size=10))
# print(random.randint(0, 10, size=(3, 4, 5)))
# print(random.choice(random.randint(0, 10, 80)))
# member1 = member('mohamed', "elsaiead", "shalan", "male")
# print(member1.mr_msr())

# db = sqlite3.connect("app.db")
# # setting up the curser
# cr = db.cursor()
# cr.execute(
#     "CREATE TABLE if not exists skiles(name Text,progress integer,user_id integer)")
# cr.execute(
#     "CREATE TABLE if not exists Users(user_id integer,name text)")
# # # # insert data
# # cr.execute("INSERT INTO Users(user_id ,name) values(1, 'mohamed')")
# # cr.execute("INSERT INTO Users(user_id ,name) values(1, 'mohamed')")

# print(cr.execute("select * from Users").fetchone())
# print(cr.execute("select * from Users").fetchone())
# print(cr.execute("select * from Users").fetchone())
# print(cr.execute("select * from Users").fetchone())


# db.commit()
# db.close()
# member_one = member("mohanmed", "elsaied", "Shalan", "male")
# # member_tow = member("nnnnn", "nnn", "nnn")
# # member_there = member("ffff", "fff", "fff")
# print(member_one.mr_msr())

# import pdb
# # print(5 // 2)
# x = int(input('enter the value of x: '))
# if x >= 10:

#     def sumfun(x):
#         y = x**2 + 5 * x + 8
#         return y
# else:

#     def sumfun(x):
#         y = 4 * x**2 + 7 * x + 8
#         return y

# print(sumfun(x))

# def area_circle(x):
#     pi = 3.014159
#     area = pi * x**2
#     return area

# print("area is %0.2f" % area_circle(2))

# print("area is {:.2f}".format(area_circle(2)))

# def times(n1, n2):
#     return n1 + n2

# x = int(
#     input(
#         "this app to sum 2 number\nenter 2 numder\nenter number of tiems of you want\n"
#     ))
# for i in range(x):
#     a = int(input("enter the first number: "))
#     b = int(input("enter the scound number: "))
#     print(times(a, b))


# def fun(x):
#     w = 1
#     for i in range(1, x + 1):
#         w = w * i
#     return w


# def sum(y):
#     z = 0
#     for i in range(y):
#         z = i + z
#     return z


# N = int(input("enter N"))
# R = int(input("enter R"))

# print((fun(N) * sum(N - 1)) / (fun(R) * fun(N - R)))
# import os
# import re
# f = open("halo.txt", 'w+', encoding="utf-8")
# arr = np.array([1, 2, 3, 5, 4], ndmin=5)
# print(arr)
# print(np.__version__)
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])
# print(arr.dtype)
# a = random.uniform(1, 10, 5)
# print(a)
# a = random.random((2, 3))  # all number here betwem 1 and 0
# b = random.normal((2, 3))  # all number here betwem 1 and 0
# a = random.randint(140, 190, size=10)
# print(b)
# a = random.randint(0, 10, 25)
# b = reshape(a, (5, 5))
# print(b)
# print(random.choice(a))
# a = linspace(4, 15, 18).reshape(3, 6)
# print(a)
# a = arange(12)
# b = shape(a)
# c = a.reshape(3, 4)
# d = shape(c)
# print(a)
# print(b)
# print(c)
# print(d)
x = [11, 22, 33, 44, 55, 66, 77, 88]
x1, x2, x3 = split(x, (3, 6))
print(x1, x2, x3)
print('-------------------')
x1, x2, x3 = split(x, (3, 5))
print(x1, x2, x3)
print('-------------------')
x1, x2, x3 = split(x, (3, 2))
print(x1, x2, x3)
print('-------------------')
# x1, x2, x3 = split(x, (1, 5))
# print(x1, x2, x3)
# print('-------------------')
