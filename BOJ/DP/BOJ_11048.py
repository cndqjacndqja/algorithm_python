from _collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1, 0, 1], [0, 1, 1]
visited = [[-1 for _ in range(m)] for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = data[0][0]

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(3):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] < visited[pop_x][pop_y] + data[nx][ny]:
                    visited[nx][ny] = visited[pop_x][pop_y] + data[nx][ny]
                    q.append((nx, ny))
    print(visited[n - 1][m - 1])


bfs()
