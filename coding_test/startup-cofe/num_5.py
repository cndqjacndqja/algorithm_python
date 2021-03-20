from _collections import deque

n, m = map(int, input().split())
dx, dy = [1, 0, 0], [0, -1, 1]
data = []
for _ in range(m):
    data.append(list(input()))


def bfs():
    start_point = []
    result = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == 'c':
                start_point.append([i, j])

    for i in start_point:
        q = deque()
        q.append((i[0], i[1], 0))
        visited = [[0 for _ in range(n)] for _ in range(m)]

        while q:
            pop_x, pop_y, count = q.popleft()

            if pop_x == m-1:
                result.append(count)
                break

            for i in range(3):
                nx, ny = pop_x + dx[i], pop_y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[pop_x][pop_y] + 1
                    if i == 1 or i == 2:
                        q.append((nx, ny, count + 1))
                    else:
                        q.append((nx, ny, count))

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        print(result[0])

bfs()