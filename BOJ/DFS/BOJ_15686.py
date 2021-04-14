from _collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

chick_map = []
house_map = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chick_map.append((i, j))
        elif data[i][j] == 1:
            house_map.append((i, j))

result_data = []
visited = [False for _ in range(len(chick_map))]


def dfs(cnt, idx, param_data):
    if cnt == m:
        cal_solved(param_data)
        return

    for i in range(idx, len(chick_map)):
        if visited[i] == False:
            visited[i] = True
            param_data.append(chick_map[i])
            dfs(cnt + 1, i, param_data)
            param_data.pop()
            visited[i] = False


glo_result = []


def cal_solved(result):
    sum_result = 0
    for i in house_map:
        sum_data = int(1e9)
        for j in result:
            x1, y1 = i
            x2, y2 = j
            sum_data = min(sum_data, (abs(x1 - x2) + abs(y1 - y2)))
        sum_result += sum_data
    glo_result.append(sum_result)

dfs(0, 0, [])
print(min(glo_result))
