n = int(input())

data = list(map(int, input().split()))
dp_left = [0 for _ in range(n)]
dp_right = [0 for _ in range(n)]

for i in range(n):
    temp = 0
    for j in range(i):
        if data[i] > data[j]:
            temp = max(dp_left[j], temp)
    dp_left[i] = temp+1

for i in range(n-1, -1, -1):
    temp = 0
    for j in range(n-1, i, -1):
        if data[i] > data[j]:
            temp = max(dp_right[j], temp)
    dp_right[i] = temp + 1

dp = [dp_right[i] + dp_left[i]-1 for i in range(n)]
print(max(dp))
