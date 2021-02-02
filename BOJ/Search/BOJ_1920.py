import sys

n = int(input())

data1 = sorted(list(map(int, sys.stdin.readline().split())))

m = int(input())
data2 = list(map(int, sys.stdin.readline().split()))


def binary_search(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2

    if data1[mid] == target:
        return 1
    elif data1[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)


for i in data2:
    print(binary_search(0, len(data1)-1, i))
