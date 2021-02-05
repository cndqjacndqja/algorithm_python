n = int(input())

data = []
dp = [0 for _ in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

for i in range(n):
    if i + data[i][0] - 1 < n:
        index = i + data[i][0] - 1
        if i == 0:
            dp[index] = max(dp[index], dp[0] + data[i][1])
        else:
            dp[index] = max(dp[index], max(dp[0: i]) + data[i][1])



print(max(dp))
