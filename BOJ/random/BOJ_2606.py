n = int(input())

graph = [[] * _ for _ in range(n + 1)]

m = int(input())

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False] * (n + 1)


def dfs(graph, start):
    global count
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            count += 1
            dfs(graph, i)


dfs(graph, 1)
print(count)
