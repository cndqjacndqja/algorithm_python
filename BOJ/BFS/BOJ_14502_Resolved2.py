import copy
from _collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 1. 벽 세우기,  바이러스 퍼뜨리기, 갯수 세기
# 바이러스 퍼뜨리기.
def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                q.append((i, j))

    copy_data = copy.deepcopy(data)
    while q:
        spread_x, spread_y = q.popleft()

        for i in range(4):
            nx, ny = spread_x + dx[i], spread_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copy_data[nx][ny] == 0:
                copy_data[nx][ny] = 2
                q.append((nx, ny))
    global result
    result = max(result, virus_count(copy_data))


def virus_count(param_data):
    copy_data = copy.deepcopy(param_data)
    count = 0
    for i in range(n):
        for j in range(m):
            if copy_data[i][j] == 0:
                count += 1
    return count


# 메인에서 이제 벽 세우고 바아러스 퍼뜨린 후, 카운트 세기

result = 0


def wall(x):
    if x == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(x + 1)
                data[i][j] = 0




# 궁금증: wall()이 재귀함수로 return 을하는데 그럼 return한번만 받으면 여러개의 값이 돌아오나?
wall(0)
print(result)