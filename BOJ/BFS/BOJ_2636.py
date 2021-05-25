from _collections import deque
from copy import deepcopy

# 겉 치즈와 아닌 치즈 구분하는 법
# 음,,, 구분을 어떻게 하지... 녹을 치즈와 안녹을 치즈,,,
# 해당 지점이 겉인지 속인지 판단하는 법.
# 움직여서 밖으로 나갈 때, 나갈 수 있으면 속치즈

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 속치즈 겉치즈 판단하는 함수
def judge_ch(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x, y))

    while q:
        pop_x, pop_y = q.popleft()
        if pop_x == n - 1 or pop_x == 0 or pop_y == 0 or pop_y == m - 1:
            return True

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and data[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
    return False


# 한번 녹이기
def melting():
    result = []

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                if judge_ch(i, j):
                    result.append((i, j))

    return result


def count_cheese(copy):
    count = 0
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 1:
                count += 1

    return count


def solved():
    global copy_data
    flag = True
    time = 0

    while flag:
        result = melting()
        if len(result) == 0:
            count = count_cheese(copy_data)
            print(time)
            print(count)
            return
        copy_data = deepcopy(data)
        for i in result:
            x, y = i
            data[x][y] = 0
        time += 1


solved()
