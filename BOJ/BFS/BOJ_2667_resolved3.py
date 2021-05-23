from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    count = 1
    q.append((x, y))
    visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and data[nx][ny] == 1:
                visited[nx][ny] = True
                data[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count


n = int(input())
data = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

result_count = 0
result = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            result.append(bfs(i, j))
            result_count += 1

print(result_count)
result.sort()
for i in result:
    print(i)
