n = int(input())

data = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = data[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < data[j] + dp[i-j]:
            dp[i] = data[j] + dp[i-j]

print(dp[n])
