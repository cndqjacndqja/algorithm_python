from _collections import deque
import copy

n, m = map(int, input().split())
dx, dy = [0, 1], [1, 0]

data = []
for _ in range(m):
    data.append(list(map(int, input().split())))


def bfs():
    q = deque()
    q.append((0, 0))
    copy_data = copy.deepcopy(data)

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(2):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if copy_data[pop_x][pop_y]+data[nx][ny] > copy_data[nx][ny]:
                    copy_data[nx][ny] = copy_data[pop_x][pop_y]+data[nx][ny]
                    q.append((nx, ny))

    print(copy_data[m-1][n-1])

bfs()
