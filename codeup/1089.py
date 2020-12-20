import sys

a, d, n = map(int, sys.stdin.readline().rstrip().split(" "))

for i in range(n):
    a += d

print(a)