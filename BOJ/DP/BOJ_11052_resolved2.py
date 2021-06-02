n = int(input())
data = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
for i in range(n):
    for j in range(n + 1):
        idx = j - (i + 1)
        if idx >= 0:
            dp[j] = max(dp[idx] + data[i], dp[j])
print(dp[n])
