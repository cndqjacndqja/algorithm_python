from _collections import deque
from copy import deepcopy

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

wall_result = []


# 바이러스 퍼뜨리기
def bfs(deep_copy):
    map = deepcopy(deep_copy)
    q = deque()
    virus = find_virus(map)
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in virus:
        x, y = i
        q.append((x, y))
        visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map[nx][ny] == 0:
                visited[nx][ny] = True
                map[nx][ny] = 2
                q.append((nx, ny))
    func_count(map)


def func_count(deep_copy):
    sum = 0
    for i in range(n):
        for j in range(m):
            if deep_copy[i][j] == 0:
                sum += 1
    result.append(sum)


# 벽세우기
def wall_dfs(deep_copy, cnt, pram_x):
    if cnt == 3:
        bfs(deep_copy)
        return

    for i in range(pram_x, n):
        for j in range(m):
            if deep_copy[i][j] == 0:
                deep_copy[i][j] = 1
                wall_dfs(deep_copy, cnt + 1, i)
                deep_copy[i][j] = 0


def find_virus(deep_copy):
    virus = []
    for i in range(n):
        for j in range(m):
            if deep_copy[i][j] == 2:
                virus.append((i, j))

    return virus


def solved():
    wall_dfs(data, 0, 0)
    print(max(result))


solved()
