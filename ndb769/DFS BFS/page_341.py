from _collections import deque
import copy
import time
start = time.time()

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []


def virus_spread(graph):
    graph_copy = copy.deepcopy(graph)
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                cnt += 1
    result.append(cnt)


def wall(x, y, cnt):
    if cnt == 3:
        virus_spread(data)
        return

    for i in range(x, n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(i, j, cnt + 1)
                data[i][j] = 0


def solved():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                wall(i, j, 0)
                print(max(result))
                return


solved()
end = time.time()
print(end-start)