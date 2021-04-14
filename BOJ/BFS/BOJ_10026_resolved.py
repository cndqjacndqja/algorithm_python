from _collections import deque

n = int(input())
data = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def color_bfs(x, y, color, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and data[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))

    return


def solved():
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                color_bfs(i, j, data[i][j], visited)
                count += 1
    # 색맹 계산
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'G':
                data[i][j] = 'R'

    visited = [[False for _ in range(n)] for _ in range(n)]
    count2 = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                color_bfs(i, j, data[i][j], visited)
                count2 += 1

    print(count, count2)


solved()
