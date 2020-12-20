import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

test = ""

for i in range(n-1, -1, -1):
    test += str(a[i]) + " "

print(test)

