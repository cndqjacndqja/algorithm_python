import sys

sys.setrecursionlimit(100000)

r, c = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

alpha = [1 for _ in range(26)]
data = [list(input()) for _ in range(r)]
result = 0


def dfs(x, y, ch, count):
    global result
    global alpha
    if alpha[ord(ch) - 65] == 0:
        result = max(result, count)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alpha[ord(data[x][y]) - 65] == 1:
            alpha[ord(data[x][y]) - 65] -= 1
            dfs(nx, ny, data[nx][ny], count + 1)
            alpha[ord(data[x][y]) - 65] += 1


dfs(0, 0, data[0][0], 0)
print(result)
