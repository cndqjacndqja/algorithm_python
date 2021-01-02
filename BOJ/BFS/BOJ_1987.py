n, m = map(int, input().split(" "))

graph = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
phase = [1] * 26

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

phase.append(graph[0][0])

result_count = 0


def dfs(data, x, y, cnt):
    global result_count
    result_count = max(result_count, cnt)
    phase[data[x][y]] = 0
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m and phase[data[new_x][new_y]] == 1:
            phase[data[new_x][new_y]] = 0
            dfs(data, new_x, new_y, cnt + 1)
            phase[data[new_x][new_y]] = 1


dfs(graph, 0, 0, 1)
print(result_count)
