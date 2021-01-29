from _collections import deque

n, m = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

data = [list(map(int, input())) for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0, 0))

    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while q:
        x, y, item = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1][item]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1 and item == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif data[nx][ny] == 0 and visited[nx][ny][item] == 0:
                    visited[nx][ny][item] = visited[x][y][item] + 1
                    q.append((nx, ny, item))
    return -1


print(bfs())
