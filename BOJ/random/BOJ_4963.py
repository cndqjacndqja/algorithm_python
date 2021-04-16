from _collections import deque

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(x, y):
    data[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        vx, xy = q.popleft()
        for z in range(8):
            nx, ny = vx + dx[z], xy + dy[z]
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 1:
                data[nx][ny] = 0
                q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    data = []
    count = 0
    for _ in range(h):
        insert_data = list(map(int, input().split()))
        data.append(insert_data)
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
