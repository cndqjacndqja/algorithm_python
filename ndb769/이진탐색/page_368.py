from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))


def binary_search(a, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if a[mid] == mid:
        return mid
    elif a[mid] > mid:
        return binary_search(a, start, mid-1)
    elif a[mid] < mid:
        return binary_search(a, mid+1, end)


print(binary_search(data, 0, n-1))