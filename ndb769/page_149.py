n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x < 1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True