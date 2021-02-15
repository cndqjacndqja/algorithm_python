import sys
from _collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 번호 매기기
def bfs_number(param_x, param_y, number):
    q = deque()
    q.append((param_x, param_y))
    visited_number = [[False for _ in range(n)] for _ in range(n)]
    data[param_x][param_y] = number
    visited_number[param_x][param_y] = True

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1 and visited_number[nx][ny] == False:
                q.append((nx, ny))
                visited_number[nx][ny] = True
                data[nx][ny] = number


# 최단 다리 찾기
def bfs_short(param_list, number):
    q = deque()
    visited_short = [[0 for _ in range(n)] for _ in range(n)]

    # number에서 0인거 다 추가.
    for i in param_list:
        param_x, param_y = i
        q.append((param_x, param_y))
        visited_short[param_x][param_y] = 1

        for j in range(4):
            param_nx, param_ny = param_x + dx[j], param_y + dy[j]
            if 0 <= param_nx < n and 0 <= param_ny < n and data[param_nx][param_ny] == number and visited_short[param_nx][param_ny] == 0:
                q.append((param_nx, param_ny))
                visited_short[param_nx][param_ny] = 1

    result = sys.maxsize
    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != number and visited_short[nx][ny] == 0:
                if data[nx][ny] != 0:
                    visited_short[nx][ny] = visited_short[pop_x][pop_y] + 1
                    result = min(visited_short[pop_x][pop_y] + 1, result)
                    return result-1
                else:
                    q.append((nx, ny))
                    visited_short[nx][ny] = visited_short[pop_x][pop_y] + 1
    return result

num = 1
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            num += 1
            bfs_number(i, j, num)


result_sum = sys.maxsize
for z in range(2, num+1):
    add_list = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == z:
                add_list.append((i, j))
    result_sum = min(bfs_short(add_list, z), result_sum)

print(result_sum-1)
