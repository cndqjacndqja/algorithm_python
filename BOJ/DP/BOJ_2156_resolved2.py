n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))
dp = [0 for _ in range(10001)]
if n >= 1:
    dp[1] = data[1]
if n >= 2:
    dp[2] = data[1] + data[2]
if n >= 3:
    dp[3] = max(data[1] + data[3], data[2] + data[3], data[1] + data[2])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + data[i - 1] + data[i], dp[i - 2] + data[i], dp[i - 1])

print(dp[n])
