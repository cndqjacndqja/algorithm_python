import heapq

v, e = map(int, input().split())
INF = int(1e9)
k = int(input())

data = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    data[a].append((c, b))
visited = [INF for _ in range(v + 1)]


def dijkstra():
    q = []
    visited[k] = 0
    heapq.heappush(q, (0, k))

    while q:
        dis, node = heapq.heappop(q)

        if visited[node] < dis:
            continue
        for i in data[node]:
            cost = dis + i[0]
            if cost < visited[i[1]]:
                visited[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    for i in range(1, len(visited)):
        if visited[i] == INF:
            print("INF")
        else:
            print(visited[i])

dijkstra()
