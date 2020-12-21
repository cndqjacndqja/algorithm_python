import sys

data = [[0] * 19 for _ in range(19)]

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    data[a-1][b-1] = 1


test = ""

for i in range(19):
    for j in range(19):
        test += str(data[i][j]) + " "
    test += "\n"

print(test)

