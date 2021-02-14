from _collections import deque

n = int(input())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(param_x, param_y):
    q = deque()
    q.append((param_x, param_y))
    global visited
    visited[param_x][param_y] = True
    cnt = 1
    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1 and visited[nx][ny] == False:
                data[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    return cnt


data = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            count = bfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)
