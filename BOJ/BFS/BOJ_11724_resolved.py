from _collections import deque

n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    push_x, push_y = map(int, input().split())
    data[push_x].append(push_y)
    data[push_y].append(push_x)
visited = [False for _ in range(n + 1)]


def bfs(param_x):
    q = deque()
    q.append(param_x)
    global visited
    visited[param_x] = True

    while q:
        pop_x = q.popleft()
        for i in data[pop_x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


result = 0
for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        bfs(i)

print(result)
