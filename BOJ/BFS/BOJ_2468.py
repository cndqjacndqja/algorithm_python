from _collections import deque
import copy

n = int(input())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

data = []
for _ in range(n):
    data.append(list(map(int, input().split(" "))))


# 이미 0과 1로 구분되어 있고, 1일때마다 돌리기.
def dfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        qx, qy = q.popleft()
        for a in range(4):
            if 0 <= qx + dx[a] < n and 0 <= qy + dy[a] < n and graph[qx + dx[a]][qy + dy[a]] == 1:
                graph[qx + dx[a]][qy + dy[a]] = 0
                q.append((qx + dx[a], qy + dy[a]))


def initial_data(graph, h):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                graph[i][j] = 0
            else:
                graph[i][j] = 1


max_num = max(map(max, data))
result = []

for i in range(max_num + 1):
    demo_data = copy.deepcopy(data)
    initial_data(demo_data, i)

    count = 0
    for z in range(n):
        for x in range(n):
            if demo_data[z][x] == 1:
                dfs(demo_data, z, x)
                count += 1
    result.append(count)

print(max(result))
