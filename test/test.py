from _collections import deque

n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

queue = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'R':
                rx, ry = i, j
            elif data[i][j] == 'B':
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True


def move(x, y, pram_dx, param_dy):
    cnt = 0
    while data[x + pram_dx][y + param_dy] != '#' and data[x][y] != 'O':
        x += pram_dx
        y += param_dy
        cnt += 1
    return x, y, cnt


def solve():
    pos_init()
    while queue:
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if data[nbx][nby] != 'O':
                if data[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))

    print(-1)


solve()
