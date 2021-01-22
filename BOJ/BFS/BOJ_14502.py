from _collections import deque

n, m = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


def spread(graph, x, y):
    q = deque()
    q.append((x, y))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    while q:
        x_pop, y_pop = q.popleft()
        for i in range(4):
            x_idx, y_idx = x_pop + dx[i], y_pop + dy[i]
            if 0 <= x_idx < n and 0 <= y_idx < m and visited[x_idx][y_idx] == False:
                if graph[x_idx][y_idx] == 0:
                    graph[x_idx][y_idx] = 2
                    visited[x_idx][y_idx] = True
                    q.append(x_idx, y_idx)


def count(graph, x, y):
    q = deque()
    q.append((x, y))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    count = 0
    while q:
        x_pop, y_pop = q.popleft()
        count += 1
        for i in range(4):
            x_idx, y_idx = x_pop + dx[i], y_pop + dy[i]
            if 0 <= x_idx < n and 0 <= y_idx < m and visited[x_idx][y_idx] == False:
                if graph[x_idx][y_idx] == 0:
                    graph[x_idx][y_idx] = 2
                    visited[x_idx][y_idx] = True
                    q.append(x_idx, y_idx)
    return count


for i in range(n):
    for j in range(m):
        data_copy = [i for i in data]
        if data_copy[i][j] == 0: