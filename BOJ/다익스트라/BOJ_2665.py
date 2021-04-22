from heapq import heappush, heappop

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dijkstra():
    q = []
    heappush(q, (0, 0, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]

    while q:
        cnt, x, y = heappop(q)

        if x == n - 1 and y == n - 1:
            print(cnt)
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if data[nx][ny] == 0:
                    heappush(q, (cnt + 1, nx, ny))
                else:
                    heappush(q, (cnt, nx, ny))
                visited[nx][ny] = True


dijkstra()
