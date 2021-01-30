from _collections import deque

n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    cnt = 0

    while q:
        rqx, rqy, bqx, bqy = q.popleft()

        for i in range(4):
            nrx, nry, nbx, nby = rqx + dx[i], rqy + dy[i], bqx + dx[i], bqy + dy[i]
            if 0 < nrx < m - 1 and 0 < nry < m - 1 and 0 < nbx < m - 1 and 0 < nby < m - 1:
                if visited[nrx][nry] == 0 and data[nrx][nry] == ".":
                    q.append((nrx, nry, nbx, nby))
                    
