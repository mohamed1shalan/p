import math
import random

# print("mohamed")
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        print(i, " is even num")
    else:
        print(i, " is odd num")
n = 5
n %= 2
print(n)

# if 'M' in "Mohamed":
#     print("true")

# # 1        int
# # 1.25     floot
# # -1.25    floot
# # 1Jk      complex
# print(int(100.2e2))

# finame = "mohamed "
# sname = "shalan"
# fname = (finame + sname)
# print(fname)

# print("2x3=", 2*3)

a, b, c = 15, 16, 17

print(f"the reslt is {a} {b} {c}")
print("the reslt is", a, b, c, "hi")
# print(a+b)
# print(20+50)

# distant = 99
# time = 10
# spead = distant/time
# print("spead = %0.3f km/s" % spead)
# del (time)

# list = ['mohamed', 'ahmad', 'tota']
# x = random.choice(list)
# print(x)

# b = 10
# m = 0

# for b in range(10, 1000, 2):
#     m = m + b
# print(m)
# num1 = 10
# num2 = 0
# while num1 < 1000:
#     num2 += num1
#     num1 += 2
# print(num2)
# print("*"*9)
# l = 1
# while l < 10:
#     print("*"*l)
#     l += 1

# x = ['m', 'o', 'h', 'a', 'm', 'e', 'd']
# for p in x:
#     print(p)
#     print(f"{p}")

# page 27
# x = 0
# for x in range(1, 11):
#     print(x)
#     y = 0
#     while y <= x*9:
#         y += x
#         # بياخد الى بين القوصين الى فى الايند وبيضيفه عدد من المرات بعد الانتجر الى مكتوب
#         print('{:>1}' .format(y), end=' ')
#     print(" ")

# for k in range(60):
#     print(k)

# for z in range(0, 10, 2):
#     print(z)

# list = [1, 7, 2, 3, 4, 5, 6, 7]

# print(list.insert(1))

# print("are you want to enter a start and end number or use a deffult number (1,100)")
# print("enter 1 to enter number ")
# print("enter 2 to use a defult number ")
# choise = int(input())

# if choise == 1:
#     start = int(input("enter start number = "))
#     end   = int(input("enter end number = "))
# elif choise == 2:
#     start = 1
#     end =100
# else
import random

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print(f"Original list is : {test_list}")

# using random.choice() to
# get a random number
random_num = random.choice(test_list)

# printing random number
print("Random selected number is : " + str(random_num))
