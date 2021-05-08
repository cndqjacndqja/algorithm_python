from heapq import heappush, heappop
INF = int(1e9)


def solution(n, start, end, roads, traps):
    data = [[] for _ in range(n+1)]
    for i in roads:
        a, b, c = i
        data[a].append((b, c))


def dijkstra(start, end, n, data):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    q = []
    heappush(q, (0, start))

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

