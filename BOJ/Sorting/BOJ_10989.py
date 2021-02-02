import sys

n = int(sys.stdin.readline())

result = [0 for _ in range(10001)]
for _ in range(n):
    result[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)