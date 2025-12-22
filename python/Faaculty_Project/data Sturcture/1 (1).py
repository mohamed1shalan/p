from scipy.linalg import lu
import math
import numpy as np
from numpy.linalg import norm, det, inv, cond

V_row = np.array([[1, 2, 3, 4]])
V_cal = np.array([[1], [6], [8], [10]])
print(V_row.shape)
print(V_row)
print(V_cal.shape)
print(V_cal)
print("V_row")
print(norm(V_row, 1))  # calc number of items
print(norm(V_row, 2))
print(math.sqrt((1 * 1) + (2 * 2) + (3 * 3) + (4 * 4)))
print(norm(V_row, np.inf))
# get sum of all number in each row and return max value
# to multublay tow v
print(np.dot(V_row, V_cal))
print()
# angle betwen to vector
# arccos(dot(v, w.T)/(norm(v) *norm(w)))
theta = np.arccos(np.dot(V_row, V_cal)/(norm(V_cal, 2)*norm(V_row, 2)))
print(theta)
print()
# Matrix
# Create matrix in pyton
m = np.array([[1, 2, 3], [1, 5, 6], [10, 3, 2]])
# operation in matrx

# المحدد
print(det(m))
print(inv(m))
print(np.dot(m, inv(m)))

# مصفوفه وحده
m2 = np.eye(4)
print(m2)

# ill بتحدد اذا كان المصفوفه قربت تبقى شازه قد ايه
# كل ما الرقم يكبر دا معناه ان المصفوفه دى قؤبت تكون شاذه
print(cond(m))
print(cond(m2))
m3 = np.array([[0, 0, 0], [0, 0, 6], [1, 23, 2]])
print(cond(m3))

# itratione methods

a = np.array([[8, 3, -3], [-2, -8, 5], [3, 5, 10]])

# احسب dominant

diag = np.diag(abs(a))

print(diag)
# مجمموع لالرقان الى مش فى القطر الرايسى
not_dia = np.sum(abs(a), axis=1)-diag
print(not_dia)
# دلوقتى هقارن
if np.all(diag > not_dia):
    print("matrix is dominant")
else:
    print("not Diamnont")
################
x1 = 0
x2 = 0
x3 = 0
esp = 0.01
containue = False
x_old = np.array([x1, x2, x3])

print("K  x1   x2   x3")

for i in range(1, 50):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/-8
    x3 = (-8-3*x1-5*x2)/-5
    x = np.array([x1, x2, x3])
    esp_new = np.sqrt(np.dot(x-x_old, x-x_old))
    print(f'{i}  {round(x1, 2)}  {round(x2, 2)}  {round(x3, 2)}')
    if esp_new < esp:
        containue = True
        print('converged')
        break
    else:
        x_old = x
if not containue:
    print("not converged, increase iteration")

# طريقه للحل بشكل مباشر
a = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])
y = np.array([2, -3, 1])
x = np.linalg.solve(a, y)
print(x)

# ممكن احسب L and U

p, l, u = lu(a)
print("p")
print(p)
print("l")
print(l)
print('u')
print(u)
print(np.dot(p, np.dot(l, u)))  # P L U
