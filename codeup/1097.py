import sys

a = [[0] * 19 for _ in range(19)]


for i in range(19):
    x = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(19):
        a[i][j] = x[j]

n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split(" "))
    for j in range(19):
        if a[x-1][j] == 0:
            a[x - 1][j] = 1
        elif a[x-1][j] == 1:
            a[x - 1][j] = 0
        else:
            a[x - 1][j] = 0
        for c in range(19):
            if a[c][y-1] == 0:
                a[c][y-1] = 1
            elif a[c][y-1] == 1:
                a[c][y-1] = 0
            else:
                a[c][y-1] = 0

test = ""

for i in range(19):
    for j in range(19):
        test += str(a[i][j]) + " "
    test += "\n"

print(test)
