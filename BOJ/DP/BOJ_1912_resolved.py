n = int(input())

data = [0] + list(map(int, input().split()))

dp = [-1000] * (n+1)

dp[1] = data[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+data[i], data[i])

print(max(dp))
