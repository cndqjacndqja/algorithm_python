n, k = map(int, input().split())
dp = [int(1e9) for _ in range(k + 1)]
dp[0] = 0
data = []
for _ in range(n):
    data.append(int(input()))

for c in data:
    for i in range(1, k+1):
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] >= int(1e9):
    print(-1)
else:
    print(dp[k])