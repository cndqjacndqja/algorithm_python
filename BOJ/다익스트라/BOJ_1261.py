from _collections import deque

m, n = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
    distance[0][0] = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if data[nx][ny] == 1:
                    distance[nx][ny] = distance[pop_x][pop_y] + 1
                    q.append((nx, ny))
                else:
                    distance[nx][ny] = distance[pop_x][pop_y]
                    q.appendleft((nx, ny))
                visited[nx][ny] = True
    print(distance[n - 1][m - 1])


bfs()
