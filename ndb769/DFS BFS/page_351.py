from _collections import deque
import copy

n = int(input())
data = [input().split() for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = False


def wall(x, cnt):
    global result
    if cnt == 3:
        if find_s(data):
            result = True
        return

    for i in range(x, n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                wall(i, cnt + 1)
                data[i][j] = 'X'


def find_s(data_param):
    data_copy = copy.deepcopy(data_param)
    q = deque()

    for i in range(n):
        for j in range(n):
            if data_copy[i][j] == 'T':
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < n and 0 <= ny < n and data_copy[nx][ny] != 'O':
                if data_copy[nx][ny] == 'S':
                    return False
                nx += dx[i]
                ny += dy[i]

    return True


def solved():
    wall(0, 0)
    if result:
        print("YES")
    else:
        print("NO")


solved()
