from _collections import deque

n, m = map(int, input().split())
data = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input())))

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y])
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and data[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


bfs()
