INF = 1e9
n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))


def small_index():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra():
    start = int(input())
    distance[start] = 0
    visited[start] = True

    for i in data[start]:
        distance[i[0]] = i[1]

    for _ in range(n - 1):
        now = small_index()
        visited[now] = True
        for i in data[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost


dijkstra()
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
