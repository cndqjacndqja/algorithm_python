m,n = map(int, input().split())
data = list(map(int, input().split()))
start = 1
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in data:
        sum = i - mid
        if sum >= 0:
            count += sum

    if count >= n:
        start = mid + 1
        if mid > result:
            result = mid
    elif count < n:
        end = mid - 1
    elif count > n:
        start = mid + 1

print(result)
