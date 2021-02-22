from _collections import deque

n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def treasure():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'L':
                treasure_long(i, j)


max_cnt = 0

def treasure_long(x, y):
    q = deque()
    global max_cnt
    q.append((x, y))
    treasure_visited = [[0 for _ in range(m)] for _ in range(n)]
    treasure_visited[x][y] = 1
    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and treasure_visited[nx][ny] == 0 and data[nx][ny] == 'L':
                treasure_visited[nx][ny] = treasure_visited[pop_x][pop_y] + 1
                q.append((nx, ny))
                max_cnt = max(max_cnt, treasure_visited[nx][ny] - 1)


treasure()
print(max_cnt)
