from _collections import deque

n, l, r = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = [[i, j]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])

    return temp


cnt = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum(data[x][y] for x, y in temp) // len(temp)
                    for x, y in temp:
                        data[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)
