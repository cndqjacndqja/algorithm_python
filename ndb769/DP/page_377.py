n = int(input())
data = []
dp = [0 for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))


for i in range(n-1, 0, -1):
    day, pay = data[i][0], data[i][1]
    if i+day-1 < n:
        if sum(dp[i:i+day]) < pay:
            dp[i+day-1] = pay
