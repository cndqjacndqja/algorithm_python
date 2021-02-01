from _collections import deque
import copy

n, m = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

data = [list(map(int, input().split())) for _ in range(n)]


# 얼음아 녹아라.
def melting():
    data_copy = copy.deepcopy(data)

    for i in range(n):
        for j in range(m):
            if data_copy[i][j] != 0:
                for z in range(4):
                    nx, ny = i + dx[z], j + dy[z]
                    if 0 <= nx < n and 0 <= ny < m and data_copy[nx][ny] == 0:
                        if data[i][j] > 0:
                            data[i][j] -= 1


# 빙산 분리 갯수
def bfs():
    data_copy = copy.deepcopy(data)
    cnt = 0

    for i in range(n):
        for j in range(m):
            if data_copy[i][j] != 0:
                q = deque()
                q.append((i, j))
                cnt += 1

                while q:
                    x, y = q.popleft()

                    for z in range(4):
                        nx, ny = x + dx[z], y + dy[z]
                        if 0 <= nx < n and 0 <= ny < m and data_copy[nx][ny] != 0:
                            data_copy[nx][ny] = 0
                            q.append((nx, ny))

    return cnt


year = 0

while True:
    count = bfs()

    if count == 0:
        print(0)
        break

    if count >= 2:
        print(year)
        break

    melting()
    year+=1
