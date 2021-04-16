from collections import deque

n, m = map(int, input().split(" "))

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split(" "))))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(graph, data):
    queue = deque()

    count = 0
    for z in graph:
        if 0 in z:
            count += 1
    if count == 0:
        print(0)
        return

    for z in data:
        queue.append(z)
        x, y = z
        graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    for z in graph:
        if 0 in z:
            print(-1)
            return

    maxNum = max(map(max, graph))

    if maxNum == 0:
        print(0)
        return
    print(maxNum)


data = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            data.append((i, j))

dfs(graph, data)
