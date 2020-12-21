import sys

n = input()

a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(min(a))

