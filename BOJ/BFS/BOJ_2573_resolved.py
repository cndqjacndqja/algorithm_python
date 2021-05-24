from copy import deepcopy
from _collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 녹이기
def melting():
    stack = []

    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                for z in range(4):
                    nx, ny = i + dx[z], j + dy[z]
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                        stack.append((i, j))

    for i in stack:
        x, y = i
        if data[x][y] > 0:
            data[x][y] -= 1


# 몇 개인지 판단하기.
def bfs_count():
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0 and not visited[i][j]:
                bfs(visited, i, j)
                count += 1

    return count


def bfs(visited, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and data[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))


def solved():
    flag = True
    result = 0
    while flag:
        count = bfs_count()
        if count > 1:
            print(result)
            return
        if count == 0:
            print(0)
            return
        melting()
        result += 1

solved()