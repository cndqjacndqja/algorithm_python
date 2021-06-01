n = int(input())
data = list(map(int, input().split()))
up_dp = [1 for _ in range(n)]
down_dp = [1 for _ in range(n)]

# 가장 긴 것 먼저 구하자.
for i in range(n):
    for j in range(i+1):
        if data[i] > data[j]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if data[i] > data[j]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)

result = 0
for i in range(n):
    result = max(up_dp[i]+down_dp[i], result)
print(result-1)
