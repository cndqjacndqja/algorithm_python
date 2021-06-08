from heapq import heappush, heappop

n, m, x = map(int, input().split())
INF = int(1e9)
data = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((c, b))


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
    result = 0
    for i in range(1, n + 1):
        result = max(result, dijkstra(i, x) + dijkstra(x, i))
    print(result)


solved()
