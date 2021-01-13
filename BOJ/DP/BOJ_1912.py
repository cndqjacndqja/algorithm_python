n = int(input())

data = list(map(int, input().split()))
data.insert(0, 0)

dp = [-1000]
dp.append(data[1])

for i in range(2, n+1):
    dp.append(max(dp[i-1] + data[i], data[i]))

print(max(dp))
