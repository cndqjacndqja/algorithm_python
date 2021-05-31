from math import sqrt

n = int(input())
dp = [0 for _ in range(100000)]
dp[1] = 1

for i in range(n+1):
    dp[i] = i
    for j in range(i):
        if j*j > i:
            break
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])