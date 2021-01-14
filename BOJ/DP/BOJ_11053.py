import copy

n = int(input())

data = list(map(int, input().split()))
dp = [0] * n

if n == 1:
    print(1)
else:
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if data[j] < data[i]:
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
