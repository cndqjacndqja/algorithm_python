from _collections import deque

n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)


def bfs(param_index):
    result_cnt = 0
    for i in range(1, n + 1):
        if i == param_index:
            continue

        q = deque()
        q.append((param_index, 0))

        while q:
            pop_data, cnt = q.popleft()
            for item in data[pop_data]:
                if item == i:
                    result_cnt += cnt + 1
                    q.clear()
                    break
                else:
                    q.append((item, cnt + 1))
    return result_cnt

def solved():
    result_visited = [[i] for i in range(n+1)]
    result_visited[0].append(0)
    for i in range(1, n+1):
        result_visited[i].append(bfs(i))
    result_visited.sort(key=lambda x: (x[1], x[0]))
    print(result_visited[1][0])


solved()
