from _collections import deque

n = int(input())
q1, q2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start, target):
    q = deque()
    count = 0
    q.append((start, count))
    while q:
        v, count = q.popleft()

        if v == target:
            return count

        if visited[v] == False:
            visited[v] = True
            for i in graph[v]:
                q.append((i, count+1))
    return -1


print(dfs(q1, q2))
