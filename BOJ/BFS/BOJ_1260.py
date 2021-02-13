from _collections import deque

n, m, v = map(int, input().split())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

for i in range(1, n + 1):
    data[i].sort()


def bfs(param_v):
    q = deque()
    q.append(param_v)
    visited = [False for _ in range(n + 1)]
    visited[param_v] = True
    while q:
        pop_x = q.popleft()
        print(pop_x, end=' ')

        for i in data[pop_x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs_visited = [False for _ in range(n + 1)]


def dfs(param_v, visited):
    q = deque()
    q.append(param_v)
    visited[param_v] = True
    print(param_v, end=' ')
    for i in data[param_v]:
        if not visited[i]:
            dfs(i, visited)


dfs(v, dfs_visited)
print()
bfs(v)
