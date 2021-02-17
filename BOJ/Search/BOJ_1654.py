k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

start, end = 1, max(data)
result = 0
while start <= end:
    mid = (start+end) // 2
    count = sum([(i // mid) for i in data])
    if count >= n:
        result = mid
        start = mid+1
    elif count < n:
        end = mid -1

print(result)