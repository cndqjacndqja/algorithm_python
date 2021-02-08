from _collections import deque

n, m, k, x = map(int, input().split())
data = [[] for _ in range(n + 1)]
for i in range(m):
    dx, dy = map(int, input().split())
    data[dx].append(dy)

result = []


def dfs(k_data, x_data):
    visited = [False for _ in range(n + 1)]
    visited[x_data] = True
    s = deque()
    global result
    cnt = 0
    s.append((x_data, cnt))
    while s:
        town, count = s.pop()
        if count == k:
            result.append(town)
        elif count < k:
            for con in data[town]:
                if not visited[con]:
                    visited[con] = True
                    s.append((con, count +1))



dfs(k, x)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
