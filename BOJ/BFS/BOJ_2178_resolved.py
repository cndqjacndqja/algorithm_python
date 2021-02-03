from _collections import deque

n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and data[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited[n-1][m-1]

print(bfs()+1)
