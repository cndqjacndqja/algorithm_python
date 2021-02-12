n = int(input())
data = [0] + list(map(int, input().split()))
dp = [i for i in data]

for i in range(1, n+1):
    for j in range(i//2+1):
        dp[i] = max(dp[j]+dp[i-j], dp[i])

print(max(dp))