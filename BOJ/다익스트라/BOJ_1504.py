from heapq import heappush, heappop

n, e = map(int, input().split())
data = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

INF = int(1e9)
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    q = []
    heappush(q, (0, start))
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue

        for i in data[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                heappush(q, (cost, i[0]))
                distance[i[0]] = cost

    return distance[end]


def solved():
    result = 0
    v1_distance = dijkstra(1, v1)
    v2_distance = dijkstra(v1, v2)
    n_distance = dijkstra(v2, n)
    result = v1_distance + v2_distance + n_distance

    v1_distance = dijkstra(1, v2)
    v2_distance = dijkstra(v2, v1)
    n_distance = dijkstra(v1, n)
    result = min(v1_distance + v2_distance + n_distance, result)

    if result >= INF:
        print(-1)
    else:
        print(result)


solved()
