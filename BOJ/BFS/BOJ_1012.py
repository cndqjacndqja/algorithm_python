from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    q = deque()

    q.append((x, y))
    visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and data[nx][ny] == 1:
                visited[nx][ny] = True
                data[nx][ny] = 0
                q.append((nx, ny))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    data = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        b, a = map(int, input().split())
        data[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
