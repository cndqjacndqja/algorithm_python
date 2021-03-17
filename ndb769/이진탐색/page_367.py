from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

data = list(map(int, input().split()))


def count_by_range(a, left_value, right_value):
    left = bisect_left(a, left_value, right_value)
    right = bisect_right(a, left_value, right_value)
    return right - left

print(count_by_range(data, x, x))