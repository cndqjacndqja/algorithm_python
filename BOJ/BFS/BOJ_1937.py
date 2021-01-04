n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]

result = 0
def dfs(graph, x, y, count):
    visited[x][y] = True
    global result
    result = max(result, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            
