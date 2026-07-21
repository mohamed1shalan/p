from collections import Counter
from sys import stdin


def input():
    return stdin.buffer.readline().decode().rstrip()


MOD = 10**9 + 7

items = int(input())
list1 = list(map(int, input().split()))

count1 = Counter(list1)

number = 0

for value in count1.values():
    number += pow(2, value, MOD) - 1
    number %= MOD

print(number)
