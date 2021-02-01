import copy
from _collections import deque

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0


def bfs():
    q = deque()
    global result

    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                q.append((i, j))

    spread_data = copy.deepcopy(data)

    while q:
        spread_x, spread_y = q.popleft()

        for i in range(4):
            nx, ny = spread_x + dx[i], spread_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if spread_data[nx][ny] == 0:
                    spread_data[nx][ny] = 2
                    q.append((nx, ny))

    sum = 0
    for i in spread_data:
        sum += i.count(0)

    result = max(result, sum)


def build_wall(x):
    if x == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                build_wall(x + 1)
                data[i][j] = 0


build_wall(0)
print(result)
