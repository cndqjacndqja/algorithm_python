from _collections import deque

n, m, k = map(int, input().split(" "))

graph = [[1] * m for _ in range(n)]
k_graph = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(k):
    k_graph.append(list(map(int, input().split(" "))))

for k_data in k_graph:
    for i in range(k_data[1], k_data[3]):
        for j in range(k_data[0], k_data[2]):
            graph[i][j] = 0


def dfs(data, x, y):
    q = deque()
    q.append((x, y))
    data[x][y] = 0
    count = 1
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                data[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count


result = []
case_count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(dfs(graph, i, j))
            case_count += 1

result.sort()
print(case_count)
for i in range(len(result)):
    print(result[i], end=' ')
