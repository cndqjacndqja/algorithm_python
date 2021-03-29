from _collections import deque

INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    q = deque()
    visited = [[INF for _ in range(n)] for _ in range(n)]
    visited[0][0] = data[0][0]
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > visited[x][y] + data[nx][ny]:
                visited[nx][ny] = min(visited[nx][ny], visited[x][y] + data[nx][ny])
                q.append((nx, ny))

    print(visited[n-1][n-1])