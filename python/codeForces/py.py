# # A. Helpful Maths
# import numpy as np
# import pandas as pd
# x = list(map(int, input().split('+')))
# x.sort()
# print('+'.join(map(str,x)))
# -------------------------------------------------------
# # A. Beautiful Matrix
# x = list()
# for i in range(5):
#     x.append(list(map(int, input().split())))
# x1, y1 = 0, 0
# for i in range(5):
#     for j in range(5):
#         if x[i][j] == 1:
#             x1, y1 = i, j
#             break

# print((abs(2 - x1) + abs(2 - y1)))

# -------------------------------------------------------
# Codeforces 266A – Stones on the Table
# n = int(input())
# x = input()
# count = 0
# for i in range(n-1):
#     if x[i] == x[i+1]:
#         count += 1
# print(count)
# -------------------------------------------------------
# # Codeforces 144A – Arrival of the General
# n = int(input())
# list1 = list(map(int, input().split()))
# max1 = max(list1)
# min1 = min(list1)
# max_index = list1.index(max1)
# min_index = list1[::-1].index(min1)
# print(max_index + min_index if (max_index + min_index)
#       < n else max_index + min_index - 1)

# -------------------------------------------------------
# Codeforces 580A – Kefa and First Steps
# n = int(input())
# arr = list(map(int, input().split()))

# current = 1
# answer = 1

# for i in range(1, n):
#     if arr[i] >= arr[i-1]:
#         current += 1
#     else:
#         current = 1
#     answer = max(answer, current)

# print(answer)
# -------------------------------------------------------
# Codeforces 476A – Dreamoon and Stairs
# import math
# n, m = map(int, input().split())

# if n == 0 or m == 0 or n < m:
#     print(-1)
# elif n == m:
#     print(m)
# else:
#     for i in range(math.ceil(n/2), n+1):
#         if i % m == 0:
#             print(i)
#             break
