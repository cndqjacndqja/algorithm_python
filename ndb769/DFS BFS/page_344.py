from _collections import deque

n, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
s, px, py = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    q = deque()
    pos = []
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                pos.append([data[i][j], i, j])

    pos.sort(key=lambda x: x[0])

    for i in pos:
        q.append((i[0], i[1], i[2], 0))

    while q:
        virus, x, y, cnt = q.popleft()

        if cnt < s:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                    data[nx][ny] = virus
                    q.append((virus, nx, ny, cnt + 1))

    print(data[px - 1][py - 1])


bfs()
