from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        pop_x, pop_y, flag = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and visited[nx][ny][flag] == -1:
                    visited[nx][ny][flag] = visited[pop_x][pop_y][flag] + 1
                    q.append((nx, ny, flag))
                elif flag == 0 and data[nx][ny] == 1 and visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[pop_x][pop_y][flag] + 1
                    q.append((nx, ny, 1))

    result1, result2 = visited[n-1][m-1][0], visited[n-1][m-1][1]
    if result1 != -1 and result2 == -1:
        print(result1)
    elif result1 == -1 and result2 != -1:
        print(result2)
    else:
        print(min(result1, result2))
bfs()

