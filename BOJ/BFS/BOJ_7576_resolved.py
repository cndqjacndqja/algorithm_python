from _collections import deque

m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(param_list):
    q = deque()
    global visited
    for i in param_list:
        x, y = i
        visited[x][y] = 1
        q.append(i)

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                data[nx][ny] = 1
                visited[nx][ny] = visited[pop_x][pop_y] + 1
tomato_list = []
result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            tomato_list.append((i, j))

bfs(tomato_list)
# 안 익은거 판별


#가장 큰 값 구하는 것.
for i in range(n):
    result = max(result, max(visited[i]))
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result = -1
if result == -1:
    print(result)
else:
    print(result-1)
