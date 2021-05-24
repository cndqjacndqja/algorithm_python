from _collections import deque

n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 물 퍼지기
def water_spread():
    stack = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == '*':
                stack.append((i, j))

    for s in stack:
        x, y = s
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == '.':
                data[nx][ny] = '*'


# 고슴도치 움직이기
def bfs():
    stack = []
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'S':
                stack.append((i, j))

    for s in stack:
        x, y = s
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == '.':
                    data[nx][ny] = 'S'
                    count += 1
                elif data[nx][ny] == 'D':
                    data[nx][ny] = 'S'
                    count += 1
    return count


def solved():
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'D':
                x, y = i, j

    flag = True
    result = 0
    while flag:
        water_spread()
        result += 1
        count = bfs()
        if count == 0:
            print("KAKTUS")
            return
        if data[x][y] == 'S':
            print(result)
            return
solved()