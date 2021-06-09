import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dx, dy = [1, 0, 0], [0, -1, 1]

dp = [[0 for _ in range(m)] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
result = 0

visited[0][0] = True
def dfs(x, y):
    global result
    if x == n - 1 and y == m - 1:
        result = max(dp[x][y], result)

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if dp[nx][ny] < dp[x][y] + data[nx][ny]:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + data[nx][ny])
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False

def dfs2(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = data[x][y]
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs2(nx, ny) + data[nx][ny])
    return dp[x][y]


# 아 이걸 우찌하지...
# 재귀로 일단 쭉쭉 가는데, 갈 때 이미 간 곳이면 가지 않는다.
# 또한 dp에 값을 저장하게 되는데, dp[nx][ny] < dp[x][y] + data[nx][ny]이면 더하지 ㅇ낳는다.

dfs2(0, 0)
print(dp)
print(result)

