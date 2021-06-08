from heapq import heappush, heappop

n, e = map(int, input().split())
INF = int(1e9)
data = [[] for _ in range(n + 1)]


for _ in range(e):
    a, b, c = map(int, input().split())
    data[a].append((c, b))
    data[b].append((c, a))


def dijkstra(start, end):
    distance = [INF for _ in range(n + 1)]

    distance[start] = 0
    q = [(0, start)]

    while q:
        dis, node = heappop(q)

        if distance[node] < dis:
            continue
        for i in data[node]:
            pop_dis, pop_node = i
            cost = dis + pop_dis
            if distance[pop_node] > cost:
                distance[pop_node] = cost
                heappush(q, (cost, pop_node))
    return distance[end]

def solved():
    v1, v2 = map(int, input().split())


    result = dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n)
    result2 = dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n)

    if result >= INF:
        print(-1)
    else:
        print(min(result, result2))
solved()