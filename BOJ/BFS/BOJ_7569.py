from _collections import deque

m, n, h = map(int, input().split())

data = []
for _ in range(h):
    insert_data = []
    for i in range(n):
        insert_data.append(list(map(int, input().split())))
    data.append(insert_data)

dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        pop_x, pop_y, pop_h = q.popleft()
        for i in range(6):
            nx, ny, nh = pop_x + dx[i], pop_y + dy[i], pop_h + dh[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h:
                if data[nh][nx][ny] == 0:
                    data[nh][nx][ny] = data[pop_h][pop_x][pop_y] + 1
                    q.append((nx, ny, nh))


q = deque()

for i in range(h):
    for j in range(n):
        for z in range(m):
            if data[i][j][z] == 1:
                q.append((j, z, i))

bfs()
minus = 1
result = 0
for i in range(h):
    for j in range(n):
        for z in range(m):
            if data[i][j][z] == 0:
                minus = -1
            else:
                result = max(result, data[i][j][z])

if minus == -1:
    print(minus)
else:
    print(result - 1)
