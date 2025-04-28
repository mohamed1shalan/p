import numpy as np
# numpy >> linear algaber >> matrix
import pandas as pd
# pandas is libarary man work is Data Munging (جعل البيانات الغير مرتبه مرتبه)
from io import StringIO
# stingIO >> input and output >> بطريقه منظمه و نسمح بستخدام كل مميزات الكائنات من ادخال و اخراج الببانات
import matplotlib.pyplot as plt
# matplotlib.pyplot as plt >> experiance in transform data to fuger
import scipy.io as sio
import scipy.misc as misc
from scipy.special import cbrt 
# f_write = open("python/intro/file.txt", "w")
# f_write.write("hi hi")
# # print(f_write.tell())
# # print(f_write.seek(1))
# f_write = open("python/intro/file.txt", "r")
# print(f_write.read())
# f_write.close()
arrary = np.ones((4,4))
sio.savemat("sec1.txt", {'av': arrary})
data = sio.loadmat("sec1.txt")
print(data['av'])
# pan = pd.read_csv("https://milliams.com/courses/data_analysis_python/rain.csv")
# print(pan)
# print(pan.mean())
# print(pan[pan > 100].count())
# g = pan.plot(xlabel='monthly', ylabel='data')

# data = "1,2,3\n4,5,6"
# print(np.genfromtxt(StringIO(data), delimiter=","))

# data1 = u"""
# #hi
# #hhhkdm
# 1,2,3
# 35,5,7
# """
# print(np.genfromtxt(StringIO(data), delimiter=",", comments='#'))

# x = np.linspace(0, 10, 100)
# y = 4 + 2 * np.sin(2*x)
# # /////////////////////////////
# x_y = plt.subplot()
# x_y.fill_between(x, y)
# plt.show()

panda = misc.face()
plt.imshow(panda)
plt.show()
print(cbrt(64))
arr =[64 , 16 ,52 ]
print(cbrt(arr))