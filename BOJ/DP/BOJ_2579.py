n = int(input())

data = [0] * 301
dp = [0] * 301

for i in range(1, n + 1):
    data[i] = int(input())

dp[1] = data[1]
dp[2] = data[1] + data[2]
dp[3] = max(data[1], data[2]) + data[3]

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + data[i - 1] + data[i], dp[i - 2] + data[i])

print(dp[n])
