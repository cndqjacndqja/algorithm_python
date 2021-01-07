n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dp_visited = [[0] * n for _ in range(n)]

result = 0


def dfs(graph, x, y):
    if dp_visited[x][y]:
        return dp_visited[x][y]

    dp_visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp_visited[x][y] = max(dp_visited[x][y], dfs(graph, nx, ny) + 1)
    return dp_visited[x][y]


for i in range(n):
    for j in range(n):
        result = max(result, dfs(graph, i, j))

print(result)
