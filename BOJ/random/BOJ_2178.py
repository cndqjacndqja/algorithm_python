from collections import deque

n, m = map(int, input().split(" "))

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
graph[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(graph[x][y])
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((x + dx[i], y + dy[i]))
