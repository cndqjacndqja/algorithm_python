from _collections import deque


def see(graph):
    print()
    for i in graph:
        print(i)


t = int(input())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(t):
    n, m, k = map(int, input().split(" "))
    count = 0
    graph = [[0] * n for _ in range(m)]
    q = deque()

    for _ in range(k):
        y, x = map(int, input().split(" "))
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                q.append((i, j))
                count += 1
                while q:
                    vx, vy = q.popleft()
                    if graph[vx][vy] == 1:
                        graph[vx][vy] = 0

                        for z in range(4):
                            nx, ny = vx + dx[z], vy + dy[z]
                            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                                q.append((nx, ny))

    print(count)
