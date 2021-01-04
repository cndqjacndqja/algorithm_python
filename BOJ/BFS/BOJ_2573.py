from _collections import deque
import copy

n, m = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 빙산 체크 bfs
def bfs(data, x, y):
    q = deque()
    q.append((x, y))
    data[x][y] = 0

    while q:
        Px, Py = q.popleft()
        for i in range(4):
            nx, ny = Px + dx[i], Py + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 0:
                q.append((nx, ny))
                data[nx][ny] = 0


def melting(graph):
    graph_melting = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                count = 0
                for z in range(4):
                    nx, ny = i + dx[z], j + dy[z]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        count += 1
                graph_melting[i][j] -= count
    return graph_melting


graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

while True:
    graph_copy = copy.deepcopy(graph)
    count = 0

    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] != 0:
                bfs(graph_copy, i, j)
                count += 1
                break

    if count == 2:
        print(result)
        break

    graph = melting(graph)
    result += 1
