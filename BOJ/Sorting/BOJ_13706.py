
n = int(input())
low, high = 1, n
while 1:
    mid = (low+high) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        high = mid -1
    else:
        low = mid + 1