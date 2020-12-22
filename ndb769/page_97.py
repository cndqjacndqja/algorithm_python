import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

result = 0
for _ in range(b):
    data = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    item = min(data)

    result = max(result, item)

print(result)