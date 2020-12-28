from _collections import deque

n, m = map(int, input().split(" "))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split(" "))
    graph[x].append(y)

q = deque()
visited = [0] * (n + 1)
count = 0

for i in range(1, n):
    if visited[i] == 0:
        q.append(i)
        count += 1

        while q:
            v = q.popleft()
            visited[v] = 1

            for j in graph[v]:
                if visited[j] == 0:
                    q.append(j)

print(count)
