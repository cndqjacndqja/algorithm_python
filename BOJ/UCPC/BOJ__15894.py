n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 4
for i in range(2, n+1):
    dp[i] = dp[i-1]-(i-1)+3+i
print(dp[n])