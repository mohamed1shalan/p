import random
import math

number = int(input("enter number of line row in Pascal's triangle = "))
list1 = [1]
# to print all row
number += 1
#
for x in range(1, number):
    y = number - x
    list2 = []
    w = 0
    for z in range(w, x + 1):
        q = z
        if z == 0 or z == x:
            if z == 2:
                list2.insert(z, list1[0])
            else:
                q = 0
                list2.insert(z, list1[0])
        else:
            list2.insert(z, list1[q] + list1[q - 1])
    print(" " * (y), *list1)
    list1 = list2
# def fact(x):
#     if x == 0 or x == 1:
#         fac = 1
#     else:
#         fac = 1
#         for f in range(2, x + 1):
#             fac = fac * f
#     return fac

# def sumi(Z):
#     s = 0
#     for i in range(N):
#         s += i
#     return s

# N = int(input('enter the value of N: '))
# R = int(input('enter the value of R: '))
# NCR = (fact(N) * sumi(N - 1)) / (fact(R) * fact(N - R))
# print('the value of NCR = ', NCR)
