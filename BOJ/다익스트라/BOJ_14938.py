from heapq import heappush, heappop

n, m, r = map(int, input().split())
item_value = [0] + list(map(int, input().split()))
data = [[] for _ in range(n + 1)]
INF = int(1e9)
for _ in range(r):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))


def dijkstra(start):
    q = []
    distance = [INF for _ in range(n + 1)]
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, node = heappop(q)

        for i in data[node]:
            cost = dis + i[1]
            if cost < distance[i[0]] and cost <= m:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance


def solved():
    max_value = -INF
    for i in range(1, n + 1):
        sum_data = 0
        result = dijkstra(i)

        for j in range(1, n+1):
            if result[j] <= m:
                sum_data += item_value[j]


        max_value = max(max_value, sum_data)
    print(max_value)

solved()
