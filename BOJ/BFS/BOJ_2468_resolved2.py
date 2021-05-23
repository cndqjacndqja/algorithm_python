from _collections import deque
from copy import deepcopy

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
high_max = 0
for i in range(n):
    high_max = max(max(data[i]), high_max)


# 퍼뜨리기만 하자. 갯수 세어주는거
def bfs(x, y, map, high):
    q = deque()
    q.append((x, y))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and map[nx][ny] > high:
                map[nx][ny] = -1
                q.append((nx, ny))


def solved():
    result = []
    for h in range(high_max+1):
        deep_copy = deepcopy(data)

        count = 0
        for i in range(n):
            for j in range(n):
                if deep_copy[i][j] > h:
                    bfs(i, j, deep_copy, h)
                    count += 1

        result.append(count)
    print(max(result))


solved()
