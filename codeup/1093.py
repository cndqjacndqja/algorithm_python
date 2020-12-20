import sys
import random

a = [0] * 24

n = int(sys.stdin.readline().rstrip())

data = map(int, sys.stdin.readline().rstrip().split(" "))

for i in data:
    a[i] += 1

test = ""

for i in range(1, 24):
    test += str(a[i])+" "

print(test)
