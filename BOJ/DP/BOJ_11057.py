n = int(input())

dp = [[0] * 10 for _ in range(n)]
for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        for z in range(j, 10):
            dp[i][z] += dp[i-1][j]
print(sum(dp[n-1]) % 10007)
