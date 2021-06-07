n = int(input())
data = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > data[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
print(result)
