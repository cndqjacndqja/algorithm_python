n = int(input())
data = []
dp = [0 for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))


num = 0
for i in range(n):
    num = max(num, dp[i])
    if i + data[i][0] > n:
        continue
    dp[i+data[i][0]] = max(num+data[i][1], dp[i+data[i][0]])

print(max(dp))