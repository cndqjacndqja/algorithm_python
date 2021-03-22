n = int(input())
data = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] < data[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(n-max(dp))
