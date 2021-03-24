import heapq

INF = 1e9
n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))


def dijkstra():
    start = int(input())
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in data[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
