from _collections import deque

n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]

visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'R':
                rx, ry = i, j
            elif data[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 0))


def move(x, y, dx, dy):
    cnt = 0
    while data[x + dx][y + dy] != '#' and data[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def solve():
    init() # R, B 좌표 찾아서 큐에 저장
    while q: # 큐가 빌 때까지 진행한다.
        rx, ry, bx, by, depth = q.popleft() # 빨간공과 파란공 좌표, 진행 횟수 pop 한다.
        if depth > 10: # 진행 횟수가 10번 넘는다면 -1출력 후 멈추기.
            print(-1)
            break
        for i in range(4): # 네 방향으로 진행
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if data[bx][by] != 'O':
                if data[rx][ry] == 'O':
                    print(depth)
                    return
                elif rx == bx and ry == by:
                    if rcnt > bcnt:
                        nrx -= 1
                        nry -= 1
                    else:
                        nbx -= 1
                        nby -= 1
                if not visited[nrx][nry][nbx][nby]:
                    q.append((nrx, nry, nbx, nby, depth+1))
                    visited[nrx][nry][nbx][nby] = True
solve()

# 궁금증: 1. 뭔가 이렇게 하면 너무 많은 경우의 수를 계산해주는 것 같은데 이런 생각이 왜 들까?
# 아,, 아마도 한쪽 방향으로 벽에 닿은 상태에서도 쭉 진행이 가능해서 그런 느낌이 드나보다.. 하지만 그건 depth>10으로 막아준 거구나.