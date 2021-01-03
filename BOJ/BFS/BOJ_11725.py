from _collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
data = [0] * (n+1)

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
for i in graph[1]:
    q.append((i, 1))
    visited[i] = True
visited[1] = True

while q:
    v, parent = q.popleft()

    data[v] = parent
    for i in graph[v]:
        if visited[i] == False:
            q.append((i, v))
            visited[i] = True


for i in range(2, n+1):
    print(data[i])