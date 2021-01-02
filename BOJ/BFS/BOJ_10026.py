from _collections import deque
import copy

n = int(input())

graph = [list(input()) for _ in range(n)]
graph2 = copy.deepcopy(graph)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = []


def dfs(data, x, y, char1):
    q = deque()
    q.append((x, y))

    data[x][y] = ' '
    while q:
        Qx, Qy = q.popleft()
        for i in range(4):
            nx, ny = Qx + dx[i], Qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == char1:
                data[nx][ny] = ' '
                q.append((nx, ny))


def dfs2(data, x, y, char1):
    q = deque()
    q.append((x, y))

    data[x][y] = ' '
    while q:
        Qx, Qy = q.popleft()
        for i in range(4):
            nx, ny = Qx + dx[i], Qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 'R' or data[nx][ny] == 'G':
                    if char1 == 'R' or char1 == 'G':
                        data[nx][ny] = ' '
                        q.append((nx, ny))
                elif char1 == 'B' and data[nx][ny] == char1:
                    data[nx][ny] = ' '
                    q.append((nx, ny))


count = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != ' ':
            dfs(graph, i, j, graph[i][j])
            count += 1
        if graph2[i][j] != ' ':
            dfs2(graph2, i, j, graph2[i][j])
            count2 += 1

print(count, count2)
